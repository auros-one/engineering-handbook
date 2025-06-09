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

1. **Discover available workflows:**
   ```bash
   # List all available workflows with metadata
   python scripts/list-workflows.py
   
   # Find workflows matching your task
   python scripts/list-workflows.py --query "your task description"
   ```

2. **Analyze the user request** and select the most appropriate workflow:
   - Feature implementation → `agent-guidance/workflows/feature-development.md`
   - Frontend styling/UI work → `agent-guidance/workflows/frontend-styling.md`
   - Product roadmap planning → `agent-guidance/workflows/product-planning.md`
   
3. **Apply the selected workflow** and document your approach in sketchbook.md

4. **Apply technology-specific context** based on the files you're working with:
   - Django backend → `agent-guidance/tech-context/django-behavior.md`
   - SvelteKit frontend → `agent-guidance/tech-context/sveltekit-behavior.md`
   
5. **Consider workflow metadata** when selecting:
   - Check **triggers** for keyword matches with your task
   - Review **description** to ensure it fits your specific use case

## Decision Framework

### When to Access Reference Documentation
- **Access reference docs when**:
  - You need specific command syntax or flags
  - Implementing a pattern for the first time
  - User explicitly asks for detailed information
- **Skip reference docs when**:
  - Following a well-defined workflow
  - Pattern is already documented in behavior guides
  - Task is straightforward and covered by core guidance

### When to Generate Custom Workflows
- **Use meta-prompt workflow when**:
  - Task doesn't fit any existing workflow
  - Discovering a repeated pattern worth documenting
  - User requests a custom process for their specific needs
- **Stick to existing workflows when**:
  - Task clearly matches existing workflow triggers
  - Only minor adaptations needed

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

### Claude Code
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