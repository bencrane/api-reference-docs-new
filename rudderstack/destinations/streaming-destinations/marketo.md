# Marketo Destination

Send your event data from RudderStack to Marketo.

* * *

  * __6 minute read

  * 


[Marketo](<https://marketo.com>) is a leading marketing automation platform that lets you identify the right audiences through effective behavioral tracking and deliver automated, personalized marketing campaigns.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/marketo>).

## Setup

> ![warning](/docs/images/warning.svg)
> 
> Before setting up the Marketo destination in RudderStack, you must create two fields in Marketo with the API names exactly as `userId` and `anonymousId`. RudderStack looks up the Marketo Lead objects using these properties.
> 
> **Without these two fields, all events will fail**.

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **Marketo**.
  2. Connect your source and click **Continue**.


### Connection settings

Configure the following settings to set up Marketo as a destination in RudderStack:

  * **Name** : Assign a name to uniquely identify the destination.
  * **Munchkin Account ID** : Enter your Munchkin account ID. You can find the Munchkin Account ID by logging into your Marketo instance and going to **Admin** > **Integration** > **Munchkin**. Your Munchkin ID is listed on the main screen in the **Tracking Code** section. For more information, see the [Marketo documentation](<https://nation.marketo.com/t5/knowledgebase/how-to-find-your-munchkin-id-for-a-marketo-instance/ta-p/248432>).
  * **Client ID** : Enter your Marketo client ID.
  * **Client Secret** : Enter your Marketo client secret.


> ![info](/docs/images/info.svg)
> 
> You can find the client ID and client secret by logging into your Marketo instance and going to **Admin** > **Integration** > **LaunchPoint**. Select the API service and click **View Details** to get the credentials. For more information, see the FAQ section below.

### Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Marketo** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
  
### Configuration settings

After completing the initial setup, configure the following settings to correctly receive your data in Marketo:

#### Custom Activity Settings

  * **Track anonymous events** : Turn on this setting to track events that don’t contain a `userId`.


> ![warning](/docs/images/warning.svg)
> 
> If you disable this setting, events that don’t contain the `userId` field will automatically fail.

  * **Create lead if it does not exist** : RudderStack creates a new Marketo lead if the user is not present. This setting is turned on by default.


#### Consent settings

  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


### Mappings

The following settings are associated with the `track` events and require you to first [create a Custom Activity in Marketo](<https://experienceleague.adobe.com/docs/marketo/using/product-docs/administration/marketo-custom-activities/create-a-custom-activity.html>) before sending an event. You also need to approve the activity in order to get the **Custom Activity ID**.

#### **Custom events**

> ![success](/docs/images/tick.svg)
> 
> You can also use the JSON mapper to set up these mappings.

  * **Map events to Marketo Activity ID and Primary Key** : Use this setting to map the event name in `track` call to Marketo’s custom activity ID and the primary key associated with the custom activity. For example, you can map a **Product Clicked** event to a custom activity with primary field `product_id` and activity ID **100001**.


> ![info](/docs/images/info.svg)
> 
> The primary field for Marketo’s custom activity is marked with an asterisk (`*`).

#### **Lead trait mapping**

  * **Map your traits to Marketo custom fields** : RudderStack maps some of the user traits to the custom Marketo fields by default (listed in the Supported mappings section). You can use this setting to override the default mappings or map any other traits to the custom Marketo fields.


For custom Marketo fields, you can use the [list of standard Marketo fields](<https://developers.marketo.com/rest-api/lead-database/fields/list-of-standard-fields/>) (REST API Name column) or any other custom field names existing in your lead records.

#### **Custom activity property map**

  * **Map your event properties to Marketo custom activity’s field** : Use this setting to map your `track` event properties to the Marketo fields listed in your custom activity.


For example, you can map **Product Clicked** event’s `product_name` property to the Marketo’s `productName` field for the custom activity **Product Wishlisted**.

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create or update a Lead object in Marketo.

A sample `identify` call is as shown:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      first_name: "Alex",
      last_name: "Keener",
      email: "alex@example.com",
    })
    

### Supported mappings

By default, RudderStack maps the following `traits` to the Marketo fields:

RudderStack trait| Marketo field  
---|---  
`address.city`| `city`  
`company.name`| `company`  
`address.country`| `country`  
`email`| `email`  
`firstName`| `firstName`  
`company.industry`| `industry`  
`lastName`| `lastName`  
`leadSource`| `leadSource`  
`company.employee_count`| `numberOfEmployees`  
`phone`| `phone`  
`address.zip`| `postalCode`  
`rating`| `rating`  
`address.state`| `state`  
`address.street`| `address`  
`title`| `title`  
`birthday`| `dateOfBirth`  
`website`| `website`  
  
> ![info](/docs/images/info.svg)
> 
> For the rest of the fields that you want to sync with Marketo, you can create a mapping of your traits and custom Marketo fields in the RudderStack dashboard, as specified in the Lead Mapping settings section.

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events to register custom activities in Marketo.

> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * Make sure to first [create the custom activities in Marketo](<https://experienceleague.adobe.com/docs/marketo/using/product-docs/administration/marketo-custom-activities/create-a-custom-activity.html>) before sending the events. Also, approve the activity in Marketo to get the **Custom Activity ID**.
>   * If you are using [RudderStack Open Source](<https://app.rudderstack.com/signup?type=opensource>), make sure to update your [transformer](<https://github.com/rudderlabs/rudder-transformer>) version to v1.51.1 or later to send your `track` events to Marketo correctly.
> 


A sample `track` call is as shown in the snippet below:
    
    
    rudderanalytics.track("Order Completed", {
      checkout_id: "C324532",
      order_id: "T1230",
      value: 15.98,
      revenue: 16.98,
      shipping: 3.0,
      coupon: "FY21",
      currency: "INR",
    })
    

> ![info](/docs/images/info.svg)
> 
> Refer to the [Custom Activity Settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/marketo/#custom-activity-settings>) section for more information on mapping the `track` events.

## FAQ

#### Why are my requests failing with the message “Lookup failed”?

Make sure you have created two fields in Marketo with the names `userId` and `anonymousId`, so that RudderStack can look up the Marketo lead database for `leadId` with the `userId` that are passed along with the event.

#### Why are my `track` events failing?

  * Make sure you have created two fields in Marketo with the API names exactly as `userId` and `anonymousId`. RudderStack looks up the Marketo lead objects using these properties. Without these two fields, all events will fail.
  * If you’re sending `track` events without `userId`, make sure you have turned on the `Track Anonymous events` setting in the RudderStack dashboard. If this setting is disabled, events that don’t contain the `userId` field will fail.


#### How do I obtain the Marketo client ID and secret?

To set up the Marketo API service and obtain the client ID and secret associated with it, follow these steps:

  1. Log into your Marketo instance and click the **Admin** tab.
  2. Select **LaunchPoint**.

[![](/docs/images/event-stream-destinations/marketo-launchpoint.webp)](</docs/images/event-stream-destinations/marketo-launchpoint.webp>)

  3. Here, you will able to see all installed services used for connecting to Marketo.

[![](/docs/images/event-stream-destinations/marketo-services.webp)](</docs/images/event-stream-destinations/marketo-services.webp>)

  4. To create a new service, click **New** > **New Service**.
  5. Enter the **Display Name**. From the **Service** dropdown, select **Custom**.
  6. Under **Settings** , enter the **Description** and select the **API Only User** , as shown. Finally, click **CREATE**.

[![](/docs/images/event-stream-destinations/marketo-services.webp)](</docs/images/event-stream-destinations/marketo-services.webp>)

> ![warning](/docs/images/warning.svg)
> 
> Make sure the **API Only User** associated with the API service has the necessary permissions to create or update contacts as wellas the custom activities.

Once the setup is complete, you should have the client ID and client secret for the API service. Use this to configure the Marketo destination in RudderStack.

[![](/docs/images/event-stream-destinations/marketo-service-details.webp)](</docs/images/event-stream-destinations/marketo-service-details.webp>)  


#### How do I create a custom activity in Marketo?

For a step-by-step guide on creating a custom activity in Marketo, refer to this [Marketo documentation](<https://experienceleague.adobe.com/docs/marketo/using/product-docs/administration/marketo-custom-activities/create-a-custom-activity.html>).