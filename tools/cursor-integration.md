# Cursor Integration Guide

How to integrate this engineering handbook with Cursor AI editor for optimal development workflow.

## Cursor Rules Setup

### .cursor/rules/ Directory Structure

To integrate with Cursor, create a `.cursor/rules/` directory in your project:

```
project-root/
├── .cursor/
│   └── rules/
│       ├── system-prompt.mdc      # Master rule referencing this handbook
│       ├── workflows/             # Workflow-specific rules (optional)
│       └── projects/              # Technology-specific rules (optional)
```

### Master System Prompt

Create `.cursor/rules/system-prompt.mdc`:

```markdown
---
description: Master system prompt that guides all AI interactions with this project
globs: ["**/*"]
alwaysApply: true
---

# Project System Prompt

You're an advanced generalist with expertise in Django, SvelteKit, and modern web development.

## Core Instructions

Reference the engineering handbook for detailed guidance:

### Agent Behavior
- Follow patterns in `engineering-handbook/agent-guidance/core-system.md`
- Select appropriate workflow from `engineering-handbook/agent-guidance/workflows/`
- Apply technology-specific context from `engineering-handbook/agent-guidance/tech-context/`

### Documentation Requirements
- Track work in sketchbook.md using template from `engineering-handbook/agent-guidance/templates/`
- Update file_structure.md after file operations:
  ```bash
  git ls-files -c --others --exclude-standard > file_structure.md
  ```

### Reference Documentation
When detailed information is needed, consult:
- Commands: `engineering-handbook/reference/commands/`
- Patterns: `engineering-handbook/reference/patterns/`

### Workflow Decision Process

1. Analyze request and select appropriate workflow:
   - Feature implementation → feature-development.md
   - Frontend styling → frontend-styling.md  
   - Product planning → product-planning.md

2. Apply technology-specific guidance:
   - Django backend → django-behavior.md
   - SvelteKit frontend → sveltekit-behavior.md

3. Document approach in sketchbook.md following the template

## Project Context

[Add specific project context here]
- Project name and description
- Key technologies and versions
- Important architectural decisions
- Current development phase
```

### Optional: Workflow-Specific Rules

Create workflow-specific rules if you want more granular control:

```markdown
---
description: Apply when implementing new features
globs: ["**/*.py", "**/*.ts", "**/*.svelte"]
alwaysApply: false
---

# Feature Development Rules

When implementing new features, follow the structured approach defined in:
`engineering-handbook/agent-guidance/workflows/feature-development.md`

Key principles:
1. Start with discussion, not code
2. Create structured PRD
3. Implement in phases
4. Continuous testing and validation

Refer to the full workflow documentation for detailed steps.
```

## Integration Benefits

### Automatic Behavior Guidance
- Cursor automatically applies rules based on file context
- Consistent behavior across all development sessions
- Access to comprehensive engineering knowledge

### Context-Aware Assistance
- Technology-specific guidance for Django and SvelteKit
- Workflow selection based on task type
- Reference to detailed commands and patterns when needed

### Documentation Automation
- Automatic sketchbook maintenance
- File structure tracking
- Decision recording and rationale

## Best Practices

### Rule Organization
1. **Keep system-prompt.mdc lean** - Reference handbook instead of duplicating content
2. **Use specific globs** - Target rules to relevant file types
3. **Set appropriate alwaysApply** - Only master rule should always apply

### Content Management
1. **Single source of truth** - Maintain detailed content in handbook
2. **Reference, don't duplicate** - Rules should point to handbook sections
3. **Update both** - When changing patterns, update both rules and handbook

### Project-Specific Customization
```markdown
# Add to system-prompt.mdc for project-specific context
## Project-Specific Guidelines

### Authentication
- JWT tokens with 24-hour expiry
- Refresh tokens stored in httpOnly cookies
- Authentication middleware in frontend API client

### Data Models
- All models extend BaseModel (UUID, created, modified)
- Use select_related/prefetch_related for performance
- Pagination required for all list endpoints

### Frontend Patterns
- TanStack Query for all API interactions
- Svelte 5 runes for state management
- Toast notifications for user feedback
```

## Migration from Existing Cursor Rules

If you have existing `.cursor/rules/`, you can migrate incrementally:

1. **Keep existing rules** that work well
2. **Reference handbook** for detailed guidance instead of duplicating
3. **Gradually consolidate** similar rules into handbook sections
4. **Update rules** to point to handbook locations

### Example Migration

```markdown
# Before (in .cursor/rules/django.mdc)
When creating Django models:
1. Extend BaseModel
2. Add proper field types
3. Create migrations
4. Add serializers
5. Create views
6. Add tests

# After (in .cursor/rules/django.mdc)
When working with Django backend, follow the detailed guidelines in:
`engineering-handbook/agent-guidance/tech-context/django-behavior.md`

For specific commands, reference:
`engineering-handbook/reference/commands/django-commands.md`
```

## Troubleshooting

### Rules Not Applied
- Check `.cursor/rules/` directory exists
- Verify glob patterns match your files
- Ensure proper YAML frontmatter format

### Conflicting Rules
- Review alwaysApply settings
- Check rule specificity and order
- Use more specific glob patterns

### Content Sync Issues
- Keep handbook as single source of truth
- Update rules when handbook changes
- Consider using git hooks to sync content

## Advanced Integration

### Dynamic Rule Generation
You can create scripts to generate Cursor rules from handbook content:

```bash
#!/bin/bash
# generate-cursor-rules.sh
# Generates .cursor/rules/ from engineering handbook

mkdir -p .cursor/rules

# Generate system prompt with handbook references
cat > .cursor/rules/system-prompt.mdc << EOF
---
description: System prompt referencing engineering handbook
globs: ["**/*"]
alwaysApply: true
---

$(cat engineering-handbook/agent-guidance/core-system.md | sed 's/^/# /')

For detailed guidance, see: engineering-handbook/
EOF
```

### CI/CD Integration
```yaml
# .github/workflows/sync-cursor-rules.yml
name: Sync Cursor Rules

on:
  push:
    paths:
      - 'engineering-handbook/**'

jobs:
  sync-rules:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Generate Cursor rules
        run: ./scripts/generate-cursor-rules.sh
      - name: Commit changes
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git add .cursor/rules/
          git commit -m "Update Cursor rules from handbook" || exit 0
          git push
```