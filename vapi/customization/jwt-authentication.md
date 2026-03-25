# JWT Authentication

## Overview
This documentation explains JWT (JSON Web Token) authentication and guides users through generating tokens and using them to secure API requests.

## Prerequisites
Users need:
- An environment supporting JWT generation and API calls
- An account with a JWT-requiring service
- Environment variables configured with credentials (organization ID and private key from Vapi portal)

## Token Generation Process

The documentation outlines four steps:

1. **Define the Payload** - Include data like `orgId` in the token
2. **Retrieve the Private Key** - Obtain from Vapi and store securely in environment variables
3. **Set Token Options** - Configure expiration time and other parameters
4. **Generate the Token** - Use JWT libraries to create the token

## Token Scopes

Tokens can be `private` or `public`, determining accessible endpoints. The documentation notes that "the only publicly scoped API endpoint is https://api.vapi.ai/call/web, which is used for Web Call creation. All other endpoints are privately scoped."

### Private Token Example
```js
const payload = {
  orgId: process.env.ORG_ID,
  token: { tag: "private" },
};
const key = process.env.PRIVATE_KEY;
const options = { expiresIn: "1h" };
const token = generateJWT(payload, key, options);
```

### Public Token Example
```js
const payload = {
  orgId: process.env.ORG_ID,
  token: {
    tag: "public",
    restrictions: {
      enabled: true,
      allowedOrigins: ["https://example.vapi.ai"],
      allowedAssistantIds: ["1cbf8c70-5fd7-4f61-a220-376ab35be1b0"],
      allowTransientAssistant: false,
    },
  },
};
```

## Making Authenticated Requests

### Server-Side Example
```js
async function getAssistants() {
  const response = await fetch("https://api.vapi.ai/assistant", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  });
  const data = await response.json();
  console.log(data);
}
```

### Web Client Example
```
import Vapi from '@vapi-ai/web';
const vapi = new Vapi('your-jwt-token');
vapi.start('your-assistant-id');
```
