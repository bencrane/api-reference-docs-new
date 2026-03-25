# Appointment Scheduling Assistant

## Overview

This guide explains how to construct an AI-powered receptionist capable of managing appointment bookings, rescheduling, and cancellations through voice interactions.

**Core Features:**
- Real-time calendar availability verification
- Appointment modifications and terminations
- Customer identity verification
- Automated SMS/email notifications

## Prerequisites

You'll need a Vapi account and access to Google Calendar or comparable scheduling infrastructure.

## Step 1: Data Preparation (Optional)

Sample CSV files are available for download to support development:
- services.csv
- customers.csv
- appointments.csv

### Upload Process

**Via Dashboard:**
Navigate to Vapi Dashboard → Files section to upload CSVs and capture file identifiers.

**Via TypeScript SDK:**
```typescript
import { VapiClient } from "@vapi-ai/server-sdk";
import fs from "fs";

const vapi = new VapiClient({ token: process.env.VAPI_API_KEY! });

async function upload(file: string) {
  const res = await vapi.files.create({ file: fs.createReadStream(file) });
  console.log(file, res.id);
  return res.id;
}
```

**Via Python:**
```python
import requests, os

def upload(path: str):
    r = requests.post(
        "https://api.vapi.ai/file",
        headers={"Authorization": f"Bearer {os.getenv('VAPI_API_KEY')}"},
        files={"file": open(path, "rb")},
    )
    r.raise_for_status()
    return r.json()["id"]
```

## Step 2: Calendar Tool Configuration

Choose between Google Calendar integration or custom HTTP-based tools. Required functions include availability checks, booking, rescheduling, and cancellation capabilities.

## Step 3: Assistant Setup

**System Prompt Example:**
"You are an AI receptionist. Verify customers, offer booking/rescheduling/cancellation services, and confirm details. Use scheduling tools appropriately."

**TypeScript Implementation:**
```typescript
const assistant = await vapi.assistants.create({
  name: "Receptionist",
  firstMessage: "Welcome! How may I assist you today?",
  model: {
    provider: "openai",
    model: "gpt-4o",
    messages: [{ role: "system", content: systemPrompt }],
  }
});
```

## Step 4: Call Creation

**Web Call (TypeScript):**
```typescript
await vapi.calls.create({
  transport: { type: "web" },
  assistant: { assistantId: "your-assistant-id" }
});
```

**Phone Call (cURL):**
```bash
curl -X POST "https://api.vapi.ai/call" \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"assistant": {"assistantId": "ID"}, "phoneNumberId": "ID"}'
```

## Step 5: Testing

Validate the following workflows:
- New appointment booking with availability confirmation
- Rescheduling existing appointments
- Cancellation with confirmation

## Additional Resources

Consult documentation on Google Calendar integration, custom tools, structured data extraction, and web platform integration for extended functionality.
