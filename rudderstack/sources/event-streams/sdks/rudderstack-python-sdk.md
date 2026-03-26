# RudderStack Python SDK Reference

Complete Python SDK API reference for tracking and sending server-side events from your Python applications.

* * *

  * __7 minute read

  * 


RudderStack’s **Python SDK** provides a comprehensive API for tracking and sending events from your Python applications to various destinations.

For implementation examples and source code, see the SDK’s [GitHub repository](<https://github.com/rudderlabs/rudder-sdk-python>).

[![Github Badge](https://img.shields.io/pypi/v/rudder-sdk-python?style=flat)](<https://pypi.org/project/rudder-sdk-python/>)

## Prerequisites

  * A Python source [set up in the RudderStack dashboard](<https://www.rudderstack.com/docs/dashboard-guides/sources/#add-a-source>)
  * The [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) for your Python source — you can find it the **Setup** tab of the source
  * The [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) associated with your RudderStack workspace


## Installation

To install the RudderStack Python SDK using [**pip**](<https://pip.pypa.io/en/stable/>), run the following command:
    
    
    pip install rudder-sdk-python
    

## Initialization

To initialize the SDK, run the following code snippet:
    
    
    import rudderstack.analytics as rudder_analytics
    
    rudder_analytics.write_key = WRITE_KEY
    rudder_analytics.dataPlaneUrl = DATA_PLANE_URL
    

## Configuration options

The Python SDK provides the following configuration options:

Parameter| Description| Default value  
---|---|---  
`on_error`| Callback for exception thrown while uploading the messages.| `None`  
`debug`| The SDK prints the logs if set to `True`.| `False`  
`send`| The SDK does not send the data to the RudderStack backend if set to `False`.| `True`  
`sync_mode`| The SDK sends the data immediately instead of queueing it, if set to `True`.| `False`  
`max_queue_size`| Maximum queue size the SDK uses to enqueue the events.| `10000`  
`gzip`| The SDK disables gzipping the event data if set to `False`.| `True`  
`timeout`| The timeout for sending POST requests to the RudderStack backend.| `15`  
`max_retries`| Maximum number of retry requests the SDK makes to the RudderStack backend.| `10`  
`upload_interval`| Maximum duration between two upload (flush) activities.| `0.5s`  
`upload_size`| Number of events in the queue that triggers a flush.| `100`  
  
## Event methods

> ![warning](/docs/images/warning.svg)
> 
> The Python SDK does not persist user state. You must specify either `user_id` or `anonymous_id` with every event API call.

### Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) method records user identity and traits.

**Example** :
    
    
    rudder_analytics.identify('1hKOmRA4GRlm', {
        'email': 'alex@example.com',
        'name': 'John Doe',
        'friends': 16
    })
    

**Parameters** :

Field| Type| Description  
---|---|---  
`user_id`  
Required, if **`anonymous_id`** is absent.| String| Unique identifier for a user in your database.  
`anonymous_id`  
Required, if **`user_id`** is absent.| String| Identifier set in cases where no unique user identifier is available.  
`traits`| Object| Dictionary of the user’s traits like `name`, `email`, etc.  
`context`| Object| Optional dictionary of information that provides context about the event.  
`integrations`| Object| Optional dictionary containing the destinations to be enabled or disabled.  
`timestamp`| Datetime| The timestamp of the event. If not provided, it defaults to the current UTC time. The SDK automatically converts it in the ISO 8601 format before sending to the server.  
  
### Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) method records user actions and their associated properties.

**Method signature** :
    
    
    rudder_analytics.track(user_id=None, anonymous_id=None, event=None, properties=None, context=None, integrations=None, timestamp=None)
    

**Parameters** :

Field| Type| Description  
---|---|---  
`user_id`  
Required, if **`anonymous_id`** is absent.| String| Unique identifier for a user in your database.  
`anonymous_id`  
Required, if **`user_id`** is absent.| String| Identifier set in cases where no unique user identifier is available.  
`event`  
Required| String| Name of the event.  
`properties`| Object| Optional dictionary of the properties associated with the event.  
`context`| Object| Optional dictionary of information that provides context about the event.  
`integrations`| Object| Optional dictionary containing the destinations to be enabled or disabled.  
`timestamp`| Datetime| The timestamp of the event. If not provided, it defaults to the current UTC time. The SDK automatically converts it in the ISO 8601 format before sending to the server.  
  
**Example** :
    
    
    rudder_analytics.track('1hKOmRA4GRlm', 'Article Read', {
        'title': 'The Independence',
        'subtitle': 'Story of the Weak',
        'author': 'John Doe'
    })
    

### Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call records page views in your application along with the relevant page information.

**Example** :
    
    
    rudder_analytics.page('1hKOmRA4GRlm', 'Documentation', 'Sample Documentation', {
        'url': 'http://rudderstack.com'
    })
    

**Parameters** :

Field| Type| Description  
---|---|---  
`user_id`  
Required, if **`anonymous_id`** is absent.| String| Unique identifier for a user in your database.  
`anonymous_id`  
Required, if **`user_id`** is absent.| String| Identifier set in cases where no unique user identifier is available.  
`name`  
Required| String| Name of the viewed page.  
`category`  
Required| String| Category of the viewed page.  
`properties`| Object| Optional dictionary of the properties associated with the page, like `url` or `referrer`.  
`context`| Object| Optional dictionary of information that provides context about the event.  
`integrations`| Object| Optional dictionary containing the destinations to be enabled or disabled.  
`timestamp`| Datetime| The timestamp of the event. If not provided, it defaults to the current UTC time. The SDK automatically converts it in the ISO 8601 format before sending to the server.  
  
### Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call records screen views in your mobile app.

**Example** :
    
    
    rudder_analytics.screen('userid', 'Settings', 'Brightness', {
        'from': 'Settings Screen'
    })
    

**Parameters** :

Field| Type| Description  
---|---|---  
`user_id`  
Required, if **`anonymous_id`** is absent.| String| Unique identifier for a user in your database.  
`anonymous_id`  
Required, if **`user_id`** is absent.| String| Identifier set in cases where no unique user identifier is available.  
`name`  
Required| String| Name of the viewed screen.  
`category`  
Required| String| Category of the viewed screen.  
`properties`| Object| Optional dictionary of the properties associated with the screen, like `url` or `referrer`.  
`context`| Object| Optional dictionary of information that provides context about the event.  
`integrations`| Object| Optional dictionary containing the destinations to be enabled or disabled.  
`timestamp`| Datetime| The timestamp of the event. If not provided, it defaults to the current UTC time. The SDK automatically converts it in the ISO 8601 format before sending to the server.  
  
### Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call links an identified user with a group and records any custom traits associated with that group.

**Example** :
    
    
    rudder_analytics.group('1hKOmRA4GRlm', '12', {
        'name': 'Company',
        'domain': 'IT'
    })
    

**Parameters** :

Field| Type| Description  
---|---|---  
`user_id`  
Required, if **`anonymous_id`** is absent.| String| Unique identifier for a user in your database.  
`anonymous_id`  
Required, if **`user_id`** is absent.| String| Identifier set in cases where no unique user identifier is available.  
`group_id`  
Required| String| Unique identifier for the group in your database.  
`traits`| Object| Dictionary of the group’s traits like `name` or `email`.  
`context`| Object| Optional dictionary of information that provides context about the event.  
`integrations`| Object| Optional dictionary containing the destinations to be enabled or disabled.  
`timestamp`| Datetime| The timestamp of the event. If not provided, it defaults to the current UTC time. The SDK automatically converts it in the ISO 8601 format before sending to the server.  
  
### Alias

> ![warning](/docs/images/warning.svg)
> 
> RudderStack supports sending `alias` events only to some destinations. See the [destination-specific documentation](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) for more information.

The [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) call merges different identities of a known user.

**Example** :
    
    
    rudder_analytics.alias('previous_id', 'user_id')
    

**Parameters** :

Field| Type| Description  
---|---|---  
`user_id`  
Required| String| Unique identifier for a user in your database.  
`previous_id`  
Required| String| Previous identifier for the user.  
`context`| Object| Optional dictionary of information that provides context about the event.  
`integrations`| Object| Optional dictionary containing the destinations to be enabled or disabled.  
`timestamp`| Datetime| The timestamp of the event. If not provided, it defaults to the current UTC time. The SDK automatically converts it in the ISO 8601 format before sending to the server.  
  
## Event flushing

The Python SDK batches the events and flushes them in the background, for faster and more efficient operation. By default, the SDK flushes a batch of 100 events every 0.5 seconds since the last flush.

You can control the event flushing by tweaking the following parameters:

Parameter| Description| Default value  
---|---|---  
`max_queue_size`| Maximum queue size the SDK uses to enqueue the events.| `10000`  
`upload_interval`| Maximum duration between two upload (flush) activities.| `0.5s`  
  
### Manual flush

You can also flush the events explicitly by using the SDK’s `flush()` method to make sure no events are left in the queue.

> ![warning](/docs/images/warning.svg)
> 
> The SDK blocks the calling thread until all messages are flushed from the queue. Hence, avoid using it as a part of your request lifecycle.

A sample flush call is shown below:
    
    
    rudder_analytics.flush()
    

## Event request compression

> ![warning](/docs/images/warning.svg)
> 
> Self-hosted data planes require [rudder-server](<https://github.com/rudderlabs/rudder-server>) version 1.4+ to support event request compression.

The Python SDK automatically gzips requests. However, you can disable this feature by setting the `gzip` parameter to `false` while initializing the SDK:
    
    
    import rudderstack.analytics as rudder_analytics
    
    rudder_analytics.write_key = WRITE_KEY
    rudder_analytics.dataPlaneUrl = DATA_PLANE_URL
    rudder_analytics.gzip = False
    

## Error handling

The Python SDK provides a `on_error` callback that lets you handle any errors that might occur when sending events.
    
    
    def on_error(error, events):
        print("Error response:", error)
    
    rudder_analytics.on_error = on_error
    

> ![warning](/docs/images/warning.svg)
> 
> The `on_error` callback only returns the errors that occur with the HTTP requests to the RudderStack gateway. It does not return any errors that occur while sending data to your downstream destinations.

The `on_error` callback function takes the following objects:

Object| Type  
---|---  
error| [APIError](<https://github.com/rudderlabs/rudder-sdk-python/blob/73f1a72bfa72b75413498eabaaf4ac4a7ab2fdba/rudderstack/analytics/request.py#L65>) type.  
events| List of events that failed while being sent to the RudderStack data plane (backend). It is the raw events data which gets buffered in the SDK. Also, each event contains all the fields included in it.  
  
The below table lists some of the common request responses:

Status| Code  
---|---  
OK| 200  
Request has neither `anonymousId` nor `userId`| 400  
Invalid write key| 401  
Invalid JSON| 400  
  
## FAQ

#### How does the Python SDK handle events larger than 32KB?

The Python SDK drops any events greater than 32KB.

#### Does the Python SDK support event ordering?

The Python SDK does not support event ordering by default.