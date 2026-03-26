# Customer.io Cloud Mode Integration

Send events to Customer.io in RudderStack cloud mode.

* * *

  * __5 minute read

  * 


After you have successfully instrumented Customer.io as a destination in RudderStack, follow this guide to correctly send your events to Customer.io in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/customerio>).

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) event lets you identify a visiting user and associate them to their actions. It also lets you record the traits about them like their name, email address, etc.

> ![info](/docs/images/info.svg)
> 
> `userId` is a mandatory field for sending `identify` events to Customer.io. If it is absent, RudderStack uses the `email` field instead. If `email` is absent too, RudderStack drops the event.

RudderStack sends the `createdAt` field (mapped to Customer.io’s `created_at` property) to register the user signup time. If it is absent in the event, RudderStack automatically assigns the event’s timestamp to `created_at` before sending it to Customer.io.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("userId", {
      name: "Tintin",
      city: "Brussels",
      country: "Belgium",
      email: "tintin@herge.com"
    });
    

Note that:

  * You **cannot** use the same `email` to make consecutive `identify` calls with different `userId` fields.
  * To update user information, you can use the Customer.io canonical identifier [`cio_id`](<https://customer.io/docs/journeys/identifying-people/#cio_id>), as shown:


    
    
    rudderanalytics.identify('<cio_id>', {
      email: '<updated_email>@example.com',
      id: '<updated_id>'
    });
    

### Unsubscribe users

You can pass `unsubscribed: true` in the `identify` call to unsubscribe a user in Customer.io:
    
    
    rudderanalytics.identify("27340af5c8819", {
      email: "alex@example.com",
      unsubscribed: true
    });
    

Make sure the user ID and the email values match the Customer.io attributes. You can verify this by selecting that user in the [People](<https://customer.io/docs/getting-started-people/>) page in your Customer.io dashboard and clicking **Attributes**.

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) event lets you record the user actions along with their associated properties and send them to Customer.io.

> ![info](/docs/images/info.svg)
> 
> `userId` is a mandatory field for sending `track` events to Customer.io. If it is absent, RudderStack uses the `anonymousId` field instead.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Track me", {
      category: "category",
      label: "label",
      value: "value",
    });
    

> ![warning](/docs/images/warning.svg)
> 
> For anonymous users, Customer.io does not permit an event name of size more than 100 Bytes. RudderStack automatically trims the event name in such a scenario.
> 
> See the [Customer.io documentation](<https://www.customer.io/docs/api/track/#section/Track-API-Event-limits>) for more information on the Track API event limits.

## Page

You can use the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) event to record the page views along with the other page-related information.

A sample `page` call is as shown below:
    
    
    // "Home" is the page name.
    rudderanalytics.page("Home", {
      path: "path",
      url: "url",
      title: "title",
      search: "search",
      referrer: "referrer",
    });
    

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) event is the mobile equivalent of the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) event and lets you record the screen views on your mobile app along with other relevant information about the viewed screen.

If you have enabled screen views in your app implementation in the [iOS (Obj-C)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>) or [Android (Java)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>) SDK, RudderStack registers the screen views as `Viewed <screen_name> Screen` in the user’s **Activities** tab.

RudderStack also forwards the event properties to Customer.io as received.

A sample `screen` call using RudderStack’s iOS (Obj-C) SDK is shown below:
    
    
    [[RudderClient sharedInstance] screen:@"Main"
                properties:@{@"prop_key" : @"prop_value"}];
    

RudderStack transforms the above event as `Viewed Main Screen` before sending it to Customer.io.

## Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) event lets you link an identified user with a group like a company, organization, or an account. It also lets you record any custom traits or properties associated with that group and send this information to Customer.io.

A sample `group` call is shown below:
    
    
    rudderanalytics.group("group@49", {
      email: "help@rudderstack.com",
      action: "identify"
    })
    

RudderStack automatically maps the following properties to the corresponding Customer.io properties:

RudderStack property| Customer.io property  
---|---  
`groupId`  
Required| `identifiers_object_id`  
`traits.action`  
`properties.action`  
  
Required - if not present, RudderStack sets it to `identify` by default.| `action`  
  
**Note** : Customer.io accepts only the following values:  
  


  * `identify`
  * `delete`
  * `delete_relationships`
  * `add_relationships`

  
`traits`| `attributes`  
`userId`| `identifiers.id`  
`context.traits.email`  
`properties.email`  
`context.externalId.0.id`| `identifiers.email`  
`traits.objectTypeId`  
  
If not specified, RudderStack sets it to `1` by default.| `identifiers.object_type_id`  
  
## Alias

The [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) event lets you merge different identities of a known user. It is an advanced method that lets you change the tracked user’s ID explicitly.

> ![info](/docs/images/info.svg)
> 
> The `alias` call is applicable only when both the user identities are present in Customer.io.
> 
> The mapping can be any one of the following:
> 
>   * ID to ID
>   * email to email
>   * email to ID
>   * ID to email
> 


A sample `alias` call is as shown below:
    
    
    rudderanalytics.alias("userId", "previousId");
    

You can also merge two accounts via the user’s email address . RudderStack sets the primary email as `userId` and secondary email as `previousId`.

A sample `alias` call merging two accounts using the email address is shown:
    
    
    rudderanalytics.alias("<primary.email>", "<secondary.email>");
    

## Device token registration

RudderStack registers the device token to Customer.io for the below [Application Lifecycle Events](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/>):

  * `Application Installed`
  * `Application Opened`


Enable the `trackApplicationLifecycleEvents` feature in your mobile SDK implementation code to use this feature.

Also, you need to register your device token after initializing the SDK. The following snippets demonstrate registering the device token for iOS and Android:
    
    
    [[[RudderClient sharedInstance] getContext] putDeviceToken:[self getDeviceToken]];
    
    
    
    RudderClient.putDeviceToken(getDeviceToken())
    

You can also specify the event name to be fired after setting the device token using the [Event sent after setting device token](<https://www.rudderstack.com/docs/destinations/streaming-destinations/customer-io/setup-guide/#device-mode-settings>) dashboard setting.

> ![warning](/docs/images/warning.svg)
> 
> Make sure to fire the event just after setting the device token in your app, so RudderStack can immediately register the device token to Customer.io and not delay until the next lifecycle event.

The following snippets highlight how to send a `device_token_registered` event after setting the device token in your app:
    
    
    [[RSClient sharedInstance] track:@"device_token_registered"];
    
    
    
    rudderClient!!.track("device_token_registered")
    

RudderStack also supports removing the device (identified by `device_id`) whenever you send a custom `Application Uninstalled` event.