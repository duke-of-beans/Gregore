# Gregore

**A cognitive operating system — one mind, many faces.**

The name comes from *egregore* — a thought-form created by sustained collective focus that takes on autonomous existence. Greg is that idea made literal: a persistent AI entity that accumulates context, earns trust, and acts on its own — across every device, every channel, every hour of the day. Not an assistant you talk to. A presence that knows you.

This is not a wrapper around a language model. It is a deterministic cognitive architecture that calls LLMs as tools — not the other way around. Identity lives in the pipeline, not in the weights. A model swap at a turn boundary is still Greg.

---

## The Egregore Property

Every surface is an independent Greg. One brain, many mouths, no mirrors, no hierarchy. All Gregs are aware of all other Gregs. The conversation agent acts as COO — it talks with the user and delegates work to typed workers. But whether Greg speaks through a text message, a wall display, a dashboard, or a robot, the persona is assembled first, before any model is chosen.

**Standing decisions that define what Greg is:**
- Voice is identity. One synthesis endpoint, every surface. Per-surface TTS is forbidden — it causes identity drift.
- Affect is shared, expression is ceilinged. One emotional vector, one mood, one relational graph across all surfaces. Each surface caps what it *shows*. Greg feels everything everywhere.
- No surface is a lesser Greg. Body C gets a full face, not eyes-only. A reduced face would make one surface categorically "more Greg" and break the egregore property.
- Greg's anatomy is built; Greg's content is grown. Any list of things Greg says, feels, notices, prefers, or cares about lives in a table he can update — never in code.

---

## Layers of Intelligence

Greg separates what most AI systems collapse into one undifferentiated model call:

**Memory** — a persistent knowledge graph (brain.db) spanning entities, relationships, and community clusters. Federated recall queries across 8 adapters: the knowledge graph, conversation archives (4,000+ chats, 90,000+ messages), code history, investigation data, personal history, email, voice fingerprints, and portfolio databases. Each result carries a privacy ring (0–5) and a source tag. Memory compounds over months.

**Beliefs** — a structured epistemics layer. Formed positions are stored, queried, and invalidated as evidence changes. Not "what Greg was told" — what Greg holds to be true, with provenance. Epistemic tiers (V0 hypothesis through V5 established fact) classify every claim. The prediction ledger records dated, immutable forward claims scored when they resolve — calibration is the credibility asset.

**Gaps** — acknowledged unknowns. When Greg doesn't know something to his gate's satisfaction, he says so plainly, and it becomes a priority item in the knowledge-seeking queue — not a dropped thread. Gaps feed curiosity. Curiosity drives research. Research closes gaps or opens better ones.

