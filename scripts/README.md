# Scripts

Utility scripts for working with the engineering handbook.

## list-workflows.py

Extracts and displays workflow metadata to help AI agents select appropriate workflows based on task descriptions.

### Usage

```bash
# List all available workflows with full metadata
python scripts/list-workflows.py

# Simple list without detailed metadata
python scripts/list-workflows.py --simple

# Find workflows matching a task description
python scripts/list-workflows.py --query "implement new feature"
python scripts/list-workflows.py --query "styling UI design"
python scripts/list-workflows.py --query "product roadmap planning"
```

### Examples

**List all workflows:**
```bash
$ python scripts/list-workflows.py
# Available Workflows

## Frontend Styling (`frontend-styling.md`)
**Description:** Apply when working on user interface elements, visual design, styling, or UI/UX improvements
**Complexity:** medium | **Duration:** medium
**Triggers:** styling, UI, UX, design, visual, aesthetics, components, design system, branding
...
```

**Query specific workflow:**
```bash
$ python scripts/list-workflows.py --query "implement new feature"
# Workflow Selection for: 'implement new feature'

## Recommended Workflow

### 1. Feature Development (`feature-development.md`)
**Description:** Apply when implementing new features or complex functionality that spans across components or services
**Match Score:** 4 | **Complexity:** high | **Duration:** long
```

### Metadata Fields

Each workflow file contains minimal YAML frontmatter with:

- **name**: Human-readable workflow name
- **description**: When to apply this workflow (the "apply when" criteria)
- **triggers**: Keywords that indicate this workflow should be used

### Adding New Workflows

To add a new workflow that can be discovered by this script:

1. Create a new `.md` file in `agent-guidance/workflows/`
2. Add YAML frontmatter at the top:

```yaml
---
name: "Your Workflow Name"
description: "Apply when working on specific task type or context"
triggers: ["keyword1", "keyword2", "keyword3"]
---
```

3. Write your workflow content below the frontmatter
4. Test with `python scripts/list-workflows.py` to verify it's discovered