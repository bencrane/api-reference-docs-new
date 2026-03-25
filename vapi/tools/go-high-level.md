# GoHighLevel Integration Documentation

## Overview

The GoHighLevel integration allows Vapi voice agents to interact directly with GoHighLevel calendars for appointment management. Agents can check existing contacts, create new leads, verify availability, and schedule appointments seamlessly.

## Key Capabilities

The integration provides four main tools:

1. **Get Contact** - Searches for existing contacts using email or phone
2. **Create Contact** - Adds new contacts with name, email, and phone information
3. **Check Availability** - Queries calendar open slots within specified date ranges
4. **Create Event** - Books appointments linked to specific contacts

## Prerequisites

Users need:
- An active GoHighLevel account
- Permission to manage calendar events
- Access to the Vapi Dashboard

## Setup Process

### Account Connection
Navigate to Vapi Dashboard → Providers Keys → Tools Provider → GoHighLevel, then click Connect and authorize the integration.

### Tool Creation
After authorization, create individual tools via Dashboard → Tools, selecting GoHighLevel and specifying which tools to enable. For Check Availability and Create Event tools, provide the valid calendar ID from GoHighLevel Settings → Calendars.

### Assistant Integration
Add selected tools to your assistant through the Tools tab, then publish changes.

### System Prompt Configuration
Provide instructions guiding the assistant through the booking workflow: gathering information, checking/creating contacts, verifying availability, and scheduling appointments.

## Important Requirement

"When creating an event in GoHighLevel, a `contactId` is required. Therefore, if you plan to use the **Create Event** tool, you **must** also add the **Get Contact** and **Create Contact** tools."

## Best Practices

- Check for existing contacts before creating new ones
- Always verify availability before booking
- Specify appropriate timezones for all operations
- Ensure all required fields are populated for event creation
- Include error handling for failed operations
