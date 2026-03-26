# ActiveCampaign Destination

Send your event data from RudderStack to ActiveCampaign.

* * *

  * __7 minute read

  * 


[ActiveCampaign](<https://www.activecampaign.com/>) is a popular marketing automation and CRM platform. It offers an all-in-one email marketing and growth platform to monitor your users’ product behavior and use the insights to design personalized customer experiences.

RudderStack supports ActiveCampaign as a destination to which you can seamlessly send your event data.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/active_campaign>).

## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **ActiveCampaign**.
  2. Connect your source and click **Continue**.


### Connection settings

Configure the following settings to set up ActiveCampaign as a destination in RudderStack:

  * **API URL:** Enter the ActiveCampaign API URL for your account.
  * **API Key:** Enter the ActiveCampaign API key.


> ![info](/docs/images/info.svg)
> 
> To get the **API URL** and **API key** , log in to your ActiveCampaign account and go to the **Settings** page under the **Developer** tab.

### Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **ActiveCampaign** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> This destination supports hybrid mode for the [JavaScript](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) source. For more information, see Send events in hybrid mode section.

### Send events in hybrid mode

You can use [hybrid mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#hybrid-mode>) to send all events to ActiveCampaign from your [JavaScript](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) source.

> ![info](/docs/images/info.svg)
> 
> In hybrid mode, RudderStack sends the `identify`, `track`, and `screen` events to ActiveCampaign via their REST API and `page` calls via the native ActiveCampaign SDK.

To send events via hybrid mode, use the hybrid mode option(highlighted below) while connecting your source to the ActiveCampaign destination.

[![ActiveCampaign hybrid mode connection setting](/docs/images/event-stream-destinations/activecampaign-hybrid-mode.webp)](</docs/images/event-stream-destinations/activecampaign-hybrid-mode.webp>)

> ![success](/docs/images/tick.svg)
> 
> Use hybrid mode to implement [site tracking](<https://help.activecampaign.com/hc/en-us/articles/221542267-An-overview-of-Site-Tracking>) in ActiveCampaign.
> 
> You can also leverage all the RudderStack cloud mode benefits like [data governance](<https://www.rudderstack.com/docs/data-governance/>) and [tracking plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>).

### Configuration settings

After completing the initial setup, configure the following settings to correctly receive your data in ActiveCampaign:

  * **Event Key:** This value is unique to your ActiveCampaign account. See [ActiveCampaign documentation](<https://help.activecampaign.com/hc/en-us/articles/221870128-An-overview-of-Event-Tracking#how-to-turn-on-event-tracking-0-3>) for more information on obtaining the event key.
  * **ActID:** Enter your ActiveCampaign `actid`. Go to **Settings** > **Tracking** > **Event Tracking API** to get your **actid**.


### Other settings

  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create a new user in ActiveCampaign. If a user already exists, RudderStack updates the user with the latest values.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("userId", {
      email: "john@example.com",
      firstName: "John",
      lastName: "Keener",
      phone: "1234567890"
    });
    

In the above snippet, RudderStack captures relevant user information like their `userId` and the associated traits like `email`, `phone`, `firstName`, and `lastName`, before sending this information to ActiveCampaign.

> ![warning](/docs/images/warning.svg)
> 
> `email` is a mandatory trait for mapping a user to ActiveCampaign.

### Set custom tags

You can associate a user with custom tags by passing the `tags` trait in your `identify` call:
    
    
    rudderanalytics.identify("userId", {
      email: "john@example.com",
      firstName: "John",
      lastName: "Keener",
      phone: "1234567890",
      tags: ["Returning User", "Coupon Used"]
    });
    

> ![info](/docs/images/info.svg)
> 
> `tags` should contain an array of tags you want to associate with the user. If any tag is already present in ActiveCampaign, RudderStack will skip creating that tag.

### Send custom fields

> ![warning](/docs/images/warning.svg)
> 
> To send custom fields to ActiveCampaign, you will need to first create the [custom fields](<https://www.activecampaign.com/learn/guides/what-are-custom-fields>) in ActiveCampaign for each custom value that you want to send.
> 
> When you call `identify` with the keys matching those traits, RudderStack updates the custom fields for that contact.

You can update a contact by passing custom fields in your `identify` calls to ActiveCampaign.

You can use the `fieldInfo` trait to set values for the custom fields, as shown:
    
    
    rudderanalytics.identify("userId", {
      email: "john@example.com",
      firstName: "John",
      lastName: "Keener",
      phone: "1234567890",
      tags: ["Returning User", "Coupon Used"],
      fieldInfo: {
        Interest: "Electronics",
        Country: "USA",
        Hobbies: ["Cricket", "Tennis"]
      }
    });
    

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * The `fieldInfo` trait contains the value of the custom field that you want to store for that contact. For using this feature, you need to create the custom fields from your ActiveCampaign dashboard before passing the values in the event.
>   * To send multi-choice field values for the fields having a checkbox, or list values as an input, you need to send the values as an array. For example: `"Hobbies": ["Cricket","Tennis"]`.
>   * For the date field, the format should be YYYY-MM-DD. Also, the values for the datetime field should be in a ISO datetime format, that is, `yyyy-MM-dd'T'HH:mm:ss. SSSXXX`.
> 


### Subscribe contacts to lists

You can subscribe or unsubscribe a contact from any number of lists by passing a `lists` trait in your `identify` call. This trait should be an array with each element having an `id` and a `status`. The value of `status` must be either `subscribe` or `unsubscribe`.
    
    
    rudderanalytics.identify("userId", {
      email: "john@example.com",
      firstName: "John",
      lastName: "Keener",
      phone: "1234567890",
      tags: ["Returning User", "Coupon Used"],
      fieldInfo: {
        Interest: "Electronics",
        Country: "USA",
        Hobbies: ["Cricket", "Tennis"]
      },
      lists: [
        {
          id: 2,
          status: "subscribe"
        },
        {
          id: 3,
          status: "unsubscribe"
        }
      ]
    });
    

> ![info](/docs/images/info.svg)
> 
> For associating a contact to any list, you need to create the list in ActiveCampaign and use the `id` parameter for mapping that contact.

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record the user actions along with any properties associated with them.

A sample `track` call looks like the following:
    
    
    rudderanalytics.track("Product Purchased", {
      name: "Rubik's Cube"
    });
    

In the above snippet, RudderStack captures the information related to the `Product Purchased` event along with the product’s `name`.

RudderStack also maps `eventData` present within the `track` event properties to ActiveCampaign’s `eventdata` field:
    
    
    rudderanalytics.track("Product Purchased", {
      name: "Rubik's Cube",
      eventData: "Learn while having fun"
    });
    

### Event name considerations

ActiveCampaign sets certain restrictions in the way you can set your `track` event names:

  * The event name must contain only alphanumeric characters. ActiveCampaign rejects any event containing special characters in the name.
  * The event name should not exceed 32 characters. ActiveCampaign automatically truncates event names longer than 32 characters. For example, if you send a `track` event with the name `Product Viewed After Opening The Browser`, ActiveCampaign automatically truncates it to `Product Viewed After Opening The`:

[![ActiveCampaign truncating event names](/docs/images/event-stream-destinations/activecampaign-eventname-truncation.webp)](</docs/images/event-stream-destinations/activecampaign-eventname-truncation.webp>)

## Page

You can use the `page` call to record user’s page views along with the associated properties and send this information to ActiveCampaign. You must call this method at least once per page load.

When you call `page`, RudderStack will send that event to ActiveCampaign as a [site tracking event](<https://help.activecampaign.com/hc/en-us/articles/221542267-An-overview-of-Site-Tracking>) \- this allowlists your domain for tracking purposes.

A sample `page` call looks like the following:
    
    
    rudderanalytics.page("home", {
      path: "path",
      url: "url",
      title: "title",
      search: "search",
      referrer: "referrer"
    });
    

In the above sample, RudderStack captures the information related to the viewed page and the `url` property is used to allowlist the website in ActiveCampaign.

> ![info](/docs/images/info.svg)
> 
> The `page` calls work only if **Site Tracking** is enabled in ActiveCampaign. You can enable this setting by going to the **Tracking** tab in your ActiveCampaign settings page.

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) lets you record whenever your user views their mobile screen with any additional relevant information about the screen.

A sample `screen` call is shown:
    
    
    [[RSClient sharedInstance] screen:@"Sample Screen Viewed" properties:@{@"prop_key" : @"prop_value"}];
    

> ![warning](/docs/images/warning.svg)
> 
> **The`screen` event name must contain only alphanumeric characters.**
> 
> ActiveCampaign rejects events with any special characters in the name.

## FAQ

#### Can I use special characters in my `screen` and `track` event names?

No - your `screen` and `track` event names must contain only alphanumeric characters. ActiveCampaign prescribes that the `screen` and `track` event names must contain only alphabets and numbers and does not allow using any special characters.

#### How does RudderStack send events to ActiveCampaign in hybrid mode?

In hybrid mode, RudderStack sends the user-generated events (`identify`, `track`, `screen`) events to ActiveCampaign via cloud mode and sends the `page` events via device mode (using the native ActiveCampaign web SDK).