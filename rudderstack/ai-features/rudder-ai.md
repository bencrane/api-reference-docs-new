# Rudder AI Beta

Leverage RudderStack’s AI-powered agent to manage and interact with your RudderStack workspace via Slack.

* * *

  * __2 minute read

  * 


**Rudder AI** is an AI agent that helps you maintain and interact with your RudderStack workspace. It has a Slack integration, allowing you to directly access the agent from your Slack channel and converse with your workspace using natural language — support for other platforms like RudderStack dashboard, Microsoft Teams, etc. is coming soon.

> ![success](/docs/images/tick.svg)
> 
> Rudder AI helps you with a broad range of tasks, like monitoring pipeline health, debugging issues, analyzing data quality, getting recommendations for your workspace configuration, and more.

## Key features

  * **Monitor pipeline health** : Check event volumes, success rates, and delivery metrics across sources and destinations
  * **Debug issues faster** : Analyze failed events and transformation errors with masked PII protection
  * **Access configuration** : View sources, destinations, transformations, and Tracking Plans
  * **Query documentation** : Get AI-powered answers to RudderStack product questions


## Operating mode

Rudder AI operates with read-only access to your workspace and complete PII protection. This mode handles most of your monitoring and debugging use cases.

## Access and permissions

Rudder AI **cannot** modify sources, destinations, or other workspace configuration. All operations are read-only.

Also, note that:

  * Rudder AI responds only in your designated Slack channel — you cannot use it in direct messages or other channels
  * Rudder AI works within your production workspace only


> ![announcement](/docs/images/announcement.svg)
> 
> Contact your RudderStack representative to opt-out of Rudder AI.

## Data privacy

Rudder AI uses [Amazon Bedrock](<https://aws.amazon.com/bedrock/>) for AI processing. Your data is never used to train AI models, and the conversations are not stored.

Note that customer PII is automatically masked before reaching the AI. The masking preserves data structure for debugging while protecting actual values, ensuring the AI does not see any PII.

## Help and support

Make sure to provide feedback on Rudder AI’s responses by clicking 👍 or 👎 on the response.

You can also contact your RudderStack representative to share feedback about the assistant or suggest features you would like to see added or improved.

## Next steps

  * [Understand Rudder AI’s key capabilities](<https://www.rudderstack.com/docs/ai-features/rudder-ai/capabilities/>)
  * [Learn about security and compliance in Rudder AI](<https://www.rudderstack.com/docs/ai-features/rudder-ai/security/>)