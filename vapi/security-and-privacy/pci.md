# PCI Compliance Documentation Summary

## Overview
Vapi provides PCI DSS compliance features to help organizations securely handle payment card data through their voice assistant platform without compromising service quality.

## Key Security Features

**Default Settings**: Vapi enables call recording, logging, and transcription by default. When PCI compliance is activated, users can optionally store data in compliant cloud solutions or receive transcripts via webhooks.

**Data Handling**: As noted in the documentation, "If no cloud storage or webhook is specified, recordings and transcripts are permanently deleted to avoid retaining sensitive data."

## Implementation Approach

Organizations can enable PCI compliance through their assistant settings and configure three main options:
- Select PCI-compliant model, voice, and transcriber options
- Optional cloud storage (AWS S3, Azure, Google Cloud, Cloudflare R2)
- Optional webhook configuration for transcripts

## Advanced Strategy: Squads

The documentation illustrates a sophisticated approach using "squads" that allow selective recording control. This enables organizations to record non-sensitive call portions while disabling all artifacts during payment data collection phases through assistant handoffs.

## Compliance Flexibility

Users can enable both HIPAA and PCI simultaneously, with the most restrictive requirements applying. The system allows toggling between default and compliant modes as business needs change.

## Support
Contact: security@vapi.ai
