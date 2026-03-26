# Cloud Extract (ETL) Sources Deprecated

Build efficient ETL pipelines by sending data from various cloud apps to your warehouse.

Available Plans

  * growth
  * enterprise


* * *

  *  __2 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **Cloud Extract (ETL) is sunset**
> 
> As of **January 10, 2026** , all ETL connections are turned off. You will not be able to activate new connections or toggle on existing connections.
> 
> See this [Release Note](<https://www.rudderstack.com/docs/releases/etl-sunset/>) for more details.

With RudderStack’s **Cloud Extract** feature, you can ingest raw events and data from different cloud apps and send them to your data warehouse via RudderStack.

Note that:

  * Cloud Extract sources support sending data only to a single [data warehouse destination](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).
  * To send data from the same Extract source to multiple warehouses, RudderStack recommends creating individual sources with the same settings for each warehouse destination.
  * RudderStack counts the number of records returned by the source APIs when queried during each sync and considers each record as an event.


## Supported sources

### [ActiveCampaign](</docs/sources/extract/activecampaign/>)### [Amplitude](</docs/sources/extract/amplitude/>)### [Bing Ads](</docs/sources/extract/bing-ads/>)### [Chargebee](</docs/sources/extract/chargebee/>)### [Customer.io](</docs/sources/extract/customerio/>)### [Facebook Ads](</docs/sources/extract/facebook-ads/>)### [Freshdesk](</docs/sources/extract/freshdesk/>)### [Google Ads](</docs/sources/extract/google-adwords/>)### [Google Analytics](</docs/sources/extract/google-analytics/>)### [Google Analytics 4](</docs/sources/extract/google-analytics/>)### [Google Search Console](</docs/sources/extract/google-search-console/>)### [Google Sheets](</docs/sources/extract/google-sheets/>)### [HubSpot](</docs/sources/extract/hubspot/>)### [Intercom](</docs/sources/extract/intercom/>)### [Iterable](</docs/sources/extract/iterable/>)### [Klaviyo](</docs/sources/extract/klaviyo/>)### [Mailchimp](</docs/sources/extract/mailchimp/>)### [Marketo](</docs/sources/extract/marketo/>)### [Marketo v2](</docs/sources/extract/marketo-v2/>)### [Mixpanel](</docs/sources/extract/mixpanel/>)### [Pipedrive](</docs/sources/extract/pipedrive/>)### [Recurly](</docs/sources/extract/recurly/>)### [Salesforce](</docs/sources/extract/salesforce/>)### [SendGrid](</docs/sources/extract/sendgrid/>)### [Stripe](</docs/sources/extract/stripe/>)### [Zendesk Chat](</docs/sources/extract/zendesk-chat/>)### [Zendesk Support](</docs/sources/extract/zendesk-support/>)

## FAQ

#### How does RudderStack count the events for Cloud Extract sources?

RudderStack counts the number of records returned by the source APIs when queried during each sync. It considers each record as an event.

#### Is it possible to have multiple Cloud Extract sources writing to the same schema?

Yes, it is.

RudderStack associates a table prefix for every Cloud Extract source writing to a warehouse schema. This way, multiple Cloud Extract sources can write to the same schema with different table prefixes.