# Voice AI Prompting Guide

## Overview

This resource teaches techniques for creating effective prompts for voice AI assistants, covering design, testing, and refinement strategies to enhance agent reliability and user experience.

## Key Concepts

**Success Rate Definition**: The percentage of requests an agent completes independently without human intervention. Complex use cases require more iteration to improve this metric.

**Why It Matters**: Quality prompts "guide the AI to produce accurate, relevant, and context-sensitive outputs" while improving handling of requests without intervention.

## The Four-Step Process

1. **Design** - Create initial prompts considering task, context, and desired outcomes
2. **Test** - Evaluate responses against expectations and intended goals
3. **Refine** - Adjust wording, add details, and reduce ambiguity
4. **Repeat** - Iterate until outputs are accurate and relevant

## Structural Best Practices

Organize prompts into distinct sections:
- **Identity**: Agent persona and role
- **Style**: Tone and stylistic guidelines
- **Response guidelines**: Formatting and structure requirements
- **Task & goals**: Objectives and step-by-step instructions

## Advanced Techniques

**Breaking Down Complexity**: Use conditional logic and numbered steps for multi-stage interactions.

**Response Timing**: Explicitly mark where agents should pause: `<wait for user response>`

**Tool Integration**: Reference external APIs by their designated names and specify usage conditions.

**Silent Transfers**: When transferring calls, trigger tools without sending text responses to maintain seamless experiences.

**Error Handling**: Include fallback options and clarifying question protocols for unclear inputs.

## Voice Naturalness Tips

- Spell out numbers rather than using digits
- Add hesitations ("uh," "um"), stuttering (repeated sounds), and pauses (ellipses)
- Use emotional emphasis through capitalization and punctuation
- Inject personality through conversational tone and reduced jargon

## Common Solutions

For robotic-sounding speech, spell numbers phonetically. To humanize assistants, add personality descriptors and conversational language patterns.
