# PostScript Cloud Mode Integration Beta

Send events to PostScript in RudderStack cloud mode.

* * *

  * __5 minute read

  * 


After you have successfully instrumented PostScript as a destination in RudderStack, follow this guide to correctly send your events to PostScript in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create or update a subscriber profile in PostScript. Use this call to:

  * Create new SMS subscribers
  * Update subscriber contact information
  * Associate subscribers with keyword campaigns


A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      phone: "+1-202-555-0146",
      email: "alex@example.com",
      firstName: "Alex",
      lastName: "Keener",
      keyword: "WELCOME"
    });
    

### Traits mapping

RudderStack property| PostScript field| Data type| Description  
---|---|---|---  
`traits.phone`  
`context.traits.phone`  
Required| `phone_number`| String| Subscriber’s phone number in E.164 format, for example, `+1-202-555-0146`.  
`traits.keyword`  
`context.traits.keyword`  
Required, if `keywordId` is not present| `keyword`| String| Opt-in keyword for subscription  
`traits.keywordId`  
`context.traits.keywordId`  
Required, if `keyword` is not present| `keyword_id`| String| Opt-in keyword ID for subscription  
`traits.email`  
`context.traits.email`| `email`| String| Subscriber’s email address.  
`traits.firstName`  
`context.traits.firstName`| `first_name`| String| Subscriber’s first name.  
`traits.lastName`  
`context.traits.lastName`| `last_name`| String| Subscriber’s last name.  
`subscriberId`| `subscriber_id`| String| PostScript subscriber ID used for updates.  
  
**Note** : You can also pass `subscriberId` in the [`externalId` field](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/#set-a-custom-user-id-externalid>) of your `identify` event.  
`traits.externalId`  
`context.traits.externalId`| `external_id`| String| External system identifier.  
`traits.shopifyCustomerId`  
`context.traits.shopifyCustomerId`| `shopify_customer_id`| Number| Shopify customer ID — this field is automatically converted to number.  
`traits.tags`  
`context.traits.tags`| `tags`| Array| Array of tags for subscriber segmentation.  
`traits.origin`  
`context.traits.origin`| `origin`| String| Source of subscriber acquisition.  
  
### Custom properties

RudderStack automatically converts any traits that don’t map to the standard PostScript subscriber fields to custom properties:
    
    
    rudderanalytics.identify("user123", {
      phone: "+1-202-555-0146",
      email: "user@example.com",
      loyaltyTier: "gold",
      purchaseCount: 5,
      lastPurchaseDate: "2024-01-15"
    });
    

### Event processing flow

When you send an `identify` event, RudderStack:

  1. **Validates required fields** : Ensures a phone number is present.
  2. **Maps user traits to PostScript fields** : Converts RudderStack traits to PostScript subscriber fields.
  3. **Determines operation type** :


  * If `subscriberId` is present, directly updates the subscriber.
  * If no `subscriberId`, performs a lookup by phone number to determine if the subscriber exists.


  4. **Executes the appropriate API call** :


  * To [create a new subscriber](<https://developers.postscript.io/reference/create-subscriber>): `POST /api/v2/subscribers`
  * To [update an existing subscriber](<https://developers.postscript.io/reference/update-subscriber-by-id>): `PATCH /api/v2/subscribers/{subscriber_id}`


## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call sends custom behavioral events to PostScript. Use these events to:

  * Trigger automated SMS flows
  * Track customer behavior
  * Build customer segments


A sample `track` call is shown below:
    
    
    rudderanalytics.track("Product Purchased", {
      product_id: "PRD123",
      product_name: "Wireless Headphones",
      price: 99.99,
      currency: "USD"
    }, {
      traits: {
        email: "alex@example.com",
        phone: "+1-202-555-0146"
      }
    });
    

### Supported mappings

PostScript accepts **all** event properties as custom properties. RudderStack maps the following `track` fields to the corresponding PostScript properties:

RudderStack property| PostScript field| Data type| Description  
---|---|---|---  
`event`  
Required| `type`| String| Event name.  
`properties`| `properties`| Object| Event properties.  
`timestamp`  
`originalTimestamp`| `occurred_at`| String| Event timestamp in ISO 8601 format.  
`userId`  
`subscriberId` (from external ID)| `subscriber_id`| String| PostScript subscriber ID.  
`externalId`| `external_id`| String| External system identifier.  
`context.traits.email`| `email`| String| Subscriber’s email.  
`context.traits.phone`| `phone`| String| Subscriber’s phone number.  
  
Note that all `track` events require **at least one** of the following identifiers:

  * `subscriberId`
  * `externalId`
  * `userId`
  * `email`
  * `phone`


> ![info](/docs/images/info.svg)
> 
> If no identifier is present, RudderStack still captures the event definition and makes it available in the PostScript Flows.

### Event processing flow

When you send a `track` event, RudderStack:

  1. **Validates the event name** to ensure the event name is present.
  2. **Builds the custom event payload** and maps event data to PostScript format.
  3. **Adds subscriber identification** by including available identifiers for subscriber matching.
  4. **Sends the event** using PostScript’s `POST /api/v2/events` [endpoint](<https://developers.postscript.io/reference/create-custom-event>).


## Other features

This section covers some key features supported by the PostScript destination.

### Batching support

PostScript supports batching for all message types with the following characteristics:

  * Individual responses for each event
  * Lookup-based operations for identify events
  * Efficient processing through batch subscriber lookups


### Event ordering

PostScript **requires** event ordering to ensure data consistency:

  * **Identify events** : Required for profile consistency

    * Profile attributes updates
    * Subscription status changes
    * Keyword associations
  * **Track events** : Recommended for accurate sequencing

    * Customer journey tracking
    * Automated flow triggers
    * Analytics and reporting


## Rate limits

PostScript enforces the following rate limits:

Endpoint| Event type| Rate limit  
---|---|---  
`/api/v2/subscribers`| Identify| 15 requests per second  
`/api/v2/events`| Track| 15 requests per second  
  
Note that the rate limits apply per API token:

  * Partner token: 15 requests per second for that partner
  * Shop token: 15 requests per second for that shop
  * Partner + Shop token combination: 15 requests per second for that combination


> ![info](/docs/images/info.svg)
> 
> PostScript returns a `429 Too Many Requests` error if the rate limits are exceeded. RudderStack automatically handles these errors with a exponential backoff retry logic.

## Error handling

This section covers the error handling and retry strategy for the PostScript destination.

Error Type| HTTP Code| Description| Retry strategy  
---|---|---|---  
Missing phone number| 400| Phone number required for `identify` events| Not retried  
Missing event name| 400| Event name required for `track` events| Not retried  
Rate limit exceeded| 429| API rate limit exceeded| Retried with exponential backoff  
Invalid API key| 401| Authentication failed| Not retried  
Server error| 5xx| PostScript server error| Retried with exponential backoff  
  
## FAQ

#### Can I replay missing events?

RudderStack **does not recommend** replaying missing events due to the following reasons:

  * Event ordering requirements
  * Risk of overwriting newer data
  * Potential duplicate events


You can use PostScript’s webhook system to capture missed events in real-time.

#### How does RudderStack handle custom properties?

  * **Identify** : RudderStack converts any unmapped traits to the snake case format and includes them as custom properties.
  * **Track** : RudderStack includes all event properties as-is.


#### How does RudderStack handle duplicate events?

  * **Identify events** : Updates overwrite existing subscriber data rather than merging intelligently.
  * **Track events** : Each event is treated as a separate occurrence, even with identical properties.