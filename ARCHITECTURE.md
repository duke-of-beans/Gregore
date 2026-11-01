# Gregore Architecture

**Public-facing overview of the cognitive operating system.**
Distilled from the internal canonical specification (GREGORE_CANON). Operational details, credentials, and deployment topology are omitted.

---

## 0. Mission

Replace the stateless chat paradigm as the primary working environment. Not “good enough to try” — better, so that opening a conventional AI chat looks like a downgrade.

---

## 1. The Core Bet

Greg’s core is a persistent deterministic logic layer that calls LLMs as tools — not an LLM that calls tools.

This is a deliberate inversion. The pipeline stages, routing decisions, scope enforcement, and state management are all deterministic code. Language models are called when reasoning is needed, chosen per-task by a router that optimizes for the cheapest model that clears the quality bar.

The persona is assembled before the model is chosen. A model swap at a turn boundary is still Greg because identity lives in the pipeline, not in the weights.

---

## 2. Subsystems

### CORTEX — Intelligence and Services Layer

The nervous system. Provides:

- **Federated Recall** — queries span a knowledge graph (brain.db), conversation archives (4,000+ chats, 90,000+ messages), code history, email, calendar, and external research. Each result carries a privacy ring (0 = most private, 5 = public) and a source tag.
- **Service Tools** — 21 services, 96 actions. Authenticated access to Railway, Vercel, Supabase, GitHub, Neon, RunPod, Twilio, Resend, Zoho, Microsoft 365, Stripe, GoDaddy, Namecheap, Cloudflare R2, Coinbase (read-only), and more. Credentials are pulled from an internal vault and scrubbed from every result.
- **Beliefs and Gaps** — a structured epistemics layer. Formed positions (beliefs) and acknowledged unknowns (gaps) are stored, queried, and invalidated as evidence changes.

### GANGLION — Fleet Dispatch

The execution engine. Work is dispatched to machines across a multi-device fleet:

- **Effectors** run on each machine, reporting capacity via heartbeat (CPU cores, available memory, probed every 15 seconds)
- **Cost-tier routing** fills free hardware first (tier 0), metered cloud last (tier 1)
- **Typed dispatches** carry a prompt, an action class, target constraints, and a preferred model
- **Signed inserts** — every dispatch is HMAC-signed to prevent injection
- **Work orders** enforce scope: acceptance criteria, out-of-scope boundaries, and a kickback mechanism when a worker attempts to exceed its scope

### The Git Plane

One write path to GitHub for all agents, all machines, all surfaces:

- Commits are authored deterministically as the owner
- PRs are opened on work branches, labelled, and auto-landed when CI passes
- A shepherd service rebases behind-main PRs, merges when green, and tracks deployment state
- Secret scanning rejects token-shaped strings in committed files
- Checkout reconciliation rescues dirty or ahead checkouts to held PRs — never resets
- Branch protection is enforced programmatically, not manually

No agent pushes to a default branch. No human runs git commands for commits, pushes, PRs, merges, or branch rules.

### PLEXUS — World Knowledge and Research

A research faculty with multiple adapters for external data. Supports multi-source investigation, entity tracking, and watchlist monitoring. Evidence chains carry provenance and confidence.

### ROSETTA — Language and Context Ingestion

Ingests natural language into structured understanding. Conversations, voice notes, and freeform input become actionable, persistent context.

### SafeWord — Credential Vault

Portfolio-wide credential management. Secrets are stored, rotated, and accessed programmatically. Non-secret identifiers (account SIDs, project IDs) are handled in plaintext; secrets never appear in chat, logs, or tool results.

---

## 3. Routing Architecture

The unifying design principle: **every control-flow decision is a typed selection from a declared set, and low confidence on that selection IS the escalation signal.**

This is the “Jev-shaped” pattern — state plus a declared option set in, one option plus calibrated confidence out. The system structurally cannot select outside the set, and structurally cannot guess when it should ask.

### The Two-Axis Router

Decisions are routed on two axes:

| | Low tokens | High tokens |
|---|---|---|
| **High leverage** | Strongest model (important decision, cheap to serve) | Split: strong model plans, cheap model or code executes |
| **Low leverage** | Cheapest adequate model | Cheapest adequate model |

The cost ladder:
- **T0**: Shell, SQL, scripts, fixed action classes — $0, never a model
- **T1**: Local or free models
- **T2**: Cheap hosted models
- **T3**: Strong reasoning models
- **T4**: Human (escalation)

### Learning from Outcomes

Verified outcomes (good fit / underpowered / overprovisioned / failed), user ratings, gate vetoes, and failovers update a decayed Beta distribution per task type × lane. Capability is read from the posterior, not from static catalog tiers.

---

## 4. The Work-Order System

Every unit of work flows through a typed chain:

```
intent → order → execution → verification → receipt
```

- **Orders** declare scope, acceptance criteria, and what is explicitly out of scope
- **Execution** is bounded — attempts outside scope trigger a kickback (structured escalation), not a guess
- **Verification** checks the real-world outcome, not just the tool’s return code
- **Receipts** record what was done, what changed, and what evidence supports the claim

### Latitude as a Dial

