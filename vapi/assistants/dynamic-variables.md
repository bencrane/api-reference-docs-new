# Variables

## Overview

The documentation explains how to personalize assistant messages using dynamic variables marked with double curly braces like `{{name}}`. Values are set through API requests using `assistantOverrides`, not the dashboard.

## Setting Dynamic Variables in Phone Calls

To implement dynamic variables, follow two steps:

**Step 1 - Prepare Your Request:**
Create a JSON payload including your `assistantId`, `assistantOverrides` with `variableValues`, the customer's phone number, and your `phoneNumberId`.

**Step 2 - Send the Request:**
Post your JSON to the `/call/phone` endpoint with the structured data containing variable assignments.

## Default Variables Available

Several variables auto-populate without manual setup:

- Time-based: `{{now}}`, `{{date}}`, `{{time}}`, `{{month}}`, `{{day}}`, `{{year}}`
- Customer info: `{{customer.number}}`, `{{customer.X}}`
- Transport details: `{{transport.conversationType}}`

## Advanced Date and Time Formatting

"You can use advanced date and time formatting in any prompt or message" with LiquidJS filters. Example format: `{{"now" | date: "%A, %B %d, %Y, %I:%M %p", "America/Los_Angeles"}}`

Common format strings include `%Y-%m-%d` for dates and `%H:%M` for 24-hour time.

## Dashboard Implementation

Include variables in prompts using double curly braces. "When you start a call, you must provide a value for each variable" through API or SDK configuration.

## Conversation Type Adaptation

Use `{{transport.conversationType}}` to differentiate behavior between chat and voice interactions, adjusting formatting and response style accordingly.

## Data Retention Considerations

With HIPAA or Zero Data Retention enabled, variable values are processed during calls but not stored afterward, ensuring privacy compliance.
