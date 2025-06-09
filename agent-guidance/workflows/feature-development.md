---
name: "Feature Development"
description: "Apply when implementing new features or complex functionality that spans across components or services. Ideal for features requiring careful planning, multi-step execution, or integration of multiple system parts."
triggers: ["feature", "implementation", "new functionality", "complex", "multi-step", "integration"]
---

# Feature Development Workflow

Apply when implementing new features or complex functionality that spans across components or services. Ideal for features requiring careful planning, multi-step execution, or integration of multiple system parts.

This workflow focuses on thorough requirement analysis, documentation, step-by-step implementation, and verification to ensure robust, maintainable code.

## 1. Problem Definition & Requirement Analysis

### Start with Discussion, Not Code
- Don't generate code immediately
- Engage the user in a conversation to explore and refine feature requirements
- Document key constraints and acceptance criteria

### Detailed Feature Description
- Ask the user to provide as much contextual information as possible
- Request references to relevant files, objects, and existing implementations
- Clarify integration points and dependencies

### Clarification Process
- Ask follow-up questions to understand the requirements fully
- Address ambiguities before proceeding to implementation
- Define clear boundaries for the scope with the user

## 2. Documentation & Planning

### Generate a Structured PRD (Product Requirements Document)
- Create a standardized template for consistency
- Include acceptance criteria for each requirement
- Document technical constraints and dependencies

### Design Documentation
- Break down implementation into clear, logical phases
- Define interfaces between components
- Present the architecture plan to the user for approval

### Comprehensive Context Provision
- Request access to relevant external documentation
- Ask for any necessary technical information not yet provided

## 3. Phased Implementation Strategy

### Step-by-Step Execution
- Implement the solution in planned, manageable phases
- Reference the design document consistently during implementation
- Focus on small, verifiable steps rather than broad changes

### Iterative Refinement
- Engage in dialogue with the user throughout implementation
- Make incremental adjustments based on feedback
- Don't attempt to achieve perfection in a single iteration

### Dynamic Project Updates
- Update project plans after each significant change
- Maintain an up-to-date roadmap reflecting current development state
- Document progress and changes in a structured format

## 4. Verification & Testing

### Continuous Testing
- Follow a testing strategy for each implementation phase
- Combine automated tests with manual validation suggestions
- Regularly validate against original requirements
- Ensure backward compatibility

## Key Principles for Success

### Small, Verifiable Steps
- Instead of: Attempting to "Add error handling to the entire codebase"
- Better: "Let me identify critical paths needing error handling in the authentication module first"

### Clear Context Boundaries
- Instead of: Accepting vague requests like "Make this code better"
- Better: Ask for specifics: "Which aspects would you like me to improve? Performance, readability, error handling, or specific edge cases?"

### Shared Understanding
- Regularly confirm alignment between the user's vision and your interpretation
- Summarize understanding before implementing major changes

### Structured Documentation
- Keep documentation updated throughout development
- Use consistent formats for requirements, plans, and technical specifications

## Common Pitfalls to Avoid

- Starting implementation without clear planning
- Accepting vague or ambiguous requirements without clarification
- Assuming project context without requesting sufficient information
- Attempting to implement too much in a single step
- Neglecting to update project documentation as development progresses

## Benefits of This Approach

- Prevents project abandonment due to increasing complexity
- Improves code quality through systematic planning and verification
- Enhances collaboration efficiency with the user
- Promotes successful project completion with structured guidance
- Creates maintainable code with comprehensive documentation

By following this structured approach, you can become an effective pair programming partner, enhancing productivity and code quality.

## Related Resources

### Workflows
- [`pull-requests.md`](./pull-requests.md) - For the PR submission phase
- [`meta-prompt.md`](./meta-prompt.md) - If you need a custom workflow for unique features

### Technology Context
- [`django-behavior.md`](../tech-context/django-behavior.md) - For Django backend features
- [`sveltekit-behavior.md`](../tech-context/sveltekit-behavior.md) - For SvelteKit frontend features

### Reference Documentation
- [`api-integration.md`](../../reference/patterns/api-integration.md) - For features involving API design
- [`architecture/guidelines.md`](../../reference/architecture/guidelines.md) - For architectural decisions