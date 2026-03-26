# Connect Reverse ETL Source to Criteo Audience

Configure a Reverse ETL source with your Criteo Audience destination.

* * *

  * __2 minute read

  * 


This guide takes you through the steps to connect a Reverse ETL source to the Criteo Audience destination. You can also create a new Audience Segmentor use an existing Audience Segment while setting up the connection.

## Connection setup

The below steps assume that you have already [set up a RETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) and chosen Criteo Audience as the corresponding destination.

  1. [Configure the connection settings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/criteo-audience/setup-criteo-audience/#connection-settings>) for Criteo Audience.
  2. Enter the **Advertiser ID** from your Criteo URL, where all the audiences are listed. For example, in this sample Criteo URL `https://marketing.criteo.com/audience-manager/list/audiences?advertiserId=1234`, the advertiser ID is `1234`.

[![](/docs/images/event-stream-destinations/criteo-advertiser-id.webp)](</docs/images/event-stream-destinations/criteo-advertiser-id.webp>)

  3. In the **Where do you want to sync data to?** section:

     * Select **Create New audience** to create a new Audience Segment (of type [Contact List](<https://developers.criteo.com/marketing-solutions/v2025.01/docs/audience-segments#contact-list>)) in Criteo. Specify the name and description of the audience in the respective fields.
[![](/docs/images/event-stream-destinations/fb-custom-audience-new.webp)](</docs/images/event-stream-destinations/fb-custom-audience-new.webp>)
     * Select **Use Existing Audience** if you have an existing Audience Segment (of type [Contact List](<https://developers.criteo.com/marketing-solutions/v2025.01/docs/audience-segments#contact-list>)) and specify the Audience Segment ID.
[![](/docs/images/event-stream-destinations/fb-custom-audience-existing.webp)](</docs/images/event-stream-destinations/fb-custom-audience-existing.webp>)
  4. Configure the remaining settings as required to set up the connection successfully.


If you have selected **Create New audience** option in Step 3, the new Audience Segment will be created for that particular advertiser ID with the same **Audience ID** as in the **Schema** tab of your Reverse ETL connection.

[![](/docs/images/retl-sources/audience-id.webp)](</docs/images/retl-sources/audience-id.webp>)

## Audience segment ID for using an existing audience

To use an existing audience from Criteo, make sure that it is created as a [Contact List Audience Segment](<https://developers.criteo.com/marketing-solutions/v2025.01/docs/audience-segments#contact-list>) and not directly in the dashboard. Follow these steps:

  1. Authenticate yourself by [generating an access token](<https://developers.criteo.com/marketing-solutions/docs/authentication#generate-an-access-token>) with your API credentials to use the Criteo API.
  2. Create a new [Contact List Audience Segment](<https://developers.criteo.com/marketing-solutions/docs/audience-segments#create-audience-segments>) by making a POST call.


The Criteo API returns a unique Audience Segment ID associated with the newly created Audience Segment. You can use this ID in the **Use Existing Audience** section in the RudderStack dashboard.