The system learns how much autonomy to take. After successful executions of a task type, supervision requirements decrease. Trust only moves in one direction — forward, based on track record, never on enthusiasm.

---

## 5. The Foundation — Capability Manifest, Standing Grants, Persistent Runtime

The architectural constitution for autonomy. Three layers, built in strict sequence:

### Layer 1: Capability Manifest

A typed registry for every action the system can take:

- Name, description, typed inputs and outputs
- Side effects — what it changes in the world
- Required credentials and required machines
- Verification method — how to confirm the real-world outcome
- Compensation path — how to roll back on failure
- Volatility class and confidence decay rate — how quickly observations go stale

New capabilities register here or they don’t exist. The registry is the source of truth for what the system can do.

### Layer 2: Standing Grants

Machine-readable authority records:

- Principal, services, allowed actions, limits
- Notification preference (immediate / summary / exception-only)
- Source provenance (ratification date, session, verbatim authorization)

Inside a grant: execute, verify, notify afterward. Outside a grant: request a precise expansion of authority with evidence of why it’s needed.

Grants are not inferred from chat history. They are explicitly ratified in a structured session. The model never infers authority from enthusiasm.

### Layer 3: Persistent Runtime

An always-on supervisor independent of any chat session, any model call, any single machine:

- Durable work queue — jobs survive model failures, container restarts, network outages
- Job leases with heartbeats — if a job stops reporting, it’s assumed dead and re-queued
- Idempotency keys — duplicate events do not create duplicate real-world actions
- Resume-from-state — crash recovery picks up from checkpoints, not from scratch
- Reconciliation against external state — verify against the real world before retrying a side effect
- Standing grant enforcement — every action checks the grant registry before executing
- Capability manifest lookup — every action resolves against the manifest for inputs, credentials, verification, and rollback

### TESSRYX as Spine

The foundation runs on a dependency intelligence graph:

- Capabilities, grants, work items, and evidence are nodes
- Dependencies between them are edges with precedence constraints
- Critical path through the work queue is prioritization as constraint satisfaction
- Blast radius analysis shows what downstream work is affected by a failure
- Every node carries time-weighted confidence that decays based on volatility class
- The reconciliation heartbeat is periodic blast radius analysis: comparing declared state to observed state

### Proof Tests

The system works only when it demonstrates all of these:

1. Work continues while no chat is open
2. A model failure does not kill the active job
3. Duplicate events do not duplicate accounts, purchases, messages, or deployments
4. A timeout triggers reconciliation before retrying a side effect
5. Verification catches a tool that claimed success incorrectly
6. A crashed workflow resumes with its evidence and pending steps intact
7. Revoking one credential does not compromise unrelated capabilities
8. The owner receives outcomes, evidence, and exceptions — not permission requests for authorized work

---

## 6. Surfaces

Gregore inhabits existing channels rather than adding another app:

- **GregLite Cockpit** — a real-time dashboard showing fleet state, dispatch belts, and the reconciliation delta (observed vs. expected vs. diverged vs. acted on)
- **Text/SMS** (Twilio) — conversational, concise, quick-choice options
- **Email** (Microsoft 365) — reads, drafts, sends, fills calendar from threads
- **Voice** — text-to-speech with emotional register; speaker verification for authentication
- **Wall Greg** — physical ambient display showing status and affect
- **Body C** — robotic embodiment (hardware CAD in progress)

Each surface adapts its register to the channel’s dynamics.

---

## 7. Deliberation System

For high-stakes decisions, the system runs a multi-seat deliberation:

- A topology function assigns seats (perspectives) based on the question type
- Each seat produces a verdict (HOLD / REVISE / CHALLENGE) with confidence
- Position stability and deadlock detection prevent infinite loops
- The result is a typed decision, not generated prose

---

## 8. Privacy Architecture

Two classes:

- **Sealed** — zero-retention, absolute, outside the ring system. Only sealed lanes (zero-retention, TEE or local inference). Never sent to third-party cloud models.
- **Ringed** — everything else. Rings 0–5 are classifications for audience and disclosure, not retention rules. A ring-0 conversation may use any eligible lane; ring classification governs what may be published or shared.

Local inference (Ollama on local hardware) and GPU-TEE (trusted execution environment) provide the sealed channel.

---

## 9. Design Philosophy

- **Undercomplexify.** Routing machines hold nothing. Build for use, not elegance.
- **Option B Perfection.** 10x, not 10%. No patches.
- **Zero Technical Debt.** No mocks, stubs, or TODOs in production.
- **Foundation Out.** Backend before surface. The foundation before the feature.
- **Lean-Out.** If a production tool exists, use it. Don’t reinvent.
- **Same fix three times → stop and redesign.**

---

## 10. Prior Art and Alignment

- **Active inference / free energy principle** — the reconciliation heartbeat is prediction-error minimization; the capability manifest is the action repertoire
- **Capability-based security** — standing grants are capability tokens, specific and unforgeable
- **Event sourcing / CQRS** — the operational journal is event-sourced; current state is derived from the event stream
- **BDI agent architecture** — beliefs (brain.db + journal), desires (goals + grants), intentions (active work items)

---

*Full architectural specification maintained internally. This document reflects the public-facing system design as of November 2026.*
