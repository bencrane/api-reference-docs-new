# RudderStack Go SDK

Use RudderStack’s Go SDK to send server-side events to various destinations.

* * *

  * __15 minute read

  * 


RudderStack’s Go SDK lets you track and send the events from your Go applications to the specified destinations.

See the Go SDK [GitHub codebase](<https://github.com/rudderlabs/analytics-go>) for implementation-specific details.

[![Github Badge](https://img.shields.io/github/v/release/rudderlabs/analytics-go.svg?label=GitHub)](<https://github.com/rudderlabs/analytics-go>)

## SDK setup requirements

  * Sign up for [RudderStack](<https://app.rudderstack.com/signup>).
  * [Set up a Go source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#adding-a-source>) in your dashboard. Note the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) for this source.
  * You will also need the [data plane URL](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>) associated with your RudderStack workspace.


> ![success](/docs/images/tick.svg)
> 
> The **Setup** tab in the RudderStack dashboard has the SDK installation snippet containing both the write key and the data plane URL. Use it to integrate the Go SDK into your application.

## Install Go SDK

To install the Go SDK in the `GOPATH`, run the following command:
    
    
    go get github.com/rudderlabs/analytics-go
    

## Initialize the SDK

Run the following code snippet to initialize the Go SDK:
    
    
    package main
    
    import (
        "github.com/rudderlabs/analytics-go/v4"
    )
    
    func main() {
        // Instantiates a client to use send messages to the RudderStack API.
        
        // Use your write key in the below placeholder:
        
        client := analytics.New(<WRITE_KEY>, <DATA_PLANE_URL>)
    
        // Enqueues a track event that will be sent asynchronously.
        client.Enqueue(analytics.Track{
            UserId: "1hKOmRA4GRlm",
            Event:  "Test Event",
        })
    
        // Flushes any queued messages and closes the client.
        client.Close()
    }
    

Alternatively, you can run the following snippet:
    
    
    package main
    
    import (
        "time"
        "github.com/rudderlabs/analytics-go/v4"
    )
    
    func main() {
        // Instantiates a client to use send messages to the RudderStack API.
        
        // Enter your write key in the below placeholder:
        
        client, _ := analytics.NewWithConfig(WRITE_KEY,
    		analytics.Config{
    			DataPlaneUrl: DATA_PLANE_URL,
    			Interval:     30 * time.Second,
    			BatchSize:    100,
    			Verbose:      true,
    			DisableGzip:  false,  // Set to true to disable Gzip compression.
    		})
    
        // Enqueues a track event that will be sent asynchronously.
        
        client.Enqueue(analytics.Track{
            UserId: "1hKOmRA4GRlm",
            Event:  "Test Event",
        })
    
        // Flushes any queued messages and closes the client.
        
        client.Close()
    }
    

### Migrate to SDK v4

To migrate to the Go SDK v4.1.0, set the data plane URL in `Config` (as seen in the above section) instead of passing it as an argument.

## SDK configuration options

The RudderStack Go SDK provides the following parameters which you can pass during the SDK’s initialization:

Parameter| Data type| Description  
---|---|---  
`DataPlaneUrl`| String| Your RudderStack [data plane URL](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>).  
`Interval`| Time.Duration| The SDK sends messages when this flushing interval time has elapsed or when the batch size limit is reached, whichever comes first.  
  
**Default value** : 5 seconds  
`BatchSize`| Integer| Total number of messages to be sent in a single batch.  
  
**Default value** : 250  
`MaxMessageBytes`| Integer| Maximum size (in Bytes) for a single message, configurable up to less than **4MB**. Messages exceeding this limit are dropped.  
  
**Default value** : 32768 (32KB)  
`MaxBatchBytes`| Integer| Maximum size (in Bytes) for a batch of messages, configurable up to **4MB**. Batches exceeding this limit are dropped.  
  
**Default value** : 512000 (500KB)  
`DefaultContext`| *Context| Default context object applied to all messages sent by the client.  
`Logger`| Logger interface| Custom logger implementation for SDK logging. If not specified, logs are written to `os.Stderr`.  
`Verbose`| Boolean| When set to `true`, the client sends more frequent and detailed messages to the logger.  
  
**Default value** : false  
`RetryAfter`| Function| Takes an integer (retry count) and returns `time.Duration`, allowing for dynamic backoff strategies.  
  
**Default behavior** : Exponential backoff with a maximum delay of 30 seconds  
`DisableGzip`| Boolean| Disables gzip compression of the requests.  
  
**Default value** : `false`  
`Transport`| http.RoundTripper| Custom HTTP transport for requests. The SDK uses `http.DefaultTransport` if this field is not specified.  
`Callback`| Callback interface| Callback functions to handle message success and failure events.  
  


> ![info](/docs/images/info.svg)The SDK invokes the `Callback` interface methods when messages are successfully sent or fail to be sent. Callback methods are called by the SDK’s internal goroutines and must return quickly to avoid interfering with the client’s workflow.  
  
`NoProxySupport`| Boolean| Set this variable to `true` if you **do not use** a proxy to send the events.  
  
**Default value** : `false`  
  


> ![info](/docs/images/info.svg)Setting `NoProxySupport` to `true` will avoid RudderStack making calls to the proxy for fetching the total number of nodes in case of a multi-node setup.  
  
A sample configuration with a custom logger and callback is shown below:
    
    
    type customLogger struct{}
    
    func (l customLogger) Logf(format string, args ...interface{}) {
        log.Printf("INFO: "+format, args...)
    }
    
    func (l customLogger) Errorf(format string, args ...interface{}) {
        log.Printf("ERROR: "+format, args...)
    }
    
    type customCallback struct{}
    
    func (c customCallback) Success(msg analytics.Message) {
        log.Printf("Message sent successfully: %v", msg)
    }
    
    func (c customCallback) Failure(msg analytics.Message, err error) {
        log.Printf("Message failed: %v, error: %v", msg, err)
    }
    
    client, _ := analytics.NewWithConfig(WRITE_KEY,
        analytics.Config{
            DataPlaneUrl: DATA_PLANE_URL,
            Interval:     30 * time.Second,
            BatchSize:    100,
            Verbose:      true,
            Logger:       customLogger{},
            Callback:     customCallback{},
        })
    

## Supported events

> ![warning](/docs/images/warning.svg)
> 
> **RudderStack does not store or persist the user state in any of the server-side SDKs**.  
>   
> Unlike the client-side SDKs that deal with only a single user at a given time, the server-side SDKs deal with multiple users simultaneously. Therefore, you must specify either the `userId` or `anonymousId` **every time** while making any API calls supported by the Go SDK.

### Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you identify a visiting user and associate them to their actions. It also lets you record the traits about them like their name, email address, etc.

A sample `identify` call is shown:
    
    
    client.Enqueue(analytics.Identify{
      UserId: "1hKOmRA4GRlm",
      Traits: analytics.NewTraits().
        SetName("Alex Keener").
        SetEmail("alex@example.com").
        Set("plan", "Free").
        Set("manager", 12),
    })
    

The `identify` method parameters are as described below:

Field| Data type| Description  
---|---|---  
`UserId`  
Required, if `AnonymousId` is absent.| String| Unique identifier for a user in your database.  
`AnonymousId`  
Required, if `UserId` is absent.| String| The SDK automatically sets this identifier in cases where there is no unique identifier for the user.  
`Traits`| Object| An optional dictionary of the user’s traits, like `Name` or `Email`.  
`Context`| Object| An optional dictionary of information that provides context about the event. It is not directly related to the API call.  
`Integrations`| Object| An optional dictionary containing the destinations to be enabled or disabled.  
`Timestamp`| Timestamp in ISO 8601 format| The timestamp of the event’s arrival.  
  
### Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record the user actions along with their associated properties. Each user action is called an **event**.

A sample `track` call is shown below:
    
    
    client.Enqueue(analytics.Track{
      UserId: "1hKOmRA4GRlm",
      Event:  "Signed Up",
      Properties: analytics.NewProperties().
        Set("plan", "Free"),
    })
    

The `track` method parameters are as described below:

Field| Data type| Description  
---|---|---  
`UserId`  
Required, if `AnonymousId` is absent.| String| Unique identifier for a user in your database.  
`AnonymousId`  
Required, if `UserId` is absent.| String| The SDK automatically sets this identifier in cases where there is no unique identifier for the user.  
`Event`  
Required| String| Name of the event.  
`Properties`| Object| An optional dictionary of the properties associated with the event.  
`Context`| Object| An optional dictionary of information that provides context about the event. It is not directly related to the API call.  
`Integrations`| Object| An optional dictionary containing the destinations to be enabled or disabled.  
`Timestamp`| Timestamp in ISO 8601 format| The timestamp of the event’s arrival.  
  
### Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record the page views on your application along with the other relevant information about the page.

A sample `page` call is as shown:
    
    
    client.Enqueue(analytics.Page{
      UserId: "12345",
      Name:   "Pizza",
      Properties: analytics.NewProperties().
        SetURL("https://dominos.com"),
    })
    

The `page` method parameters are as described below:

Field| Data type| Description  
---|---|---  
`UserId`  
Required, if `AnonymousId` is absent.| String| Unique identifier for a user in your database.  
`AnonymousId`  
Required, if `UserId` is absent.| String| The SDK automatically sets this identifier in cases where there is no unique identifier for the user.  
`Name`  
Required| String| Name of the viewed page.  
`Properties`| Object| An optional dictionary of the properties associated with the viewed page, like `URL` or `Referrer`.  
`Context`| Object| An optional dictionary of information that provides context about the event. It is not directly related to the API call.  
`Integrations`| Object| An optional dictionary containing the destinations to be enabled or disabled.  
`Timestamp`| Timestamp in ISO 8601 format| The timestamp of the event’s arrival.  
  
### Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call is the mobile equivalent of the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call. It lets you record the screen views on your mobile app along with other relevant information about the screen.

A sample `screen` call is as shown:
    
    
    client.Enqueue(analytics.Screen{
      UserId: "1hKOmRA4GRlm",
      Name:   "Pizza",
      Properties: analytics.NewProperties().
        SetURL("https://dominos.com"),
    })
    

The `screen` method parameters are as described below:

Field| Data type| Description  
---|---|---  
`UserId`  
Required, if `AnonymousId` is absent.| String| Unique identifier for a user in your database.  
`AnonymousId`  
Required, if `UserId` is absent.| String| The SDK automatically sets this identifier in cases where there is no unique identifier for the user.  
`Name`  
Required| String| Name of the viewed screen.  
`Properties`| Object| An optional dictionary of the properties associated with the viewed screen, like `URL` or `Referrer`.  
`Context`| Object| An optional dictionary of information that provides context about the event. It is not directly related to the API call.  
`Integrations`| Object| An optional dictionary containing the destinations to be enabled or disabled.  
`Timestamp`| Timestamp in ISO 8601 format| The timestamp of the event’s arrival.  
  
### Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call lets you link an identified user with a group, such as a company, organization, or an account. It also lets you record any custom traits or properties associated with that group.

A sample `group` call made using the Go SDK is shown below:
    
    
    client.Enqueue(analytics.Group{
      UserId:  "1hKOmRA4GRlm",
      GroupId: "1",
      Traits: map[string]interface{}{
        "name": "Company",
        "description": "Facebook",
      },
    })
    

The `group` method parameters are as follows:

Field| Data type| Description  
---|---|---  
`UserId`  
Required, if `AnonymousId` is absent.| String| Unique identifier for a user in your database.  
`AnonymousId`  
Required, if `UserId` is absent.| String| The SDK automatically sets this identifier in cases where there is no unique identifier for the user.  
`GroupId`  
Required| String| Unique identifier of the group in your database.  
`Traits`| Object| An optional dictionary of the group’s traits like `Name` or `Email`.  
`Context`| Object| An optional dictionary of information that provides context about the event. It is not directly related to the API call.  
`Integrations`| Object| An optional dictionary containing the destinations to be enabled or disabled.  
`Timestamp`| Timestamp in ISO 8601 format| The timestamp of the event’s arrival.  
  
### Alias

The [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) call lets you merge different identities of a known user. It is an advanced method that lets you change the tracked user’s ID explicitly. You can use `alias` for managing the user’s identity in some of the downstream destinations.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack supports sending `alias` events only to select downstream destinations. See the [destination-specific documentation](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) for more details.

A sample `alias` call is as shown:
    
    
    client.Enqueue(analytics.Alias{
      PreviousId: "12345",
      UserId:     "1hKOmRA4GRlm",
    })
    

The `alias` method parameters are as mentioned below:

Field| Data type| Description  
---|---|---  
`UserId`  
Required, if `AnonymousId` is absent.| String| Unique identifier for a user in your database.  
`AnonymousId`  
Required, if `UserId` is absent.| String| The SDK automatically sets this identifier in cases where there is no unique identifier for the user.  
`PreviousId`  
Required| String| The previous unique identifier of the user.  
`Context`| Object| An optional dictionary of information that provides context about the event. It is not directly related to the API call.  
`Integrations`| Object| An optional dictionary containing the destinations to be enabled or disabled.  
`Timestamp`| Timestamp in ISO 8601 format| The timestamp of the event’s arrival.  
  
## Context and traits

The `Context` object supports sending [standard contextual properties](<https://github.com/rudderlabs/analytics-go/blob/fa84ac94e566e22ba2a8f771b4bf6b3c09c5ce68/context.go#L11-L34>) along with the `Extra` object to add any custom properties.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * All event APIs support sending contextual data through the `Context` field.
>   * The custom properties sent through the `Extra` field appear directly in root level of the context object of the event payload.
> 


The `Traits` object lets you include user attributes that provide additional context about the user.

A sample `track` event containing the above fields is shown below:
    
    
    client.Enqueue(analytics.Track{
      UserId: "1hKOmRA4GRlm",
      Event:  "Button Clicked",
      Properties: analytics.NewProperties().
        Set("button_name", "signup_cta").
        Set("button_location", "header").
        Set("page_section", "hero").
        Set("value", 29.99),
      Context: &analytics.Context{
        Traits: analytics.Traits{
          "subscription_level": "premium",
          "age":                30,
        },
        Extra: map[string]interface{}{
          "customField":   "customValue",
          "experimentId":  12345,
        },
      },
    })
    

The corresponding event payload looks when you include these contextual properties is shown below:
    
    
    {
        "anonymousId": "anon_67890",
        "channel": "server",
        "context": {
            "app": {
                "build": "100",
                "name": "MyApp",
                "namespace": "com.mycompany.myapp",
                "version": "1.0.0"
            },
            "library": {
                "name": "analytics-go",
                "version": "4.2.2"
            },
            "traits": {
                // User attributes from Context.Traits
                "age": 30,
                "subscription_level": "premium"
            },
            // Custom properties from Context.Extra
            "customField": "customValue",
            "experimentId": 12345
        },
        "event": "Button Clicked",
        "integrations": {
            "All": true,
            "Google Analytics": false
        },
        "messageId": "68c19e6e-3a9d-4546-97c0-75180bfbdadf",
        "originalTimestamp": "2025-10-13T21:02:23.06924+05:30",
        "properties": {
            // Event-specific properties
            "button_location": "header",
            "button_name": "signup_cta",
            "page_section": "hero",
            "value": 29.99
        },
        "receivedAt": "2025-10-13T15:32:25.953026288Z",
        "request_ip": "106.51.149.173",
        "rudderId": "ac59e9bd-5503-42e7-9054-8bfb3fd08d67",
        "sentAt": "2025-10-13T21:02:25.070593+05:30",
        "type": "track",
        "userId": "1hKOmRA4GRlm"
    }
    

## Gzip requests

> ![info](/docs/images/info.svg)
> 
> The Go SDK supports the Gzip compression feature from v4.1.0 and above.

The Go SDK automatically gzips requests. However, you can disable this by setting the `DisableGzip` parameter to `true` while initializing the SDK:
    
    
    client, _ := analytics.NewWithConfig(WRITE_KEY,
    		analytics.Config{
    			DataPlaneUrl: DATA_PLANE_URL,
    			Interval:     30 * time.Second,
    			BatchSize:    100,
    			Verbose:      true,
    			DisableGzip: true
    		})
    

> ![warning](/docs/images/warning.svg)
> 
> The `DisableGzip` parameter requires [rudder-server](<https://github.com/rudderlabs/rudder-server>) **version 1.4 or higher**. Otherwise, your events might fail.

## Flush events

The Go SDK automatically flushes events when either:

  * The configured `Interval` time has elapsed
  * The batch reaches the configured `BatchSize` limit
  * The batch size reaches the `MaxBatchBytes` limit (default: 500KB, configurable up to 4MB)


The `Close()` method flushes all queued events synchronously before closing the client. Note that this method is a blocking call that waits until all queued messages are sent and the client is fully shut down.

> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Call the `Close()` method in the following scenarios:
> 
>   * In short-lived scripts that exit immediately after sending events
>   * Before shutting down a worker or process, or during graceful shutdown
>   * Before deployments where the process is terminated
> 


An example of using the `Close()` method is shown below:
    
    
    client.Enqueue(analytics.Track{
        UserId: "1hKOmRA4GRlm",
        Event:  "Job Finished",
    })
    client.Close()  // Blocks until all queued events are sent
    

An example of using the `Close()` method during a graceful shutdown is shown below:
    
    
    defer func() {
        client.Close()
    }()
    

#### Flushing behavior

The Go SDK flushes events based on time intervals and batch size limits:

  * Events are flushed when the `Interval` timer triggers (**default** : 5 seconds)
  * Events are flushed immediately when the batch reaches `BatchSize` messages (**default** : 250)
  * Events are flushed immediately when the batch size reaches `MaxBatchBytes` (**default** : 500KB, configurable up to 4MB)


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** If your workloads are sending a large number of events at a time:
> 
>   * Increase the `BatchSize` value so the SDK can send more events per request
>   * Adjust the `Interval` to balance between latency and batch efficiency
>   * Always call the `Close()` method during graceful shutdown to ensure the queue is drained
> 


## Troubleshooting

This section provides solutions to common issues encountered while using the Go SDK.

### Events not sent

If events sent via the Go SDK are not appearing in your destinations:

  * Verify that your write key and data plane URL are correct
  * Call the `Close()` method to ensure events are sent for scripts that exit immediately:


    
    
    client.Close()
    

  * Check if messages are being dropped due to size limits. Messages larger than `MaxMessageBytes` (**default** : 32KB, configurable up to less than 4MB) are dropped
  * Track any errors using a custom callback:


    
    
    type errorCallback struct{}
    
    func (c errorCallback) Success(msg analytics.Message) {
        // Handle successful messages
    }
    
    func (c errorCallback) Failure(msg analytics.Message, err error) {
        log.Printf("Message failed: %v, error: %v", msg, err)
    }
    
    client, _ := analytics.NewWithConfig(WRITE_KEY,
        analytics.Config{
            DataPlaneUrl: DATA_PLANE_URL,
            Callback:     errorCallback{},
        })
    

### Common errors

Error| Solution  
---|---  
`analytics.NewWithConfig: negative time intervals are not supported`| Ensure `Interval` is not negative  
`analytics.NewWithConfig: negative batch sizes are not supported`| Ensure `BatchSize` is not negative  
`analytics.Track.Event: invalid field value`| Provide an `Event` parameter to the `Track` method  
`analytics.Track.UserId: invalid field value`| Provide at least one identifier (`UserId` or `AnonymousId`) for each event  
`the client was already closed`| Do not call `Enqueue()` after calling `Close()`  
`the message exceeds the maximum allowed size`| Reduce the size of your message to be under the `MaxMessageBytes` limit (default: 32KB, configurable up to less than 4MB)  
  
### Performance issues

If you are encountering performance issues when using the Go SDK in high-volume applications:

  * Increase the batch size by setting the `BatchSize` parameter to a higher value during initialization:


    
    
    BatchSize: 500
    

  * Adjust the flush interval by setting the `Interval` parameter:


    
    
    Interval: 10 * time.Second
    

  * Increase the maximum batch bytes if you have large messages (configurable up to 4MB):


    
    
    MaxBatchBytes: 1024000  // 1 MB
    

## Examples

This section provides examples of how to use the Go SDK for some common use cases.

The following example tracks the user’s shopping behavior from browsing to purchase:
    
    
    // Product Viewed
    client.Enqueue(analytics.Track{
        UserId: "1hKOmRA4GRlm",
        Event:  "Product Viewed",
        Properties: analytics.NewProperties().
            SetProductId("SKU-123").
            SetSKU("SKU-123").
            SetName("Go SDK Guide").
            SetPrice(29.99).
            SetCurrency("USD").
            SetCategory("Books"),
    })
    
    // Product Added to Cart
    client.Enqueue(analytics.Track{
        UserId: "1hKOmRA4GRlm",
        Event:  "Product Added",
        Properties: analytics.NewProperties().
            SetProductId("SKU-123").
            Set("cart_id", "CART-789"),
    })
    
    // Order Completed
    client.Enqueue(analytics.Track{
        UserId: "1hKOmRA4GRlm",
        Event:  "Order Completed",
        Properties: analytics.NewProperties().
            SetOrderId("ORD-456").
            SetTotal(35.98).
            SetRevenue(35.98).
            SetCurrency("USD").
            SetProducts(
                analytics.Product{
                    ID:    "SKU-123",
                    SKU:   "SKU-123",
                    Price: 29.99,
                },
            ),
    })
    
    client.Close()
    

The following example tracks the complete user journey:
    
    
    // New user signup
    client.Enqueue(analytics.Identify{
        UserId: "1hKOmRA4GRlm",
        Traits: analytics.NewTraits().
            SetEmail("newuser@example.com").
            SetName("John Doe").
            SetCreatedAt(time.Now()).
            Set("signup_source", "website"),
    })
    
    // Track activation event
    client.Enqueue(analytics.Track{
        UserId: "1hKOmRA4GRlm",
        Event:  "User Activated",
        Properties: analytics.NewProperties().
            Set("plan", "free").
            Set("feature", "project_creation"),
    })
    
    // Upgrade to paid plan
    client.Enqueue(analytics.Track{
        UserId: "1hKOmRA4GRlm",
        Event:  "Subscription Upgraded",
        Properties: analytics.NewProperties().
            Set("previous_plan", "free").
            Set("new_plan", "pro").
            SetRevenue(49.99).
            SetCurrency("USD"),
    })
    
    client.Close()
    

The following example tracks organization-level events and user-to-organization relationships:
    
    
    // Create organization context
    client.Enqueue(analytics.Group{
        UserId:  "1hKOmRA4GRlm",
        GroupId: "org_456",
        Traits: analytics.NewTraits().
            SetName("Tech Startup Inc").
            Set("plan", "enterprise").
            Set("industry", "SaaS").
            Set("employees", 150),
    })
    
    // Track organization-level events
    client.Enqueue(analytics.Track{
        UserId: "1hKOmRA4GRlm",
        Event:  "Feature Used",
        Properties: analytics.NewProperties().
            Set("feature_name", "Advanced Analytics").
            Set("workspace", "org_456"),
        Context: &analytics.Context{
            Extra: map[string]interface{}{
                "group_id": "org_456",
            },
        },
    })
    
    client.Close()
    

## FAQ

#### How does the Go SDK handle events larger than 32KB?

The Go SDK drops any events greater than the `MaxMessageBytes` limit (**default** : 32KB).

To avoid data loss, ensure your events are within this size limit. You can customize this limit by setting `MaxMessageBytes` during initialization, up to less than 4MB. However, it is not recommended to exceed 4MB as the server will reject larger messages.

#### Does the Go SDK support event ordering?

The Go SDK does not support event ordering by default. Events are processed asynchronously in batches for better performance.

#### What happens if the data plane URL is unreachable?

If the data plane URL is unreachable, the SDK will:

  1. Retry sending the events based on the `RetryAfter` configuration. By default, it is set to **exponential backoff** with up to **10** retry attempts and a maximum delay of **30 seconds**
  2. Buffer events up to the configured `BatchSize` and `MaxBatchBytes` limits
  3. Drop events if they exceed the `MaxMessageBytes` limit (**default** : 32KB) or if retries are exhausted


#### How does the Go SDK handle retries?

The Go SDK retries failed requests up to 10 times by default using an exponential backoff strategy. The backoff delay is calculated by the `RetryAfter` function, which defaults to exponential backoff with a maximum delay of 30 seconds. You can customize this behavior by providing a custom `RetryAfter` function during initialization.

## See more

  * [Go SDK codebase](<https://github.com/rudderlabs/analytics-go>): Source code and issues
  * [RudderStack Event Specification](<https://www.rudderstack.com/docs/event-spec/standard-events/>): Learn about the RudderStack event schemas and properties
  * [Community Slack](<https://rudderstack.com/join-rudderstack-slack-community>): Get help from the community