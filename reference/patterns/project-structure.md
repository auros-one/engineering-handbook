# Project Structure Patterns

Common organizational patterns for Django + SvelteKit projects with supporting services.

## Full-Stack Project Layout

```
project-root/
├── backend/                    # Django application
│   ├── project/
│   │   ├── core/              # Core utilities and base models
│   │   │   └── utils/
│   │   │       └── models.py  # BaseModel definition
│   │   ├── apps/              # Individual Django apps
│   │   │   ├── vacancies/
│   │   │   │   ├── models.py
│   │   │   │   ├── serializers.py
│   │   │   │   ├── views.py
│   │   │   │   ├── urls.py
│   │   │   │   └── tests/
│   │   │   └── users/
│   │   ├── settings/
│   │   └── urls.py
│   ├── manage.py
│   ├── pyproject.toml         # Poetry configuration
│   ├── .env.example
│   └── Dockerfile
├── frontend/                   # SvelteKit application
│   ├── src/
│   │   ├── lib/
│   │   │   ├── api/           # API client and types
│   │   │   │   ├── index.ts   # API client setup
│   │   │   │   └── backend-api-schema.d.ts  # Generated types
│   │   │   ├── components/    # Reusable components
│   │   │   └── stores/        # State management
│   │   ├── routes/            # File-based routing
│   │   │   ├── +layout.svelte
│   │   │   ├── +page.svelte
│   │   │   └── jobs/
│   │   │       ├── +page.svelte
│   │   │       └── [id]/
│   │   │           └── +page.svelte
│   │   └── app.html
│   ├── package.json
│   ├── .env.example
│   └── Dockerfile
├── docker-compose.yml          # Service orchestration
├── .env.example               # Environment template
└── README.md
```

## Django App Organization

### Core Utilities Pattern

```python
# project/core/utils/models.py
import uuid
from django.db import models

class BaseModel(models.Model):
    """Base model with common fields for all entities"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]
        abstract = True
```

### App Structure Pattern

```python
# Typical Django app structure
app/
├── __init__.py
├── models.py              # Data models extending BaseModel
├── serializers.py         # DRF serializers for API
├── views.py              # API views and viewsets
├── urls.py               # URL routing for the app
├── admin.py              # Django admin configuration
├── tests/                # Test files
│   ├── __init__.py
│   ├── test_models.py
│   ├── test_views.py
│   └── test_serializers.py
└── management/           # Custom management commands
    └── commands/
        └── setup.py      # Custom setup command
```

### API Organization Pattern

```python
# views.py - Consistent API view structure
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema_view, extend_schema

@extend_schema_view(
    list=extend_schema(operation_id="listVacancies"),
    create=extend_schema(operation_id="createVacancy"),
    retrieve=extend_schema(operation_id="getVacancy"),
)
class VacancyViewSet(ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    
    @extend_schema(operation_id="searchVacancies")
    @action(detail=False, methods=['post'])
    def search(self, request):
        # Custom search endpoint
        pass
```

## SvelteKit Frontend Organization

### API Integration Structure

```typescript
// src/lib/api/index.ts
import createClient from 'openapi-fetch';
import type { paths } from './backend-api-schema';

export const apiClient = createClient<paths>({
    baseUrl: import.meta.env.VITE_API_URL || '/api'
});

// Add authentication middleware
apiClient.use({
    onRequest({ request }) {
        const token = getAuthToken();
        if (token) {
            request.headers.set('Authorization', `Bearer ${token}`);
        }
    }
});
```

### Component Organization

```typescript
// src/lib/components/ structure
components/
├── ui/                    # Basic UI components
│   ├── Button.svelte
│   ├── Input.svelte
│   └── Modal.svelte
├── forms/                 # Form-specific components
│   ├── JobSearchForm.svelte
│   └── VacancyForm.svelte
├── loading/               # Loading states
│   └── Spinner.svelte
└── vacancy/               # Domain-specific components
    ├── VacancyCard.svelte
    ├── VacancyList.svelte
    └── VacancyDetail.svelte
```

### Query Organization Pattern

