# RudderStack Java SDK Reference

Complete Java SDK API reference for tracking and sending server-side events from your Java applications.

* * *

  * __10 minute read

  * 


RudderStack’s **Java SDK** provides a comprehensive API for tracking and sending events from your Java applications to various destinations.

For implementation examples and source code, see the SDK’s [GitHub repository](<https://github.com/rudderlabs/rudder-sdk-java>).

[![](https://img.shields.io/maven-metadata/v.svg?label=Maven%20Central&metadataUrl=https://repo1.maven.org/maven2/com/rudderstack/sdk/java/analytics/analytics-parent/maven-metadata.xml)](<https://search.maven.org/search?q=g:com.rudderstack.sdk.java.analytics>)

## Prerequisites

  * A Java source [set up in the RudderStack dashboard](<https://www.rudderstack.com/docs/dashboard-guides/sources/#add-a-source>)
  * The [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) for your Java source — you can find it the **Setup** tab of the source
  * The [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) associated with your RudderStack workspace


## Installation

RudderStack recommends using the Maven build system to add the Java SDK to your project.

Add the following lines to your `pom.xml` file:
    
    
    <dependency>
       <groupId>com.rudderstack.sdk.java.analytics</groupId>
         <artifactId>analytics</artifactId>
       <version>3.0.0</version>
    </dependency>
    

Add the following line to your dependencies:
    
    
    implementation 'com.rudderstack.sdk.java.analytics:analytics:3.0.0'
    

## Initialization

To initialize the RudderStack client, use the following code:
    
    
    RudderAnalytics analytics = RudderAnalytics
             .builder("<WRITE_KEY>")
             .setDataPlaneUrl("<DATA_PLANE_URL>")
             .build();
    

> ![info](/docs/images/info.svg)
> 
> To migrate to the Java SDK v3, set the data plane URL using `setDataPlaneUrl("<DATA_PLANE_URL>")` instead of passing it as an argument.

## Configuration options

The `RudderClient.Builder` class provides the following configuration methods:

Method| Type| Description| Default value  
---|---|---|---  
`client`| `OkHttpClient`| Sets a custom `OkHttpClient`| Created by default  
`setGZIP`| Boolean| Enables/disables Gzip compression| `true`  
`log`| Log| Sets logging level (`VERBOSE`, `DEBUG`, `ERROR`, `NONE`)| `NONE`  
`setDataPlaneUrl`| String| Sets data plane URL| Your [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>)  
  
**Note:** The method automatically appends `v1/batch` to the URL if not present.  
`setUploadURL`| String| Sets data plane URL (used for Segment compatibility)| `https://YOUR_DATA_PLANE_URL/v1/batch`  
`userAgent`| String| Sets HTTP request user agent| `analytics-java/{version}`  
`queueCapacity`| Integer| Sets queue capacity| `Integer.MAX_VALUE`  
`retries`| Integer| Sets maximum event retries| `3`  
`networkExecutor`| `ExecutorService`| Sets executor service for HTTP requests| `SingleThreadExecutor`  
`callback`| Callback| Invoked on event processing| Empty list  
`forceTlsVersion1`| Boolean| Enforces TLS v1| `false`  
  
### Beta configuration options

> ![warning](/docs/images/warning.svg)
> 
> The following methods are currently in beta and subject to change.

Method| Type| Description| Default value  
---|---|---|---  
`messageTransformer`| `MessageTransformer`| Transforms message before upload| `null`  
`messageInterceptor`| `MessageInterceptor`| Intercepts messages| `null`  
`flushQueueSize`| Integer| Queue size triggering flush| `250`  
`maximumQueueSizeInBytes`| Integer| Maximum queue size for flush| `1024*500 Bytes`  
`flushInterval`| Long, TimeUnit| Queue flush interval| `10 seconds`  
`threadFactory`| `ThreadFactory`| Thread factory for creation| `null`  
`plugin`| `Plugin`| Builder configuration| `null`  
  
## Event methods

> ![warning](/docs/images/warning.svg)
> 
> The Java SDK does not persist user state. You must specify either `userId` or `anonymousId` with every event API call.

### Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) method records user identity and traits.

**Example** :
    
    
    analytics.enqueue(IdentifyMessage.builder()
        .userId("1hKOmRA4GRlm")
        .traits(ImmutableMap.builder()
            .put("name", "Alex Keener")
            .put("email", "alex@example.com")
            .put("plan", "enterprise")
            .put("logins", 24)
            .build()
        )
    );
    

**Parameters** :

Field| Type| Description  
---|---|---  
`userId`  
Required, if **`anonymousId`** is absent.| String| Unique identifier for a user in your database.  
`anonymousId`  
Required, if **`userId`** is absent.| String| Identifier set in cases where no unique user identifier is available.  
`traits`| Object| Dictionary of the user’s traits like `name`, `email`, etc.  
`context`| Object| Optional dictionary of information that provides context about the event.  
`integrations`| Object| Optional dictionary containing the destinations to be enabled or disabled.  
`timestamp`| Timestamp in ISO 8601 format| The event’s timestamp. If not provided, it defaults to the current time when the message was built.  
  
### Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) method records user actions and their associated properties.

**Example** :
    
    
    // Create a map to store event properties
    Map<String, Object> properties = new LinkedHashMap<>();
    properties.put("product_id", "P123");
    properties.put("product_name", "Running Shoes");
    properties.put("price", 89.99);
    properties.put("currency", "USD");
    properties.put("category", "Sports");
    
    // Send the track event
    analytics.enqueue(
       TrackMessage.builder("Product Added")
           .properties(properties)
           .userId("1hKOmRA4GRlm")
    );
    

**Parameters** :

Field| Type| Description  
---|---|---  
`userId`  
Required, if **`anonymousId`** is absent.| String| Unique identifier for a user in your database.  
`anonymousId`  
Required, if **`userId`** is absent.| String| Identifier set in cases where no unique user identifier is available.  
`event`  
Required| String| Name of the event.  
`properties`| Object| Optional dictionary of the properties associated with the event.  
`context`| Object| Optional dictionary of information that provides context about the event.  
`integrations`| Object| Optional dictionary containing the destinations to be enabled or disabled.  
`timestamp`| Date| The event’s timestamp. If not provided, it defaults to the current time when the message is created. The SDK automatically converts it in the ISO 8601 format before sending to the server.  
  
### Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call records page views in your application along with the relevant page information.

**Example** :
    
    
    analytics.enqueue(PageMessage.builder("Schedule")
        .userId("1hKOmRA4GRlm")
        .properties(ImmutableMap.builder()
            .put("category", "Cultural")
            .put("path", "/a/b")
            .build()
        )
    );
    

**Parameters** :

Field| Type| Description  
---|---|---  
`userId`  
Required, if **`anonymousId`** is absent.| String| Unique identifier for a user in your database.  
`anonymousId`  
Required, if **`userId`** is absent.| String| Identifier set in cases where no unique user identifier is available.  
`name`  
Required| String| Name of the viewed page.  
`properties`| Object| Optional dictionary of the properties associated with the viewed page, like `url` or `referrer`.  
`context`| Object| Optional dictionary of information that provides context about the event.  
`integrations`| Object| Optional dictionary containing the destinations to be enabled or disabled.  
`timestamp`| Timestamp in ISO 8601 format| The event’s timestamp. If not provided, it defaults to the current time when the message was built.  
  
### Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call records screen views in your mobile app.

**Example** :
    
    
    analytics.enqueue(ScreenMessage.builder("Product List")
        .userId("1hKOmRA4GRlm")
        .properties(ImmutableMap.builder()
            .put("category", "Sports")
            .put("path", "/products/sports")
            .put("view_type", "grid")
            .put("filters_applied", true)
            .build()
        )
    );
    

**Parameters** :

Field| Type| Description  
---|---|---  
`userId`  
Required, if **`anonymousId`** is absent.| String| Unique identifier for a user in your database.  
`anonymousId`  
Required, if **`userId`** is absent.| String| Identifier set in cases where no unique user identifier is available.  
`name`  
Required| String| Name of the viewed screen.  
`properties`| Object| Optional dictionary of the properties associated with the screen, like `url` or `referrer`.  
`context`| Object| Optional dictionary of information that provides context about the event.  
`integrations`| Object| Optional dictionary containing the destinations to be enabled or disabled.  
`timestamp`| Timestamp in ISO 8601 format| The event’s timestamp. If not provided, it defaults to the current time when the message was built.  
  
### Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call links an identified user with a group and records any custom traits associated with that group.

**Example** :
    
    
    analytics.enqueue(GroupMessage.builder("org_123")
        .userId("1hKOmRA4GRlm")
        .traits(ImmutableMap.builder()
            .put("name", "Acme Corp")
            .put("industry", "Technology")
            .put("employees", 500)
            .put("plan", "enterprise")
            .build()
        )
    );
    

**Parameters** :

Field| Type| Description  
---|---|---  
`userId`  
Required, if **`anonymousId`** is absent.| String| Unique identifier for a user in your database.  
`anonymousId`  
Required, if **`userId`** is absent.| String| Identifier set in cases where no unique user identifier is available.  
`groupId`  
Required| String| Unique identifier for the group in your database.  
`traits`| Object| Dictionary of the group’s traits like `name`or `email`.  
`context`| Object| Optional dictionary of information that provides context about the event.  
`integrations`| Object| Optional dictionary containing the destinations to be enabled or disabled.  
`timestamp`| Timestamp in ISO 8601 format| The event’s timestamp. If not provided, it defaults to the current time when the message was built.  
  
### Alias

> ![warning](/docs/images/warning.svg)
> 
> RudderStack supports sending `alias` events only to some destinations. See the [destination-specific documentation](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) for more information.

The [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) call merges different identities of a known user.

**Example** :
    
    
    analytics.enqueue(AliasMessage.builder("old_user_123")
        .userId("new_user_456")
    );
    

**Parameters** :

Field| Type| Description  
---|---|---  
`userId`  
Required, if **`anonymousId`** is absent.| String| Unique identifier for a user in your database.  
`anonymousId`  
Required, if **`userId`** is absent.| String| Identifier set in cases where no unique user identifier is available.  
`previousId`  
Required| String| Previous identifier for the user.  
`traits`| Object| Optional dictionary of the user’s traits like `name` or `email`.  
`context`| Object| Optional dictionary of information that provides context about the event.  
`integrations`| Object| Optional dictionary containing the destinations to be enabled or disabled.  
`timestamp`| Timestamp in ISO 8601 format| The event’s timestamp. If not provided, it defaults to the current time when the message was built.  
  
## Context object

The `context` object in the Java SDK provides additional information about the event:
    
    
    analytics.enqueue(TrackMessage.builder("Order Completed")
        .userId("1hKOmRA4GRlm")
        .context(ImmutableMap.builder()
            .put("ip", "203.0.113.9")
            .put("locale", "en-US")
            .put("userAgent", "Mozilla/5.0")
            .put("timezone", "America/New_York")
            .build()
        )
    );
    

The SDK automatically adds the following library information to every message:
    
    
    "context": {
        "library": {
            "name": "analytics-java",
            "version": "x.x.x"
        }
    }
    

Any custom information passed in the `context` object is merged with the existing context, except for the `library` information.

## Destination filtering

The SDK provides methods to enable or disable sending events to specific destinations by passing the `integrations` object in your API calls:
    
    
    analytics.enqueue(TrackMessage.builder("Order Completed")
        .userId("1hKOmRA4GRlm")
        .enableIntegration("All", false)  // Disable all destinations
        .enableIntegration("Amplitude", true)  // Enable only Amplitude
        .properties(ImmutableMap.builder()
            .put("revenue", 99.99)
            .put("currency", "USD")
            .build()
        )
    );
    

> ![warning](/docs/images/warning.svg)
> 
> Destination flags are case-sensitive and must match the destination names in the [RudderStack dashboard](<https://app.rudderstack.com/directory>).

## Event batching

The SDK queues events in memory and flushes them in batches for optimal performance. Each SDK API call adds the event to the queue instead of making an immediate HTTP request.

### Batch size limits

  * Maximum batch request size: 500KB
  * Maximum single event size: 32KB


> ![warning](/docs/images/warning.svg)
> 
> The [RudderStack HTTP Tracking API](<https://www.rudderstack.com/docs/api/http-api/>) accepts batch requests up to 500KB. Keep single event payloads below 32KB to avoid errors.

## Event flushing

The Java SDK provides a `flush` method that notifies the RudderStack client to upload the events and make sure no events are left in the queue at any given point.

### Manual flush

The `flush` method usage is shown below:
    
    
    analytics.flush()
    

### Flush blocking

By default, the Java SDK does not support blocking event flush implicitly. However, you can implement it using the following two classes:

  * `BlockingFlush`: Handles up to 65535 parallel flush calls
  * `TierBlockingFlush`: No limit on parallel flush calls


> ![warning](/docs/images/warning.svg)
> 
> Both the `BlockingFlush` and `TierBlockingFlush` classes are not included in the core SDK.

#### `BlockingFlush` implementation
    
    
    final BlockingFlush blockingFlush = BlockingFlush.create();
    
    RudderAnalytics analytics = RudderAnalytics
             .builder("<WRITE_KEY>")
             .plugin(blockingFlush.plugin())
             .setDataPlaneUrl("<DATA_PLANE_URL>")
             .build();
    
    // ...YOUR CODE...
    
    analytics.flush(); // Triggers a flush.
    blockingFlush.block();
    analytics.shutdown(); // Shuts down after the flush is complete.
    
    
    
    package sample;
    
    import com.rudderstack.sdk.java.analytics.RudderAnalytics;
    import com.rudderstack.sdk.java.analytics.Callback;
    import com.rudderstack.sdk.java.analytics.MessageTransformer;
    import com.rudderstack.sdk.java.analytics.Plugin;
    import com.rudderstack.sdk.java.analytics.messages.Message;
    import com.rudderstack.sdk.java.analytics.messages.MessageBuilder;
    import java.util.concurrent.Phaser;
    
    /*
     * The {@link RudderAnalytics} class doesn't come with a blocking {@link RudderAnalytics#flush()} implementation
     * out of the box. It's trivial to build one using a {@link Phaser} that monitors requests and is
     * able to block until they're uploaded.
     */
    public class BlockingFlush {
    
      public static BlockingFlush create() {
        return new BlockingFlush();
      }
    
      BlockingFlush() {
        this.phaser = new Phaser(1);
      }
    
      final Phaser phaser;
    
      public Plugin plugin() {
        return builder -> {
          builder.messageTransformer(
                  builder1 -> {
                    phaser.register();
                    return true;
                  });
    
          builder.callback(
              new Callback() {
                @Override
                public void success(Message message) {
                  phaser.arrive();
                }
    
                @Override
                public void failure(Message message, Throwable throwable) {
                  phaser.arrive();
                }
              });
        };
      }
    
      public void block() {
        phaser.arriveAndAwaitAdvance();
      }
    }
    

#### `TierBlockingFlush` implementation
    
    
    final TierBlockingFlush blockingFlush = TierBlockingFlush.create();
    
    RudderAnalytics analytics = RudderAnalytics
             .builder("<WRITE_KEY>")
             .plugin(blockingFlush.plugin())
             .setDataPlaneUrl("<DATA_PLANE_URL>")
             .build();
    
    // ...YOUR CODE...
    
    analytics.flush(); // Trigger a flush.
    blockingFlush.block();
    analytics.shutdown(); // Shut down after the flush is complete.
    
    
    
    package sample;
    
    import com.rudderstack.sdk.java.analytics.Callback;
    import com.rudderstack.sdk.java.analytics.Plugin;
    import com.rudderstack.sdk.java.analytics.messages.Message;
    
    import java.util.concurrent.Phaser;
    
    /**
     * Blocking flush implementor for cases where parties exceed 65535
     */
    public class TierBlockingFlush {
    
        private static final int MAX_PARTIES_PER_PHASER = (1 << 16) - 2; // max a phaser can accommodate
    
        public static TierBlockingFlush create() {
            return new TierBlockingFlush(MAX_PARTIES_PER_PHASER);
        }
    
        private TierBlockingFlush(int maxPartiesPerPhaser) {
            this.currentPhaser = new Phaser(1);
            this.maxPartiesPerPhaser = maxPartiesPerPhaser;
        }
    
        private Phaser currentPhaser;
        private final int maxPartiesPerPhaser;
    
        public Plugin plugin() {
            return builder -> {
                builder.messageTransformer(
                        messageTransformationBuilder -> {
                            currentPhaser = currentPhaser.getRegisteredParties() == maxPartiesPerPhaser ? new Phaser(currentPhaser) : currentPhaser;
                            currentPhaser.register();
                            return true;
                        });
    
                builder.callback(
                        new Callback() {
                            @Override
                            public void success(Message message) {
                                onResult();
                            }
    
                            @Override
                            public void failure(Message message, Throwable throwable) {
                                onResult();
                            }
    
                            private void onResult() {
                                if (currentPhaser.getUnarrivedParties() == 0) {
                                    currentPhaser = currentPhaser.getParent();
                                }
                                currentPhaser.arrive();
                            }
                        });
            };
        }
    
        public void block() {
            currentPhaser.arriveAndAwaitAdvance();
        }
    }
    

## Event request compression

> ![info](/docs/images/info.svg)
> 
> Note the following:
> 
>   * The event request compression feature via Gzip is enabled by default in the Java SDK version 3.0.0.
>   * Self-hosted data planes require [rudder-server](<https://github.com/rudderlabs/rudder-server>) version 1.4+ to support event request compression.
> 


The Java SDK automatically gzips event requests by leveraging interceptors in [OkHttp](<https://github.com/square/okhttp#rewriting-requests>).

When using a custom [OkHttp client](<https://github.com/rudderlabs/rudder-sdk-java/blob/c0de9e6de6d8fdde43df418edd33a7e6cc720680/analytics-sample/src/main/java/sample/Main.java#L95>) with the `client` API, its interceptor configuration takes precedence over the `setGZIP` setting.

See the [sample application](<https://github.com/rudderlabs/rudder-sdk-java/blob/master/analytics-sample/src/main/java/sample/Main.java>) for a working example.

### Disable compression
    
    
    RudderAnalytics analytics = RudderAnalytics
             .builder("<WRITE_KEY>")
             .setDataPlaneUrl("<DATA_PLANE_URL>")
             .setGZIP(false)
             .build();
    

## Logging

The SDK provides verbose logging for debugging. You can find the following resources in the SDK’s GitHub repository:

  * Logging configuration: [Logging Plugin](<https://github.com/rudderlabs/rudder-sdk-java/blob/master/analytics-sample/src/main/java/sample/LoggingPlugin.java>)
  * Implementation example: [Sample application](<https://github.com/rudderlabs/rudder-sdk-java/blob/master/analytics-sample/src/main/java/sample/Main.java>)


## FAQ

#### Can I use the `ImmutableMap` class?

Yes, you can use the `ImmutableMap` class via the [Guava library](<https://guava.dev/>) or use the standard Java maps.

#### Does the Java SDK support event ordering?

The Java SDK does not support event ordering by default.

#### How does the Java SDK handle events larger than 32KB?

Events larger than 32KB are sent as individual batches to the backend.