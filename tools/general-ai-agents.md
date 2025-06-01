# General AI Agents Integration

Guidelines for integrating this engineering handbook with various AI coding agents and tools.

## Supported AI Agents

This handbook is designed to work with any AI coding agent that can:
- Read markdown documentation
- Follow structured guidelines
- Access project files and context
- Execute commands and scripts

### Tested Agents
- **Claude Code** (claude.ai/code) - Primary integration via CLAUDE.md
- **Cursor AI** - Integration via .cursor/rules/ (see cursor-integration.md)
- **GitHub Copilot** - Via .github/copilot-instructions.md
- **Codeium** - Via inline documentation and comments
- **Any agent with file system access** - Direct handbook reference

## Universal Integration Pattern

### 1. Agent Context Setup

For any AI agent, provide this context at the start of a session:

```markdown
## Engineering Handbook Context

This project uses a comprehensive engineering handbook located at:
`engineering-handbook/`

### Core Guidance
- **Behavior rules**: `agent-guidance/core-system.md`
- **Workflows**: `agent-guidance/workflows/` (feature-development, frontend-styling, product-planning)
- **Tech context**: `agent-guidance/tech-context/` (django-behavior, sveltekit-behavior)
- **Templates**: `agent-guidance/templates/` (project-sketchbook, session-tracking)

### Reference Documentation
- **Commands**: `reference/commands/` (django, sveltekit, docker)
- **Patterns**: `reference/patterns/` (api-integration, project-structure)

### Instructions
1. Read `agent-guidance/core-system.md` for core behavior
2. Select appropriate workflow from `agent-guidance/workflows/`
3. Apply technology-specific guidance from `agent-guidance/tech-context/`
4. Reference detailed commands/patterns from `reference/` as needed
5. Maintain project documentation using templates from `agent-guidance/templates/`
```

### 2. Project-Specific Instructions

Add these instructions to your project's documentation:

```markdown
## AI Agent Instructions

### Before Starting Work
1. Read the engineering handbook: `engineering-handbook/agent-guidance/core-system.md`
2. Review current project state in `sketchbook.md`
3. Check `file_structure.md` for project organization

### During Development
1. Follow workflow guidelines from `agent-guidance/workflows/`
2. Apply technology-specific patterns from `agent-guidance/tech-context/`
3. Reference commands from `reference/commands/` when needed
4. Document decisions and progress in `sketchbook.md`

### After File Operations
Update file structure:
```bash
git ls-files -c --others --exclude-standard > file_structure.md
```

### Key Principles
- Behavior-first: Follow guidance patterns over raw documentation
- Context-efficient: Access detailed docs only when needed
- Documentation: Maintain sketchbook for session continuity
```

## Tool-Specific Integrations

### GitHub Copilot

Create `.github/copilot-instructions.md`:

```markdown
# GitHub Copilot Instructions

## Engineering Standards

This project follows patterns defined in the engineering handbook.

### Core Behavior
Before suggesting code, consider:
- Workflow context (feature development, styling, planning)
- Technology patterns (Django backend, SvelteKit frontend)
- Project conventions and existing patterns

### Code Suggestions
- Django: Extend BaseModel, use proper serializers, include tests
- SvelteKit: Use TanStack Query, follow type safety, implement proper error handling
- API Integration: Maintain type safety with OpenAPI-generated types

### Reference Locations
- Detailed patterns: `engineering-handbook/reference/patterns/`
- Command references: `engineering-handbook/reference/commands/`
- Behavior guidelines: `engineering-handbook/agent-guidance/`

For comprehensive guidance, agents should read the engineering handbook.
```

### VS Code Extensions

Create `.vscode/settings.json` with relevant extensions and settings:

```json
{
  "ai.handbook.path": "./engineering-handbook",
  "ai.context.include": [
    "engineering-handbook/agent-guidance/core-system.md",
    "sketchbook.md",
    "file_structure.md"
  ],
  "files.watcherExclude": {
    "**/.git/**": true,
    "**/node_modules/**": true,
    "**/.next/**": true
  }
}
```

### Custom AI Agent Integration

For custom or proprietary AI agents:

