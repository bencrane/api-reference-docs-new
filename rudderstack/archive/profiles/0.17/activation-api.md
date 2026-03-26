# Activation API (Early Access)

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Activation API (Early Access)

Expose user profiles stored in your Redis instance over an API.

* * *

  * __7 minute read

  * 


With RudderStack’s Activation API, you can fetch enriched user traits stored in your Redis instance and use them for near real-time personalization for your target audience.

> ![warning](/docs/images/warning.svg)
> 
> You must have a working Redis instance in place before setting up the connection.

[![Activation API](/docs/images/profiles/activation-api.webp)](</docs/images/profiles/activation-api.webp>)

## Overview

A brief summary of how the Activation API works:

  1. Sync all your customer 360 data from your Profiles project to your Redis store.
  2. The Activation API sits on top of this Redis instance and provides endpoints for retrieving and using the enriched user data for personalization.


## How to use the Activation API

  1. For the warehouse used for your Profiles project, create the RudderStack schema and grant permissions to it. Refer to the detailed steps for each warehouse:

     * [Snowflake](<https://www.rudderstack.com/docs/sources/reverse-etl/snowflake/#creating-the-rudderstack-schema-and-granting-permissions>)
     * [Redshift](<https://www.rudderstack.com/docs/sources/reverse-etl/amazon-redshift/#creating-the-rudderstack-schema-and-granting-permissions>)
     * [Databricks](<https://www.rudderstack.com/docs/sources/reverse-etl/databricks/#creating-the-rudderstack-schema-and-granting-permissions>)
     * [BigQuery](<https://www.rudderstack.com/docs/sources/reverse-etl/google-bigquery/#creating-the-rudderstack-schema-and-granting-permissions>)
  2. In your Profiles project settings, scroll down to **Activation API** and turn on the **Enable sync to Redis** toggle.


> ![warning](/docs/images/warning.svg)
> 
> Before you enable the Activation API toggle, make sure that:
> 
>   * You have at least one successful Profiles run.
>   * Your `pb_project.yaml` > `entities` defines a `feature_views` property.
> 


> ![warning](/docs/images/warning.svg)
> 
> **Required permissions to enable sync to Redis**
> 
>   * **New Access Management system** : [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) can turn on the **Enable sync to Redis** toggle by default. However, [Members](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) need to have the [**Profiles Edit**](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) permission for the specific Profiles project.
>   * **Legacy Access Management system** : In the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), only [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#org-admin>) can turn on this toggle.
> 


[![Enable Redis sync for using Activation API](/docs/images/profiles/enable-redis.webp)](</docs/images/profiles/enable-redis.webp>)

  3. Enter the account credentials for your Redis instance and click **Create**. This will also create a Redis destination in your dashboard.

[![Enable Redis sync for using Activation API](/docs/images/profiles/enable-redis-sync.webp)](</docs/images/profiles/enable-redis-sync.webp>)

  4. Generate a workspace-level Service Access Token with in your RudderStack dashboard with the following [permission](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) — this token is required to authenticate and use the Activation API:

Resource| Permissions  
---|---  
PII Permission| **Destination Data Access** for the specific Redis destination  
  
> ![info](/docs/images/info.svg)
> 
> **Token permissions for legacy RBAC system**
> 
> If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), your workspace-level Service Access Token should have **Admin** permissions.
> 
> See [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for more information.

  5. Note the destination ID from the [**Settings**](<https://www.rudderstack.com/docs/dashboard-guides/destinations/#destination-details>) tab of your Redis destination.
  6. Use the Activation API endpoint to fetch user profiles from your Redis instance.


## Authorization

This API uses [Bearer Authentication](<https://swagger.io/docs/specification/authentication/bearer-authentication/>) for authenticating all requests. Set the Service Access Token as the bearer token for authentication.

## Base URL
    
    
    https://profiles.rudderstack.com/v1/
    

## Get user profiles

POST

/activation

#### Request body

entity

Required

String

Entity type

destinationId

Required

String

Redis destination ID.

id

Required

Object

ID containing `type` and `value`
    
    
    {
      "entity": <entity_type>,  // User, project, account, etc.
      "destinationId": <redis_destination_id> , // Redis destination ID
      "id": {
        "type": <id_type>,
        "value": <id_value>
      }
    }
    

#### Example request
    
    
    POST /v1/activation HTTP/1.1
    Host: profiles.rudderstack.com
    Content-Type: application/json
    Authorization: Bearer <personal_access_token>
    Content-Length: 90
    
    {
     "entity": <entity_type>,
     "destinationId": <redis_destination_id>, // Redis destination ID
     "id": {
       "type": <id_type>,
       "value": <id_value>
     }
    }
    
    
    
    curl --location 'https://profiles.rudderstack.com/v1/activation' \
    --header 'Content-Type: application/json' \
    --header 'Authorization: Bearer <personal_access_token>' \
    --data '{
     "entity": <entity_type>,
     "destinationId": <redis_destination_id>, // Redis destination ID
     "id": {
       "type": <id_type>,
       "value": <id_value>
     }
    }'
    
    
    
    const axios = require('axios');
    let data = JSON.stringify({
      "destinationId": <redis_destination_id>,
      "entity": <entity_type>,
      "id": {
        "type": <id_type>,
        "value": <id_value>
      }
    });
    
    let config = {
      method: 'post',
      maxBodyLength: Infinity,
      url: 'https://profiles.rudderstack.com/v1/activation',
      headers: {
        'Content-Type': 'application/json',
        'authorization': 'Bearer <personal_access_token>'
      },
      data: data
    };
    
    axios.request(config)
      .then((response) => {
        console.log(JSON.stringify(response.data));
      })
      .catch((error) => {
        console.log(error);
      });
    

#### Responses

  * If the Service Access Token is absent or trying to access a destination to which it does not have access:


    
    
    statusCode: 401
    Response: {
      "error": "Unauthorized request. Please check your access token"
    }
    

  * If the destination is not Redis or the destination ID is absent/blank:


    
    
    statusCode: 404
    Response: {
      "error": "Invalid Destination. Please verify you are passing the right destination ID"
    }
    

  * If ID is present:


    
    
    statusCode: 200
    Response:
    {
      "entity": <entity_type>,
      "id": {
        "type": <id_type>,
        "value": <id_value>
      },
      "data": {
        <traits_from_Redis>
      }
    }
    

  * If ID is not present in Redis:


    
    
    statusCode: 200
    Response:
    {
      "entity": <entity_type>,
      "id": {
        "type": <id_type>,
        "value": <id_value>
      },
      "data": {}
    }
    

## Use case

You can use the Activation API for real-time personalization. Once you fetch the user traits from your Redis instance via the API, you can pull them into your client application to alter the application behavior in real-time based on user interactions.

You can respond immediately with triggered, user-focused messaging based on actions like page views or app clicks and provide a better customer experience.

[![Real time personalization use case](/docs/images/profiles/activation-api-use-case.webp)](</docs/images/profiles/activation-api-use-case.webp>)

## Redis configuration

> ![warning](/docs/images/warning.svg)
> 
> You must have a working Redis instance in place before setting up the connection.

  * **Address** : Enter the public endpoint of your Redis database. If you are using [Redis Cloud](<https://app.redislabs.com/#/>), you can find this endpoint by going to your Redis database and navigating to **Configuration** tab > **General**.


> ![success](/docs/images/tick.svg)
> 
> You can also use [Amazon ElastiCache for Redis](<https://aws.amazon.com/elasticache/redis/>) to set up your Redis database. See the [ElastiCache documentation](<https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/GettingStarted.html>) to get started.

[![Redis database public endpoint](/docs/images/profiles/redis-public-endpoint.webp)](</docs/images/profiles/redis-public-endpoint.webp>)

  * **Password** : Enter the database password. You can find it in the **Security** section of the **Configuration** tab:

[![Redis database password](/docs/images/profiles/redis-database-password.webp)](</docs/images/profiles/redis-database-password.webp>)

  * **Cluster Mode** : Turn on this setting if you’re connecting to a Redis cluster.
  * **Secure** : Enable this setting to secure the TLS communication between RudderStack Redis client and your Redis server.


## Data mapping

RudderStack creates multiple Reverse ETL sources automatically based on your Profiles project. You will see separate sources for different `id_served` connected to the same Redis destination.

The following `pb_project.yaml` snippet shows the sources to be created:
    
    
    entities:
      - name: user
        id_types:
          - main_id
          - user_id
        feature_views:
          using_ids:
            - id: email
              name: features_by_email # Optional. Takes default view name, if not specified.
            - id: salesforce_id
              name: salesforce_id_stitched_features
          features: # Optional
            - from: models/cart_feature_table
              include:
                - "*"
    

## FAQ

#### How do I generate a workspace-level Service Access Token to use the Activation API?

Follow these steps to generate a workspace-level Service Access Token to use the Activation API:

> ![info](/docs/images/info.svg)
> 
> [Workspace-level Service Access Tokens](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-level-sats>) are linked to a specific workspace — their usage is restricted to workspace-level resources (sources, destinations, transformations, etc.) and [APIs](<https://www.rudderstack.com/docs/api/>).

  1. Log in to your [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Go to **Settings** > **Access Management** > **Service Access Tokens**.
  3. Click the **Workspace** tab.

[![Workspace tab in Service Access Tokens section](/docs/images/access-management/service-access-tokens/workspace-tab.webp)](</docs/images/access-management/service-access-tokens/workspace-tab.webp>)

  4. Click **Generate new token**.
  5. Enter the name of the SAT.
  6. Choose the relevant workspace (applicable for a multi-workspace organization) where the token will be applicable. Then, click **Next**.

[![Workspace level Service Access Token generation in RudderStack dashboard](/docs/images/access-management/service-access-tokens/workspace-sat-name.webp)](</docs/images/access-management/service-access-tokens/workspace-sat-name.webp>)

  7. Under **Workspace SAT access policy** , configure the [access policy](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) for the token with the following permission:

Resource| Permissions  
---|---  
PII Permission| **Destination Data Access** for the specific Redis destination  
  
> ![warning](/docs/images/warning.svg)
> 
> **Important** : Once generated, you cannot edit the access policy of the workspace-level Service Access Token.

  8. Click **Generate** to generate the token.
  9. Note the token and use it to authenticate the Activation API.


> ![warning](/docs/images/warning.svg)
> 
> Secure the token value — you will not be able to see it again once you click **Close**.

[![Workspace level Service Access Token generated in RudderStack dashboard](/docs/images/access-management/service-access-tokens/workspace-token-generated.webp)](</docs/images/access-management/service-access-tokens/workspace-token-generated.webp>)

#### How can I make Profiles work with the Activation API?

To use the Activation API with your Profiles project, you need a successful run of your Profiles project that is not past the retention period.

To enable the Activation API for your Profiles project, turn on the **Enable sync to Redis** setting. A Profile run will then sync automatically.

[![Toggle API in Settings](/docs/images/rudderstack-api/activation-api-toggle-settings.png)](</docs/images/rudderstack-api/activation-api-toggle-settings.png>)

#### Why am I getting an error trying to enable API in my instance for a custom project hosted on GitHub?

For GitHub projects, you need to explicitly add the IDs of the custom project that need to be served.

In your `pb_project.yaml` file, you can specify them as shown:
    
    
    entities:
      - name: user
        id_types:
          - main_id
          - user_id
        feature_views:
          name: user_feature_view
          using_ids:
            - id: email
              name: features_by_email
            - id: salesforce_id
              name: salesforce_id_stitched_features
          features:
            - from: models/cart_feature_table
              include:
                - "*"
    

#### If I force a full resync, stop it, and then start a new sync, does RudderStack always perform a full sync the next time?

It depends on the state of the task when it was canceled.

  * If the sync is cancelled while RudderStack is preparing a snapshot, then next run depends on the state of the previous successful run and any mapping changes.
  * If it is cancelled after the sync data is prepared, the next run is incremental.


Generally if a sync is cancelled manually, it is recommended to trigger a full sync if the previous cancelled task was a full sync. If the previously cancelled sync was incremental, triggering an incremental sync is recommended.

#### Does RudderStack perform a full sync if I add a new column?

RudderStack does not change the sync mode if you make any column additions. It triggers a full sync only if you change/update the data mappings, for example, if the newly added column is sent to the destination via the [Visual Data Mapper](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/visual-data-mapper/>).

For Profiles activation syncs, RudderStack updates the mappings and automatically sends all columns from the customer 360 view by triggering a full sync.

#### Suppose I’m running a full sync and the Profiles job is running in parallel and finishes eventually. What happens to the scheduled sync? Does it get queued?

RudderStack first creates a temporary snapshot copy of any sync when it starts. So its syncing the created copy. Even if a Profiles job is running in parallel, the sync - if started - is not impacted by it.

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.17/data-apps/real-time-personalization/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.17/example/>)