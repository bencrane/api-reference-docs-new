# How to Specify the Cookie Domain

> Version: Latest (v3)v1.1

# How to Specify the Cookie Domain

Configure the JavaScript SDK to store cookies on a specific domain.

* * *

  * __3 minute read

  * 


This guide shows you how to configure the RudderStack JavaScript SDK to store its cookies on a specific domain, rather than the default top-level domain. This can be useful in scenarios where you need finer control over cookie scope.

## Default behavior

The SDK automatically sets cookies at the top-level domain (for example, `example.com`). This enables consistent user identification across subdomains like `admin.example.com` and `app.example.com`, without requiring additional configuration.

This behavior can be customized by configuring SDK’s [`load` options](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/>).

## Configuration steps

  1. Initialize the JavaScript SDK using the `rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, loadOptions)` method.
  2. Set the [`storage.cookie.domain` parameter](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#cookie-settings>) to the domain where you want cookies to be stored.


## Code example
    
    
    // Replace with your write key and data plane URL
    const WRITE_KEY = "YOUR_WRITE_KEY";
    const DATA_PLANE_URL = "YOUR_DATA_PLANE_URL";
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      // Other load options
    
      storage: {
        cookie: {
          // Specify the domain for cookies
          domain: "subdomain.example.com" // Example: Store only on .subdomain.example.com, allowing it to be accessible from its subdomains like blog.subdomain.example.com, etc.
    
          // domain: "example.com" // Example: Explicitly store on top-level domain enabling tracking across all subdomains, the default behavior
        }
      }
    });
    

## Enable strict domain-level cookie scoping

You can use the [`sameDomainCookiesOnly` parameter](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/>) to enable strict domain-level cookie scoping. When set to `true`, the SDK sets cookies only for the exact domain where the SDK is loaded, preventing them from being shared with subdomains or the top-level domain.

This can be useful in scenarios where you need to:

  * Isolate cookie data to a specific subdomain for security or compliance reasons.
  * Prevent cookie sharing between different subdomains.
  * Ensure that each subdomain maintains its own separate user tracking.


> ![info](/docs/images/info.svg)
> 
> If you set `sameDomainCookiesOnly: true`, it takes precedence over the `storage.cookie.domain` parameter, and ensures cookies are scoped to the exact domain, regardless of the `storage.cookie.domain` setting.

A sample snippet highlighting the usage of the `sameDomainCookiesOnly` parameter is shown below:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      // Enable strict domain-level cookie scoping
      sameDomainCookiesOnly: true,
      
      // Other load options
    });
    

## Default behavior vs. strict scoping

`sameDomainCookiesOnly` value| Behavior  
---|---  
`false`| Cookies are stored at the top-level domain (for example, `.example.com`), allowing them to be shared across all subdomains (for example, `app.example.com`, `blog.example.com`).  
`true`| Cookies are scoped only to the exact domain where the SDK is loaded. For example, if the SDK is loaded on `app.example.com`, cookies are scoped only to `app.example.com` and are not accessible from `blog.example.com`, `example.com`, or `sub.app.example.com`.  
  
## Scenarios

The following scenarios illustrate the difference between the default behavior and the strict domain-level cookie scoping.

### Default behavior (shared cookies)

If you load the SDK on `app.example.com` with `sameDomainCookiesOnly: false` (default):
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      sameDomainCookiesOnly: false // or omit this parameter
    });
    

  * Cookies are set for `.example.com` (top-level domain)
  * Cookies are accessible from all subdomains (`app.example.com`, `blog.example.com`, etc.)
  * User tracking is consistent across all subdomains


### Subdomain isolation

If you load the SDK on `app.example.com` with `sameDomainCookiesOnly: true`:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      sameDomainCookiesOnly: true
    });
    

  * Cookies are set only for `app.example.com`
  * Cookies are **not** accessible from `blog.example.com`, `example.com`, or `sub.app.example.com`
  * Each subdomain maintains separate user tracking


  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/persistent-data-storage/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/decrypt-persisted-data/>)