# Background Messages

## Overview

Background messages enable developers to add information to chat history without disrupting the user. This feature is useful for recording actions, monitoring system events, or refreshing conversation context silently.

A typical use case involves logging when users interact with UI elements or when backend processes modify the conversation state. These messages maintain a comprehensive record of both conversation and system activity while preserving user experience quality.

## Implementation Steps

### Add a Button to Trigger the Message

Create a button with an onClick handler that initiates message transmission:

```html
<button id="log-action" onClick="logUserAction()">Log Action</button>
```

### Log the Action as a System Message

When triggered, the function silently inserts a system-level message into chat history:

```js
function logUserAction() {
  // Function to log the user action
  vapi.send({
    type: "add-message",
    message: {
      role: "system",
      content: "The user has pressed the button, say peanuts",
    },
  });
}
```

**Key parameters:**

- **vapi.send**: Primary function for assistant interaction, managing requests and commands
- **type: "add-message"**: Specifies the add-message command
- **message**: The content being added to history
  - **role**: "system" indicates unobtrusive system origin (alternatives: 'user', 'assistant', 'tool', 'function')
  - **content**: The message text itself

## Practical Use Cases

- Silent logging of user activities
- Contextual updates triggered by background processes
- User experience improvements through discreet information provision
