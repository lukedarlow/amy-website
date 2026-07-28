# Execution plans

Use an execution plan (ExecPlan) for work that spans several subsystems, contains meaningful unknowns, changes architecture, or is likely to take more than one focused session. Small, obvious changes do not need one.

An ExecPlan is a living, self-contained design document. A new contributor should be able to understand the goal, constraints, current state, next action, and verification method using only the repository and the plan.

Store active plans in `docs/plans/` with a descriptive kebab-case filename.

## Required sections

### Purpose and user outcome

Explain what a visitor or Amy will be able to do after the work and how a reviewer can observe it.

### Context and constraints

Name the relevant files, product requirements, legal/privacy considerations, terms that need definition, and explicit non-goals.

### Current state

Describe what exists now. Include evidence from the repo rather than assumptions.

### Proposed approach

Explain the design in plain language, including important interfaces and data flow. Record alternatives considered and why this approach is preferred.

### Milestones

Break the work into independently verifiable outcomes. For each milestone include:

- files or areas affected;
- concrete action;
- commands or review steps;
- expected observable result.

### Progress

Maintain a dated checklist. Update it whenever work pauses or a milestone changes.

### Decisions

Record decisions with dates, rationale, and consequences. Do not erase superseded decisions; mark them superseded.

### Discoveries and risks

Record unexpected behavior, legal/content blockers, performance concerns, and evidence that changes the plan.

### Verification and acceptance

List exact automated checks, browser sizes and flows, accessibility checks, security/privacy checks, and any required human approvals.

### Recovery and handoff

Explain how to safely rerun steps, where artifacts live, what remains, and the single next action.

## Plan rules

- Keep the plan accurate as implementation proceeds.
- Prefer demonstrable behavior over a list of code edits.
- Use prototypes for material unknowns and record what they prove.
- Never use an ExecPlan to broaden the user's requested scope.
- Do not mark a milestone complete until its stated verification has run or is explicitly recorded as blocked.
