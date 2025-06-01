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