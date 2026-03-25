# Phone Calls - Vapi Documentation

## Overview

Vapi streamlines the process of building voice agents capable of handling inbound and outbound phone calls. The platform enables developers to launch a functional voice assistant within approximately five minutes.

## Learning Objectives

This guide covers three primary skills:
- Building an assistant via Dashboard or programmatic methods
- Configuring phone number infrastructure
- Executing initial inbound and outbound call interactions

## Requirements

- Active Vapi account (accessible at dashboard.vapi.ai)
- API key obtained from your Dashboard (required for SDK implementations)

## CLI Alternative

Developers preferring command-line interfaces can leverage the Vapi CLI for assistant creation, phone number administration, and call management directly from their terminal environment.

## Creating Your Initial Voice Assistant

### Dashboard Approach

Users navigate to the dashboard, select the customer support specialist template, and configure two key elements:

**Opening Message:**
The assistant introduces itself with a greeting such as: "Hi there, this is Alex from TechSolutions customer support."

**System Instructions:**
The system prompt establishes behavioral guidelines, emphasizing friendly communication, conversational naturalness, appropriate confidence levels, and genuine concern for customer needs.

### Programmatic Implementation

The TypeScript, Python, and cURL implementations each demonstrate creating an assistant through API calls, specifying:
- Model configuration (OpenAI's GPT-4o)
- Voice provider (ElevenLabs with specific voice ID)
- Initial greeting message
- System role definition

## Phone Number Configuration

### Dashboard Setup

The phone numbers section allows users to either create complimentary US phone numbers or import existing numbers from external providers like Twilio. Once created, users attach their assistant to the number, enabling automatic responses to incoming calls.

### API-Based Setup

Programmatic approaches use the phone-number endpoint, specifying the assistant ID and preferred area code for number allocation.

## Making Calls

### Inbound Testing

Users dial their configured phone number; the assistant answers and initiates conversation using the pre-configured opening message.

### Outbound Calling

Dashboard users enter the target number, select their assistant, and trigger the call. SDK implementations use the calls.create method with assistant ID, phone number ID, and customer phone number parameters.

### Web-Based Testing

The dashboard provides a direct calling interface requiring no phone number for initial testing.

## Recommended Next Steps

- Refine the system prompt for specific use cases
- Integrate external tools and APIs
- Experiment with alternative speech and language models
- Scale operations using REST API for programmatic assistant creation
