# Web Widget Documentation

## Overview

The Vapi Web Widget enables developers to integrate AI chat and voice capabilities into websites through a single embeddable component. It provides a customizable floating interface supporting both text and voice conversations.

## Key Features

- **Voice Mode**: Full voice conversations with transcription capabilities
- **Chat Mode**: Text-based interactions similar to ChatGPT
- **Custom Styling**: Theme, color, and positioning customization
- **Cross-platform**: Works across modern browsers with WebRTC support

## Installation Methods

Two primary approaches exist:

1. **CDN Script**: Add a single script tag to HTML with the `<vapi-widget>` component
2. **React Component**: Install via npm/yarn and use as a React component

## Core Configuration Requirements

You must supply a public API key. Additionally, provide either an assistant ID or inline assistant configuration (voice mode only).

## Customization Options

The widget supports extensive personalization:

- **Themes**: Light or dark mode selection
- **Colors**: Base, accent, button colors customizable via hex codes
- **Size Options**: Tiny, compact, or full-width layouts
- **Text Labels**: Customizable button text and empty state messages
- **Position**: Four corner placement options

## Event Handling

Both vanilla JavaScript and React implementations support event listeners for:

- Call start/end events
- Message receipt notifications
- Error handling

## Advanced Features

- Dynamic assistant configuration
- Variable overrides for personalization
- Consent management for compliance
- Transcript display toggles

## Browser Support

Modern browsers are required: Chrome/Edge 79+, Firefox 86+, Safari 14.1+, and mobile browsers with WebRTC capabilities.

## Production Requirements

HTTPS is mandatory for production deployments, along with microphone permissions for voice functionality.
