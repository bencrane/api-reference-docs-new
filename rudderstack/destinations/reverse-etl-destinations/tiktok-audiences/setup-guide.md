# Setup Guide

Send your event data from RudderStack to TikTok Audiences.

* * *

  * __less than a minute

  * 


This guide will help you set up TikTok Audiences as a destination in RudderStack when connecting to a [Reverse ETL source](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/launchdarkly-segments/connect-retl-source/>).

> ![info](/docs/images/info.svg)
> 
> Make sure you have already set up a [Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) in RudderStack before following the steps in this guide.

## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **TikTok Audiences**.

### Connection settings

To successfully set up TikTok Audiences as a destination, configure the following settings:

  * **Account Settings** : Click **Create Account** > **Connect with TikTok Audience** and give RudderStack the required permissions to access your TikTok account.
  * **Enable Hashing** : This setting is enabled by default and hash encodes the user data in the SHA-256 format.


## `audienceList` event structure

The following code snippet shows a sample `audienceList` call made to TikTok after removing some common fields:
    
    
    {
      "type": "audiencelist",
      "event": "Add_Audience",
      "userId": "2TVX1ChyqWl25rU15MCDUPsOxYD-2WsebOFmeLuduTyc3RTVtRLqRsR",
      "externalId": [{
        "type": "TIKTOK_AUDIENCE-175960432",
        "identifierType": "AAID_MD5"
      }],
      "properties": {
        "listData": {
          "add": [{
            "AAID_MD5": 22
          }],
          "remove": [{
            "AAID_MD5": 21
          }]
        }
      }
    }