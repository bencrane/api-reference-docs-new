# Google Cloud Functions

Send your event data from RudderStack to Google Cloud Functions.

* * *

  * __3 minute read

  * 


[Google Cloud Functions](<https://cloud.google.com/functions>) is a Functions-as-a-Service (FaaS) product that lets you run your code in the cloud without any servers or containers.

RudderStack supports Google Cloud Functions as a destination where you can send your event data seamlessly.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/google_cloud_function>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** AMP , Android (Java) , Android (Kotlin) , Cordova, Cloud, Flutter, iOS (Obj-C) , iOS (Swift) , React Native , Unity, Warehouse, Web, Shopify
  * Refer to it as **Google Cloud Function** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Google Cloud Functions, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Google Cloud Functions**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully set up Google Cloud Functions as a destination, you need to configure the following settings:

  * **URL** : Enter the Trigger URL obtained in the **Trigger** field during the cloud function setup. For more information on obtaining the URL, see FAQ below.
  * **Required Authentication** : This setting is turned on by default. Turn it off if your cloud function does not require authentication.
  * **Credentials** : Enter your service account credentials here. This is a required field if **Required Authentication** setting is turned on, that is, your cloud function requires authentication. To create service account credentials from scratch, see the [Google documentation](<https://developers.google.com/workspace/guides/create-credentials#service-account>).
  * **Enable Batch Input** : Turn on this setting to pass a batch input (array of events) to your cloud function.
    * **Max Batch Size** : If **Enable Batch Input** setting is turned on, specify the maximum batch size in this field.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Supported events

Google Cloud Functions accepts [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>), [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>), [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>), [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>), and [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) events.

> ![info](/docs/images/info.svg)
> 
> This destination accepts raw event data similar to a webhook. RudderStack sends the entire event payload to Google Cloud Functions without any transformation or modification.

## FAQ

#### How do I create a Google Cloud Function?

  1. Log in to your [Cloud Functions account](<https://cloud.google.com/functions>) and click **VIEW CONSOLE**.
  2. Select your project.
  3. Then, click **CREATE FUNCTION**.
  4. Enter a **Function name** and select the **Region** from the dropdown.


> ![warning](/docs/images/warning.svg)
> 
> Verify that your cloud function name is valid.

  5. In the **Trigger** field, select **HTTP** or **HTTPS** , depending on your use-case.
  6. In the **Runtime, build and connections settings** , specify the memory allocated for the cloud function in the **Memory allocated** field.
  7. Configure the rest of the cloud function settings as per your requirement and click **Next**.

[![Google Cloud Functions setup](/docs/images/event-stream-destinations/gcf-setup-1.webp)](</docs/images/event-stream-destinations/gcf-setup-1.webp>)

  8. Add the function code and the language in the **Runtime** field.
  9. Enter the function name as defined in your code in the **Entry point** field.
  10. Click **Deploy** to save your settings and create the Cloud Function.
  11. In the **TRIGGER** tab, copy the trigger URL - this is required to set up Google Cloud Functions as a destination in RudderStack.

[![Google Cloud Functions trigger URL](/docs/images/event-stream-destinations/gcf-url.webp)](</docs/images/event-stream-destinations/gcf-url.webp>)