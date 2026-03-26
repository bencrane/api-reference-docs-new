# Activation API

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Activation API

Expose user profiles stored in your Redis instance over an API.

* * *

  * __7 minute read

  * 


With RudderStack’s Activation API, you can fetch enriched user traits stored in your Redis instance and use them for near real-time personalization for your target audience.

You can sync all your customer 360 data from Profiles project to your Redis store. Then, use the Activation API endpoints to retrieve and use the enriched user data for personalization.

[![Activation API](/docs/images/profiles/activation-api.webp)](</docs/images/profiles/activation-api.webp>)![](https://img.shields.io/badge/API%20Version-2-7447fc.svg?logo=data:image/png;base64,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&logoColor=&logoWidth=&style=)

## Prerequisites

To use the Activation API:

  * You must have a working Redis instance in place to use the Activation API
  * You must have at least one successful Profiles run
  * Your `pb_project.yaml` > `entities` must have a [`feature_views`](<https://www.rudderstack.com/docs/profiles/concepts/feature-views/>) property
  * Generate a workspace-level Service Access Token in your RudderStack dashboard with the following permission — this token is required to authenticate and use the API

Resource| Permissions  
---|---  
PII Permission| **Destination Data Access** for the specific Redis destination  
  
#### Token permissions for legacy RBAC system

If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), your workspace-level Service Access Token should have **Admin** permissions.

See [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for more information on generating the token.

[![workspace-level Service Access Token with Admin permission](/docs/images/access-management/permissions/legacy/admin.webp)](</docs/images/access-management/permissions/legacy/admin.webp>)

## Use Activation API

  1. For the warehouse used for your Profiles project, create the RudderStack schema and grant permissions to it. Refer to the following sections for detailed steps for each warehouse:

     * [Snowflake](<https://www.rudderstack.com/docs/sources/reverse-etl/snowflake/#creating-the-rudderstack-schema-and-granting-permissions>)
     * [Redshift](<https://www.rudderstack.com/docs/sources/reverse-etl/amazon-redshift/#creating-the-rudderstack-schema-and-granting-permissions>)
     * [Databricks](<https://www.rudderstack.com/docs/sources/reverse-etl/databricks/#creating-the-rudderstack-schema-and-granting-permissions>)
     * [BigQuery](<https://www.rudderstack.com/docs/sources/reverse-etl/google-bigquery/#creating-the-rudderstack-schema-and-granting-permissions>)
  2. In your Profiles project settings, scroll down to **Activation API** and turn on the **Enable sync to Redis** toggle.


[![Enable Redis sync for using Activation API](/docs/images/profiles/enable-redis.webp)](</docs/images/profiles/enable-redis.webp>)

> ![warning](/docs/images/warning.svg)
> 
> **Required permissions to enable sync to Redis**
> 
>   * **New Access Management system** : [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) can turn on the **Enable sync to Redis** toggle by default. However, [Members](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) need to have the [**Profiles Edit**](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) permission for the specific Profiles project.
>   * **Legacy RBAC system** : In the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), only [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#org-admin>) can turn on this toggle.
> 


  3. Enter the account credentials for your Redis instance and click **Create**. This will also create a Redis destination in your dashboard.

[![Enable Redis sync for using Activation API](/docs/images/profiles/redis-settings.webp)](</docs/images/profiles/redis-settings.webp>)

  4. Note the destination ID from the [**Settings**](<https://www.rudderstack.com/docs/dashboard-guides/destinations/#destination-details>) tab of your Redis destination.
  5. Use the Activation API endpoint to fetch user profiles from your Redis instance.


## Authorization

This API uses [Bearer Authentication](<https://swagger.io/docs/specification/authentication/bearer-authentication/>) for authenticating all requests. Set the Service Access Token as the bearer token for authentication.

## Base URL
    
    
    https://profiles.rudderstack.com/v2/
    

## Get user profiles

POST

/activation

### Request body

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
    

### Sample request
    
    
    POST /v2/activation HTTP/1.1
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
    
    
    
    curl --location 'https://profiles.rudderstack.com/v2/activation' \
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
      url: 'https://profiles.rudderstack.com/v2/activation',
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
    

### Responses

You will get the following response if the Service Access Token is absent or trying to access a destination to which it does not have access:
    
    
    statusCode: 401
    Response: {
      "error": "Unauthorized request. Please check your access token"
    }
    

You will get the following response if the destination is not Redis or the destination ID is absent/blank:
    
    
    statusCode: 404
    Response: {
      "error": "Invalid Destination. Please verify you are passing the right destination ID"
    }
    

You will get the following response if the destination ID is present and valid:
    
    
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
    

You will get the following response if the destination ID is not present in Redis:
    
    
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
    

## Delete user profiles

DELETE

/activation

### Request body

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

### Sample request
    
    
    POST /v2/activation HTTP/1.1
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
    
    
    
    curl --location 'https://profiles.rudderstack.com/v2/activation' \
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
      url: 'https://profiles.rudderstack.com/v2/activation',
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
    

### Responses
    
    
    statusCode: 200
    Response: {
      "deletedKeys": 20,
      "actualKeys": 30
    }
    
    
    
    statusCode: 400
    Response: {
      "message": "id should have at least one item"
    }
    
    
    
    statusCode: 200
    Response: {
      "message": "Internal server error"
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

RudderStack creates multiple Reverse ETL sources automatically based on your Profiles project. You will see separate sources connected to the same Redis destination.

The following `pb_project.yaml` snippet shows the sources to be created:
    
    
    entities:
      - name: user
        id_types:
          - main_id
          - user_id
          - email
          - salesforce_id
        feature_views:
          using_ids:
            - id: email
              name: features_by_email # Optional. Takes default view name, if not specified.
            - id: salesforce_id
              name: salesforce_id_stitched_features
    

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

#### Why am I getting an error trying to enable API in my instance for a custom project hosted on GitHub?

For GitHub projects, you need to explicitly add the IDs of the custom project that need to be served.

In your `pb_project.yaml` file, you can specify them as shown:
    
    
    entities:
      - name: user
        id_types:
          - main_id
          - user_id
          - email
          - salesforce_id
        feature_views:
          name: user_feature_view
          using_ids:
            - id: email
              name: features_by_email
            - id: salesforce_id
              name: salesforce_id_stitched_features
    

#### Does RudderStack perform a full sync if I add a new feature to my project?

Yes, RudderStack updates the mappings and automatically sends all columns from the customer 360 view by triggering a full sync.

#### Suppose I’m running a full sync and the Profiles job is running in parallel and finishes eventually. What happens to the scheduled sync? Does it get queued?

RudderStack first creates a temporary snapshot copy of any sync when it starts. So its syncing the created copy. Even if a Profiles job is running in parallel, the sync - if started - is not impacted by it.

##### [Activation API v1](</docs/archive/profiles/0.19/dev-docs/activation-api/v1/>)

Expose user profiles stored in your Redis instance over an API.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.19/dev-docs/warehouse-output/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.19/dev-docs/activation-api/v1/>)