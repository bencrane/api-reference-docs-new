# RudderStack Rust SDK Reference

Complete Rust SDK API reference for tracking and sending server-side events from your Rust applications.

* * *

  * __7 minute read

  * 


RudderStack’s **Rust SDK** provides a comprehensive API for tracking and sending events from your Rust applications to various destinations.

For implementation examples and source code, see the SDK’s [GitHub repository](<https://github.com/rudderlabs/rudder-sdk-rust>).

[![Github Badge](https://img.shields.io/crates/v/rudderanalytics?style=flat)](<https://crates.io/crates/rudderanalytics/>)

## Prerequisites

  * A Rust source [set up in the RudderStack dashboard](<https://www.rudderstack.com/docs/dashboard-guides/sources/#adding-a-source>)
  * The [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) for your Rust source — you can find it in the **Setup** tab of the source
  * The [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) associated with your RudderStack workspace


## Installation

Add the RudderStack Rust SDK crate as a project dependency by adding the following line to your `Cargo.toml` file:
    
    
    [dependencies]
    rudderanalytics = "1.0.0"
    

## Initialization

To initialize the RudderStack client, use the following code:
    
    
    use rudderanalytics::client::RudderAnalytics;
    
    let rudder_analytics = RudderAnalytics::load(
        "<WRITE_KEY>".to_string(),
        "<DATA_PLANE_URL>".to_string()
    );
    

> ![info](/docs/images/info.svg)
> 
> The SDK initialization is synchronous and returns a client instance that you can use to send events.

## Event methods

> ![warning](/docs/images/warning.svg)
> 
> The Rust SDK does not persist user state. You must specify either `user_id` or `anonymous_id` with every event API call.

### Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) method records user identity and traits.

**Example** :
    
    
    use rudderanalytics::message::{ Identify, Message };
    
    rudder_analytics
        .send(Message::Identify(Identify {
            user_id: Some("1hKOmRA4GRlm".to_string()),
            traits: Some(json!({
                "name": "Alex Keener",
                "email": "alex@example.com",
                "plan": "enterprise",
                "logins": 24,
            })),
            ..Default::default()
        }))
        .expect("Identify call failed to send data to RudderStack");
    

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
`original_timestamp`| Datetime| The timestamp of the event’s occurrence in ISO 8601 format.  
  
If not explicitly specified, the SDK appends the timestamp of the event’s receipt.  
  
### Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) method records user actions and their associated properties.

**Example** :
    
    
    use rudderanalytics::message::{ Track, Message };
    
    rudder_analytics
        .send(Message::Track(Track {
            user_id: Some("1hKOmRA4GRlm".to_string()),
            event: "Product Added".to_owned(),
            properties: Some(json!({
                "product_id": "P123",
                "product_name": "Running Shoes",
                "price": 89.99,
                "currency": "USD",
                "category": "Sports"
            })),
            ..Default::default()
        }))
        .expect("Track call failed to send data to RudderStack");
    

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
`original_timestamp`| Datetime| The timestamp of the event’s occurrence in ISO 8601 format.  
  
If not explicitly specified, the SDK appends the timestamp of the event’s receipt.  
  
### Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call records page views in your application along with the relevant page information.

**Example** :
    
    
    use rudderanalytics::message::{ Page, Message };
    
    rudder_analytics
        .send(Message::Page(Page {
            user_id: Some("1hKOmRA4GRlm".to_string()),
            name: "Schedule".to_owned(),
            properties: Some(json!({
                "category": "Cultural",
                "path": "/a/b"
            })),
            ..Default::default()
        }))
        .expect("Page call failed to send data to RudderStack");
    

**Parameters** :

Field| Type| Description  
---|---|---  
`user_id`  
Required, if **`anonymous_id`** is absent.| String| Unique identifier for a user in your database.  
`anonymous_id`  
Required, if **`user_id`** is absent.| String| Identifier set in cases where no unique user identifier is available.  
`name`  
Required| String| Name of the viewed page.  
`properties`| Object| Optional dictionary of the properties associated with the viewed page, like `url` or `referrer`.  
`context`| Object| Optional dictionary of information that provides context about the event.  
`integrations`| Object| Optional dictionary containing the destinations to be enabled or disabled.  
`original_timestamp`| Datetime| The timestamp of the event’s occurrence in ISO 8601 format.  
  
If not explicitly specified, the SDK appends the timestamp of the event’s receipt.  
  
### Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call records screen views in your mobile app.

**Example** :
    
    
    use rudderanalytics::message::{ Screen, Message };
    
    rudder_analytics
        .send(Message::Screen(Screen {
            user_id: Some("1hKOmRA4GRlm".to_string()),
            name: "Product List".to_owned(),
            properties: Some(json!({
                "category": "Sports",
                "path": "/products/sports",
                "view_type": "grid",
                "filters_applied": true
            })),
            ..Default::default()
        }))
        .expect("Screen call failed to send data to RudderStack");
    

**Parameters** :

Field| Type| Description  
---|---|---  
`user_id`  
Required, if **`anonymous_id`** is absent.| String| Unique identifier for a user in your database.  
`anonymous_id`  
Required, if **`user_id`** is absent.| String| Identifier set in cases where no unique user identifier is available.  
`name`  
Required| String| Name of the viewed screen.  
`properties`| Object| Optional dictionary of the properties associated with the screen.  
`context`| Object| Optional dictionary of information that provides context about the event.  
`integrations`| Object| Optional dictionary containing the destinations to be enabled or disabled.  
`original_timestamp`| Datetime| The timestamp of the event’s occurrence in ISO 8601 format.  
  
If not explicitly specified, the SDK appends the timestamp of the event’s receipt.  
  
### Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call links an identified user with a group and records any custom traits associated with that group.

> ![info](/docs/images/info.svg)
> 
> An identified user can belong to multiple groups.

**Example** :
    
    
    use rudderanalytics::message::{ Group, Message };
    
    rudder_analytics
        .send(Message::Group(Group {
            user_id: Some("1hKOmRA4GRlm".to_string()),
            group_id: "org_123".to_owned(),
            traits: Some(json!({
                "name": "Acme Corp",
                "industry": "Technology",
                "employees": 500,
                "plan": "enterprise"
            })),
            ..Default::default()
        }))
        .expect("Group call failed to send data to RudderStack");
    

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
`original_timestamp`| Datetime| The timestamp of the event’s occurrence in ISO 8601 format.  
  
If not explicitly specified, the SDK appends the timestamp of the event’s receipt.  
  
### Alias

> ![warning](/docs/images/warning.svg)
> 
> RudderStack supports sending `alias` events only to some destinations. See the [destination-specific documentation](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) for more information.

The [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) call merges different identities of a known user.

**Example** :
    
    
    use rudderanalytics::message::{ Alias, Message };
    
    rudder_analytics
        .send(Message::Alias(Alias {
            user_id: Some("1hKOmRA4GRlm".to_string()),
            previous_id: "12LKsA544gh".to_owned(),
            ..Default::default()
        }))
        .expect("Alias call failed to send data to RudderStack");
    

**Parameters** :

Field| Type| Description  
---|---|---  
`user_id`  
Required, if **`anonymous_id`** is absent.| String| Unique identifier for a user in your database.  
`anonymous_id`  
Required, if **`user_id`** is absent.| String| Identifier set in cases where no unique user identifier is available.  
`previous_id`  
Required| String| Previous identifier for the user.  
`traits`| Object| Optional dictionary of the user’s traits like `name` or `email`.  
`context`| Object| Optional dictionary of information that provides context about the event.  
`integrations`| Object| Optional dictionary containing the destinations to be enabled or disabled.  
`original_timestamp`| Datetime| The timestamp of the event’s occurrence in ISO 8601 format.  
  
If not explicitly specified, the SDK appends the timestamp of the event’s receipt.  
  
### Batch

The `batch` call lets you send multiple events in a single API call. It supports all event types: `identify`, `track`, `page`, `screen`, `group`, and `alias`.

> ![info](/docs/images/info.svg)
> 
> The maximum batch request size is 4 MB.

**Example** :
    
    
    use rudderanalytics::message::{ Batch, Message, BatchMessage };
    
    rudder_analytics
        .send(Message::Batch(Batch {
            batch: vec![
                BatchMessage::Identify(Identify {
                    user_id: Some("foo".to_string()),
                    traits: Some(json!({})),
                    ..Default::default()
                }),
                BatchMessage::Track(Track {
                    user_id: Some("bar".to_string()),
                    event: "Bar".to_owned(),
                    properties: Some(json!({})),
                    ..Default::default()
                }),
                BatchMessage::Track(Track {
                    user_id: Some("baz".to_string()),
                    event: "Baz".to_owned(),
                    properties: Some(json!({})),
                    ..Default::default()
                }),
            ],
            context: Some(json!({
                "foo": "bar",
            })),
            ..Default::default()
        }))
        .expect("Batch call failed to send data to RudderStack");
    

**Parameters** :

Field| Type| Description  
---|---|---  
`batch`  
Required| Vector| Contains one or more event calls of type `identify`, `track`, `page`, `screen`, `group`, and `alias`.  
`context`| Object| Optional dictionary of information that provides context about the event.  
`integrations`| Object| Optional dictionary containing the destinations to be enabled or disabled.  
`original_timestamp`| Datetime| The timestamp of the event’s occurrence in ISO 8601 format.  
  
If not explicitly specified, the SDK appends the timestamp of the event’s receipt.  
  
## Destination filtering

You can enable or disable sending events to specific destinations by passing the `integrations` object in your API calls:
    
    
    let integrations = json!({
        "All": false,  // Disable all destinations
        "Amplitude": true  // Enable only Amplitude
    });
    
    rudder_analytics
        .send(Message::Track(Track {
            user_id: Some("1hKOmRA4GRlm".to_string()),
            event: "Order Completed".to_owned(),
            properties: Some(json!({
                "revenue": 99.99,
                "currency": "USD"
            })),
            integrations: Some(integrations),
            ..Default::default()
        }))
        .expect("Track call failed to send data to RudderStack");
    

The following table describes all `integrations` parameters in detail:

Field| Type| Description  
---|---|---  
`All`| Boolean| Corresponds to all destinations to which the event is to be sent. Defaults to `true`.  
  
Setting `All: false` instructs RudderStack to not send the event data to any destinations.  
`<Destination>`| Boolean| Name of the specific destination to which the SDK sends the event, depending on the Boolean value assigned to it.  
  
> ![warning](/docs/images/warning.svg)
> 
> Destination flags are case-sensitive and must match the destination names in the [RudderStack dashboard](<https://app.rudderstack.com/directory>).

## FAQ

#### Does the Rust SDK support event ordering?

The Rust SDK does not support event ordering by default.