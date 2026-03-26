# Zendesk

Send data from RudderStack to Zendesk.

* * *

  * __6 minute read

  * 


[Zendesk](<https://www.zendesk.com/>) is a popular CRM and customer support service suite. It offers features like live chat, call center software capabilities, and a smart knowledge base for your executives to help them resolve customers’ queries and concerns.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/zendesk>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Zendesk** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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

Once you have confirmed that the source platform supports sending events to Zendesk, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Zendesk**.
  2. Assign a name to your destination and click **Continue**.


### Connection settings

To successfully configure Zendesk as a destination, you need to configure the following settings:

  * **Email** : Enter the email address used to log in to your Zendesk account.
  * **API Token** : Enter the Zendesk API token used to authenticate the integration. To generate a new API token, see the [Zendesk support article](<https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token->).
  * **Zendesk Subdomain** : Enter your Zendesk subdomain **excluding** `.zendesk.com`.
  * **Source Name** : Enter the events source name. If not specified, RudderStack sets this field to `Rudder` by default.
  * **Create users as verified** : Enable this setting to create verified users in Zendesk. When enabled, RudderStack sends `verified` as `true` in the event and Zendesk skips the email verification for these users.
  * **Send Group calls without User ID** : Enable this setting if you do not want to associate a particular user with a group. When enabled, RudderStack creates or updates a group only if `userId` is **not** present in the event.
  * **Enable Removing Users from Organizations** : Enable this setting to remove users from an organization via the `identify` call. For more information on this setting, see Removing users from an organization section below.
  * **Update user’s primary email** : Enable this setting to set the email present in the event as the user’s primary email in Zendesk, replacing the previously-set primary email. For more information on this setting, see Updating user’s primary email in Zendesk section below.


  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create or update a user in Zendesk.

> ![info](/docs/images/info.svg)
> 
> It is highly recommended to include the user’s `email` in the `identify` call as RudderStack uses this field to create or update a user in Zendesk.
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
      country: "USA",
    });
    

RudderStack persists the user details from the `identify` call for all subsequent calls made to Zendesk.

### Supported mapping

RudderStack maps the following event properties to the standard Zendesk user attributes:

**RudderStack property**| **Zendesk attribute**  
---|---  
`name`  
Required| `name`  
`email`  
Optional, but recommended| `email`  
`organizationId` / `company.id`| `organization_id`  
`timezone`| `time_zone`  
`phone`| `phone`  
`userId`| `user_id`  
`userId`| `external_id`  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack creates a new custom field in Zendesk for any other unmapped attributes.

### Removing users from an organization

Enable the **Enable Removing Users from Organizations** setting in the dashboard to use this feature.

To remove a user from an organization, the following fields must be present in the `identify` [`traits`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/#sample-payload>):

  * `company.id`
  * `company.remove` (set to `true`)


A sample `identify` call for this action is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm",{
      name: "Alex Keener",
      email: "alex@example.com",
      country: "USA",
      company:{
        id: 900001329943,
        remove: true
      }
    });
    

The above `identify` call updates the user (if they exist) as well as removes them from the organization associated with the ID `900001329943`.

RudderStack assumes a valid Zendesk `organization_id` in the `company.id` field. Then, it finds the organization corresponding to that ID and removes the user.

### Updating user’s primary email in Zendesk

To set the email present in the event as the user’s primary email in Zendesk, enable the **Update user’s primary email** dashboard setting and pass the `email` trait in the `identify` call:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
      country: "USA",
    });
    

When you send the above event, Zendesk sets `alex@example.com` as the user’s primary email.

If the **Update user’s primary email** dashboard setting is disabled, RudderStack sets the `email` present in the `identify` traits as the user’s secondary email in Zendesk, **if** any primary mail already exists.

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record the user actions along with any associated properties and send this information to Zendesk.

You need to first set the `userId` by calling `identify` before sending any `track` events to Zendesk.

> ![info](/docs/images/info.svg)
> 
> Zendesk expects a `userId` for every `track` call.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      userId: "1hKOmRA4GRlm"
      currency: "USD",
      revenue: 77,
      value: 99.99,
    });
    

> ![info](/docs/images/info.svg)
> 
> RudderStack uses the [Zendesk Events API](<https://developer.zendesk.com/rest_api/docs/sunshine/events_api>) to send the `track` calls.

## Group

You can use the [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call to create or update an organization in Zendesk. RudderStack uses the `groupId` to do this.

A sample `group` call is shown below:
    
    
    rudderanalytics.group("group01", {
      name: "Softworks",
      country: "UK",
      group_plan: "trial",
    });
    

### Associating user to an organization

You can also use the `group` call to associate a particular user to an organization. To do so, disable the **Send Group Calls without User ID** dashboard setting in RudderStack and pass the `userId` via the `identify` call before sending any `group` calls to Zendesk.

> ![info](/docs/images/info.svg)
> 
> RudderStack assumes that an `identify` call (containing the `userId`) is made before any `group` call.

If you do not want to associate a particular user with a group, enable the **Send Group Calls without User ID** dashboard setting. If this setting is enabled, the group will be created or updated only if `userId` is **not** present in the event.

### Standard mapping

RudderStack maps the following **optional** `group` traits to the standard Zendesk organization attributes:

**RudderStack**| **Zendesk**  
---|---  
`name`| `name`  
`domainNames`| `domain_names`  
`tags`| `tags`  
`groupId`| `external_id`  
`url`| `url`  
`deleted`| `deleted`  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack creates a new custom field in Zendesk for any other unmapped attributes.

### How RudderStack does the user-organization association

  * If both `userId` and `groupId` are present in the `group` event, then RudderStack first finds the user by looking for the `email` field present in the [`context.traits`](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/#contextual-fields>) object.

    * If `email` is present, then RudderStack associates the user with the `organizationId` and sends all user information for this call.
    * If `email` is absent, RudderStack creates the user. It will then find the organization associated with the `groupId` present in the payload.
  * If `groupId` is absent in the event payload, RudderStack creates a new organization in Zendesk and then does the association.


The above discussion can be summarized as follows:

`email` present?| `groupId` present?| Description| Expected behavior  
---|---|---|---  
No| No| User and the organization do not exist in Zendesk.| RudderStack creates a new user and organization and associates both.  
Yes| No| User already exists in Zendesk but not the organization.| RudderStack creates a new organization and associates the existing user information with it.  
No| Yes| Organization already exists in Zendesk but not the user.| RudderStack creates a new user and associates them with the organization.  
Yes| Yes| Both the user and the organization exist in Zendesk.| RudderStack does the user-organization association.