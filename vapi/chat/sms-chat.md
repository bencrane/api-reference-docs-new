# SMS Chat Documentation

## Overview
The SMS chat feature enables customers to communicate with Vapi assistants through text messaging, leveraging familiar channels for AI-powered support.

## Key Requirements
To implement SMS chat, you need:
- A Vapi account with an existing assistant
- A "10DLC-approved Twilio phone number (required for assistant responses)"
- Basic phone number management knowledge

## Critical Limitation
"Only customers can initiate conversations - assistants cannot send the first message."

## Setup Process
The implementation involves three main steps: importing your Twilio number into Vapi (where SMS is enabled automatically), assigning the number to your chosen assistant, and sending a test message to verify functionality.

## How Sessions Work
When customers text your number, Vapi automatically creates a chat session. The system maintains conversation context throughout the exchange and delivers responses via SMS. Sessions automatically expire after 24 hours of inactivity, creating fresh sessions for subsequent conversations.

## Current Constraints
The feature currently supports only Twilio and requires 10DLC approval. Additional SMS providers aren't yet available. Assistants cannot initiate outbound messages to customers.

## Optimization Tip
For optimal results, configure your assistant with "concise responses and clear conversation flows" since SMS users expect rapid, direct communication.