```typescript
// src/lib/queries/vacancies.ts
import { createQuery, createMutation } from '@tanstack/svelte-query';
import { apiClient } from '$lib/api';
import type { components } from '$lib/api/backend-api-schema';

type Vacancy = components['schemas']['Vacancy'];

export const vacancyQueries = {
    list: (filters: SearchFilters) => createQuery({
        queryKey: ['vacancies', filters],
        queryFn: async () => {
            const { data, error } = await apiClient.GET('/api/vacancies/', {
                params: { query: filters }
            });
            if (error) throw new Error(error.detail);
            return data;
        }
    }),
    
    detail: (id: string) => createQuery({
        queryKey: ['vacancy', id],
        queryFn: async () => {
            const { data, error } = await apiClient.GET('/api/vacancies/{id}/', {
                params: { path: { id } }
            });
            if (error) throw new Error(error.detail);
            return data;
        },
        enabled: Boolean(id)
    })
};
```

## Docker Service Architecture

### Multi-Service Setup

```yaml
# docker-compose.yml pattern
version: '3.8'

services:
  web:                        # Django backend
    build: ./backend
    ports:
      - "8000:8000"
    depends_on:
      - db
      - redis
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/dbname
      - REDIS_URL=redis://redis:6379/0

  db:                         # PostgreSQL database
    image: postgres:15
    ports:
      - "5433:5432"          # Different port to avoid conflicts
    environment:
      - POSTGRES_DB=project_db
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:                      # Message broker for Celery
    image: redis:7-alpine
    ports:
      - "6380:6379"

  celeryworker:              # Background task processing
    build: ./backend
    command: celery -A project worker -l info
    depends_on:
      - db
      - redis
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/dbname
      - REDIS_URL=redis://redis:6379/0

  flower:                    # Celery monitoring
    build: ./backend
    command: celery -A project flower
    ports:
      - "5555:5555"
    depends_on:
      - redis

volumes:
  postgres_data:
```

## Environment Configuration Patterns

### Backend Environment

```bash
# backend/.env
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://postgres:postgres@localhost:5433/project_db
REDIS_URL=redis://localhost:6380/0
OPENAI_API_KEY=your-openai-key

# Production overrides
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
CORS_ALLOWED_ORIGINS=https://yourdomain.com
```

### Frontend Environment

```bash
# frontend/.env
VITE_API_URL=http://localhost:8000/api
VITE_WS_URL=ws://localhost:8000/ws
PUBLIC_SITE_URL=http://localhost:5173

# Production overrides
VITE_API_URL=https://api.yourdomain.com
VITE_WS_URL=wss://api.yourdomain.com/ws
PUBLIC_SITE_URL=https://yourdomain.com
```

## Development Workflow Patterns

### File Structure Tracking

```bash
# Maintain project structure awareness
git ls-files -c --others --exclude-standard > file_structure.md
```

### Cross-Service Development

1. **Backend changes** → Update models/serializers/views
2. **Database migration** → Apply schema changes
3. **API documentation** → Regenerate OpenAPI schema
4. **Frontend sync** → Update TypeScript types
5. **Integration testing** → Verify end-to-end functionality

### Port Management Strategy

```yaml
# Avoid port conflicts across projects
Project A:
  - Backend: 8000
  - Frontend: 5173
  - Database: 5433
  - Redis: 6380

Project B:
  - Backend: 8001
  - Frontend: 5174
  - Database: 5434
  - Redis: 6381
```

## Common Patterns and Conventions

### Naming Conventions

- **Django apps**: Snake_case (e.g., `job_applications`)
- **API endpoints**: Kebab-case (e.g., `/api/job-applications/`)
- **Frontend routes**: Kebab-case (e.g., `/job-applications`)
- **Component files**: PascalCase (e.g., `JobApplicationForm.svelte`)
- **Database tables**: Snake_case with app prefix

### Code Organization Principles

1. **Domain-driven structure**: Organize by business domain, not technical layer
2. **Consistency**: Follow established patterns within the project
3. **Separation of concerns**: Clear boundaries between frontend/backend/services
4. **Type safety**: Leverage TypeScript throughout the frontend
5. **API-first**: Design APIs that serve multiple clients (web, mobile, etc.)