---
name: "Meta Prompt - Workflow Generator"
description: "Apply when you need to create a custom workflow for a specific task or pattern that doesn't fit existing workflows. This meta-workflow helps you analyze requirements and generate a new, reusable workflow."
triggers: ["custom workflow", "new pattern", "workflow creation", "meta", "generate workflow", "unique task"]
---

# Meta Prompt - Workflow Generator

Apply when you need to create a custom workflow for a specific task or pattern that doesn't fit existing workflows. This meta-workflow helps you analyze requirements and generate a new, reusable workflow.

## Purpose

This workflow enables dynamic adaptation to unique development patterns by:
- Analyzing task requirements that don't fit existing workflows
- Creating structured, reusable workflows for new patterns
- Self-reviewing for quality and completeness
- Integrating new workflows into the handbook ecosystem

## Process

### 1. Task Analysis & Pattern Recognition

**Identify the unique aspects:**
- What makes this task different from existing workflows?
- What are the key steps that need to be followed?
- What are the common pitfalls or challenges?
- What technology-specific considerations apply?

**Define success criteria:**
- What constitutes successful completion?
- How can progress be measured?
- What deliverables are expected?

### 2. Workflow Structure Design

**Create the workflow outline:**
```markdown
# [Workflow Name]

## Overview
[Brief description of when and why to use this workflow]

## Prerequisites
[Any required knowledge, tools, or setup]

## Steps
1. [First major phase]
   - [Specific action]
   - [Verification step]

2. [Second major phase]
   - [Specific action]
   - [Decision point]

...

## Best Practices
- [Key principle]
- [Common pattern]

## Pitfalls to Avoid
- [Common mistake]
- [Anti-pattern]
```

### 3. Self-Review Process

**Review your draft workflow for:**
- **Clarity**: Can someone follow this without additional context?
- **Completeness**: Are all necessary steps included?
- **Practicality**: Is this actionable and specific?
- **Consistency**: Does it align with handbook philosophy?
- **Reusability**: Will this help with similar future tasks?

**Refine based on review:**
- Simplify complex steps
- Add missing verification points
- Remove redundant instructions
- Ensure alignment with existing patterns

### 4. Documentation & Integration

**Create the workflow file:**
```bash
# Save in the meta subdirectory:
# agent-guidance/workflows/meta/[descriptive-name].md
```

**Add proper metadata:**
```yaml
---
name: "[Descriptive Workflow Name]"
description: "Apply when [specific conditions/triggers]"
triggers: ["keyword1", "keyword2", "keyword3"]
---
```

**Update documentation:**
1. Add to file_structure.md
2. Create sketchbook entry documenting the new workflow
3. Test with the workflow discovery script:
   ```bash
   python scripts/list-workflows.py --query "relevant keyword"
   ```

### 5. Immediate Execution

After creating the workflow:
1. Save it in `agent-guidance/workflows/meta/[descriptive-name].md`
2. Follow the newly created workflow for the current task
3. Document any refinements discovered during execution

## Example Meta-Generated Workflows

Potential workflows that could be generated:
- `meta/database-migration-strategy.md` - For complex schema changes
- `meta/performance-optimization.md` - For systematic performance improvements
- `meta/legacy-code-refactor.md` - For modernizing old codebases
- `meta/api-versioning.md` - For implementing API version strategies
- `meta/debugging-production-issues.md` - For systematic production debugging

## Template for Meta-Generated Workflows

```markdown
---
name: "[Generated Workflow Name]"
description: "Apply when [specific scenario]. Generated on [date] for [original task]."
triggers: ["[analyzed keywords]"]
generated_by: "meta-prompt"
---

# [Workflow Title]

*This workflow was dynamically generated to address: [original requirement]*

## When to Use
[Specific conditions that trigger this workflow]

## Process
[Step-by-step instructions tailored to the pattern]

## Verification
[How to confirm successful completion]

## Notes
- Generated on: [date]
- Original context: [brief description]
- Refinements: [any updates made during execution]
```

## Benefits

- **Adaptability**: Create workflows for unique project needs
- **Knowledge Capture**: Document successful patterns for reuse
- **Continuous Improvement**: Handbook evolves with your project
- **Reduced Cognitive Load**: Future similar tasks have a guide
- **Team Scalability**: Others can follow your documented patterns 