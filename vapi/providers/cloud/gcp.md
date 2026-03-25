# GCP Cloud Storage Documentation Summary

## Overview
This documentation explains how to configure Vapi assistants to record and store chat conversations in Google Cloud Platform's Cloud Storage service.

## Key Setup Requirements

According to the page, users need to "configure the credential and bucket settings in the 'Cloud Providers' section of the 'Provider Credentials' page in the Vapi dashboard."

The documentation references two external resource guides:
- Instructions for generating service account keys for GCP
- Instructions for creating HMAC Keys for Cloud Storage

## Required Credential Settings

The configuration table specifies nine fields:

1. **Credential Reference Name** — identifier for the credential
2. **GCP Service Account Key (JSON)** — the authentication key in JSON format
3. **Bucket Name** — destination bucket identifier
4. **Bucket Region** — geographic location of the bucket
5. **Bucket Path Prefix** — optional directory path supporting dynamic templating with LiquidJS date formatting (example: `{{ "now" | date: "%Y/%m/%d" }}`)
6. **HMAC Access Key** — typically 24 characters for user accounts or 61 characters for service accounts
7. **HMAC Secret** — a 40-character base-64 encoded string

## Functionality

The system automatically uploads conversation recordings to the specified GCP bucket upon conversation completion, with optional path organization based on date patterns.
