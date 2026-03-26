# Intercom API v2.10 Migration Guide

Configuration changes and differences in sending events when migrating from Intercom API v1.4 to v2.10.

* * *

  * __4 minute read

  * 


This guide covers the steps to migrate your Intercom [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) integration from Intercom API v1.4 to v2.10.

## Step 1: Change Intercom API version

In the Intercom [destination settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/intercom/#connection-settings>), change the **Intercom REST API Version** [connection setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/intercom/#connection-settings>) from **1.4** to **latest**.

## Step 2: Review connection settings

Once you set the **Intercom REST API Version** to **latest** , note that the following configuration setting will not be visible in the RudderStack dashboard as it is **no longer supported** in Intercom API v2.10:

Setting| Comments  
---|---  
Enable this to update the last seen to the current time| Used to enable the `update_last_request_at` parameter in Intercom.  
  
Instead, the following new connection setting is added:

Setting| Comments  
---|---  
API Server| Your Intercom workspace server.  
  
By default, RudderStack sets it to **Standard** (US) and provides two other options: **EU** (Europe) and **AU** (Australia).  
  


> ![warning](/docs/images/warning.svg)If your Intercom regional hosting is either **EU** or **AU** , make sure to update this setting in the dashboard.  
  
## Step 3: Review instrumentation changes

After reviewing the configuration changes, follow these sections to send your events to Intercom correctly:

### Send custom attributes

> ![warning](/docs/images/warning.svg)
> 
> If you’re migrating your Intercom destination integration from v1.4 to the latest version v2.10, make sure that the custom attributes that you wish to send to Intercom via the `identify` and `group` events are already defined in the Intercom dashboard. Otherwise, your events might fail.

RudderStack supports sending custom attributes (`custom_attributes`) to Intercom at a user and company level (via `identify` and `group` calls).

In the older integrations leveraging the Intercom API v1.4, you could send a custom attribute that was not defined in the Intercom dashboard already. Intercom did not validate the attribute and created a new custom attribute instead.

In the new integration that leverages the Intercom API v2.10, Intercom validates the custom attributes first, meaning it throws an error if a custom attribute present in the event is not already defined in the Intercom dashboard.

See the [Intercom documentation](<https://www.intercom.com/help/en/articles/179-send-custom-user-attributes-to-intercom>) for more information on creating and sending custom attributes to Intercom.

#### Use case

The following use case highlights how RudderStack considers and sends custom attributes to Intercom in the new API implementation.

Suppose you send the following `identify` event to Intercom:
    
    
    rudderanalytics.identify(
      "alex98", {
        name: "Alex Keener",
        createdAt: "2024-01-05T19:11:00.337Z",
        email: "alex@example.com",
        phone: "+800 555‑0100",
        address: {
          city: "New Orleans",
          state: "Louisiana",
        },
        plan: "enterprise",
      }, {
        integrations: {
          INTERCOM: {
            lookup: "phone",
          },
        },
      });
    

RudderStack extracts the following standard Intercom attributes from the event payload and considers all the other attributes as custom attributes:

  * `userId`
  * `email`
  * `phone`
  * `name`
  * `createdAt`


If the custom attributes are a part of an object, then RudderStack flattens them, so the `custom_attribute` object in the final event payload sent to Intercom looks like the following:
    
    
    "custom_attributes": {
      "address_city": "New Orleans",
      "address_state": "Louisiana",
      "plan": "enterprise"
    }
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure to create all the above custom attributes in the Intercom dashboard to successfully send the events.

**Reference: Standard Intercom attributes for`identify` and `group` calls**  
**Identify**  


  * `userId`
  * `role`
  * `email`
  * `phone`
  * `name`
  * `avatar`
  * `company`
  * `ownerId`
  * `lastName`
  * `lastname`
  * `firstName`
  * `firstname`
  * `createdAt`
  * `timestamp`
  * `lastSeenAt`
  * `originalTimestamp`
  * `unsubscribedFromEmails`

**Group**  


  * `tags`
  * `size`
  * `plan`
  * `name`
  * `email`
  * `userId`
  * `website`
  * `industry`
  * `segments`
  * `userCount`
  * `createdAt`
  * `sessionCount`
  * `monthlySpend`
  * `remoteCreatedAt`


### Attribute lookup

RudderStack supports user lookup in the `identify` and `group` calls. By default, it does a lookup based on the user’s `email`. However, you can change this behavior by passing the required field in the `integrations` object.

A sample `identify` call highlighting the user lookup feature is shown below:
    
    
    rudderanalytics.identify(
      "alex98", {
        name: "Alex Keener",
        email: "alex@example.com",
        phone: "+800 555‑0100"
      }, {
        integrations: {
          INTERCOM: {
            lookup: "phone",
          },
        },
      });
    

Note that:

  * You can only send the [fields accepted by Intercom](<https://developers.intercom.com/docs/references/rest-api/api.intercom.io/contacts/searchcontacts#section/Accepted-Fields>) for user lookup. **These fields are case sensitive**.
  * The field you are passing for lookup must be present in the event’s `context.traits` object.


### Send last seen timestamp

In the older implementation leveraging Intercom API v1.4, RudderStack supported the **Enable this to update the last seen to the current time** dashboard setting that lets you enable the last seen timestamp (`update_last_request_at` parameter) for a contact in Intercom.

This feature is no longer supported in the new Intercom API v2.10. To update the last seen timestamp of a contact, you will need to include the `lastSeenAt` field in the event.