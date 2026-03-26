# Trengo

Send your event data from RudderStack to Trengo.

* * *

  * __5 minute read

  * 


[Trengo](<https://trengo.com/>) is a popular business messaging and communications platform that lets you bring together all your messages via email, SMS, social media, etc. into a single central communication hub. It allows you to set up cross-platform collaborations with your team, automate conversations with your users, and deliver personalized customer experiences.

RudderStack allows you to configure Trengo as a destination to which you can send your event data.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/trengo>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Trengo** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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

Once you have confirmed that the platform supports sending events to Trengo, perform the steps below:

  * From your [RudderStack dashboard](<https://app.rudderlabs.com/>), add the source. Then, select **Trengo** from the list of destinations.
  * Assign a name to the destination and click **Next**. You should then see the following screen:

[![](/docs/images/trengo-config.webp)](</docs/images/trengo-config.webp>)

### Connection Settings

In the **Connection Settings** , you will see the following options:

  * **API Token:** This is a unique token generated for your Trengo account. To generate this API token, you need to select **REST API** from **Apps and Integrations** under the **Settings** option in your Trengo account.
  * **Channel ID:** This corresponds to the unique ID for the channel to which you want to send your data via RudderStack.
  * **Channel Identifier:** Select this option depending on the type of channel you want to send your data.
  * **Enable deduplication for Contacts:** By default, RudderStack will _Deduplicate_ contacts generated from your `identify` events. You can disable this option if you want to create duplicate contacts with same identifier.
  * **Map events with template:** To send `track` events to Trengo, you need to add the `event` to the _Event Name_ field. If you wish to customize the subject for the event, you can do so by adding a _template_.


> ![info](/docs/images/info.svg)
> 
> For a particular event the **Channel ID** can be overriden using `externalId`, For example: `(context.externalId: [{type:trengoChannelId, id:channelId}])`.

> ![warning](/docs/images/warning.svg)
> 
> When using an `externalId` to override _channelId_ , make sure that the **Channel Identifier** of that specific channel matches with the **Channel Identifier** you have selected in RudderStack dashboard.

### Effects on the Identify events

Disabling the option **Enable deduplication for Contacts** will have the following consequences on the `identify` events:

  * RudderStack will not update exising contacts with the same `identifier`.
  * For the channel identifier **phone** :
    * If a contact is present with the same `phone`number as an identifier, it will be duplicated.
    * If you want to store multiple contacts for a particular `phone` number as an identifier for different channels (where the `channel identifiers` are **phone** too), you will need to disable the `deduplication` option from RudderStack dashboard.
  * For the channel identifier **email** :
    * If a contact is present with the same `email` address as an identifier, it will not be duplicated. This is a known destination behavior.
    * For creating multiple contacts with `email` address as an identifer, you need a unique email address.


## Identify

The `identify` call lets you associate a user with their actions and capture all relevant traits about them.

For each `identify` call, RudderStack creates a `contact` using `email` or `phone` as an identifier (depending on the `channel identifier`) using the [Trengo Contact API](<https://developers.trengo.com/reference#create-update-a-user>).

If a contact is already present with same `identifier` (`email`/`phone`), RudderStack will update the contact using the [Trengo Contact API](<https://developers.trengo.com/reference#update-a-user-1>).

A sample `identify` call looks like the following:
    
    
    rudderanalytics.identify("userid", {
      firstName: "Name",
      lastName: "Surname",
      email: "name@website.com",
    })
    

> ![info](/docs/images/info.svg)
> 
> **NOTE:** If you already have Trengo `contactId` you can pass it in `externalId`, `(example context.externalId: [{type:trengoContactId, id:channelId}])`, in that case will we avoid searching for `contactId` using `identifier(email/phone)` before updating.

## Track

The `track` call allows you to capture any action that the user might perform along with the properties associated with that action. Each action is considered to be an event. For every `track` event, RudderStack creates a `ticket` in Trengo using the [Trengo Ticket API](<https://developers.trengo.com/reference#create-a-ticket>).

A sample `track` call looks like the following:
    
    
    rudderanalytics.track("Product Purchased", {
      Clicked_Rush_delivery_Button: true,
      total_value: 2000,
      revenue: 2000,
    })
    

## Mapping Track Events with Trengo’s Event Template

The following table demonstrates the use of the **Map events with template:** option for your `track` events:

**Event Name**| **Event Template**| **Subject Generated**  
---|---|---  
`Product Purchased`| `{{ event }} from our store`| `Product Purchased from our store`  
`Added to cart`| `Product was of value:{{ revenue }}`| `Product was of value:2000`  
`Checked Out`| `Cart was checked out`| `Cart was checked out`  
  
A few things to note while using this option:

  * For particular **Event Name** , the **Event Template** is optional. If left blank, the subject will not generated using the Template. (Note: Subjects are generally used for creating tickets in the channels where the channel identifier is `email`.)
  * For `track` calls, the `contact identifier` is mandatory. For example, for tracking events to an `email` channel, `email` is a mandatory event field. Similarly, for tracking events to a `phone` channel, `phone` is a mandatory event field.


> ![warning](/docs/images/warning.svg)
> 
> For lodging your `track` events to Trengo, it is mandatory to add the `event` name in **Event Name** field. If the **Event Name** is not present, the particular `track` events will not flow through.