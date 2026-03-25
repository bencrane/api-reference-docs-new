# SIP Introduction

## Overview

This documentation explains how to configure SIP calls with Vapi assistants using any SIP client or softphone. The process involves creating an assistant, assigning it a SIP phone number, and initiating calls through a SIP URI. Additionally, you can pass template variables using SIP headers.

## Setup Steps

### Step 1: Create an Assistant

Use the `POST /assistant` endpoint to create an assistant. This process mirrors creating assistants for other transport methods.

Example payload:
```json
{
  "name": "My SIP Assistant",
  "firstMessage": "Hello {{first_name}}, you've reached me over SIP."
}
```

### Step 2: Create a SIP Phone Number

Use the `POST /phone-number` endpoint to create a SIP phone number.

Example payload:
```json
{
  "provider": "vapi",
  "sipUri": "sip:your_unique_user_name@sip.vapi.ai",
  "assistantId": "your_assistant_id"
}
```

**Note:** The SIP URI format is `sip:username@sip.vapi.ai`, where you can select any username.

### Step 3: Start a SIP Call

Use any SIP softphone application (such as Zoiper or Linphone) to dial your SIP URI. The assistant will automatically answer incoming calls without requiring authentication or SIP registration.

### Step 4: Send SIP Headers for Template Variables

Pass custom SIP headers to populate template variables. For instance, to fill a `first_name` variable, include:

```
x-first_name: John
```

Header names are case-insensitive across variations.

### Step 5: Use Custom Assistant per Call

Configure a different assistant for each SIP call by setting `assistantId` to `null` and providing your server's URL via the `PATCH /phone-number/:id` endpoint:

```json
{
  "assistantId": null,
  "serverUrl": "https://your_server_url"
}
```

Your server will receive an `assistant-request` event for each incoming call.
