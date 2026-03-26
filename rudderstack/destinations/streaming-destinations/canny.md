# Canny Destination

Send your event data from RudderStack to Canny.

* * *

  * __4 minute read

  * 


[Canny](<https://canny.io/>) is a customer feedback management tool which captures, organizes, and analyzes product feedback in one place to help you make informed product decisions.

RudderStack supports Canny as a destination to which you can seamlessly send your event data.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Canny** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
  
## Get started

Once you have confirmed that the source platform supports sending events to Canny, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Canny**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure Canny as a destination, you will need to configure the following settings:

[![Canny connection settings](/docs/images/event-stream-destinations/canny-connection-settings.webp)](</docs/images/event-stream-destinations/canny-connection-settings.webp>)

  * **API Key** : Enter your API key from the Canny dashboard.


> ![info](/docs/images/info.svg)
> 
> Refer to the FAQ section below for more information on getting the API Key.

### Event settings

  * **Mapping to trigger Canny Events for the respective Event** : Enter the event name and choose the Canny event from the dropdown to be triggered when that event is called.


> ![success](/docs/images/tick.svg)
> 
> You can specify multiple **Canny Events** for one **Event Name** and vice versa.

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to [create or update a user](<https://developers.canny.io/api-reference#create_or_update_user>) in Canny.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4el9Zt1WSfVJIVo4GRlm", {
        "name": "Alex Keener",
        "email": "alex@example.com",
        "gender": "Male",
        "profession": "singer-songwriter",
        "companies": [{
            "created": "2020-01-23T04:56:07.890Z",
            "customFields": {
                "field1": "value1",
            },
            "id": "company123",
            "monthlySpend": 500.00,
            "name": "company name"
        }]
    });
    

### Property mappings

The following table lists the mappings between RudderStack and Canny properties:

RudderStack property| Canny property| Presence| Data type  
---|---|---|---  
`userId`/`traits.userId`/`traits.id`/`context.traits.userId`/`context.traits.id`| `userId`| Required| String  
`context.traits.name`/`traits.name`| `name`| Required| String  
`context.traits.email`/`traits.email`/`properties.email`| `email`| Optional| String  
`context.traits`/`traits` (after removing `email` and `name`)| `customFields`| Optional| Object  
`originalTimestamp`/`timestamp`| `created`| Optional| ISO 8601 Timestamp  
`context.traits.avatarURL`/`traits.avatarURL`| `avatarURL`| Optional| String  
`context.traits.companies`/`traits.companies`| `companies`| Optional| Array of object (in company objects `id` and `name` are the only required fields)  
  
## Track

You can create the following events using the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call:

  * [Create post](<https://developers.canny.io/api-reference#create_post>)
  * [Create vote](<https://developers.canny.io/api-reference#create_vote>)


RudderStack [retrieves the user](<https://developers.canny.io/api-reference#retrieve_user>) data using `userId` or `email` and uses that information to create post or vote.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Submit", {
        boardId: "62de88676bc28b44eeef25dd",
        details: "Require new feature",
        title: "New Feature",
        eta: "10.08.2022",
        priority: "High"
    })
    

### Property mappings for Create post event

The following table lists the mappings between RudderStack and Canny properties for the **Create post** event:

RudderStack property| Canny property| Presence| Data type| Notes  
---|---|---|---|---  
`properties.boardID`/`properties.boardId`/`properties.board.id`| `boardID`| Required| String| -  
Collect from `externalId` or [retrieve user](<https://developers.canny.io/api-reference#retrieve_user>) API call| `authorID`| Required| String| -  
`properties.details`| `details`| Required| String| -  
`properties.title`| `title`| Required| String| -  
`properties.byID`/`properties.byId`/`properties.by.id`| `byID`| Optional| String| -  
`properties.categoryID`/`properties.categoryId`/`properties.category.id`| `categoryID`| Optional| String| -  
`properties.customFields`| `customFields`| Optional| Object| Ensure that you create the custom fields in Canny dashboard to send the event successfully.  
`properties.eta`| `eta`| Required if `etaPublic` is present.| String| Should be in the MM/YYYY format.  
`properties.etaPublic`| `etaPublic`| Required if `eta` is present.| Boolean| -  
`properties.imageURLs`| `imageURLs`| Optional| Array of strings| -  
  
### Property mappings for Create vote event

The following table lists the mappings between RudderStack and Canny properties for the **Create vote** event:

RudderStack property| Canny property| Presence| Data type  
---|---|---|---  
`properties.postId`/`properties.postID`/`properties.post.id`| `postID`| Required| String  
Collect from `externalId` or [retrieve user](<https://developers.canny.io/api-reference#retrieve_user>) API call| `voterID`| Required| String  
  
> ![info](/docs/images/info.svg)
> 
> The key name for `externalId` is `cannyUserId`.

## FAQ

#### Where can I find the Canny API Key?

To find the Canny API Key:

  1. Log into your [Canny account](<https://canny.io/login>).
  2. Go to **Settings** > **API & Webhooks** under your profile:

[![Canny dashboard](/docs/images/event-stream-destinations/canny-api-key.webp)](</docs/images/event-stream-destinations/canny-api-key.webp>)

#### How to create custom fields in the Canny dashboard?

To create custom fields in Canny Dashboard:

  1. Log into your [Canny account](<https://canny.io/login>).
  2. Under your profile, navigate to **Settings** > **Post Fields** > **Create New Field**.
  3. Enter the field name and click **Create**.
  4. Navigate to **Boards** and select the desired **Board** from the dropdown.
  5. Select **Create Post Form** > **Add Fields** in the **Fields** section.
  6. Select the relevant **Post Field** from the dropdown.
  7. Enter details and click **Save**.

[![Canny dashboard](/docs/images/event-stream-destinations/canny-new-field.webp)](</docs/images/event-stream-destinations/canny-new-field.webp>)