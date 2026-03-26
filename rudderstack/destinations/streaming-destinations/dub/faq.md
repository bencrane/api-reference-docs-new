# Dub Integration FAQ Beta

Answers to some of the commonly asked questions related to the Dub integration.

* * *

  * __3 minute read

  * 


This guide answers some of the commonly asked questions related to setting up and using the Dub integration with RudderStack.

## General

#### What is Dub and how does it work?

Dub is a link attribution platform that helps you track the performance of your links and campaigns. It provides analytics, attribution tracking, and conversion optimization tools to measure the effectiveness of your marketing campaigns and identify which channels drive the most valuable conversions.

#### Is Dub integration available for all RudderStack sources?

Yes, Dub works with all RudderStack SDKs and sources through cloud mode, including web, mobile (Android/iOS), server-side, and cloud sources.

#### Can I use Dub with Reverse ETL sources?

Dub does not support the Reverse ETL functionality. You can only send real-time events from supported sources.

## Plans and pricing

#### What Dub plan do I need to use conversion tracking?

Dub’s conversion tracking endpoints (`/track/lead` and `/track/sale`) are available only for users on the **Business plan** or higher.

Free, Pro, and Starter plans do not include conversion attribution capabilities.

#### What are the rate limits for Dub by plan?

Plan| Requests per Second| Requests per Minute  
---|---|---  
Free| 10| 600  
Pro| 25| 1,500  
Starter| 50| 3,000  
Business| 100| 6,000  
Enterprise| Custom limits| Custom limits  
  
If rate limits are exceeded, Dub returns a `429 Too Many Requests` error. RudderStack automatically handles these errors with exponential backoff retry logic.

## Setup and configuration

#### Do I need to configure event mappings?

Yes, event mappings are essential for Dub integration.

You must map your RudderStack events to either `LEAD_CONVERSION` or `SALES_CONVERSION` events in Dub. Only events with a `clickId` and configured in this mapping are successfully delivered.

## Event tracking and attribution

#### What events can I track with Dub?

You can track any conversion-related events, but they must be mapped to either:

  * **Lead Conversion** : For lead generation events (signups, demos, downloads)
  * **Sales Conversion** : For revenue-generating events (purchases, subscriptions)


#### Do I need a `clickId` for attribution?

Yes, a valid `clickId` is required for Dub to attribute conversions back to specific campaign clicks. Without a `clickId`, events will fail and not be processed.

#### Can I track multiple conversions for the same click?

Yes, Dub supports multiple conversions per click. Each conversion will be properly attributed to the original click.

## Data and privacy

#### How does consent management work with Dub?

When consent management is enabled, RudderStack only sends events to Dub when users have provided appropriate consent. You can configure this with OneTrust, Ketch, iubenda, or custom consent providers.

#### What happens to conversion data without consent?

Events are queued until the user provides consent. Once consent is given, accumulated events are processed and sent to Dub.

## Technical questions

#### What happens if events fail?

Failed events will appear in your destination events tab with error details. Common failure reasons include:

  * Missing required fields (`clickId`, `revenue`, `currency`)
  * Invalid API key
  * Incorrect or missing event mapping in the destination’s [configuration settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/dub/setup-guide/#configuration-settings>)


#### Does this integration support multiplexing?

No, Dub does not support multiplexing.

Each `track` event generates a single API call to either `/track/lead` or `/track/sale` endpoint.

#### Can I update conversion data after it’s sent to Dub?

No, Dub does not support updating existing conversions. Each conversion event creates a new conversion record.