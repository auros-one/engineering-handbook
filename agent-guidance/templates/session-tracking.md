# Session Tracking Guidelines

Guidelines for maintaining project continuity and file structure awareness during development sessions.

## File Structure Tracking

### Automatic File Structure Updates

After any file system operation (create/rename/delete files), run:

```bash
git ls-files -c --others --exclude-standard > file_structure.md
```

**When to update:**
- Creating new files or directories
- Renaming or moving files
- Deleting files
- Reorganizing project structure

**Purpose:**
- Maintains awareness of project organization
- Helps AI agents understand current state
- Provides quick reference for file locations
- Tracks project evolution over time

### File Structure Content

The file_structure.md should contain:
- All tracked files in the repository
- Untracked files that are not in .gitignore
- Current project organization
- Recent structural changes

## Session Documentation

### Start of Session
1. Review existing sketchbook.md
2. Check current file_structure.md
3. Understand active workflows and pending tasks
4. Update Current Tasks section with session goals

### During Session
1. Document significant decisions and reasoning
2. Track files being modified
3. Note any architectural changes or patterns
4. Update file_structure.md after file operations

### End of Session
1. Complete Development History entry
2. Update Next Steps with remaining work
3. Note any new questions or blockers
4. Ensure file_structure.md is current

## Integration with Workflows

### Workflow Selection
- Document which workflow is being applied
- Reference specific workflow guidelines
- Track workflow completion status

### Progress Tracking
- Link sketchbook entries to specific workflow phases
- Document deviations from standard workflows
- Record lessons learned for future sessions

## Benefits

1. **Continuity**: AI agents can resume work effectively
2. **Context**: Clear understanding of project state
3. **History**: Preserved decision-making rationale
4. **Structure**: Always current view of project organization
5. **Collaboration**: Shared understanding between sessions