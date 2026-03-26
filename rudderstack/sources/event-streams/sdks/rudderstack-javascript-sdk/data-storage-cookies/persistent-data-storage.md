# Configure Persistent Data Storage in JavaScript SDK

> Version: Latest (v3)v1.1

# Configure Persistent Data Storage in JavaScript SDK

Set your information storage preferences while loading the JavaScript SDK.

* * *

  * __5 minute read

  * 


While loading the JavaScript SDK, you can specify the information to store (`userId`, `anonymousId`, session information, etc.) and whether to store it in your browser or not store it at all (fully anonymous tracking).

> ![success](/docs/images/tick.svg)
> 
> The fully anonymous tracking feature is a part of RudderStack’s [Data Governance toolkit](<https://www.rudderstack.com/docs/data-governance/overview/>) that ensures the quality and integrity of your data in a secure and compliant manner.

## Persisted data

You can use the JavaScript SDK to persist the following data:

  * User (ID and traits)
  * Group (ID and traits)
  * Anonymous user ID
  * Initial referrer and domain
  * Session
  * Authentication token


## Set storage type

> ![warning](/docs/images/warning.svg)
> 
> You can set the storage configuration only for the persisted data mentioned above.
> 
> It is **not** applicable for the [local storage cookies](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/#local-storage>) that the SDK uses to process and send events to the RudderStack backend.

To set the storage type for your stored information, provide a `type` field in the [`storage` option](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#storage>) while loading the JavaScript SDK:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      storage: {
        type: "cookieStorage" / "localStorage" / "sessionStorage" / "memoryStorage" / "none"
      }
      // other load options
    });
    

The `type` parameter accepts the following values:

Value| Description  
---|---  
`cookieStorage`| SDK persists the user information in cookies and uses it for subsequent events.  
  
If cookies are unavailable (for example, incognito mode), then the SDK falls back to local storage, followed by session storage, and then in-memory storage.  
`localStorage`| SDK persists user information in local storage and uses it for subsequent events.  
  
If local storage support is unavailable (for example, incognito mode), then the SDK falls back to session storage.  
`sessionStorage`| SDK persists user information in the browser’s session storage and uses it for subsequent events.  
  
If session storage support is not available, the SDK falls back to in-memory storage.  
`memoryStorage`| User information is persisted in-memory.  
  
SDK uses this information for subsequent events till the browser tab is closed or you reload/refresh the page.  
`none`| SDK performs [fully anonymous tracking](<https://www.rudderstack.com/docs/data-governance/cookieless-tracking/>) without storing any user information.  
  
Every event payload will have a new `anonymousId` and subsequent events will not carry any user data from the previous event. To identify these truly anonymous events, SDK sets a new flag `trulyAnonymousTracking` in the `context` object.  
  
> ![warning](/docs/images/warning.svg)
> 
> Do not block or denylist `localStorage` entries as they are critical for the functioning of the JavaScript SDK.

> ![info](/docs/images/info.svg)
> 
> Note the following:
> 
>   * If not specified, the SDK sets the default storage `type` to `cookieStorage` and uses it to store all user data.
>   * If you set the storage `type` to `none`, the SDK generates a new `anonymousId` for each event. This ensures complete anonymity but may impact user journey tracking across multiple events.
> 


### Set storage for specific information type

You can also set a different storage option for a specific information while loading the JavaScript SDK. Use the `entries` object in the `storage` load option and define the storage type for your user data.

Note the following:

  * The storage options set in the `entries` object override the global storage `type`.
  * The SDK uses the global storage `type` for storing user data that is not explicitly defined in the `entries` object.
  * The SDK migrates the existing user data to the newly selected storage option automatically.
  * The SDK removes any stored user data if you set `type` to `none`.


    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      storage: {
        entries: {
          userId: {
            type: "cookieStorage"
          },
          userTraits: {
            type: "localStorage"
          },
          sessionInfo: {
            type: "none"
          }
        }
      }
      // other load options
    });
    

In the above snippet, the global storage `type` is not defined. Hence, the SDK uses `cookieStorage` as the default storage option. Based on the `entries` object configured above, the SDK stores the user information as follows:

User information| Storage option  
---|---  
`userId`, `anonymousId`, `groupId`, `groupTraits`, `initialReferrer`, `initialReferringDomain`| `cookieStorage`  
`userTraits`| `localStorage`  
`sessionInfo`| `none`  
  
## Use cases

Suppose you define the following storage configurations for `userId` while loading the JavaScript SDK:

**Case 1**
    
    
     rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      storage: {
        entries: {
          userId: {
            type: "cookieStorage"
          },
        }
      }
      // other load options
    });
    

When you trigger an `identify` call with `user123` as the `userId`, the SDK persists `user123` in the cookie storage. If a `track` call is triggered next, the payload will contain `user123` as the `userId`.

**Case 2**
    
    
     rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      storage: {
        entries: {
          userId: {
            type: "none"
          },
        }
      }
      // other load options
    });
    

When you trigger an `identify` call, the SDK will **not** store the `userId` and the next set of events will have `userId` as an empty string (`""`).

**Case 3**

If you set the global storage `type` to `none` and then define the `type` in the `entries` object, then the SDK will **not** treat it as truly anonymous tracking.
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      storage: {
        type: "none",
        entries: {
          userId: {
            type: "cookieStorage"
          },
        }
      }
      // other load options
    });
    

In this case, the SDK replicates the behavior described in **Case 1**.

## Test and verify storage configuration

  1. Load the SDK with the required storage settings.

  2. Open your browser’s developer tools:

     * Chrome: Right-click and select **Inspect** or press Ctrl+Shift+I (Windows/Linux) or Cmd+Option+I (Mac)
     * Firefox: Right-click and select **Inspect Element** or press Ctrl+Shift+I (Windows/Linux) or Cmd+Option+I (Mac)
  3. Navigate to the appropriate storage tab:

     * For Cookies: Go to the **Application** tab (Chrome) or **Storage** tab (Firefox) and select **Cookies**.
     * For Local Storage: Go to the **Application** tab (Chrome) or **Storage** tab (Firefox) and select **Local Storage**.
     * For Session Storage: Go to the **Application** tab (Chrome) or **Storage** tab (Firefox) and select **Session Storage**.
  4. Trigger various SDK calls (`identify`, `track`, etc.) and observe the stored data in the relevant storage locations.

  5. Refresh the page or open a new tab to verify persistence.

  6. Use incognito mode to test fallback behavior.


Example:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      storage: {
        type: "localStorage",
        entries: {
          userId: { type: "cookieStorage" }
        }
      }
    });
    
    rudderanalytics.identify("1hKOmRA4GRlm", { name: "Alex Keener" });
    

After running this code, check your browser’s local storage for user traits and cookies for `userId`.

  


  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/specify-cookie-domain/>)