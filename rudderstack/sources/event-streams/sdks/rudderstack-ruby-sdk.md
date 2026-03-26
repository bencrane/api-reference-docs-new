# RudderStack Ruby SDK

Use RudderStack’s Ruby SDK to send server-side events from your Ruby applications to various destinations asynchronously.

* * *

  * __14 minute read

  * 


RudderStack’s Ruby SDK lets you track and send the events from your Ruby applications to the specified destinations asynchronously. This way, you can use the SDK to improve the performance of your application by reducing the time taken to send the data.

> ![warning](/docs/images/warning.svg)
> 
> This guide covers the recommended asynchronous Ruby SDK.
> 
> See this [documentation](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ruby-sdk-sync/>) for the synchronous version, which exists for legacy purposes but will be deprecated soon.

Refer to the SDK’s [GitHub codebase](<https://github.com/rudderlabs/rudder-sdk-ruby>) for the implementation-specific details.

[![Github Badge](https://img.shields.io/gem/v/rudder-sdk-ruby?style=flat)](<https://rubygems.org/gems/rudder-sdk-ruby>)

## SDK setup requirements

  * Install Ruby v2.0 or later on your system.
  * Sign up for [RudderStack](<https://app.rudderstack.com/signup>).
  * [Set up a Ruby source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#adding-a-source>) in the dashboard. Note the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) for this source.
  * You will also need the [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) associated with your RudderStack workspace.


> ![success](/docs/images/tick.svg)
> 
> The **Setup** tab in the RudderStack dashboard has the SDK installation snippet containing both the write key and the data plane URL. Use it to integrate the Ruby SDK into your application.

## Install Ruby SDK

  1. Add the following line to your application’s Gem file:


    
    
    gem 'rudder-sdk-ruby'
    

  2. Run `bundle install` to install the gem.


## Initialize the SDK

To initialize the SDK, create a client instance as shown below:
    
    
    require 'rudder-sdk-ruby'
    
    analytics = Rudder::Analytics.new(
      write_key: 'WRITE_KEY',
      data_plane_url: 'DATA_PLANE_URL',
      gzip: true
    )
    

Replace the `WRITE_KEY` and `DATA_PLANE_URL` values in the above snippet with the actual values obtained above.

## SDK configuration options

You can customize Ruby SDK’s behavior by passing the following options during initialization:

Field| Data type| Description  
---|---|---  
`write_key`  
Required| String| Your Ruby source write key.  
`data_plane_url`  
Required| String| Your data plane URL.  
`gzip`| Boolean| Enables Gzip compression for event requests.  
  
**Default value** : `true`  
`ssl`| Boolean| Uses SSL/TLS for requests.  
  
**Default value** : `true`  
`batch_size`| Integer| Defines the maximum number of events per batch.  
  
**Default value** : `100`  
`max_queue_size`| Integer| Defines the maximum queue size before dropping events.  
  
**Default value** : `10000`  
`retries`| Integer| Defines the number of retry attempts for failed requests.  
  
**Default value** : `10`  
`stub`| Boolean| Enables stub mode for testing.  
  
**Default value** : `false`  
`test`| Boolean| Enables test mode to capture events locally.  
  
**Default value** : `nil`  
`on_error`| Proc| Error handler callback.  
  
**Default value** : `proc {  
`on_error_with_messages`| Proc| Error handler with failed messages.  
  
**Default value** : `proc {  
`backoff_policy`| Object| Defines a custom backoff policy for retry attempts.  
  
**Default behavior** : Exponential backoff  
  
> ![info](/docs/images/info.svg)
> 
> The SDK invokes both the `on_error` and `on_error_with_messages` callback functions when events cannot be processed or delivered.
> 
> Any logging you implement inside these callbacks will not replace the default logging behavior — your custom logs will be in addition to the default logs.

A sample configuration is shown below:
    
    
    analytics = Rudder::Analytics.new(
      write_key: 'WRITE_KEY',
      data_plane_url: 'DATA_PLANE_URL',
      gzip: true,
      batch_size: 50,
      max_queue_size: 5000,
      retries: 5,
      on_error: proc { |status, error|
        # Log errors
        puts "Error: #{status} - #{error}"
      },
      on_error_with_messages: proc { |status, error, messages|
        # Handle failed messages
        messages.each do |msg|
          # Retry or persist messages
          puts "Failed: #{msg}"
        end
      }
    )
    

## Send events

> ![warning](/docs/images/warning.svg)
> 
> **RudderStack does not store or persist the user state in any of the server-side SDKs**.  
>   
> Unlike the client-side SDKs that deal with only a single user at a given time, the server-side SDKs deal with multiple users simultaneously. Therefore, you must specify either the `user_id` or `anonymous_id` **every time** while making any API calls supported by the Ruby SDK.

### Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you identify a visiting user and associate them to their actions. It also lets you record the traits about them like their name, email address, etc.

A sample `identify` call made using the Ruby SDK is shown below:
    
    
    analytics.identify(
      user_id: '1hKOmRA4GRlm',
      traits: {
        email: "alex@example.com",
        createdAt: "2023-07-24T00:00:00Z",
        subscribe: true
      },
      context: { ip: '10.81.20.10' }
    )
    

The `identify` method parameters are as shown:

Field| Data type| Description  
---|---|---  
`user_id`  
Required, if **anonymous_id** is absent.| String| Unique identifier for the user in your database.  
`anonymous_id`  
Required, if **user_id** is absent.| String| Use this field to set an identifier when there is no unique user identifier available.  
`traits`| Object| Optional dictionary of user traits, like `name`, `email`, etc.  
`context`| Object| Optional dictionary of contextual information for the event. It is not directly related to the API call.  
`integrations`| Object| Optional dictionary containing the destinations to be either enabled or disabled.  
`timestamp`| Timestamp| The event’s timestamp.  
  
**Note** : If not provided, it defaults to the current time when the message is created. The SDK automatically converts it in the ISO 8601 format before sending to RudderStack.  
  
### Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record user actions along with their associated properties.

A sample `track` call made using the Ruby SDK is shown below:
    
    
    analytics.track(
      user_id: '1hKOmRA4GRlm',
      event: 'Product Shipped',
      properties: {
        product_id: 'SKU-123',
        product_name: 'Ruby Complete Reference',
        price: 29.99,
        currency: 'USD',
        category: 'Books'
      }
    )
    

The `track` method parameters are as described below:

Field| Data type| Description  
---|---|---  
`user_id`  
Required, if **anonymous_id** is absent.| String| Unique identifier for the user in your database.  
`anonymous_id`  
Required, if **user_id** is absent.| String| Use this field to set an identifier when there is no unique user identifier available.  
`event`  
Required| String| Name of the event.  
`properties`| Object| Optional dictionary of the properties associated with the event.  
`context`| Object| Optional dictionary of contextual information for the event. It is not directly related to the API call.  
`integrations`| Object| Optional dictionary containing the destinations to be either enabled or disabled.  
`timestamp`| Timestamp| The event’s timestamp.  
  
**Note** : If not provided, it defaults to the current time when the message is created. The SDK automatically converts it in the ISO 8601 format before sending to RudderStack.  
  
### Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record page views on your application along with the other relevant information about the page.

A sample `page` call made using the Ruby SDK is shown below:
    
    
    analytics.page(
      user_id: '1hKOmRA4GRlm',
      category: 'Food',
      name: 'Pizza',
      properties: {
        URL: 'https://website.com'
      }
    )
    

The `page` method parameters are as described below:

Field| Data type| Description  
---|---|---  
`user_id`  
Required, if **anonymous_id** is absent.| String| Unique identifier for the user in your database.  
`anonymous_id`  
Required, if **user_id** is absent.| String| Use this field to set an identifier when there is no unique user identifier available.  
`name`| String| Name of the viewed page.  
`properties`| Object| Optional dictionary of the properties associated with the viewed page, like `url`, `referrer`, etc.  
`context`| Object| Optional dictionary of contextual information for the event. It is not directly related to the API call.  
`integrations`| Object| Optional dictionary containing the destinations to be either enabled or disabled.  
`timestamp`| Timestamp| The event’s timestamp.  
  
**Note** : If not provided, it defaults to the current time when the message is created. The SDK automatically converts it in the ISO 8601 format before sending to RudderStack.  
  
### Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call is the mobile equivalent of the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call. It lets you record the screen views on your mobile app along with other relevant information about the screen.

A sample `screen` call is as shown:
    
    
    analytics.screen(
      user_id: '1hKOmRA4GRlm',
      category: 'Food',
      name: 'Pizza',
      properties: {
        URL: 'https://website.com'
      }
    )
    

The `screen` method parameters are as described below:

Field| Data type| Description  
---|---|---  
`user_id`  
Required, if **anonymous_id** is absent.| String| Unique identifier for the user in your database.  
`anonymous_id`  
Required, if **user_id** is absent.| String| Use this field to set an identifier when there is no unique user identifier available.  
`name`  
Required| String| Name of the viewed screen.  
`category`| String| The screen’s category.  
`properties`| Object| Optional dictionary of the properties associated with the viewed screen.  
`integrations`| Object| Optional dictionary containing the destinations to be either enabled or disabled.  
`context`| Object| Optional dictionary of contextual information for the event. It is not directly related to the API call.  
`timestamp`| Timestamp| The event’s timestamp.  
  
**Note** : If not provided, it defaults to the current time when the message is created. The SDK automatically converts it in the ISO 8601 format before sending to RudderStack.  
  
### Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call lets you link an identified user with a group, like a company, organization, or an account. It also lets you record any custom traits or properties associated with that group.

A sample `group` call made using the Ruby SDK is shown below:
    
    
    analytics.group(
      user_id: '1hKOmRA4GRlm',
      group_id: '12',
      traits: {
        name: 'Company',
        description: 'Software'
      }
    )
    

The `group` method parameters are as follows:

Field| Data type| Description  
---|---|---  
`user_id`  
Required, if **anonymous_id** is absent.| String| Unique identifier for the user in your database.  
`anonymous_id`  
Required, if **user_id** is absent.| String| Use this field to set an identifier when there is no unique user identifier available.  
`group_id`  
Required| String| Unique identifier of the group in your database.  
`traits`| Object| Optional dictionary of the group’s traits like `name`, `email`, etc.  
`integrations`| Object| Optional dictionary containing the destinations to be either enabled or disabled.  
`context`| Object| Optional dictionary of contextual information for the event. It is not directly related to the API call.  
`timestamp`| Timestamp| The event’s timestamp.  
  
**Note** : If not provided, it defaults to the current time when the message is created. The SDK automatically converts it in the ISO 8601 format before sending to RudderStack.  
  
### Alias

The [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) call lets you merge different identities of a known user. It is an advanced method that lets you change the tracked user’s ID explicitly. You can use `alias` for managing the user’s identity in some of the downstream destinations.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack supports sending `alias` events only to some downstream destinations.
> 
> See the [destination-specific documentation](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) for more information.

A sample `alias` call made using the Ruby SDK is shown below:
    
    
    analytics.alias(
      previous_id: '1hKOmRA4GRlm',
      user_id: '12345'
    )
    

The `alias` method parameters are as mentioned below:

Field| Data type| Description  
---|---|---  
`user_id`  
Required, if **anonymous_id** is absent.| String| Unique identifier for the user in your database.  
`anonymous_id`  
Required, if **user_id** is absent.| String| Use this field to set an identifier when there is no unique user identifier available.  
`previous_id`  
Required| String| The previous unique identifier of the user.  
`traits`| Object| Optional dictionary of the user’s traits like `name`, `email`, etc.  
`integrations`| Object| Optional dictionary containing the destinations to be either enabled or disabled.  
`context`| Object| Optional dictionary of contextual information for the event. It is not directly related to the API call.  
`timestamp`| Timestamp| The event’s timestamp.  
  
**Note** : If not provided, it defaults to the current time when the message is created. The SDK automatically converts it in the ISO 8601 format before sending to RudderStack.  
  
## Test and stub modes

Use the SDK’s `test` mode to capture events locally without sending them to RudderStack:
    
    
    analytics = Rudder::Analytics.new(
      write_key: 'WRITE_KEY',
      data_plane_url: 'DATA_PLANE_URL',
      test: true
    )
    
    analytics.track(
      user_id: '1hKOmRA4GRlm',
      event: 'Test Event',
      properties: { test: true }
    )
    
    # Access ALL captured events
    analytics.test_queue.all.each do |msg|
      puts msg.inspect
    end
    

#### Stub mode

Use the SDK’s `stub` mode to prevent actual network requests to RudderStack during testing:
    
    
    analytics = Rudder::Analytics.new(
      write_key: 'WRITE_KEY',
      data_plane_url: 'DATA_PLANE_URL',
      stub: true
    )
    
    analytics.flush
    

## Gzip requests

> ![info](/docs/images/info.svg)
> 
> The Gzip feature is enabled by default in the Ruby SDK.

The Ruby SDK automatically gzips requests. However, you can disable this feature by setting the `Gzip` parameter to `false` while initializing the SDK:
    
    
    analytics = Rudder::Analytics.new(
      write_key: 'WRITE_KEY', # required
      data_plane_url: 'DATA_PLANE_URL',
      gzip: false  # Set to true to enable Gzip compression
    )
    

> ![warning](/docs/images/warning.svg)
> 
> Gzip requires [rudder-server](<https://github.com/rudderlabs/rudder-server>) **v1.4 or higher**. Otherwise, your events might fail.

## Queue management

The Ruby SDK uses an in-memory queue to buffer events before sending. If the queue becomes full, events are dropped to prevent memory issues.
    
    
    analytics = Rudder::Analytics.new(
      write_key: 'WRITE_KEY',
      data_plane_url: 'DATA_PLANE_URL',
      max_queue_size: 10000  # Increase for high-volume applications
    )
    

Monitor queue size using:
    
    
    analytics.queued_messages  # Returns number of queued messages
    

## Flush events

Use `flush` to synchronously send all queued events to RudderStack.

> ![info](/docs/images/info.svg)
> 
> The `flush` method is a blocking call that waits until the internal queue is drained.

You can use the `flush` method in the following scenarios:

  * In short‑lived scripts that exit immediately after sending events
  * Before shutting down a worker/process, or during graceful shutdown
  * Before deployments where the process is terminated


An example of using the `flush` method is shown below:
    
    
    analytics.track(user_id: '1hKOmRA4GRlm', event: 'Job Finished')
    analytics.flush  # Blocks until all queued events are sent
    

An example of using the `flush` method during a graceful shutdown is shown below:
    
    
    at_exit do
      analytics.flush
    end
    

> ![info](/docs/images/info.svg)
> 
> Combine with `retries` and `on_error` handlers to observe delivery issues.

#### Flushing behavior

The Ruby SDK does not flush on fixed time intervals. Events are flushed automatically when either the batch reaches the configured `batch_size`, or the overall request size reaches **500 KB** , whichever is earlier.

Note that:

  * The number of events per flush is configurable by the `batch_size` parameter (**Default value** : 100)
  * The `flush` API call is synchronous and waits until the queue is completely emptied.


> ![info](/docs/images/info.svg)
> 
> **High volume guidance**
> 
> If your workloads are sending a large number of events at a time:
> 
>   * Increase the `batch_size` value so the SDK can send more events per request.
>   * Increase the `max_queue_size` value substantially to provide headroom while the worker drains the queue. For very large bursts, for example, 100k+, size the queue at least 100× the burst to allow producers to continue enqueueing while consumers flush.
>   * Always call the `flush` API call during graceful shutdown to ensure the queue is drained.
> 


## Customize retry behavior

By default, the Ruby SDK retries failed requests with an exponential backoff policy — this helps during temporary network issues or server problems.

For most use cases, the default behavior is suitable. However, you can customize it by passing a custom backoff policy during initialization, as shown:
    
    
    # Define a custom backoff policy
    custom_backoff = Rudder::Analytics::BackoffPolicy.new(
      min_timeout_ms: 200,        # Minimum wait time (milliseconds)
      max_timeout_ms: 20000,      # Maximum wait time (milliseconds)
      multiplier: 2.0,            # How much to multiply wait time per retry
      randomization_factor: 0.3   # Amount of randomness (0.0 to 1.0)
    )
    
    # Initialize the SDK with the custom backoff policy
    analytics = Rudder::Analytics.new(
      write_key: 'WRITE_KEY',
      data_plane_url: 'DATA_PLANE_URL',
      backoff_policy: custom_backoff,
      retries: 5  # Number of retry attempts (default: 10)
    )
    

The following are the parameters you can configure:

Parameter| Data type| Description  
---|---|---  
`min_timeout_ms`| Integer| Minimum wait time between retry attempts.  
  
**Default value** : 100 ms  
`max_timeout_ms`| Integer| Maximum wait time between retry attempts.  
  
**Default value** : 10000 ms  
`multiplier`| Float| Multiplier applied to wait time for each retry attempt.  
  
**Default value** : 1.5  
`randomization_factor`| Float| Randomness variation (`0` to `1.0`) added to prevent retry synchronization.  
  
**Default value** : 0.5  
  
> ![info](/docs/images/info.svg)
> 
> **When to use a custom backoff policy**
> 
> Consider customizing the backoff policy only if:
> 
>   * You have strict latency requirements and want faster retries
>   * You experience frequent rate limiting and need longer delays
>   * You need to fine-tune retry behavior for your specific infrastructure
> 


## Troubleshooting

This section provides solutions to common issues encountered while using the Ruby SDK.

### Events not sent

If events sent via the Ruby SDK are not appearing in your destinations:

  * Verify that your write key and data plane URL are correct.
  * Call the `flush` API to ensure events are sent for scripts that exit immediately:


    
    
    analytics.flush
    

  * Check if the queue is full:


    
    
    puts "Queued messages: #{analytics.queued_messages}"
    

  * Track any errors using an error handler:


    
    
    analytics = Rudder::Analytics.new(
      write_key: 'WRITE_KEY',
      data_plane_url: 'DATA_PLANE_URL',
      on_error: proc { |status, error, exception, response|
        puts "Error occurred: #{status} - #{error}"
        puts "Exception: #{exception}" if exception
      }
    )
    

### Common errors

Error| Solution  
---|---  
Missing required option :write_key| Provide a valid write key during initialization.  
Missing required option :data_plane_url| Provide a valid data plane URL during initialization.  
Must supply either user_id or anonymous_id| Provide at least one identifier for each event.  
Event must be given| Provide an `event` parameter to the `track` method.  
  
### Performance issues

If you are encountering performance issues when using the Ruby SDK in high-volume applications:

  * Increase the queue size by setting the `max_queue_size` parameter to a higher value during initialization.


    
    
    max_queue_size: 20000
    

  * Adjust the batch size by setting the `batch_size` parameter to a higher value during initialization.


    
    
    batch_size: 200
    

## Examples

This section provides examples of how to use the Ruby SDK for some common use cases.

The following example tracks the user’s shopping behavior from browsing to purchase:
    
    
    # Product Viewed
    analytics.track(
      user_id: '1hKOmRA4GRlm',
      event: 'Product Viewed',
      properties: {
        product_id: 'SKU-123',
        sku: 'SKU-123',
        name: 'Ruby SDK Guide',
        price: 29.99,
        currency: 'USD',
        category: 'Books'
      }
    )
    
    # Product Added to Cart
    analytics.track(
      user_id: '1hKOmRA4GRlm',
      event: 'Product Added',
      properties: {
        product_id: 'SKU-123',
        cart_id: 'CART-789'
      }
    )
    
    # Order Completed
    analytics.track(
      user_id: '1hKOmRA4GRlm',
      event: 'Order Completed',
      properties: {
        order_id: 'ORD-456',
        total: 35.98,
        revenue: 35.98,
        currency: 'USD',
        products: [
          {
            product_id: 'SKU-123',
            quantity: 1,
            price: 29.99
          }
        ]
      }
    )
    
    analytics.flush
    

The following example tracks the complete user journey:
    
    
    # New user signup
    analytics.identify(
      user_id: '1hKOmRA4GRlm',
      traits: {
        email: 'newuser@example.com',
        name: 'John Doe',
        created_at: Time.now,
        signup_source: 'website'
      }
    )
    
    # Track activation event
    analytics.track(
      user_id: '1hKOmRA4GRlm',
      event: 'User Activated',
      properties: {
        plan: 'free',
        feature: 'project_creation'
      }
    )
    
    # Upgrade to paid plan
    analytics.track(
      user_id: '1hKOmRA4GRlm',
      event: 'Subscription Upgraded',
      properties: {
        previous_plan: 'free',
        new_plan: 'pro',
        revenue: 49.99,
        currency: 'USD'
      }
    )
    
    analytics.flush
    

The following example tracks organization-level events and user-to-organization relationships:
    
    
    # Create organization context
    analytics.group(
      user_id: '1hKOmRA4GRlm',
      group_id: 'org_456',
      traits: {
        name: 'Tech Startup Inc',
        plan: 'enterprise',
        industry: 'SaaS',
        employees: 150
      }
    )
    
    # Track organization-level events
    analytics.track(
      user_id: '1hKOmRA4GRlm',
      event: 'Feature Used',
      properties: {
        feature_name: 'Advanced Analytics',
        workspace: 'org_456'
      },
      context: {
        group_id: 'org_456'
      }
    )
    
    analytics.flush
    

## FAQ

#### How does the Ruby SDK handle events larger than 32KB?

The Ruby SDK drops any events greater than 32KB.

#### Does the Ruby SDK support event ordering?

The Ruby SDK does not support event ordering by default.

## See more

  * [Ruby SDK codebase](<https://github.com/rudderlabs/rudder-sdk-ruby>): Source code and issues
  * [RudderStack Event Specification](<https://www.rudderstack.com/docs/event-spec/standard-events/>): Learn about the RudderStack event schemas and properties
  * [Community Slack](<https://rudderstack.com/join-rudderstack-slack-community>): Get help from the community