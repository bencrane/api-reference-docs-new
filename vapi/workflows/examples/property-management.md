# Property Management Call Routing Workflow Documentation

## Overview

This documentation describes building an intelligent call routing system for property management using Vapi's Workflow API. The system dynamically routes calls based on tenant verification, inquiry classification, and agent availability.

## Key Capabilities

The workflow handles:
- Tenant status verification and prioritization
- Inquiry type classification (emergency, maintenance, lease, rent, general)
- Real-time agent availability checking
- Emergency escalation with priority queuing

## Quick Start

A complete workflow can be created via cURL with conversation nodes for initial greeting and emergency handling, plus transfer nodes. The basic structure includes:

1. **Initial Greeting Node** - Extracts caller phone and inquiry type using GPT-4
2. **Emergency Handling Node** - Routes urgent maintenance situations
3. **Transfer Node** - Routes to appropriate departments

## Implementation Steps

### 1. Create the Workflow
Start in the Vapi dashboard under Workflows, create a new workflow named "Property Management Call Router," and configure the initial greeting conversation node with appropriate prompts and variable extraction schemas.

### 2. Tenant Verification
Add an API Request node that:
- Calls your property management system
- Accepts phone number and inquiry type
- Returns tenant status, property address, and account standing
- Includes error handling with fallback to general queue

### 3. Emergency Routing
Implement dedicated emergency handling with:
- Rapid routing to emergency maintenance teams
- Priority-based call queuing
- Context-rich transfers including property details

### 4. Inquiry-Based Routing
Create separate routing branches for:
- **Maintenance**: Routes to maintenance coordinator
- **Leasing**: Routes to leasing office
- **Billing**: Routes to billing department
- **General**: Routes to main office queue

### 5. Agent Availability
Before transfers, check agent availability via API to:
- Identify available agents by department
- Calculate estimated wait times
- Offer callback options when queues are full

### 6. Transfer Context
Each transfer includes rich contextual information such as tenant name, property address, account status, and inquiry history.

### 7. Error Handling
Implement fallback routing for API failures, unavailable agents, and system errors, with voicemail options as last resort.

### 8. Testing
Test various scenarios including emergency calls, maintenance requests, leasing inquiries, and unrecognized callers to verify correct routing.

## API Integration Examples

**Tenant Lookup Response Structure:**
```
Returns tenant ID, name, status, property address, and account standing
```

**Agent Availability Check:**
```
Returns available agents, queue length, and estimated wait times by department
```

**Emergency Routing:**
```
Returns emergency destination phone, agent assignment, and ticket ID
```

## Advanced Features

- **Priority-Based Routing**: Commercial tenants and emergency situations receive critical priority
- **Business Hours Logic**: Different routing for weekday/weekend and after-hours scenarios
- **Queue Management**: Intelligent handling of full queues with callback scheduling

## Next Steps

Consider implementing customer support escalation systems, workflow analytics tracking, integration templates for property management platforms, and advanced routing with multiple conditions.
