# Gregore

A cognitive operating system built around one idea: an AI assistant shouldn't forget you the moment the conversation ends.

## The problem

Every AI assistant today has the same limitation — it forgets you between sessions. You re-explain your projects, re-teach your preferences, re-establish context every single time. The intelligence is real but blind: it doesn't know what you're waiting on, doesn't know what a colleague mentioned three months ago that's relevant now, doesn't know what's been quietly broken for two days.

## What changes

Gregore makes context permanent, makes intelligence proactive, and makes the interface invisible.

**You never re-explain yourself.** Context compounds over months rather than resetting every conversation.

**It works while you're not looking.** Work gets proposed, executed, and reported on its own schedule — not just when you open a chat window.

**It shows up where you already are.** Not another app to check — it reaches you through channels you already use, adapting its register to each one the way a person would.

**Trust is earned, not configured.** New kinds of action start with approval required. After a pattern proves reliable, it graduates toward acting independently. Trust only moves in one direction — forward, based on track record.

## Architecture, at the level that matters publicly

Gregore is built on a persistent, multi-system cognitive architecture — memory, curiosity, adversarial self-checking, epistemic calibration, and autonomous maintenance as separate, named, composable systems rather than one undifferentiated model call. Several of those systems already have their own public write-ups; see [davidkirsch.me/builds](https://davidkirsch.me/builds) for the full picture of how the pieces relate. The implementation specifics — stack, infrastructure, cost model — stay private; what's here is the shape of the thing and why it's built this way.

## Status

Active development. Not yet publicly available.
