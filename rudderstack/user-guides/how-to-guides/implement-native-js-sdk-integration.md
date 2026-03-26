# Implement Native JavaScript SDK Integration

Add a destination SDK to the base RudderStack JavaScript SDK when sending events through the native integration.

* * *

  * __2 minute read

  * 


This guide is helpful if you want to add a destination SDK to the [RudderStack JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) while sending events directly via your native integration **without RudderStack support**.

> ![info](/docs/images/info.svg)
> 
> This guide uses the terms **integration** and **destination** interchangeably.

The RudderStack JavaScript SDK reads the config data from the control plane to fetch native integrations. The native integrations must have the following methods/attributes defined by you as shown below. The RudderStack SDK calls these for initializing the destination global object and forwarding event data namely `identify`, `page` and `track`.

[![](/docs/images/screenshot-2019-12-10-at-7.57.43-pm.webp)](</docs/images/screenshot-2019-12-10-at-7.57.43-pm.webp>)

  * **constructor** : RudderStack JS SDK, constructs an integration object with the destination specific keys such as `name`, `apiKey,` `custom mappings etc`, fetched from your config plane. These information are required by the below calls.
  * **init** : Add the destination script (JavaScript snippet provided by the destination to initialize a global queue on window object)
  * **identify** : RudderStack JS SDK calls this method to pass identify event data. One can write custom logic specific to the destination before calling destination specific implementation.
  * **page** : Similar to identify, with page event data
  * **track** : Similar to identify, with track event data
  * **isLoaded** : RudderStack JS SDK checks the output of this method, once true, events are forwarded to above methods.


> ![info](/docs/images/info.svg)
> 
> RudderStack JS SDK makes a call to the config plane to fetch all native SDK **true** destinations before constructing and initializing the integration object with the fetched config.
> 
> The **isLoaded** method return true when the global destination object is ready. RudderStack JS SDK waits for a maximum of 10 secs and polls for this flag to be ready every 1sec. Once all native SDK enabled integrations are ready, all event data accumulated from the time of page load is replayed on these integrations.

> ![info](/docs/images/info.svg)
> 
> The input to identify, page, track methods/property of the integration object is the entire event data object constructed by utility methods of the core analytics object.

### Code structure

[![](/docs/images/screenshot-2019-12-10-at-7.21.35-pm.webp)](</docs/images/screenshot-2019-12-10-at-7.21.35-pm.webp>)[![](/docs/images/screenshot-2019-12-10-at-7.22.25-pm.webp)](</docs/images/screenshot-2019-12-10-at-7.22.25-pm.webp>)

To add a new integration, add the above said methods to a JS object and export that object to be picked up by the **integrations** map.

This map is iterated and matched against the config fetched from the control plane to construct only those enabled integrations. This is matched against the `name` property of the integration object and destination config `name` .

`All the activities of fetching configs and constructing and event forwarding to integrations is handled by the core analytics object.`

> Refer the existing integrations in case of any parameter reference.  
> For adding destination JS snippet, use the init method of the new integration.

##### [How to add a device mode SDK to the RudderStack JavaScript SDK](</docs/user-guides/how-to-guides/implement-native-js-sdk-integration/add-device-mode-sdk-to-js/>)

Add an integration to the RudderStack JavaScript SDK to enable native device mode.