---
name: "Frontend Styling"
description: "Apply when working on user interface elements, visual design, styling, or UI/UX improvements. This workflow is appropriate for tasks focused on enhancing visual consistency, improving user experience, implementing design systems, or styling new components."
triggers: ["styling", "UI", "UX", "design", "visual", "aesthetics", "components"]
---

# Frontend Style & UI Workflow

Apply when working on user interface elements, visual design, styling, or UI/UX improvements. This workflow is appropriate for tasks focused on enhancing visual consistency, improving user experience, implementing design systems, or styling new components.

Use when the primary goal is aesthetics, usability, or design language consistency rather than functional implementation.

## Step-by-Step Guide

### 1. Select Source UI

- Find an existing UI design on platforms like Dribbble, focusing solely on styling, not functionality.

### 2. Generate Detailed Style Guide with LLM

- Paste the selected UI image into an AI assistant (e.g., Claude).
- Use the following detailed prompt:

```
I need you to describe, in detail, the styling and branding on this UI. The engineer who will implement this design cannot see it. Write a highly detailed stylesheet/spec that clearly explains how to replicate the overall styling—colors, fonts, spacing, feel, overlaps, etc. Focus purely on the visual aesthetics and vibes rather than specific layout elements.
```

### 3. Refine and Prepare the Style Guide

- Remove unnecessary filler information for clarity and precision.
- Insert the refined style guide into the following prompt template:

```
<style_guide>
PASTE YOUR STYLE GUIDE HERE
</style_guide>

I want you to apply this style guide to restyle my entire app. Ensure the result perfectly matches the described aesthetics.
```

### 4. Implementation with AI Coding Assistant

- Paste the prompt into Cursor Composer (using Sonnet 3.7) or Claude-Code.
- Iteratively refine as necessary until the desired styling is achieved.

## Benefits

- Efficient and effective replication of professional design aesthetics.
- Rapid styling iterations without direct visual references.