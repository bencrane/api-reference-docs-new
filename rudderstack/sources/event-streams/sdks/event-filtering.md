# Client-side Events Filtering

Filter events for your allowlist or denylist.

* * *

  * __2 minute read

  * 


RudderStack’s client-side event filtering feature lets you specify which events should be discarded or allowed to flow through by allowlisting or denylisting them.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * Client-side event filtering is applicable only for `track` calls. In case of mobile SDKs, it also applies to the following application lifecycle events:
>     * Application Installed
>     * Application Opened
>     * Application Backgrounded
>     * Application Updated
>   * You can use this feature for all RudderStack destinations that support sending events via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).
>   * To use this feature with the latest [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>), note that:
>     * Empty and non-string event names are not allowlisted anymore.
>     * Event name comparison is case-sensitive.
> 


## Supported SDKs

The following source SDKs support this feature:

  * [JavaScript](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>)
  * [Android (Java)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>)
  * [iOS (Obj-C)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>)
  * [React Native](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-react-native-sdk/>)
  * [Flutter](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-flutter-sdk/>)
  * [Cordova](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-cordova-sdk/>)


## Event filtering options

RudderStack gives you the ability to configure your event filtering options while setting up your device mode destination in the dashboard:

[![Event filtering options](/docs/images/event-stream-sources/rudderstack-event-filtering.webp)](</docs/images/event-stream-sources/rudderstack-event-filtering.webp>)

You will see the following dropdown options under **Event Filtering** , in the **Connection Settings** page:

### Disable

Event filtering will be disabled if you select this option from the dropdown. In this case, RudderStack will not filter any events and allow all events to flow through.

### Allowlist

Upon selecting the **Allowlist** option from the dropdown, you can specify the names of the events that you want RudderStack to **allow** or flow through to the destination.

> ![info](/docs/images/info.svg)
> 
> If you choose the **Allowlist** option for event filtering, any events specified in the **Denylist** field will be ignored.

You can add as many events as you want to the allowlist by clicking the **Add More** option.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack will discard any event that is not specified in the allowlist. If you do not specify any events in the allowlist, **all** the calls will be discarded.

### Denylist

Upon selecting the **Denylist** option from the dropdown, you can specify the names of the events that you want RudderStack to **discard**. These events will not be sent to the destination.

> ![info](/docs/images/info.svg)
> 
> If you choose the **Denylist** option for event filtering, any events specified in the **Allowlist** field will be ignored.

You can add as many events as you want to the denylist by clicking on the **Add More** option.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack will only discard events explicitly specified in the denylist. If you do not specify any events in the denylist, then **all** calls will be allowed through.