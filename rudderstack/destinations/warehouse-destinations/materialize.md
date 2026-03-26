# Materialize

Send your event data from RudderStack to Materialize.

* * *

  * __3 minute read

  * 


[Materialize](<https://materialize.com/>) is a streaming database used to process data at scale and high speeds without the cost and complexity of the traditional streaming platforms.

You can set up Materialize as a webhook destination in RudderStack to seamlessly send your event data.

## Prerequisites

Before you begin, make sure you have created a Materialize cluster and a webhook source in Materialize to ingest data from RudderStack.

### Step 1: Create Materialize cluster

To create a managed cluster in Materialize, run the following SQL command:
    
    
    CREATE CLUSTER rudderstack_cluster SIZE = '3xsmall';
    

See the Materialize documentation on [creating a cluster](<https://materialize.com/docs/sql/create-cluster/>) for more information.

### Step 2: Create shared secret

Establish a shared secret to ensure the authenticity of data sent from RudderStack to Materialize. The following command creates a shared secret that lets RudderStack authenticate each incoming request and ensure data integrity.
    
    
    CREATE SECRET rudderstack_shared_secret AS '<secret_value>';
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure to change `<secret_value>` to a unique value and store it in a secure location for later reference.

### Step 3: Set up webhook source in Materialize

Use the secret from Step 2 to [create a webhook source](<https://materialize.com/docs/sql/create-source/webhook/>) in Materialize and ingest data coming from RudderStack:
    
    
    CREATE SOURCE rudderstack_source IN CLUSTER rudderstack_cluster
      FROM WEBHOOK
        BODY FORMAT JSON
        CHECK (
          WITH (
            HEADERS,
            BODY AS request_body,
            SECRET rudderstack_shared_secret
          )
          constant_time_eq(headers->'authorization', rudderstack_shared_secret)
    );
    

> ![info](/docs/images/info.svg)
> 
> The above webhook source uses [basic authentication](<https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication#basic_authentication_scheme>).

## Set up webhook destination in RudderStack

Follow these steps to set up Materialize as a webhook destination in RudderStack:

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **Webhook**.
  2. Select the source from where you want to ingest events and click **Continue**. See [Add a source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#add-a-source>) for more information.


### Connection settings

Configure the following settings to set up Ortto as a destination in RudderStack:

  * **Webhook URL** : Define the endpoint used to dispatch the events ingested by RudderStack. The [webhook URL structure](<https://materialize.com/docs/sql/create-source/webhook/#webhook-url>) is defined as:


    
    
    https://<HOST>/api/webhook/<database>/<schema>/<src_name>
    

  * **URL Method** : Select the `POST` method from the dropdown used to send events to Materialize.

  * **Headers** : Specify the headers that are added to every RudderStack request sent to your webhook. Make sure to add the following headers:

    * `Content-Type`: `application/json`
    * `Authorization`: `<secret_value`> obtained in Step 2: Create shared secret.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/>) for more information on this feature.


## Monitor incoming data

  1. Log in to the [Materialize console](<https://console.materialize.com/>).
  2. Go to the SQL shell.
  3. Select your cluster.
  4. Use SQL queries to analyze the incoming data:


    
    
    SELECT * FROM rudderstack_source;
    

Here, `rudderstack_source` is the webhook source created in Step 3: Set up webhook source to ingest data coming from RudderStack.

> ![warning](/docs/images/warning.svg)
> 
> If you do not see any data, check the [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) tab to verify if the events are flowing through correctly.

## Parse incoming data

You can create materialized views to parse any incoming data from RudderStack, depending on your use case. An example is shown below:
    
    
    CREATE VIEW json_parsed AS
      SELECT
        (body -> '_metadata' ->> 'nodeVersion')::text AS nodeVersion,
        (body ->> 'channel')::text AS channel,
        (body ->> 'event')::text AS event,
        (body ->> 'userId')::text AS userId
      FROM rudderstack_source;
    

In the above query, `json_parsed` parses the incoming data and transforms the JSON structure into columns in your Materialize schema like `nodeVersion`, `channel`, `event`, and `userId`.

You can also use the `DISTINCT` clause to remove any duplicates received due to any issues. For more information, see the [Materialize webhook source documentation](<https://materialize.com/docs/sql/create-source/webhook/#handling-duplicated-and-partial-events>).