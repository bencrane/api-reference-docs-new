# Assistants Quickstart

## Overview

Build a voice assistant by defining a prompt, connecting a phone number, and initiating calls. The guide also covers adding tools for performing real-world actions.

**This quickstart covers:**
- Setting up an assistant through Dashboard or SDK
- Connecting a phone number
- Making both inbound and outbound calls

## Prerequisites

You'll need a Vapi account and corresponding API credentials.

## 1) Create an Assistant

**Via Dashboard:**
Navigate to the Vapi Dashboard, select Assistants, and choose Create Assistant. Enter your system prompt (the documentation shows an example keeping responses under 30 words). Publish your work and use the "Talk to Assistant" feature to test functionality.

**Via TypeScript SDK:**
Use the VapiClient to programmatically create an assistant with OpenAI's GPT-4o model, specifying the system message and initial greeting.

## 2) Add a Phone Number

**Dashboard approach:** Access Phone Numbers in the Dashboard, create a new number, and assign your assistant to it.

**SDK approach:** Call the phoneNumbers.create method, passing the assistant ID to link them together.

## 3) Make Your First Calls

- **Inbound:** Call your created number; the assistant responds with its configured greeting
- **Outbound:** Use the SDK's calls.create method, specifying the assistant and recipient phone number

## Recommended Next Steps

Explore adding custom tools, configuring speech parameters, implementing structured data outputs, or scaling to multi-assistant systems through squads.
