# Clinic Triage with Handoff Tools

## Overview

This documentation describes a multi-assistant clinic system using handoff tools for seamless patient routing. The system features three specialized assistants working together: a triage assistant that assesses symptoms, an emergency assistant for urgent situations, and a scheduler assistant for appointment management.

**Core capabilities include:**
- Intelligent triage assessment with routing decisions
- Emergency detection triggering immediate handoffs
- Appointment scheduling with provider coordination
- Context preservation across assistant transfers

## System Architecture

The implementation consists of three specialized assistants:

### Triage Assistant
The entry point that evaluates patient needs and determines appropriate routing. This assistant greets patients, collects their name, and assesses whether they require emergency care or appointment scheduling. It uses two handoff tools for routing decisions.

### Emergency Assistant
Handles urgent medical situations with immediate care protocols. The assistant receives the patient's name via the `{{patientName}}` variable from the triage handoff, allowing personalized emergency response with a calm but urgent tone.

### Scheduler Assistant
Manages appointment booking and provider coordination. This assistant also receives the patient name through variable passing, enabling friendly, personalized scheduling service for non-emergency needs.

## Handoff Configuration

The handoff system includes:

- **`handoff_to_Emergency`**: Routes patients indicating emergencies or urgent symptoms
- **`handoff_to_Scheduler`**: Directs routine appointment scheduling requests
- **Context preservation**: Complete conversation history transfers to receiving assistants
- **Variable extraction**: Patient names automatically extract and pass to specialized assistants

## Testing Scenarios

**Routine appointment examples:**
- "I need to schedule a checkup"
- "Can I reschedule my appointment?"
- "I'd like to see Dr. Smith next week"

**Emergency examples:**
- "I'm having chest pain"
- "My child has a high fever"
- "I think I broke my arm"

## Expected Patient Flow

Patients call the triage assistant, which collects their name and assesses their needs. Based on responses, the system automatically triggers appropriate handoffs while preserving full conversation context and patient information.
