# Google Sheets

Send your event data from RudderStack to Google Sheets.

* * *

  * __4 minute read

  * 


[Google Sheets](<https://www.google.com/sheets/about/>) is a popular spreadsheet program. You can seamlessly create spreadsheets that update and save automatically and are easy to access from your Google Drive.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/googlesheets>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Google Sheets** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
  
## Get started

Once you have confirmed that the source platform supports sending events to Google Sheets, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Google Sheets**.
  2. Assign a name to the destination and click **Continue**.


## Service account permissions

To add Google Sheets as a destination in RudderStack, you must first obtain the Google Cloud service account credentials required for the configuration. Follow these steps:

  1. Go to your [Google Cloud console](<https://console.cloud.google.com/>). Under **Quick access** , click **APIs & Services**.
  2. In the left sidebar, click **Credentials**.
  3. Click **\+ CREATE CREDENTIALS** > **Service account** :

[![Google Sheets create credentials option](/docs/images/event-stream-destinations/google-sheets-create-credentials.webp)](</docs/images/event-stream-destinations/google-sheets-create-credentials.webp>)

  4. Enter the service account details and click **CREATE AND CONTINUE**.
  5. Under **Grant this service account access to project** , select the **Editor** role:

[![Google Sheets editor role](/docs/images/event-stream-destinations/google-sheets-editor-role.webp)](</docs/images/event-stream-destinations/google-sheets-editor-role.webp>)

  6. Click **DONE** to finish the service account configuration. The service account is now created.
  7. Under the **KEYS** tab, click **ADD KEY** > **Create new key**.

[![Google Sheets add key option](/docs/images/event-stream-destinations/google-sheets-add-key.webp)](</docs/images/event-stream-destinations/google-sheets-add-key.webp>)

  8. Choose **JSON** as the key type and click **CREATE**.


The private key JSON will be downloaded and saved to your computer automatically. Use this JSON to set up your Google Sheets destination in RudderStack.

> ![warning](/docs/images/warning.svg)
> 
> Before setting up the destination in RudderStack, make sure you enable the [Google Sheets API](<https://console.cloud.google.com/apis/library/sheets.googleapis.com?q=sheets&id=739c20c5-5641-41e8-a938-e55ddc082ad1&project=rudder-integration&supportedpurview=project>) for your project.

## Connection settings

To successfully configure Google Sheets as a destination, you will need to configure the following settings:

  * **Credentials** : Enter the contents of the credentials JSON obtained in the Service account permissions section above.
  * **Sheet ID** : Enter your Google Sheet ID present in the spreadsheet’s URL. For example, if the URL is `https://docs.google.com/spreadsheets/d/aBC-123_xYz/edit#gid=920137070`, then the sheet ID is `920137070`.
  * **Sheet Name** : Enter the name of the spreadsheet to which you want to send the data. You can find the sheet name in the bottom left corner of the spreadsheet.

[![Google Sheets name](/docs/images/event-stream-destinations/google-sheets-spreadsheet-name.webp)](</docs/images/event-stream-destinations/google-sheets-spreadsheet-name.webp>)

  * **Map Event to Google Sheets** : Use this setting to send an event property to a specific sheet’s column.


> ![warning](/docs/images/warning.svg)
> 
>   * For mapping the traits or event properties, enter the trait/property name directly, for example, `firstName`, `email`, etc. However, it is highly recommended to provide the absolute path to avoid ambiguity when you have the same attribute name in your event’s `traits`, `context.traits`, or `properties` object.
>   * For mapping contextual fields or nested attributes, you must enter the absolute path to the attribute using dot notation. For example, `context.app.build`, `address.zip`, etc.
> 


  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call captures the relevant details about the visiting user.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com"
      age: 25
    })
    

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) method lets you capture user events along with the properties associated with them.

A sample `track` event is shown below:
    
    
    rudderanalytics.track("Product Purchased", {
      revenue: 4.99,
      currency: "USD",
      name: "Shirt",
      voucherCode: "FIRSTSALE",
      order_id: "OR19",
    });
    

## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views with any additional relevant information about the viewed page.

A sample `page` event is shown below:
    
    
    rudderanalytics.page("Cart", "Cart Viewed", {
      path: "/cart",
      referrer: "test.com",
      search: "term",
      title: "test_item",
      url: "http://test.in",
    })
    

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call lets you record whenever your user views their mobile screen, with any additional relevant information about the screen. This call is similar to the `page` call but is exclusive to your mobile device.

A sample `screen` event is shown below:
    
    
    [[RSClient sharedInstance] screen:@"Sample Screen Name" properties:@{@"prop_key" : @"prop_value"}];
    

## FAQ

#### Why aren’t the events sent to my Google Sheet?

To ensure that RudderStack sends your events to Google Sheets, verify if you have done the following:

  * Created a service account with **Editor** permissions for accessing and sending data to your Google Sheet.

  * Enabled the [Google Sheets API](<https://console.cloud.google.com/apis/library/sheets.googleapis.com?q=sheets&id=739c20c5-5641-41e8-a938-e55ddc082ad1&project=rudder-integration&supportedpurview=project>) for your project.

  * Set up the Google Sheets destination in RudderStack correctly:

    * Entered the credentials JSON.
    * Added the correct sheet ID and name.
    * Added the required property-column mappings in the dashboard settings.