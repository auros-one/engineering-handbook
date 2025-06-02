# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an engineering handbook containing a structured rule system for Cursor AI and various project components. The repository serves as a central documentation hub for development workflows, AI behavior rules, and project management templates.

## Key Architecture

### Cursor Rules System
- **System Prompt** (.cursor/rules/system-prompt.mdc): Master rule file that guides all AI interactions and workflow selection
- **Workflow Rules** (.cursor/rules/workflows/): Task-specific rules for structured coding, frontend styling, and product roadmapping
- **Project Rules** (.cursor/rules/projects/): Technology-specific guidelines for Django backend and SvelteKit frontend implementations

### Documentation Templates
- **sketchbook.md**: Project journal template for tracking development history, decisions, and implementation patterns
- **file_structure.md**: Auto-generated file listing (updated after file operations)

## Core Commands

### File Structure Management
After any file system operations (create/rename/delete), update the file structure:
```bash
git ls-files -c --others --exclude-standard > file_structure.md
```

### Docker Services (for multi-component projects)
```bash
# Start only database (recommended for development)
docker compose up db -d

# Start all services
docker compose up

# Reset database (clears all data)
docker compose down -v
```

### Django Backend (when present)
```bash
# Install dependencies
poetry install

# Activate virtual environment
poetry shell

# Run migrations
python manage.py migrate

# Create superuser
python manage.py setup

# Start development server
python manage.py runserver
```

### Frontend Development (when present)
```bash
# Install dependencies
npm install --include=dev

# Start development server
npm run dev

# Type checking
npm run check
```

## Development Workflow

1. **Analyze requests** and select appropriate workflow from .cursor/rules/workflows/
2. **Document approach** in sketchbook.md following the template structure
3. **Apply technology-specific rules** based on project context
4. **Update file_structure.md** after file operations
5. **Maintain sketchbook entries** with implementation details and decisions

### Multi-Terminal Development Setup
For full-stack projects requiring coordinated service management:
```bash
# Terminal 1: Backend Database
docker compose up db -d

# Terminal 2: Backend Application  
cd backend/ && poetry shell && python manage.py runserver

# Terminal 3: Frontend Development
cd frontend/ && npm run dev

# Terminal 4: Background Services (optional)
cd backend/ && celery -A project worker -l info
```

Refer to agent-guidance/workflows/multi-project-development.md for comprehensive multi-service coordination patterns.

## Important Patterns

### API Integration (Full-stack projects)
- Backend generates OpenAPI schema via Django Spectacular
- Frontend uses typed API client (openapi-fetch) for type-safe requests
- TanStack Query handles caching and state management
- JWT authentication automatically added via middleware

### Asynchronous Task Processing
- Celery workers for background tasks
- Redis as message broker and queue
- Flower UI for monitoring tasks and workers
- Celery Beat for scheduled tasks

## Environment Setup

Create `.env` files from `.env.example` templates in both frontend and backend directories. Key variables:
- Database connection settings
- API keys (OpenAI, etc.)
- Service configuration

## Project Structure Awareness

The repository may contain multiple project components:
- Individual project folders (frontend/backend)
- Shared documentation and rules
- Media assets and artifacts
- Deprecated/legacy components

Always check project context before applying technology-specific rules or making assumptions about available tooling.