# HubSpot Cloud Mode Integration (Legacy API) Deprecated

Send events to HubSpot via cloud mode using the legacy API.

* * *

  * __3 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> HubSpot has deprecated the legacy API (v1). Use the [New API (v3)](<https://www.rudderstack.com/docs/destinations/streaming-destinations/hubspot/cloud-mode/new-api/>) instead.

RudderStack supports the following API calls while sending data to Hubspot via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) using the [legacy API](<https://legacydocs.hubspot.com/docs/overview?_ga=2.34803302.670362313.1663315856-97001172.1658910392>).

> ![warning](/docs/images/warning.svg)
> 
> RudderStack does not support the [new datetime data type](<https://www.youtube.com/watch?v=2YjCUQUt8iY&ab_channel=HubSpot>) introduced by HubSpot.

## Identify

RudderStack sends the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create or update a contact in HubSpot. The contact’s email ID must be present in the `traits` object of the `identify` call.

A sample `identify` call is as shown:
    
    
    rudderanalytics.identify({
      firstName: "Alex",
      city: "New Orleans",
      country: "USA",
      phone: "+1-202-555-0146",
      email: "alex@example.com",
      custom_flavor: "chocolate",
      custom_date: 1574769933368,
      custom_date1: new Date("2019-10-14T11:15:53.296Z"),
    })
    

### Special fields

HubSpot supports the following traits as special fields:

  * `address`
  * `city`
  * `companyName`
  * `email`
  * `firstName`
  * `lastName`
  * `position`
  * `phone`
  * `zip`


### Custom properties

RudderStack supports sending custom properties to HubSpot via the `identify` call. These properties will update the `contact` property you have **already created** in HubSpot:

[![HubSpot create property](/docs/images/event-stream-destinations/hubspot-create-property.webp)](</docs/images/event-stream-destinations/hubspot-create-property.webp>)

> ![info](/docs/images/info.svg)
> 
> Refer to the [HubSpot Knowledge Base](<https://knowledge.hubspot.com/crm-setup/manage-your-properties>) for more information on creating custom properties.

When you provide any custom property in the event, RudderStack automatically converts the field name into the lower case and replaces any space with an underscore. This is because HubSpot does not accept properties in the upper case and spaces.

RudderStack then maps the field values present in the `traits` to the corresponding HubSpot custom property.

> ![warning](/docs/images/warning.svg)
> 
> HubSpot discards any property that does not exist and returns a **400 Bad Request** error.

### Dates

For sending properties of `date` type, you can send them as the [epoch time](<https://en.wikipedia.org/wiki/Unix_time>) or as a `date` object. RudderStack converts them to the required HubSpot format (midnight UTC).

## Track

A [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record various user actions and any properties associated with them.

To associate a `track` call with a user, you need to specify the user’s `email` under `context.traits` . Additionally, RudderStack associates the `track` events with the same user after an `identify` request is successfully made.

A sample `track` event is as shown:
    
    
    rudderanalytics.track(
      "Order Completed", {
        value: 30,
      }, {
        context: {
          traits: {
            firstname: "Alex",
            city: "New Orleans",
            country: "USA",
            phone: "+1-202-555-0146",
            email: "alex@example.com",
          },
        },
      }
    )
    

The `track` call also supports [`externalId`](<https://legacydocs.hubspot.com/docs/methods/enterprise_events/http_api#:~:text=%26favorite_color%3Dorange-,External%20id,-%26id%3D%7Bvalue%7D>) as a parameter which is mapped from `externalID` `hubspotId`. A sample `track` call containing the `externalId` is as shown:
    
    
    rudderanalytics.track(
      "Order Completed", {
      value: 30,
    }, {
      context: {
        traits: {
          firstname: "Alex",
          city: "New Orleans",
          country: "USA",
          phone: "+1-202-555-0146",
          email: "alex@example.com",
        },
      },
      externalId: [{
        type: "hubspotId",
        id: "6556"
      }]
    })
    

### Revenue events

For the revenue events, a `value` or `revenue` key should be included in the event properties to be recorded in HubSpot.

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call lets you record whenever your user views their mobile screen, with any additional information about the viewed screen.

If you have enabled screen views in your [Android (Java)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>) or [iOS (Obj-C)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>) app implementation, RudderStack will send this information to HubSpot. RudderStack also forwards the `properties` you’ve passed along with the `screen` call without any changes.

A sample `screen` call sent via the iOS (Obj-C) SDK is shown below:
    
    
    [[RSClient sharedInstance] screen:@"Main"
                properties:@{@"prop_key" : @"prop_value"}];