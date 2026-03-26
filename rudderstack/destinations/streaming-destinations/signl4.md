# SIGNL4 Destination

Send your event data from RudderStack to SIGNL4.

* * *

  * __5 minute read

  * 


[SIGNL4](<https://www.signl4.com/>) is a tool for instant mobile alerting. It generates real-time alerts to inform teams about incidents and automatically delivers critical information to the right people at the right time.

> ![success](/docs/images/tick.svg)
> 
> RudderStack also supports SIGNL4 as a source. Refer to the [SIGNL4 source](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/signl4/>) documentation for more information.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/signl4>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **SIGNL4** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to SIGNL4, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **SIGNL4**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure SIGNL4 as a destination, you will need to configure the following settings:

  * **API Key** : Enter the team secret of your SIGNL4 team. Refer to the FAQ section for more information on obtaining the team secret.
  * **X-S4-Service** : Enter a category for the alert, for example, `IT`. Refer to the Signl categories section to learn more about these categories.[![SIGNL4 connection setting](/docs/images/event-stream-destinations/signl4-connection-settings-2.webp)](</docs/images/event-stream-destinations/signl4-connection-settings-2.webp>)
  * **X-S4-Location** : Enter the location in the `latitude, longitude` format to display the correct location on the map in your mobile app.[![SIGNL4 connection setting](/docs/images/event-stream-destinations/signl4-connection-settings.webp)](</docs/images/event-stream-destinations/signl4-connection-settings.webp>)
  * **X-S4-Status** : Enter the alert status by choosing from the **new** , **acknowledged** , or **resolved** values.[![SIGNL4 connection setting](/docs/images/event-stream-destinations/signl4-conn-settings-3.webp)](</docs/images/event-stream-destinations/signl4-conn-settings-3.webp>)
  * **X-S4-AlertingScenario** : Use this setting to control how SIGNL4 notifies the team. RudderStack gives you the following options:
    * single_ack: Only one person needs to acknowledge the alert.
    * multi_ack: All on-duty persons need to acknowledge the alert.
    * emergency: All persons, irrespective of their duty status, are notified and need to acknowledge the alert.[![SIGNL4 connection setting](/docs/images/event-stream-destinations/signl4-conn-settings-2.webp)](</docs/images/event-stream-destinations/signl4-conn-settings-2.webp>)
  * **X-S4-ExternalID** : Use this field to pass the unique ID of a record if an event originates from that record in a third-party system.[![SIGNL4 connection setting](/docs/images/event-stream-destinations/signl4-conn-settings-5.webp)](</docs/images/event-stream-destinations/signl4-conn-settings-5.webp>)


The RudderStack dashboard contains the following fields for each of the above-mentioned settings:

  * **Default Value** : Enter or select the required value for the field.
  * **RudderStack property name** : Enter the property name whose actual value will be taken from the event payload and assigned to the field.


Although these fields are optional, RudderStack prioritizes **RudderStack property name** over **Default Value** if both are specified. For example, consider the following use-case:

  * If you provide `new` in the **Default value** field for the **X-S4-Status** setting, the event payload sent to SIGNL4 will contain `X-S4-Status: new`.

  * If you set **RudderStack property name** for the **X-S4-Status** setting to `alert_status`, RudderStack looks for the event property `properties.alert_status`. Suppose the value for `properties.alert_status` is set to `resolved`, then the output payload sent to SIGNL4 will contain `X-S4-Status: resolved`.

  * If you provide values in both the fields, the final output payload sent to SIGNL4 will contain `X-S4-Status: resolved`, as the **RudderStack property name** is given higher priority over **Default Field**.

  * **X-S4-Filtering** : Enable this setting in the RudderStack dashboard and **Filter events/Signls** setting in the SIGNL4 dashboard to send an alert notification only if the input payload contains any keyword for a category. Refer to the Signl categories section to learn more about keywords and category categories.[![SIGNL4 connection setting](/docs/images/event-stream-destinations/signl4-conn-settings-4.webp)](</docs/images/event-stream-destinations/signl4-conn-settings-4.webp>)


> ![info](/docs/images/info.svg)
> 
> Refer to the [SIGNL4 documentation](<https://connect.signl4.com/webhook/docs/index.html>) to learn more about these connection settings.

  * **Event to title mapping** : This setting lets you map the RudderStack event name to a specific alert title. If you do not provide any value, RudderStack sets the alert title as the event name.


## Signl categories

In SIGNL4, you can use the categories to mark and tag Signls based on severity, type, or relating to IT systems, machines, sensors, and services. Refer to the [SIGNL4 documentation](<https://account.signl4.com/manage/Category>) to learn more about the different categories.

You can use the **X-S4-Service** setting in the RudderStack dashboard to specify the Signl category. If not provided, the keywords present in the payload decide the category of the alert. For example, an event payload containing keywords like `ambulance`, `doctor`, `hospital`, `nurse`, `surgery`, etc., is automatically categorized as **Healthcare**.

[![SIGNL4 connection setting](/docs/images/event-stream-destinations/categories-signl4.webp)](</docs/images/event-stream-destinations/categories-signl4.webp>)

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to push alerts for events with a particular alert title, message, or other additional details.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Security Alert", {
      "status": "UP",
      "message": "Aggressive passenger",
      "Source": "Gate agent",
      "Type": "Security"
    });
    

You can pass any key-value pair in the `track` call; RudderStack maps it as is in the SIGNL4 destination.

### Property mapping

The following table lists the mappings between RudderStack and SIGNL4 properties:

RudderStack property| SIGNL4 property| Presence| Description  
---|---|---|---  
`event`| `title`| Required| Title of the alert.  
`property.message`| `message`| Optional| Text message of the alert.  
  
## FAQ

#### Where can I find the SIGNL4 API Key?

The team secret of your SIGNL4 team is the SIGNL4 API key in the RudderStack dashboard. To find the team secret, follow these steps:

  1. Log into your [SIGNL4 dashboard](<https://connect.signl4.com/>).
  2. Select **Teams** to find the **Secret** :

[![SIGNL4 script url](/docs/images/event-stream-destinations/signl-dashboard-2.webp)](</docs/images/event-stream-destinations/signl-dashboard-2.webp>)

#### How can I create a member in the SIGNL4 team?

To create a member in the SIGNL4 team, follow these steps:

  1. Log into your [SIGNL4 dashboard](<https://connect.signl4.com/>).
  2. Select **Users** > **Invite new user**.