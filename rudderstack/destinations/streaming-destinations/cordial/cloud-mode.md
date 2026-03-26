# Cordial Cloud Mode Integration Beta

Send events to Cordial using RudderStack cloud mode.

* * *

  * __2 minute read

  * 


After you have successfully instrumented Cordial as a destination in RudderStack, follow this guide to correctly send your events to Cordial in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/main/src/cdk/v2/destinations/cordial/>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create or update a contact in Cordial. RudderStack uses the [Contacts API](<https://support.cordial.com/hc/en-us/articles/203885958-Contacts-API>) to send this data.

> ![info](/docs/images/info.svg)
> 
> Make sure to create the contact attributes in the Cordial dashboard before sending them in your `identify` events.

A sample `identify` call is shown:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
      logins: 2,
    }, {
      externalId: [{
        type: "cordialContactId",
        id: "12345"
      }, ],
    });
    

### Supported mappings

RudderStack maps the following `identify` fields to the corresponding Cordial properties:

RudderStack property| Cordial property| Note  
---|---|---  
`traits.email`  
`context.traits.email`  
Either `email` or `externalId.id` is required.| `channels.email.address`| -  
`context.externalId.id`  
Either `email` or `externalId.id` is required.| `cID`| `externalId.type` should be set to `cordialContactId` (Cordial-generated database identifier).  
`traits.subscribedStatus`  
`context.traits.subscribeStatus`| `channels.email.subscribeStatus`|   
`traits`| `attributes`| User traits except the `email` and `subscribeStatus` fields.  
  
## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to track and create a contact’s activity in Cordial. RudderStack uses the [Contact Activities](<https://support.cordial.com/hc/en-us/articles/203885968-Contact-activities-events-API#postContactActivities>) API to send this data.

> ![info](/docs/images/info.svg)
> 
> Make sure to create a contact in Cordial using an `identify` call before sending the `track` events for that contact.

A sample `track` call is shown:
    
    
    rudderanalytics.track(
      "Product Reviewed", {
        review_id: "86ac1cd43",
        product_id: "9578257311",
        rating: 4.0,
        review_body: "Good product.",
      }, {
        externalId: [{
          type: "cordialContactId",
          id: "12345",
        }, ],
      },
    );
    

> ![warning](/docs/images/warning.svg)
> 
> Cordial has [reserved some event names](<https://support.cordial.com/hc/en-us/articles/203885968-Contact-activities-events-API#reservedEvents:~:text=Actions%20taken%20within%20a%20message%20%28reserved%20actions%29%20will%20automatically%20generate%20an%20activity%20record.%20These%20include%3A>) that automatically generate an activity record. Hence, do not use these names while sending your `track` events to Cordial.

### Supported mappings

RudderStack maps the following `track` fields to the corresponding Cordial properties:

RudderStack property| Cordial property| Note  
---|---|---  
`event`  
Required| `a`| -  
`context.externalId.id`  
`traits.email`  
`context.traits.email`  
Required| `contact identifier`| `externalId.type` should be set to `cordialContactId` (Cordial-generated database identifier).  
`properties`| `properties`| -  
`timestamp`  
`originalTimestamp`| `ats`| ISO 8601 date in the format `yyyy-MM-ddTHH:mm:ss.SSSZ`.  
  
For example: `2022-02-01T19:14:18.381Z`