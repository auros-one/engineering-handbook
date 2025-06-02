# Docker Commands Reference

Essential Docker commands for development and service management.

## Service Management

### Starting Services
```bash
# Start only database (recommended for development)
docker compose up db -d

# Start all services defined in docker-compose.yml
docker compose up

# Start in background (detached mode)
docker compose up -d

# Start specific services
docker compose up web db redis -d
```

### Stopping Services
```bash
# Stop all services
docker compose down

# Stop and remove volumes (resets database)
docker compose down -v

# Stop specific service
docker compose stop db
```

### Service Status
```bash
# Show running containers
docker compose ps

# Show all containers (including stopped)
docker compose ps -a

# View service logs
docker compose logs
docker compose logs db
docker compose logs -f web  # Follow logs
```

## Development Workflow

### Database Reset
```bash
docker compose down -v
docker compose up db -d
sleep 1.5
python manage.py migrate
python manage.py setup_dev_env
```

### Service Restart
```bash
# Restart specific service
docker compose restart web

# Restart all services
docker compose restart
```

## Common Service Architecture

Based on the project structure, typical services include:

### Core Services
- **web**: Django backend application
- **db**: PostgreSQL database
- **redis**: Key-value store for task queues

### Background Processing
- **celeryworker**: Asynchronous task processing
- **celerybeat**: Scheduled task management
- **flower**: Celery monitoring UI

## Port Management

### Avoiding Port Conflicts
Projects typically map to different ports to avoid conflicts:
```bash
# Example mapping (check your docker-compose.yml)
# Database: 5432 (internal) -> 5433 (host)
# Web: 8000 (internal) -> 8000 (host)
# Redis: 6379 (internal) -> 6380 (host)
```

### Accessing Services
```bash
# Application typically available at:
http://localhost:8000

# Database connection from host:
# Host: localhost
# Port: 5433 (or mapped port)
# Database: project_db
```

## Debugging and Maintenance

### Container Inspection
```bash
# Execute command in running container
docker compose exec web bash
docker compose exec db psql -U postgres

# View container details
docker compose config

# Check resource usage
docker stats
```

### Volume Management
```bash
# List volumes
docker volume ls

# Remove unused volumes
docker volume prune

# Inspect specific volume
docker volume inspect project_db_data
```

### Image Management
```bash
# Rebuild services (after Dockerfile changes)
docker compose build

# Pull latest images
docker compose pull

# Remove unused images
docker image prune
```

## Environment Configuration

### Environment Files
```bash
# Copy example environment
cp .env.example .env

# Key environment variables for Docker:
# - Database connection settings
# - Service configuration
# - Port mappings
```

### Internal vs External Access
```bash
# Internal Docker network (between services):
DATABASE_HOST=db
REDIS_URL=redis://redis:6379

# External access (from host machine):
DATABASE_HOST=localhost
DATABASE_PORT=5433  # Mapped port
```

## Production Considerations

### Security
```bash
# Use specific image tags, not 'latest'
# Set appropriate environment variables
# Use secrets for sensitive data
# Configure proper networking
```

### Monitoring
```bash
# Health checks
docker compose exec web python manage.py check

# Service status
docker compose ps
docker compose logs --tail=50
```

## Troubleshooting

### Common Issues
```bash
# Port already in use
sudo lsof -i :5432  # Find process using port
docker compose down  # Stop all services

# Permission issues
docker compose down
docker volume prune  # Remove volumes if needed
docker compose up -d

# Network issues
docker network ls
docker network prune
```

### Fresh Start
```bash
# Complete reset (removes all data)
docker compose down -v
docker system prune -f
docker compose up -d
```