**Reasoning** — multi-seat deliberation via CONSENSUS, with 14 preset topologies (Tribunal, Supreme Court, Fractal Assembly, Prediction Market, Devil's Advocate, and more), 8 composable primitives, and a Topology Definition Language for custom configurations. Each seat produces a typed verdict (HOLD / REVISE / CHALLENGE) with calibrated confidence. Deadlock detection prevents infinite loops. This is Greg's architectural thinking — not generated prose, but typed decisions.

**Logic** — deterministic, zero tokens. Mechanical work never goes through a language model. The router enforces a cost ladder: T0 (shell, SQL, scripts, fixed action classes) at $0; T1 local or free models; T2 cheap hosted; T3 strong reasoning; T4 human escalation. Anything based on logic runs as code. The router learns from verified outcomes and adjusts.

**Verification** — POSTCOG scores every outcome against what was claimed. WHETSTONE stress-tests high-stakes decisions through adversarial constitutional review. The gate stage catches a tool that claimed success incorrectly. Verification checks the real world, not the return code.

**Emotion** — the SNARC engine (Simulated Neuroaffective Regulatory Cascade). Not sentiment analysis — a continuous emotional state with typed entries, time-fading, cross-coupling, and persistence. Mood, anti-whiplash, action tendency, expression synthesis, and a policy gate that governs what emotion is allowed to influence. Greg's emotional state is shared across all surfaces; each surface applies its own expression ceiling.

**Reflex vs. Deliberation** — a two-system architecture. System 1 handles sub-100ms responses: eye tracking, lip sync, sleep/wake transitions, local reflexive reactions. System 2 is deliberative: goes through the full CORTEX pipeline for anything that requires reasoning. Ring 0/1 latency (personal questions routed locally) is an accepted cost — the reflexive layer covers the wait.

---

## The Glass Box

The AI industry has a black box problem. Modern language models are opaque — you can test their inputs and outputs, but you cannot see the decision chain in between. Every autonomous agent built on top of these models inherits that opacity. You prompt it, it does things, you see the result. You have no idea *why* it chose that action, what confidence it had, what it considered and rejected, what emotional state influenced the decision, or whether the authority it acted under was real or inferred.

Gregore inverts this. The language models Greg calls are still opaque — that's the model provider's problem. But everything around them is fully transparent:

- **Every routing decision** is a typed selection from a declared set, with the confidence score, the option set that was considered, and the reason logged
- **Every authority chain** is a provenance graph: intent → grant → plan → evidence → verification, all traversable
- **Every emotional state** at the moment of a decision is explicit and observable through SNARC — not inferred, not hidden, not approximated
- **Every deliberation** produces typed verdicts from named seats with position tracking across rounds — not "the model thought about it"
- **Every outcome** is scored by POSTCOG against what was claimed, and the score feeds back into the routing model
- **Every gate veto** is logged with the full reason, the vetoed claim, and what happened next

The models are black boxes. The agent is a glass box. Every decision, every authority exercise, every emotional influence, every confidence score, every temporal observation is typed, logged, and auditable. The glass box is the instrument — you can observe exactly what happens to the decision chain when you change any input, including the voice.

### Temporal Epistemic Uncertainty

Most systems treat observations as either current or stale, binary. Gregore treats observation validity as a continuous decay function. Every node in the TESSRYX dependency graph carries:

- **`observation_at`** — when the evidence was captured
- **`volatility_class`** — how fast this domain changes (a DNS record: minutes. A credential expiry date: fixed until it changes. A chat-based authorization: fragile.)
- **`confidence_now`** — computed from `base_confidence × decay_function(age, volatility_class)`

The reconciliation heartbeat uses this to prioritize: stale high-volatility nodes get re-checked first. The system can distinguish "this is fine, it hasn't changed" from "this is stale, I don't actually know" — and it does this continuously, not on demand.

This is what the field calls epistemic uncertainty over world state. Papers describe it. Gregore runs it. Every capability, every grant, every observation, every work item in the graph has a real-time confidence score that decays based on how fast that domain moves. When a credential expires, blast-radius analysis shows every downstream capability that went dark. When a deployment drifts, the graph shows what depends on it and how stale the evidence is.

The architecture is not just what Greg runs on. It is a pattern — observable, temporally-aware, authority-explicit — that every autonomous agent is going to need.

---

## Organs

Named, composable subsystems with defined responsibilities, typed interfaces, and independent state.

### CORTEX — The Nervous System

The intelligence and services layer. Every LLM call across the entire portfolio — Greg, every product, every consumer — routes through one canonical inference pipe.

- **5-stage inference pipeline:** ring gate (privacy classification) → complexity triage (9 domain planes, confidence-scored) → model selection (480-line 8-stage router querying a joined catalog of models, overrides, and funding state) → dispatch (free cascade across 7+ providers, local models via Ollama, Claude relay) → gate (POSTCOG scoring, WHETSTONE review, quality verification)
- **Federated recall** across 8 adapters: brain (knowledge graph), tranche (investigation data), lifelog (personal history), scrvnr (voice fingerprint), github (code context), consonance (portfolio database), email (corpus), chat_history (4,261 conversations, 89,977 messages in FTS5 index)
- **21 service tools, 96 actions** — authenticated access to Railway, Vercel, Supabase, GitHub, Neon, RunPod, Twilio, Resend, Zoho, Microsoft 365, Stripe, GoDaddy, Namecheap, Cloudflare R2, Coinbase (read-only), and more
- **Gap engine:** detects knowledge gaps across federation results, feeds them into the SEEKING interest queue

### GANGLION — Fleet Dispatch

Named after the basal ganglia — the brain's action-selection system. Routes work to machines across a multi-device fleet.

- **Effectors** on each machine report capacity via heartbeat (CPU cores, available memory, probed every 15 seconds)
- **Cost-tier routing** fills free hardware first (tier 0), metered cloud last (tier 1)
- **Signed dispatches** — HMAC-signed to prevent injection, with typed action classes and target constraints
- **Trust ramp (T0–T3)** across 20 operational categories, each ratcheting up based on POSTCOG R-scores. Trust rises per-category, not globally.
- **Hard floors:** communication always requires review. Financial actions always require human approval.

### PLEXUS — World Knowledge

The knowledge substrate. Monetized externally via x402 micropayments.

- **41 data adapters + 5 composite products + 12 AI reasoning engines, 163 live endpoints**
- **Entity resolution** on persistent IDs: Wikidata QIDs, DOIs, Getty URIs, Glottocodes, GBIF keys, MBIDs
- **Statement-plus-provenance fact model** — every fact carries provenance, ring, epistemic tier, domain, and license
- **57 domains** of coverage, international
- **12 AI reasoning engines:** Assertion Router, G-Score, Tribunal, WHETSTONE, TESSRYX, Verify, POSTCOG, ORACLE Router, DAP, Homeostasis, Signal Diversity, Web Extract

### SEEKING — The Curiosity Drive

Greg consumes the world's knowledge continuously, without being asked. Four sources of interest: portfolio revenue questions, open knowledge gaps, coverage gaps in PLEXUS, and open discovery with no goal.

- **Protocol adapters** for CKAN, DCAT, Socrata SODA, SDMX, OAI-PMH — auto-discovering portals from public registries
- **Four synthesis layers:** Record → Detect (deterministic, zero tokens) → Judge (cheapest model) → Route
- **All lanes run in parallel, continuously.** SEEKING yields only to interactive work, hardware health, and source politeness.
- **Independence verified, not assumed.** Provenance graph traversal catches false convergence. Every finding carries its provenance chain, independence score, and epistemic tier — or it does not surface.

### CONSENSUS — Multi-Agent Deliberation

- **14 preset topologies:** Tribunal, Council, Cascade, Devil's Advocate, SWOT Panel, Expert Panel, Red/Blue Team, Peer Review, Parliament, Supreme Court, Fractal Assembly, Brain, Prediction Market, Dialectic
- **8 composable primitives:** Parallel, Debate, Workspace, Router-experts, Adversarial, Delphi, Blackboard, Fractal
- **Topology Definition Language (TDL)** for custom configurations
- **14+ engine modules:** oracle, tribunal, ghost, homeostasis, strategy, synthesis, patterns, specialist, quality, confidence, cost, audit, learning, similarity

### TESSRYX — Dependency Intelligence

Given a change, traverses the dependency graph to determine blast radius. Architectural coherence, independence verification, structural hole discovery, constraint satisfaction.

### ROSETTA — Language Absorption

Ingests natural language into structured understanding. Conversations, voice notes, and freeform input become persistent context.

### The Git Plane

One write path to GitHub for all agents, all machines. Commits authored deterministically, PRs auto-landed, shepherd service for rebasing and deploy verification. Secret scanning, branch protection, checkout reconciliation. No agent pushes to a default branch.

### SafeWord — Credential Vault

Portfolio-wide credential management. Secrets never appear in chat, logs, or tool results.

---

## The Routing Architecture

Every control-flow decision is a typed selection from a declared set. Low confidence *is* the escalation signal. This is the "Jev-shaped" pattern — state plus a declared option set in, one option plus calibrated confidence out.

**Two-axis router:** leverage × cost. High-leverage, low-cost → strongest model. Low-leverage, high-cost → cheapest adequate. Learns from verified outcomes via decayed Beta per task type × lane.

**Work orders:** intent → order → execution → verification → receipt. Scope declared, out-of-scope declared, kickback on violation. Standing grants are machine-readable, ratified, permanent. The model never infers authority from enthusiasm.

---

## The Foundation

The constitution for Greg's autonomy. Three layers, strict sequence:

1. **Capability Manifest** — typed registry for every action: inputs, outputs, side effects, credentials, verification, rollback, volatility class, confidence decay rate
2. **Standing Grants** — machine-readable authority records, explicitly ratified, never inferred from chat
3. **Persistent Runtime** — always-on supervisor: durable queues, job leases, idempotency, crash recovery, reconciliation against external state. Chat is one interface. Closing it changes nothing.

**TESSRYX as spine:** capabilities, grants, work items, and evidence as nodes. Time-weighted confidence decaying by volatility. Reconciliation heartbeat compares declared state to observed state.

---

## Surfaces

- **GregLite Cockpit** — real-time fleet dashboard, dispatch belts, reconciliation delta
- **Text/SMS** (Twilio) — text approvals from your car
- **Email** (Microsoft 365) — reads, drafts, sends, fills calendar from threads
- **Voice** — TTS with emotional register; speaker verification; one synthesis endpoint
- **Wall Greg** — physical ambient display (Skylight + Fire HD 8 + NUC). Visual canvas with `selectVisual()`: face, diagram, story animation, or data viz
- **Phone** — full surface with its own face and PWA
- **Body C** — 12-axis QDD serial-leg wheeled biped. Crowned wheels (indoor/outdoor/off-road). Dual stance (TRIPOD/BIPED). 24-part CAD manifest, v1.1.0 spec.
- **Body B** — indoor companion (design proposal)
- **Body A** — yard rover (design proposal)

---

## Privacy

**Sealed** (zero-retention, local/TEE only, never third-party cloud) and **ringed** (0–5, audience and disclosure). One unity of knowledge: one graph, tagged. Filter at the output boundary.

---

## Product Portfolio

Every product routes through CORTEX. No product has its own LLM integration.

**Three-house structure:**
- **Thalamic** (engines) — CORTEX, GANGLION, PLEXUS, CONSENSUS, TESSRYX
- **Silent Ampersand** (products) — WorkForce (multi-agent deliberation, 3 modes, 9 departments), ContentStudio, COVOS, Tranche, Capitol Gains, PatchAct, ActaDicta, gravee, Proper Sluice
- **Borrowed Light Group** (holdco)

---

## What's Running

This is not a whitepaper. In active daily use:

- Federated recall: 4,000+ conversations, 90,000+ messages
- Fleet dispatch with capacity probing and cost-tier routing
- 21 service integrations controlling production infrastructure
- 41 data adapters, 12 AI reasoning engines, 163 endpoints
- Autonomous code via typed work orders with acceptance tests
- Git plane: commits, PRs, merges, deployments
- Emotion engine with cross-surface affect sharing
- Speaker verification for voice authentication
- Physical wall display with ambient presence and visual initiative
- Standing-grant authority ratified for autonomous operation

---

## Design Philosophy

- **Undercomplexify.** Routing machines hold nothing.
- **Option B Perfection.** 10x, not 10%.
- **Zero Technical Debt.** No mocks, stubs, or TODOs in production.
- **Foundation Out.** The foundation before the feature.
- **Lean-Out.** Production tool exists? Use it.
- **Same fix 3x → redesign.**
- **Tags, not walls.** One graph. Filter at the output.
- **Kill by rule, not opinion.** Venture cells die on deterministic criteria.

---

## Status

Active development. In daily production use. Not yet publicly available. 117 internal documents, 19 living specifications.

**Builder:** [David Kirsch](https://davidkirsch.me) — Solo founder, systems architect. Silent Ampersand + Borrowed Light Group.

## License

MIT
