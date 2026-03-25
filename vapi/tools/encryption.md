# Tool Arguments Encryption Documentation

## Overview
This guide explains how to protect sensitive information through tool argument encryption. The system encrypts fields like Social Security Numbers and credit card data before transmitting them to your server.

## Key Learning Outcomes
Users will learn to:
- Set up custom credentials with encryption capabilities
- Generate RSA key pairs
- Configure which tool fields should be encrypted
- Decrypt received data on their server

## Setup Requirements
- Active Vapi account with dashboard access
- OpenSSL or equivalent for key generation
- Server capable of receiving and decrypting data

## Configuration Steps

**Step 1: Enable Encryption in Credentials**
Navigate to custom credentials and activate encryption with RSA-OAEP-256 algorithm using SPKI-PEM format.

**Step 2: Generate Key Pair**
Use OpenSSL commands to create a 2048-bit RSA private key and extract its corresponding public key in PEM format. The private key must remain secure on your server.

**Step 3: Upload Public Key**
Copy the public key contents into the Vapi dashboard's credential settings.

**Step 4: Select Tool**
Choose which Custom Tool or API Request Tool should implement encryption.

**Step 5: Configure Encryption Fields**
Link your credential to the tool and specify JSON paths for fields requiring encryption (e.g., "ssn" or "payment.cardNumber").

**Step 6: Test Configuration**
Save settings and run a test call to verify encrypted data arrives at your server as base64-encoded strings.

**Step 7: Implement Decryption**
Use TypeScript or Python code examples to decrypt received data with your private key.

## Decryption Code Examples

Both TypeScript and Python implementations use RSA-OAEP with SHA-256 hashing to decrypt base64-encoded values.

## Security Recommendations
- Avoid storing private keys in version control
- Implement periodic key rotation
- Encrypt only necessary fields
- Validate all decrypted data
- Use HTTPS for server endpoints

## Related Resources
- Custom tools documentation
- API request tools guide
- Server URL configuration
