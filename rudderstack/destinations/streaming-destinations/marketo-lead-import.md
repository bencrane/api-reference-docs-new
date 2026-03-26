# Marketo Lead Import Beta

Send your leads data from RudderStack to Marketo.

* * *

  * __3 minute read

  * 


[Marketo](<https://marketo.com>) is a leading marketing automation platform. It lets you identify the right audiences and deliver enhanced user experiences through effective marketing campaigns and behavioral tracking.

RudderStack supports Marketo Lead Import as a destination to which you can send large amounts of lead records asynchronously via Marketo’s [bulk API](<https://developers.marketo.com/rest-api/bulk-import/bulk-lead-import/>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/marketo_bulk_upload>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Marketo Lead Import** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Marketo Lead Import, follow these steps:

  * From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Marketo Lead Import**.
  * Assign a name to your destination and then click **Next**.


## Connection settings

To successfully configure Marketo Lead Import as a destination, you will need to configure the following settings:

[![](/docs/images/event-stream-destinations/marketo-lead-import-connection-settings.webp)](</docs/images/event-stream-destinations/marketo-lead-import-connection-settings.webp>)

  * **Munchkin Account ID** : Enter your Munchkin ID, which is a unique identifier for your Marketo instance. To obtain this ID, log into your Marketo instance and navigate to the **Admin** section. In the left menu, go to **Integration** > **Munchkin**. Your Munchkin Account ID will be listed in the **Tracking Code** section on the main screen.


> ![info](/docs/images/info.svg)
> 
> For more information on finding your Munchkin Account ID, refer to the [Marketo knowledge base](<https://nation.marketo.com/t5/knowledgebase/how-to-find-your-munchkin-id-for-a-marketo-instance/ta-p/248432>).

  * **Client ID** : To get your **Client ID** , go to the the **Admin** section of your Marketo instance. In the left menu, go to **Integration** > **LaunchPoint**. Finally, select the API service and click **View Details** to get your client ID.


> ![info](/docs/images/info.svg)
> 
> For more information on finding your Client ID, refer to the [Marketo knowledge base](<https://developers.marketo.com/rest-api/authentication/>).

  * **Client Secret** : You can find your Marketo client secret next to the **Client ID** obtained in the previous step.
  * **De-duplication Field** : Marketo uses this field to de-duplicate user information. Make sure it is also present in the **Column Fields Mapping** setting below.


> ![warning](/docs/images/warning.svg)
> 
> This field should be present in all events sent to Marketo Lead Import for proper de-duplication.

> ![info](/docs/images/info.svg)
> 
> While calling the [Bulk Lead Import API](<https://developers.marketo.com/rest-api/bulk-import/bulk-lead-import/>), RudderStack uses this field for lookup. Marketo then uses it to de-duplicate user information. Generally, `email` should be preferred for de-duplication.

  * **Column Fields Mapping** : This option lets you map your incoming events’ traits to the **Leads** table columns’ API names.


For example, to send the data from the event traits `firstName` and `email` to the Marketo columns with the API names `name` and `Email`, set the mapping as shown:

**RudderStack traits**| **Marketo API name**  
---|---  
`firstName`| `name`  
`email`| `Email`  
  
You can find your columns’ API names by following the [Marketo documentation](<https://developers.marketo.com/rest-api/bulk-import/bulk-custom-object-import/>).

## Identify

> ![info](/docs/images/info.svg)
> 
> RudderStack supports only `identify` event type for this destination.

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you identify a visiting user and associate them to their actions. It also lets you record the traits about them like their name, email address, etc.

A sample `identify` call is as shown:
    
    
    rudderanalytics.identify("name123", {
      name: "Name Surname",
      firstName: "Name",
      lastName: "Surname",
      email: "name@surname.com",
      createdAt: "Thu Mar 24 2020 17:46:45 GMT+0000 (UTC)",
    });
    

The corresponding mapping to the Marketo traits for the above event is as shown:

**Marketo field name**| **Traits**  
---|---  
`name`| `firstName`  
`Email`| `email`  
`birthday`| `birthday`  
`phone`| `phone_number`  
`timestamp`| `createdAt`  
  
RudderStack then sends the following values to Marketo:
    
    
    Name, name@surname.com, , , Thu Mar 24 2020 17:46:45 GMT+0000 (UTC)