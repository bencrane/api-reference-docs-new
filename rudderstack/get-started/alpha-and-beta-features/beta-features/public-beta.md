# Public Beta Features

Learn about the Public Beta features available in RudderStack.

* * *

  * __3 minute read

  * 


This page lists the latest **Public Beta** features supported by RudderStack.

## Overview

**Public Beta** features are stable, production-ready and available to all RudderStack users. These features have undergone extensive testing and are considered safe for production use. While they may still receive updates and improvements based on user feedback, they offer reliable functionality with minimal risk.

## Features list

**Data Governance**

  * Tracking Plan Codegen
  * Bot management


**Beta integrations**

  * Sources
  * Destinations
  * HTTP Webhook destination


**AI features**

  * Rudder AI


The following sections explain each of these **Public Beta** features in more detail.

## Data governance

The following sections explain each of the **Public Beta** features that are a part of RudderStack’s [Data Governance](<https://www.rudderstack.com/docs/data-governance/overview/>) offering.

### Tracking Plan Codegen

The **Code Generation (Codegen)** feature in Tracking Plans automatically generates language-specific code snippets based on your defined event schemas. This streamlines the instrumentation process by providing accurate code represents the schema definition, including:

  * Clear structure of the properties object
  * Correct keys
  * Examples that represent the correct data type
  * Comments that specify whether properties are optional


See the [Release Notes](<https://www.rudderstack.com/docs/releases/tracking-plan-codegen/>) for more information, or [Tracking Plan Code Generation (Codegen) documentation](<https://www.rudderstack.com/docs/data-governance/tracking-plans/codegen/>) to get started.

### Bot management

> ![announcement](/docs/images/announcement.svg)
> 
> Note that:
> 
>   * Bot management is available in [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plans only.
> 
>   * This feature supports only the following web sources:
> 
>     * [JavaScript](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>)
>     * [Flutter](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-flutter-sdk/>)
>     * [AMP Analytics](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-amp-analytics/>)
> 


RudderStack’s [Bot Management](<https://www.rudderstack.com/docs/data-governance/bot-management/>) feature detects, flags, and drops bot traffic at the source to improve data quality and reduce costs in your data pipelines.

With this feature, you can:

  * Detect bot events on web sources using user agent analysis.
  * Flag bot events for downstream analysis or drop them entirely.
  * Apply global bot management settings across all web sources.
  * Configure custom bot management settings for individual sources.
  * Monitor bot event volume patterns through source metrics.


See the [Bot Management documentation](<https://www.rudderstack.com/docs/data-governance/bot-management/>) to get started.

## Integrations

The following sections explain the RudderStack integrations currently in **Public Beta**.

### Sources

Below is the list of **Beta** sources available in RudderStack:

[![iOS \(Swift\) logo](/docs/images/logos/sources/ios-swift.svg)iOS (Swift)](</docs/sources/event-streams/sdks/swift-sdk/>)[![Close CRM logo](/docs/images/logos/sources/close.webp)Close CRM](</docs/sources/event-streams/cloud-apps/close-crm/>)[![Facebook Lead Ads logo](/docs/images/logos/sources/facebook.svg)Facebook Lead Ads](</docs/sources/event-streams/cloud-apps/facebook-lead-ads/>)[![RevenueCat logo](/docs/images/logos/sources/revenuecat.webp)RevenueCat](</docs/sources/event-streams/cloud-apps/revenuecat/>)[![Slack logo](/docs/images/logos/sources/slack.svg)Slack](</docs/sources/event-streams/cloud-apps/slack/>)

### Destinations

Below is the list of **Beta** destinations available in RudderStack:

[![Accoil Analytics logo](/docs/images/logos/destinations/accoil-analytics.svg)Accoil Analytics](</docs/destinations/streaming-destinations/accoil-analytics/>)[![Adroll logo](/docs/images/logos/destinations/adroll.webp)Adroll](</docs/destinations/streaming-destinations/adroll/>)[![Bloomreach logo](/docs/images/logos/destinations/bloomreach.svg)Bloomreach](</docs/destinations/streaming-destinations/bloomreach/>)[![Bloomreach Catalog logo](/docs/images/logos/destinations/bloomreach.svg)Bloomreach Catalog](</docs/destinations/reverse-etl-destinations/bloomreach-catalog/>)[![Amazon Audience logo](/docs/images/logos/destinations/amazon.svg)Amazon Audience](</docs/destinations/reverse-etl-destinations/amazon-audience/>)[![Bing Ads Audience logo](/docs/images/logos/destinations/bing-ads.svg)Bing Ads Audience](</docs/destinations/reverse-etl-destinations/bing-ads-audience/>)[![Bing Ads Offline Conversions logo](/docs/images/logos/destinations/bing-ads.svg)Bing Ads Offline Conversions](</docs/destinations/reverse-etl-destinations/bing-ads-offline-conversions/>)[![Bloomreach Catalog logo](/docs/images/logos/destinations/bloomreach.svg)Bloomreach Catalog](</docs/destinations/reverse-etl-destinations/bloomreach-catalog/>)[![Bluecore logo](/docs/images/logos/destinations/bluecore.svg)Bluecore](</docs/destinations/streaming-destinations/bluecore/>)[![Campaign Manager 360 logo](/docs/images/logos/destinations/campaign-manager.svg)Campaign Manager 360](</docs/destinations/streaming-destinations/campaign-manager-360/>)[![ClickSend logo](/docs/images/logos/destinations/clicksend.webp)ClickSend](</docs/destinations/streaming-destinations/clicksend/>)[![CommandBar logo](/docs/images/logos/destinations/commandbar.svg)CommandBar](</docs/destinations/streaming-destinations/commandbar/>)[![Cordial logo](/docs/images/logos/destinations/cordial.svg)Cordial](</docs/destinations/streaming-destinations/cordial/>)[![Customer.io Audience logo](/docs/images/logos/destinations/customerio.svg)Customer.io Audience](</docs/destinations/reverse-etl-destinations/customerio-audience/>)[![Dub logo](/docs/images/logos/destinations/dub-logo.webp)Dub](</docs/destinations/streaming-destinations/dub/>)[![Eloqua logo](/docs/images/logos/destinations/eloqua.svg)Eloqua](</docs/destinations/reverse-etl-destinations/eloqua/>)[![Emarsys logo](/docs/images/logos/destinations/emarsys.svg)Emarsys](</docs/destinations/streaming-destinations/emarsys/>)[![FactorsAI logo](/docs/images/logos/destinations/factorsai.svg)FactorsAI](</docs/destinations/streaming-destinations/factors/>)[![Fullstory logo](/docs/images/logos/destinations/fullstory.svg)Fullstory](</docs/destinations/streaming-destinations/fullstory/>)[![Gladly logo](/docs/images/logos/destinations/gladly.webp)Gladly](</docs/destinations/streaming-destinations/gladly/>)[![Google Ads Offline Conversions logo](/docs/images/logos/destinations/googleads.svg)Google Ads Offline Conversions](</docs/destinations/streaming-destinations/google-ads-offline-conversions/>)[![Klaviyo Bulk upload logo](/docs/images/logos/destinations/klaviyo.svg)Klaviyo Bulk upload](</docs/destinations/reverse-etl-destinations/klaviyo-bulk-upload/>)[![Koala logo](/docs/images/logos/destinations/koala.svg)Koala](</docs/destinations/streaming-destinations/koala/>)[![Koddi logo](/docs/images/logos/destinations/koddi.svg)Koddi](</docs/destinations/streaming-destinations/koddi/>)[![LaunchDarkly Segments logo](/docs/images/logos/destinations/launchdarkly.svg)LaunchDarkly Segments](</docs/destinations/reverse-etl-destinations/launchdarkly-segments/>)[![LinkedIn Ads logo](/docs/images/logos/destinations/linkedin.svg)LinkedIn Ads](</docs/destinations/streaming-destinations/linkedin-ads/>)[![Linkedin Audience logo](/docs/images/logos/destinations/linkedin.svg)Linkedin Audience](</docs/destinations/reverse-etl-destinations/linkedin-audience/>)[![Loops logo](/docs/images/logos/destinations/loops.svg)Loops](</docs/destinations/streaming-destinations/loops/>)[![Lytics Bulk Upload logo](/docs/images/logos/destinations/lytics.svg)Lytics Bulk Upload](</docs/destinations/reverse-etl-destinations/lytics-bulk-upload/>)[![Marketo Lead Import logo](/docs/images/logos/destinations/marketo.svg)Marketo Lead Import](</docs/destinations/streaming-destinations/marketo-lead-import/>)[![Marketo Static Lists logo](/docs/images/logos/destinations/marketo.svg)Marketo Static Lists](</docs/destinations/reverse-etl-destinations/marketo-static-lists/>)[![Movable Ink logo](/docs/images/logos/destinations/movable-ink.svg)Movable Ink](</docs/destinations/streaming-destinations/movable-ink/>)[![Ninetailed logo](/docs/images/logos/destinations/ninetailed.webp)Ninetailed](</docs/destinations/streaming-destinations/ninetailed/>)[![Ortto logo](/docs/images/logos/destinations/autopilot.svg)Ortto](</docs/destinations/streaming-destinations/ortto/>)[![PostScript logo](/docs/images/logos/destinations/postscript.webp)PostScript](</docs/destinations/streaming-destinations/postscript/>)[![Rakuten logo](/docs/images/logos/destinations/rakuten.webp)Rakuten](</docs/destinations/streaming-destinations/rakuten/>)[![SFTP logo](/docs/images/logos/destinations/sftp.svg)SFTP](</docs/destinations/reverse-etl-destinations/sftp/>)[![Smartly logo](/docs/images/logos/destinations/smartly.svg)Smartly](</docs/destinations/streaming-destinations/smartly/>)[![Stormly logo](/docs/images/logos/destinations/stormly.webp)Stormly](</docs/destinations/streaming-destinations/stormly/>)[![The Trade Desk Real Time Conversions logo](/docs/images/logos/destinations/the-trade-desk.svg)The Trade Desk Real Time Conversions](</docs/destinations/streaming-destinations/trade-desk-realtime-conversions/>)[![The Trade Desk Audience logo](/docs/images/logos/destinations/the-trade-desk.svg)The Trade Desk Audience](</docs/destinations/reverse-etl-destinations/trade-desk-audience/>)[![Topsort logo](/docs/images/logos/destinations/topsort.svg)Topsort](</docs/destinations/streaming-destinations/topsort/>)[![TUNE logo](/docs/images/logos/destinations/tune.svg)TUNE](</docs/destinations/streaming-destinations/tune/>)[![X Ads logo](/docs/images/logos/destinations/twitter.svg)X Ads](</docs/destinations/streaming-destinations/twitter-ads/>)[![Userpilot logo](/docs/images/logos/destinations/userpilot.svg)Userpilot](</docs/destinations/streaming-destinations/userpilot/>)[![X Pixel logo](/docs/images/logos/destinations/twitter.svg)X Pixel](</docs/destinations/streaming-destinations/xpixel/>)[![Yandex.Metrica Offline Events logo](/docs/images/logos/destinations/yandex-metrica.svg)Yandex.Metrica Offline Events](</docs/destinations/reverse-etl-destinations/yandex-metrica-offline-events/>)[![Zoho logo](/docs/images/logos/destinations/zoho.svg)Zoho](</docs/destinations/reverse-etl-destinations/zoho/>)[![X Audience logo](/docs/images/logos/destinations/twitter.svg)X Audience](</docs/destinations/reverse-etl-destinations/x-audience/>)[![HTTP Webhook logo](/docs/images/logos/destinations/webhook.svg)HTTP Webhook](</docs/destinations/http-webhook/>)

  


### HTTP Webhook destination

**This feature is available in production.**

  


With our new HTTP Webhook destination, you can now quickly and easily configure custom destinations without writing a single line of code. Features include:

  * Flexible authentication options
  * Batching support
  * Dynamic configurations for payload fields, URL paths, query parameters, and custom headers


See the [Release Notes](<https://www.rudderstack.com/docs/releases/http-webhook-destination/>) for more information, or [HTTP Webhook Destination documentation](<https://www.rudderstack.com/docs/destinations/http-webhook/>) to get started.

## AI features

The following sections explain the RudderStack AI features currently in **Public Beta**.

### Rudder AI

RudderStack’s [Rudder AI](<https://www.rudderstack.com/docs/ai-features/rudder-ai/>) feature is an AI-powered Slack assistant that helps your team monitor, debug, and manage RudderStack pipelines from Slack.

You can use Rudder AI to check event volumes, analyze delivery failures, review tracking plan compliance, test transformations, and query RudderStack documentation — all through natural language. It operates with read-only access and automatically masks PII, so your data stays protected throughout every interaction.

See the [Rudder AI documentation](<https://www.rudderstack.com/docs/ai-features/rudder-ai/>) to get started.