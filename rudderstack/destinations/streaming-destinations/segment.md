# Segment Destination

Send your event data from RudderStack to Segment.

* * *

  * __3 minute read

  * 


[Segment](<http://segment.com/>) is a leading Customer Data Platform (CDP). It lets you track and collect your customer events from a variety of digital touchpoints and send them to the marketing and analytics platforms of your choice.

With RudderStack, you can send your customer events to Segment in real-time.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Segment** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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

To enable sending data to Segment, you will first need to add it as a destination in the RudderStack dashboard. Once the destination is configured and enabled, events from RudderStack will start flowing to Segment.

  * Configure the data source in RudderStack.
  * From the list of destinations, select **Segment**.

[![](/docs/images/2%20%2827%29.webp)](</docs/images/2%20%2827%29.webp>)

  * Then, assign a name to the destination and click **Next**.

[![](/docs/images/3%20%2824%29.webp)](</docs/images/3%20%2824%29.webp>)

  * Select the data source and click **Next**.

[![](/docs/images/4%20%2823%29.webp)](</docs/images/4%20%2823%29.webp>)

  * Enter the Segment write key to configure the destination:

[![](/docs/images/5%20%2822%29.webp)](</docs/images/5%20%2822%29.webp>)

  * To transform your event data before sending it to this destination, click **Create New Transformation**. Otherwise, click **Next**.

[![](/docs/images/6%20%2820%29.webp)](</docs/images/6%20%2820%29.webp>)

  * Your Segment destination is now configured and enabled.

[![](/docs/images/7%20%2815%29.webp)](</docs/images/7%20%2815%29.webp>)

## Identify

The `identify` call lets you associate a visiting user to their actions as well as record their traits.

> ![info](/docs/images/info.svg)
> 
> As a best practice, please make sure that the `identify`call is made at the start of every session or page load for logged-in users, if possible. This will ensure all latest traits are captured.

A sample `identify` call is as shown:
    
    
    rudderanalytics.identify("userid", {
      name: "Name Surname",
      email: "name@website.com",
      phone: "phone",
      birthday: "birthday",
      gender: "M",
      avatar: "link to image",
      title: "Owner",
    })
    

## Track

The `track` call allows you to record the customer events, i.e. the actions that they perform, along with their associated properties.

A sample `track` call is as shown:
    
    
    rudderanalytics.track("Event Name", {
      Plan: "plan value",
    })
    

## Page

The `page` call lets you record your website’s page views, with any additional relevant information about the viewed page.

A sample `page` call is as shown:
    
    
    rudderanalytics.page("Cart", "Cart Viewed", {
      path: "/cart",
      referrer: "test.com",
      search: "term",
      title: "test_item",
      url: "http://test.in",
    })
    

## Group

The `group` call lets you associate a particular identified user with a group, such as a company, organization, or an account. It also lets you record the custom traits associated with that group, such as the name of the group, number of employees, etc.

A sample `group` call is as shown:
    
    
    rudderanalytics.group("sample-group-id", {
      name: "Example Company",
      employees: 1000,
      industry: "Software",
    });
    

## Alias

The alias call allows you to associate one user identity with another. This is quite useful in case of some destinations such as Mixpanel (associating `anonymousId` with an identified user on signup) or Kissmetrics (when the user switches IDs).

A sample `alias` call is as shown:
    
    
    rudderanalytics.alias("to", "from", options, callback)
    

The above `alias` call has the following parameters:

**Parameter**| **Presence**| **Description**  
---|---|---  
**`to`**|  Required| Denotes the new identifier  
**`from`**|  Optional| Denotes the old identifier which will be an alias for the `to` parameter. If not provided, the SDK will populate this as the currently identified `userId`, or `anonymousId` in case of anonymous users.  
**`options`**|  Optional| This dictionary provides additional context to the event payload.  
**`callback`**|  Optional| This function gets executed after successful execution of the **`alias()`** method.  
  
## FAQ

#### How do I get the Segment Write Key?

To get the Segment Write Key, you can create a HTTP source in your Segment dashboard.

Once you create the source, you can copy the **Write Key** for that source and use it in RudderStack for sending the data.