# User Trait Deduplication in Braze Destination

Use Braze’s deduplication feature to save data points and avoid billing overages.

Available Plans

  * growth
  * enterprise


* * *

  *  __7 minute read

  * 


This guide explains how to use Braze’s deduplication feature to save data points and avoid billing overages.

## Overview

Braze charges its consumption based on [data points](<https://www.braze.com/docs/user_guide/data_and_analytics/data_points/#consumption-count>) it ingests for every user property and events like session starts and ends, purchases, etc. These data points are accumulated whenever you update a user profile or when the users perform specific actions.

Braze counts all data points irrespective of whether you send any duplicates. It considers every property (except the standard ones) as a data point and counts it against your billing.

With the deduplication feature, RudderStack prevents duplicate user traits in the `identify` and `track` calls from being sent to Braze, thus saving data points and ultimately avoiding billing overages in Braze.

  * This feature is helpful in Reverse ETL scenarios where a large number of rows are sent with duplicate columns.
  * You can use this feature to deduplicate **only the user attributes** present in the `identify` and `track` calls sent to Braze. Braze does not deduplicate the entire `identify`/`track` events.


> ![warning](/docs/images/warning.svg)
> 
> **API rate limits in cloud mode**
> 
> When sending data to Braze in cloud mode, RudderStack implements the deduplication logic such that it does not surpass Braze’s API limits in most cases.
> 
>   * If you onboarded with Braze on or after August 22, 2024, then the endpoint used for deduplication (`/users/export/ids`) has a rate limit of **250** requests per minute.
>   * If you onboarded before this date, the rate limit is **2500** requests per minute.
> 

> 
> In cases where this limit is surpassed, RudderStack defaults to sending all events **without deduplication** until the volume returns below the permissible rate limits.

## Get started

To use the Braze deduplication feature, follow these steps:

  1. Log in to your [Braze dashboard](<https://dashboard.braze.com/auth>) and go to **Settings** > **Developer Console**.
  2. Generate a new REST API key with the `users.export.ids` permission. You can find it in the **User Data** section of permissions.


> ![warning](/docs/images/warning.svg)
> 
> You also need to include the permissions listed in the Braze destination’s [connection settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/setup-guide/#connection-settings>).

[![Setting Braze REST API key for dedup](/docs/images/event-stream-destinations/braze-dedup-permissions.webp)](</docs/images/event-stream-destinations/braze-dedup-permissions.webp>)

  3. Use this REST API key to set up your Braze destination.
  4. Toggle on the **Deduplicate Traits (Beta)** option in the Braze [destination configuration settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/setup-guide/#deduplication-settings>):

[![Enable Braze deduplication setting](/docs/images/event-stream-destinations/braze-dedup-enable.webp)](</docs/images/event-stream-destinations/braze-dedup-enable.webp>)

  5. Enable the connection and start sending your events to Braze.

[![Enable Braze deduplication setting](/docs/images/event-stream-destinations/braze-enable-connection.webp)](</docs/images/event-stream-destinations/braze-enable-connection.webp>)

To verify if you are receiving deduplicated traits in Braze, see FAQ.

> ![success](/docs/images/tick.svg)
> 
> You can use the deduplication feature when sending data to Braze from your [Event Stream](<https://www.rudderstack.com/docs/sources/event-streams/>) sources via both [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) and [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).
> 
> It also works for [Reverse ETL](<https://www.rudderstack.com/docs/sources/reverse-etl/>) sources.

## How deduplication works

This section explains how the deduplication feature works when sending events in different [connection modes](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/>).

### In device mode

RudderStack stores the previous `identify` object and uses it for comparison - this check occurs directly in the Braze SDK.

### In cloud mode

RudderStack uses the [`/users/export/ids`](<https://www.braze.com/docs/api/endpoints/export/user_data/post_users_identifier/>) endpoint to export data from a user profile by specifying a user identifier.

> ![info](/docs/images/info.svg)
> 
> The `/users/export/ids` endpoint leverages the **users.export.ids** scope in the [REST API key](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/setup-guide/#connection-settings>) used for setting up the Braze destination.

RudderStack then:

  1. Compares the user profile against the incoming user traits to determine any deltas.
  2. If a delta is found, sends only the updated user traits to Braze and drops the others.


### Example

The following example highlights how RudderStack sends deduplicated data to Braze:
    
    
    user_attributes: {
      name: "Alex Keener",
      age: 30,
      location: {
        city: "New York",
        area: "Manhattan",
        country: "US"
      },
      interests: ["hiking", "soccer"]
    }
    
    
    
    user_attributes: {
      name: "Alex Keener",
      age: 30,
      location: {
        city: "San Francisco", // delta
        area: "California", // delta
        country: "US" // delta
      },
      interests: ["hiking", "soccer", "cycling"] // delta
    }
    
    
    
    user_attributes: {
      location: {
        city: "San Francisco",
        area: "California",
        country: "US"
      },
      interests: ["hiking", "soccer", "cycling"]
    }
    

## Attributes considered for deduplication

RudderStack deduplicates only the [billable Braze attributes](<https://www.braze.com/docs/user_guide/data/data_points/?tab=billable>), including custom attributes — it does not deduplicate the following [non-billable attributes](<https://www.braze.com/docs/user_guide/data/data_points/?tab=non-billable>):

RudderStack property| Braze data point| Braze data type  
---|---|---  
`userId`| User ID| Profile data  
`user_alias`| User alias| Profile data  
`country`| Country| Profile data  
`language`| Language| Profile data  
`email_subscribe`| Email subscribed| Contact settings  
`push_subscribe`| Push subscribed| Contact settings  
`subscription_groups`| Subscription group| Contact settings  
  
> ![warning](/docs/images/warning.svg)
> 
> **Important considerations**
> 
>   * Make sure the data type of custom attributes sent in the events is the same as that of the attributes configured in the Braze dashboard.
>   * When sending dates or timestamps as custom attributes, make sure they are in the [Braze-supported format](<https://www.braze.com/docs/api/objects_filters/user_attributes_object#:~:text=true%20or%20false-,Dates,-Must%20be%20stored>).
> 

> 
> Otherwise, the deduplication feature will not work correctly.

## FAQ

#### Which RudderStack Cloud plans support the Braze deduplication feature?

The Braze deduplication feature is available in RudderStack Cloud [Growth and Enterprise](<https://rudderstack.com/pricing>) plans.

#### How do I verify if deduplicated traits are being sent to Braze?

  1. Set up your Braze destination in RudderStack by following these steps.
  2. Create a test `identify` or `track` payload with a new test `userId` in Postman that includes several user traits.


> ![info](/docs/images/info.svg)
> 
> **You can use the RudderStack HTTP API to send the payloads.**
> 
>   1. Import the Postman collection using this [URL](<https://www.getpostman.com/collections/480307c55ad2b9dd4e27>).
>   2. Edit the variable `source_write_key` with the write key of the source connected to your Braze destination.
>   3. Edit the variable `data_plane_url` with your [data plane URL](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>).
>   4. Use **Basic Authentication** for authenticating all HTTP requests.
> 

> 
> See the [RudderStack HTTP API](<https://www.rudderstack.com/docs/api/http-api/>) documentation for more details.

  3. If you don’t have a test payload, you can use the following snippet:


    
    
    {
      "type": "identify",
      "sentAt": "2023-04-15T12:07:41.050Z",
      "traits": {
        "first_name": "John",
        "last_name": "Doe",
        "email": "johndoe@example.com",
        "attribute_a": "value_a",
        "attribute_b": "value_b",
        "myObj": {
          "test": "value"
        },
        "myArr": [
          "value1",
          "value3"
        ]
      },
      "userId": "john@doe",
      "context": {
        "library": {
          "name": "rudder-analytics-php",
          "version": "1.0.1",
          "consumer": "LibCurl"
        }
      },
      "rudderId": "86a09397-07e3-4cc4-9bd3-1fa262a5b521",
      "messageId": "fb203095-df9d-40bd-bcf3-97eb8084fea4",
      "timestamp": "2023-04-15T13:07:39.000+01:00",
      "receivedAt": "2023-04-15T12:07:40.222Z",
      "request_ip": "212.129.29.104",
      "originalTimestamp": "2023-04-15T12:07:41.050Z"
    }
    

  4. Go to the Braze destination in your RudderStack dashboard and click the [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/#destination-live-events>) button. Also, log in to your Braze dashboard.

[![Braze live events button](/docs/images/event-stream-destinations/braze-live-events.webp)](</docs/images/event-stream-destinations/braze-live-events.webp>)

  5. Send the test payloads - you should be able to see them in your Live Events viewer. Also, confirm that the attributes show up as expected in your Braze dashboard by going to the **User Search** tab.
  6. Add or update a few attributes while retaining the rest of the event payload. If you used the event payload in **Step 3** , you can use the following modified payload to test the impact of the attribute changes:


    
    
    {
    "type": "identify",
    "sentAt": "2023-04-15T12:07:41.050Z",
    "traits": {
      "first_name": "John",
      "last_name": "Doe",
      "email": "johndoe@example.com",
      "attribute_a": "value_a.1",
      "attribute_b": "value_b",
      "myObj": {
        "test": "value_changed"
      },
      "myArr": [
        "value1",
        "value3"
      ]
    },
    "userId": "john@doe",
    "context": {
      "library": {
        "name": "rudder-analytics-php",
        "version": "1.0.1",
        "consumer": "LibCurl"
      }
    },
    "rudderId": "86a09397-07e3-4cc4-9bd3-1fa262a5b521",
    "messageId": "fb203095-df9d-40bd-bcf3-97eb8084fea4",
    "timestamp": "2023-04-15T13:07:39.000+01:00",
    "receivedAt": "2023-04-15T12:07:40.222Z",
    "request_ip": "212.129.29.104",
    "originalTimestamp": "2023-04-15T12:07:41.050Z"
    }
    

  7. Resend your event payload. You should see the new event with only the added/updated attributes. You can also confirm in the Braze dashboard that the attributes were added/updated (by going to the **User Search** tab for the same test user ID).


#### I see some custom attributes are not deduplicated even though their values have not changed. Why is this happening?

Make sure the data type of custom attributes sent in the events is the same as that of the custom attributes configured in the Braze dashboard. Otherwise, deduplication will not work.

#### How do I observe the difference in data point billing due to deduplication?

In your Braze dashboard, go to [Subscriptions and usage](<https://www.braze.com/docs/user_guide/administrative/app_settings/subscription_and_usage/?redirected=true>) and check the metrics by the appropriate date filters (before and after enabling deduplication) to observe the data point differences over that period.

#### Does RudderStack support deduplication in case of nested arrays?

RudderStack supports the deduplication of both simple and nested arrays stored as properties.

However, if there are any changes within the nested array or object, RudderStack considers the entire array or object as changed before sending it to Braze.

For example, if you send the below data that is **already** sent previously to Braze, RudderStack deduplicates it and prevents additional data point consumption.
    
    
    {
      "attributes": [{
        "external_id": "userId",
        "pets": [{
            "id": 1,
            "type": "dog",
            "breed": "beagle",
            "name": "Tommy"
          },
          {
            "id": 2,
            "type": "cat",
            "breed": "calico",
            "name": "Garfield"
          }
        ]
      }]
    }
    

However, if you make some changes to the above data, as shown:
    
    
    {
      "attributes": [{
        "external_id": "userId",
        "pets": [{
            "id": 1,
            "type": "cat",
            "breed": "street",
            "name": "Toby"
          },
          {
            "id": 2,
            "type": "cat",
            "breed": "calico",
            "name": "Garfield"
          }
        ]
      }]
    }
    

In that case, RudderStack identifies the entire object as new data and sends it to Braze without any deduplication.