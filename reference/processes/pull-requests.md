# Pull Request Standards & Process

## Workflow Overview

1. **Author opens PR** and completes self‑review.
2. **Reviewer leaves free‑form comments** (no special prefix needed).
3. **Author classifies every reviewer comment** *before* re‑requesting review by adding a threaded reply with *one* of the tags below.
4. **Reviewer re‑checks.** 🔁
5. **Automation** fails the PR if any reviewer comment lacks a classification reply or references an unknown rule ID.
6. **Metrics are aggregated in the notion issue** and feed into the Shipping Hygiene OKR dashboard.
7. **Author sets issue to Done**

## ✅ PR Definition of Done

### Architecture Compliance
- [ ] Code follows [Architecture Guidelines](../architecture/guidelines.md).

### Code Quality  
- [ ] **All CI/CD are green**.
- [ ] **Zero** `print`, `console.log`, `debugger`, or `TODO` comments remain.
- [ ] Strong typing everywhere feasible (Python & TypeScript).
- [ ] Any new env-vars added to `.env.example`.

### Tests
- [ ] At least **one meaningful test** per new important logical branch or public function/method.
- [ ] Test coverage **does not decrease**.

### Migrations *(if applicable)*
- [ ] Database migrations are backwards compatible
- [ ] Migration rollback tested if data transformation involved
- [ ] New fields have appropriate defaults or are nullable

### UI Changes *(if frontend is affected)*
- [ ] Cross-browser compatibility verified
- [ ] Responsive design maintained
- [ ] Accessibility standards followed
- [ ] Visual regression testing passed

### Documentation
- [ ] Relevant ADR, README, or comments updated.

### Reviewer Prep
- [ ] Clear **what** & **why** in the PR description.
- [ ] Quick-start steps for reviewers (env-vars, demo data).

### AI Review Resolution
- [ ] **All AI reviewer comments have been resolved, or addressed with a comment**

### Self-Review
- [ ] All items above checked off **before** tagging a reviewer.

## Requesting a Review

- Link the PR in notion
- Send the notion issue to the reviewer to request a review

## Reviewing

- Reviewer must provide PR review within 1 business day

## Addressing a Review

Turn code‑review into a self‑service learning loop: every piece of feedback must either:

① map to an existing rule, 

② spawn a new Architecture Decision Record, or 

③ extend the Shipping Handbook. 

The *author* does this mapping, making review-learnings their responsibility and freeing the reviewer to focus on higher‑level concerns.

### How

- The author replies to every review comment
- After merging the PR, the author tallies all comments to create an overview of the tags and their counts

### Classification Tags (used in author replies)

| Tag | Meaning | Example Usage |
|-----|---------|---------------|
| `ack` | Acknowledged, will fix | Simple typos, obvious bugs |
| `done` | Already implemented | When reviewer missed existing code |
| `wontfix` | Intentional design choice | Explained in ADR or has business justification |
| `followup` | Will address in future PR | Technical debt, non-blocking improvements |
| `discuss` | Needs team discussion | Architectural decisions, breaking changes |
| `rule:AO-X` | Maps to existing rule | Reference to Architecture Outline rule |
| `adr:new` | Spawns new ADR | Complex architectural decisions |
| `handbook:extend` | Extends this handbook | New patterns or processes |

### Rule Proposal Template

**Problem**

Describe the recurring issue.

**Rule**

**AO-X**: One crisp, testable sentence.

**Example**

```python
# bad
service.send_email(...)

# good
infra.notifications.send_email(...)
```