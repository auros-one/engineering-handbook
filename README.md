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
│   ├── commands/           # Command references
│   │   ├── django-commands.md
│   │   ├── sveltekit-commands.md
│   │   └── docker-commands.md
│   └── patterns/           # Implementation patterns
│       ├── api-integration.md
│       └── project-structure.md
├── tools/                  # AI agent integration guides
│   ├── cursor-integration.md
│   └── general-ai-agents.md
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

1. Read `agent-guidance/core-system.md` for core behavior patterns
2. Select appropriate workflow from `agent-guidance/workflows/`
3. Apply technology-specific guidance from `agent-guidance/tech-context/`
4. Reference detailed documentation from `reference/` as needed
5. Maintain project documentation using templates

### For Developers

1. **Choose your AI agent integration**:
   - Claude Code: Use existing `CLAUDE.md` 
   - Cursor: Follow `tools/cursor-integration.md`
   - Other agents: See `tools/general-ai-agents.md`

2. **Set up project documentation**:
   ```bash
   # Create project sketchbook
   cp agent-guidance/templates/project-sketchbook.md ./sketchbook.md
   
   # Initialize file structure tracking
   git ls-files -c --others --exclude-standard > file_structure.md
   ```

3. **Configure your AI agent** to reference this handbook for all development tasks

## Key Features

### Consistent Development Patterns
- Standardized workflows for common development tasks
- Technology-specific best practices and patterns
- Structured approach to feature development and planning

### Efficient Context Usage
- Behavior guidance keeps context lean
- Detailed reference documentation accessed on-demand
- Smart workflow selection based on task analysis

### Tool Agnostic
- Works with Claude Code, Cursor, GitHub Copilot, and other AI agents
- Standard markdown format for universal compatibility
- Integration guides for popular development tools

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
