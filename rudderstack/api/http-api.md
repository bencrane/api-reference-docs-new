# HTTP API

Send event data from source to destination using our HTTP API.

* * *

  * __10 minute read

  * 


RudderStack offers an easy-to-use **HTTP API** that you can use to send your events programmatically. The API is fully Segment-compatible and is helpful in cases where you cannot use the SDKs.

See the [HTTP API documentation](<https://documenter.getpostman.com/view/16242548/TzeWFT6D>) for details, along with the sample requests and responses.

> ![info](/docs/images/info.svg)
> 
> RudderStack recommends using the [RudderStack SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/>) for tracking and routing user events from your sources. The SDKs also offer automatic tagging of user context, event batching, and a retry functionality during delivery failure.

## Prerequisites

  * The RudderStack HTTP server must be accessible from your HTTP client
  * [Set up a source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#add-a-source>) and connect it to a [destination](<https://www.rudderstack.com/docs/dashboard-guides/destinations/#add-a-destination>) in your RudderStack dashboard
  * Note your [source write key](<https://www.rudderstack.com/docs/dashboard-guides/sources/#overview>) to authenticate API requests

[![Source information](/docs/images/dashboard-guides/sources/source-information.webp)](</docs/images/dashboard-guides/sources/source-information.webp>)

  * Download (Right click > **Save Link As**) and import the Postman collection in this [URL](<https://www.getpostman.com/collections/480307c55ad2b9dd4e27>). Then, edit the variables `source_write_key` and `data_plane_url`with your write key and [data plane URL](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>)


## Authorization

RudderStack uses Basic Authentication for authenticating all HTTP requests.

If you’re using Postman, authenticate the API by including an empty string (`""`) as the username and your source write key as the password in the **Authorization** tab.

> ![info](/docs/images/info.svg)
> 
> To send events via the RudderStack HTTP API, set the **Content-Type** header to `application/json`.

## Base URL

Use the [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) as the base URL for your API requests.

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you associate a visiting user to their actions and record any associated traits.

POST

/v1/identify

#### Sample payload
    
    
    {
      "userId": "identified user id",
      "anonymousId":"anon-id-new",
      "context": {
        "traits": {
           "trait1": "new-val"  
        },
        "ip": "14.5.67.21",
        "library": {
            "name": "http"
        }
      },
      "timestamp": "2020-02-02T00:23:09.544Z"
    }
    

#### Usage
    
    
    curl -u <source_write_key>: -X POST <data_plane_url>/v1/identify \
    -d @identify.json \
    --header "Content-Type: application/json" 
    
    
    
    http -a <source_write_key>: <DATA_PLANE_URL>/v1/identify < identify.json
    

#### Accepted fields

anonymousId

optional

string

Sets the user ID for cases where there is no unique identifier for the user. Either `userId` or `anonymousId` is required.

userId

required, if `anonymousId` is not present

string

Unique identifier for a particular user in your database.

context

optional

object

Dictionary of information that provides context about a message. However, it is not directly related to the API call.

integrations

optional

object

A dictionary containing the destinations to be either enabled or disabled.

timestamp

optional

datetime

The timestamp of the message’s arrival. If you are passing the timestamp in the event, make sure it conforms to the ISO 8601 date format `yyyy-MM-ddTHH:mm:ss.SSSZ`. For example: `2022-02-01T19:14:18.381Z`

traits

optional

object

Dictionary of the traits associated with the user, such as `name`or `email`

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you track user actions along with any properties associated with them.

POST

/v1/track

#### Sample payload
    
    
    {
      "userId": "identified user id",
      "anonymousId":"anon-id-new",
      "event": "Product Purchased new",
      "properties": {
        "name": "Shirt",
        "revenue": 4.99
      },
      "traits": {
        "email": "alex@example.com"
      },
      "context": {
        "ip": "14.5.67.21",
        "library": {
            "name": "http"
        }
      },
      "timestamp": "2020-02-02T00:23:09.544Z"
    }
    

#### Usage
    
    
    curl -u <source_write_key>: -X POST <data_plane_url>/v1/track \
    -d @track.json \
    --header "Content-Type: application/json" 
    
    
    
    http -a <source_write_key>: <DATA_PLANE_URL>/v1/track < track.json
    

#### Accepted fields

anonymousId

optional

string

Sets the user ID for cases where there is no unique identifier for the user. Either `userId` or `anonymousId` is required.

userId

required, if `anonymousId` is not present

string

Unique identifier for a particular user in your database.

context

optional

object

Dictionary of information that provides context about a message. However, it is not directly related to the API call.

event

required

string

Name of the event being performed by the user.

properties

optional

object

Dictionary of the properties associated with a particular event.

traits

optional

object

Explicitly specified user traits. Note that:  
  


  * The client-side SDKs automatically add this object persisted from the `identify` event.
  * Any traits specified in the `track` event will override the existing traits persisted from the `identify` event.
  * The override will be applicable only for the particular `track` event where the `traits` object is specified explicitly. For future events, the user traits persisted from the `identify` event are used.


integrations

optional

object

A dictionary containing the destinations to be either enabled or disabled.

timestamp

optional

datetime

The timestamp of the message’s arrival. If you are passing the timestamp in the event, make sure it conforms to the ISO 8601 date format `yyyy-MM-ddTHH:mm:ss.SSSZ`. For example: `2022-02-01T19:14:18.381Z`

## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views with any additional relevant information about the viewed page.

POST

/v1/page

#### Sample payload
    
    
    {
      "userId": "identified user id",
      "anonymousId":"anon-id-new",
      "name": "Page View",
      "properties": {
        "title": "Home",
        "path": "/"
      },
      "context": {
        "ip": "14.5.67.21",
        "library": {
            "name": "http"
        }
      },
      "timestamp": "2020-02-02T00:23:09.544Z"
    }
    

#### Usage
    
    
    curl -u <source_write_key>: -X POST <data_plane_url>/v1/page \
    -d @page.json \
    --header "Content-Type: application/json" 
    
    
    
    http -a <your_write_key>: <DATA_PLANE_URL>/v1/page < page.json
    

#### Accepted fields

anonymousId

optional

string

Sets the user ID for cases where there is no unique identifier for the user. Either `userId` or `anonymousId` is required.

userId

required, if `anonymousId` is not present

string

Unique identifier for a particular user in your database.

context

optional

object

Dictionary of information that provides context about a message. However, it is not directly related to the API call.

integrations

optional

object

A dictionary containing the destinations to be either enabled or disabled.

name

required

string

Name of the page being viewed.

properties

optional

object

Dictionary of the properties associated with a particular event.

timestamp

optional

datetime

The timestamp of the message’s arrival. If you are passing the timestamp in the event, make sure it conforms to the ISO 8601 date format `yyyy-MM-ddTHH:mm:ss.SSSZ`. For example: `2022-02-01T19:14:18.381Z`

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call is the mobile equivalent of the `page` call. It lets you record whenever your user views their mobile screen with any additional relevant information about the screen.

POST

/v1/screen

#### Sample payload
    
    
    {
      "userId": "identified user id",
      "anonymousId":"anon-id-new",
      "name": "Screen View",
      "properties": {
        "prop1": "5"
      },
      "context": {
        "ip": "14.5.67.21",
        "library": {
            "name": "http"
        }
      },
      "timestamp": "2020-02-02T00:23:09.544Z"
    }
    

#### Usage
    
    
    curl -u <source_write_key>: -X POST <data_plane_url>/v1/screen \
    -d @screen.json \
    --header "Content-Type: application/json" 
    
    
    
    http -a <source_write_key>: <DATA_PLANE_URL>/v1/screen < screen.json
    

#### Accepted fields

anonymousId

optional

string

Sets the user ID for cases where there is no unique identifier for the user. Either `userId` or `anonymousId` is required.

userId

required, if `anonymousId` is not present

string

Unique identifier for a particular user in your database.

context

optional

object

Dictionary of information that provides context about a message. However, it is not directly related to the API call.

integrations

optional

object

A dictionary containing the destinations to be either enabled or disabled.

name

required

string

Name of the screen being viewed.

properties

optional

object

Dictionary of the properties associated with the page being viewed, such as `url` and `referrer`.

timestamp

optional

datetime

The timestamp of the message’s arrival. If you are passing the timestamp in the event, make sure it conforms to the ISO 8601 date format `yyyy-MM-ddTHH:mm:ss.SSSZ`. For example: `2022-02-01T19:14:18.381Z`

## Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call lets you link an identified user with a group such as a company, organization, or an account. It also lets you record any custom traits associated with that group, like the name of the company, the number of employees, etc.

POST

/v1/group

#### Sample payload
    
    
    {
      "userId": "user123",
      "groupId": "group1",
      "traits": {
        "name": "Company",
        "industry": "Industry",
        "employees": 123
      },
      "context": {
        "traits": {
           "trait1": "new-val"  
        },
        "ip": "14.5.67.21",
        "library": {
            "name": "http"
        }
      },
      "timestamp": "2020-01-21T00:21:34.208Z"
    }
    

#### Usage
    
    
    curl -u <source_write_key>: -X POST <data_plane_url>/v1/group \
    -d @group.json \
    --header "Content-Type: application/json" 
    
    
    
    http -a <source_write_key>: <DATA_PLANE_URL>/v1/group < group.json
    

#### Accepted fields

anonymousId

optional

string

Sets the user ID for cases where there is no unique identifier for the user. Either `userId` or `anonymousId` is required.

userId

required, if `anonymousId` is not present

string

Unique identifier for a particular user in your database.

context

optional

object

Dictionary of information that provides context about a message. However, it is not directly related to the API call.

integrations

optional

object

A dictionary containing the destinations to be either enabled or disabled.

groupId

required

string

Unique identifier of the group, as present in your database.

traits

optional

object

Dictionary of the traits associated with the group, such as `name`or `email`

timestamp

optional

datetime

The timestamp of the message’s arrival. If you are passing the timestamp in the event, make sure it conforms to the ISO 8601 date format `yyyy-MM-ddTHH:mm:ss.SSSZ`. For example: `2022-02-01T19:14:18.381Z`

## Alias

The [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) call lets you merge different identities of a known user.

> ![info](/docs/images/info.svg)
> 
> `alias` is an advanced method that lets you change the tracked user’s ID explicitly. This method is useful when managing identities for some of the downstream destinations.

POST

/v1/alias

#### Sample payload
    
    
    {
      "userId": "user123",
      "previousId": "previd1",
      "context": {
        "traits": {
           "trait1": "new-val"  
        },
        "ip": "14.5.67.21",
        "library": {
            "name": "http"
        }
      },
      "timestamp": "2020-01-21T00:21:34.208Z"
    }
    

#### Usage
    
    
    curl -u <source_write_key>: -X POST <data_plane_url>/v1/alias \
    -d @alias.json \
    --header "Content-Type: application/json" 
    
    
    
    http -a <source_write_key>: <DATA_PLANE_URL>/v1/alias < alias.json
    

#### Accepted fields

userId

required, if `anonymousId` is not present

string

Unique identifier for a particular user in your database.

context

optional

object

Dictionary of information that provides context about a message. However, it is not directly related to the API call.

integrations

optional

object

A dictionary containing the destinations to be either enabled or disabled.

previousId

required

string

The previous unique identifier of the user.

traits

optional

object

Dictionary of the traits associated with the group, such as `name`or `email`

timestamp

optional

datetime

The timestamp of the message’s arrival. If you are passing the timestamp in the event, make sure it conforms to the ISO 8601 date format `yyyy-MM-ddTHH:mm:ss.SSSZ`. For example: `2022-02-01T19:14:18.381Z`

## Batch

The `batch` call allows you to send a series of `identify`, `track`, `page`, `group` and `screen` requests in a single batch. This call helps you minimize the number of outbound requests, thus enabling better performance.

> ![info](/docs/images/info.svg)
> 
> RudderStack sets a maximum limit of `4 MB` per batch request and `32 KB` per call.

POST

/v1/batch

#### Sample payload
    
    
    {
        "batch": [{
                "userId": "identified user id",
                "anonymousId": "anon-id-new",
                "type": "identify",
                "context": {
                    "traits": {
                        "trait1": "new-val"
                    },
                    "ip": "14.5.67.21",
                    "library": {
                        "name": "http"
                    }
                },
                "timestamp": "2020-02-02T00:23:09.544Z"
            },
            {
                "userId": "identified user id",
                "anonymousId": "anon-id-new",
                "event": "Product Purchased new",
                "type": "track",
                "properties": {
                    "name": "Shirt",
                    "revenue": 4.99
                },
                "context": {
                    "ip": "14.5.67.21",
                    "library": {
                        "name": "http"
                    }
                },
                "timestamp": "2020-02-02T00:23:09.544Z"
            },
            {
                "userId": "identified user id",
                "anonymousId": "anon-id-new",
                "name": "Page View",
                "type": "page",
                "properties": {
                    "title": "Home",
                    "path": "/"
                },
                "context": {
                    "ip": "14.5.67.21",
                    "library": {
                        "name": "http"
                    }
                },
                "timestamp": "2020-02-02T00:23:09.544Z"
            },
            {
                "userId": "identified user id",
                "anonymousId": "anon-id-new",
                "name": "Screen View",
                "type": "screen",
                "properties": {
                    "prop1": "5"
                },
                "context": {
                    "ip": "14.5.67.21",
                    "library": {
                        "name": "http"
                    }
                },
                "timestamp": "2020-02-02T00:23:09.544Z"
            },
            {
                "userId": "user123",
                "type": "group",
                "groupId": "group1",
                "traits": {
                    "name": "Company",
                    "industry": "Industry",
                    "employees": 123
                },
                "context": {
                    "traits": {
                        "trait1": "new-val"
                    },
                    "ip": "14.5.67.21",
                    "library": {
                        "name": "http"
                    }
                },
                "timestamp": "2020-01-21T00:21:34.208Z"
            },
            {
                "userId": "user123",
                "previousId": "previd1",
                "type":"alias",
                "context": {
                    "traits": {
                        "trait1": "new-val"
                    },
                    "ip": "14.5.67.21",
                    "library": {
                        "name": "http"
                    }
                },
                "timestamp": "2020-01-21T00:21:34.208Z"
            }
    
        ]
    }
    

#### Usage
    
    
    curl -u <source_write_key>: -X POST <data_plane_url>/v1/batch \
    -d @batch.json \
    --header "Content-Type: application/json" 
    
    
    
    http -a <source_write_key>: <DATA_PLANE_URL>/v1/batch < batch.json
    

#### Accepted fields

batch

required

array

An array of `identify`, `track`, `page`, `group` and `screen` calls. Each call must have a `type` property and a valid method name.

## HTTP responses

Status code| Description  
---|---  
`200`| Successful API request  
`400`| Bad request—possible reasons include:  
  


  * Invalid request method
  * Invalid request body
  * Invalid source/destination ID
  * Empty batch payload

  
`401`| Missing or invalid authorization header  
  


> ![info](/docs/images/info.svg)Make sure that the source write key and the basic authentication header is valid.  
  
`404`| Source or destination is disabled  
`413`| Request body is too large  
`429`| Too many requests  
`500`| Internal server error  
  
## Maximum allowed request size

RudderStack allows messages with a maximum size of `32 KB` per call. The `batch` endpoint accepts a maximum call size of `4 MB` per batch, and `32 KB` per call. RudderStack responds with a `400 Bad Request` error if these limits are exceeded.

## Event ordering

To maintain event ordering while using the HTTP API, make sure to include [`sentAt`](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/#common-fields>) and `anonymousId` as a header in every request.

[![Event ordering](/docs/images/api/http-event-ordering.webp)](</docs/images/api/http-event-ordering.webp>)

## Historical imports

RudderStack lets you import any historical data by simply adding the `timestamp` argument to any of your API calls. However, this can be done only for the destinations that accept historical time-stamped data, like Amplitude, Mixpanel, etc.

> ![info](/docs/images/info.svg)
> 
> If you are tracking current events, leave out the `timestamp` field. RudderStack will automatically add the timestamps to the event requests.