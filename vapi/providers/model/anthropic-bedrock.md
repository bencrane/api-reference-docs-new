# Anthropic Bedrock Integration Documentation

## Overview

The documentation describes how to integrate Anthropic's Claude models through AWS Bedrock with Vapi. As stated, "Amazon Bedrock is a fully managed service that provides access to foundation models from leading AI companies, including Anthropic's Claude models."

The integration enables users to "connect your own AWS Bedrock resources to power voice assistants with Claude models," maintaining control over AWS billing and data residency.

## Setup Requirements

Before configuration, users need:
- An active AWS account with Bedrock access
- Model access for Anthropic Claude models in Bedrock console
- IAM permissions to create roles and policies

## Configuration Steps

### Step 1: IAM Role Creation
Create a new IAM role in the AWS console that Vapi will assume to access Bedrock resources. The documentation recommends using a descriptive name like "VapiBedrockRole."

### Step 2: Trust Policy Configuration
Two policy options are provided:

**Basic approach** (without External ID):
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::533267069243:root"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

**Enhanced security** (with External ID):
Include a condition block requiring the External ID to match between the IAM policy and Vapi credential configuration.

### Step 3: Permissions Policy

Two permission levels are available:

**Broad access** grants permissions to all Anthropic models across regions using wildcard patterns for foundation models and inference profiles.

**Restrictive access** limits permissions to specific models and regions, allowing organizations to enforce tighter security controls.

Both policies include the actions: `bedrock:InvokeModel` and `bedrock:InvokeModelWithResponseStream`

### Step 4: Vapi Credential Creation

Use the Vapi API with curl to create credentials:

```bash
curl -X POST "https://api.vapi.ai/credential" \
  -H "Authorization: Bearer YOUR_VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "provider": "anthropic-bedrock",
    "region": "us-east-1",
    "authenticationPlan": {
      "type": "aws-sts",
      "roleArn": "arn:aws:iam::YOUR_AWS_ACCOUNT_ID:role/VapiBedrockRole",
      "externalId": "your-optional-external-id"
    }
  }'
```

Required fields include provider, region, authentication type, and role ARN.

## Key Benefits

**Security**: The service offers "data residency control with regional deployments" and "enterprise-grade security and compliance" including SOC 2 and HIPAA eligibility.

**Cost Management**: Organizations use their own AWS quotas and avoid shared resource constraints with predictable billing.

**AWS Integration**: Features include CloudWatch monitoring, IAM access control, and seamless AWS ecosystem connectivity.

## Troubleshooting Guide

| Error | Cause | Solution |
|-------|-------|----------|
| Access Denied | Trust policy doesn't authorize Vapi's AWS account | Verify Vapi's account ID (533267069243) and External ID match |
| Invalid External ID | Mismatch between trust policy and credential | Ensure exact matching of External ID values |
| Model access denied | Missing permissions or Bedrock access not enabled | Verify policy ARNs and enable model access in Bedrock console |
| Region not supported | Region lacks Bedrock availability | Use supported regions like us-east-1, us-west-2, or eu-west-1 |
