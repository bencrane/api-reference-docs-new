# ProfitWell Cloud Mode Integration

Send events to ProfitWell using RudderStack Cloud mode.

* * *

  * __3 minute read

  * 


Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/profitwell>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **ProfitWell** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to ProfitWell, follow the steps below:

  * From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. From the list of destinations, select **ProfitWell**.
  * Assign a name to the destination, and click **Next**. You will then see the following **Connection Settings** window:

[![Profitwell connection settings](/docs/images/event-stream-destinations/profitwell-connection.webp)](</docs/images/event-stream-destinations/profitwell-connection.webp>)

### Connection Settings

To successfully configure ProfitWell as a Cloud Mode destination, enter the following connection settings:

  * **Private API Key** : Enter your ProfitWell private API key here. To obtain the **Private API Key** , log into your ProfitWell account. Then, navigate to the **Account Settings** \- **Integration** option. Here, you can get your API key under [API Keys/Dev Kit](<https://www2.profitwell.com/app/account/integrations>), as shown in the following image:

[![Profitwell API key](/docs/images/event-stream-destinations/profitwell-key.webp)](</docs/images/event-stream-destinations/profitwell-key.webp>)

> ![info](/docs/images/info.svg)
> 
> To send events to ProfitWell via cloud mode, you don’t need to enter the **Public API Key**.

  * Finally, click **Next** to complete the setup. ProfitWell should now be configured and enabled as a destination in RudderStack.


## Identify

The `identify` call lets you create or update a subscription for a particular user.

A sample `identify` call is as shown:
    
    
    rudderanalytics.identify(
      "user0001",
      {
        planId: "Starter",
        email: "axel@testmail.com",
        planInterval: "month",
        effectiveDate: 1630645519,
        planCurrency: "USD",
        subscriptionAlias: "starter_axel",
        value: "2000",
        name: "Axel Rose",
        age: 25,
        phone: "+911234665544",
      },
      {
        externalId: [
          { type: "profitwellSubscriptionId", id: "pws_psqfbi9zODBB" },
          { type: "profitwellUserId", id: "pws_MS2g4ON214dU" },
        ],
      }
    );
    

> ![info](/docs/images/info.svg)
> 
> RudderStack passes the fields `profitwellUserId` and `profitwellSubscriptionId` as `externalId`.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * The `externalId` of type `profitwellUserId` is mapped to ProfitWell’s `user_id` field.
>   * The `externalId` of type `profitwellSubscriptionId` is mapped to ProfitWell’s `subscription_id` field.
> 


### Identify Mapping

This section lists the various criteria for mapping RudderStack fields to ProfitWell fields.

The following table lists all supported fields for **`Creating Subscriptions`** with their relative mapping to the ProfitWell fields:

**RudderStack Field**| **ProfitWell Field**  
---|---  
`userId`| `user_alias`  
`subscriptionAlias`| `subscription_alias`  
`email`| `email`  
`planId`| `plan_id`  
`planInterval`| `plan_interval`  
`planCurrency`| `plan_currency`  
`status`| `status`  
`value`| `value`  
`effectiveDate`| `effective_date`  
  
The following table lists all supported fields for **`Updating Subscriptions`** with their relative mapping to the ProfitWell fields:

**RudderStack Field**| **ProfitWell Field**  
---|---  
`planId`| `plan_id`  
`planInterval`| `plan_interval`  
`value`| `value`  
`status`| `status`  
`effectiveDate`| `effective_date`  
  
> ![info](/docs/images/info.svg)
> 
> While creating a subscription, if `effectiveDate` is not provided in the `identify` call, then RudderStack takes the date from the event call’s `timestamp`/`originalTimestamp`.

> ![info](/docs/images/info.svg)
> 
> For more information on using these fields, refer to the [ProfitWell documentation](<https://profitwellapiv2.docs.apiary.io/#>).

RudderStack discards the `identify` event in the following two scenarios:

  * For a given `profitwellUserId`, a user account is not found in ProfitWell.
  * For a given `profitWellUserId`, a `profitwellSubscriptionId` is not found.


> ![info](/docs/images/info.svg)
> 
> If you provide a `userId`(mapped to `user_alias` in ProfitWell) or a `subscriptionAlias` (mapped to `subscription_alias`) in the `identify` call, a new user subscription is created if it is not already present.

## FAQ

#### Where do I get the API Key for ProfitWell?

To obtain your ProfitWell **Private API Key** , log into your ProfitWell dashboard. Navigate to the **Account Settings** \- **Integration** option. Here, you can get your API key under [API Keys/Dev Kit](<https://www2.profitwell.com/app/account/integrations>), as shown in the following image:

[![Profitwell API key](/docs/images/event-stream-destinations/profitwell-key.webp)](</docs/images/event-stream-destinations/profitwell-key.webp>)