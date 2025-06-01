# API Integration Patterns

Implementation patterns for connecting Django backend with SvelteKit frontend using type-safe APIs.

## Architecture Overview

The project uses a type-safe API integration pattern:

1. **Django + DRF Spectacular** generates OpenAPI schema
2. **openapi-fetch** creates TypeScript client from schema
3. **TanStack Query** handles caching and state management
4. **Automatic authentication** via middleware

## Backend API Patterns

### Model → Serializer → View → URL Flow

```python
# 1. Model (extending BaseModel)
from project.core.utils.models import BaseModel

class Vacancy(BaseModel):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    # ... other fields

# 2. Serializer
from rest_framework import serializers

class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = '__all__'

# 3. ViewSet with proper documentation
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.viewsets import ModelViewSet

@extend_schema_view(
    list=extend_schema(
        operation_id="listVacancies",
        summary="List all vacancies",
        description="Retrieve paginated list of job vacancies"
    )
)
class VacancyViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    
    # Performance optimization
    def get_queryset(self):
        return super().get_queryset().select_related('company')

# 4. URL configuration
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'vacancies', VacancyViewSet)
urlpatterns = router.urls
```

### API Documentation Best Practices

```python
# Use operation_id for consistent frontend naming
@extend_schema(
    operation_id="searchJobs",  # Becomes searchJobs in frontend
    parameters=[
        OpenApiParameter(
            name="skills",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Comma-separated skills filter"
        )
    ]
)
def search_jobs(request):
    # Implementation
    pass
```

## Frontend Integration Patterns

### Type-Safe API Client

```typescript
// Generated types from backend schema
import type { components, paths } from '$lib/api/backend-api-schema';

// Type definitions
type Vacancy = components['schemas']['Vacancy'];
type VacancyList = components['schemas']['PaginatedVacancyList'];

// API operations
type SearchJobsParams = paths['/api/jobs/search/']['post']['requestBody']['content']['application/json'];
type SearchJobsResponse = paths['/api/jobs/search/']['post']['responses']['200']['content']['application/json'];
```

### Query Pattern with TanStack Query

```typescript
import { createQuery } from '@tanstack/svelte-query';
import { apiClient } from '$lib/api';

// List query with pagination
const vacanciesQuery = createQuery<VacancyList>({
    queryKey: ['vacancies', page, filters],
    queryFn: async () => {
        const { data, error } = await apiClient.GET('/api/vacancies/', {
            params: {
                query: {
                    page,
                    page_size: 20,
                    skills: filters.skills?.join(',')
                }
            }
        });

        if (error) throw new Error(error.detail || 'Failed to fetch');
        return data;
    },
    staleTime: 5 * 60 * 1000, // 5 minutes
});

// Detail query with caching
const vacancyQuery = createQuery<Vacancy>({
    queryKey: ['vacancy', id],
    queryFn: async () => {
        const { data, error } = await apiClient.GET('/api/vacancies/{id}/', {
            params: { path: { id } }
        });

        if (error) throw new Error(error.detail || 'Not found');
        return data;
    },
    enabled: Boolean(id),
});
```

### Mutation Pattern with Optimistic Updates

```typescript
import { createMutation, useQueryClient } from '@tanstack/svelte-query';
import toast from 'svelte-french-toast';

const createVacancyMutation = createMutation({
    mutationFn: async (vacancyData: Partial<Vacancy>) => {
        const { data, error } = await apiClient.POST('/api/vacancies/', {
            body: vacancyData
        });

        if (error) {
            toast.error(error.detail || 'Failed to create vacancy');
            throw new Error(error.detail);
        }
        return data;
    },

    // Optimistic update
    onMutate: async (newVacancy) => {
        await queryClient.cancelQueries({ queryKey: ['vacancies'] });
        
        const previousVacancies = queryClient.getQueryData(['vacancies']);
        
        queryClient.setQueryData(['vacancies'], (old: VacancyList) => ({
            ...old,
            results: [{ ...newVacancy, id: 'temp-id' }, ...old.results]
        }));

        return { previousVacancies };
    },

    onError: (err, variables, context) => {
        if (context?.previousVacancies) {
            queryClient.setQueryData(['vacancies'], context.previousVacancies);
        }
    },

    onSuccess: (data) => {
        toast.success('Vacancy created successfully');
        queryClient.invalidateQueries({ queryKey: ['vacancies'] });
    }
});
```

## Authentication Integration

### Automatic JWT Token Handling

```typescript
// API client with authentication middleware
import createClient from 'openapi-fetch';

export const apiClient = createClient<paths>({ 
    baseUrl: '/api' 
});

// Add authentication token to all requests
apiClient.use({
    onRequest({ request }) {
        const token = getAuthToken(); // From your auth store
        if (token) {
            request.headers.set('Authorization', `Bearer ${token}`);
        }
    },
    
    onResponse({ response }) {
        // Handle 401 responses globally
        if (response.status === 401) {
            // Redirect to login or refresh token
            handleAuthError();
        }
    }
});
```

### Protected vs Unprotected Routes

```typescript
// Explicitly mark unprotected endpoints
const publicApiClient = createClient<paths>({ baseUrl: '/api' });

// For authentication endpoints
await publicApiClient.POST('/auth/login/', {
    body: { username, password }
});

// Protected endpoints use main client with auth
await apiClient.GET('/api/user/profile/');
```

## Performance Optimization

### Query Optimization

```python
# Backend: Optimize database queries
class VacancyViewSet(ModelViewSet):
    def get_queryset(self):
        return Vacancy.objects.select_related(
            'company', 'location'
        ).prefetch_related(
            'skills', 'requirements'
        )
```

### Frontend Caching Strategy

```typescript
// Smart caching with TanStack Query
const vacancyQueries = {
    // List with short cache time
    list: (filters: FilterParams) => ({
        queryKey: ['vacancies', 'list', filters],
        queryFn: () => fetchVacancies(filters),
        staleTime: 2 * 60 * 1000, // 2 minutes
    }),
    
    // Detail with longer cache time
    detail: (id: string) => ({
        queryKey: ['vacancies', 'detail', id],
        queryFn: () => fetchVacancy(id),
        staleTime: 10 * 60 * 1000, // 10 minutes
    }),
};
```

## Error Handling Patterns

### Consistent Error Structure

```python
# Backend: Standardized error responses
from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    
    if response is not None:
        custom_response_data = {
            'error': response.data,
            'status_code': response.status_code,
            'message': get_error_message(exc)
        }
        response.data = custom_response_data
    
    return response
```

```typescript
// Frontend: Centralized error handling
const handleApiError = (error: any) => {
    if (error.status === 400) {
        // Validation errors
        showValidationErrors(error.error);
    } else if (error.status === 403) {
        // Permission denied
        toast.error('You don\'t have permission for this action');
    } else if (error.status >= 500) {
        // Server errors
        toast.error('Server error. Please try again later.');
    } else {
        // Generic error
        toast.error(error.message || 'An unexpected error occurred');
    }
};
```

## Development Workflow

### Type Synchronization Process

1. **Backend changes** → Update models/serializers/views
2. **Generate schema** → DRF Spectacular creates OpenAPI spec
3. **Sync types** → `npm run sync-types` updates frontend types
4. **Type checking** → `npm run check` validates integration
5. **Testing** → Verify both backend and frontend functionality

### Common Integration Issues

```typescript
// Handle timing issues with type sync
if (syncTypesError) {
    // Wait for backend restart
    await new Promise(resolve => setTimeout(resolve, 5000));
    // Retry sync-types
    await syncTypes();
}
```