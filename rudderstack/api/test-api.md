# RudderStack Test API

Use the RudderStack Test API to verify the event workflow for your configured sources and destinations.

* * *

  * __12 minute read

  * 


The **RudderStack Test API** offers two endpoints to verify successful event transformation and delivery for a given source-destination setup, without having to refer to the [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) tab.

> ![warning](/docs/images/warning.svg)
> 
> The Test API is currently not supported for **Open-source RudderStack**.
> 
> Also, some destinations like Apache Kafka, Google Pub/Sub, Google Sheets, etc. are not supported by this API. For the complete list, refer to the FAQ section below.

This guide details the various endpoints of the Test API.

## Prerequisites

The following prerequisites must be met to use the Test API successfully:

  * Set up a source-destination connection in RudderStack. See the [Quickstart](<https://www.rudderstack.com/docs/data-pipelines/event-stream/quickstart/>) guide for detailed steps.
  * Generate a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) in your RudderStack workspace.


> ![info](/docs/images/info.svg)
> 
> The workspace-level Service Access Token has **Read** permissions by default. You do not need to assign any [resource permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) while generating the token.

#### Token permissions for legacy RBAC system

If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), your workspace-level Service Access Token should have minimum **Viewer** permissions.

See [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for more information on generating the token.

[![workspace-level Service Access Token with Viewer permission](/docs/images/access-management/permissions/legacy/viewer.webp)](</docs/images/access-management/permissions/legacy/viewer.webp>)

## API authorization

The Test API uses **Basic Authentication** for authenticating all requests.

If you’re using Postman, authenticate the API by including an empty string (`""`) as the username and your [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#generate-service-access-token>) as the password in the **Authorization** tab.

> ![info](/docs/images/info.svg)
> 
> RudderStack recommends using:
> 
>   * [Service Access Tokens (SATs)](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#generate-service-access-token>) for production use cases that require shared access to the services and resources across the organization or workspace.
>   * [Personal Access Tokens (PATs)](<https://www.rudderstack.com/docs/access-management/personal-access-tokens/>) for testing a service/feature or personal use cases.
> 


You can also pass your Service Access Token in the authorization header directly:
    
    
    Authorization: Basic {Base64Encoded(:<SERVICE_ACCESS_TOKEN>)}
    

An example is shown below:

  * Username: `""` (empty string)
  * Service Access Token: `<SERVICE_ACCESS_TOKEN>`
  * Header: `Basic {Base64Encoded(:<SERVICE_ACCESS_TOKEN>)}`


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Verify that the Service Access Token is valid if you get an **Invalid Authorization Header** error.

## Base URL

Use the base URL for your API requests depending on your region:
    
    
    https://api.rudderstack.com
    
    
    
    https://api.eu.rudderstack.com
    

## Verifying destination events

This request verifies if the test events are successfully transformed and delivered to the specified destination.

  * **Request Type** : **POST**

  * **Request Format** :


    
    
    https://api.rudderstack.com/v0/testDestination/<destination_ID>
    

Here, `<destination_ID>` should be replaced with the ID associated with the destination configured on the dashboard:

[![Destination ID](/docs/images/test-api-1.webp)](</docs/images/test-api-1.webp>)

> ![info](/docs/images/info.svg)
> 
> The `/testDestination` endpoint **does not require** a source to be connected to the destination.

  * **Request body** :


    
    
    {
      "stage": {
        "user_transform": true,
        "dest_transform": true,
        "send_to_destination": true
      },
      "message": {
        // RudderStack HTTP Payload (identify, track, etc.)
      }
    }
    

> ![info](/docs/images/info.svg)
> 
> To learn more about the `stage` object, refer to the Verification stages section below.

  * **Sample payload** :


    
    
    {
      "message": {
        "context": {
          "traits": {
            "firstName": "James",
            "lastName": "Doe"
          }
        },
        "type": "identify",
        "userId": "abc@123.com"
      }
    }
    

> ![info](/docs/images/info.svg)
> 
> For more information on the message `type`, refer to the Supported message types section below.

  * **Sample request** :


    
    
    curl --location --request POST 'https://api.rudderstack.com/v0/testDestination/1zl4i0J8M8T7sozoLnueW46RVYe' \
    --header 'Authorization: Basic YEDZaVaah5YSs5ODdAcnVkZGVyc3RhY2suY29tOjF6bDRzOUt2NkducjVhRkhZV1E3RUg3Z2dwTA==' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "message": {
            "context": {
                "traits": {
                    "firstName": "James",
                    "lastName": "Doe"
                }
            },
            "type": "identify",
            "userId": "abc@123.com"
        },
        "stage": {
            "user_transform": true,
            "dest_transform": true,
            "send_to_destination": true
        }
    }'
    

  * **Expected response** :


    
    
    {
      "destinationId": "1zl4i0J8M8T7sozoLnueW46RVYe",
      "destination": "WEBHOOK",
      "destinationName": "test-webhook-dest",
      "data": [{
        "user_transformed_payload": {
          "error": "Transformation VersionID not found"
        },
        "dest_transformed_payload": [{
          "version": "1",
          "type": "REST",
          "method": "POST",
          "endpoint": "https://webhook.site/9d5e3e43-6c2b-4b84-be9f-0147347b4cdf",
          "headers": {
            "content-type": "application/json"
          },
          "params": {},
          "body": {
            "JSON": {
              "context": {
                "traits": {
                  "firstName": "James",
                  "lastName": "Doe"
                }
              },
              "type": "identify",
              "userId": "abc@123.com"
            },
            "JSON_ARRAY": {},
            "XML": {},
            "FORM": {}
          },
          "files": {}
        }],
        "destination_response": [{
          "success": false,
          "error": {
            "message": "Token not found",
            "id": null
          }
        }],
        "destination_response_status": [
          404
        ]
      }]
    }
    

### Verifying events for disabled destinations

If the `/testDestination` endpoint is used to verify the events sent to a disabled destination, the API will return the following response:
    
    
    {
      "destinationId": "<destination_ID>",
      "destinationName": "<destination_name>",
      "error": "Destination with id <destination_ID> is disabled"
    }
    

A sample response highlighting the above error is shown below:
    
    
    {
      "destinationId": "1zl4i0J8M8T7sozoLnueW46RVYe",
      "destinationName": "test-webhook-dest",
      "error": "Destination with id 1zl4i0J8M8T7sozoLnueW46RVYe is disabled"
    }
    

To override this behavior and send the event to a disabled destination, you can call the `/testDestination` endpoint with the query parameter `force=true`:
    
    
    https://api.rudderstack.com/v0/testDestination/<destination_ID>?force=true
    

### Overriding existing destination configuration

You can also leverage the `/testDestination` endpoint to send your destination configuration as a part of the HTTP request body. This configuration overrides the existing destination configuration in RudderStack.

> ![warning](/docs/images/warning.svg)
> 
> To use this feature, you must have set up the destination in RudderStack.

A sample request body highlighting this feature is shown below:
    
    
    {
      "stage": {
        "user_transform": true,
        "dest_transform": true,
        "send_to_destination": true
      },
      "message": {
        // RudderStack HTTP Payload (identify, track, etc.)
      },
      "destinationConfig": {
            "webhookUrl": "<webhook_URL>"
        }
    }
    

> ![warning](/docs/images/warning.svg)
> 
> The `destinationConfig` field can be passed only for the `testDestination` endpoint.

#### Getting the destination definition variables

To override the destination configuration using the `/testDestination` endpoint, you need to know the configuration variables to use within `destinationConfig`. To get these variables, use the **`destination-definitions`** endpoint. The request format is listed below:

  * **Request Type** : **GET**

  * **Request Format** :


    
    
    https://api.rudderstack.com/destination-definitions
    

> ![success](/docs/images/tick.svg)
> 
> This endpoint does not require any authentication.

Once you run this endpoint, you should be able to view all variable names within the `defaultConfig` parameter of that destination, as seen below:

[![Configuration variables](/docs/images/test-api-3.webp)](</docs/images/test-api-3.webp>)

As seen in the above example, for the webhook destination, the configuration variables are `webhookUrl`, `webhookMethod`, and `headers`. These correspond to the webhook destination settings as seen in the RudderStack dashboard below:

[![Dashboard settings](/docs/images/test-api-4.webp)](</docs/images/test-api-4.webp>)

To override the dashboard settings, provide the new values for the destination configuration variables in the request body of the `/testDestination` endpoint as seen in the [Overriding existing destination configuration](<https://www.rudderstack.com/docs/api/test-api/#overriding-existing-destination-configuration>) section above.

> ![success](/docs/images/tick.svg)
> 
> For a detailed use-case on how to use this feature, refer to the FAQ section below.

## Verifying source events

This request verifies if the test events are successfully sent from the specified source and delivered to all connected destinations.

  * **Request Type** : **POST**

  * **Request Format** :


    
    
    https://api.rudderstack.com/v0/testSource/<source_ID>
    

Here, `<source_ID>` should be replaced with the ID associated with the source configured on the dashboard:

[![Source ID](/docs/images/test-api-2.webp)](</docs/images/test-api-2.webp>)

> ![info](/docs/images/info.svg)
> 
> The `/testSource` endpoint requires the specified source to be connected to at least one destination.

> ![success](/docs/images/tick.svg)
> 
> The `/testSource` endpoint essentially calls the `/testDestination` endpoint for each destination connected to that source and returns an array of responses.

  * **Request body** :


    
    
    {
      "stage": {
        "user_transform": true,
        "dest_transform": true,
        "send_to_destination": true
      },
      "message": {
        // RudderStack HTTP Payload (identify, track, etc.)
      }
    }
    

> ![info](/docs/images/info.svg)
> 
> To learn more about the `stage` object, refer to the **Verification stages** section below.

  * **Sample payload** :


    
    
    {
      "message": {
        "context": {
          "traits": {
            "firstName": "James",
            "lastName": "Doe"
          }
        },
        "type": "identify",
        "userId": "abc@123.com"
      }
    }
    

> ![info](/docs/images/info.svg)
> 
> For more information on the message `type`, refer to the Supported message types section below.

  * **Sample request** :


    
    
    curl --location --request POST 'https://api.rudderstack.com/v0/testSource/1zlmsBMe1dcPbu3u6NTZFUFBrNQ' \
    --header 'Authorization: Basic YEDZaVaah5YSs5ODdAcnVkZGVyc3RhY2suY29tOjF6bDRzOUt2NkducjVhRkhZV1E3RUg3Z2dwTA==' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "message": {
            "context": {
                "traits": {
                    "firstName": "James",
                    "lastName": "Doe"
                }
            },
            "type": "identify",
            "userId": "abc@123.com"
        },
        "stage": {
            "user_transform": true,
            "dest_transform": true,
            "send_to_destination": true
        }
    }'
    

  * **Expected response** :


    
    
    [{
        "destinationId": "1tIgXcaRnQDlBBtxlJMGGHFUWGb",
        "destinationName": "salesforce",
        "error": "Destination with id 1tIgXcaRnQDlBBtxlJMGGHFUWGb is disabled"
      },
      {
        "destinationId": "1zl4i0J8M8T7sozoLnueW46RVYe",
        "destination": "WEBHOOK",
        "destinationName": "test-webhook-dest",
        "data": [{
          "user_transformed_payload": {
            "error": "Transformation VersionID not found"
          },
          "dest_transformed_payload": [{
            "version": "1",
            "type": "REST",
            "method": "POST",
            "endpoint": "https://webhook.site/9d5e3e43-6c2b-4b84-be9f-0147347b4cdf",
            "headers": {
              "content-type": "application/json"
            },
            "params": {},
            "body": {
              "JSON": {
                "context": {
                  "traits": {
                    "firstName": "James",
                    "lastName": "Doe"
                  }
                },
                "type": "identify",
                "userId": "abc@123.com"
              },
              "JSON_ARRAY": {},
              "XML": {},
              "FORM": {}
            },
            "files": {}
          }],
          "destination_response": [{
            "success": false,
            "error": {
              "message": "Token not found",
              "id": null
            }
          }],
          "destination_response_status": [
            404
          ]
        }]
      },
      {
        "destinationId": "1tKpO0kantcKjd5czXVD1cdwUBE",
        "destination": "MARKETO",
        "destinationName": "Marketo",
        "data": [{
          "user_transformed_payload": {
            "error": "Transformation VersionID not found"
          },
          "dest_transformed_payload": [{
            "version": "1",
            "type": "REST",
            "method": "POST",
            "endpoint": "https://585-AXP-425.mktorest.com/rest/v1/leads.json",
            "headers": {
              "Authorization": "Bearer f54f0384-583b-4718-b533-38aaed4bc5ae:cd",
              "Content-Type": "application/json"
            },
            "params": {},
            "body": {
              "JSON": {
                "action": "createOrUpdate",
                "input": [{
                  "FirstName": "James",
                  "LastName": "Doe",
                  "lastName": "Doe",
                  "firstName": "James",
                  "id": 1328262,
                  "userId": "abc@123.com"
                }],
                "lookupField": "id"
              },
              "JSON_ARRAY": {},
              "XML": {},
              "FORM": {}
            },
            "files": {}
          }],
          "destination_response": [{
            "requestId": "555d#17d31b0a392",
            "result": [{
              "id": 1328262,
              "status": "updated"
            }],
            "success": true
          }],
          "destination_response_status": [
            200
          ]
        }]
      }
    ]
    

The above response indicates that the source with the source ID `1zlmsBMe1dcPbu3u6NTZFUFBrNQ` is connected to three destinations:

  * Salesforce, a disabled destination
  * Webhook, with no transformation specified in the dashboard, and
  * Marketo


### Verifying events from a disabled source

If the `/testSource` endpoint is used to verify the events sent from a disabled source, the API will send the following response:
    
    
    {
      "message": "Source with <source_ID> is disabled"
    }
    

To override this behavior and send the event from a disabled source to all connected destinations, you can call the `/testSource` endpoint with the query parameter `force=true`:
    
    
    https://api.rudderstack.com/v0/testSource/<source_ID>?force=true
    

### Verifying events for disabled destinations

If the `/testSource` endpoint is used to verify the events sent to a disabled destination, the API will send the following response:
    
    
    {
      "destinationId": "<destination_ID>",
      "destinationName": "<destination_name>",
      "error": "Destination with id <destination_ID> is disabled"
    }
    

To override this behavior and send the event to a disabled destination, you can call the `/testSource` endpoint with the query parameter `force=true`:
    
    
    https://api.rudderstack.com/v0/testSource/<source_ID>?force=true
    

## Verification stages

The request body for the `testDestination` and `testSource` endpoints of this API is as shown:
    
    
    {
      "stage": {
        "user_transform": true,
        "dest_transform": true,
        "send_to_destination": true
      },
      "message": {
        // RudderStack HTTP Payload (identify, track, etc.)
      }
    }
    

Here, `stage` essentially defines the different stages enabled in the pipeline through which the API verifies the event payload. These stages are:

  * `user_transform`
  * `dest_transform`
  * `send_to_destination`


The following sections define each of these stages in detail.

### `user_transform`

If `user_transform` is set to `true`, the API checks if a user transformation is connected to a destination and returns the transformed event as a response. If set to `false`, the API skips this stage completely and moves to the next stage (`dest_transform`).

Note the following:

  * Suppose you set `user_transform` to `true`, but no user transformation is specified while configuring the destination in the dashboard. In this case, the API returns the following response before skipping to the next stage:


    
    
    "user_transformed_payload": {
      "error": "Transformation VersionID not found"
    }
    

  * If an error occurs while applying the transformation to the payload, the API returns an error, and the next stages are aborted.


A sample API response is shown below:
    
    
    [{
      "data": [{
        "user_transformed_payload": {
          "error": "Error: Error."
        },
        "dest_transformed_payload": {
          "error": "error encountered in user_transformation stage. Aborting."
        },
        "destination_response": {
          "error": "error encountered in dest_transformation stage. Aborting."
        }
      }]
    }]
    

### `dest_transform`

If `dest_transform` is set to `true`, the API returns the transformer response. This response shows the payload after it has been transformed into a destination-specific format.

A sample API response when `dest_transform` is set to `true` is shown below:
    
    
    "dest_transformed_payload": [{
      "version": "1",
      "type": "REST",
      "method": "POST",
      "endpoint": "https://webhook.site/9d5e3e43-6c2b-4b84-be9f-0147347b4cdf",
      "headers": {
        "content-type": "application/json"
      },
      "params": {},
      "body": {
        "JSON": {
          "context": {
            "traits": {
              "firstName": "James",
              "lastName": "Doe"
            }
          },
          "type": "identify",
          "userId": "abc@123.com"
        },
        "XML": {},
        "FORM": {}
      },
      "files": {}
    }]
    

### `send_to_destination`

When `send_to_destination` is set to `true`, the event is sent to the destination and the API returns the response. If set to `false`, this stage is skipped completely.

A sample API response when `send_to_destination` is set to `true` is shown below:
    
    
    "destination_response": [{
      "status": "success",
      "processed": 1,
      "unprocessed": []
    }],
    "destination_response_status": [200]
    

## Supported message types

The Test API supports the following message `type`:

  * `identify`
  * `track`
  * `page`
  * `screen`
  * `group`
  * `alias`


> ![info](/docs/images/info.svg)
> 
> For more information on these message types, refer to the [RudderStack Events Specification](<https://www.rudderstack.com/docs/event-spec/standard-events/>) guide.

If you specify any other message `type` apart from the supported events mentioned in the above list, you will get the following error:
    
    
    {
        "message": "message type is unsupported"
    }
    

You will get the following error message if no message `type` is specified in the payload, or if `type` is not a string:
    
    
    {
        "message": "message type missing or invalid"
    }
    

## FAQ

#### Which destinations are not supported by the Test API?

The Test API does not support the destinations that leverage the [rudder-server](<https://github.com/rudderlabs/rudder-server>) to send the test events. These destinations include:

  * [Amazon Kinesis](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-kinesis/>)
  * [Apache Kafka](<https://www.rudderstack.com/docs/destinations/streaming-destinations/kafka/>)
  * [Azure Event Hub](<https://www.rudderstack.com/docs/destinations/streaming-destinations/azure-event-hubs/>)
  * [Amazon Kinesis Firehose](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-kinesis-firehose/>)
  * [Amazon EventBridge](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-eventbridge/>)
  * [Amazon Personalize](<https://www.rudderstack.com/docs/destinations/streaming-destinations/aws-personalize/>)
  * [Confluent Cloud](<https://www.rudderstack.com/docs/destinations/streaming-destinations/confluent-cloud/>)
  * [Google Pub/Sub](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-pub-sub/>)
  * [Google Sheets](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-sheets/>)
  * [Redis](<https://www.rudderstack.com/docs/destinations/streaming-destinations/redis/>)
  * [BigQuery Stream](<https://www.rudderstack.com/docs/destinations/streaming-destinations/bigquery-stream/>)
  * [Amazon S3](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-s3/>)
  * [Azure Blob Storage](<https://www.rudderstack.com/docs/destinations/streaming-destinations/microsoft-azure-blob-storage/>)
  * [DigitalOcean Spaces](<https://www.rudderstack.com/docs/destinations/streaming-destinations/digitalocean-spaces/>)
  * [Google Cloud Storage](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-cloud-storage/>)
  * [MinIO](<https://www.rudderstack.com/docs/destinations/streaming-destinations/minio/>)


> ![warning](/docs/images/warning.svg)
> 
> The Test API also does not support the [data warehouse destinations](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

#### What happens if `type` is not included in the event payload?

Simply put, `type` refers to the event type in the payload.

  * If `type` is missing in the event payload, the API will return the following error:


    
    
    {
        "message": "message type missing or invalid"
    }
    

  * If you set `type` to any value other than `identify`, `track`, `page`, `screen`, `group`, or `alias`, the API will return the following error:


    
    
    {
        "message": "message type is unsupported"
    }
    

For more information, refer to the supported message types section above.

#### Can I disable a particular verification stage in the `stage` object?

The request body for the `testDestination` and `testSource` includes the `stage` object, which is defined as follows:
    
    
    {
      "stage": {
        "user_transform": true,
        "dest_transform": true,
        "send_to_destination": true
      }
    

The `stage` object defines the different stages enabled in the pipeline through which the API verifies the event payload. These stages are:

  * `user_transform`
  * `dest_transform`
  * `send_to_destination`


To disable or a specific verification stage, you can set the value of that parameter to be `false`. For example, if you don’t want the API to check if a user transformation is applied to the event payload, you can set `user_transform` to false:
    
    
    {
      "stage": {
        "user_transform": false,
        "dest_transform": true,
        "send_to_destination": true
      }
    

> ![info](/docs/images/info.svg)
> 
> Refer to the Verification stages section above for more information on each of the `stage` object parameters.

#### Can I override the destination settings specified in the RudderStack dashboard using this API?

Yes, you can.

Suppose you have configured a webhook destination in the RudderStack dashboard with the following settings:

[![Dashboard settings for webhook destination](/docs/images/test-api-5.webp)](</docs/images/test-api-5.webp>)

You can leverage the `/testDestination` endpoint to send the new configuration as a part of the HTTP request body. This configuration overrides the existing destination settings configured in RudderStack.

Your HTTP request body should look like the following:
    
    
    {
      "stage": {
        "user_transform": true,
        "dest_transform": true,
        "send_to_destination": true
      },
      "message": {
        // RudderStack HTTP Payload (identify, track, etc.)
      },
      "destinationConfig": {
            "webhookUrl": <webhook_URL>,
            "webhookMethod": <new_webhook_method>
        }
    }
    

To get the variable names to use in `destinationConfig`, run the following **GET** request:
    
    
    https://api.rudderstack.com/destination-definitions
    

Next, look for the webhook destination and the corresponding configuration variables for it under `defaultConfig`:

[![Configuration variables](/docs/images/test-api-3.webp)](</docs/images/test-api-3.webp>)

Finally, specify the new configuration value for the required variables and run the request. For instance, the new `webhookUrl` and `webhookMethod` values will replace the existing settings configured in the RudderStack dashboard.