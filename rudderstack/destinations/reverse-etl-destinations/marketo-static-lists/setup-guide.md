# Setup Guide Beta

Set up and configure Marketo Static Lists as a destination in RudderStack.

* * *

  * __2 minute read

  * 


This guide will help you set up Marketo Static Lists as a destination in RudderStack. It also lists the configuration settings required to correctly send data from the supported sources to Marketo Static Lists.

## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Marketo Static Lists**.

### Connection settings

Setting| Description  
---|---  
Munchkin Account ID| Enter your Munchkin account ID.  
Client ID| Enter your Marketo client ID.  
Client Secret| Enter the client secret for the above ID.  
Static List ID| Enter your Marketo static list ID. RudderStack uses this ID to add or remove leads from the specific list.  
  
## Next steps

  * [Connect Reverse ETL source to Marketo Static Lists](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/marketo-static-lists/connect-retl-source/>)


## FAQ

#### Where can I find my Munchkin account ID?

  1. Log in to your Marketo instance.
  2. Go to **Admin** > **Integration** > **Munchkin**.


Your Munchkin ID is listed on the main screen in the **Tracking Code** section:

[![Marketo Munchkin ID](/docs/images/event-stream-destinations/marketo-munchkin-id.webp)](</docs/images/event-stream-destinations/marketo-munchkin-id.webp>)

See the [Marketo documentation](<https://nation.marketo.com/t5/knowledgebase/how-to-find-your-munchkin-id-for-a-marketo-instance/ta-p/248432>) for more information on the Munchkin ID.

#### How do I obtain the Marketo client ID and secret?

To set up the Marketo API service and obtain the client ID and secret associated with it, follow these steps:

  1. Log in to your Marketo instance and click the **Admin** tab.
  2. Select **LaunchPoint**.

[![](/docs/images/event-stream-destinations/marketo-launchpoint.webp)](</docs/images/event-stream-destinations/marketo-launchpoint.webp>)

  3. Here, you will see all the installed services used for connecting to Marketo.

[![](/docs/images/event-stream-destinations/marketo-services.webp)](</docs/images/event-stream-destinations/marketo-services.webp>)

  4. To create a new service, click **New** > **New Service**.
  5. Enter the **Display Name**. From the **Service** dropdown, select **Custom**.
  6. Under **Settings** , enter the **Description** and select the **API Only User**. Finally, click **CREATE**.


> ![warning](/docs/images/warning.svg)
> 
> Make sure the **API Only User** associated with the API service has the necessary permissions to create or update contacts and custom activities.

Once the setup is complete, you should have the client ID and client secret for the API service.

[![](/docs/images/event-stream-destinations/marketo-service-details.webp)](</docs/images/event-stream-destinations/marketo-service-details.webp>)

#### Where can I find the Marketo static list ID?

  1. Log in to your Marketo instance.
  2. Go to the **Database** tab.
  3. Create a new [static list](<https://experienceleague.adobe.com/docs/marketo/using/product-docs/core-marketo-concepts/smart-lists-and-static-lists/static-lists/create-a-static-list.html?lang=en>).
  4. Open the static list. You can find the list ID in the resulting URL, as shown:

[![Marketo static list ID](/docs/images/event-stream-destinations/marketo-static-list-id.webp)](</docs/images/event-stream-destinations/marketo-static-list-id.webp>)

For example, if the static list URL is `https://engage-ab.marketo.com/?munchkinId=123-AXP-456#/classic/ST1234A1`, then the static list ID is `1234`.