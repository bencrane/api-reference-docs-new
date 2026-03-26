# Connect Reverse ETL Source to TikTok Audiences

Configure a Reverse ETL source with your TikTok Audiences destination.

* * *

  * __2 minute read

  * 


This guide takes you through the steps to connect a Reverse ETL source to the TikTok Audiences destination.

## Set up the connection

> ![warning](/docs/images/warning.svg)
> 
> **The Reverse ETL feature supports only source-driven pipeline configuration.**
> 
> Make sure you have [set up a Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and connected it to your TikTok Audiences destination before following the below steps.

  1. [Confirm the connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/launchdarkly-segments/setup-guide/#connection-settings>) for TikTok Audiences destination and click **Continue**.

  2. In the **Where do you want to sync data to?** section:

     * Select **Create New audience** if you want to create a new audience in TikTok. Specify the name and description of the audience in the respective fields.
[![](/docs/images/event-stream-destinations/fb-custom-audience-new.webp)](</docs/images/event-stream-destinations/fb-custom-audience-new.webp>)
     * Select **Use Existing Audience** if you have an existing audience in TikTok and specify the [Audience ID](<>).
[![](/docs/images/event-stream-destinations/fb-custom-audience-existing.webp)](</docs/images/event-stream-destinations/fb-custom-audience-existing.webp>)
  3. Set the [Sync mode](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-modes/>) to specify how RudderStack should sync the data to TikTok Audiences.

  4. In **Choose identifier** , specify the warehouse column that RudderStack uses to identify your records.

  5. Map your warehouse columns to specific TikTok fields using the **Map fields** setting.


[![](/docs/images/event-stream-destinations/tiktok-audience-identifier-map-fields.webp)](</docs/images/event-stream-destinations/tiktok-audience-identifier-map-fields.webp>)

If you have selected **Create New audience** option in Step 2, the new audience will be created in the destination for that particular advertiser ID with the same **Audience ID** as in the **Schema** tab of your Reverse ETL connection.

[![](/docs/images/retl-sources/audience-id.webp)](</docs/images/retl-sources/audience-id.webp>)

## Supported mappings

You can map your warehouse columns to the following TikTok fields:

  * `IDFA_MD5`: MD5 hash of an iOS IDFA.
  * `AAID_MD5`: MD5 hash of an Android AAID/GAID.
  * `IDFA_SHA256`: SHA256 hash of an iOS IDFA.
  * `AAID_SHA256`: SHA256 hash of an Android AAID/GAID.
  * `EMAIL_SHA256`: SHA256 hash of email ID. See [Important Notes for Streaming API- Email Specific Normalization](<https://business-api.tiktok.com/portal/docs?id=1739566528222210>) section for more information.
  * `PHONE_SHA256`: SHA256 hash of a phone number in E.164 format, for example, `+1231234567`.


## FAQ

#### Why can’t I add a Reverse ETL source from the destination page?

The Reverse ETL feature supports only source-driven pipeline configuration. It means that you must configure a Reverse ETL source in RudderStack and then connect it to a new or existing destination. Note that this destination should not be connected to any other source.

See [Reverse ETL FAQ](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/faq/>) for more information.

#### How do I view the synced segments in TikTok?

To view the synced audience, go to your [TikTok Ads Manager](<https://ads.tiktok.com/i18n/home>) and go to **Tools** > **Audience manager**.

[![](/docs/images/event-stream-destinations/tiktok-ads-audiences.webp)](</docs/images/event-stream-destinations/tiktok-ads-audiences.webp>)

To see the sync status, check the **Availability** column.

[![](/docs/images/event-stream-destinations/tiktok-ads-sync-status.webp)](</docs/images/event-stream-destinations/tiktok-ads-sync-status.webp>)