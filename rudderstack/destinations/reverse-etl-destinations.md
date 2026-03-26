# Reverse ETL Destinations

Send event data from Reverse ETL sources to downstream tools.

* * *

  * __3 minute read

  * 


With RudderStack, you can send the enriched warehouse data from your [Reverse ETL](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/>) sources to various downstream marketing and advertising tools. You can also use the data to build custom audiences and lists supported by these tools.

See the below table for details on the Reverse ETL features available in **all** the supported destinations:

> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * RudderStack supports the [Full sync mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/#full-sync-mode>) for all destinations except the destinations that only support [Mirror mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/#mirror-mode>).
>   * **The below table is not a complete list** — it only lists the destinations thoroughly tested for all the Reverse ETL features.
> 


Name| Sync Modes| Data mapping| Source creation method  
---|---|---|---  
Upsert| Mirror| VDM| JSON| Table| Model| Audience  
[Active  
Campaign](<https://www.rudderstack.com/docs/destinations/streaming-destinations/activecampaign/>)|  __| __| __| __| __| __| __  
[Adjust](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/>)|  __| __| __| __| __| __| __  
[Adobe  
Analytics](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adobe-analytics/>)|  __| __| __| __| __| __| __  
[Airship](<https://www.rudderstack.com/docs/destinations/streaming-destinations/airship/>)|  __| __| __| __| __| __| __  
[Algolia](<https://www.rudderstack.com/docs/destinations/streaming-destinations/algolia-insights/>)|  __| __| __| __| __| __| __  
[Amazon  
Kinesis](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-kinesis/>)|  __| __| __| __| __| __| __  
[Amazon  
Audience](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-audience/>)|  __| __| __| __| __| __| __  
[Amazon  
Kinesis  
Firehose](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-kinesis-firehose/>)|  __| __| __| __| __| __| __  
[Amazon  
S3](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-s3/>)|  __| __| __| __| __| __| __  
[Amplitude](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amplitude/>)|  __| __| __| __| __| __| __  
[Apache  
Kafka](<https://www.rudderstack.com/docs/destinations/streaming-destinations/kafka>)|  __| __| __| __| __| __| __  
[Appcues](<https://www.rudderstack.com/docs/destinations/streaming-destinations/appcues/>)|  __| __| __| __| __| __| __  
[AppsFlyer](<https://www.rudderstack.com/docs/destinations/streaming-destinations/appsflyer/>)|  __| __| __| __| __| __| __  
[Attentive  
Tag](<https://www.rudderstack.com/docs/destinations/streaming-destinations/attentive-tag/>)|  __| __| __| __| __| __| __  
[Attribution](<https://www.rudderstack.com/docs/destinations/streaming-destinations/attribution/>)|  __| __| __| __| __| __| __  
[Autopilot  
(Ortto)](<https://www.rudderstack.com/docs/destinations/streaming-destinations/autopilot/>)| __| __| __| __| __| __| __  
[Awin](<https://www.rudderstack.com/docs/destinations/streaming-destinations/awin/>)|  __| __| __| __| __| __| __  
[AWS  
Event  
Bridge](<https://www.rudderstack.com/docs/destinations/streaming-destinations/amazon-eventbridge/>)|  __| __| __| __| __| __| __  
[AWS  
Lambda](<https://www.rudderstack.com/docs/destinations/streaming-destinations/aws-lambda/>)|  __| __| __| __| __| __| __  
[AWS  
Personalize](<https://www.rudderstack.com/docs/destinations/streaming-destinations/aws-personalize/>)|  __| __| __| __| __| __| __  
[Azure  
Blob  
Storage](<https://www.rudderstack.com/docs/destinations/streaming-destinations/microsoft-azure-blob-storage/>)|  __| __| __| __| __| __| __  
[Azure  
Event  
Hubs](<https://www.rudderstack.com/docs/destinations/streaming-destinations/azure-event-hubs/>)|  __| __| __| __| __| __| __  
[BigQuery  
Stream](<https://www.rudderstack.com/docs/destinations/streaming-destinations/bigquery-stream>)|  __| __| __| __| __| __| __  
[Bing Ads Audience](<https://rudderstack.com/docs/destinations/reverse-etl-destinations/bing-ads-audience/>)|  __| __| __| __| __| __| __  
[Bing Ads  
Offline Conversions](<https://rudderstack.com/docs/destinations/reverse-etl-destinations/bing-ads-offline-conversions/>)|  __| __| __| __| __| __| __  
[Bloomreach](<https://www.rudderstack.com/docs/destinations/streaming-destinations/bloomreach/>)|  __| __| __| __| __| __| __  
[Bloomreach  
Catalog](<https://rudderstack.com/docs/destinations/reverse-etl-destinations/bloomreach-catalog/>)  
(Beta)| __| __| __| __| __| __| __  
[Bluecore](<https://www.rudderstack.com/docs/destinations/streaming-destinations/bluecore/>)|  __| __| __| __| __| __| __  
[Blueshift](<https://www.rudderstack.com/docs/destinations/streaming-destinations/blueshift/>)|  __| __| __| __| __| __| __  
[Branch](<https://www.rudderstack.com/docs/destinations/streaming-destinations/branchio/>)|  __| __| __| __| __| __| __  
[Braze](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/>)|  __| __| __| __| __| __| __  
[Campaign  
Manager  
360](<https://www.rudderstack.com/docs/destinations/streaming-destinations/campaign-manager-360/>)  
(Beta)| __| __| __| __| __| __| __  
[Candu](<https://www.rudderstack.com/docs/destinations/streaming-destinations/candu/>)|  __| __| __| __| __| __| __  
[Canny](<https://www.rudderstack.com/docs/destinations/streaming-destinations/canny/>)|  __| __| __| __| __| __| __  
[CleverTap](<https://www.rudderstack.com/docs/destinations/streaming-destinations/clevertap/>)|  __| __| __| __| __| __| __  
[ClickUp](<https://www.rudderstack.com/docs/destinations/streaming-destinations/clickup/>)|  __| __| __| __| __| __| __  
[Confluent  
Cloud](<https://www.rudderstack.com/docs/destinations/streaming-destinations/confluent-cloud/>)|  __| __| __| __| __| __| __  
[Courier](<https://www.rudderstack.com/docs/destinations/streaming-destinations/courier/>)|  __| __| __| __| __| __| __  
[Criteo  
Audience](<https://rudderstack.com/docs/destinations/reverse-etl-destinations/criteo-audience/>)|  __| __| __| __| __| __| __  
[Custify](<https://www.rudderstack.com/docs/destinations/streaming-destinations/custify/>)|  __| __| __| __| __| __| __  
[Customer.io](<https://www.rudderstack.com/docs/destinations/streaming-destinations/customer.io/>)|  __| __| __| __| __| __| __  
[Customer.io  
Audience](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/customerio-audience/>)  
(Beta)| __| __| __| __| __| __| __  
[DCM  
Floodlight](<https://www.rudderstack.com/docs/destinations/streaming-destinations/dcm-floodlight/>)|  __| __| __| __| __| __| __  
[Delighted](<https://www.rudderstack.com/docs/destinations/streaming-destinations/delighted/>)|  __| __| __| __| __| __| __  
[DigitalOcean  
Spaces](<https://www.rudderstack.com/docs/destinations/streaming-destinations/digitalocean-spaces/>)|  __| __| __| __| __| __| __  
[Discord](<https://www.rudderstack.com/docs/destinations/streaming-destinations/discord/>)|  __| __| __| __| __| __| __  
[Drip](<https://www.rudderstack.com/docs/destinations/streaming-destinations/drip/>)|  __| __| __| __| __| __| __  
[Dynamic  
Yield](<https://www.rudderstack.com/docs/destinations/streaming-destinations/dynamic-yield/>)|  __| __| __| __| __| __| __  
[Eloqua](<https://rudderstack.com/docs/destinations/reverse-etl-destinations/eloqua/>)  
(Beta)| __| __| __| __| __| __| __  
[Engage](<https://www.rudderstack.com/docs/destinations/streaming-destinations/engage/>)|  __| __| __| __| __| __| __  
[Facebook  
App  
Events](<https://www.rudderstack.com/docs/destinations/streaming-destinations/facebook-app-events/>)|  __| __| __| __| __| __| __  
[Facebook  
Conversions](<https://www.rudderstack.com/docs/destinations/streaming-destinations/fb-conversions/>)|  __| __| __| __| __| __| __  
[Facebook Custom Audience](<https://rudderstack.com/docs/destinations/reverse-etl-destinations/facebook-custom-audience/>)|  __| __| __| __| __| __| __  
[Facebook  
Pixel](<https://www.rudderstack.com/docs/destinations/streaming-destinations/fb-pixel/>)|  __| __| __| __| __| __| __  
[FactorsAI](<https://www.rudderstack.com/docs/destinations/streaming-destinations/factors/>)  
(Beta)| __| __| __| __| __| __| __  
[Freshmarketer](<https://www.rudderstack.com/docs/destinations/streaming-destinations/freshmarketer/>)|  __| __| __| __| __| __| __  
[Freshsales](<https://www.rudderstack.com/docs/destinations/streaming-destinations/freshsales/>)|  __| __| __| __| __| __| __  
[FullStory](<https://www.rudderstack.com/docs/destinations/streaming-destinations/fullstory/>)|  __| __| __| __| __| __| __  
[Gainsight](<https://www.rudderstack.com/docs/destinations/streaming-destinations/gainsight/>)|  __| __| __| __| __| __| __  
[Gainsight PX](<https://www.rudderstack.com/docs/destinations/streaming-destinations/gainsight-px/>)|  __| __| __| __| __| __| __  
[Gladly](<https://www.rudderstack.com/docs/destinations/streaming-destinations/gladly/>)|  __| __| __| __| __| __| __  
[Google Ads  
Enhanced  
Conversions](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-adwords-enhanced-conversions/>)|  __| __| __| __| __| __| __  
[Google Ads  
Offline  
Conversions](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-ads-offline-conversions/>)|  __| __| __| __| __| __| __  
[Google Ads  
Remarketing Lists](<https://rudderstack.com/docs/destinations/reverse-etl-destinations/google-ads-remarketing-lists/>)|  __| __| __| __| __| __| __  
[Google  
Analytics  
360](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-360/>)|  __| __| __| __| __| __| __  
[Google  
Analytics 4](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-analytics-4/>)  
(Beta)| __| __| __| __| __| __| __  
[Google  
Cloud  
Function](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-cloud-functions/>)|  __| __| __| __| __| __| __  
[Google  
Pub/Sub](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-pub-sub/>)|  __| __| __| __| __| __| __  
[Google  
Cloud  
Storage](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-cloud-storage/>)|  __| __| __| __| __| __| __  
[Google  
Sheets](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-sheets/>)|  __| __| __| __| __| __| __  
[Heap](<https://www.rudderstack.com/docs/destinations/streaming-destinations/heap.io/>)|  __| __| __| __| __| __| __  
[HubSpot](<https://www.rudderstack.com/docs/destinations/streaming-destinations/hubspot/>)|  __| __| __| __| __| __| __  
[Impact.com](<https://www.rudderstack.com/docs/destinations/streaming-destinations/impact-com/>)|  __| __| __| __| __| __| __  
[Indicative](<https://www.rudderstack.com/docs/destinations/streaming-destinations/indicative/>)|  __| __| __| __| __| __| __  
[InMoment](<https://www.rudderstack.com/docs/destinations/streaming-destinations/inmoment>)|  __| __| __| __| __| __| __  
[Intercom](<https://www.rudderstack.com/docs/destinations/streaming-destinations/intercom/>)|  __| __| __| __| __| __| __  
[Iterable](<https://www.rudderstack.com/docs/destinations/streaming-destinations/iterable/>)|  __| __| __| __| __| __| __  
[June](<https://www.rudderstack.com/docs/destinations/streaming-destinations/june/>)|  __| __| __| __| __| __| __  
[Keen](<https://www.rudderstack.com/docs/destinations/streaming-destinations/keen/>)|  __| __| __| __| __| __| __  
[Kissmetrics](<https://www.rudderstack.com/docs/destinations/streaming-destinations/kissmetrics/>)|  __| __| __| __| __| __| __  
[Klaviyo](<https://www.rudderstack.com/docs/destinations/streaming-destinations/klaviyo/>)|  __| __| __| __| __| __| __  
[Klaviyo Bulk Upload](<https://rudderstack.com/docs/destinations/reverse-etl-destinations/klaviyo-bulk-upload/>)|  __| __| __| __| __| __| __  
[Kochava](<https://www.rudderstack.com/docs/destinations/streaming-destinations/kochava/>)|  __| __| __| __| __| __| __  
[Kustomer](<https://www.rudderstack.com/docs/destinations/streaming-destinations/kustomer/>)|  __| __| __| __| __| __| __  
[LaunchDarkly Segments](<https://rudderstack.com/docs/destinations/reverse-etl-destinations/launchdarkly-segments/>)  
(Beta)| __| __| __| __| __| __| __  
[Leanplum](<https://www.rudderstack.com/docs/destinations/streaming-destinations/leanplum/>)|  __| __| __| __| __| __| __  
[Lemnisk](<https://www.rudderstack.com/docs/destinations/streaming-destinations/lemnisk/>)|  __| __| __| __| __| __| __  
[LinkedIn Ads](<https://www.rudderstack.com/docs/destinations/streaming-destinations/lemnisk/>)|  __| __| __| __| __| __| __  
[LinkedIn Audience](<https://www.rudderstack.com/docs/destinations/streaming-destinations/lemnisk/>)|  __| __| __| __| __| __| __  
[Lytics](<https://www.rudderstack.com/docs/destinations/streaming-destinations/lytics/>)|  __| __| __| __| __| __| __  
[Lytics Bulk  
Upload](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/lytics-bulk-upload/>)|  __| __| __| __| __| __| __  
[Mailchimp](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mailchimp>)|  __| __| __| __| __| __| __  
[Mailjet](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mailjet/>)|  __| __| __| __| __| __| __  
[Mailmodo](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mailmodo/>)|  __| __| __| __| __| __| __  
[Marketo](<https://www.rudderstack.com/docs/destinations/streaming-destinations/marketo>)|  __| __| __| __| __| __| __  
[Marketo  
Lead  
Import](<https://www.rudderstack.com/docs/destinations/streaming-destinations/marketo-lead-import>)  
(Beta)| __| __| __| __| __| __| __  
[Marketo  
Static Lists](<https://rudderstack.com/docs/destinations/reverse-etl-destinations/marketo-static-lists/>)  
(Beta)| __| __| __| __| __| __| __  
[Mautic](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mautic>)|  __| __| __| __| __| __| __  
[MinIO](<https://www.rudderstack.com/docs/destinations/streaming-destinations/minio>)|  __| __| __| __| __| __| __  
[Mixpanel](<https://www.rudderstack.com/docs/destinations/streaming-destinations/mixpanel>)|  __| __| __| __| __| __| __  
[MoEngage](<https://www.rudderstack.com/docs/destinations/streaming-destinations/moengage>)|  __| __| __| __| __| __| __  
[Monday](<https://www.rudderstack.com/docs/destinations/streaming-destinations/monday>)|  __| __| __| __| __| __| __  
[Monetate](<https://www.rudderstack.com/docs/destinations/streaming-destinations/monetate>)|  __| __| __| __| __| __| __  
[New Relic](<https://www.rudderstack.com/docs/destinations/streaming-destinations/new-relic>)|  __| __| __| __| __| __| __  
[Ninetailed](<https://www.rudderstack.com/docs/destinations/streaming-destinations/ninetailed/>)|  __| __| __| __| __| __| __  
[Ometria](<https://www.rudderstack.com/docs/destinations/streaming-destinations/ometria>)|  __| __| __| __| __| __| __  
[OneSignal](<https://www.rudderstack.com/docs/destinations/streaming-destinations/onesignal>)|  __| __| __| __| __| __| __  
[Optimizely Feature Experimentation](<https://www.rudderstack.com/docs/destinations/streaming-destinations/optimizely-feature-experimentation/>)|  __| __| __| __| __| __| __  
[Ortto](<https://www.rudderstack.com/docs/destinations/streaming-destinations/ortto>)  
(Beta)| __| __| __| __| __| __| __  
[PagerDuty](<https://www.rudderstack.com/docs/destinations/streaming-destinations/pagerduty>)|  __| __| __| __| __| __| __  
[Pardot](<https://www.rudderstack.com/docs/destinations/streaming-destinations/pardot>)|  __| __| __| __| __| __| __  
[PersistIQ](<https://www.rudderstack.com/docs/destinations/streaming-destinations/persistiq>)|  __| __| __| __| __| __| __  
[Pinterest  
Tag](<https://www.rudderstack.com/docs/destinations/streaming-destinations/pinterest-ads>)|  __| __| __| __| __| __| __  
[Pipedream](<https://www.rudderstack.com/docs/destinations/streaming-destinations/pipedream>)|  __| __| __| __| __| __| __  
[PostHog](<https://www.rudderstack.com/docs/destinations/streaming-destinations/posthog>)|  __| __| __| __| __| __| __  
[PostScript  
(Beta)](<https://www.rudderstack.com/docs/destinations/streaming-destinations/postscript>)| __| __| __| __| __| __| __  
[ProfitWell](<https://www.rudderstack.com/docs/destinations/streaming-destinations/profitwell>)|  __| __| __| __| __| __| __  
[Rakuten](<https://www.rudderstack.com/docs/destinations/streaming-destinations/rakuten/>)|  __| __| __| __| __| __| __  
[Reddit](<https://www.rudderstack.com/docs/destinations/streaming-destinations/reddit>)|  __| __| __| __| __| __| __  
[Redis](<https://www.rudderstack.com/docs/destinations/streaming-destinations/redis>)|  __| __| __| __| __| __| __  
[Refiner](<https://www.rudderstack.com/docs/destinations/streaming-destinations/refiner/>)|  __| __| __| __| __| __| __  
[Revenue  
Cat](<https://www.rudderstack.com/docs/destinations/streaming-destinations/revenue-cat>)|  __| __| __| __| __| __| __  
[Rockerbox](<https://www.rudderstack.com/docs/destinations/streaming-destinations/rockerbox>)|  __| __| __| __| __| __| __  
[Salesforce](<https://www.rudderstack.com/docs/destinations/streaming-destinations/salesforce>)|  __| __| __| __| __| __| __  
[Salesforce  
Marketing  
Cloud](<https://www.rudderstack.com/docs/destinations/streaming-destinations/sfmc>)|  __| __| __| __| __| __| __  
[Segment](<https://www.rudderstack.com/docs/destinations/streaming-destinations/segment>)|  __| __| __| __| __| __| __  
[SendGrid](<https://www.rudderstack.com/docs/destinations/streaming-destinations/sendgrid>)|  __| __| __| __| __| __| __  
[Sendinblue](<https://www.rudderstack.com/docs/destinations/streaming-destinations/sendinblue>)|  __| __| __| __| __| __| __  
[SFTP](<https://rudderstack.com/docs/destinations/reverse-etl-destinations/sftp/>)  
(Beta)| __| __| __| __| __| __| __  
[Serenytics](<https://www.rudderstack.com/docs/destinations/streaming-destinations/serenytics>)|  __| __| __| __| __| __| __  
[Shynet](<https://www.rudderstack.com/docs/destinations/streaming-destinations/shynet>)|  __| __| __| __| __| __| __  
[SIGNL4](<https://www.rudderstack.com/docs/destinations/streaming-destinations/signl4>)|  __| __| __| __| __| __| __  
[Singular](<https://www.rudderstack.com/docs/destinations/streaming-destinations/singular>)|  __| __| __| __| __| __| __  
[Slack](<https://www.rudderstack.com/docs/destinations/streaming-destinations/slack/>)|  __| __| __| __| __| __| __  
[Smartly](<https://www.rudderstack.com/docs/destinations/streaming-destinations/smartly/>)|  __| __| __| __| __| __| __  
[Snapchat  
Conversion](<https://www.rudderstack.com/docs/destinations/streaming-destinations/snapchat-conversion>)|  __| __| __| __| __| __| __  
[Snapchat  
Custom Audience](<https://rudderstack.com/docs/destinations/reverse-etl-destinations/snapchat-custom-audience/>)|  __| __| __| __| __| __| __  
[Split](<https://www.rudderstack.com/docs/destinations/streaming-destinations/split>)|  __| __| __| __| __| __| __  
[Sprig](<https://www.rudderstack.com/docs/destinations/streaming-destinations/sprig>)|  __| __| __| __| __| __| __  
[Statsig](<https://www.rudderstack.com/docs/destinations/streaming-destinations/statsig>)|  __| __| __| __| __| __| __  
[Stormly](<https://www.rudderstack.com/docs/destinations/streaming-destinations/stormly>)  
(Beta)| __| __| __| __| __| __| __  
[TikTok Audiences](<https://rudderstack.com/docs/destinations/reverse-etl-destinations/tiktok-audiences/>)|  __| __| __| __| __| __| __  
[TikTok Ads  
Offline  
Events](<https://www.rudderstack.com/docs/destinations/streaming-destinations/tiktok-ads-offline-events>)|  __| __| __| __| __| __| __  
[The Trade Desk  
Audience](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/trade-desk-audience/>)  
(Beta)| __| __| __| __| __| __| __  
[The Trade Desk  
Real Time  
Conversions](<https://www.rudderstack.com/docs/destinations/streaming-destinations/trade-desk-realtime-conversions/>)  
(Beta)| __| __| __| __| __| __| __  
[Trengo](<https://www.rudderstack.com/docs/destinations/streaming-destinations/trengo>)|  __| __| __| __| __| __| __  
[TUNE](<https://www.rudderstack.com/docs/destinations/streaming-destinations/tune/>)|  __| __| __| __| __| __| __  
[User.com](<https://www.rudderstack.com/docs/destinations/streaming-destinations/user-com>)|  __| __| __| __| __| __| __  
[Userlist](<https://www.rudderstack.com/docs/destinations/streaming-destinations/userlist>)|  __| __| __| __| __| __| __  
[Variance](<https://www.rudderstack.com/docs/destinations/streaming-destinations/variance>)|  __| __| __| __| __| __| __  
[Vero](<https://www.rudderstack.com/docs/destinations/streaming-destinations/vero>)|  __| __| __| __| __| __| __  
[Vitally](<https://www.rudderstack.com/docs/destinations/streaming-destinations/vitally>)|  __| __| __| __| __| __| __  
[WebEngage](<https://www.rudderstack.com/docs/destinations/streaming-destinations/webengage>)|  __| __| __| __| __| __| __  
[Woopra](<https://www.rudderstack.com/docs/destinations/streaming-destinations/woopra>)|  __| __| __| __| __| __| __  
[X Audience](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/x-audience/>)  
(Beta)| __| __| __| __| __| __| __  
[Yandex.Metrica  
Offline Events](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/yandex-metrica-offline-events/>)  
(Beta)| __| __| __| __| __| __| __  
[Zapier](<https://www.rudderstack.com/docs/destinations/streaming-destinations/zapier>)|  __| __| __| __| __| __| __  
[Zendesk](<https://www.rudderstack.com/docs/destinations/streaming-destinations/zendesk>)|  __| __| __| __| __| __| __  
[Webhooks](<https://www.rudderstack.com/docs/destinations/webhooks>)|  __| __| __| __| __| __| __  
  
The following integrations are built to accept data**only** from the Reverse ETL sources:

[![Amazon Audience logo](/docs/images/logos/destinations/amazon.svg)Amazon Audience](</docs/destinations/reverse-etl-destinations/amazon-audience/>)[![Bing Ads Audience logo](/docs/images/logos/destinations/bing-ads.svg)Bing Ads Audience](</docs/destinations/reverse-etl-destinations/bing-ads-audience/>)[![Bing Ads Offline Conversions logo](/docs/images/logos/destinations/bing-ads.svg)Bing Ads Offline Conversions](</docs/destinations/reverse-etl-destinations/bing-ads-offline-conversions/>)[![Bloomreach Catalog logo](/docs/images/logos/destinations/bloomreach.svg)Bloomreach Catalog](</docs/destinations/reverse-etl-destinations/bloomreach-catalog/>)[![Criteo Audience logo](/docs/images/logos/destinations/criteo.svg)Criteo Audience](</docs/destinations/reverse-etl-destinations/criteo-audience/>)[![Customer.io Audience logo](/docs/images/logos/destinations/customerio.svg)Customer.io Audience](</docs/destinations/reverse-etl-destinations/customerio-audience/>)[![Eloqua logo](/docs/images/logos/destinations/eloqua.svg)Eloqua](</docs/destinations/reverse-etl-destinations/eloqua/>)[![Facebook Custom Audience logo](/docs/images/logos/destinations/facebook.svg)Facebook Custom Audience](</docs/destinations/reverse-etl-destinations/facebook-custom-audience/>)[![Google Ads Remarketing Lists \(Customer Match\) logo](/docs/images/logos/destinations/googleads.svg)Google Ads Remarketing Lists (Customer Match)](</docs/destinations/reverse-etl-destinations/google-ads-remarketing-lists/>)[![Klaviyo Bulk upload logo](/docs/images/logos/destinations/klaviyo.svg)Klaviyo Bulk upload](</docs/destinations/reverse-etl-destinations/klaviyo-bulk-upload/>)[![LaunchDarkly Segments logo](/docs/images/logos/destinations/launchdarkly.svg)LaunchDarkly Segments](</docs/destinations/reverse-etl-destinations/launchdarkly-segments/>)[![Linkedin Audience logo](/docs/images/logos/destinations/linkedin.svg)Linkedin Audience](</docs/destinations/reverse-etl-destinations/linkedin-audience/>)[![Lytics Bulk Upload logo](/docs/images/logos/destinations/lytics.svg)Lytics Bulk Upload](</docs/destinations/reverse-etl-destinations/lytics-bulk-upload/>)[![Marketo Static Lists logo](/docs/images/logos/destinations/marketo.svg)Marketo Static Lists](</docs/destinations/reverse-etl-destinations/marketo-static-lists/>)[![SFTP logo](/docs/images/logos/destinations/sftp.svg)SFTP](</docs/destinations/reverse-etl-destinations/sftp/>)[![Snapchat Custom Audience logo](/docs/images/logos/destinations/snapchat.svg)Snapchat Custom Audience](</docs/destinations/reverse-etl-destinations/snapchat-custom-audience/>)[![The Trade Desk Audience logo](/docs/images/logos/destinations/the-trade-desk.svg)The Trade Desk Audience](</docs/destinations/reverse-etl-destinations/trade-desk-audience/>)[![TikTok Audiences logo](/docs/images/logos/destinations/tiktok-ads.svg)TikTok Audiences](</docs/destinations/reverse-etl-destinations/tiktok-audiences/>)[![Yandex.Metrica Offline Events logo](/docs/images/logos/destinations/yandex-metrica.svg)Yandex.Metrica Offline Events](</docs/destinations/reverse-etl-destinations/yandex-metrica-offline-events/>)[![Zoho logo](/docs/images/logos/destinations/zoho.svg)Zoho](</docs/destinations/reverse-etl-destinations/zoho/>)[![X Audience logo](/docs/images/logos/destinations/twitter.svg)X Audience](</docs/destinations/reverse-etl-destinations/x-audience/>)