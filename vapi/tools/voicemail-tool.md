# Voicemail Tool Documentation

## Overview

The voicemail tool empowers your assistant to manage voicemail interactions intelligently. As the documentation states, it provides "Maximum flexibility - Assistant decides when and what to say" and operates differently from automatic system-level detection.

## Key Functionality

The tool operates through a straightforward process: your assistant identifies voicemail indicators in greetings, invokes the tool, delivers a configured message, and the call terminates. This differs from automatic detection because "detection and response entirely in the assistant's hands."

## Configuration Approaches

### Text-to-Speech Messages
You can use dynamic template variables like `{{company}}`, `{{message}}`, and `{{phone}}` to create flexible, consistent messaging without hardcoding values.

### Pre-recorded Audio
The system supports `.wav` and `.mp3` files hosted at URLs. This approach suits situations requiring "brand-specific messaging or when you need precise pronunciation."

## Implementation Guidance

**Detection prompting** requires specificity about voicemail cues: unavailable, leave a message, voicemail, at the tone, and beep.

**Message structure** should remain "Brief - Under 30 seconds," "Clear - State name, company, and purpose," and "Actionable - Include callback number or next steps."

## Tool vs. Automatic Detection

The voicemail tool offers assistant-driven control and lower costs (triggering only when needed), while automatic detection provides system-level handling. The documentation warns against combining both simultaneously due to potential complications.

## Use Cases

Common applications include sales outreach, appointment reminders, customer service callbacks, and lead qualification—all scenarios where personalized, context-aware voicemail messages add value.
