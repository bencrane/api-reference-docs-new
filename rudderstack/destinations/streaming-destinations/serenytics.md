# Serenytics

Send your event data from RudderStack to Serenytics.

* * *

  * __4 minute read

  * 


[Serenytics](<https://www.serenytics.com/>) is a full-featured platform for creating dashboards. Generate charts and track KPIs from multiple sources, and easily share results with management and cross-functional teams.

With this integration you can use the full range of RudderStack tools to create functions, transform and filter your events on their way to the Serenytics warehouse where you can then visualize your data.

Find the open source code for this destination in this [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/serenytics>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Serenytics** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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

Once you have confirmed that the source platform supports sending events to Serenytics, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Serenytics**.
  2. Assign a name to your destination and click **Continue**.


## Connection settings

To configure Serenytics as a destination, first retrieve your data storage URL from the Serenytics dashboard under the **Data** tab.

[![](/docs/images/event-stream-destinations/serenytics-data-storage.webp)](</docs/images/event-stream-destinations/serenytics-data-storage.webp>)

Then in the RudderStack dashboard, add the data storage URL to the URL fields in **Connection Settings**.  


[![](/docs/images/event-stream-destinations/serenytics-connection-settings.webp)](</docs/images/event-stream-destinations/serenytics-connection-settings.webp>)

## Supported Calls

All RudderStack events are sent to Serenytics and stored in the Serenytics warehouse. The most common events for each RudderStack method are mapped automatically to the Serenytics naming convention. See the method-specific table below for a reference of the standard mappings.

Properties/fields that are not included in the mapping tables are passed as `trait_{key_name}` in the Serenytics dashboard.

For example, in this example RudderStack event:
    
    
    rudderanalytics.identify(
        "newUser",
        {
          email: "user@gmail.com",
          phone: "+919876543210",
          subscription: "youtube",
          channelName: ["b", "d", "e", "f", "g", "h", "i", "j", "k"],
          obj: {
            first: "Bob",
            last: "Smith",
          },
        }
      );
    

The `userId` and `email` properties are mapped to `user_id` and `email`, and the remaining traits are mapped as `trait_phone`, etc.:
    
    
    {
      user_id: "newUser",
      email: "user@gmail.com",
      trait_phone: "+919876543210",
      trait_subscription: "youtube",
      trait_channelName: ["b", "d", "e", "f", "g", "h", "i", "j", "k"],
      trait_obj: {
        first: "Bob",
        last: "Smith",
      }
    }
    

### Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you uniquely identify a user and record any associated traits about them like their name, email, etc.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4el9Zt1WSfVJIVo4GRlm", {
      likes_movies: true,
      favorite_color: "purple",
      age: 13
    });
    

**Event parameter mapping** :

RudderStack property| Serenytics property  
---|---  
`messageId`| `id`  
`userId`| `user_id`  
`context.ip`  
`request_ip`| `context.ip`  
`request_ip`  
`firstName`| `first_name`  
`lastName`| `last_name`  
`traits.age`  
`context.traits.age`| `age`  
`email`| `email`  
`receivedAt`| `received_at`  
`sentAt`| `sent_at`  
`originalTimestamp`| `original_timestamp`  
`timestamp`| `timestamp`  
  
### Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture user events along with the properties associated with them.

**Event parameter mapping** :

RudderStack property| Serenytics property  
---|---  
`event`  
Required| `event`  
`messageId`| `id`  
`anonymousId`| `anonymous_id`  
`context.ip`  
`request_ip`| `context_ip`  
`receivedAt`| `received_at`  
`sentAt`| `sent_at`  
`originalTimestamp`| `original_timestamp`  
`timestamp`| `timestamp`  
`properties.price`| `price`  
`properties.currency`| `currency`  
`properties.product_id`| `product_id`  
`properties.product_name`| `product_name`  
  
### Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call lets you link an identified user with a group such as a company, organization, or an account, and record any traits associated with that group, for example, company name, number of employees, etc.

A sample `group` call is shown below:
    
    
    rudderanalytics.group(
      {
      userId: "1hKOmRA4el9Zt1WSfVJIVo4GRlm",
      likes_movies: true,
      age: 25,
      }
    );
    

**Event parameter mapping** :

RudderStack property| Serenytics property  
---|---  
`groupId`  
Required| `id`  
`context.ip`  
`request_ip`| `context_ip`  
`receivedAt`| `received_at`  
`sentAt`| `sent_at`  
`originalTimestamp`| `original_timestamp`  
`timestamp`| `timestamp`  
  
### Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views with any additional relevant information about the viewed page.

**Event parameter mapping** :

RudderStack property| Destination property  
---|---  
`messageId`| `id`  
`anonymousId`| `anonymous_id`  
`name`  
`properties.name`| `name`  
`context.ip`  
`request_ip`| `context_ip`  
`receivedAt`| `received_at`  
`sentAt`| `sent_at`  
`originalTimestamp`| `original_timestamp`  
`timestamp`| `timestamp`  
`properties.category`| `category`  
`properties.path`| `path`  
`pageUrl`| `url`  
`properties.title`| `title`  
  
### Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call lets you record whenever your user views their mobile screen with any additional relevant information about the screen.

**Event parameter mapping** :

RudderStack property| Serenytics property  
---|---  
`messageId`| `id`  
`anonymousId`| `anonymous_id`  
`name`  
`properties.name`| `name`  
`context.ip`  
`request_ip`| `context_ip`  
`receivedAt`| `received_at`  
`sentAt`| `sent_at`  
`originalTimestamp`| `original_timestamp`  
`timestamp`| `timestamp`  
`properties.category`| `category`  
`properties.path`| `path`  
`pageUrl`| `url`  
`properties.title`| `title`  
  
### Alias

The [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) call lets you merge different identities of a known user.

**Event parameter mapping** :

RudderStack property| Serenytics property  
---|---  
`userId`  
Required| `user_id`  
`previousId`  
`anonymousId`| `previous_id`  
`context.ip`  
`request_ip`| `context_ip`  
`receivedAt`| `received_at`  
`sentAt`| `sent_at`  
`originalTimestamp`| `original_timestamp`  
`timestamp`| `timestamp`  
  
## FAQ

#### How do I get the data storage URL?

  1. Log in to the [Serenytics dashboard](<https://app.serenytics.com/studio/login>) and click the **Data** tab.
  2. Click the **New data source** button and select the **Serenytics Datawarehouse** tab > **Storage** from the popup.
  3. From your newly-create source, retrieve the `Url` from the **Configuration** tab. Use this URL to populate your connection settings in RudderStack.