# User.com

Send your event data from RudderStack to User.com.

* * *

  * __5 minute read

  * 


[User.com](<https://user.com/en/>) is a popular marketing automation platform. It provides robust tools for the marketing, sales, management, and support teams to boost their brand value, enhance customer engagement, and increase conversions.

Find the open source code for this destination in this [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/user>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **user.com** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to User.com, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **User.com**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully set up User.com as a destination, you will need to configure the following settings:

  * **Public REST API Key** : Enter your public User.com REST API key.
  * **App Subdomain** : Enter the subdomain of your User.com app.


> ![info](/docs/images/info.svg)
> 
> For more information on obtaining the public REST API key and app subdomain, see the FAQ section below.

  * **Map Rudder user attributes to User.com attributes** : With this setting, you can map the RudderStack user attributes to specific User.com user attributes.
  * **Map RudderStack event name to User.com event name** : Use this setting to map the RudderStack event names to specific User.com events. You can map one or more RudderStack events to a single User.com event but **not** vice-versa.
  * **Map your event property** : Enter the RudderStack and User.com event properties you want to map for the above-mentioned event names. You can map a RudderStack property only to one User.com property and vice-versa.
  * **Map Rudder company attributes to User.com company attributes** : Use this setting to map the RudderStack company attributes to specific User.com company attributes.


## User lookup

> ![info](/docs/images/info.svg)
> 
> This functionality is applicable only for the `identify`, `track`, and `page` calls.

RudderStack looks up a user in User.com using the `userKey`, `email`, or `phone` properties.

  * You can pass the `userKey` in the `externalId` array:


    
    
    "externalId": [{
      "type": "userKey",
      "id": "uehfuuiuednjk"
    }],
    

  * You can pass the `email` or `phone` in the `integrations` object:


    
    
    integrations: {
    user: {
      lookup: "email/phone"
    }
    });
    

> ![warning](/docs/images/warning.svg)
> 
> You must pass only one of `email` or `phone` in `lookup`. Also, `email` or `phone` (whichever is passed) must have unique values in User.com.

The precedence order for looking up a user based on the above properties is:

  * The `userKey` is given the highest priority.
  * The `lookup` value is given the second highest priority. If `phone`/`email` (whichever is passed) is not found, RudderStack will throw an error.
  * If none of the above is present, RudderStack falls back to the `userId`. If not found, RudderStack will throw an error.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create a new user in User.com. If the user already exists, RudderStack updates the user details.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify('1hKOmRA4el9Zt1WSfVJIVo4GRlm', {
          firstName: 'Alex',
          lastName: 'Keener',
          email: "alex@example.com"
        }, {
          externalId: [{
            type: "userKey",
            id: "Df344sdFgdDsS4"
          }],
          integrations: {
            User.com: {
              lookup: "email"
            }
          }
        );
    

#### Traits mapping

The following table lists the mappings between RudderStack and User.com properties for `identify` call:

RudderStack property| User.com property  
---|---  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  
`anonymousId`  
Required| `custom_id`  
`traits.firstName`  
`traits.firstname`  
`traits.first_name`  
`context.traits.firstName`  
`context.traits.firstname`  
`context.traits.first_name`| `first_name`  
`traits.lastName`  
`traits.lastname`  
`traits.last_name`  
`context.traits.lastName`  
`context.traits.lastname`  
`context.traits.last_name`| `last_name`  
`traits.email`  
`context.traits.email`  
`properties.email`  
`context.externalId.0.id`| `email`  
`traits.phone`  
`context.traits.phone`  
`properties.phone`| `phone_number`  
`traits.tags`  
`context.traits.tags`| `tags`  
`traits.address.city`  
`context.traits.address.city`| `city`  
`traits.region`  
`context.traits.region`| `region`  
`traits.country`  
`context.traits.country`| `country`  
`traits.gender`  
`context.traits.gender`| `gender`  
`traits.status`  
`context.traits.status`| `status`  
`traits.googleUrl`  
`context.traits.googleUrl`| `google_url`  
`traits.linkedinUrl`  
`context.traits.linkedinUrl`| `linkedin_url`  
`traits.twitterUrl`  
`context.traits.twitterUrl`| `twitter_url`  
`traits.facebookUrl`  
`context.traits.facebookUrl`| `facebook_url`  
`traits.avatar`  
`context.traits.avatar`  
`traits.avatarURL`  
`context.traits.avatarURL`  
`traits.avatar_URL`  
`context.traits.avatar_URL`| `gravatar_url`  
`traits.timezone`  
`context.traits.timezone`| `timezone`  
  
## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to record a new event which, in turn, can be used to filter and bucket users in User.com.

A sample `track` call is shown below:
    
    
    rudderanalytics.track('Add to cart', {
      purchased_item: "T-Shirt",
      brand: "Zara",
      email: "alex@example.com"
    }, {
      integrations: {
        User.com: {
          lookup: "email"
        }
      }
    ););
    

#### Property mapping

The following table lists the mappings between RudderStack and User.com properties for the `track` call:

RudderStack property| User.com property  
---|---  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  
Required| `user_id`  
`event`  
Required| `name`  
`properties`| `data`  
`originalTimestamp`  
`timestamp`| `timestamp`  
  
## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views with any additional relevant information about the viewed page.

A sample `page` call is shown below:
    
    
    rudderanalytics.page("section-name", {
          path: "path",
          url: "url",
          title: "title",
          search: "search",
          referrer: "referrer",
          phone: "1-202-555-0146",
        }, {
          integrations: {
            User.com: {
              lookup: "phone"
            }
          });
    

#### Property mapping

The following table lists the mappings between RudderStack and User.com properties for `page` call:

RudderStack property| User.com property  
---|---  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  
Required| `client_user`  
`traits.url`  
`context.traits.url`  
Required| `page_domain`  
`traits.path`  
`context.traits.path`  
Required| `page_path`  
`originalTimestamp`  
`timestamp`  
Required| `timestamp`  
  
## Group

You can use the [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call to create or update a company profile and associate a user with it.

A sample `group` call is shown below:
    
    
    rudderanalytics.group(
      "group01", {
        name: "Alex Keener",
        phone: "1-202-555-0146",
        size: 51,
        zipcode: 90009,
        street: "6649 N Blue Gum Street",
        city: "New Orleans",
        region: "Louisiana",
        country: "USA"
      },
    );
    

#### Property mapping

The following table lists the mappings between RudderStack and User.com properties for the `group` call:

RudderStack property| User.com property  
---|---  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  
`anonymousId`  
Required| `custom_id`(user)  
`groupId`  
`traits.groupId`| `custom_id`(company)  
`traits.name`| `name`(company name)  
`traits.email`  
`context.traits.email`  
`properties.email`  
`context.externalId.0.id`| `email`  
`traits.address`  
`context.traits.address`| `address`  
`traits.address.city`  
`context.traits.address.city`| `city`  
`traits.region`  
`context.traits.region`| `region`  
`traits.country`  
`context.traits.country`| `country`  
`traits.description`| `description`  
`traits.phone`  
`context.traits.phone`  
`properties.phone`| `phone_numbers`  
`traits.zip`  
`traits.zipcode`  
`traits.address.zipcode`  
`traits.address.postalcode`  
`context.traits.zip`  
`context.traits.zipcode`  
`context.traits.address.zipcode`  
`context.traits.address.postalcode`| `postal_code`  
`traits.size`| `size`  
`traits.tags`| `tags`  
  
## FAQ

#### Where can I find the User.com public REST API key?

To get your public REST API key, follow these steps:

  1. Log into your [User.com dashboard](<https://app.user.com/accounts/login/>) and go to your app.
  2. Click **Settings** > **App settings** > **Advanced** > **Public REST API keys**.
  3. Click **Create API key** :

[![User.com connection settings](/docs/images/event-stream-destinations/user-com-dashboard.webp)](</docs/images/event-stream-destinations/user-com-dashboard.webp>)

#### Where can I find the User.com app subdomain?

To get your app subdomain, follow these steps:

  1. Log into your [User.com dashboard](<https://app.user.com/accounts/login/>) and go to your app.
  2. Click **Settings** > **Setup & Integrations** to see the app domain. The subdomain is the part of the complete domain excluding `.user.com`:

[![User.com connection settings](/docs/images/event-stream-destinations/user-com-dashboard-2.webp)](</docs/images/event-stream-destinations/user-com-dashboard-2.webp>)