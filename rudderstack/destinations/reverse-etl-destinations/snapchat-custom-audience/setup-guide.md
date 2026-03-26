# Setup Guide

Send your event data from RudderStack to Snapchat Custom Audience.

* * *

  * __4 minute read

  * 


This guide will help you set up Snapchat Custom Audience as a destination in RudderStack

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/snapchat_custom_audience>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Cloud, Warehouse, Shopify
  * Refer to it as **Snapchat Custom Audience** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Snapchat Custom Audience, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Snapchat Custom Audience**.
  2. Assign a name to your destination and click **Continue**.


### Connection settings

To successfully configure Snapchat Custom Audience as a destination, first authenticate your account by following the below steps:

  1. Click **Create Account** in the **Account Settings** section.
  2. From the modal, click the **Sign in with Google** button.
  3. Choose the required account and grant RudderStack the required permissions.
  4. Click **Save** to use the specified account:

[![Google Account authentication](/docs/images/event-stream-destinations/cm-360-account-connect-normal.webp)](</docs/images/event-stream-destinations/cm-360-account-connect-normal.webp>)

> ![info](/docs/images/info.svg)
> 
> In case you have authenticated multiple accounts, you can click **Edit Credentials** to select/delete any other authenticated account:
> 
> ![Google Account authentication](/docs/images/event-stream-destinations/cm-360-edit-account-creds.webp)
> 
> RudderStack **gives an error** if you try to delete an account used by any other connection set up for the same destination.

Next, configure the following settings:

  * **Segment ID** : Enter your Snapchat segment ID. For more information on getting your segment ID, refer to the FAQ section below.
  * **Schema** : Select the schema (**EMAIL** , **MOBILE AD ID** , or **PHONE**) from the dropdown.


> ![warning](/docs/images/warning.svg)
> 
> The corresponding field (`email`, `phone`, or `mobileAdId`/`mobile_id`) must be present in your events. Otherwise, RudderStack will not send the events to Snapchat Custom Audience.

  * **Disable hashing** : By default, RudderStack hashes the `email`, `phone`, and `mobileAdId` in the SHA-256 format. If enabled, RudderStack will **not** perform the hashing.


> ![warning](/docs/images/warning.svg)
> 
> If you enable this setting, make sure you [normalize and SHA-256 hash your identifiers](<https://marketingapi.snapchat.com/docs/#normalizing-hashing>) before sending the data to RudderStack.

## `audienceList` event structure

> ![info](/docs/images/info.svg)
> 
> RudderStack supports [additions](<https://marketingapi.snapchat.com/docs/#adding-users>) and [deletions](<https://marketingapi.snapchat.com/docs/#removing-users>) to an audience list.

The following code snippet shows a sample `audienceList` call:
    
    
    {
      "type": "audiencelist",
      "event": "Order Created",
      "sentAt": "2022-06-14T12:34:53.514Z",
      "traits": null,
      "userId": "6201002000600",
      "context": {
        "library": {
          "name": "RudderStack Shopify Cloud",
          "version": "1.0.0"
        },
        "integration": {
          "name": "SHOPIFY"
        }
      },
      "rudderId": "b66112d4-a5af-4856-a6e4-2dbad7104c91",
      "messageId": "99a56bfb-45bf-4852-a911-03f73c3fdcdf",
      "timestamp": "2022-06-14T12:34:48.000Z",
      "properties": {
        "listData": {
          "add": [{
            "email": "alex@example",
            "phone": "+1-202-555-0146",
            "country": "USA",
            "lastName": "Keener",
            "firstName": "Alex ",
            "postalCode": "90009"
          },
            {
              "email": "alexis@example.com",
              "phone": "+1-202-555-0145",
              "country": "USA",
              "lastName": "Alexis",
              "firstName": "Keener",
              "postalCode": "90009"
            }
          ],
          "remove": [{
            "email": "jack@hotmail.com",
            "phone": "+1-202-555-0145",
            "country": "USA",
            "lastName": "Jack",
            "firstName": "Jackson ",
            "postalCode": "90009"
          }]
        }
      },
      "receivedAt": "2022-06-14T12:34:53.113Z",
      "request_ip": "35.231.104.198",
      "anonymousId": "760bf220-046f-4c2a-ad2b-3424be593740",
      "integrations": {
        "SHOPIFY": true
      },
      "originalTimestamp": "2022-06-14T12:34:53.514Z"
    }
    

## Schema fields mapping

The following table details the mapping of the schema fields (as specified in the RudderStack dashboard) and the [Snapchat Marketing API](<https://marketingapi.snapchat.com/docs/?&_ga=2.64649388.22530882.1663148304-88679508.1663136652#create-an-audience-segment>).

RudderStack normalizes the raw identifiers by following the [Snapchat-prescribed rules](<https://marketingapi.snapchat.com/docs/#normalizing-hashing>) before SHA-256 hashing and sending them to Custom Audience.

> ![info](/docs/images/info.svg)
> 
> RudderStack groups the identifiers in batches with a maximum of 100000 identifiers per request. For more information, refer to the [Snapchat Marketing API](<https://marketingapi.snapchat.com/docs/#adding-users>).

RudderStack schema field| Custom Audience field| Notes  
---|---|---  
`properties.listData.add.email`| `users.data.[sha256(email)]`| RudderStack trims any leading and trailing whitespaces and converts all characters into the lower case before hashing.  
`properties.listData.add.phone`  
  
`properties.listData.add.mobile`| `users.data.[sha256(phone)]`  
  
`users.data.[sha256(mobile)]`| RudderStack includes the country code and removes any double 0s in front of it. It also excludes any non-numeric characters like whitespaces, parentheses, `+`, or `-`.  
`properties.listData.add.mobileId`  
  
`properties.listData.add.mobileAdId`  
  
`properties.listData.add.mobile_id`| `users.data.[sha256(mobileId)]`  
  
`users.data.[sha256(mobileAdId)]`  
  
`users.data.[sha256(mobile_id)]`| RudderStack converts all characters into the lower case. It does not remove any hyphens.  
  
> ![warning](/docs/images/warning.svg)
> 
> `email`, `mobileAdId`/`mobile_id`, or `mobile` must be present in your events depending on the **Schema** setting configured in the RudderStack dashboard. Otherwise, RudderStack will not send the events to Snapchat Custom Audience.

## FAQ

#### Where can I find my Snapchat Segment ID?

To get your Snapchat Segment ID, follow the steps below:

  1. Log into your [Snapchat Ads Manager dashboard](<https://ads.snapchat.com/>).
  2. Go to **Assets** > **Audiences**.
  3. Under **Audience Library** , select the required audience.
  4. Copy the ID after `/audiences/custom-audience/` in the URL of the resulting page. This is your segment ID.

[![Snapchat segment ID](/docs/images/event-stream-destinations/snapchat-segment-id.webp)](</docs/images/event-stream-destinations/snapchat-segment-id.webp>)

For example, consider the following URL:
    
    
    https://ads.snapchat.com/cc9c3e81-8a7e-44c0/audiences/custom-audience/1234567890123456/
    

In the above case, `1234567890123456` is the segment ID.

#### How do I create a Customer List Audience in Snapchat?

For detailed steps on creating a Snapchat Customer List Audience, refer to the [Snapchat support page](<https://businesshelp.snapchat.com/s/article/create-sam-audience?language=en_US>).