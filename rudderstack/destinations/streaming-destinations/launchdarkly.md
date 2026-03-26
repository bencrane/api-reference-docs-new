# LaunchDarkly

Send your event data from RudderStack to LaunchDarkly.

* * *

  * __3 minute read

  * 


[LaunchDarkly](<https://launchdarkly.com/>) is a popular feature management platform that offers cutting-edge A/B testing and experimentation functionalities. It lets you efficiently automate and manage feature flags and improve overall product workflow and software quality.

RudderStack supports LaunchDarkly as a destination to which you can seamlessly send your data for flag management.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **LaunchDarkly** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the LaunchDarkly native SDK from the`https://unpkg.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the LaunchDarkly SDK successfully.

## Get started

Once you have confirmed that the source platform supports sending events to LaunchDarkly, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **LaunchDarkly**.
  2. Assign a name to the destination and click **Continue**.


### Connection settings

To successfully configure LaunchDarkly as a destination, you will need to configure the following settings:

[![LaunchDarkly connection settings](/docs/images/event-stream-destinations/launchdarkly-connection-settings.webp)](</docs/images/event-stream-destinations/launchdarkly-connection-settings.webp>)

  * **Client-side ID** : Enter the client-side ID of your LaunchDarkly project.


> ![info](/docs/images/info.svg)
> 
> For more information on getting the LaunchDarkly client-side ID, refer to the FAQ section below.

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you create or update a user in LaunchDarkly.

> ![warning](/docs/images/warning.svg)
> 
> You must call `identify` before making any `track` or `alias` calls.

A sample `identify` call is as shown below:
    
    
    rudderanalytics.identify(
      "1hKOmRA4GRlm", {
        anonymous: false,
        avatar: "https://avatarfiles.alphacoders.com/837/83744.jpg",
        country: "USA",
        custom: {
          favourite_color: "black"
        },
        email: "alex@example.com",
        firstName: "Alex",
        ip: "12.23.34.45",
        lastName: "Keener",
        name: "Alex Keener",
        privateAttributeNames: ["avatar", "country"],
        secondary: "abcd21234"
      }
    );
    

### LaunchDarkly key

RudderStack assigns the `userId` to LaunchDarkly’s `key` field to uniquely identify a user.

> ![info](/docs/images/info.svg)
> 
> `key` is the only required field in LaunchDarkly’s `identify` call. If no unique identifier is provided, RudderStack will automatically assign `anonymousId` as `key`.

### Supported traits

The following table lists the supported fields for the `traits` object in the `identify` call:

Field| Type| Presence| Description  
---|---|---|---  
`anonymous`| Boolean| Optional| Must be set to `true`.  
`avatar`| String| Optional| User’s avatar image URL.  
`country`| String| Optional| Country associated with the user.  
`custom`| Object| Optional| Additional attributes associated with the user.  
`email`| String| Optional| User’s email address.  
`firstName`| String| Optional| User’s first name.  
`ip`| String| Optional| User’s IP address.  
`lastName`| String| Optional| User’s last name.  
`name`| String| Optional| User’s full name.  
`privateAttributeNames`| String Array| Optional| List of attribute names (built-in or custom) marked as private and not sent to LaunchDarkly as analytics events.  
`secondary`| String| Optional| User’s secondary identifier.  
  
> ![info](/docs/images/info.svg)
> 
> If you have chosen to bucket the users by a specific attribute, the `secondary` field can be used to further distinguish the users who are otherwise identical as per that attribute.

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record user events and send them to LaunchDarkly as custom conversion metrics for your experiments.

> ![warning](/docs/images/warning.svg)
> 
> As mentioned above, you must call `identify` before sending any `track` events to LaunchDarkly.

A sample `track` call is as shown:
    
    
    rudderanalytics.track("Test Event", {
      foo: "bar"
    });
    

## Alias

The [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) call lets you merge different identities of a known user. You can explicitly change the identity of a user via this call.

A sample `alias` call is shown below:
    
    
    rudderanalytics.alias("newUserId","userId");
    

## FAQ

#### Where do I get the LaunchDarkly Client-side ID?

To get your LaunchDarkly client-side ID, follow these steps:

  1. Log into your [LaunchDarkly dashboard](<https://app.launchdarkly.com/>).
  2. Select your project:

[![LaunchDarkly projects](/docs/images/event-stream-destinations/launchdarkly-projects.webp)](</docs/images/event-stream-destinations/launchdarkly-projects.webp>)

  3. Then, navigate to **Account settings** > **Projects**.
  4. You will see the client-side ID for your project here.

[![LaunchDarkly client-side ID](/docs/images/event-stream-destinations/launchdarkly-clientsideID.webp)](</docs/images/event-stream-destinations/launchdarkly-clientsideID.webp>)