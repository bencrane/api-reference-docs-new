# Snowflake Streaming Destination

Sync real-time data streams from RudderStack to Snowflake using the Snowpipe Streaming API.

Available Plans

  * starter
  * growth
  * enterprise


* * *

  *  __7 minute read

  * 


> ![announcement](/docs/images/announcement.svg)
> 
> **The Snowflake Streaming destination is now Generally Available for Starter, Growth and Enterprise plans**
> 
>   * [Enterprise](<https://rudderstack.com/pricing/enterprise>) customers get Snowflake Streaming as a part of their plan
>   * [Starter and Growth](<https://rudderstack.com/pricing/>) customers will get a free trial through June 8, 2026 — after which they can purchase it as an add-on
> 

> 
> [Contact your Customer Success Manager](<mailto:support@rudderstack.com>) for any questions.

[Snowflake Streaming](<https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-overview>) is a powerful tool for handling real-time data streams. It allows you to stream data rows directly in Snowflake tables with minimal latency.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/main/src/v0/destinations/snowpipe_streaming>).

> ![info](/docs/images/info.svg)
> 
> **Migrating from Snowflake batch destination?**
> 
> To migrate from RudderStackʼs [Snowflake batch destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/>) to the newer, low-latency Snowflake Streaming destination, see the [Migration Guide](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake-streaming/migration-guide/>) for detailed instructions.

## When to use Snowflake Streaming

Snowflake Streaming is ideal for the following scenarios:

  * **Continuous data streams** : If your data sources produce a steady stream of data in small batches, for example, clickstream data, event logs, etc.
  * **Low latency requirements** : When your application requires immediate/frequent updates to the Snowflake table as new data arrives. Some use cases include real-time dashboards, streaming analytics, etc.
  * **Cost optimization for streaming data** : Snowflake Streaming can potentially reduce costs for real-time pipelines as it allows micro-batch ingestion without needing a traditional Snowflake warehouse running constantly.


## Prerequisites

Before setting up the Snowflake Streaming destination in RudderStack:

  * You will need to have the `ACCOUNTADMIN` system role or any account with `MANAGE GRANTS` privilege.
  * You will need to set the correct user permissions in Snowflake for RudderStack to send the data correctly.


The following sections walk you through the process of setting up a virtual warehouse, database, role, and user in Snowflake.

### 1\. (Optional) Create a warehouse

> ![info](/docs/images/info.svg)
> 
> Note the following:
> 
>   * You can skip this step if you wish to use an existing warehouse.
>   * For this integration, RudderStack uses the warehouse only to run some queries for performing connection validations as well as schema evolution management. It **does not use** the warehouse for data loading.
> 


In your Snowflake console, create a `X-Small` warehouse.

[![Create a virtual warehouse](/docs/images/dw-integrations/snowflake-create-warehouse.webp)](</docs/images/dw-integrations/snowflake-create-warehouse.webp>)

Alternatively, run the following SQL commands to create a new warehouse:
    
    
    CREATE WAREHOUSE "<WAREHOUSE_NAME>"
      WITH WAREHOUSE_SIZE = 'XSMALL'
        WAREHOUSE_TYPE = 'STANDARD'
        AUTO_SUSPEND = 600
        AUTO_RESUME = TRUE;
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure to set `AUTO_SUSPEND` to ~10 minutes and enable `AUTO_RESUME` to avoid any extra costs.

### 2\. Create a database

RudderStack recommends creating a new database to avoid conflicts with your existing data. Note that RudderStack [creates its own tables](<>) within this database while storing your events.

[![Create a database](/docs/images/dw-integrations/snowflake-create-database.webp)](</docs/images/dw-integrations/snowflake-create-database.webp>)

Alternatively, you can create a new database by running the following SQL command:
    
    
    CREATE DATABASE "<DATABASE_NAME>";
    

### 3\. Create a role for RudderStack

To create a new role with the required permissions to load your data into the above database, run the following SQL commands **in the exact order**. Make sure to replace the placeholder names with your preferred names.

  1. Create a new role called `<ROLE>`:


    
    
    CREATE ROLE "<ROLE>";
    

  2. Grant access to the warehouse `<WAREHOUSE_NAME>`:


    
    
    GRANT USAGE ON WAREHOUSE "<WAREHOUSE_NAME>" TO ROLE "<ROLE>";
    

  3. Grant access to the database `<DATABASE_NAME>`:


    
    
    GRANT USAGE ON DATABASE "<DATABASE_NAME>" TO ROLE "<ROLE>";
    GRANT CREATE SCHEMA ON DATABASE "<DATABASE_NAME>" TO ROLE "<ROLE>";
    GRANT ALL ON ALL SCHEMAS IN DATABASE "<DATABASE_NAME>" TO ROLE "<ROLE>";
    

> ![info](/docs/images/info.svg)
> 
> You can also create a custom role with the necessary permissions and specify it in the dashboard settings while setting up the Snowflake Streaming destination in RudderStack.

### 4\. Create a user

Since Snowflake is in the process of deprecating password-only authentication, the Snowflake Streaming destination only supports key-pair authentication.

Use the following query to create a Snowflake user that connects RudderStack to your warehouse. Make sure to replace the placeholder names with your preferred values.
    
    
    CREATE USER "<USER_NAME>"
      RSA_PUBLIC_KEY = "<public_key>"
      MUST_CHANGE_PASSWORD = FALSE
      DEFAULT_ROLE = "<ROLE>"
      PASSWORD = NULL
    GRANT ROLE "<ROLE>" TO USER "<USER_NAME>";
    

## Setup

> ![tip](/docs/images/tip.svg)
> 
> **Tip:** If your sources send data to different schemas, create multiple Snowflake Streaming destinations (each with a different namespace) and connect the relevant sources accordingly.

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then select **Snowflake Streaming** from the list of destinations.
  2. Assign a name to your destination and click **Continue**.


### Connection settings

Setting| Description  
---|---  
Account| Enter the account ID of your Snowflake warehouse. This ID is part of the Snowflake URL.  
  
See the Snowflake account ID examples for more information on how this ID varies depending on various cloud providers.  
Database| Enter the name of the database created in the Create database section.  
Warehouse| Enter the name of your warehouse.  
User| Enter the name of the user created in the Create user section.  
Role| Specify the role to be assigned to the above user. If not specified, RudderStack uses the default role.  
  


> ![warning](/docs/images/warning.svg)Make sure your role has the necessary permissions for RudderStack to load the data into the warehouse.  
  
Private Key| Generate a [private key](<https://docs.snowflake.com/en/user-guide/key-pair-auth#configuring-key-pair-authentication>) and specify it in this field. Make sure to include the delimiters.  
  
See the following sections in the Snowflake documentation to generate and use the key pair:  
  


  * [Generate private key](<https://docs.snowflake.com/en/user-guide/key-pair-auth#generate-the-private-key>)
  * [Generate public key](<https://docs.snowflake.com/en/user-guide/key-pair-auth#generate-a-public-key>)
  * [Assign public key to Snowflake user](<https://docs.snowflake.com/en/user-guide/key-pair-auth#assign-the-public-key-to-a-snowflake-user>)

  
Private Key Passphrase| Specify the password you set while encrypting the private key. Leave this field blank if your private key is not encrypted.  
  


> ![danger](/docs/images/danger.svg)The user authentication will fail if your private key is encrypted and you do not specify the passphrase.  
  
Namespace| Enter the schema name for the warehouse where RudderStack creates all tables. If not specified, RudderStack sets the namespace to the source name by default.  
  


> ![warning](/docs/images/warning.svg)You **cannot** change the namespace later.  
  
#### Snowflake account ID examples

The below table illustrates the slight differences in the account IDs depending on the various cloud providers. See the [Snowflake documentation](<https://docs.snowflake.com/en/user-guide/admin-account-identifier.html#non-vps-account-locator-formats-by-cloud-platform-and-region>) for more information on the account locator formats depending on your region or cloud provider.

Account ID example| Snowflake URL| Snowflake cloud provider  
---|---|---  
`qya56091.us-east-1`  
  
`qya56091.us-east-2.aws`| `https://`**`qya56091.us-east-1`**`.snowflakecomputing.com`  
  
`https://`**`qya56091.us-east-2.aws`**`.snowflakecomputing.com`| AWS  
  
**Note** : In the case of AWS, `.aws` is present in the account locator of some region accounts and must be included in this setting.  
`rx18795.east-us-2.azure`| `https://`**`rx18795.east-us-2.azure`**`.snowflakecomputing.com`| Microsoft Azure  
`ah76025.us-central1.gcp`| `https://`**`ah76025.us-central1.gcp`**`.snowflakecomputing.com`| Google Cloud Platform  
  
### Advanced settings

Setting| Description  
---|---  
Skip Tracks Table| Toggle on this setting to skip sending events to the [`tracks`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table.  
Skip Users Table| This destination **does not support** the [`users`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#table-users>) table.  
Merge Mode| This destination **does not support** merge mode.  
JSON Columns| This setting lets you ingest semi-structured event data not defined by a fixed schema. Specify the required JSON column paths in the dot notation, separated by commas.  
  
See the [JSON Column Support](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/json-column-support/>) guide for more information.  
  


> ![warning](/docs/images/warning.svg)Make sure to update your SDK code to use this feature correctly for snowflake streaming.  
  
### Consent settings

Setting| Description  
---|---  
Consent management provider| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs.  
  
See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/>) for more information on this feature.  
  
## IPs to be allowlisted

To enable network access to RudderStack, allowlist the following RudderStack IPs depending on your region and [RudderStack plan](<https://www.rudderstack.com/pricing>):

Plan| Region  
---|---  
| **US**| **EU**  
Free, Starter, and Growth| 

  * 3.216.35.97
  * 18.214.35.254
  * 23.20.96.9
  * 34.198.90.241
  * 34.211.241.254
  * 52.38.160.231
  * 54.147.40.62

| 

  * 3.123.104.182
  * 3.125.132.33
  * 18.198.90.215
  * 18.196.167.201

  
Enterprise| 

  * 3.216.35.97
  * 34.198.90.241
  * 44.236.60.231
  * 54.147.40.62
  * 100.20.239.77

| 

  * 3.66.99.198
  * 3.64.201.167
  * 3.123.104.182
  * 3.125.132.33

  
  
> ![info](/docs/images/info.svg)
> 
> All the outbound traffic is routed through these RudderStack IPs.

## Migrate from Snowflake destination

See the [Snowflake Streaming Migration Guide](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake-streaming/migration-guide/>) for more information on how to migrate from the [Snowflake batch destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/>) to the Snowflake Streaming destination.

## FAQ

#### What is the difference between Snowflake Streaming and a traditional Snowflake warehouse?

The following table highlights the key differences between Snowflake Streaming and the traditional Snowflake warehouse:

Feature| Snowflake Streaming| Traditional Snowflake warehouse  
---|---|---  
Use case| Real-time data use| Analytical and batch processing  
Latency| Real-time or near real-time| Higher latency (batch-oriented)  
Data volume| Small, continuous data streams| Large, periodic batches  
Cost efficiency| Optimized for streaming and real-time ingestion| Optimized for batch processing  
  
#### Why am I not seeing the `users` table in the schema for `identify` events?

This integration sends the `identify` events exclusively to the [`identifies`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table and skips the [`users`](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#schema>) table entirely.