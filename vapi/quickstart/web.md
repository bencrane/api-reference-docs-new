# Web Calls Documentation

## Overview

This guide covers building voice applications across web browsers, mobile apps, and backend systems using Vapi's SDK ecosystem. It teaches developers to "Create real-time voice interfaces for web and mobile" and implement automated call systems.

## Integration Approaches

Vapi offers two primary paths:

**Client-Side Solutions** target user-facing applications, supporting browser-based assistants, real-time conversations, and mobile implementations (iOS, Android, React Native, Flutter).

**Server-Side Solutions** handle backend automation, including outbound campaigns, inbound routing, CRM integrations, and webhook processing.

## Web Voice Interfaces

### Installation Options

The Web SDK installs via npm, yarn, pnpm, or bun. Basic initialization requires:

```typescript
import Vapi from '@vapi-ai/web';
const vapi = new Vapi('YOUR_PUBLIC_API_KEY');
vapi.start('YOUR_ASSISTANT_ID');
```

The framework supports event listeners for call lifecycle and message handling, including transcript monitoring.

### Mobile Implementations

- **React Native**: Uses VapiProvider wrapper with useVapi hooks
- **Flutter**: Implements VapiClient with state management
- **iOS**: Native integration via VapiClient with delegation pattern

### Voice Widget Options

The HTML script tag approach offers the fastest deployment path. React/TypeScript implementation provides a sophisticated widget with transcript display, connection status, and speaking indicators.

## Server-Side Call Management

### SDK Installation

Six languages are supported: TypeScript, Python, Java, Ruby, C#, and Go. Each follows standard package manager installation patterns.

### Creating Assistants

Assistants require configuration including name, first message, language model selection (OpenAI, Anthropic), temperature settings, system prompts, and voice provider selection (11Labs).

### Bulk Operations

"Run automated call campaigns for sales, surveys, or notifications" by iterating through prospect lists with rate limiting to respect API constraints.

## Webhook Integration

The documentation provides implementations across all supported languages for handling:

- Status updates on call progress
- Transcript messages capturing conversation flow
- Function calls enabling dynamic backend integration

## Resources

Official SDKs are available on GitHub for all platforms. Additional resources include API reference documentation and community support channels.
