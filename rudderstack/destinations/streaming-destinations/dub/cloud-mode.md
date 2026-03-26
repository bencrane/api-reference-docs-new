# Dub Cloud Mode Integration Beta

Send events to Dub in RudderStack cloud mode.

* * *

  * __8 minute read

  * 


After you have successfully instrumented Dub as a destination in RudderStack, follow this guide to correctly send your events to Dub in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

> ![warning](/docs/images/warning.svg)
> 
> **Business plan is required for conversion tracking**
> 
> Dub’s conversion tracking feature requires a [Business plan](<https://dub.co/pricing>) or higher. The Free, Pro, and Starter plans do not support conversion attribution.

## How to use the integration

This section gives an overview of how to use the Dub cloud mode integration with RudderStack:

  1. **Dashboard setup** : Set up the [Dub destination](<https://www.rudderstack.com/docs/destinations/streaming-destinations/dub/setup-guide/>) in RudderStack.
  2. **Initialize the Dub client on your website** : Add the `@dub/analytics` script to your website client on your website **before** initializing the RudderStack SDK.


  * See the [Dub documentation](<https://dub.co/docs/sdks/client-side/installation-guides/manual>) for more information on how to initialize the Dub script.


  3. **Initialize the RudderStack SDK** : Initialize the RudderStack SDK **after** initializing the Dub client. While setting up the SDK, retrieve the `clickId` value from the cookies and use it to instrument your `track` events.


  * See the Property mappings section for more information on how `clickId` property is mapped.


## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call sends conversion events to Dub for attribution tracking. Use these events to:

  * Track conversions back to specific campaign clicks
  * Measure campaign performance and ROI
  * Attribute sales and leads to marketing channels


A sample `track` call is shown below:
    
    
    rudderanalytics.track('User Signed Up', {
        userId: 'abc123',
        firstName: 'John',
        lastName: 'Doe',
        customerAvatar: 'https://example.com/avatar.jpg'
      }, {
        dubClickId: 'ABC123',
        traits: {
          email: 'xyz@example.com'
        }
      }
    );
    
    
    
    rudderanalytics.track('Order Completed', {
      order_id: 'order_123',
      invoiceId: 'invoice_123',
      amount: 100,
      products: {
        product_id: 'prod_123',
        sku: 'sku_123',
        name: 'Product Name',
        quantity: 1
      },
      currency: 'USD',
      paymentProcessor: 'stripe'
    });
    

> ![warning](/docs/images/warning.svg)
> 
> RudderStack processes only events that have a valid `clickId` and are mapped to Dub conversion events in the dashboard settings before successfully sending them to Dub.
> 
> Events without a `clickId` or not configured in the event mapping will fail.

### Mapping setup

Before sending `track` events, make sure to configure event mappings in your [Dub destination settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/dub/setup-guide/#configuration-settings>) to map RudderStack events to Dub conversion types.

An example is shown below — you can add these mappings based on your requirement:

RudderStack event| Dub conversion type| Use case  
---|---|---  
Purchase Completed| `SALES_CONVERSION`| Track revenue-generating conversions  
Signup Completed| `LEAD_CONVERSION`| Track lead generation conversions  
Trial Started| `LEAD_CONVERSION`| Track free trial signups  
Demo Requested| `LEAD_CONVERSION`| Track demo requests  
  
### Property mappings

This section explains the property mappings for the **Lead** and **Sale** conversion events.

#### Lead event

A Lead event occurs when a user performs an action that is not related to a revenue-generating conversion. For example, a user signing up for an account, adding a product to the cart, etc.

RudderStack maps the following properties in the `track` events (mapped to the `LEAD_CONVERSION` event in the dashboard settings) to the corresponding Dub fields:

> ![info](/docs/images/info.svg)
> 
> RudderStack sets the mode to `wait` for the lead event.
> 
> See the [Dub documentation](<https://dub.co/docs/api-reference/endpoint/track-lead#body-mode>) for more information on this mode.

RudderStack property| Dub field| Description  
---|---|---  
`context.clickId`  
Required| `clickId`| Unique `dub_id` parameter the lead conversion event is attributed to.  
`event`  
Required| `eventName`| Name of the event (must match the event mapping specified in the dashboard settings)  
`externalId.customerExternalId`  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.id`  
`context.traits.userId`  
Required| `customerExternalId`| Unique user identifier in your system.  
`traits.email`  
`properties.email`| `customerEmail`| Email address of the customer. If not passed, a random email address is generated.  
`traits.fullName`  
`traits.name`  
`traits.firstName + traits.lastName`| `customerName`| User’s name. A random name is generated if not specified, for example, `Big Red Machine`.  
`traits.avatar`| `customerAvatar`| User’s avatar URL. A random avatar URL is generated if not specified.  
`properties.eventQuantity`| `eventQuantity`| Numerical value associated with this lead event, for example, number of provisioned seats in a free trial. If defined as `x`, the lead event will be tracked `x` times.  
`properties`| `metadata`| Additional metadata stored with the `track` event — cannot exceed 10,000 characters.  
  
> ![warning](/docs/images/warning.svg)
> 
> RudderStack discards any other fields in the `traits` object apart from the ones listed above.

#### Sale event

A **Sale** event occurs when a user performs an action that is related to a revenue-generating conversion. For example, subscribing to a paid plan, upgrading from one plan to another, etc.

RudderStack maps the following properties in the `track` events (mapped to the `SALES_CONVERSION` event in the dashboard settings) to the corresponding Dub fields:

RudderStack property| Dub field| Description  
---|---|---  
`externalId.customerExternalId`  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.id`  
`context.traits.userId`  
Required| `customerExternalId`| Unique user identifier in your system.  
`event`| `eventName`| Name of the event — defaults to `Purchase`  
`properties.total`  
`properties.amount`  
Required| `amount`| Amount of sale in cents  
`properties.paymentProcessor`| `paymentProcessor`| Name of the payment processor used for processing the sale  
`properties.invoiceId`  
`properties.orderId`  
`properties.order_id`| `invoiceId`| Unique ID of the invoice in your system  
`properties.currency`| `currency`| Currency of the sale — defaults to `USD`  
`properties.leadEventName`| `leadEventName`| Name of the lead event that occurred before the sale — **it is case-sensitive**. Note that:  
  


  * You can use this name to associate the sale event with a particular lead event (instead of the latest lead event for a link-customer combination — the default behavior)
  * For direct sale tracking, you can also use this field to specify the lead event name

  
`context.dubClickId`| `clickId`| Unique ID of the click that the sale conversion event is attributed to. You can read this value from `dub_id` cookie  
`traits.fullName`  
`traits.name`  
`traits.firstName + traits.lastName`| `customerName`| User’s name. A random name is generated if not specified, for example, `Big Red Machine`.  
`traits.email`  
`properties.email`| `customerEmail`| Email address of the customer. If not passed, a random email address is generated.  
`traits.avatar`| `customerAvatar`| User’s avatar URL. A random avatar URL is generated if not specified.  
`properties`| `metadata`| Contains additional information about the sale  
  
> ![warning](/docs/images/warning.svg)
> 
> RudderStack discards any other fields in the `traits` object apart from the ones listed above.

### User identification

RudderStack sets the following hierarchy for identifying a user in Dub:

  1. `context.externalId` with type `customerExternalId`
  2. `userId` field from the event


> ![warning](/docs/images/warning.svg)
> 
> RudderStack throws an instrumentation error if no customer identifier is found.

### Custom properties

RudderStack automatically includes any additional properties from your `track` event as metadata in Dub:
    
    
    rudderanalytics.track("Purchase Completed", {
      clickId: "clk_abc123def456",
      revenue: 149.99,
      currency: "USD",
      product_category: "Electronics",
      discount_code: "SAVE20",
      customer_segment: "Premium",
      campaign_source: "email_newsletter"
    });
    

### Event processing flow

When you send a `track` event, RudderStack:

  1. **Validates the required fields** : Ensures `clickId`, `revenue`, and `currency` are present
  2. **Checks event mapping** : Verifies the event name is configured in the destination mapping
  3. **Maps event data** : Converts RudderStack format to Dub’s conversion event format
  4. **Handles amount conversion** : Multiplies revenue by 100 if the [Convert amount to cents](<https://www.rudderstack.com/docs/destinations/streaming-destinations/dub/setup-guide/#connection-settings>) setting is enabled
  5. **Sends the conversion event** : Uses Dub’s conversion attribution API


> ![info](/docs/images/info.svg)
> 
> RudderStack does not send the events if any validation fails. These events may appear as a failed event in your destination.

## Rate limits

Dub enforces rate limits that vary by subscription plan:

Plan| Requests  
(per second)| Requests  
(per minute)  
---|---|---  
Free| 10| 600  
Pro| 25| 1,500  
Starter| 50| 3,000  
Business| 100| 6,000  
Enterprise| Custom limits| Custom limits  
  
> ![info](/docs/images/info.svg)
> 
> If rate limits are exceeded, Dub returns a `429 Too Many Requests` error. RudderStack automatically handles these errors with exponential backoff retry logic.

## Event ordering

Dub requires **strict event ordering** for proper conversion attribution — the mandatory flow is **Click** > **Lead** > **Sale**. If events are processed out of order (for example, sale before lead), the conversion attribution chain will be broken and events may not be properly tracked.

> ![success](/docs/images/tick.svg)
> 
> RudderStack automatically handles this ordering requirement.

## Error handling

This section covers common error scenarios and how RudderStack handles them:

Error Type| HTTP Code| Description| Retry strategy  
---|---|---|---  
Missing `clickId`| 400| `clickId` is required for conversion events| Not retried  
Missing revenue| 400| Revenue amount is required| Not retried  
Invalid currency| 400| Currency code is invalid| Not retried  
Invalid API key| 401| Authentication failed| Not retried  
Event not mapped| 422| Event name not found in mapping configuration| Not retried  
Rate limit exceeded| 429| API rate limit exceeded| Retried with exponential backoff  
Server error| 5xx| Dub server error| Retried with exponential backoff  
  
## Troubleshooting

Issue| Steps  
---|---  
Events failing in RudderStack| 

  * Verify that you have configured event mappings for your event names
  * Your events include a valid `clickId`
  * Required fields (`revenue`, `currency`) are present
  * Check if the rate limits are exceeded (varies by your Dub plan)

  
Conversions not appearing in Dub dashboard| 

  * Verify that your API key has the required permissions to send conversion events
  * Event mappings are correctly configured
  * Events must include valid `clickId` values
  * You are on a **Business** plan or higher (required for conversions)

  
Authentication errors| 

  * Verify your API key is correct and active
  * Ensure your Dub account is on the **Business** plan or higher
  * Check that the API key has permissions for conversion events

  
  
## Best practices

This section includes some best practices for correctly using the Dub integration with RudderStack.

#### Event naming

Use consistent, descriptive event names in your mappings:
    
    
    // Good: Clear and specific
    rudderanalytics.track("product_purchase_completed", {...});
    rudderanalytics.track("demo_request_submitted", {...});
    rudderanalytics.track("trial_signup_completed", {...});
    
    // Avoid: Generic or unclear
    rudderanalytics.track("event", {...});
    rudderanalytics.track("action", {...});
    

#### Attribution timing

For accurate attribution, send conversion events as soon as possible after the conversion occurs. Delaying conversion tracking can impact attribution accuracy:
    
    
    // Send conversion event immediately after purchase
    rudderanalytics.track("Purchase Completed", {
      clickId: processedPurchase.clickId,
      revenue: processedPurchase.amount,
      currency: processPayment.currency
    });
    

#### Metadata structure

Organize your conversion metadata in a logical structure:
    
    
    rudderanalytics.track("Purchase Completed", {
      clickId: "clk_abc123def456",
      revenue: 99.99,
      currency: "USD",
      
      // Product information
      product_id: "prod_456",
      product_name: "Premium Plan",
      product_category: "SaaS Subscription",
      
      // Customer information
      customer_segment: "enterprise",
      customer_type: "existing",
      
      // Campaign data
      campaign_type: "email",
      campaign_name: "monthly_newsletter",
      utm_source: "email",
      utm_medium: "newsletter",
      utm_campaign: "product_launch"
    });
    

## See also

See the following Dub API documentation for more information:

  * [Dub API Overview](<https://dub.co/docs/api-reference>)
  * [Track Lead API](<https://dub.co/docs/api-reference/endpoint/track-lead>)
  * [Track Sale API](<https://dub.co/docs/api-reference/endpoint/track-sale>)
  * [API Authentication](<https://dub.co/docs/api-reference/tokens>)
  * [Error Handling](<https://dub.co/docs/api-reference/errors>)