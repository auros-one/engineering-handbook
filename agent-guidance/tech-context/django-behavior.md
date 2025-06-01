# Django Backend Behavior Guidelines

Apply when working with the Django backend - includes step-by-step guidelines for models, views, serializers, URLs, and testing.

## Core Principles

This project uses Django for the backend and SvelteKit for the frontend. Always maintain consistency with existing project patterns and best practices.

## End-to-End Feature Implementation

### 1. Create or Update Models

- Models are usually found in `project/app/models.py` file or folder
- Always extend from BaseModel for consistency:

```python
"""
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created"]
        abstract = True
"""
from project.core.utils.models import BaseModel

class ModelName(BaseModel):
    pass
```

### 2. Create and Run Migrations

- Run `python manage.py makemigrations`
- Run `python manage.py migrate`

### 3. Create or Update Serializers

- Model serializers are usually found in `project/app/serializers` file or folder
- Find existing serializers by grepping `model = ModelName`
- Stick to `serializers.ModelSerializer` and other best practices

### 4. Create or Update Views

- Views are usually found in `project/app/views.py` file or folder
- Find views by grepping serializers or `queryset = ModelName.*`
- **Performance considerations:**
  - Use `select_related`/`prefetch_related` for queries
  - List endpoints should always have pagination
- **Documentation:**
  - Use `@extend_schema` and/or `@extend_schema_view` for API documentation (drf-spectacular)
  - Keep documentation simple - used by openapi-fetch to generate frontend types
- **Code quality:**
  - Ensure proper permission checks and business logic
  - Add sparse comments only when needed for clarity
  - Avoid docstring spam

### 5. Create or Update URLs

- View URLs are defined in the `urls.py` file of their app

### 6. Create or Update Admin (Optional)

- Only implement if useful/relevant/helpful for the feature

### 7. Create or Update Tests

- Follow KISS principle - don't require total coverage
- Test important parts of the code:
  - Basic success case of views
  - Important edge cases that need certainty
- After creating/editing tests:
  - Run `pytest project/path/or/folder/to/test` for specific tests
  - Run `pytest` for all tests to check for regressions

### 8. Sync OpenAPI Schema

- After updating views, sync the OpenAPI schema
- Command: TODO: fill out command here once this is set up in a proper monorepo

## Consistency Guidelines

Before writing any files from scratch:

1. **Inspect existing files** to understand project patterns
2. **Follow established conventions** for file structure and naming
3. **Match existing coding style** and architectural patterns

**Example:** If creating a new `views.py` file, first inspect existing `views.py` files to ensure consistency with the project's approach.