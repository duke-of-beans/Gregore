# Gregore

**A cognitive operating system — one mind, many faces.**

Gregore is a persistent, autonomous AI system built to replace the stateless chat paradigm. It remembers everything, works while you sleep, and shows up wherever you already are — text, email, calendar, browser, voice — not as another app, but as a presence.

This is not a wrapper around an LLM. It is a deterministic cognitive architecture that calls language models as tools, not the other way around.

---

## Architecture

Gregore is built on named, composable subsystems — not one monolithic model call. Each organ has a defined responsibility, typed interfaces, and independent state.

### CORTEX — The Nervous System

The intelligence and services layer. 21 service tools spanning 96 actions across production infrastructure (Railway, Vercel, Supabase, GitHub, Twilio, Resend, Stripe, GoDaddy, Cloudflare, and more). Federated recall across a persistent knowledge graph, conversation archives, code history, email, and external research. Every service credential is pulled from an internal credential vault and scrubbed from all results.

### GANGLION — Fleet Dispatch

A multi-device execution engine. Work is dispatched to machines across the fleet — cloud servers, local hardware, GPU nodes — with automatic capacity probing, cost-tier routing (free hardware fills first, metered cloud sits idle until saturated), and typed work orders that enforce scope. Each dispatch is signed, tracked, and verified against real-world outcomes.

### The Git Plane

A single write path to GitHub for all agents, all machines, all surfaces. Commits are authored deterministically, PRs are opened and auto-landed when checks pass, and a shepherd service handles rebasing, merge conflicts, and deployment verification. No agent pushes to a default branch. No human runs git commands. The plane handles branch protection, secret scanning, and checkout reconciliation across the fleet.

### PLEXUS — World Knowledge

A research and monitoring faculty. Adapters connect to external data sources for multi-source investigation, entity tracking, and watchlist monitoring. Evidence chains carry provenance and confidence scores.

### ROSETTA — Language and Context

Ingests natural language into structured understanding. Conversations, voice notes, and freeform input become actionable context that persists across sessions and surfaces.

### The Routing Architecture

Every control-flow decision is a typed selection from a declared set. Low confidence on that selection *is* the escalation signal — structurally, the system cannot guess outside its options. Model selection, task routing, deliberation verdicts, and scope checks all follow this pattern.

The router operates on two axes: **leverage** (how important is this decision) and **cost** (how many tokens will it take). High-leverage, low-cost decisions go to the strongest model. Low-leverage, high-cost work goes to the cheapest model that clears the bar. The system learns from verified outcomes and adjusts.

### Work Orders and Receipts

Every unit of work flows through a typed order-receipt chain:

1. An order declares scope, acceptance criteria, and out-of-scope boundaries
2. A worker executes within that scope — attempts outside it trigger a kickback, not a guess
3. Verification checks the real-world outcome, not just the tool’s return code
4. A receipt records what was done, what changed, and what evidence supports it

This is how autonomous execution stays safe without being conservative. The system has explicit authority (standing grants ratified by the owner) rather than implicit permission that drifts.

### The Foundation

The most recent architectural layer — the constitution for autonomy:

- **Capability Manifest** — a typed registry of every action the system can take, with inputs, outputs, side effects, required credentials, verification methods, and rollback paths
- **Standing Grants** — machine-readable authority records that replace vague trust tiers with explicit, permanent, ratified grants
- **Persistent Runtime** — an always-on supervisor with durable work queues, job leases, idempotency, crash recovery, and reconciliation against external state
- **TESSRYX Spine** — a dependency intelligence graph (nodes, edges, constraints, provenance, blast radius, critical path) with time-weighted confidence decay on every observation

The proof tests: work continues while no chat is open; model failures don’t kill active jobs; duplicate events don’t duplicate real-world actions; crashed workflows resume with evidence intact; revoking one credential doesn’t break unrelated capabilities.

---

## Surfaces

Gregore is not an app. It inhabits existing channels:

- **GregLite** — a cockpit dashboard showing fleet state, dispatch activity, and the reconciliation delta
- **Text/SMS** — conversational interface; you text approvals from your car
- **Email** — reads, drafts, and sends through Microsoft 365
- **Calendar** — fills itself from project timelines, email threads, and work orders
- **Voice** — text-to-speech with emotional register, speaker verification for authentication
- **Wall Greg** — a physical ambient display showing status and affect
- **Body C** — a robotic embodiment (hardware in progress)

Each surface adapts its register — a text about sprint approvals is concise with quick-choice options; a research discovery gets the full story.

---

## The Core Bet

The persona is assembled before the model is chosen, so a lane change at a turn boundary is still Greg. The conversation agent (COO) talks with the user and delegates work to typed workers. Workers are Jev-shaped: a work order in, a declared outcome set, calibrated confidence out.

Mechanical work never goes through a language model. Anything based on logic runs as code. The router enforces this with a cost ladder: shell and SQL at $0, local models next, cheap hosted after that, strong reasoning only when the bar requires it.

---

## What’s Running

This is not a whitepaper. The system is in active daily use across production infrastructure:

- Federated recall across 4,000+ conversations and 90,000+ messages
- Fleet dispatch across multiple machines with automatic capacity probing
- 21 service integrations controlling real production infrastructure
- Autonomous code development via typed work orders with acceptance tests
- Git operations through a dedicated plane handling commits, PRs, merges, and deployments
- Credential management through a portfolio-wide vault
- Proactive monitoring with systemd failure alerting and checkout reconciliation

---

## Design Philosophy

- **Undercomplexify.** Routing machines hold nothing. Build for use, not elegance.
- **Option B Perfection.** 10x, not 10%. No patches.
- **Zero Technical Debt.** No mocks, stubs, or TODOs in production.
- **Foundation Out.** Backend before surface. The foundation before the feature.
- **Lean-Out.** If a production tool exists, use it. Don’t reinvent.
- **Same fix three times means stop and redesign.**

---

## Status

Active development. In daily production use. Not yet publicly available.

See [ARCHITECTURE.md](ARCHITECTURE.md) for the detailed system overview.

**Builder:** [David Kirsch](https://davidkirsch.me) — Solo founder, systems architect. Silent Ampersand + Borrowed Light Group.

---

## License

MIT
