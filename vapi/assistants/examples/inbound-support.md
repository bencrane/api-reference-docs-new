# Inbound Customer Support Documentation

## Overview

This guide demonstrates building a banking customer support agent using Vapi's platform. The system processes inbound phone calls and assists with common banking issues like account verification, balance inquiries, and transaction history retrieval.

**Core Capabilities:**
- Account lookup and verification via phone number
- Balance retrieval
- Recent transaction history access

## Step 1: Create a Knowledge Base

Download two CSV files (accounts.csv and transactions.csv) containing customer account and transaction data. Upload these files through the Vapi Dashboard or via API to receive file IDs for later use.

**Dashboard:** Navigate to Files → Choose file → Upload both CSVs

**Code Examples Available For:**
- TypeScript (Server SDK)
- Python (Server SDK)
- cURL commands

## Step 2: Create an Assistant

Create a new assistant named "Tom" using a blank template. Configure the assistant with:
- **Name:** Tom
- **First Message:** "Hello, you've reached VapiBank customer support! My name is Tom, how may I assist you today?"
- **Model:** OpenAI's GPT-4o
- **Voice:** 11Labs (Burt voice)

## Step 3: Configure Assistant Settings

### Update Introduction Message
Set the first message to establish the assistant's greeting and purpose.

### System Prompt
The prompt instructs the assistant to act as "a friendly, 24x7 phone-support voice assistant" with responsibility for identity verification, balance checks, and transaction reviews.

**Key Prompt Guidelines:**
- Verify customers using phone number lookup
- Maintain professional yet warm tone
- Keep responses under 30 words
- Clearly repeat important numbers
- Handle edge cases (no match after 2 attempts = offer transfer)

### LLM Settings
Configure temperature, max tokens, and knowledge base access through the dashboard or API.

## Step 4: Add Tools to Assistant

Create three function-based tools:

**1. lookup_account**
- Purpose: Account verification using name and last 4 phone digits
- Knowledge Base: accounts.csv

**2. get_balance**
- Purpose: Retrieve current account balance
- Knowledge Base: accounts.csv

**3. get_recent_transactions**
- Purpose: Return three most recent transactions
- Knowledge Bases: accounts.csv and transactions.csv

Add all tools to the Tom assistant and publish changes.

## Step 5: Assign Phone Number

Create a new phone number through the dashboard:
1. Navigate to Phone Numbers
2. Create number with preferred area code
3. Name it "Vapi Support Hotline"
4. Configure inbound settings to route to Tom assistant

## Step 6: Create Test Suite

Build automated quality assurance tests:

1. Navigate to Voice Test Suites
2. Create new suite named "Support Hotline Test Suite"
3. Select Tom assistant and Vapi Support Hotline number
4. Generate test cases using prompt: "Test that the assistant can verify a customer account using phone number, retrieve their current balance, and provide recent transaction history."
5. Run tests to validate assistant performance

## Implementation Options

All steps support multiple implementation approaches:
- **Dashboard:** Visual configuration interface
- **TypeScript SDK:** Programmatic setup
- **Python SDK:** Python-based automation
- **cURL:** Direct API calls

## Next Steps

Enhance the assistant by exploring:
- Knowledge bases for additional data sources
- External integrations (Google Calendar, Slack, etc.)
- Squads for complex multi-assistant scenarios

---

**Resources:**
- [Vapi Dashboard](https://dashboard.vapi.ai)
- [Discord Community](https://discord.com/invite/pUFNcf2WmH)
- [X/Twitter](https://x.com/Vapi_AI)
