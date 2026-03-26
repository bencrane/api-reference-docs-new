# Rudder AI FAQ Beta

Answers to frequently asked questions about Rudder AI — including access control, data privacy, and operational capabilities.

* * *

  * __3 minute read

  * 


This guide answers common questions about Rudder AI.

## General questions

#### What is Rudder AI?

Rudder AI is an AI agent that helps you manage and interact with your RudderStack workspace. It has a Slack integration so you can access the agent from Slack and converse with your workspace using natural language.

> ![success](/docs/images/tick.svg)
> 
> ` Rudder AI can help you with a broad range of tasks, like monitoring pipeline health, debugging issues, analyzing data quality, getting recommendations for your workspace configuration, etc.

See the following guides to learn more about Rudder AI, its capabilities, usage, and best practices:

  * [Rudder AI Overview](<https://www.rudderstack.com/docs/ai-features/rudder-ai/>)
  * [Rudder AI Capabilities](<https://www.rudderstack.com/docs/ai-features/rudder-ai/capabilities/>)
  * [Rudder AI Best Practices](<https://www.rudderstack.com/docs/ai-features/rudder-ai/best-practices/>)


## Access and permissions

#### Which data can Rudder AI access?

Rudder AI can access configuration, masked PII, and metrics corresponding to your production workspace.

#### Who can use Rudder AI?

Anyone in the Slack channel can interact with Rudder AI.

#### Can I use Rudder AI in direct messages?

No — Rudder AI only responds in the designated Slack channel. You cannot use it in direct messages or other channels.

#### How do I control what Rudder AI can access?

Rudder AI works in your primary production workspace. Contact your RudderStack representative for any of the following:

  * Disable Rudder AI for you
  * Change the workspace to a different one


## Capabilities

#### Can Rudder AI make changes to my production pipelines?

No — Rudder AI **cannot** make any changes to your production pipelines. All operations are read-only.

#### Can Rudder AI create new sources or destinations?

No — Rudder AI cannot create, modify, or delete sources, destinations, transformations, or any other workspace configuration. All operations are read-only.

#### Does Rudder AI work with all RudderStack features?

Rudder AI supports most RudderStack features including sources, destinations, transformations, Tracking Plans, Data Catalog, warehouse syncs, and Reverse ETL

You can ask Rudder AI directly about specific capabilities.

## Data privacy

#### Where is my data processed?

Rudder AI uses Amazon Bedrock to process your data and generate responses

Note that the data is neither stored by the provider, nor used for training.

#### Is my data used to train Rudder AI’s AI models?

No — your data is never used to train AI models.

#### How long is the conversation data stored?

The conversation data is not stored by the AI provider — only your Slack workspace retains the conversation history.

## Customization

#### Can I restrict specific Rudder AI capabilities?

Yes — you can contact your RudderStack representative to disable specific tool categories at deployment time. This lets you customize permissions based on your requirements.

#### Can I change which Slack channel Rudder AI uses?

Yes — you can contact your RudderStack representative to change the designated Slack channel. The RudderStack team will then redeploy Rudder AI to the new channel.

#### Can I have multiple Rudder AI instances for different teams?

Yes — you can contact your RudderStack representative to discuss multi-channel or multi-workspace deployments.

## Troubleshooting

#### The assistant gives incorrect information. What should I do?

Use the thumbs down (👎) button on the response to provide feedback. You can also ask Rudder AI to clarify or provide sources for its information.

## Help and support

#### Who do I contact for support?

  * **For the assistant itself** : Ask Rudder AI directly, as it can often diagnose common issues
  * **For deployment or configuration** : Contact your RudderStack representative
  * **For urgent production issues** : Use the standard support channels


#### How do I provide feedback on Rudder AI?

Use the thumbs up (👍) or thumbs down (👎) buttons on Rudder AI’s responses based on whether you found the response helpful or not.

You can also share feedback with your RudderStack representative about features you would like to see added or improved.