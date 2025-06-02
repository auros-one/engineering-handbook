# Architecture Guidelines

## Purpose & Scope

This document defines **where each kind of logic belongs** in the project.

It is the single reference for code-reviews, new feature design, and onboarding.

## High-Level Components

| Component | Responsibility | Examples |
|-----------|---------------|----------|
| **Domain** | Core business entities and rules | User, Product, Order models with business validation |
| **Services** | Business workflows and orchestration | OrderProcessingService, UserRegistrationService |
| **Adapters** | External system integration | PaymentGateway, EmailService, DatabaseRepository |

## Ground Rules

### 1. Zero presentation logic in the backend
When you see `<br>`, CSS, i18n strings, pixels → it **does not belong** in `.models.py` (or any server-side layer except the API serializer).

### 2. Strict layer boundaries
- **Views** → **Services** → **Domain** → **Adapters**
- No skipping layers
- No reverse dependencies

### 3. Business rules live in Domain + Service layers
New rules are added there—not in views or adapters.

### 4. External dependencies are injected via adapters
Services receive interfaces; concrete implementations live in `infra/`.

### 5. Tests follow the same boundaries
- **Unit tests**: Domain & Services (no DB)
- **Integration tests**: Adapters & API  
- **End-to-end**: API ↔ Frontend where relevant

### 6. Naming conventions
Names should be concise, descriptive, and follow Django idioms.

**Examples:**
```python
# Good - Clear business intent
class OrderService:
    def process_payment(self, order: Order) -> PaymentResult:
        pass

# Bad - Generic naming
class OrderManager:
    def do_stuff(self, order: Order) -> dict:
        pass
```

**Model naming:**
```python
# Good - Business domain language
class SubscriptionPlan(models.Model):
    billing_interval = models.CharField(...)
    
# Bad - Technical jargon
class SubPlan(models.Model):
    interval_type = models.CharField(...)
```

### 7. ViewSet Action vs. Separate API View

**Use ViewSet actions when:**
- Operating on a single resource type
- Action is conceptually part of CRUD operations
- Keeps related endpoints grouped

```python
class DocumentViewSet(viewsets.ModelViewSet):
    @action(detail=True, methods=['post'])
    def regenerate(self, request, pk=None):
        # Operates on a specific document
        pass
```

**Use separate API views when:**
- Crossing multiple resource boundaries
- Complex workflows involving multiple models
- Standalone utility endpoints

```python
class DocumentComparisonView(APIView):
    def post(self, request):
        # Compares multiple documents - crosses boundaries
        pass
```

### 8. No adding/removing newlines without a reason
Maintain consistent formatting. Changes should have semantic purpose, not just style preferences.

### 9. Add clarification comments for non-obvious code or architectural changes

**Good examples:**
```python
# Using lazy evaluation to avoid N+1 queries
documents = Document.objects.select_related('project', 'author')

# Preserving original timestamp for audit trail
original_created_at = instance.created_at
```

**Avoid:**
```python
# Loop through documents
for doc in documents:
    pass
```

## Architecture Decision Records

See [Decision Records](./decision-records.md) for specific architectural decisions and their rationale.

## Code Quality Standards

### Type Safety
- Use type hints in Python (`typing` module)
- Use TypeScript strict mode in frontend
- Avoid `any` types unless absolutely necessary

### Error Handling
- Use specific exception types
- Handle errors at appropriate architectural boundaries
- Log errors with sufficient context for debugging

### Database Patterns
- Use select_related/prefetch_related to avoid N+1 queries
- Keep migrations backwards compatible
- Use database constraints to enforce business rules

### API Design
- Follow RESTful conventions
- Use appropriate HTTP status codes
- Provide clear error messages with actionable guidance