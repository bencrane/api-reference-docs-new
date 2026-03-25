# Assistant-Based Warm Transfer Documentation

## Overview

This guide covers using dedicated AI assistants to manage call transfers. The system allows you to configure custom behavior through prompts, giving the assistant access to previous conversation context to decide whether to complete or cancel transfers.

**Key learning objectives:**
- Setting up transfer assistants with custom prompts
- Managing assistant-operator interactions
- Addressing failed transfer scenarios

## How It Works

The warm transfer process follows these steps:

1. Customer requests transfer from original assistant
2. Customer placed on hold with audio
3. Transfer assistant contacts the destination operator
4. Assistant follows configured instructions based on previous conversation
5. Assistant either completes the transfer or cancels it

**Cancellation triggers include:**
- Reaching `maxDurationSeconds` limit
- Operator doesn't answer
- Voicemail detection (based on prompt configuration)
- Custom conditions in prompts

## Core Configuration Elements

**Transfer Assistant Properties:**
- `firstMessage`: Initial greeting when operator answers
- `firstMessageMode`: "assistant-speaks-first" or "assistant-waits-for-user"
- `maxDurationSeconds`: Automatic cancellation timeout
- `silenceTimeoutSeconds`: Silence duration before cancellation (10-3600 seconds)
- `model`: Provider, model type, and system messages controlling behavior

**Built-in Tools:**
- `transferSuccessful`: Merges calls and removes assistant
- `transferCancel`: Disconnects operator and returns customer to original assistant

## Key Features

- Custom hold audio via `request-complete` message type
- Multiple department-specific configurations
- Operator interaction handling through system prompts
- Access to previous conversation context
- Voicemail and busy signal detection capabilities

## Important Limitations

- Requires `warm-transfer-experimental` mode
- Compatible only with Twilio, Vapi phone numbers, and SIP trunks
- Built-in tools cannot be removed
- Call duration restricted by `maxDurationSeconds`

## Best Practices

Keep initial messages brief and purposeful. Set timeout durations between 60-120 seconds. Configure prompts to handle voicemail detection, verify human presence, provide context, manage rejections, and complete interactions within time limits.
