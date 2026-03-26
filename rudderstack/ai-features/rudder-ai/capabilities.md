# Rudder AI Key Capabilities Beta

Complete reference for Rudder AI features, enabling comprehensive interaction with your RudderStack workspace.

* * *

  * __3 minute read

  * 


Rudder AI is an AI agent that provides a range of capabilities for managing and interacting with your RudderStack workspace.

Rudder AI provides read-only access to your workspace with **no** customer PII exposure. It covers most monitoring and debugging use cases like:

  * Pipeline configuration
  * Event analysis and monitoring
  * Workspace activity monitoring
  * Data governance and quality
  * Warehouse and Reverse ETL operations
  * Transformation development and testing
  * Documentation access


> ![info](/docs/images/info.svg)
> 
> Rudder AI **cannot** create, modify, or delete any workspace configuration — all operations are read-only.

The following sections explain each use case with sample questions you can ask the assistant.

### Pipeline configuration

  * View all sources, destinations, and their connections
  * Examine transformation code and configuration
  * Browse source and destination definitions and settings
  * List all configured Tracking Plans and Data Catalog resources


**Example questions**

  * “Show me all active sources in my workspace”
  * “List the transformations connected to my Amplitude destination `<destination_name>`”
  * “List the destinations connected to the iOS source `<source_name>`”


### Event analysis and monitoring

  * Check event volumes and success rates by source
  * Examine event schemas and property structures
  * Identify duplicate or similar event names
  * Monitor destination delivery metrics including success and failure counts, timing
  * Track transformation processing performance


> ![info](/docs/images/info.svg)
> 
> The sensitive fields containing PII information in event logs and metrics are automatically masked before reaching the AI.
> 
> The masking preserves data structure for debugging while protecting actual values, ensuring the AI does not see any PII.

**Example questions**

  * “Show me event volume by source for the last 24 hours”
  * “Which destinations have delivery failures right now?”
  * “What is the success rate for events sent to Amplitude?”
  * “Show me the schema for the `Order Completed` event”


### Workspace activity monitoring

  * Review configuration changes made by workspace users, including usernames and actions
  * View [Audit Logs](<https://www.rudderstack.com/docs/dashboard-guides/audit-logs/>) for compliance and troubleshooting


**Example questions**

  * “Who modified the transformation `<transformation_name>` last week?”
  * “Show me recent changes to the web source `<source_name>` configuration”


### Data governance and quality

  * Review Tracking Plan compliance metrics
  * Browse your Data Catalog including events and properties
  * Check Tracking Plan coverage across sources
  * View validation statistics


**Example questions**

  * “What is our Tracking Plan compliance rate?”
  * “Show me all events in the Data Catalog”
  * “List all sources that are not connected to any Tracking Plan”


### Warehouse and Reverse ETL operations

  * Check warehouse sync status and history
  * View detailed table-level sync information
  * Monitor Reverse ETL sync performance
  * Track data freshness and upload schedules


**Example questions**

  * “What is the status of our warehouse syncs?”
  * “When was the last successful sync to Snowflake?”


### Transformation development and testing

  * Test new transformation code with sample events
  * Test existing transformations against new event samples
  * Browse pre-built transformation templates
  * View transformation processing metrics


**Example questions**

  * “Test this transformation code with a sample Order Completed event”
  * “Show me the transformation templates for filtering events”


### Documentation access

  * Search RudderStack documentation and get AI-powered answers to your questions
  * Access integration guides and best practices


**Example questions**

  * “Which sources does the Amplitude destination support?”
  * “Which event types are supported for the HubSpot destination?”
  * “Does Profiles work on Databricks?”


## See more

  * [Rudder AI Overview](<https://www.rudderstack.com/docs/ai-features/rudder-ai/>)
  * [Rudder AI Security and Compliance](<https://www.rudderstack.com/docs/ai-features/rudder-ai/security/>)
  * [Rudder AI FAQ](<https://www.rudderstack.com/docs/ai-features/rudder-ai/faq/>)
  * [Rudder AI Best Practices](<https://www.rudderstack.com/docs/ai-features/rudder-ai/best-practices/>)