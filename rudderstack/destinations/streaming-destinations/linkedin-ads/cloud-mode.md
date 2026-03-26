# LinkedIn Ads Cloud Mode Integration Beta

Send events to LinkedIn Ads using RudderStack cloud mode.

* * *

  * __2 minute read

  * 


After you have [successfully instrumented](<https://www.rudderstack.com/docs/destinations/streaming-destinations/linkedin-ads/setup-guide/>) LinkedIn Ads as a destination in RudderStack, follow this guide to correctly send your events to LinkedIn Ads in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

> ![info](/docs/images/info.svg)
> 
> RudderStack leverages the [LinkedIn Conversions API](<https://www.linkedin.com/help/lms/answer/a1680223>) (covered under [LinkedIn’s Data Processing Agreement](<https://www.linkedin.com/legal/l/dpa>)) to send the events.
> 
> Note that:
> 
>   * LinkedIn holds the conversion data for a maximum of 180 days before erasing it. It persists only the aggregate conversion reporting data in the Campaign Manager is persisted.
>   * RudderStack hashes all the email addresses in SHA256 format before sending them to LinkedIn.
>   * The Conversions API supports a batch size of 5000 records with a rate limit of 300 events per minute.
> 


Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/main/src/cdk/v2/destinations/linkedin_ads>).

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to send your conversion data to LinkedIn to measure and optimize the campaigns.
    
    
    rudderanalytics.track(
      "Conversion Event", {
        campaign: "Conversion",
        tax: 2,
        total: 27.5,
        coupon: "coupon55",
        revenue: 48,
        price: 25,
        quantity: 2
      }, {
        traits: {
          firstName: "Alex",
          lastName: "Keener",
          email: "alex@example.com"
        }
      }
    );
    

### Supported mappings

RudderStack maps the following `track` fields to the corresponding LinkedIn Ads properties:

RudderStack property| LinkedIn Ads property  
---|---  
`traits.email`  
`context.traits.email`  
`properties.email`  
Required, if `context.externalId.id.identifierType` is not present.| `SHA256_EMAIL`  
If `context.externalId.id.identifierType` is set to `LINKEDIN_FIRST_PARTY_ADS_TRACKING_UUID`  
Required, if `email` is not present.| `LINKEDIN_FIRST_PARTY_ADS_TRACKING_UUID`  
If `context.externalId.id.identifierType` is set to `ACXIOM_ID`  
Required, if `email` is not present.| `ACXIOM_ID`  
If `context.externalId.id.identifierType` is set to `ORACLE_MOAT_ID`  
Required, if `email` is not present.| `ORACLE_MOAT_ID`  
`traits.firstName`  
`traits.firstname`  
`traits.first_name`  
`context.traits.firstName`  
`context.traits.firstname`  
`context.traits.first_name`  
Required, if you are sending user traits.| `firstName`  
`traits.lastName`  
`traits.lastname`  
`traits.last_name`  
`context.traits.lastName`  
`context.traits.lastname`  
`context.traits.last_name`  
Required, if you are sending user traits.| `lastName`  
`traits.title`  
`context.traits.title`| `title`  
`context.traits.companyName`| `companyName`  
`context.traits.countryCode`| `countryCode`  
`properties.eventId`  
`properties.messageId`| `eventId`  
`timestamp`| `conversionHappenedAt`  
  
> ![info](/docs/images/info.svg)
> 
> Note the following:
> 
>   * LinkedIn uses the `eventId` field for deduplicating the data.
>   * The event’s `timestamp` must be within the last 90 days.
>   * If the **Hash and encode data** data is turned on in the dashboard settings, RudderStack automatically hash encodes the user’s email associated with the conversion event in the SHA256 format. If the events already contain hashed emails, make sure to turn off this setting.
>   * Your conversion event must have at least one of the following fields:
>     * `email`
> 
>     * `context.externalId.id.identifierType` set to either:
> 
>       * `LINKEDIN_FIRST_PARTY_ADS_TRACKING_UUID`
>       * `ACXIOM_ID`
>       * `ORACLE_MOAT_ID`
> 


**Calculating conversion value**

  * For events not having a `product` array:

RudderStack property| LinkedIn Ads property  
---|---  
`properties.currency`| `conversionValue.currencyCode`  
`properties.price` * `properties.quantity`| `conversionValue.amount`  
  
  * For events having a `product` array:

RudderStack property| LinkedIn Ads property  
---|---  
`properties.currency`| `conversionValue.currencyCode`  
Σ (`properties.product[i].price` * `properties.product[i].quantity`)| `conversionValue.amount`