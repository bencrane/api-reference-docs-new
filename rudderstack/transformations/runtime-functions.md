# Runtime Functions in Transformations

Complete reference for runtime functions available in transformations.

* * *

  * __7 minute read

  * 


This guide provides a complete reference for the runtime functions available in JavaScript and Python transformations.

> ![announcement](/docs/images/announcement.svg)
> 
> Python transformations are available only in the RudderStack [Growth](<https://rudderstack.com/pricing/>) and [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plans.

## Overview

RudderStack injects several runtime functions into your transformations. You can use these functions to:

  * Access event metadata
  * Make external API calls
  * Enrich events with geolocation data
  * Retrieve credentials
  * Capture debug logs


## `metadata()`

RudderStack injects the `metadata` function as the second argument to `transformEvent` and `transformBatch`. Use it to access event metadata and customize your transformation logic based on source, destination, or connection mode.

### What you can do

  * Read source and destination identifiers for routing or filtering
  * Access the unique message ID for each event
  * Check the connection mode (`deviceMode` or `cloudMode`) in hybrid mode destinations
  * Access the device mode token (`Custom-Authorization`) for tokenization validation


### What it returns

An object containing the following properties when available:

Property| Description  
---|---  
`sourceId`| The source ID from the [Settings](<https://www.rudderstack.com/docs/dashboard-guides/sources/#source-details>) tab of your source.  
`sourceName`| The source name set in the RudderStack dashboard. For example, `JavaScript-QA`, `TestJSSource`.  
`destinationId`| The destination ID from the [Settings](<https://www.rudderstack.com/docs/dashboard-guides/destinations/#destination-details>) tab of your destination.  
`messageId`| The unique ID for each event.  
`sourceType`| The source type, for example, Android, iOS.  
`destinationType`| The destination type where RudderStack sends the transformed event, for example, Snowflake.  
`mode`| The connection mode: `deviceMode` or `cloudMode`. Available for hybrid mode destinations.  
`Custom-Authorization`| The device mode token when [tokenization](<https://www.rudderstack.com/docs/transformations/usage/#tokenization>) is enabled.  
  
### Examples
    
    
    export function transformEvent(event, metadata) {
      const meta = metadata(event);
      event.sourceId = meta.sourceId;
    
      return event;
    }
    
    
    
    def transformEvent(event, metadata):
        meta = metadata(event)
        event['sourceId'] = meta['sourceId']
        return event
    

### Usage

See [Transform a single event](<https://www.rudderstack.com/docs/transformations/usage/#apply-transformation-on-single-event>) for more information on using the `metadata` function.

## `fetch()`

RudderStack injects an asynchronous `fetch` function in JavaScript transformations. Use it to make external API calls and enrich events with data from third-party services.

### What you can do

  * Make HTTP requests (GET, POST, PUT, DELETE, and others) to external APIs
  * Enrich events with data from services like Clearbit, IP geolocation APIs, or custom backends
  * Pass custom headers and request bodies


### What it returns

The response from the API call in JSON format.

> ![warning](/docs/images/warning.svg)
> 
> For JavaScript transformations, RudderStack imposes a [4 second execution timeout limit](<https://www.rudderstack.com/docs/transformations/usage/#limitations>). This limit does not include the time for `fetch` or `fetchV2` calls to complete. RudderStack recommends using batch API requests instead of a separate request per event when possible.
> 
> Depending on your use case, you may also need to [allowlist RudderStack IP addresses](<https://www.rudderstack.com/docs/transformations/usage/#ip-allowlisting>) for the API endpoints you access.

### Examples
    
    
    export async function transformEvent(event, metadata) {
      const res = await fetch("https://api.example.com/enrich", {
        method: "POST",
        headers: {
          "Content-Type": "application/json;charset=UTF-8",
          Authorization: "Bearer <authorization_token>"
        },
        body: JSON.stringify(event)
      });
      event.response = JSON.stringify(res);
      return event;
    }
    

### Usage

See the following sections for more information on using the `fetch` function:

  * [Make external API requests](<https://www.rudderstack.com/docs/transformations/usage/#make-external-api-requests>)
  * [User Enrichment](<https://www.rudderstack.com/docs/transformations/templates/#user-enrichment>)


## `fetchV2()`

`fetchV2` is a wrapper for the `fetch` call in JavaScript transformations. Use it when you need structured access to response properties such as status code, headers, and body, or when you need timeout control.

### What you can do

  * Make external API calls with structured response handling
  * Access response status, URL, headers, and body separately
  * Set a timeout to handle slow or unresponsive APIs
  * Handle failures more efficiently than with raw `fetch`


### What it returns

An object with the following properties:

Property| Description  
---|---  
`status`| The HTTP status code of the response, for example, `200`.  
`url`| The URL of the Fetch API request.  
`headers`| The response headers.  
`body`| The response body in JSON or TEXT format. By default, it is JSON.  
  
### Examples
    
    
    export async function transformEvent(event, metadata) {
      try {
        const res = await fetchV2("https://api.example.com/data", { timeout: 1000 });
        if (res.status == 200) {
          event.response = JSON.stringify(res.body);
        }
      } catch (err) {
        log(err.message);
      }
      return event;
    }
    

Using `fetchV2` with credentials:
    
    
    export async function transformEvent(event, metadata) {
      const url = getCredential('URL');
      const authToken = getCredential('authToken');
      const response = await fetchV2(`${url}/endpoint`, {
        headers: {
          Authorization: "Bearer " + authToken
        }
      });
      event.value = response.body;
      return event;
    }
    

> ![info](/docs/images/info.svg)
> 
> Depending on your use case, you may also need to [allowlist RudderStack IP addresses](<https://www.rudderstack.com/docs/transformations/usage/#ip-allowlisting>) for the API endpoints you access via `fetchV2`.

### Usage

See the following sections for more information on using the `fetchV2` function:

  * [Make external API requests](<https://www.rudderstack.com/docs/transformations/usage/#make-external-api-requests>)
  * [Use credentials in transformations](<https://www.rudderstack.com/docs/transformations/credentials/#use-credentials-in-transformations>)
  * [Geolocation enrichment transformation template](<https://www.rudderstack.com/docs/transformations/templates/#geolocation-enrichment>)


## `geolocation()`

The `geolocation` function enriches events with geolocation data from an IP address. RudderStack uses the MaxMind GeoLite2 database embedded in its service.

> ![info](/docs/images/info.svg)
> 
> This function is available only on the [Growth](<https://rudderstack.com/pricing/>) and [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plans. For source-level enrichment, RudderStack recommends the [Geolocation Enrichment at Source](<https://www.rudderstack.com/docs/data-governance/geolocation-service/>) feature.

> ![announcement](/docs/images/announcement.svg)
> 
> If you host RudderStack on-premise, [contact the Customer Success team](<mailto:support@rudderstack.com>) to use this feature.

### What you can do

  * Resolve an IP address to geolocation data
  * Enrich events with city, country, region, and timezone for analytics and segmentation
  * Query events by location in your warehouse or destination


### What it returns

An object containing the following geolocation fields:

Property| Description  
---|---  
City| The city name.  
Country| The country code.  
Region| The region or state.  
Location| Latitude and longitude.  
Postal code| The postal or ZIP code.  
Timezone| The timezone.  
  
> ![warning](/docs/images/warning.svg)
> 
> RudderStack returns a `400 Bad Request` error if you pass a malformed IP address. The geolocation data varies in accuracy by country.

### Examples
    
    
    export async function transformEvent(event, metadata) {
      if (event.request_ip) {
        try {
          if (!event.context) event.context = {};
          event.context.geo = await geolocation(event.request_ip);
        } catch (e) {
          log(e.message);
        }
      }
      return event;
    }
    
    
    
    def transformEvent(event, metadata):
        try:
            if event.get('request_ip'):
                res = geolocation(event["request_ip"])
                if not event.get('context', None):
                    event['context'] = {}
                event['context']['geo'] = res
        except Exception as e:
            log(str(e))
        return event
    

### Usage

See [Geolocation Enrichment](<https://www.rudderstack.com/docs/transformations/geolocation-enrichment/>) for more information on using the `geolocation` function.

## `getCredential()`

The `getCredential` function retrieves secrets and variables from the RudderStack [credential store](<https://www.rudderstack.com/docs/transformations/credentials/>). Use it to avoid hardcoding sensitive data like API keys and tokens in your transformations.

> ![info](/docs/images/info.svg)
> 
> The credential store and `getCredential` are available only on the [Starter](<https://rudderstack.com/pricing/>), [Growth](<https://rudderstack.com/pricing/>), and [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plans.

### What you can do

  * Retrieve secrets (encrypted) and variables (non-encrypted) from the credential store
  * Use API keys, tokens, and configuration values securely in transformations
  * Reference credentials by name without exposing them in transformation code


### What it returns

  * Returns the credential value as a string when the key exists and is valid
  * Returns `undefined` (JavaScript) or `null` (Python) when the key does not exist or is invalid


> ![warning](/docs/images/warning.svg)
> 
> `getCredential` is a restricted keyword. Do not use it for naming functions or variables. You cannot use credentials in [transformation libraries](<https://www.rudderstack.com/docs/transformations/libraries/>). RudderStack drops the event if an error occurs while using `getCredential` in a transformation connected to a destination.

### Examples
    
    
    export function transformEvent(event, metadata) {
      try {
        event.context.url = getCredential('dev_url');
      } catch (error) {
        log(error);
      }
      return event;
    }
    
    
    
    def transformEvent(event, metadata):
        try:
            event['context']['url'] = getCredential('dev_url')
        except Exception as e:
            log(e)
        return event
    

### Usage

See [Transformation Credentials](<https://www.rudderstack.com/docs/transformations/credentials/>) for more information on using the `getCredential` function.

## `log()`

The `log` function captures output during transformation testing. Use it to inspect event data, metadata, or intermediate values when you run tests in the RudderStack dashboard.

### What you can do

  * Debug transformations by printing values to the **Logs** section
  * Inspect event properties, metadata, or computed values during development
  * Trace execution flow when troubleshooting transformation logic


### What it returns

Nothing. The function is used for its side effect of writing to the transformation logs.

> ![info](/docs/images/info.svg)
> 
> You can pass a string, number, or object as an argument to the `log` function. Logs appear in the **Logs** section when you click **Run Test** in the transformation editor.

### Examples
    
    
    export function transformEvent(event, metadata) {
      const meta = metadata(event);
      log("Event Name is", event.event, ";", "Message ID is", event.messageId);
      log("Source ID is", meta.sourceId);
      return event;
    }
    
    
    
    def transformEvent(event, metadata):
        meta = metadata(event)
        log("Event Name is", event['event'], ";", "Message ID is", event['messageId'])
        log("Source ID is", meta['sourceId'])
        return event
    

### Usage

See [Capture event information with logs](<https://www.rudderstack.com/docs/transformations/create/#capture-event-information-with-logs>) for more information on using the `log` function.

## See more

  * [Use Transformations](<https://www.rudderstack.com/docs/transformations/usage/>): Use transformations in cloud, device, and hybrid mode
  * [Transformation Credentials](<https://www.rudderstack.com/docs/transformations/credentials/>): Store and use secrets and variables
  * [Geolocation Enrichment](<https://www.rudderstack.com/docs/transformations/geolocation-enrichment/>): Enrich events with geolocation data