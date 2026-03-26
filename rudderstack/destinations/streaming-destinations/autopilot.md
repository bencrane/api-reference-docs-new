# Autopilot Destination (Legacy)

Send your event data from RudderStack to Autopilot.

* * *

  * __4 minute read

  * 


[Autopilot](<https://www.autopilothq.com/>) is a popular marketing automation platform that allows you to track and capture new leads, create detailed customer journeys, and boost customer retention.

> ![warning](/docs/images/warning.svg)
> 
> This documentation is for the legacy Autopilot destination in RudderStack. Autopilot is now rebranded as [Ortto](<https://ortto.com/autopilot/>).
> 
> Refer to this documentation only if you set up the Autopilot destination in RudderStack before the rebranding, or if you are leveraging the [Autopilot REST API](<https://autopilot.docs.apiary.io/#>) to send the data.
> 
> See the [Ortto destination documentation](<https://www.rudderstack.com/docs/destinations/streaming-destinations/ortto/>) for more information on using the new Ortto integration.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/autopilot>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Autopilot** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
  
## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), set up a source.
  2. Go to the **Overview** tab of your source and select **Add Destination** > **Create new destination**.

[![Add new destination in RudderStack dashboard](/docs/images/event-stream-destinations/add-new-destination.webp)](</docs/images/event-stream-destinations/add-new-destination.webp>)

  3. Select **Autopilot** from the list of destinations. Then, click **Continue**.


## Connection settings

Setting| Description  
---|---  
Name| Assign a name to uniquely identify the destination in RudderStack.  
API Key| Enter your Autopilot API key.  
Trigger ID| Enter the Trigger ID from your Autopilot journey. RudderStack uses this ID in `track` calls to add contacts to a journey.  
  
See [Autopilot REST API documentation](<https://autopilot.docs.apiary.io/#reference/api-methods/trigger-journey/add-a-contact-to-a-journey>) for more information.  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs.  
  
See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call captures relevant details about the visiting user and creates or updates a contact in Autopilot.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("user_123", {
      email: "john@example.com",
      firstName: "John",
      lastName: "Doe",
      phone: "+1234567890",
      company: {
        name: "Acme Corp"
      },
      status: "active",
      LeadSource: "website",
      customField: "custom value"
    });
    

### Supported fields

RudderStack maps the following `identify` event traits to the standard Autopilot fields:

RudderStack property| Autopilot field| Description  
---|---|---  
`traits.email`  
`context.traits.email`| `Email`| Contact’s email address  
`traits.firstName`  
`traits.firstname`| `FirstName`| Contact’s first name  
`traits.lastName`  
`traits.lastname`| `LastName`| Contact’s last name  
`traits.phone`| `Phone`| Contact’s phone number  
`traits.company.name`| `Company`| Contact’s company name  
`traits.status`| `Status`| Contact’s status  
`traits.LeadSource`| `LeadSource`| Source of the lead  
  
RudderStack sends additional traits as custom properties to Autopilot.

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to trigger journeys in Autopilot by adding contacts to specific triggers.

To send `track` events to Autopilot successfully, note that:

  * The `track` event must include an email address in either `properties.email` or `traits.email` to identify the contact in Autopilot.
  * You must configure a valid Autopilot trigger ID in your destination settings.


### Sample track event
    
    
    rudderanalytics.track("Purchase Completed", {
      email: "john@example.com",
      productId: "prod_123",
      amount: 99.99,
      currency: "USD"
    });
    

## API endpoints

RudderStack uses the following API endpoints to send events to Autopilot:

Use case| Endpoint  
---|---  
Contact management  
Applicable for Identify events| `https://api2.autopilothq.com/v1/contact`  
Journey triggers  
Applicable for Track events| `https://api2.autopilothq.com/v1/trigger/{triggerId}/contact/{email}`  
  
## Troubleshooting

This section lists some common issues you may encounter while using this integration and their solutions.

#### Track events failing with “Email is required” error

If you receive this error, make sure that your `track` events include an email address. You can provide the email in the following fields:

  * `properties.email`
  * `traits.email`
  * `context.traits.email`


#### Invalid trigger ID error

If you encounter trigger ID errors:

  * Verify that the trigger ID in your destination settings matches the trigger ID in your Autopilot dashboard.
  * Ensure the trigger is active in Autopilot.
  * Check that your API key has permission to access the trigger.


#### Contact not created or updated

If contacts aren’t being created or updated:

  * Verify your API key is valid and has the correct permissions
  * Check that the email field is properly formatted
  * Ensure the contact data doesn’t exceed Autopilot’s field limits


## FAQ

#### Where can I find the Autopilot API key?

  1. Log in to your [Autopilot](<https://login.autopilothq.com/login?redirect=%2Fselect>) dashboard.
  2. Go to **Settings** > **Autopilot API**.
  3. Click **Generate** and copy the API key.


See the [Autopilot documentation](<https://autopilot.docs.apiary.io/#reference/authentication>) for more information.