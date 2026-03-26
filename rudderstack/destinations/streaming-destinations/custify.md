# Custify

Send your event data from RudderStack to Custify.

* * *

  * __5 minute read

  * 


[Custify](<https://www.custify.com/>) is a next-generation Customer Success software for B2B SaaS companies. It helps you meet your customers’ needs by reducing user churn and increasing their lifetime value. With Custify, you can get insights on product usage and all data from your CRM, support, billing, and other systems in one place.

RudderStack supports Custify as a destination where you can seamlessly send your customer data.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/custify>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Custify** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Custify, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Custify**.
  2. Assign a name to the destination and click **Continue**.


### Connection settings

To successfully configure Custify as a destination, you need to configure the following settings:

[![Custify connection settings](/docs/images/event-stream-destinations/custify-connection-settings.webp)](</docs/images/event-stream-destinations/custify-connection-settings.webp>)

  * **API Key** : This is a mandatory field. Enter the Custify API key used to authenticate the request.


> ![info](/docs/images/info.svg)
> 
> To create an API key, go to the [Custify API Access page](<https://app.custify.com/settings/developer/api-key>) and click **Generate API key**.

  * **Fall back to anonymousId if userId is not present** : If this setting is enabled, RudderStack will use `anonymousId` to identify the user if `userId` is not present in the event.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create or update a user in Custify. RudderStack uses the `userId` or `email` field in the event’s `traits` to do so. Hence, it is highly recommended to include the `userId` or at least the user’s `email` in the `identify` call.

You can also identify your users with `anonymousId` in case `userId` is not present in the event via the **Fall back to anonymousId if userId is not present** dashboard setting.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
      country: "USA"
    });
    

### Supported mapping

RudderStack maps the following event properties to a subset of the standard Custify user attributes. It also creates a new custom field for the unmapped attributes.

RudderStack property| Custify property| Presence  
---|---|---  
`userId` (or `anonymousId` if `userId` is absent)| `user_id`| Required  
`traits.email` / `context.traits.email`| `email`| Required, if `userId` or `anonymousId` is absent.  
`traits.phone` / `context.traits.phone`| `phone`| Optional  
`traits.sessionCount` / `context.traits.sessionCount`| `session_count`| Optional  
`traits.unsubscribedFromEmails` / `context.traits.unsubscribedFromEmails`| `unsubscribed_from_emails`| Optional  
`traits.unsubscribedFromCalls` / `context.traits.unsubscribedFromCalls`| `unsubscribed_from_calls`| Optional  
`traits.name` / `context.traits.name`| `name`| Optional  
`traits.signedUpAt` / `context.traits.signedUpAt` / `timestamp` / `originalTimestamp`| `signed_up_at`| Optional  
`traits` / `context.traits`| `custom_attributes`| Optional  
  
### Removing users from an organization

To remove a given user from an organization, the following fields must be present in the event’s `context.traits`:

  * `company.id`
  * `company.remove` (set to `true`)


RudderStack assumes a valid Custify `company_id` in the `company.id` field. Then, it finds the organization corresponding to that ID and dissociates the user from the organization.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
      country: "USA",
      company: {
        id: "company_123",
        remove: true
      }
    });
    

The above `identify` call updates the user as well as removes them from the company having the `id` as `company_123`.

## Track

RudderStack uses the [Custify Events API](<https://docs.custify.com/#tag/Event>) to send the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events generated by the users’ actions.

> ![info](/docs/images/info.svg)
> 
> Custify expects a `userId` for every `track` call. You can set the `userId` by making an `identify` call before sending any `track` events.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      category: "category",
      label: "label",
      value: 120
    });
    

### Supported mapping

The following table lists the supported property mappings between RudderStack and Custify for the `track` events:

RudderStack property| Custify property  
---|---  
`userId` / `anonymousId`| `user_id`  
`email`| `email`  
`event`| `name`  
`timestamp` / `originalTimestamp`| `created_at`  
  
## Group

You can use the [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call to create or update a company in Custify and associate a user to it.

RudderStack assumes that an `identify` call (containing the `userId`) is made before any `group` call. It uses the `groupId` to uniquely identify a group.

A sample `group` call is shown below:
    
    
    rudderanalytics.group("group01", {
      traits: {
        "name": "Tech Group",
        "size": 150,
        "plan": "Pro"
      },
      context: {
        "traits": {
          "name": "Alex Keener",
          "email": "alex@example.com"
        }
      },
    });
    

### Supported mapping

RudderStack maps the following **optional** `group` traits to a subset of the standard Custify company attributes. It also creates a new custom field for any unmapped attributes.

RudderStack property| Custify property  
---|---  
`groupId`| `company_id`  
`traits.name`| `name`  
`traits.industry`| `industry`  
`traits.size`| `size`  
`traits.website` / `traits.url`| `website`  
`traits.plan`| `plan`  
`traits.monthlyRevenue` / `traits.mrr`| `monthly_revenue`  
`traits.churned`| `churned`  
`traits`| `custom_attributes`  
  
### How RudderStack does the user-organization association

To do the user-company association, RudderStack first finds the Custify user by looking for the `userId` present in the [`context.traits`](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/#contextual-fields>) object.

  * If `userId` and `groupId` are present in the event, RudderStack associates the Custify user with the organization and sends all user-specific information.
  * If `userId` and `groupId` are not present, RudderStack first creates the user and the organization in Custify and then does the association.


The above discussion can be summarized as follows:

`userId` present?| `groupId` present?| Description| Expected behavior  
---|---|---|---  
No| No| User and the organization do not exist in Custify.| RudderStack creates a new user and organization in Custify and associates both.  
No| Yes| Organization exists in Custify but not the user.| RudderStack creates a new user and associates them with the organization.  
Yes| No| User exists in Custify but not the organization.| RudderStack creates a new organization and associates the user with it.  
Yes| Yes| Both the user and the organization exist in Custify| RudderStack does the user-organization association.