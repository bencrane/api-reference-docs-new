# Data Persistence in JavaScript SDK

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk>)

# Data Persistence in JavaScript SDK

Understand how our JavaScript SDK persists user data stored in cookies or local storage.

* * *

  * __3 minute read

  * 


The JavaScript SDK stores persistent user data in the cookies by default. If the cookies are not supported, the SDK uses local storage instead.

By default, the SDK stores all cookies in the top-level domain. It helps you to identify the users visiting websites hosted under a particular sub-domain. For example, if you include the JavaScript SDK in both `admin.samplewebsite.com` and `app.samplewebsite.com`, the SDK will store the cookie in `samplewebsite.com`. However, you can specify the cookie storage location by using the `setCookieDomain` parameter in the [`load`](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/load-js-sdk/>) API options as shown:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      setCookieDomain: "samplewebsite.com",
    });
    

> ![info](/docs/images/info.svg)
> 
> Replace the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) in the snippet with their actual values.

## Cookies

The cookie values are encrypted and their length is directly proportional to the values provided to the SDK. Also, all cookie names are prefixed with `rl_` and the values are prefixed with `RudderEncrypt:`. For example, `rl_user_id —> RudderEncrypt:U2FsdGVkX1+UKmiooYoGmKdNws7sgmWgGfHe`.

The following table lists the cookies used by the JavaScript SDK to store persistent user data:

Name| Description| Clearing mechanism  
using the SDK  
---|---|---  
`rl_user_id`| Stores the user ID set via the `identify` API.  
  
For example: `4578`, `USER_001`| `rudderanalytics.reset()`  
`rl_trait`| Stores the user traits object set via the `identify` API.  
  
For example:
    
    
    {  
      email: “[alex@example.com](<mailto:alex@example.com>)”,  
      accountType: “pro”,  
      country: “US”,  
      someObj: {  
        key1: val1,  
        key2: val2,  
      }  
    }

| `rudderanalytics.reset()`  
`rl_anonymous_id`| Stores the anonymous ID. By default, it would be the auto-generated unique ID by SDK for each visitor unless overridden via `setAnonymousId` API.  
  
For example: `5bfe258f-bd2f-49cf-bddd-8b844f74ab4b`, `customAnonId`| `rudderanalytics.reset(true)`  
`rl_group_id`| Stores the user group ID set via the `group` API.  
  
For example: `GRP_3`, `98`| `rudderanalytics.reset()`  
`rl_group_trait`| Stores the user group traits set via the `group` API.  
  
For example:
    
    
    {  
      location: “New Orleans”,  
      nationality: “US”,  
      someObj: {  
        key1: val1,  
        key2: val2,  
      }  
    }

| `rudderanalytics.reset()`  
`rl_page_init_referrer`| Stores the initial referrer of the page when a user visits a site for the first time.  
  
For example: `https://www.google.com/`| Cannot be cleared using SDK.  
`rl_page_init_referring_domain`| Stores the initial referring domain of the page when a user visits a site for the first time.  
  
For example: `google.com`| Cannot be cleared using SDK.  
`test_rudder_cookie`| Checks whether the cookie storage of a browser is accessible or not. Once checked, the SDK removes the cookie immediately.  
  
For example: `test_rudder_cookie:true`| Cleared automatically.  
`rl_session`| Stores the session-related information including `sessionId` if session tracking is enabled.  
  
For example: `1678961874`| Manual session tracking: `rudderanalytics.endSession()`  
  
Automatic session tracking: Automatically cleared by the SDK (if `autoTrack`: `false`).  
`rl_auth_token`| Stores the authentication token passed by the user.  
  
For example: `MOx2ZmMwLNE2A2IdNKL0N2VhN2I3Z`| `rudderanalytics.reset()`  
  
## Local storage

RudderStack stores the local storage cookie names with `rudder.<uuid>.` prefix where `uuid` is in the standard UUID v4 format. For example, `rudder.2dc2aee6-2836-4273-be69-79c90c04ddec.reclaimEnd`.

The JavaScript SDK uses local storage to keep track of the events sent to the RudderStack backend, as listed in the below table:

Name| Description  
---|---  
`ack`| Timer for other browser tabs to claim control of the retry queue.  
For example, `1639734070124`  
`reclaimStart` and `reclaimEnd`| Determines if a tab takes over the queue from another tab.  
For example, `2dc2aee6-2836-4273-be69-79c90c04ddec`  
`inProgress`| Keeps track of the events in progress. For example:  

    
    
    {  
      “d89d7fb5-945e-4378-bda5-492e4b596fb4”: {  
       “item”: {  
        “url”: “[https://rudderstack-dataplane.rudderstack.com/v1/track"](<https://rudderstack-dataplane.rudderstack.com/v1/track%22>),  
        “headers”: {  
         “Content-Type”: “application/json”,  
          …  
        },  
        “message”: {   
         …  
        }  
        “attemptNumber”: 1,  
        “time”: 1639734792773,  
        “id”: “a4d89d7f-b594-4eb3-b8bd-a5492e4b596f”  
       }  
      }  
    }  
      
  
`queue`| Keeps track of the events that are in the processing queue. For example:  

    
    
    [  
      {  
       “item”: {  
        “url”: “https://rudderstack-dataplane.rudderstack.com/v1/track”,  
        “headers”: {  
         “Content-Type”: “application/json”,  
          …  
        },  
        “message”: {   
         …  
        }  
        “attemptNumber”: 0,  
        “time”: 1639734792773,  
        “id”: “a4d89d7f-b594-4eb3-b8bd-a5492e4b596f”  
       }  
      }  
    ]  
      
  
  * [![](/docs/images/previous.svg)Previous](</docs/archive/javascript-sdk/1.1/supported-api/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/javascript-sdk/1.1/filtering/>)