# Google Calendar Integration Guide

## Overview

The Google Calendar integration enables Vapi assistants to perform two key functions: creating calendar events through voice commands and checking calendar availability for scheduling purposes. This allows real-time appointment management during phone conversations.

## Prerequisites

Users need three things before implementation:
- An active Google Calendar account
- Access to the Vapi Dashboard
- A previously created Vapi assistant

## Setup Process

### Step 1: Account Connection

Begin by linking your Google Calendar to Vapi through the Dashboard's Integrations section. The authorization process requests permission to "create events and check availability" on your calendar.

### Step 2: Tool Creation

After authorization, create tools via the Dashboard's Tools page. You can configure:
- **Google Calendar Create Event Tool** — for scheduling appointments
- **Google Calendar Check Availability Tool** — for viewing open time slots

Descriptions are particularly important here, as they guide the AI model on when to invoke each tool.

### Step 3: Assistant Integration

Add your selected tools to your assistant through the Tools tab on the Assistants page, then publish your changes.

## Tool Field Specifications

**Create Event Tool** requires:
- Summary (event title)
- Start/end datetime
- Attendee email addresses (optional)
- Timezone and calendar ID

**Availability Check Tool** requires:
- Start/end datetime range
- Timezone and calendar ID

All datetime values must follow ISO 8601 format.

## Implementation Recommendations

The documentation emphasizes clear system instructions, proper timezone handling, complete field population, and checking availability before scheduling to prevent conflicts.

## Additional Resources

- [Discord community support](https://discord.gg/pUFNcf2WmH)
- [API reference documentation](/api-reference/tools/create)
