# Setup Guide Beta

Set up and configure Bing Ads Offline Conversions as a destination in RudderStack.

* * *

  * __2 minute read

  * 


This guide will help you set up Bing Ads Offline Conversions as a destination in RudderStack. It also lists the configuration settings required to correctly send data from the supported sources to Bing Ads Offline Conversions.

## Prerequisites

Before setting up Bing Ads Offline Conversions in your RudderStack dashboard, make sure to set up an [OfflineConversion](<https://learn.microsoft.com/en-us/advertising/campaign-management-service/offlineconversion?view=bingads-13>) in your [Microsoft Advertising dashboard](<https://developers.ads.microsoft.com/Account>).

Also, note the following while setting up your [OfflineConversionGoal](<https://learn.microsoft.com/en-us/advertising/campaign-management-service/offlineconversiongoal?view=bingads-13>):

  * If you set [`CountType`](<https://learn.microsoft.com/en-us/advertising/campaign-management-service/offlineconversiongoal?view=bingads-13#counttype>) to `All`, then all offline conversions for a given `MicrosoftClickId` with different conversion times are added cumulatively.
  * If you set the `CountType` field to `Unique` (**recommended**), then only the first conversion that happens after an ad click is counted. Duplicate conversions with the same `MicrosoftClickId` and `ConversionTime` are ignored.


## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Bing Ads Offline Conversions**.

### Connection settings

Setting| Description  
---|---  
Name| Assign a name to uniquely identify your destination in RudderStack.  
Customer Account ID| Enter your Bing Ads account ID.  
Customer ID| Enter your Bing Ads customer ID.  
  
## Next steps

  * [Connect Reverse ETL source to Bing Ads Offline Conversions](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/bing-ads-offline-conversions/connect-retl-source/>)


## FAQ

#### Where can I find my Bing Ads customer ID and customer account ID?

To get your Bing Ads customer ID and account ID, sign in to your Microsoft Advertising web app and click the **Campaigns** tab. The URL contains a `cid` key/value pair in the query string that contains the customer ID and an `aid` key/value pair that identifies your account ID.

A sample URL is shown:
    
    
    https://ui.ads.microsoft.com/campaign/Campaigns.m?cid=<CUSTOMER_ID>
    &aid=<ACCOUNT_ID>#/customer/<CUSTOMER_ID>/account/<ACCOUNT_ID>/campaign.
    

#### Why am I getting the “AADSTS650052” error when authenticating to Microsoft Advertising?

If you encounter the following error while authenticating to Microsoft Advertising:
    
    
    Error Code: AADSTS650052
    Error Message: "The app is trying to access a service that your organization lacks a service principal for."
    

This issue commonly occurs when you sign in using a work or school account that belongs to an Azure AD-managed domain. Organizational accounts may have restrictions that prevent RudderStack from completing the authentication.

To resolve this issue, consider using a personal Microsoft account, for example, emails having `@outlook.com`, `@hotmail.com`, or `@live.com` domains.