```python
# example_agent_integration.py
class EngineeringHandbookAgent:
    def __init__(self, handbook_path="./engineering-handbook"):
        self.handbook_path = handbook_path
        self.load_guidance()
    
    def load_guidance(self):
        """Load core guidance patterns from handbook"""
        core_path = f"{self.handbook_path}/agent-guidance/core-system.md"
        with open(core_path, 'r') as f:
            self.core_guidance = f.read()
    
    def select_workflow(self, task_description):
        """Select appropriate workflow based on task"""
        if "feature" in task_description.lower():
            return self.load_workflow("feature-development")
        elif "style" in task_description.lower() or "ui" in task_description.lower():
            return self.load_workflow("frontend-styling")
        elif "plan" in task_description.lower() or "roadmap" in task_description.lower():
            return self.load_workflow("product-planning")
        return None
    
    def get_tech_context(self, file_path):
        """Get technology-specific guidance based on file type"""
        if file_path.endswith('.py'):
            return self.load_tech_context("django-behavior")
        elif file_path.endswith(('.svelte', '.ts', '.js')):
            return self.load_tech_context("sveltekit-behavior")
        return None
```

## Integration Best Practices

### 1. Context Management

```markdown
## Agent Context Template

### Session Start
- Review engineering handbook core guidance
- Check current sketchbook.md for project state
- Understand active workflows and pending tasks

### During Work
- Follow selected workflow patterns
- Apply technology-specific guidance
- Reference detailed documentation as needed
- Document decisions and progress

### Session End
- Update sketchbook.md with progress
- Update file_structure.md if files changed
- Record next steps and open questions
```

### 2. Prompt Engineering

For better AI agent performance, use these prompt patterns:

```markdown
## Context-Rich Prompts

### Good Prompt
"Following the feature development workflow from the engineering handbook, 
implement user authentication for this Django + SvelteKit project. 
Reference the API integration patterns and maintain type safety."

### Better Prompt
"Using the engineering handbook:
1. Follow agent-guidance/workflows/feature-development.md
2. Apply django-behavior.md for backend implementation
3. Apply sveltekit-behavior.md for frontend integration
4. Reference api-integration.md patterns for type safety
5. Document approach in sketchbook.md

Implement user authentication with JWT tokens."
```

### 3. Error Recovery

When AI agents encounter issues:

```markdown
## Error Recovery Pattern

1. **Reference Check**: Verify agent is following handbook guidance
2. **Context Reset**: Re-read core-system.md and relevant workflow
3. **Pattern Lookup**: Check reference/patterns/ for similar implementations
4. **Command Reference**: Consult reference/commands/ for correct syntax
5. **Documentation**: Record issue and resolution in sketchbook.md
```

## Evaluation and Feedback

### Agent Performance Metrics

Track how well AI agents follow handbook guidance:

```markdown
## Performance Evaluation

### Positive Indicators
- Follows selected workflow patterns
- Applies technology-specific guidance
- Maintains documentation (sketchbook, file structure)
- References appropriate handbook sections
- Consistent code patterns with project conventions

### Areas for Improvement
- Skips workflow selection
- Ignores technology-specific patterns
- Poor documentation maintenance
- Inconsistent with established patterns
- Doesn't reference handbook when needed
```

### Continuous Improvement

```markdown
## Handbook Improvement Process

1. **Agent Feedback**: Record common agent mistakes or confusion
2. **Pattern Updates**: Update patterns based on real usage
3. **Guidance Refinement**: Improve behavior guidance clarity
4. **Integration Testing**: Test with multiple AI agents
5. **Documentation Enhancement**: Add examples and clarifications
```

## Advanced Integration Features

### Dynamic Context Loading

```typescript
// dynamic-context-loader.ts
export class HandbookContextLoader {
    async loadContextForTask(taskType: string, fileContext: string[]) {
        const coreGuidance = await this.loadFile('agent-guidance/core-system.md');
        const workflow = await this.selectWorkflow(taskType);
        const techContext = await this.getTechContext(fileContext);
        
        return {
            core: coreGuidance,
            workflow,
            techContext,
            references: await this.getRelevantReferences(taskType)
        };
    }
}
```

### Automated Handbook Sync

```bash
#!/bin/bash
# sync-handbook-context.sh
# Keeps AI agent context synchronized with handbook updates

HANDBOOK_DIR="./engineering-handbook"
AGENT_CONTEXT_FILE="./.ai-context.md"

# Generate fresh context from handbook
cat > "$AGENT_CONTEXT_FILE" << EOF
# AI Agent Context (Auto-generated)
Generated: $(date)

## Core Guidance
$(cat "$HANDBOOK_DIR/agent-guidance/core-system.md")

## Available Workflows
$(find "$HANDBOOK_DIR/agent-guidance/workflows" -name "*.md" -exec basename {} .md \;)

## Technology Contexts  
$(find "$HANDBOOK_DIR/agent-guidance/tech-context" -name "*.md" -exec basename {} .md \;)

EOF

echo "AI agent context updated: $AGENT_CONTEXT_FILE"
```

This integration approach ensures that any AI coding agent can effectively use the engineering handbook to provide consistent, high-quality assistance following your established patterns and workflows.