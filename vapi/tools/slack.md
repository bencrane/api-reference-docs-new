# Slack Integration Documentation

## Overview
This guide covers connecting a Vapi assistant to Slack for sending messages during phone calls. The integration enables team notifications and information sharing directly through Slack channels.

## Prerequisites
You'll need:
- An active Slack workspace
- Access to the Vapi Dashboard
- An existing Vapi assistant
- A designated Slack channel for message delivery

## Setup Process

### Connecting Slack Account
Navigate to the Vapi Dashboard's provider keys section, locate the Slack tool option, and click "Connect" to authorize workspace access through a popup prompt.

### Creating the Slack Tool
In the Tools section, create a new tool by selecting Slack and choosing the Send Message option. The description field is particularly important—it should clearly specify the target channel and conditions for tool usage, such as "Send urgent notifications to the #customer-support channel."

### Adding to Your Assistant
Go to your assistant's Functions tab, select the Slack tool from the tools dropdown, and publish your changes.

## Tool Details
The Slack Send Message Tool transmits messages to channels specified in its configuration description. The bot must be added to target channels beforehand. Channel names should follow the "#channel-name" format.

## Best Practices
- Verify correct channel names before sending
- Keep messages clear and professional
- Include fallback responses for failures
- Confirm with users before sending notifications
- Ensure bot channel membership

## Resources
The documentation includes links to the Discord community and API reference documentation for additional support.
