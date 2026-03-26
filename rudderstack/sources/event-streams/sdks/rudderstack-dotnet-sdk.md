# .NET SDK

Use RudderStack’s .NET SDK to send server-side events to various destinations.

* * *

  * __7 minute read

  * 


RudderStack’s .NET SDK lets you track your customer event data from your .NET applications and send it to your specified destinations via RudderStack.

Refer to the SDK’s [GitHub codebase](<https://github.com/rudderlabs/rudder-sdk-.net>) for the implementation-specific details.

[![Github Badge](https://img.shields.io/nuget/v/RudderAnalytics?style=flat)](<https://www.nuget.org/packages/RudderAnalytics/>)

## SDK setup requirements

  * Sign up for [RudderStack](<https://app.rudderstack.com/signup>).
  * [Set up a .NET source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#adding-a-source>) in your dashboard. Note the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) for this source.
  * You will also need the [data plane URL](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>) associated with your RudderStack workspace.


## Installing the .NET SDK

You can use [NuGet](<https://docs.microsoft.com/en-us/nuget/consume-packages/install-use-packages-powershell>) to install the .NET SDK into your project.
    
    
    Install-Package RudderAnalytics -Version 2.0.0
    

> ![info](/docs/images/info.svg)
> 
> The SDK uses the [Newton.JSON](<https://www.newtonsoft.com/json>) library for JSON processing.

## Initializing the SDK

To initialize the SDK **asynchronously** (default behavior), run the following code snippet:
    
    
    using RudderStack;
    
    RudderAnalytics.Initialize(
        WRITE_KEY,
        new RudderConfig(dataPlaneUrl: DATA_PLANE_URL)
    );
    

To send events synchronously, initialize the SDK as shown:
    
    
    using RudderStack;
    
    RudderAnalytics.Initialize(
        WRITE_KEY,
        new RudderConfig(dataPlaneUrl: DATA_PLANE_URL, async: false)
    );
    

> ![info](/docs/images/info.svg)
> 
> When initialized in synchronous mode, the .NET SDK sends each event as a single batch. In asynchronous mode, it groups events together and sends them to the backend as a single batch.

## Gzipping requests

> ![success](/docs/images/tick.svg)
> 
> The Gzip feature is enabled by default in the .NET SDK from version `2.0.0`

The .NET SDK automatically gzips requests. However, you can disable this by setting the `gzip` parameter of `RudderConfig` to `false` while initializing the SDK:
    
    
    using RudderStack;
    RudderAnalytics.Initialize(
        WRITE_KEY,
        new RudderConfig(dataPlaneUrl: DATA_PLANE_URL, gzip: false)
    );
    

> ![warning](/docs/images/warning.svg)
> 
> Gzip requires [rudder-server](<https://github.com/rudderlabs/rudder-server>) **v1.4 or higher**. Otherwise, your events might fail.

## Sending events

> ![warning](/docs/images/warning.svg)
> 
> **RudderStack does not store or persist the user state in any of the server-side SDKs**.  
>   
> Unlike the client-side SDKs that deal with only a single user at a given time, the server-side SDKs deal with multiple users simultaneously. Therefore, you must specify either `userId` or `anonymousId` every time while making any API calls supported by the .NET SDK.

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you identify a visiting user and associate them to their actions. It also lets you record the traits about them like their name, email address, etc.

A sample `identify` call made using the .NET SDK is shown below:
    
    
    RudderAnalytics.Client.Identify(
        "1hKOmRA4GRlm",
        new Dictionary<string, object> { {"subscription", "inactive"}, }
    );
    

The `identify` method parameters are as described below:

**Field**| **Type**| **Description**  
---|---|---  
`userId`  
Required, if **anonymousId** is absent.| String| Unique identifier for a user in your database.  
`traits`| Object| An optional dictionary of the user’s traits like `name` or `email`.  
`options`| Object| Object containing `anonymousId`, `integrations`, `timestamp`, and `context`.  
  
See the options parameter section for more information on the `options` object and its fields.

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record the user actions along with their associated properties. Each user action is called an **event**.

A sample `track` call is shown below:
    
    
    RudderAnalytics.Client.Track(
        "1hKOmRA4GRlm",
        "CTA Clicked",
        new Dictionary<string, object> {  {"plan", "premium"}, }
    );
    

The `track` method parameters are as described below:

**Field**| **Type**| **Description**  
---|---|---  
`userId`  
Required, if **anonymousId** is absent.| String| Unique identifier for a user in your database.  
`event`  
Required| String| Name of the event.  
`properties`| Object| An optional dictionary of the properties associated with the event.  
`options`| Object| Object containing `anonymousId`, `integrations`, `timestamp`, and `context`.  
  
See the options parameter section for more information on the `options` object and its fields.

## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record the page views on your application along with the other relevant information about the page.

A sample `page` call is as shown:
    
    
    RudderAnalytics.Client.Page(
        "1hKOmRA4GRlm",
        "Sign Up",
        new Dictionary<string, object> { {"url", "https://wwww.example.com/sign-up"}, }
    );
    

The `page` method parameters are as described below:

**Field**| **Type**| **Description**  
---|---|---  
`userId`  
Required, if **anonymousId** is absent.| String| Unique identifier for a user in your database.  
`name`  
Required| String| Name of the viewed page.  
`category`| String| Category of the viewed page.  
`properties`| Object| An optional dictionary of the properties associated with the viewed page, like `url` or `referrer`.  
`options`| Object| Object containing `anonymousId`, `integrations`, `timestamp`, and `context`.  
  
See the options parameter section for more information on the `options` object and its fields.

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call is the mobile equivalent of the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call. It allows you to record the screen views on your mobile app along with the other relevant information about the app screen.

A sample `screen` call is as shown:
    
    
    RudderAnalytics.Client.Screen(
        "1hKOmRA4GRlm",
        "Dashboard",
        new Dictionary<string, object> { {"name", "Paid Dashboard"}, }
    );
    

The `screen` method parameters are as described below:

**Field**| **Type**| **Description**  
---|---|---  
`userId`  
Required, if **anonymousId** is absent.| String| Unique identifier for a user in your database.  
`name`  
Required| String| Name of the viewed screen.  
`category`| String| Category of the viewed screen.  
`properties`| Object| An optional dictionary of the properties associated with the viewed screen, like `url` or `referrer`.  
`options`| Object| Object containing `anonymousId`, `integrations`, `timestamp`, and `context`.  
  
See the options parameter section for more information on the `options` object and its fields.

## Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call lets you link an identified user with a group, such as a company, organization, or an account. It also lets you record any custom traits or properties associated with that group.

A sample `group` call made using the .NET SDK is shown below:
    
    
    RudderAnalytics.Client.Group(
        "1hKOmRA4GRlm",
        "12",
        new Dictionary<string, object> { {"role", "Owner"}, }
    );
    

The `group` method parameters are as follows:

**Field**| **Type**| **Description**  
---|---|---  
`userId`  
Required, if **anonymousId** is absent.| String| Unique identifier for a user in your database.  
`groupId`  
Required| String| Unique identifier of the group in your database.  
`traits`| Object| An optional dictionary of the group’s traits like `name`or `email`.  
`options`| Object| Object containing `anonymousId`, `integrations`, `timestamp`, and `context`.  
  
See the options parameter section for more information on the `options` object and its fields.

## Alias

The [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) call lets you merge different identities of a known user. It is an advanced method that lets you change the tracked user’s ID explicitly. You can use `alias` for managing the user’s identity in some of the downstream destinations.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack supports sending `alias` events only to select downstream destinations. Refer to the [destination-specific documentation](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) for more details.

A sample `alias` call is as shown:
    
    
    RudderAnalytics.Client.Alias("1hKOmRA4GRlm", "12345");
    

The `alias` method parameters are as mentioned below:

**Field**| **Type**| **Description**  
---|---|---  
`previousId`  
Required| String| The previous unique identifier of the user.  
`userId`  
Required, if **anonymousId** is absent.| String| Unique identifier for a user in your database.  
`options`| Object| Object containing `anonymousId`, `integrations`, `timestamp`, and `context`.  
  
See the options parameter section for more information on the `options` object and its fields.

## Options parameter

The `options` object contains the following fields:

**Field**| **Type**| **Description**  
---|---|---  
`anonymousId`  
Required, if **userId** is absent.| String| Use this field to set an identifier in cases where there is no unique user identifier.  
`integrations`| Object| An optional dictionary containing the destinations to be either enabled or disabled.  
`timestamp`| Timestamp in ISO 8601 format| The timestamp of the event’s arrival.  
`context`| Object| An optional dictionary of information that provides context about the event. It is not directly related to the API call.  
  
## Flushing events

To make sure no events are left in the queue, you can flush the events explicitly by using the SDK’s `flush()` method.
    
    
    RudderAnalytics.Client.Flush();
    

> ![warning](/docs/images/warning.svg)
> 
> You cannot call the `flush()` method again until all messages are flushed from the queue.

## Logging

The .NET SDK supports detailed logging. You can enable this feature as shown:
    
    
    using RudderStack;
    
    Logger.Handlers += LoggingHandler;
    
    static void LoggingHandler(Logger.Level level, string message, IDictionary<string, object> args)
    {
        if (args != null)
        {
            foreach (string key in args.Keys)
            {
                message += String.Format(" {0}: {1},", "" + key, "" + args[key]);
            }
        }
        Console.WriteLine(String.Format("[RudderAnalytics] [{0}] {1}", level, message));
    }
    

> ![info](/docs/images/info.svg)
> 
> The logger must be on a minimum version of .NET Core 2.1.

## FAQ

#### How does the .NET SDK handle events larger than 32KB?

If you are running the .NET SDK asynchronously, RudderStack drops any events greater than 32KB.

For synchronous initialization, the SDK accepts and sends each event greater than 32KB as a single batch and sends them to the RudderStack data plane (backend).

#### Does the .NET SDK support event ordering?

The .NET SDK does not support event ordering by default.