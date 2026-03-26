# Data Persistence in JavaScript SDK

> Version: Latest (v3)v1.1

# Data Persistence in JavaScript SDK

Understand how our JavaScript SDK persists user data stored in cookies or local storage.

* * *

  * __4 minute read

  * 


The JavaScript SDK persists some user data in the browser to maintain user identity and session information across page loads and visits. It primarily uses cookies but can fall back to other browser storage mechanisms. The SDK also persists some essential data to ensure efficient event delivery.

## Storage strategy

The JavaScript SDK uses a hierarchical storage strategy for the user data by default.

  1. **Cookies (Default):** The SDK attempts to store persistent data in cookies first, as they provide the best cross-domain capabilities.
  2. **Local Storage (Fallback):** If cookies are not available (due to browser settings or limitations), the SDK automatically falls back to using local storage.
  3. **Session Storage (The next fallback):** If the local storage is not available, the SDK falls back to session storage.
  4. **Memory Storage (The final fallback):** If none of the other storage available, the SDK stores data in the memory. In this case, the data is lost on closing/refreshing the page.


You can explicitly customize the [storage settings](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/persistent-data-storage/#set-storage-type>) as per your preferences.

> ![success](/docs/images/tick.svg)
> 
> By default, cookies are set on the top-level domain (e.g., `example.com`) to enable user identification across different subdomains (like `app.example.com` and `docs.example.com`). You can configure the SDK to use a specific domain instead. See [How to Specify the Cookie Domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/specify-cookie-domain/>) for guidance.

## Cookie storage

The SDK stores various pieces of data related to user identity and session state.

  * All SDK-managed cookie names are prefixed with `rl_`
  * Stored cookie values are encrypted and prefixed with `RS_ENC_v3_`


### Cookies used by the JavaScript SDK

The following table lists the cookies used by the JavaScript SDK to store persistent user data:

> ![info](/docs/images/info.svg)
> 
> Cookie data persists in all subsequent event payloads until cleared automatically or manually (see “How to Clear” column)

Cookie| Example Value (unencrypted)| Description| How to Clear  
---|---|---|---  
`rl_user_id`| `4578` or `USER_001`| User ID set via the `identify` API call| `rudderanalytics.reset()`  
`rl_trait`| `{ "email": "alex@example.com", country: "US", someObj: { key1: val1 } }`| User traits object set via the `identify` API call| `rudderanalytics.reset()`  
`rl_anonymous_id`| `5bfe258f-bd2f-49cf-bddd-8b844f74ab4b`| Anonymous ID string. Defaults to an auto-generated UUID unless overridden via `setAnonymousId` API| `rudderanalytics.reset(true)`  
`rl_group_id`| `GRP_3` or `98`| Group ID set via the `group` API call| `rudderanalytics.reset()`  
`rl_group_trait`| `{ location: "London", nationality: "US", someObj: { key1: val1 } }`| Group traits object set via the `group` API call| `rudderanalytics.reset()`  
`rl_page_init_referrer`| `https://www.google.com/`| Initial referrer URL string from the user’s first visit in the storage lifetime| Cannot be cleared using SDK  
`rl_page_init_referring_domain`| `google.com`| Initial referring domain string from the user’s first visit| Cannot be cleared using SDK  
`test_rudder_cookie`| `true`| Temporary cookie used internally to check if cookie storage is accessible. Removed immediately| Cleared automatically  
`rl_session`| `{"id":1744610733549,"expiresAt":1744612623357,"timeout":1800000,"autoTrack":true,"sessionStart":false}`| Session information when session tracking is enabled| Manual: `rudderanalytics.endSession()`  
Automatic: Cleared automatically if `autoTrack: false`  
`rl_auth_token`| `MOx2ZmMwLNE2A2IdNKL0N2VhN2I3Z`| User-provided authentication token| `rudderanalytics.reset()`  
  
> ![success](/docs/images/tick.svg)
> 
> You can manage the [storage type settings](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/persistent-data-storage/#set-storage-type>) for these entries.

## Local storage

The SDK utilizes local storage for two main reasons:

  1. **Event Queue Management:** Internally tracks event delivery status, manages retries, and handles event batching. This usage is independent of user data persistence settings.
  2. **Fallback Storage:** Serves as a storage location for user identity and session data if cookies are unavailable and `localStorage` is configured as the primary or fallback mechanism.


### Naming convention for internal keys

Local storage keys used for internal event queue management are prefixed as follows:

  * **Standard Mode Transport** : `rudder_<write-key>.<uuid>.` e.g. `rudder_28xsd8CjukXbMPt1ZaTzdedjXRE.2dc2aee6-2836-4273-be69-79c90c04ddec.queue`
  * **Beacon Mode Transport** (when `useBeacon: true` in the SDK’s `load` options): `rudder_beacon_<write-key>.<uuid>.` e.g. `rudder_beacon_28xsd8CjukXbMPt1ZaTzdedjXRE.2dc2aee6-2836-4273-be69-79c90c04ddec.ack`


> Where `<write-key>` is your RudderStack source write key and `<uuid>` is a standard v4 UUID

### Internal local storage keys

The table below lists keys used internally by the SDK for event processing:

Name| Purpose| Example  
---|---|---  
`ack`| Timer for browser tabs to claim control of the retry queue| `1639734070124` (timestamp)  
`batchQueue`| Tracks the events queued for batched processing| Array of grouped events pending delivery  
`reclaimStart` and `reclaimEnd`| Coordinates tab handover for event processing| `2dc2aee6-2836-4273-be69-79c90c04ddec`  
`inProgress`| Tracks events currently being processed| Object mapping event IDs to their processing state  
`queue`| Tracks all events in the processing queue| Array of events pending delivery  
  
> ![warning](/docs/images/warning.svg)
> 
> **Important considerations**
> 
> Note the following:
> 
>   * You cannot change the [storage configuration type](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/persistent-data-storage/#set-storage-type>) for these entries as they are necessary for processing the events.
>   * Do not block or denylist the `localStorage` entries as they are critical for the functioning of the JavaScript SDK.
> 


To learn about other storage mechanisms, check out [Persistent Data Storage Configuration](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/persistent-data-storage/#set-storage-type>).

## Accessing stored data

If you need to programmatically access or decrypt data stored by the SDK (e.g., reading the anonymous ID on the server-side), utility functions are available.

See [How to Decrypt Stored SDK Data](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/decrypt-persisted-data/>) for instructions and examples.

  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/events-tracking-assistant/troubleshooting/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/persistent-data-storage/>)