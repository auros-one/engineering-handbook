# Architecture Decision Records (ADR)

## What is an ADR?

Architecture Decision Records document important architectural decisions made during development. They capture the context, decision, and consequences to help future developers understand why certain choices were made.

## When to Create an ADR

Create an ADR when:
- Making a significant architectural change
- Choosing between multiple technical approaches
- Establishing new patterns or conventions
- A reviewer comment during PR review spawns architectural discussion

## ADR Format

```markdown
# ADR-XXX: [Short Title]

## Status
[Proposed | Accepted | Deprecated | Superseded by ADR-YYY]

## Context
What is the issue that we're seeing that is motivating this decision or change?

## Decision
What is the change that we're proposing or have agreed to implement?

## Consequences
What becomes easier or more difficult to do and any risks introduced by this change?
```

## Current ADRs

### ADR-001: Business Logic in Service Layers

**Status**: Accepted

**Context**: 
Django's `save()` method and model methods can become complex business logic containers, making testing difficult and violating single responsibility principle.

**Decision**:
- `save()` persists objects to the database only
- Business logic is contained in service layers
- Models contain only data validation and simple computed properties

**Consequences**:
- ✅ Easier unit testing of business logic
- ✅ Clear separation of concerns
- ✅ Better reusability across different interfaces
- ❌ More files and classes to maintain
- ❌ Learning curve for Django developers used to fat models

### ADR-002: Data Integrity During Schema Changes

**Status**: Accepted

**Context**:
During the transition from `Eval` and `EvalRun` to `DocumentEval` and `DocumentEvalRun`, we need to preserve historical evaluation data while enabling safe rollbacks.

**Decision**:
For schema changes involving data migration, we explicitly include **both a forward** (`transfer_eval_data`) **and backward** (`reverse_transfer_eval_data`) **migration function**. This ensures a **non-destructive schema change**, allowing us to copy existing records to the new structure while preserving the ability to roll back if needed.

**Consequences**:
- ✅ **Safer deployments** - can roll back without data loss
- ✅ **Minimizes data loss risk** during migrations
- ✅ **Backward compatibility** for analytics, audit trails, and test reproducibility
- ✅ **Forward-backward symmetry** supports safer deployments
- ❌ More complex migration files
- ❌ Temporary data duplication during transition period

## Creating New ADRs

### From PR Review Process

When a reviewer comment is tagged with `adr:new`, follow these steps:

1. **Create new ADR file**: `reference/architecture/adr-XXX-short-title.md`
2. **Use the ADR format** above
3. **Reference the ADR** in your PR reply: `adr:new → ADR-XXX created`
4. **Add to this index** with a brief summary

### ADR Numbering

- Use sequential numbering: ADR-001, ADR-002, etc.
- Check existing ADRs to find the next available number
- Use descriptive short titles that indicate the decision area

### ADR Review Process

1. **Draft ADR** in separate PR or include in feature PR
2. **Team review** for architectural decisions
3. **Update status** from "Proposed" to "Accepted" after approval
4. **Reference in code** where the decision is implemented

## ADR Lifecycle

### Status Transitions

- **Proposed** → **Accepted**: Team approves the decision
- **Accepted** → **Deprecated**: No longer recommended but not forbidden
- **Accepted** → **Superseded**: Replaced by a newer ADR

### Updating ADRs

- **Never delete** accepted ADRs - they provide historical context
- **Mark as deprecated** when practices change
- **Create superseding ADR** for significant changes
- **Update consequences** if new information emerges

## Best Practices

### Writing ADRs

- **Be concise** but thorough in context
- **Include alternatives considered** and why they were rejected
- **List both positive and negative consequences**
- **Use simple, clear language**
- **Include code examples** when helpful

### Using ADRs

- **Reference ADRs in code comments** for non-obvious decisions
- **Link to ADRs in PR descriptions** when implementing related changes
- **Review relevant ADRs** before making architectural changes
- **Update ADR status** when decisions change

### ADR Review

- **Include architects/senior developers** in ADR reviews
- **Consider long-term implications** not just immediate needs
- **Evaluate alternatives thoroughly** before accepting
- **Ensure consequences are realistic** and comprehensive