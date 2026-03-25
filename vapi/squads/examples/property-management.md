# Property Management Routing Squad

## Overview

This documentation describes a conversational AI system designed to handle tenant inquiries through intelligent routing. The setup uses a primary "Router" assistant that classifies incoming requests and directs them to specialized team members.

## Key Components

The system operates with three distinct roles:

1. **Router Assistant** - Evaluates tenant inquiries and determines the appropriate department
2. **Maintenance Specialist** - Handles emergency repairs and maintenance-related issues
3. **Leasing Specialist** - Addresses questions about leasing agreements and rental matters

## Core Functionality

The router identifies inquiries falling into these categories: emergencies, maintenance requests, leasing questions, rental concerns, and general inquiries. Based on this classification, it transfers callers to the relevant specialist or escalates to human staff when necessary.

## Implementation Options

The documentation provides code examples across three platforms:

- **TypeScript**: Uses the Vapi Server SDK to configure and initialize the squad
- **Python**: Similar implementation leveraging the Python-based Vapi client
- **cURL**: Direct REST API approach for those preferring command-line tools

## Testing and Deployment

After configuration, teams should assign the Squad to a phone number and validate each routing pathway functions correctly. The documentation suggests reviewing additional resources on dynamic transfers for enhanced escalation capabilities.
