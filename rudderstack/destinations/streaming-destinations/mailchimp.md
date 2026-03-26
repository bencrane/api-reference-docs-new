# Mailchimp Destination

Send your event data from RudderStack to Mailchimp.

* * *

  * __6 minute read

  * 


> ![announcement](/docs/images/announcement.svg)
> 
> **The RudderStack Mailchimp integration is experiencing intermittent issues.**
> 
> Not all customers are experiencing these issues. Our engineering team is actively working on a fix. For questions, contact [RudderStack Support](<mailto:support@rudderstack.com>).

[Mailchimp](<https://mailchimp.com/>) is a popular email marketing automation platform used worldwide by thousands of businesses. Built specially for eCommerce and retail, Mailchimp allows you to build your audience and send them personalized campaign and marketing messages through web or mobile.

RudderStack supports Mailchimp as a destination to which you can seamlessly send your event data. Also, you can add people to your Mailchimp list via a simple `identify` call.

Find the open-source transformer code for this destination in our [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/mailchimp>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Mailchimp** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Mailchimp, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Mailchimp**.
  2. Assign a name to the destination and click **Continue**.


### Connection settings

To successfully configure Mailchimp as a destination, you will need to configure the following settings:

[![](/docs/images/event-stream-destinations/mailchimp-connection-settings.webp)](</docs/images/event-stream-destinations/mailchimp-connection-settings.webp>)

  * **Mailchimp API Key** : Enter your Mailchimp API Key.


> ![info](/docs/images/info.svg)
> 
> It is recommended to create a new API key for the RudderStack destination. Mailchimp restricts each API key to a maximum of 10 concurrent requests. Hence, creating a dedicated key for RudderStack ensures maximum throughput for the outgoing calls. Refer to the [Mailchimp documentation](<https://mailchimp.com/help/about-api-keys/>) for more detaails.

  * **Mailchimp Audience ID** : Enter your Mailchimp Audience ID.
  * **Mailchimp DataCenter ID** : Enter your Mailchimp DataCenter ID.
  * **Enable Merge fields** : Enable this setting if you want to add merge fields while updating a subscriber.


> ![info](/docs/images/info.svg)
> 
> Refer to the FAQ section for more information on how to get the above details.

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call captures the details about the visiting user along with the properties associated with that user.

### Adding or updating a user

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4el9Zt1WSfVJIVo4GRlm", {
        firstName: "Alex",
        lastName: "Keener",
        email: "alex@example.com"
    });
    

Every time an `identify` call is made including an email address, RudderStack performs the following steps:

  * RudderStack first checks with Mailchimp whether that specific email address exists for the `listId` provided in the destination settings.
  * If the email address does not exist in the list, RudderStack subscribes the associated user to the list immediately. If the `doubleOptIn` setting is enabled, Mailchimp sends a confirmation email to that user, and that email is tagged with a `pending` subscriber status. The subscriber status automatically changes to `subscribed` once the user confirms the email.
  * If the user already has a subscriber status such as `pending`, `subscribed`, `unsubscribed` or `cleaned`, RudderStack will **not** resubscribe them, but only update their associated user traits.


> ![info](/docs/images/info.svg)
> 
> `email` is a required field for the `identify` call. The rest of the fields must match the **Merge Field** tag in Mailchimp.

### Capture custom user traits

You can capture the custom user traits in the Mailchimp list dashboard by creating a custom merge field in Mailchimp.

> ![info](/docs/images/info.svg)
> 
> Mailchimp supports merge tags only up to 10 characters. Hence, every user trait sent inside the `identify` call is trimmed to the first 10 characters and converted to uppercase before being sent to Mailchimp. Also, the `Merge Tags` is created by taking the 10 characters (excluding whitespace/special characters) of its `Field Label`.  
>   
> For example, if you set the `Field Label` as `Upto 10-Char`, the `Merge Tag` will be `UPTO10CHAR`. The `user.trait` inside your `identify` call, which is, `Upto 10-Char`, will be converted to `UPTO10CHAR` before being sent to Mailchimp.

### Creating custom merge fields

> ![info](/docs/images/info.svg)
> 
> Create custom merge fields only for the traits you want to see in your list view and not for all `user.traits`.

To create and send custom merge fields or user traits to Mailchimp, please follow these steps:

  * Create the merge field in Mailchimp for every trait you want sent to it.
  * When you make the `identify` call, the keys that match the traits above will automatically appear in your Mailchimp list.


> ![info](/docs/images/info.svg)
> 
> The `identify` call will **not change** in this case.

### Overriding `listId`

If you have multiple lists that your users can subscribe to, you can override the default `listId` as a parameter to Mailchimp.

The following sample snippet overrides the default `listId` with `esf1rd234a` as `listId`:
    
    
    rudderanalytics.identify(
      "1hKOmRA4el9Zt1WSfVJIVo4GRlm",
      {
        email: "alex@example.com"
      },
      {
        integrations: {
          Mailchimp: {
            listId: "esf1rd234a"
          }
        }
      }
    );
    

### Updating the subscription status

RudderStack provides you with the option to manually update the subscription status of a user by passing the `subscriptionStatus` parameter to Mailchimp.

An example is shown below:
    
    
    rudderanalytics.identify(
      "1hKOmRA4el9Zt1WSfVJIVo4GRlm",
      {
        email: "alex@example.com"
      },
      {
        integrations: {
          Mailchimp: {
            subscriptionStatus: "unsubscribed"
          }
        }
      }
    );
    

> ![info](/docs/images/info.svg)
> 
> This setting will **NOT** work for new users. For new users, the subscription status will always be set as `pending` or `subscribed`, depending on the set `doubleOptIn` setting.

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to track user actions or [trigger targeted automations](<https://mailchimp.com/developer/marketing/guides/track-outside-activity-events/#trigger-automations-with-events>) in Mailchimp using their [Events](<https://mailchimp.com/developer/marketing/api/list-member-events/>) API.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("registered_referral", {
      "referee_id": "1233",
      "referral_acceptance": "accepted",
      "email": "alex@example.com"
    })
    

