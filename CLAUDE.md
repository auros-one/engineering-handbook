# Job Funnel Project Guidelines

## Project Structure

This repository contains several sub-projects:
- Frontend (SvelteKit)
- Backend (Django)
- Browser automation extension
- Job scraping tools
- Auto-apply agent

## Development Guidelines

### Frontend Guidelines
- Use SvelteKit for frontend development
- Follow Tailwind CSS for styling
- Use TypeScript for all components
- Keep components small and reusable
- Prefer server-side rendering where possible

### Backend Guidelines
- Use Django for backend development
- Follow DRY principles and Django best practices
- Create comprehensive tests for all endpoints
- Document API endpoints using OpenAPI/Swagger
- Properly handle authentication and permissions

## Structured Workflows

When appropriate, follow these workflows:

### Feature Implementation Workflow
1. Understand the requirements thoroughly
2. Plan the implementation approach
3. Create or modify necessary files
4. Write tests for the functionality
5. Implement the feature
6. Verify all tests pass
7. Document the changes in sketchbook.md

### Bug Fix Workflow
1. Reproduce the issue first
2. Identify the root cause
3. Plan the fix
4. Implement the fix
5. Add tests to prevent regression
6. Verify the fix works
7. Document the bug and solution in sketchbook.md

### Refactoring Workflow
1. Identify the code to be refactored
2. Document current behavior to ensure it's preserved
3. Plan the refactoring approach
4. Make incremental changes 
5. Keep running tests to ensure functionality is preserved
6. Document the improvements in sketchbook.md

## File Tracking

After any file system operation (creating, renaming, or deleting files), run:
```bash
git ls-files -c --others --exclude-standard > file_structure.md
```

This command outputs all tracked and untracked (but not ignored) files to file_structure.md for easy reference.

## Sketchbook

Always keep track of important decisions, design patterns, and architectural choices in sketchbook.md. This file serves as a living document of the project's evolution.

## System Prompts

When working with coding agents, they should:
1. Decide which workflow is appropriate for the current task
2. Follow the chosen workflow systematically 
3. Keep track of changes and decisions in sketchbook.md
4. Update file_structure.md after filesystem changes
5. Always consider both frontend and backend implications of changes