# Structured Outputs Examples - Documentation Summary

This page provides production-ready templates for five common business use cases with complete JSON schemas and example outputs.

## Key Use Cases Covered

**Healthcare Appointment Booking**: Extracts patient demographics, medical history, appointment preferences, and urgency levels. Required fields include patient name, phone, appointment type, and department.

**E-commerce Order Processing**: Captures customer information, ordered items with customization options, shipping addresses, payment methods, and promotional codes for sales call transcription.

**Real Estate Lead Qualification**: Qualifies prospects by collecting contact details, property preferences, budget ranges, desired features, timeline, and current housing situation to assign follow-up priority.

**Insurance Claim Intake**: Documents policyholder information, incident details, damage assessments, injured parties, witness information, and available documentation for claim processing.

**Financial Services Applications**: Processes loan applications including personal data, employment verification, financial history, loan specifications, and co-applicant information.

## Best Practices Highlighted

The guide emphasizes four key principles: organizing schemas into reusable components, prioritizing essential fields while keeping detailed fields optional, providing contextual descriptions for AI clarity, and balancing validation constraints without excessive restrictions.

## Testing & Monitoring

Recommended testing includes scenarios with complete information, partial data, ambiguous details, edge cases, and real conversation samples. Production monitoring should track extraction success rates, processing time, token usage, validation failures, and frequently missing fields.

## Data Delivery Format

Structured outputs arrive via webhook payload containing call artifacts with extracted data organized by output ID, or retrievable through API responses including call status and timestamp information.