> ![info](/docs/images/info.svg)
> 
> `email` is a required field for making a `track` call successfully. You can pass it in either `traits.email`, `ucontext.traits.email`, or `properties.email`. RudderStack hashes the `email` field and replaces `subscriber_hash` in the [Mailchimp Events API endpoint](<https://mailchimp.com/developer/marketing/api/list-member-events/>).

### Supported mappings

The following table lists the mappings between the RudderStack and Mailchimp properties:

RudderStack property| Mailchimp property| Notes  
---|---|---  
`event`  
Required| `name`| Event name must contain 2-30 characters.  
`properties`| `properties`| -  
`properties.isSyncing`| `is_syncing`| RudderStack triggers the [targeted automations](<https://mailchimp.com/developer/marketing/guides/track-outside-activity-events/#trigger-automations-with-events>) by default. However, you can set `isSyncing` to `true` if you don’t want to trigger them.  
`originalTimestamp`| `occurred_at`| -  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack stringifies all values received in `properties[key]` as Mailchimp only accepts the string values in `properties[key]`.

## FAQ

#### Where do I get the Mailchimp API Key?

To get the Mailchimp API Key, log in to Mailchimp, and go to **Account** > **Extras** > **API Keys**.

#### Where do I get the Mailchimp Audience ID?

You can find the Mailchimp Audience ID by logging in to Mailchimp and navigating to **Audience** > **Manage Audience** > **Settings** > **Audience name and defaults**.

#### Where do I get the Mailchimp DataCenter ID?

To get the DataCenter ID, please refer to your Mailchimp URL in the browser. For example, if the URL is `https://us20.admin.mailchimp.com/lists`, the DataCenter ID is `us20` in this case.