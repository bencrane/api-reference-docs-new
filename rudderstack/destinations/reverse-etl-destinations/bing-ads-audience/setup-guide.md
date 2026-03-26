# Bing Ads Audience Setup Guide Beta

Set up and configure Bing Ads Audience as a destination in RudderStack.

* * *

  * __3 minute read

  * 


This guide will help you set up Bing Ads Audience as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Bing Ads.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Cloud, Warehouse, Shopify
  * Refer to it as **BingAds Audience** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Bing Ads Audience, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Bing Ads Audience**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

Connection settings| Description  
---|---  
Account Settings| Click **Create Account** > **Connect with Bing Ads Audience** and give RudderStack the required permissions to access to your Bing Ads account.  
Customer Account ID| Enter your Bing Ads account identifier.  
Customer ID| Enter your Bing Ads customer ID.  
Audience ID| Enter your Bing Ads audience ID for which you want to sync the data.  
  


> ![info](/docs/images/info.svg)See FAQ for more information on obtaining the required credentials.  
  
Hash Email| This setting is on by default and hash-encrypts the email present in your event.  
  


> ![warning](/docs/images/warning.svg)Make sure to turn off this setting if you are already sending a hashed email in your event.  
  
## FAQ

#### Where can I find my Bing Ads customer ID and customer account ID?

To get your Bing Ads customer ID and account ID, sign in to your Microsoft Advertising web app and click the **Campaigns** tab. The URL contains a `cid` key/value pair in the query string that contains the customer ID and an `aid` key/value pair that identifies your account ID.

A sample URL is shown:
    
    
    https://ui.ads.microsoft.com/campaign/Campaigns.m?cid=<CUSTOMER_ID>&aid=
    <ACCOUNT_ID>#/customer/<CUSTOMER_ID>/account/<ACCOUNT_ID>/campaign.
    

#### Where can I find the Bing Ads audience ID?

To get your Bing Ads audience, go to **Tools** > **Audiences**.

[![Audiences option](/docs/images/event-stream-destinations/audiences-option.webp)](</docs/images/event-stream-destinations/audiences-option.webp>)

You will see the list of audiences with their corresponding **Audience ID**.

[![Audience ID](/docs/images/event-stream-destinations/bingads-audience-id.webp)](</docs/images/event-stream-destinations/bingads-audience-id.webp>)

#### How to create an audience in Bing Ads?

  1. Go to **Tools** > **Audiences**.

[![Create BingAds audience](/docs/images/event-stream-destinations/bingads-2.webp)](</docs/images/event-stream-destinations/bingads-2.webp>)

  2. Click **Create** to create the new audience.

[![Create BingAds audience](/docs/images/event-stream-destinations/bingads-3.webp)](</docs/images/event-stream-destinations/bingads-3.webp>)

  3. Name the audience, select **Customer match list** as the audience type and click **Next**.

[![Create BingAds audience](/docs/images/event-stream-destinations/bingads-4.webp)](</docs/images/event-stream-destinations/bingads-4.webp>)

  4. Choose **hashed file** , download a specimen template and upload the same by clicking on **Browse**.

[![Create BingAds audience](/docs/images/event-stream-destinations/bingads-5.webp)](</docs/images/event-stream-destinations/bingads-5.webp>)

  5. Accept the terms and conditions, choose membership duration as **No expiration** and sharing field according to your access levels.

[![Create BingAds audience](/docs/images/event-stream-destinations/bingads-6.webp)](</docs/images/event-stream-destinations/bingads-6.webp>)

  6. Finally, click **Apply changes** to create the audience successfully.

[![Create BingAds audience](/docs/images/event-stream-destinations/bingads-7.webp)](</docs/images/event-stream-destinations/bingads-7.webp>)

#### Why am I getting the “AADSTS650052” error when authenticating to Microsoft Advertising?

If you encounter the following error while authenticating to Microsoft Advertising:
    
    
    Error Code: AADSTS650052
    Error Message: "The app is trying to access a service that your organization lacks a service principal for."
    

This issue commonly occurs when you sign in using a work or school account that belongs to an Azure AD-managed domain. Organizational accounts may have restrictions that prevent RudderStack from completing the authentication.

To resolve this issue, consider using a personal Microsoft account, for example, emails having `@outlook.com`, `@hotmail.com`, or `@live.com` domains.