# Rudder AI Security and Compliance Beta

Understand Rudder AI’s security model, data privacy guarantees, and compliance features for protecting your workspace and customer data.

* * *

  * __2 minute read

  * 


This guide explains Rudder AI’s security model, access controls, and data privacy policy.

## Access control

This section explains Rudder AI’s access control policy.

### Workspace isolation

Rudder AI can only access your production workspace. It **cannot access** other workspaces.

### Permissions

Rudder AI has no write access to any workspace components. All operations are read-only.

### Shared channel access

Anyone in the designated Slack channel can use Rudder AI — this includes users who may not have direct access to the connected RudderStack workspace.

Note that:

  * All interactions are visible to everyone in the channel
  * Rudder AI responds **only** in the designated shared channel, not in other channels or direct messages


### Revoke access

Contact your RudderStack representative to revoke access to Rudder AI. Once the access is revoked, Rudder AI will then be removed from your Slack channel and immediately lose access to your RudderStack workspace.

## Data privacy

This section covers details on the model provider used for Rudder AI and its data retention and PII handling policies.

### AI model provider

Rudder AI uses [Amazon Bedrock](<https://aws.amazon.com/bedrock/>) for processing your queries and generating responses.

> ![info](/docs/images/info.svg)
> 
> **No data is used** to train AI models and the conversations are **not stored**.

### PII handling

Rudder AI provides comprehensive PII masking and protection. Rudder AI has **no access** to unmasked customer PII.

Tools that access event payload data automatically mask sensitive fields before sending to the AI. Masking preserves data structure for debugging while protecting actual values.

## See more

  * [Rudder AI Overview](<https://www.rudderstack.com/docs/ai-features/rudder-ai/>)
  * [Rudder AI Capabilities](<https://www.rudderstack.com/docs/ai-features/rudder-ai/capabilities/>)
  * [Rudder AI Best Practices](<https://www.rudderstack.com/docs/ai-features/rudder-ai/best-practices/>)
  * [Rudder AI FAQ](<https://www.rudderstack.com/docs/ai-features/rudder-ai/faq/>)