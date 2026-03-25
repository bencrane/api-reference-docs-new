# Authentication
Source: https://developers.deepgram.com/reference/authentication

Authenticating requests made to the Deepgram API

If you need to create short lived tokens for /Listen, /Speak, or /Read API requests, you can use the Token-based Auth API.

Send requests to the API with an Authorization header that references your project's API Key:

```
Authorization: Token <YOUR_DEEPGRAM_API_KEY>
```

You can create a Deepgram API Key in the Deepgram Console. You must create your first API Key using the Console.

All API requests must be made over HTTPS. Calls made over plain HTTP will fail. API requests made without authentication will also fail.

## Security Scheme

- **Type:** API Key
- **Header parameter name:** Authorization
