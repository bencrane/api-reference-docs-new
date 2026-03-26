# Setup Guide Beta

Set up and configure Klaviyo Bulk Upload as a destination in RudderStack.

* * *

  * __2 minute read

  * 


This guide will help you set up Klaviyo Bulk Upload as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Klaviyo.

## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Klaviyo Bulk Upload**.

### Connection settings

Setting| Description  
---|---  
Name| Assign a name to uniquely identify your destination in RudderStack.  
Private API Key| Enter the Klaviyo private API key by navigating to **Settings** > **API Keys**.  
  


> ![warning](/docs/images/warning.svg)The private API key must have the necessary permissions (`profiles:write` and `lists:write` scopes) to send the data successfully.  
  
### Configuration settings

Setting| Description  
---|---  
List ID| Enter the default list ID to which you want to add and subscribe users.  
  
## Next steps

  * [Connect Reverse ETL source to Klaviyo Bulk Upload](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/klaviyo-bulk-upload/connect-retl-source/>)


## FAQ

#### Which permissions are needed to send data to the Klaviyo Bulk Upload destination correctly?

For bulk import jobs in Klaviyo, you need to create a private API key with the following scopes:

  * `profiles:write`
  * `lists:write`


Follow these steps to create a new private API key with the above scopes:

  1. Go to **Settings** > **API Keys**.
  2. Click **Create Private API Key**.
  3. Name the key and choose the **Custom Key** option from the access level options.
  4. Select **Read/Write Access** for the **List** and **Profiles** API scopes.

[![](/docs/images/event-stream-destinations/klaviyo-custom-private-api-key.webp)](</docs/images/event-stream-destinations/klaviyo-custom-private-api-key.webp>)

  5. Click **Create**.
  6. Specify this key in the Private API key setting.