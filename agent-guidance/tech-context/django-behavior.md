# Django Backend Behavior Guidelines

Apply when working with the Django backend - includes step-by-step guidelines for models, views, serializers, URLs, and testing.

## Core Principles

This project uses Django for the backend and SvelteKit for the frontend. Always maintain consistency with existing project patterns and best practices.

## End-to-End Feature Implementation

**When creating an end-to-end feature, do the backend first:**

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
- Find existing serializers by grepping `model = ModelName` because we usually use `rest_framework.serializers.serializers.ModelSerializer` for serializers when possible
- Stick to `serializers.ModelSerializer` and other best practices

### 4. Create or Update Views

- Views are usually found in `project/app/views.py` file or folder
- Find views by grepping serializers or `queryset = ModelName.*` to find views
- **Performance considerations:**
  - Use `select_related`/`prefetch_related` for queries when writing queries, take performance into account
  - List endpoints should always have pagination
- **Documentation:**
  - If needed, use `@extend_schema` and/or `@extend_schema_view` to add API documentation (drf-spectacular)
  - We try to keep it simple
  - The drf-spectacular docs are used by openapi-fetch to generate the frontend types
- **Code quality:**
  - Ensure proper permission checks and business logic
  - Sparsely add comments to clear up code if needed (but keep it sparse, we don't want docstring spam)

### 5. Create or Update URLs

- View URLs are defined in the `urls.py` file of their app

### 6. Create or Update Admin (Optional)

- Only do this if it's useful/relevant/helpful

### 7. Create or Update Tests

- We follow KISS and don't require total coverage, but we do like to have tests for the most important parts of the code
- For example, the basic success case of a view should be tested so we're confident it works
- If there are any important edge cases we need certainty about, we should test those
- After creating/editing tests:
  - Run `pytest project/path/or/folder/to/test` to make sure they pass
  - Afterwards also run all tests with `pytest` to assure you didn't cause any regressions

## Consistency Guidelines

**Try to stay consistent with the project's style and best practices.** So if you write any of these files from scratch, first inspect existing files to see how those are written to make sure you stay consistent with the project.

**Example:** If you create a new `views.py` file and don't have other examples in your context yet, first inspect existing `views.py` files to see how those are written to ensure consistency with the project's approach.

Before writing any files from scratch:

1. **Inspect existing files** to understand project patterns
2. **Follow established conventions** for file structure and naming
3. **Match existing coding style** and architectural patterns

## After Backend Implementation

Once the backend is complete, proceed to the frontend:

1. **Sync the backend types** with the frontend types by running `npm run sync-types`
   - If you just updated the backend code, the dev server will automatically restart and probably need 5-10 seconds to be ready, so then you might want to sleep for 5 seconds
   - If you run `npm run sync-types` and get an error, wait for 5 seconds and try again. Probably the backend was just restarted
   - If issues persist, something might be wrong with the backend. Run `pytest` in the backend to check
   - If all tests pass but `sync-types` still fails, stop and ask for help

2. **Inspect existing frontend code** to see how it's organized, where the new scope/feature will fit in, and how the existing UI/UX is designed and styled

3. **Reason about the best way** to implement the scope or feature; code organization and UI/UX

4. **Create or update the frontend code**

5. **Run quality checks:**
   - Type checking with `npm run check`
   - Linting with `npm run lint`