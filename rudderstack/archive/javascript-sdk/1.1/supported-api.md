# JavaScript SDK API

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk>)

# JavaScript SDK API

Implement the JavaScript SDK API.

* * *

  * __11 minute read

  * 


The JavaScript SDK provides a comprehensive API that lets you track and send your event data to any destination.

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) method lets you identify a user and associate them to their actions. It also lets you record any traits about them like their name, email, etc.

Once you make the `identify` call, the SDK persists the user information and passes it to the subsequent calls.

The JavaScript SDK defines the `identify` method as shown:
    
    
    rudderanalytics.identify(userId, [traits], [apiOptions], [callback]);
    

The following table describes the above (optional) parameters in detail:

Parameter| Type| Description  
---|---|---  
`userId`| String| The unique user identifier in the database. When provided, the SDK sends this argument to the destinations instead of `anonymousId`.  
`traits`| Dictionary| Contains the user’s traits or the properties associated with `userId` such as email, address, etc. [Reference](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/#identify-traits>).  
`apiOptions`| Dictionary| Provides information such as `integrations`, `anonymousId`, and `originalTimestamp`.  
`callback`| Function| Invoked after successfully processing and queueing the event data for delivery. It **does not** indicate the actual event delivery but ensures that the SDK makes a delivery attempt.  
  
#### apiOptions

The structure of the **apiOptions** parameter is as shown:
    
    
    {
      integrations: IntegrationOpts,
      anonymousId: string,
      originalTimestamp: ISO 8601 date string,
      <other keys>: <value> // merged with event's contextual information
    }
    

The following table describes the above parameters in detail:

**Parameter**| **Type**| **Description**  
---|---|---  
`integrations`| [IntegrationOpts](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/load-js-sdk/#integrationopts>)| Use to send event data only to the [selective destinations](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/filtering/#filtering-destinations>).  
`anonymousId`| String| Overrides the current event’s `anonymousId` at the top level.  
`originalTimestamp`| ISO 8601 Date string| Overrides the current event’s `originalTimestamp` at the top level. [Reference.](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/#clock-skew-considerations>)  
`<other keys>: <value>`| -| Merged with the event’s contextual information.  
  
A sample `identify` call is shown below:
    
    
    rudderanalytics.identify(
      "1hKOmRA4el9Zt1WSfVJIVo4GRlm", {
        firstName: "Alex",
        lastName: "Keener",
        email: "alex@example.com",
        phone: "+1-202-555-0146"
      }, {
        page: {
          path: "/best-seller/1",
          referrer: "https://www.google.com/search?q=estore+bestseller",
          search: "estore bestseller",
          title: "The best sellers offered by EStore",
          url: "https://www.estore.com/best-seller/1"
        }
      },
      () => {
        console.log("identify call");
      }
    );
    

In the above example, the JavaScript SDK captures the `userId`, `email` and the [contextual information](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/#contextual-fields>).

> ![warning](/docs/images/warning.svg)
> 
> If you specify the IP address in the event payload, RudderStack uses that instead of automatically capturing it in the backend. You can use this feature to anonymize your users’ IP addresses.

### Anonymous ID

The `anonymousId` is an auto-generated **UUID** (Universally Unique Identifier) that gets assigned to each unique and unidentified visitor to your website.

#### Retrieving anonymous ID

To retrieve the anonymous ID of any visitor, run the following:
    
    
    rudderanalytics.getAnonymousId();
    

> ![info](/docs/images/info.svg)
> 
> If the `anonymousId` is `null` in the SDK and you call the above function, RudderStack will automatically set a new `anonymousId`.

#### How the SDK uses `anonymousId`

The JavaScript SDK generates a unique `anonymousId`, stores it in the `rl_anonymous_id` cookie in the top-level domain, and attaches it to every subsequent event. This helps RudderStack to identify the anonymous users from other sites hosted under a sub-domain.

> ![info](/docs/images/info.svg)
> 
> If you identify a user with your application’s unique identifier like email, database ID, etc., RudderStack stores this ID in the `rl_user_id` cookie and attaches it to every event.

Refer to the [Data Storage](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/data-storage-cookies/>) guide for more information on how the JavaScript SDK stores persistent user data in cookies.

#### Overriding anonymous ID

You can use any of the following three methods to override the `anonymousId` generated by the JavaScript SDK:

  * Provide the `anonymousId` in the **apiOptions** parameter of the `identify` call.


> ![info](/docs/images/info.svg)
> 
> Note that all other events will have the `anonymousId` persisted from the cookie except the particular event where you override the **apiOptions** parameter.

An example is shown below:
    
    
    rudderanalytics.identify(
      "1hKOmRA4el9Zt1WSfVJIVo4GRlm", {
        email: "alex@example.com"
      }, {
        anonymousId: "my-anonymous-id"
      },
      () => {
        console.log("identify call");
      }
    );
    

  * Set the `anonymousId` for all future events using the `setAnonymousId()` method. An example is shown below:


    
    
    rudderanalytics.setAnonymousId("my-anonymous-id");
    // All event payloads will have the anonymousId key set "my-anonymous-id".
    rudderanalytics.identify("1hKOmRA4el9Zt1WSfVJIVo4GRlm", {
      email1: "alex@example.com"
    }, () => {
      console.log("identify call");
    });
    

  * Parse the AMP Linker ID and set the `anonymousId` using AMP Analytics:


    
    
    rudderanalytics.setAnonymousId(
      null,
      "<version>*<checkSum>*<idName1>*<idValue1>*<idName2>*<idValue2>..."
    );
    

Here, the second parameter is the AMP Linker ID format in the [specified structure](<https://github.com/ampproject/amphtml/blob/master/extensions/amp-analytics/linker-id-receiving.md#format>). For websites using the [RudderStack AMP Analytics SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-amp-analytics/#amp-linker>), the `<idName1>` value will be `rs_amp_id`.

Calling the above method will parse the Linker ID and set the `rs_amp_id` key value as the `anonymousId`.

### Setting a blank user ID

To set a blank user ID, you can pass an empty string or `" "` to `userId`.

> ![warning](/docs/images/warning.svg)
> 
> Do not pass an `identify` call with `null` as RudderStack will not allow you to pass a traits object and retain the current `userId`.

#### Use-case

Suppose an anonymous user is identified with a `userId` and then logs out of their account. You can then call `identify("", {isLoggedIn: false})` and the user will continue to be identified by their `anonymousId` for the future events.

### Identifying new users

To identify new users in scenarios like new logins, you can use any one of the following approaches:

  * Call `identify` with a new `userId`  
OR
  * Call `reset` followed by the `identify`


RudderStack resets all cookies related to the user (associated with the `userId` and `traits`) and updates them with the newly provided values.

> ![info](/docs/images/info.svg)
> 
> The `anonymousId` will remain unchanged in this case. It will be the auto-generated value set by the SDK or the one explicitly set using the `setAnonymousId` method.

### Updating user traits

For updating the user traits, you can call `identify` method with the same `userId` multiple times with the new traits. This will append or modify all traits associated with that user. An example is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4el9Zt1WSfVJIVo4GRlm", {
        email1: "alex@example.com"
    }, () => {
        console.log("identify call");
    });
    
    rudderanalytics.identify("1hKOmRA4el9Zt1WSfVJIVo4GRlm", {
        email2: "john@example.com"
    }, () => {
        console.log("identify call");
    });
    

In the above example, both `email1` and `email2` will be sent in the payload for the second `identify` call.

> ![info](/docs/images/info.svg)
> 
> Calling `reset()` method resets the existing user traits and calling `identify()` method with new traits updates the new user traits.

### Setting a custom user ID

You can pass a custom `userId` along with the standard `userId` in your `identify` call. RudderStack adds this value under `context.externalId`.

The following code snippet highlights how you can add an `externalId` to your `identify` request:
    
    
    rudderanalytics.identify(
      "1hKOmRA4GRlm", {
        firstName: "Alex",
        city: "New Orleans",
        country: "Louisiana",
        phone: "+1-202-555-0146",
        email: "alex@example.com",
        custom_flavor: "chocolate",
      } {
        externalId: [{
          id: "some_external_id_1",
          type: "brazeExternalId",
        }, ],
      }
    );
    

## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views with any additional relevant information about the viewed page.

> ![info](/docs/images/info.svg)
> 
> Many destinations require the `page` call to be made at least once every page load.

The JavaScript SDK defines the `page` method as shown:
    
    
    rudderanalytics.page(category, name, [properties], [apiOptions], [callback]);
    

The following table describes the above (optional) parameters in detail:

**Parameter**| **Type**| **Description**  
---|---|---  
`category`| String| Category of the page.  
`name`| String| Name of the page.  
`properties`| Dictionary| Properties of the page auto-captured by the SDK.  
`apiOptions`| Dictionary| Provides information such as `integrations`, `anonymousId`, and `originalTimestamp`. Reference.  
`callback`| Function| Invoked after successfully processing and queueing the event data for delivery. It **does not** indicate the actual event delivery but ensures that the SDK makes a delivery attempt.  
  
A sample `page` call is shown below:
    
    
    rudderanalytics.page(
      "Cart",
      "Cart Viewed", {
        path: "/best-seller/1",
        referrer: "https://www.google.com/search?q=estore+bestseller",
        search: "estore bestseller",
        title: "The best sellers offered by EStore",
        url: "https://www.estore.com/best-seller/1"
      },
      () => {
        console.log("page call");
      }
    );
    

In the above example, the JavaScript SDK captures the page `category`, `name` and the [contextual information](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/#contextual-fields>).

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture user events along with the associated properties.

The JavaScript SDK defines the `track` method as shown:
    
    
    rudderanalytics.track(event, [properties], [apiOptions], [callback]);
    

The following table describes the above parameters in detail:

**Parameter**| **Type**| **Presence**| **Description**  
---|---|---|---  
`event`| String| Required| The name of the tracked event.  
`properties`| Dictionary| Optional| The event-related properties.  
`apiOptions`| Dictionary| Optional| Provides information such as `integrations`, `anonymousId`, and `originalTimestamp`. Reference.  
`callback`| Function| Invoked after successfully processing and queueing the event data for delivery. It **does not** indicate the actual event delivery but ensures that the SDK makes a delivery attempt.|   
  
A sample `track` call is shown below:
    
    
    rudderanalytics.track(
      "Order Completed", {
        revenue: 30,
        currency: "USD",
        user_actual_id: 12345
      },
      () => {
        console.log("track call");
      }
    );
    

In the above example, the `track` method tracks the `Order Completed` event along with other information like `revenue`, `currency`, and the `user_actual_id`.

Refer to the [Ecommerce Events Specification](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) for more information on the ecommerce events captured by RudderStack.

## Alias

The [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) call lets you merge different identities of a known user.

The JavaScript SDK defines the `alias` method as shown:
    
    
    rudderanalytics.alias(to, from, [apiOptions], [callback]);
    

The following table describes the above parameters in detail:

**Parameter**| **Type**| **Presence**| **Description**  
---|---|---|---  
`to`| String| Required| New user identifier.  
`from`| String| Optional| Old user identifier which will be an alias for the `to` parameter. If not provided, the SDK populates this as the currently identified `userId`, or `anonymousId` in case of anonymous users.  
`apiOptions`| Dictionary| Optional| Provides information such as `integrations`, `anonymousId`, and `originalTimestamp`. Reference.  
`callback`| Function| Invoked after successfully processing and queueing the event data for delivery. It **does not** indicate the actual event delivery but ensures that the SDK makes a delivery attempt.|   
  
A sample `alias` call is shown below:
    
    
    rudderanalytics.alias("new_id", "old_id", () => {
      console.log("alias call");
    });
    

## Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call lets you associate an identified user with a group such as a company, organization, or an account.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack does not support associating a user to more than one group per `group` call.

The JavaScript SDK defines the `group` method as shown:
    
    
    rudderanalytics.group(groupId, [traits], [apiOptions], [callback]);
    

The following table describes the above parameters in detail:

**Parameter**| **Type**| **Presence**| **Description**  
---|---|---|---  
`groupId`| String| Required| The unique group identifier in the database. RudderStack calls the relevant destination APIs to associate the identified user to this group.  
`traits`| Dictionary| Optional| The group-related traits. RudderStack passes these traits to the destination to enhance the group properties.  
`apiOptions`| Dictionary| Optional| Provides information such as `integrations`, `anonymousId`, and `originalTimestamp`. Reference.  
`callback`| Function| Invoked after successfully processing and queueing the event data for delivery. It **does not** indicate the actual event delivery but ensures that the SDK makes a delivery attempt.|   
  
A sample `group` call is shown:
    
    
    rudderanalytics.group("sample_group_id", {
      name: "Apple Inc.",
      location: "USA",
    });
    

## Reset

The `reset` method resets the ID and traits of both the user and the group.

In [session tracking](<https://rudderstack.com/docs/sources/event-streams/sdks/session-tracking/#:~:text=tracking%20is%20enabled%3A-,sessionId,-%28Number%29%3A%20The%20session>), calling the `reset` method clears the current `sessionId` and generates a new one.

The JavaScript SDK defines the `reset` method as shown:
    
    
    rudderanalytics.reset();
    

You can also reset the `anonymousId` along with the above-mentioned details by passing `true` to the `reset()` method:
    
    
    rudderanalytics.reset(true);
    

> ![warning](/docs/images/warning.svg)
> 
> The `reset()` method only clears the [cookies and local storage](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/data-storage-cookies/>) set by RudderStack. It does not clear the information stored by the integrated destinations.

## Callbacks to common methods

RudderStack lets you define callbacks to the common methods of the `rudderanalytics` object.

> ![warning](/docs/images/warning.svg)
> 
> This functionality is supported only for the `syncPixel` method which is called by the SDK while making synchronization calls for the relevant destinations.

An example is shown below:
    
    
    rudderanalytics.syncPixelCallback = obj => {
      rudderanalytics.track(
        "sync lotame", {
          destination: obj.destination
        }, {
          integrations: {
            All: false,
            S3: true
          }
        }
      );
    };
    
    <script src="https://cdn.rudderlabs.com/rudder-analytics.min.js"></script>
    

Here, RudderStack defines `syncPixelCallback` on the `rudderanalytics` object while loading the SDK. Further, RudderStack calls this registered callback with the parameter `{destination: <destination_name>}` whenever a SDK makes a sync call the SDK to the relevant integration - in this case, Lotame.

You can also add the callback in the **loadOptions** parameter as shown below:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      clientSuppliedCallbacks: {
        syncPixelCallback: () => {
          console.log("sync done");
        },
      },
    });
    

> ![info](/docs/images/info.svg)
> 
> Replace the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) in the snippet with their actual values.

## Query string API

RudderStack’s Query string API lets you trigger the `track` and `identify` calls using the query parameters within the URL. The query parameters are listed in the following table:

Parameter| Action  
---|---  
`ajs_uid`| Triggers a `rudderanalytics.identify()` call with `userId` having the parameter value.  
`ajs_aid`| Triggers a `rudderanalytics.setAnonymousId()` call with `anonymousId` having the parameter value.  
`ajs_event`| Triggers a `rudderanalytics.track()` call with `event` name as the parameter value.  
`ajs_prop_<property>`| If `ajs_event` is passed as a query string, the value of this parameter populates the `properties` of the corresponding event in the `track` call.  
`ajs_trait_<trait>`| If `ajs_uid` is provided as a query string, the value of this parameter populates the `traits` of the `identify` call.  
  
For example, consider the following URL containing the query string parameters:

`http://hostname.com/?ajs_uid=12345&ajs_event=test%20event&ajs_aid=abcde&ajs_prop_testProp=prop1&ajs_trait_name=Firstname+Lastname`

It will trigger the following API calls:
    
    
    // Sets the user ID/anonymous ID
    rudderanalytics.setAnonymousId("abcde");
    
    // Identify call
    rudderanalytics.identify("12345", {
      name: "Firstname Lastname"
    });
    
    // Track call
    rudderanalytics.track("test event", {
      testProp: "prop1"
    });
    

## Context and traits

The JavaScript SDK automatically captures certain event-specific and user-specific data based on the event type.

The `context` and `traits` dictionaries are provided in the [apiOptions](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/supported-api/#apioptions>) parameter of the supported API methods.

### Context

The `context` object is a dictionary of additional information about a particular event data, such as a user’s locale.

> ![info](/docs/images/info.svg)
> 
> A context is a complete and specific piece of information. Any other information provided outside this specification is ignored.

### Traits

The `traits` object is an optional dictionary included within `context` specifying the user’s unique traits. This is a very useful field for linking the user’s information from a previously made `identify` call to the subsequent calls, for example, `track` or `page`.

#### Use-case

To understand the concept of context and traits better, refer to the following `identify` event:
    
    
    rudderanalytics.identify("1hKOmRA4el9Zt1WSfVJIVo4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
      subscriptionStatus: "subscribed",
      plan: "Silver"
    });
    

The traits in the above event are `name`, `email`, `subscriptionStatus`, and `plan`. If you wish to add or override any traits in the subsequent `track` or `page` event triggered by the user, you can do so by passing it in `traits` as shown:
    
    
    rudderanalytics.track(
      "Subscription Update", {
        campaign: "Subscribe"
      }, {
        traits: {
          plan: "Gold",
          addOn: true
        }
      }
    );
    

The above snippet will add a new trait `addOn` and update the user trait `plan` to `Gold`.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/javascript-sdk/1.1/load-js-sdk/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/javascript-sdk/1.1/data-storage-cookies/>)