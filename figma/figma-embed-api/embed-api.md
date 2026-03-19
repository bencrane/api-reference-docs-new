# Figma Embed API

The Embed API enables interaction with embedded Figma prototypes through message passing and event handling across iframe boundaries.

Source: https://developers.figma.com/docs/embeds/embed-api/

## Setup Requirements

To implement the Embed API, you must:

1. **Create an OAuth application** at Figma's developer portal with name, website, and logo
2. **Obtain a client ID** from your OAuth app configuration
3. **Register embed origins** via the Embed API settings to whitelist domains
4. **Add the client-id parameter** to the iframe src URL

## Embed URL Format

```
https://embed.figma.com/proto/{FILE_ID}/{FILE_NAME}
  ?node-id={NODE_ID}
  &embed-host={DOMAIN}
  &client-id={CLIENT_ID}
```

**Important:** The second argument for the postMessage method (the target origin) must always be `https://www.figma.com`.

## Message Types (Controlling Prototypes)

| Type | Purpose | Required Data |
|------|---------|---------------|
| `NAVIGATE_TO_FRAME_AND_CLOSE_OVERLAYS` | Navigate to frame and close overlays | `nodeId` |
| `NAVIGATE_FORWARD` | Move to next frame | None |
| `NAVIGATE_BACKWARD` | Move to previous frame | None |
| `CHANGE_COMPONENT_STATE` | Change component variant | `nodeId`, `newVariantId` |
| `RESTART` | Reset to starting node | None |

## Event Types (From Prototype)

| Event | Description |
|-------|-------------|
| `MOUSE_PRESS_OR_RELEASE` | Click tracking with position data |
| `PRESENTED_NODE_CHANGED` | Frame/overlay navigation events |
| `INITIAL_LOAD` | Prototype finished loading |
| `NEW_STATE` | Component instance state changed |
| `REQUEST_CLOSE` | User pressed spacebar |
| `LOGIN_SCREEN_SHOWN` | Authentication required |
| `PASSWORD_SCREEN_SHOWN` | Password entry needed |

## Code Examples

### Sending Messages to Prototype

```javascript
// Restart the prototype
iframe.contentWindow.postMessage(
  { type: "RESTART" },
  "https://www.figma.com"
);

// Navigate to a specific frame
iframe.contentWindow.postMessage(
  {
    type: "NAVIGATE_TO_FRAME_AND_CLOSE_OVERLAYS",
    nodeId: "123:456"
  },
  "https://www.figma.com"
);

// Change component state
iframe.contentWindow.postMessage(
  {
    type: "CHANGE_COMPONENT_STATE",
    nodeId: "123:456",
    newVariantId: "789:012"
  },
  "https://www.figma.com"
);
```

### Listening for Events

```javascript
window.addEventListener("message", (event) => {
  // Always verify the origin
  if (event.origin !== "https://www.figma.com") {
    return;
  }

  switch (event.data.type) {
    case "INITIAL_LOAD":
      console.log("Prototype loaded");
      break;
    case "PRESENTED_NODE_CHANGED":
      console.log("Navigated to:", event.data.nodeId);
      break;
    case "MOUSE_PRESS_OR_RELEASE":
      console.log("Click at:", event.data.x, event.data.y);
      break;
    case "NEW_STATE":
      console.log("Component state changed");
      break;
  }
});
```
