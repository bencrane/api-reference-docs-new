# Zadarma SIP Integration with Vapi.ai

This documentation outlines the process for connecting a Zadarma SIP trunk to Vapi.ai to enable AI voice assistants to manage inbound and outbound calls.

## Setup Overview

The integration requires five primary steps: obtaining API credentials, configuring SIP credentials in Vapi.ai, registering a virtual number, assigning voice assistants, and establishing call forwarding through Zadarma.

## Key Configuration Steps

**API Authentication**: Users must first retrieve their private key from their Vapi.ai account's Organization Settings under the API Keys section.

**SIP Credential Registration**: The process involves submitting a curl request to Vapi.ai's credential endpoint with Zadarma-specific details, including the server address "sip.zadarma.com," the SIP number, and corresponding password.

**Virtual Number Association**: After credential creation, users register their virtual number through another API call, linking it to the credential ID obtained in the previous step.

**Voice Assistant Assignment**: Through the Vapi.ai dashboard's Build section, users select their Zadarma number and assign voice assistants for both inbound and outbound call handling.

**Call Forwarding Setup**: In Zadarma's settings, users enable the "External server (SIP URI)" option and specify the forwarding address using the format "YOUR_VIRTUAL_NUMBER@sip.vapi.ai."

This integration enables seamless call management through AI voice assistants using Zadarma's infrastructure.
