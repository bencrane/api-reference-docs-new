# Clinic Triage and Scheduling Workflow Documentation

## Overview

This documentation describes building an AI-powered clinic receptionist system using Vapi workflows that handles patient triage, appointment scheduling, and emergency routing with medical protocol compliance.

## Key Capabilities

The workflow system provides:

- Medical triage assessment with symptom-based routing
- Emergency detection with global safety protocols
- Provider scheduling with urgency prioritization
- Prescription refill processing with safety checks

## Implementation Steps

### 1. Knowledge Base Setup

Four CSV files are required for the system:
- **patients.csv** - Patient records
- **providers.csv** - Healthcare provider information
- **triage_protocols.csv** - Medical assessment guidelines
- **appointments.csv** - Scheduling availability

These files upload through the Vapi dashboard Files section or via API, generating file IDs for tool creation.

### 2. Tool Creation

Three primary tools support the workflow:

**Patient Lookup Tool** - Retrieves patient medical records using patient ID, date of birth, or name for verification purposes.

**Triage Assessment Tool** - Evaluates symptoms, onset timing, and severity levels to determine urgency classification following medical protocols.

**Appointment Scheduling Tool** - Books patient appointments based on availability and urgency level.

### 3. Workflow Architecture

The workflow uses conversation nodes with conditional branching:

- **Initial greeting** identifies the caller's purpose (emergency, triage, appointment, prescription, general)
- **Patient verification** collects identification information
- **Purpose-based routing** directs to appropriate workflow branch
- **Global emergency detection** monitors for red-flag symptoms throughout

### 4. Call Purpose Routing

**Emergency Path**: Direct 911 for life-threatening situations; transfer to triage nurse for urgent medical needs.

**Medical Triage Path**: Collect symptoms, assess severity, determine urgency level, and route to appropriate care.

**Appointment Path**: Identify appointment type, check provider availability, present options, and confirm booking.

### 5. Phone Configuration

The system requires configuring phone numbers with:
- Workflow assignment
- Call recording for medical documentation
- Voicemail detection for after-hours
- Emergency transfer capabilities
- Maximum call duration settings

## Integration Considerations

The example uses JSONPlaceholder for demonstration. Production implementations require:

**EHR Systems**: Epic on FHIR, Cerner SMART on FHIR, or Allscripts APIs

**Scheduling**: Epic MyChart, Cerner PowerChart, or athenahealth APIs

**Medical Decision Support**: IBM Watson Health, Microsoft Healthcare Bot, or Infermedica

## Compliance Requirements

All healthcare integrations must maintain HIPAA compliance. The system includes call recording, secure data handling, and privacy protocol adherence for protected health information.

## Conclusion

The workflow automates clinic receptionist functions while maintaining medical safety standards and appropriate emergency response capabilities. Integration with actual healthcare systems requires proper API configuration and regulatory compliance implementation.
