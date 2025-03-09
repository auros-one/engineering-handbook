# Cursor Rules System

This repository contains a structured rule system for Cursor AI to enhance coding assistant interactions and improve development workflow.

## Overview

Cursor Rules provide a flexible system for guiding AI behavior when working on development projects. This repository contains:

- Workflow rules for different development activities
- Technology-specific implementation guidelines
- Templates for project documentation
- File tracking mechanisms

## Directory Structure

```
cursor-rules/
├── .cursor/
│   └── rules/              # AI behavior rules
│       ├── projects/       # Technology-specific rules
│       │   ├── django-backend.mdc
│       │   └── sveltekit-frontend.mdc
│       ├── workflows/      # Task-specific workflows
│       │   ├── structured-coding.mdc
│       │   ├── frontend-style.mdc
│       │   └── product-roadmap.mdc
│       ├── system-prompt.mdc  # Master rules file
│       └── sketchbook.mdc      # Sketchbook template
├── CLAUDE.md              # Instructions for Claude Code CLI
├── file_structure.md      # Tracked file structure
└── sketchbook.md          # Project journal template
```

## Rule Types

### System Prompt (system-prompt.mdc)

The master rule that guides all AI interactions, directing workflow selection and documentation requirements.

### Workflow Rules

- **structured-coding.mdc**: For implementing new features with thorough planning and iterative development
- **frontend-style.mdc**: For UI/UX design and styling work
- **product-roadmap.mdc**: For planning features and product requirements

### Project Rules

- **django-backend.mdc**: Guidelines for Django backend implementation
- **sveltekit-frontend.mdc**: Guidelines for SvelteKit frontend implementation

## Template Files

### Sketchbook (sketchbook.md)

A template for maintaining project context and development history. AI agents use this to:

- Track active workflows
- Document development decisions
- Record implementation patterns
- Manage open questions

### File Structure (file_structure.md)

Automatically generated file showing project structure, updated after file operations.
