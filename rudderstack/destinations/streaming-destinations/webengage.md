# WebEngage

Send your event data from RudderStack to WebEngage.

* * *

  * __6 minute read

  * 


[WebEngage](<https://webengage.com/>) is a full stack marketing automation tool. It lets you drive growth for your businesses by engaging your users via push and in-app notifications, email campaigns, etc. You can also leverage WebEngage’s analytics capabilities to get a 360-degree view of your users and the product.

RudderStack supports WebEngage as a destination to which you can seamlessly send your event data for efficient marketing and analytics.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/webengage>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web, Cloud, Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Unity, AMP , Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **WebEngage** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to WebEngage, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **WebEngage**.
  2. Assign a name to the destination and click **Continue**.


### Connection settings

To successfully configure WebEngage as a destination, you will need to configure the following settings:

[![WebEngage connection settings](/docs/images/event-stream-destinations/webengage-connection-settings.webp)](</docs/images/event-stream-destinations/webengage-connection-settings.webp>)

  * **License Code** : Enter your WebEngage license code.
  * **API Key** : Enter your WebEngage API key.


> ![info](/docs/images/info.svg)
> 
> To get your WebEngage license code and API key, log into your WebEngage dashboard and go to **Data Platform** > **Integrations** > **REST API**. For more information, refer to the FAQ section below.

  * **Data Center** : Select your WebEngage data center from the dropdown.


## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) method lets you identify a user and associate them to their actions. It also lets you record any traits about them like their name, email, etc.

RudderStack uses the `identify` call to create or update the customer information in WebEngage. It maps `userId` or `anonymousId` (`userId` is prioritized if both are present ) to WebEngage’s `userId` before sending the data via the [`users`](<https://docs.webengage.com/docs/rest-api-tracking-users#users>) API.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      email: "alex@example.com",
      phone: "+1-202-555-0146",
    });
    

### Traits mapping

RudderStack maps the following `identify` traits to the corresponding WebEngage attributes:

RudderStack trait| WebEngage attribute| Presence| Notes  
---|---|---|---  
`userId`| `userId`| Required if `anonymousId` is not present.| `userId` cannot exceed 100 characters.  
`anonymousId`| `anonymousId`| Required if `userId` is not present.| `anonymousId` cannot exceed 100 characters.  
`firstName`| `firstName`| Optional| The user’s first name.  
`lastName`| `lastName`| Optional| The user’s last name.  
`birthday`/`dateOfBirth`/`dateofbirth`/`dob`/`DOB`| `birthDate`| Optional| The user’s birth date in the ISO format: `yyyy-MM-dd`.  
`gender`| `gender`| Optional| The user’s gender.  
`email`| `email`| Optional| The user’s email.  
`phone`| `phone`| Optional| The user’s phone.  
`emailOptIn`| `emailOptIn`| Optional| The user’s email subscription preference.  
`smsOptIn`| `smsOptIn`| Optional| The user’s SMS subscription preference.  
`whatsappOptIn`| `whatsappOptIn`| Optional| The user’s WhatsApp subscription preference.  
`company.name`| `company`| Optional| The user’s company.  
`hashedEmail`| `hashedEmail`| Optional| The user’s hashed email for email services.  
`hashedPhone`| `hashedPhone`| Optional| The user’s encrypted phone number for SMS services.  
`postalcode` / `address.postalCode`| `postalCode`| Optional| The user’s postal code.  
`region` / `address.region`| `region`| Optional| The user’s region.  
`locality` / `address.locality`| `locality`| Optional| The user’s locality.  
`city` / `address.city`| `city`| Optional| The user’s city.  
`country` / `address.country`| `country`| Optional| The user’s country.  
`attributes`| `attributes`| Optional| The user’s custom attributes as key-value pairs.  
  
### Identify traits considerations

Note the following when sending `identify` traits to WebEngage:

  * Either `userId` or `anonymousId` must be present in the `identify` call.
  * If both `userId` and `anonymousId` are present in the `identify` call, RudderStack ignores `anonymousId`.
  * WebEngage prioritizes `hashedEmail` over `email`. Hence, once you set `hashedEmail`, it can then be updated only through a new `hashedEmail`.
  * WebEngage prioritizes `hashedPhone` over `phone`. Hence, once you set `hashedPhone`, it can then be updated only through a new `hashedPhone`.


## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) method lets you capture user events along with the properties associated with them.

RudderStack uses the `track` call to send the custom events to WebEngage via the [`events`](<https://docs.webengage.com/docs/rest-api-tracking-events#events>) API.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      timestamp: "2022-05-05T14:58:10.000Z",
      currency: "USD",
      checkout_id: "X23441",
      order_id: "ORD00123"
    });
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure you call `identify` before `track` for RudderStack to include the `userId` in the `track` events. Otherwise, RudderStack will send the `track` calls to WebEngage with an `anonymousId`.

### Property mapping

RudderStack maps the following event properties to the corresponding WebEngage attributes:

RudderStack trait| WebEngage attribute| Presence| Notes  
---|---|---|---  
`userId`| `userId`| Required if `anonymousId` is not present.| `userId` cannot exceed 100 characters.  
`anonymousId`| `anonymousId`| Required if `userId` is not present.| `anonymousId` cannot exceed 100 characters.  
`eventName`| `event`| Required| The event name.  
`timestamp`/`originalTimestamp`| `eventTime`| Optional| The date and time of the event in ISO format: `yyyy-MM-ddTHH:mm:ss±hhmm`.  
`properties`| `eventData`| Optional| The custom event attributes as key-value pairs.  
  
### Setting custom attributes

WebEngage lets you send custom attributes as key-value pairs in the `eventData` parameter as described in the above section. However, there are a few things you should keep in mind:

  * WebEngage ignores any custom attributes starting with `we_` as these are reserved for internal use.
  * User attribute names must be less than 50 characters, while the `string` attribute values cannot exceed 1000 characters. WebEngage automatically truncates any additional characters.
  * You can create a maximum of 25 custom user attributes of each data type.
  * If the attribute value is a JSON object, it can only be used to personalize your campaigns. These attributes cannot be used to create user segments.
  * Once defined, the data type of a custom user attribute cannot be changed again.


## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views with any additional relevant information about the viewed page.

RudderStack internally transforms the `page` call into a `track` call before sending it as a custom event to WebEngage. It sends the event/category name by transforming it in the `Viewed ${category} ${name} page` format.

For example, consider the following `page` call:
    
    
    rudderanalytics.page("Home", "Clothes", {
      path: "/best-seller/1",
      referrer: "https://www.google.com/search?q=estore+bestseller",
      search: "estore bestseller",
      title: "The best sellers offered by EStore",
      url: "https://www.estore.com/best-seller/1"
    });
    

RudderStack transforms the above event into a `track` call named `Viewed Home Clothes page` and sends it to WebEngage as a custom event.

> ![info](/docs/images/info.svg)
> 
> RudderStack sends the `page` event properties to WebEngage, similar to the `track` event properties.

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) method lets you record whenever your user views their mobile screen with any additional relevant information about the screen. It is the mobile equivalent of a  call.

RudderStack internally transforms the `screen` call into a `track` call before sending it as a custom event to WebEngage. It sends the event/category name by transforming it in the `Viewed ${category} ${name} screen` format.

For example, consider the following `screen` call:
    
    
    rudderClient.screen(
        "Games",
        "home",
        RudderProperty().putValue("foo", "bar"),
        null
    )
    

RudderStack transforms the above event into a `track` call named `Viewed Games home screen` and sends it to WebEngage as a custom event.

> ![info](/docs/images/info.svg)
> 
> RudderStack sends the `screen` event properties to WebEngage, similar to the `track` event properties.

## FAQ

#### Where can I find the WebEngage License Code and API key?

To get your WebEngage License Code and API key, follow these steps:

  1. Log into your [WebEngage dashboard](<https://dashboard.webengage.com/>).
  2. Go to **Data Platform** > **Integrations** > **REST API**.
  3. You will find the WebEngage **License Code** and **API Key** listed under **Project Credentials** :

[![WebEngage license code and API key](/docs/images/event-stream-destinations/webengage-license-api-key.webp)](</docs/images/event-stream-destinations/webengage-license-api-key.webp>)