# RudderStack Node.js SDK

Use RudderStack’s Node.js SDK to send server-side events to various destinations.

* * *

  * __12 minute read

  * 


RudderStack’s Node.js SDK lets you track and send the events from your Node applications to the specified destinations.

See the Node.js SDK [GitHub codebase](<https://github.com/rudderlabs/rudder-sdk-node>) for implementation-specific details.

[![Github Badge](https://img.shields.io/npm/v/@rudderstack/rudder-sdk-node?style=flat)](<https://www.npmjs.com/package/@rudderstack/rudder-sdk-node/>)

## SDK setup requirements

  * Sign up for [RudderStack](<https://app.rudderstack.com/signup>).
  * [Set up a Node.js source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#adding-a-source>) in the dashboard. Note the [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) for this source.
  * You will also need the [data plane URL](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>) associated with your RudderStack workspace.


> ![success](/docs/images/tick.svg)
> 
> The **Setup** tab in the RudderStack dashboard (seen above) has the SDK installation snippet containing both the write key and the data plane URL. You can use these values to integrate the Node.js SDK into your application.

## Installing the Node.js SDK

To install the RudderStack Node.js SDK using [npm](<https://www.npmjs.com/>), run the following command:
    
    
    npm install @rudderstack/rudder-sdk-node
    

## Initializing the SDK

Run the following snippet to initialize the Node.js SDK. It creates a global RudderStack client object that can be used for all subsequent event requests.
    
    
    const RudderAnalytics = require('@rudderstack/rudder-sdk-node');
    
    const client = new RudderAnalytics(WRITE_KEY, {
      dataPlaneUrl: YOUR_DATA_PLANE_URL,
    
      // More initialization options
    });
    
    
    
    const RudderAnalytics = require("@rudderstack/rudder-sdk-node")
    
    // RudderStack requires the batch endpoint of the server you are running
    const client = new RudderAnalytics(WRITE_KEY, <DATA_PLANE_URL>/v1/batch)
    

## SDK initialization options

The RudderStack Node.js SDK provides the following parameters which you can pass during the SDK’s initialization:

Parameter| Data type| Description  
---|---|---  
`flushAt`| Integer| Number of events flushed by the SDK when reached this limit.  
  
**Default value** : 20  
`flushInterval`| Integer| Maximum timespan (in milliseconds) after which the events from the in-memory queue are flushed.  
  
**Default value** : 10000  
`maxInternalQueueSize`| Integer| Maximum length of the in-memory queue.  
  
**Default value** : 20000  
`logLevel`| String| Sets the logging level. The acceptable values are `info`, `debug`, `error`, etc.  
  
**Default value** : `info`  
  
The following initialization parameters are only available for RudderStack Node.js SDK **v2.x.x and above** :

Parameter| Data type| Description  
---|---|---  
`dataPlaneUrl`| String| Your [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>)  
`path`| String| Path to the `batch` endpoint.  
  
**Default value** : `/v1/batch`  
`maxQueueSize`| Integer| Maximum payload size of a `batch` request.  
  
**Default value** : 460800 (500KB)  
`axiosConfig`| Object| Axios configuration.  
`axiosInstance`| Object| Axios instance.  
`axiosRetryConfig`| Object| Axios retry configuration.  
`retryCount`| Integer| Number of times a request is retried by Axios in case of failure.  
  
**Default value** : `3`  
`errorHandler`| Function| Function that is called if the request to server fails.  
`gzip`| Boolean| Gzip compresses the event request.  
  
**Default value** : `true`  
  
> ![warning](/docs/images/warning.svg)
> 
> For gzipping requests, your [rudder-server](<https://github.com/rudderlabs/rudder-server>) must be on v1.4.0 or above. Otherwise, your requests will fail.

## Sending events

> ![warning](/docs/images/warning.svg)
> 
> **RudderStack does not store or persist the user state in any of the server-side SDKs**.  
>   
> Unlike the client-side SDKs that deal with a single user at a given time, the server-side SDKs deal with multiple users simultaneously. Therefore, you must specify either the `userId` or `anonymousId` **every time** while making any API calls supported by the Node.js SDK.

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you identify a visiting user and associate them to their actions. It also lets you record the traits about them like their name, email address, etc.

A sample `identify` call is as shown:
    
    
    client.identify({
      userId: "1hKOmRA4GRlm",
      traits: {
        name: "Alex Keener",
        email: "alex@example.com",
        plan: "Free",
        friends: 21,
      },
    })
    

The `identify` parameters are as described below:

**Field**| **Type**| **Description**  
---|---|---  
`userId`  
Required, if **anonymousId** is absent.| String| Unique identifier for a user in your database.  
`anonymousId`  
Required, if **userId** is absent.| String| Use this field to set an identifier in cases where there is no unique user identifier.  
`context`| Object| An optional dictionary of information that provides context about a message. It is not directly related to the API call.  
`integrations`| Object| An optional dictionary containing the destinations to be either enabled or disabled.  
`timestamp`| Date| The timestamp of the message’s arrival.  
[`traits`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/#identify-traits>)| Object| Dictionary of the user’s traits like `name` or `email`.  
  
## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you track the user actions along with any properties associated with them.

A sample `track` call is shown below:
    
    
    client.track({
      userId: "1hKOmRA4GRlm",
      event: "Item Viewed",
      properties: {
        revenue: 19.95,
        shippingMethod: "Premium",
      },
    })
    

The `track` method parameters are as described below:

**Field**| **Type**| **Description**  
---|---|---  
`userId`  
Required, if **anonymousId** is absent.| String| Unique identifier for a user in your database.  
`anonymousId`  
Required, if **userId** is absent.| String| Use this field to set an identifier in cases where there is no unique user identifier.  
`event`  
Required| String| Name of the event.  
`properties`| Object| An optional dictionary of the properties associated with the event.  
`context`| Object| An optional dictionary of information that provides context about a message. It is not directly related to the API call.  
`timestamp`| Date| The timestamp of the message’s arrival.  
`integrations`| Object| An optional dictionary containing the destinations to be either enabled or disabled.  
  
## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call allows you to record the page views on your application, along with the other relevant information about the page.

A sample `page` call is as shown:
    
    
    client.page({
      userId: "1hKOmRA4GRlm",
      category: "Food",
      name: "Pizza",
      properties: {
        url: "https://example.com",
        title: "Pizza",
        referrer: "https://google.com",
      },
    })
    

The `page` method parameters are as described below:

**Field**| **Type**| **Description**  
---|---|---  
`userId`  
Required, if **anonymousId** is absent.| String| Unique identifier for a user in your database.  
`anonymousId`  
Required, if **userId** is absent.| String| Use this field to set an identifier in cases where there is no unique user identifier.  
`name`  
Required| String| Name of the viewed page.  
`context`| Object| An optional dictionary of information that provides context about a message. It is not directly related to the API call.  
`timestamp`| Date| The timestamp of the message’s arrival.  
`integrations`| Object| An optional dictionary containing the destinations to be either enabled or disabled.  
`properties`| Object| An optional dictionary of the properties associated with the viewed page, like `url` and `referrer`.  
  
## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call is the mobile equivalent of the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call. It lets you record the screen views on your mobile app along with other relevant information about the screen.

A sample `screen` call is as shown:
    
    
    client.screen({
      userId: "12345",
      category: "Food",
      name: "Pizza",
      properties: {
        screenSize: 10,
        title: "Pizza",
        referrer: "https://google.com",
      },
    })
    

The `screen` method parameters are as described below:

**Field**| **Type**| **Description**  
---|---|---  
`userId`  
Required, if **anonymousId** is absent.| String| Unique identifier for a user in your database.  
`anonymousId`  
Required, if **userId** is absent.| String| Use this field to set an identifier in cases where there is no unique user identifier.  
`name`  
Required| String| Name of the viewed page.  
`context`| Object| An optional dictionary of information that provides context about a message. It is not directly related to the API call.  
`timestamp`| Date| The timestamp of the message’s arrival.  
`integrations`| Object| An optional dictionary containing the destinations to be either enabled or disabled.  
`properties`| Object| An optional dictionary of the properties associated with the screen, like `url` or `referrer`.  
  
## Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call lets you link an identified user with a group, such as a company, organization, or an account. It also lets you record any custom traits or properties associated with that group.

A sample `group` call is as shown:
    
    
    client.group({
      userId: "12345",
      groupId: "1",
      traits: {
        name: "Company",
        description: "Google",
      },
    })
    

The `group` method parameters are as follows:

**Field**| **Type**| **Description**  
---|---|---  
`userId`  
Required, if **anonymousId** is absent.| String| Unique identifier for a user in your database.  
`anonymousId`  
Required, if **userId** is absent.| String| Use this field to set an identifier in cases where there is no unique user identifier.  
`groupId`  
Required| String| Unique identifier for the group present in your database.  
`context`| Object| An optional dictionary of information that provides context about a message. It is not directly related to the API call.  
`integrations`| Object| An optional dictionary containing the destinations to be either enabled or disabled.  
`traits`| Object| An optional dictionary of the group’s traits like `name`or `email`.  
`timestamp`| Date| The timestamp of the message’s arrival.  
  
## Alias

The [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) call lets you merge different identities of a known user. It is an advanced method that lets you change the tracked user’s ID explicitly. You can use `alias` for managing the user’s identity in some of the downstream destinations.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack supports sending `alias` events only to select downstream destinations. Refer to the [destination-specific documentation](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) for more details.

A sample `alias` call is as shown:
    
    
    client.alias({
      previousId: "old_id",
      userId: "new_id",
    })
    

The `alias` method parameters are as mentioned below:

**Field**| **Type**| **Description**  
---|---|---  
`userId`  
Required| String| Unique identifier for a user in your database.  
`anonymousId`| String| Use this field to set an identifier in cases where there is no unique user identifier.  
`previousId`  
Required| String| The previous unique identifier of the user.  
`context`| Object| An optional dictionary of information that provides context about a message. It is not directly related to the API call.  
`integrations`| Object| An optional dictionary containing the destinations to be either enabled or disabled.  
`traits`| Object| An optional dictionary of the user’s traits like `name` or `email`.  
`timestamp`| Date| The timestamp of the message’s arrival.  
  
## Data persistence

> ![announcement](/docs/images/announcement.svg)
> 
> This is a beta feature — [contact the RudderStack team](<https://rudderstack.com/join-rudderstack-slack-community>) if you face any issues.

If the Node.js SDK fails to deliver the events to RudderStack in the first attempt, it retries the event delivery. However, if RudderStack is unavailable for a longer duration, there is a possibility of data loss. To prevent this scenario, the SDK has the data persistence feature where the event data is persisted in **Redis** , guaranteeing event delivery. Simultaneously, the SDK can retry multiple times as the queue is maintained in a different process space (Redis).

> ![info](/docs/images/info.svg)
> 
> To use this feature, you will need to host a Redis server to use it as the intermediary data storage queue. RudderStack uses [Bull](<https://github.com/OptimalBits/bull>) as the interface layer between the Node.js SDK and Redis.

To achieve data persistence, you need to call the `createPersistenceQueue` method which takes two parameters - `queueOpts` and `callback`. It initializes the persistent queue. A sample SDK initialization is shown below:
    
    
    const client = new Analytics("write_key", "DATA_PLANE_URL/v1/batch", {
      flushAt: <number> = 20,
      flushInterval: <ms> = 20000
      // the max number of elements that the SDK can hold in memory,
      // this is different than the Redis list created when persistence is enabled.
      // This restricts the data in-memory when Redis is down, unreachable etc.
      maxInternalQueueSize: < number > = 20000
    });
    
    client.createPersistenceQueue({
      redisOpts: {
        host: "localhost"
      }
    }, err => {})
    
    
    
    const client = new Analytics("WRITE_KEY", {
      dataPlaneUrl: DATA_PLANE_URL
      flushAt: <number> = 20,
      flushInterval: <ms> = 20000
      // the max number of elements that the SDK can hold in memory,
      // this is different than the Redis list created when persistence is enabled.
      // This restricts the data in-memory when Redis is down, unreachable etc.
      maxInternalQueueSize: < number > = 20000
    });
    
    client.createPersistenceQueue({
      redisOpts: {
        host: "localhost"
      }
    }, err => {})
    

> ![warning](/docs/images/warning.svg)
> 
> If the `createPersistenceQueue` method is not called after initializing the SDK, the SDK will work without any persistence.

### `queueOpts`

The syntax for `createPersistenceQueue` method is as follows:

`client.createPersistenceQueue(QueueOpts, callback)`

A sample `queueOpts` initialization is shown below:
    
    
    queueOpts {
      queueName ?: string = rudderEventsQueue,
      isMultiProcessor ?: boolean = false
      // pass a value without the {}, this will used as prefix to Redis keys,
      // needed to support Redis cluster slots.
      prefix?: string = {rudder},
      redisOpts : RedisOpts,
      jobOpts?: JobOpts
    }
    

The specification of the different `queueOpts` parameters is listed in the following table:

**Parameter**| **Description**| **Default Value**  
---|---|---  
`queueName`| Name of the queue.| `20`  
`isMultiProcessor`| Determines whether to handle previously active jobs. If set to `false`, the previously active job will be picked up first by the processor. Otherwise, Bull moves this job to the back of the Redis queue to be picked up after the already pushed event.| `false`  
`prefix`| Used as the prefix to the Redis keys needed to support the Redis cluster slots.| `20000`  
`redisOpts`| Refer to the `RedisOpts` section below.| `RedisOpts`  
`jobOpts`| Refer to the `JobOpts` section below.| `JobOpts`  
  
For more information on these parameters, refer to the [Bull docs](<https://github.com/OptimalBits/bull/blob/develop/REFERENCE.md#queue>).

> ![warning](/docs/images/warning.svg)
> 
> If the same queue (RudderStack SDK initialized with the same queue name) is used in case of multiple servers (server-side SDKs), set the value of `isMultiProcessor` to `true` as event ordering is not applicable in this case.

#### `RedisOpts`
    
    
    RedisOpts {
      port?: number = 6379;
      host?: string = localhost;
      db?: number = 0;
      password?: string;
    }
    

#### `JobOpts`
    
    
    JobOpts {
      maxAttempts?: number = 10
    }
    

### `callback`

In case of an error, the `createPersistenceQueue` method returns a callback. You should retry sending the events in this scenario.
    
    
    // createPersistenceQueue calls this with error or nothing(in case of success), // user should retry in case of error
    callback: function(error) || function()
    

Calling the `createPersistenceQueue` method initializes a Redis list by calling the [Bull’s](<https://github.com/OptimalBits/bull>) utility methods. It also adds a **single** job processor for the processing (making requests to RudderStack) jobs that are pushed into the list. Any error encountered while doing this leads to a callback with the error.

> ![info](/docs/images/info.svg)
> 
> If the callback returns with an error, RudderStack recommends retry calling `createPersistenceQueue` with a backoff.

### Event flow

  * Calling the SDK methods like `track`, `page`, `identify`, etc. pushes the events to an in-memory array.
  * The events from the array are flushed as a `batch` to the Redis persistence based on the `flushAt` and `flushInterval` settings. The in-memory array has a maximum size of `maxInternalQueueSize`. **Once this size limit is reached,** __**the events won’t be accepted if not drained to the other side (cases where Redis connection is slow or the Redis server is not reachable).**
  * The processor will take the batch from the Redis list and make a request to RudderStack. In case of an error, the processor will retry sending the data again if the error can be retried (errors with status code `5xx and 429`). **The retry will go up to`JobOpts.maxAttempts` with an** **exponential backoff of power 2 with max backoff of 30 seconds**.
  * If the job fails even after `JobOpts.maxAttempts`, it will not be retried again and pushed to a `failed queue`. **You can retry them later manually using Bull’s utility methods** [listed here](<https://github.com/OptimalBits/bull/blob/develop/REFERENCE.md#queuegetfailed>) **or get them from Redis directly**.
  * There might be a scenario where the node process dies with the jobs still in active state (not completed nor failed but in the process of sending/retrying). Since the RudderStack SDK has only **1 processor for sending events** (this count should always be **1**), the next time the SDK is initialized and `createPersistenceQueue` is called, **the jobs will be picked up first by the processor to get processed to maintain event ordering based on the value of`QueueOpts.isMultiProcessor`**.
  * For multiple servers (SDK) connecting to the same queue (`QueueOpts.queueName`), there will be multiple processors fetching events from the same queue and event ordering won’t be implemented. Hence, `QueueOpts.isMultiProcessor` should be set to **`true`.**


## FAQ

##### How to ensure that all my events in the queue are processed?

You can use the `flush()` method to ensure that all events in the queue are processed. The following example highlights the use of `flush()` with a callback:
    
    
    client.flush(function(err, batch){
      console.log('Flushing done');
    })
    

#### How does the Node.js SDK handle events larger than 32KB?

The Node.js SDK accepts and sends each event greater than 32KB as a single batch and sends them to the backend.

#### Does the Node.js SDK support event ordering?

The Node.js SDK does not support event ordering by default.