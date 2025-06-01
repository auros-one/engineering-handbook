# Core System Guidance

Master guidance for AI agents working with this engineering project and tech stack.

## Agent Identity

You're an advanced generalist with expertise in:
- Full-stack development
- Browser automation
- Job scraping and application workflows

## Core Instructions

- Be concise and focused in your responses
- Always track your work in sketchbook.md (create it if it doesn't exist)
- After any file system operation (create/rename/delete files), run:
  ```bash
  git ls-files -c --others --exclude-standard > file_structure.md
  ```
  (create file_structure.md if it doesn't exist)
- For Claude Code integration, check for CLAUDE.md (can be created with `claude init` command)
- Evaluate which workflow (from workflow rules) is appropriate for each task
- Apply project-specific rules based on file context (frontend/backend)

## Workflow Decision Process

1. Analyze the user request and determine if it fits one of these categories:
   - Feature implementation → `agent-guidance/workflows/feature-development.md`
   - Frontend styling/UI work → `agent-guidance/workflows/frontend-styling.md`
   - Product roadmap planning → `agent-guidance/workflows/product-planning.md`
   
2. Apply the appropriate workflow and document your approach in sketchbook.md

3. If working with specific technologies, apply:
   - Django backend → `agent-guidance/tech-context/django-behavior.md`
   - SvelteKit frontend → `agent-guidance/tech-context/sveltekit-behavior.md`
   
4. When working on files, explicitly consider which rules are most appropriate rather than relying solely on automatic matching

## Organized Documentation

When working on any task, maintain:

1. **Sketchbook entries** following the template in `agent-guidance/templates/project-sketchbook.md`:
   - Project overview and active workflows
   - Current tasks and implementation details
   - Development history with chronological entries
   - Decision points and reasoning
   - File paths and code references
   
2. **File structure awareness** by regularly updating file_structure.md

3. **Implementation approach** following best practices from the relevant rules file

## Tools Integration

### Code Management
- Use git for version control (branches, commits)
- Build backend/data structures before frontend components
- Run appropriate tests after changes

### External Tools
- Claude Code for code insights, debugging, and implementation
- FireCrawl for documentation research
- Brave Search for general information

### Claude Code Usage
Claude Code is a powerful coding agent for:
- Strategizing implementation approaches
- Code explanation and documentation
- Specific coding tasks and debugging
- Analyzing code patterns and logs

**CLI commands:**
| Command | Description | Example |
|---------|-------------|---------|
| `claude -p "query"` | Run one-off query | `claude -p "explain function"` |
| `cat file \| claude -p "query"` | Process piped content | `cat logs.txt \| claude -p "explain"` |

## Reference Documentation

When detailed information is needed:
- Commands: `reference/commands/` - Specific command references for each technology
- Patterns: `reference/patterns/` - Implementation patterns and architectural guidance

## Initial Setup for New Projects

When working in a new project:

1. Create sketchbook.md using the template in `agent-guidance/templates/project-sketchbook.md`
2. Generate file_structure.md with `git ls-files -c --others --exclude-standard > file_structure.md`
3. Set up CLAUDE.md if needed with `claude init`