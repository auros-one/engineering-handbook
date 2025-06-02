# Django Commands Reference

Essential Django commands extracted from existing project patterns and workflows.

## Development Setup

### Environment Setup
```bash
# Install dependencies
poetry install

# Activate virtual environment
poetry shell
# or
poetry env activate
```

### Database Operations
```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Reset database (with Docker)
docker compose down -v  # Clears volumes/data
docker compose up db -d
python manage.py migrate
```

### Custom Management Commands
```bash
# Setup development environment (creates superuser + test data)
python manage.py setup

# Alternative alias (if configured)
dj setup  # Shorthand for python manage.py
```

## Development Server

### Local Development
```bash
# Start Django development server
python manage.py runserver

# Alternative alias
dj runserver
```

### Docker Development
```bash
# Start only database (recommended)
docker compose up db -d

# Start all services
docker compose up

# Run in background
docker compose up -d

# Stop services
docker compose down
```

## Testing

### Running Tests
```bash
# Run all tests
pytest

# Run specific test file/folder
pytest project/path/or/folder/to/test

# Run tests for specific app
pytest project/app_name/tests/

# Run with coverage
pytest --cov=project

# Django's built-in test runner (alternative)
python manage.py test
```

## Database Management

### Superuser Management
```bash
# Create superuser interactively
python manage.py createsuperuser

# Create via custom command (if available)
python manage.py setup  # Often includes superuser creation
```

### Database Inspection
```bash
# Django shell
python manage.py shell

# Database shell
python manage.py dbshell
```

## API Documentation

### Django Spectacular (OpenAPI)
```bash
# Generate OpenAPI schema
python manage.py spectacular --color --file schema.yml

# Serve API docs (usually available at /api/docs/)
# Check project URLs for exact path
```

## Debugging and Utilities

### Django Admin
- Usually available at `/admin/`
- Requires superuser account
- Often integrated into project for convenience

### Development Aliases
Common project aliases (if configured):
```bash
# Instead of python manage.py
dj makemigrations
dj migrate
dj runserver
dj shell
```

## Environment Variables

### Required .env Setup
```bash
# Copy example environment file
cp .env.example .env

# Edit with appropriate values
# Common variables:
# - DATABASE_URL or database connection settings
# - SECRET_KEY
# - DEBUG=True (for development)
# - API keys (OpenAI, etc.)
```

## Performance and Monitoring

### Development Tools
- Django Debug Toolbar (if installed)
- Django Extensions (if installed)
- Profiling tools for query optimization

### Query Optimization
- Use `select_related()` for foreign keys
- Use `prefetch_related()` for many-to-many and reverse foreign keys  
- Monitor query counts in development
- Use Django Debug Toolbar for query analysis
- Check slow query logs in production

## Project-Specific Patterns

### BaseModel Usage
Many projects extend a custom BaseModel instead of Django's Model:

```python
# Common BaseModel pattern
from project.core.utils.models import BaseModel

class MyModel(BaseModel):  # Instead of models.Model
    # Automatically includes:
    # - UUID primary key
    # - created_at timestamp
    # - modified_at timestamp
    title = models.CharField(max_length=200)
```

### Management Command Creation

Create custom commands in `management/commands/` directory:

```python
# app/management/commands/setup.py
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Setup development environment'
    
    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com', 
                password='admin'
            )
            self.stdout.write('Created admin user')
        
        # Add test data creation logic
        self.stdout.write('Development setup complete')
```

## Troubleshooting

### Common Development Issues

**"No module named django" errors:**
```bash
# Check virtual environment
which python
poetry env info

# Reinstall if needed
poetry install
poetry shell
```

**Database connection issues:**
```bash
# Check database is running
docker compose ps db

# Test connection
python manage.py dbshell

# Check environment variables
echo $DATABASE_HOST
echo $DATABASE_PORT
```

**Migration issues:**
```bash
# Reset migrations (careful - loses data)
docker compose down -v
docker compose up db -d
python manage.py migrate

# Fix migration conflicts
python manage.py makemigrations --merge
```

### Useful Django Extensions Commands
```bash
# If django-extensions is installed:
python manage.py shell_plus      # Enhanced shell with auto-imports
python manage.py show_urls        # List all URL patterns
python manage.py validate_templates  # Check template syntax
python manage.py graph_models app_name  # Generate model diagrams
```