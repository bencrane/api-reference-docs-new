# RudderStack SDK FAQ

Answers to the generally asked questions related to the RudderStack SDKs.

* * *

  * __7 minute read

  * 


### What is the event size limit for various RudderStack SDKs?

The following RudderStack SDKs drop any events greater than 32KB:

  * iOS (Obj-C)
  * Android (Java)
  * React Native
  * Flutter
  * Unity
  * Go
  * Ruby
  * Python
  * .NET ([async initialization](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-dotnet-sdk/#initializing-the-sdk>))


The following SDKs accept events greater than 32KB:

  * Java
  * Node
  * [.NET (synchronous initialization)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-dotnet-sdk/#initializing-the-sdk>)


The [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) exhibits the following behavior:

  * If the event size exceeds 32KB, the SDK logs an error message (warning, in the case of JavaScript SDK) but forwards it to the RudderStack data plane (backend).
  * If you send the event using [`sendBeacon`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#send-events-using-beacon>), the SDK batches the events with a size limit of 64KB on the **entire** batch payload. If a single event’s size exceeds 64KB, the browser might drop the event. Note that this is applicable for the legacy SDK (v1.1) and the SDK v3.


### How does RudderStack handle `anonymousId` ?

The following are the different ways in which RudderStack handles `anonymousId` across different SDKs:

#### JavaScript SDK

The RudderStack JavaScript SDK automatically generates one unique `anonymousId` to identify a user uniquely. It then stores it in a cookie named `rl_anonymous_id` and attaches it to every subsequent event. This helps in identifying the users from other sites that are hosted under a sub-domain.

> ![info](/docs/images/info.svg)
> 
> If `anonymousId` is explicitly provided by the user using the `setAnonymousId` method, the user-specified `anonymousId` overrides the SDK-generated one.

For more information on how RudderStack handles overriding `anonymousId`, refer to the [Overriding anonymous ID](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#overriding-anonymous-id>) section.

#### Android (Java) SDK

RudderStack captures your `deviceId` and uses that as `anonymousId` for identifying the user. It is used to track the users across the application installation. To attach more information to the user, you can use the `identify` method.

You can use the `setAnonymousId` method to override and use your own `anonymousId` with the SDK.

> ![info](/docs/images/info.svg)
> 
> On Android devices, the `deviceId` is assigned during the first boot. It remains consistent across the applications and installs. It changes only after a factory reset.

#### iOS (Obj-C) SDK

RudderStack captures `deviceId` and uses that as `anonymousId` for identifying the user. To attach more information to the user, you can use the `identify` method.

You can use the `setAnonymousId` method to override and use your own `anonymousId` with the SDK.

> ![info](/docs/images/info.svg)
> 
> According to the Apple [documentation](<https://developer.apple.com/documentation/uikit/uidevice/1620059-identifierforvendor>), if the device has multiple apps from the same vendor, all those apps will be assigned the same `deviceId`. If allse apps are uninstalled, then on the next install, the apps will be assigned a new `deviceId`.

For more information on how RudderStack handles`anonymousId` in the iOS (Obj-C) SDK, see the [Anonymous ID](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/#anonymous-id>) section.

### How do I identify anonymous users across client-side and server-side?

To identify anonymous users across both client-side and server-side, **it is advisable to use a separate, new cookie at your end**.

During the user’s first visit, your server generates a new `anonymousId` to make the event calls using the server-side SDKs and sends the `set_cookie` response to the browser to set the `visitor_id` cookie.

  * If the RudderStack JavaScript SDK is **not blocked** , you can use the `setAnonymousId` method to set the same value as the `visitor_id`.
  * In case the RudderStack JavaScript SDK **is blocked** , still the next requests to the server will have the `visitor_id` cookie which can be used by the server-side events for `anonymousId`.


> ![info](/docs/images/info.svg)
> 
> The RudderStack JavaScript SDK generates a unique `anonymousId` for every unique user visit. It then stores this value in a cookie named `rl_anonymous_id` and attaches it to every subsequent event.
> 
> Users sometimes try to directly use the browser APIs to get or set the value for this cookie. However, this is not advisable since the RudderStack cookies are encrypted, and the cookie may not be present altogether (if the SDK is blocked).
> 
> It is, therefore, always advisable to use RudderStack’s `getAnonymousId` and `setAnonymousId` methods to update the cookie value.

To set `anonymousId`, use the `setAnonymousId` call after the SDK snippet as below:
    
    
    rudderanalytics.setAnonymousId("my-anon-id");
    

To get the `anonymousId` stored in a RudderStack cookie, use the `getAnonymousId` call inside the `ready` callback - this ensures that the method is available and returns the previously set `anonymousId` value.
    
    
    rudderanalytics.ready(
    	() => {
    	  var anonId = window.rudderanalytics.getAnonymousId();
    		console.log(anonId);
    	}
    );
    

### What is RudderStack’s retry and backoff logic after the connection fails?

When the dataplane gets disconnected from the SDK and events are no longer able to be sent to Rudder Server, then some of the SDK’s will store events and retry sending them to Rudder Server with a certain backoff logic.

> ![warning](/docs/images/warning.svg)
> 
> Not all SDKs support retry of failed events. Refer to the below table for more information.

#### General support and logic

SDK| Supported| Event Storage| Retry limit  
---|---|---|---  
[JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>)| Yes| 100 events in local storage| 10 times  
[Android (Java) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>)| Yes| 10000 events in SQLite database| Infinity  
[iOS (Obj-C) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>)| Yes| 10000 events in SQLite database| Infinity  
[React Native SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-react-native-sdk/>)| Yes| 10000 events in SQLite database| Infinity  
[Flutter SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-flutter-sdk/>)| Yes| 10000 events in SQLite database| Infinity  
[Node.js SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-node-sdk/>)| Yes| 20000 events in-memory| 10 times  
Other SDKs| No| N/A| N/A  
  
#### JavaScript SDK

This SDK can be configured to match your requirements for retry and backoff logic. By default, if the dataplane goes down and the JS SDK cannot send events to the Rudder Server, up to 100 events will be stored. While still disconnected from the dataplane, the JS SDK will try to resend the stored events to the Rudder Server. However, for each retry, the delay duration will grow. The equation to get the duration of delay is as follows:

dt = md * (F^n)

Where, `dt` is the delay time in ms, `md` is the `minRetryDelay` (configurable; default is 1000 ms), `F` is the `backoffFactor` (configurable; default is 2), and `n` is the current retry attempt. The SDK will retry until the attempts surpass the `maxAttempts` value. This is by default set to 10 attempts but is configurable. Each retry attempt, the delay time grows exponentially. However, it will max out at whatever the `maxRetryDelay` is. By default, this value is set at 360000 ms, but it is configurable.

#### iOS (Obj-C) and Android (Java) SDK

Starting from v1.24.0 (Android (Java)) and v1.28.0 ( iOS (Obj-C)), both the SDKs implement an exponential backoff mechanism to handle data plane connection failures.

If the data plane becomes unavailable, both the Android (Java) and iOS (Obj-C) SDKs store up to 10000 events and continue retrying indefinitely to send the failed events.

Retries occur exponentially for all `4xx` and `5xx` status codes, except for `400` and `404`— for these specific status codes, as well as in cases where the network is unavailable, retries occur every second. The exponential backoff delay increases with each retry attempt, capping at a maximum of 5 minutes, after which the retry process resets and starts over.

#### Node.js SDK

Currently the Node.js SDK is the only server-side SDK that supports event retry and backoff logic. The logic is quite similar to the JavaScript SDK. If the connection fails, up to 20,000 events will be stored. However, this is in-memory storage and can result in data loss. The SDK will retry a maximum of 10 times, by default. For each retry the delay duration between retries will grow and can be calculated using the following equation.

dt = 1000 * (2^n)

Where, dt is the delay time in ms and n is the current retry attempt. The SDK will retry until the attempts surpass the `maxAttempts` value which is set to 10 attempts. With each retry attempt, the delay time will grow exponentially. However, it will never be greater than the maximum delay duration which is 30 seconds.

> ![info](/docs/images/info.svg)
> 
> The Node.js SDK does have a feature to persist the event data in Redis for more event storage and better guarantees of failed event delivery. Instructions on how to configure the Redis solution can be found [here](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-node-sdk/#data-persistence>).

### Can I filter and selectively send event data to certain destinations?

Yes, you can use RudderStack’s [Client-side Event Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) feature to specify which events should be discarded or allowed to flow through - by allowlisting or denylisting them in the RudderStack dashboard while setting up your destination. This method is useful if you are sending the events via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).