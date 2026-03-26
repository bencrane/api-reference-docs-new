# Rudder AI Best Practices Beta

Learn best practices for using Rudder AI effectively, including onboarding strategies, usage patterns, and security recommendations.

* * *

  * __2 minute read

  * 


This guide provides best practices for using Rudder AI effectively and securely.

## Usage

  * Test the assistant with read-only queries to familiarize yourself with its responses
  * Use threads for complex issues to maintain conversation context
  * Provide feedback (by clicking 👍 or 👎 on the response) to help improve the assistant’s accuracy
  * Report any security or privacy concerns immediately


### Be specific

Ask clear, specific questions with details and context:

  * **Good** : “Show me event volume for the iOS source in the last 24 hours”
  * **Less effective** : “How are my events being sent?”


### Provide context

Include relevant details:

  * **Good** : “Why are `Order Completed` events failing to reach Amplitude with error code `400`?”
  * **Less effective** : “Why are my events failing?”


### Use natural language

You do not need special syntax:

  * **Good** : “What transformations are connected to my web source?”
  * **Also good** : “List all transformations for the web source”


### Upload supporting materials

Include screenshots or error logs when troubleshooting issues:

  * Take a screenshot of the error or issue
  * Upload the image to Slack
  * Mention the assistant and ask about the error
  * Rudder AI will analyze the image and provide guidance


## Security considerations

This section covers security considerations for using Rudder AI securely.

### Monitor channel

Rudder AI is deployed in your designated Slack channel and is accessible to all members present in it.

Make sure to periodically monitor channel membership and remove users who no longer need access.

## Limitations

Understand the following limitations to use Rudder AI effectively:

  * Rudder AI **cannot** modify sources, destinations, transformations, or any other workspace configuration — all operations are read-only
  * Rudder AI’s scope is limited to your production workspace
  * Rudder AI can only respond in the designated Slack channel
  * Anyone in the channel can use Rudder AI


## See more

  * [Rudder AI Overview](<https://www.rudderstack.com/docs/ai-features/rudder-ai/>)
  * [Rudder AI Capabilities](<https://www.rudderstack.com/docs/ai-features/rudder-ai/capabilities/>)
  * [Rudder AI Security and Compliance](<https://www.rudderstack.com/docs/ai-features/rudder-ai/security/>)
  * [Rudder AI FAQ](<https://www.rudderstack.com/docs/ai-features/rudder-ai/faq/>)