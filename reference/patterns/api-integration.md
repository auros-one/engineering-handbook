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

### Complete Query Implementation Template

**Full-featured query with comprehensive error handling and UI states:**

```svelte
<script lang="ts">
    import type { components } from '$lib/api/backend-api-schema';
    import { createQuery, useQueryClient } from '@tanstack/svelte-query';
    import { apiClient } from '$lib/api';
    import Spinner from '$lib/components/loading/Spinner.svelte';

    // 1. Type Definition (if needed)
    type ResponseType = components['schemas']['YourSchemaType'];  // Use backend schema types
    // eg: type UserDetails = components['schemas']['UserDetails'];
    // eg: type PaginatedUserListList = components['schemas']['PaginatedUserListList'];
    type ErrorType = Error;  // Optional, defaults to unknown

    // 2. Query Client (if needed for cache invalidation)
    const queryClient = useQueryClient();

    // 3. Create Query Implementation
    const query = createQuery<ResponseType, ErrorType>({
        queryKey: ['uniqueKey', optionalId],
        queryFn: async () => {
            const { data, error } = await apiClient.GET('/your/endpoint/', {
                params: {
                    path: {
                        id: optionalId
                    },
                    query: {
                        page: pageNumber,
                    }
                }
            });

            if (error) throw new Error(error);
            if (!data) throw new Error('No data returned');

            return data;
        },
        staleTime: 5 * 60 * 1000,
        cacheTime: 10 * 60 * 1000,
        enabled: Boolean(optionalId),
        retry: 3,
    });

    // 4. Using the Query Results
    $: data = $query.data;
    $: isLoading = $query.isPending;
    $: error = $query.error;

    // 5. Cache Invalidation (if needed)
    async function invalidateCache() {
        await queryClient.invalidateQueries({ queryKey: ['uniqueKey'] });
    }
</script>

<div class="relative flex flex-col">
    <!-- Loading State -->
    {#if $query.isPending}
        <div class="flex h-[60vh] w-full items-center justify-center">
            <Spinner />
        </div>
    <!-- Error State -->
    {:else if $query.error}
        <div class="flex flex-col items-center justify-center gap-4 rounded-lg bg-red-50 p-6 text-red-700">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
            </svg>
            <p class="text-lg font-semibold">An error occurred: {$query.error.message}</p>
        </div>
    <!-- Success State -->
    {:else if $query.isSuccess}
        <div class="space-y-6">
            <!-- Example of data display -->
            {#if $query.data}
                <div class="rounded-lg bg-white p-6 shadow-sm">
                    <!-- Your data display here -->
                    <pre class="whitespace-pre-wrap text-sm text-gray-700">
                        {JSON.stringify($query.data, null, 2)}
                    </pre>
                </div>

                <!-- Example of refresh button -->
                <button
                    on:click={invalidateCache}
                    class="inline-flex items-center gap-2 rounded-md bg-primary-600 px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2"
                >
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                    </svg>
                    Refresh Data
                </button>
            {/if}
        </div>
    {/if}
</div>
```

### Complete Mutation Implementation Template

**Full-featured mutation with optimistic updates and comprehensive error handling:**

```svelte
<script lang="ts">
    import type { components } from '$lib/api/backend-api-schema';
    import { createMutation, useQueryClient } from '@tanstack/svelte-query';
    import { apiClient } from '$lib/api';
    import toast from 'svelte-french-toast';
    import Spinner from '$lib/components/loading/Spinner.svelte';

    // 1. Type Definitions
    type MutationRequest = {
        id: string;
        data: any;  // Replace with your specific type
    };
    type MutationResponse = components['schemas']['YourResponseType'];

    // 2. Query Client for cache updates
    const queryClient = useQueryClient();

    // 3. Create Mutation Implementation
    const mutation = createMutation({
        // Required: The mutation function
        mutationFn: async ({ id, data }: MutationRequest) => {
            const { data: responseData, error } = await apiClient.POST('/your/endpoint/{id}/', {
                params: {
                    path: {
                        id: id
                    }
                },
                body: data
            });

            if (error) {
                // Use toast for error feedback
                toast.error(error.error || 'An error occurred');
                throw new Error(error.error || 'An error occurred');
            }

            return responseData;
        },

        // Optional: Before mutation starts
        onMutate: async (variables) => {
            // Cancel any outgoing refetches
            await queryClient.cancelQueries({ queryKey: ['yourQueryKey'] });

            // Snapshot the previous value
            const previousData = queryClient.getQueryData(['yourQueryKey']);

            // Optimistically update the cache
            queryClient.setQueryData(['yourQueryKey'], (old: any) => ({
                ...old,
                // Your optimistic update
            }));

            // Return context with the snapshotted value
            return { previousData };
        },

        // Optional: On successful mutation
        onSuccess: async (data, variables) => {
            // Show success message
            toast.success('Operation successful!');

            // Invalidate and refetch relevant queries
            await queryClient.invalidateQueries({ queryKey: ['yourQueryKey'] });
        },

        // Optional: On mutation error
        onError: (error, variables, context) => {
            // Show error message
            toast.error('Operation failed');

            // Rollback to the previous value if available
            if (context?.previousData) {
                queryClient.setQueryData(['yourQueryKey'], context.previousData);
            }
        },

        // Optional: Run after either success or error
        onSettled: () => {
            // Clean up or final tasks
        }
    });

    // 4. Function to trigger the mutation
    async function handleMutation() {
        try {
            await $mutation.mutateAsync({
                id: 'your-id',
                data: { /* your data */ }
            });
        } catch (error) {
            console.error('Mutation error:', error);
        }
    }
</script>

<!-- 5. Usage in Template -->
<div class="space-y-4">
    <!-- Example of a form/button triggering the mutation -->
    <button
        on:click={handleMutation}
        disabled={$mutation.isPending}
        class="inline-flex items-center gap-2 rounded-md bg-primary-600 px-4 py-2 font-semibold text-white shadow-sm transition-colors duration-200 hover:bg-primary-700 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2"
    >
        {#if $mutation.isPending}
            <Spinner color="white" size={18} ringThickness={1.5} />
            Processing...
        {:else}
            Submit
        {/if}
    </button>

    <!-- Loading State -->
    {#if $mutation.isPending}
        <div class="flex items-center gap-2 text-gray-600">
            <Spinner />
            <span>Processing your request...</span>
        </div>
    {/if}

    <!-- Error State -->
    {#if $mutation.isError}
        <div class="rounded-md bg-red-50 p-4 text-red-700">
            <p>Error: {$mutation.error.message}</p>
        </div>
    {/if}

    <!-- Success State -->
    {#if $mutation.isSuccess}
        <div class="rounded-md bg-green-50 p-4 text-green-700">
            <p>Operation completed successfully!</p>
        </div>
    {/if}
</div>
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

### Enhanced Type Sync Troubleshooting

```bash
# If you just updated the backend code, wait for dev server restart
sleep 5

# Run type sync
npm run sync-types

# If sync-types fails, wait and retry
if [ $? -ne 0 ]; then
    echo "Type sync failed, waiting 5 seconds and retrying..."
    sleep 5
    npm run sync-types
fi

# If issues persist, check backend health
if [ $? -ne 0 ]; then
    echo "Type sync still failing, checking backend..."
    pytest
    echo "If tests pass but sync-types fails, stop and ask for help"
fi
```

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