# Web Snippet: Vapi Voice Widget Integration

## Overview

The Vapi Voice Widget enables developers to integrate voice assistant capabilities into websites. As the documentation states, this tool allows visitors to "engage with a voice assistant for support and interaction, offering a smooth and contemporary way to connect."

## Implementation Methods

### HTML Script Tag Approach

The quickest setup involves inserting a script directly into your webpage. You'll need to substitute your assistant ID and public API key into the provided template. The script dynamically loads the Vapi SDK and initializes the voice widget with your specified configuration.

### React/TypeScript Implementation

For React projects, install the SDK via npm, yarn, pnpm, or bun, then create a component that manages call states, transcripts, and user interactions. The component includes event listeners for call lifecycle management and displays a fixed widget in the bottom-right corner.

## Key Features

**State Management**: The React implementation tracks connection status, speaking status, and conversation transcripts in real-time.

**Event Listeners**: The widget responds to call-start, call-end, speech-start, speech-end, message, and error events for comprehensive functionality.

**UI Elements**: An inactive state shows a microphone button; the active state displays a conversation panel with transcript history and call controls.

## Customization Options

Developers can modify button styles, panel appearances, and positioning. The documentation provides examples using gradient backgrounds and custom shadow effects to match brand aesthetics.

## Practical Use Cases

Two integration examples demonstrate real-world applications: e-commerce support scenarios and healthcare appointment scheduling, each with customized greetings and voice provider settings.
