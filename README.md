# Engineering Handbook

A comprehensive engineering handbook designed to improve AI coding agent performance through behavior-first guidance and structured workflows.

## Overview

This handbook provides AI coding agents with:

- **Behavior guidance** for consistent development practices
- **Workflow patterns** for different types of development tasks
- **Technology-specific context** for Django + SvelteKit projects
- **Reference documentation** for commands and implementation patterns
- **Tool integration** guides for various AI agents

## Directory Structure

```
engineering-handbook/
├── agent-guidance/           # Core AI agent behavior and workflows
│   ├── core-system.md       # Master behavior guidance
│   ├── workflows/           # Task-specific workflows
│   │   ├── feature-development.md
│   │   ├── frontend-styling.md
│   │   └── product-planning.md
│   ├── tech-context/        # Technology-specific behavior
│   │   ├── django-behavior.md
│   │   └── sveltekit-behavior.md
│   └── templates/           # Documentation templates
│       ├── project-sketchbook.md
│       └── session-tracking.md
├── reference/               # Detailed reference documentation
│   ├── architecture/       # Architecture guidelines and decisions
│   │   ├── guidelines.md
│   │   └── decision-records.md
│   ├── processes/          # Engineering processes and standards
│   │   └── pull-requests.md
│   ├── commands/           # Command references
│   │   ├── django-commands.md
│   │   ├── sveltekit-commands.md
│   │   └── docker-commands.md
│   └── patterns/           # Implementation patterns
│       ├── api-integration.md
│       └── project-structure.md
├── scripts/                 # Utility scripts
│   └── list-workflows.py    # Workflow discovery tool
├── CLAUDE.md              # Claude Code specific guidance
└── README.md              # This file
```

## Core Concepts

### Behavior-First Approach

The handbook prioritizes **agent behavior guidance** over comprehensive documentation. AI agents follow structured patterns and access detailed documentation only when needed, keeping context usage efficient.

### Workflow Selection

AI agents analyze tasks and select appropriate workflows:

- **Feature Development**: For implementing new functionality with structured planning
- **Frontend Styling**: For UI/UX work and design implementation  
- **Product Planning**: For high-level planning and roadmap creation

### Technology Context

Specialized guidance for the tech stack:

- **Django Backend**: Models, serializers, views, testing patterns
- **SvelteKit Frontend**: Components, API integration, state management

## Quick Start

### For AI Agents

1. **Discover workflows** using the metadata script:
   ```bash
   python scripts/list-workflows.py --query "your task description"
   ```
2. **Read core guidance**: `agent-guidance/core-system.md` for behavior patterns
3. **Select appropriate workflow** from `agent-guidance/workflows/`
4. **Apply technology context** from `agent-guidance/tech-context/`
5. **Reference detailed documentation** from `reference/` as needed
6. **Maintain documentation** using templates

### For Developers

1. **Set up project documentation**:
   ```bash
   # Create project sketchbook
   cp agent-guidance/templates/project-sketchbook.md ./sketchbook.md
   
   # Initialize file structure tracking
   git ls-files -c --others --exclude-standard > file_structure.md
   ```

2. **Configure your AI agent** to:
   - Use `CLAUDE.md` for Claude Code specific guidance
   - Reference `agent-guidance/core-system.md` as the main entry point
   - Follow workflows from `agent-guidance/workflows/`

## Key Features

### Consistent Development Patterns
- Standardized workflows for common development tasks
- Technology-specific best practices and patterns
- Structured approach to feature development and planning
- **Comprehensive API integration templates** with production-ready TanStack Query examples
- **Complete UI component patterns** with error handling, loading states, and accessibility
- Comprehensive pull request standards and review process
- Architecture guidelines with clear layer boundaries

### Efficient Context Usage
- Behavior guidance keeps context lean
- Detailed reference documentation accessed on-demand
- Smart workflow selection based on task analysis
- **Production-ready code templates** for immediate implementation

### Tool Agnostic
- Works with Claude Code, Cursor, GitHub Copilot, and other AI agents
- Standard markdown format for universal compatibility
- Core guidance in `agent-guidance/core-system.md` serves as main entry point

### Project Continuity
- Sketchbook template for tracking development sessions
- Decision documentation and reasoning
- File structure awareness and tracking

## Integration Examples

### Django + SvelteKit Full-Stack
- Type-safe API integration with OpenAPI
- TanStack Query for frontend data management
- Celery for background task processing
- Docker Compose for development environment

### Development Workflow
1. AI agent selects appropriate workflow
2. Applies technology-specific patterns
3. Documents decisions in project sketchbook
4. Maintains file structure awareness
5. References detailed commands/patterns as needed

## Contributing

When extending the handbook:

1. **Behavior changes** go in `agent-guidance/`
2. **Detailed documentation** goes in `reference/`
3. **Tool integrations** go in `tools/`
4. **Keep context efficient** - prioritize guidance over comprehensive docs
5. **Test with AI agents** to ensure patterns work effectively

## Benefits

- **Improved AI agent performance** through structured guidance
- **Consistent development practices** across projects and sessions
- **Reduced context overhead** with behavior-first approach
- **Technology-specific expertise** for Django + SvelteKit stack
- **Tool flexibility** supporting multiple AI coding agents
