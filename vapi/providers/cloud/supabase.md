# Supabase S3 Storage

## Overview

The documentation explains that "assistants can be configured to record chat conversations and upload the recordings to a bucket in Supabase Storage when the conversation ends."

Configuration requires setup through the Vapi dashboard's "Cloud Providers" section under "Provider Credentials." The guide references [Supabase's authentication documentation](https://supabase.com/docs/guides/storage/s3/authentication) for generating necessary tokens and locating your endpoint and region.

## Configuration Parameters

The system requires six credential settings:

- **Bucket Name**: Specifies which Supabase Storage bucket receives the recordings
- **Storage Region**: Identifies the Supabase project's region
- **Storage Endpoint**: The upload destination URL for recordings
- **Bucket Path Prefix**: Optional prefix supporting LiquidJS Date format templating (e.g., `{{ "now" | date: "%Y/%m/%d" }}` for YYYY/MM/DD structure)
- **Storage Access Key ID**: Authentication credential for Supabase Storage
- **Storage Secret Access Key**: Secret key paired with the access key ID

An example configuration screenshot is referenced but not displayed in text format.
