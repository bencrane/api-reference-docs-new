# Google Ads Offline Conversions Destination Setup Guide Beta

Set up Google Ads Offline Conversions as a destination in RudderStack.

* * *

  * __6 minute read

  * 


This guide will help you set up Google Ads Offline Conversions as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Google Ads Offline Conversions.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Google Ads Offline Conversions** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), set up a source.
  2. Go to the **Overview** tab of your source and select **Add Destination** > **Create new destination**.

[![Add new destination in RudderStack dashboard](/docs/images/event-stream-destinations/add-new-destination.webp)](</docs/images/event-stream-destinations/add-new-destination.webp>)

  3. Select **Google Ads Offline Conversions** from the list of destinations. Then, click **Continue**.


## Account settings

To successfully configure Google Ads Offline Conversions as a destination, first authenticate your account by following these steps:

  1. Click **Create Account** in the **Account Settings** section.
  2. Under **Connect a new account** , select **OAuth** and click **Next**.
  3. Specify the account name and click **Connect account**.

[![Google Ads Account authentication](/docs/images/event-stream-destinations/gaoc/gaoc-account-name.webp)](</docs/images/event-stream-destinations/gaoc/gaoc-account-name.webp>)

  4. Choose the required Google Ads account and grant RudderStack the required permissions.


> ![warning](/docs/images/warning.svg)
> 
> **Important: Google Ads permissions**
> 
> To authenticate successfully, your Google Ads user permissions must be at least **Standard** or **Admin**.
> 
> Note that:
> 
>   * If you authorize the integration without the **Standard** or **Admin** permissions, the API calls will fail and a “RudderStack Admin” user will disable the integration.
>   * If you encounter an entry in your [audit logs](<https://www.rudderstack.com/docs/dashboard-guides/audit-logs/>) from a `Rudder Admin/admin@rudderstack.com` user, it means that RudderStack disabled the integration on account of insufficient user permissions. To avoid this, ensure that the authorizing user has the **Standard** permissions, at minimum.
> 


If you have authenticated multiple accounts, click the meatballs menu (`...`) and click **Switch account** to switch to the required account.

[![Google Ads Offline Conversions switch accounts](/docs/images/event-stream-destinations/gaoc/gaoc-switch-accounts.webp)](</docs/images/event-stream-destinations/gaoc/gaoc-switch-accounts.webp>)

> ![warning](/docs/images/warning.svg)
> 
> RudderStack gives an error if you try to delete an account used by any other connection set up for the same destination.

## Connection settings

Setting| Description  
---|---  
Name| Assign a name to uniquely identify the destination in RudderStack.  
Customer ID| Enter the ID associated with your Google Ads account.  
  
See FAQ for more information on obtaining your customer ID.  
Subaccount| Turn on this setting if you are using a Google Ads subaccount (subaccount of a manager account).  
  
See the [Google Ads](<https://support.google.com/campaignmanager/answer/2829448?hl=en#zippy=%2Cwhat-are-subaccounts>) documentation for more information on subaccounts.  
Login Customer ID| This setting is activated if you toggle on the **Subaccount** setting. Specify the customer ID of the manager account.  
  
See the [Google Ads Help guide](<https://support.google.com/google-ads/thread/1467498/where-can-i-find-the-customer-id-for-my-mcc-account?hl=en>) for more information on obtaining this ID.  
  
## Event settings

Setting| Description  
---|---  
Map your events with Google Ads Offline Conversions| Enter the RudderStack event name you want to map to the **Click** , **Call** , or **Store** conversion type in Google Ads.  
  


> ![warning](/docs/images/warning.svg)To successfully deliver events to Google Ads Offline Conversions, you must configure the event mappings via this setting.  
>   
> See the [Cloud Mode Integration](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-ads-offline-conversions/cloud-mode/>) guide for detailed mapping instructions.  
  
Map your Google Ads Conversions Names| Enter the RudderStack event name corresponding to the Google Ads Conversion name created in the Google Ads dashboard.  
  
See FAQ for more information on creating click and call conversions in Google Ads dashboard.  
Map your variable names to custom Google Ads variables| Enter the `track` event property to map to the Google Ads custom variable (defined in the Google dashboard).  
  
See FAQ for more information.  
User Identifier Source| Select the type of user identifier source from the dropdown. RudderStack provides the following options:  
  


  * **None**
  * **UNSPECIFIED**
  * **UNKNOWN**
  * **FIRST_PARTY**
  * **THIRD_PARTY**

  
Conversion Environment| Select the conversion environment of the uploaded conversion from the dropdown. RudderStack provides the following options:  
  


  * **None**
  * **UNSPECIFIED**
  * **UNKNOWN**
  * **APP**
  * **WEB**

  
The user identifier for store and click conversions| Select the default user identifier from **Email** or **Phone Number** for store and click conversions.  
Hash User Identifying Information (SHA-256)| This setting is turned on by default and hashes the user identifying information like email and phone number using SHA-256.  
Validate Only| Turn on this setting to only validate the request and not execute it.  
  
## Next steps

After setting up your Google Ads Offline Conversions destination in RudderStack:

  * See the [Google Ads Offline Conversions Cloud Mode Integration](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-ads-offline-conversions/cloud-mode/>) guide to understand how RudderStack maps and sends events to Google Ads Offline Conversions
  * Send test events to verify your setup is working correctly


## FAQ

#### Where can I find my Google Ads customer ID?

The Google Ads customer ID is a unique number used to identify your Google Ads account. To get this ID:

  1. Sign in to your [Google Ads account](<https://ads.google.com/home/>).
  2. Click your profile picture in the top right corner — the customer ID is listed under **Account Information**.


See the [Google Ads Help Center](<https://support.google.com/google-ads/answer/1704344?hl=en>) for more information on finding your Google Ads customer ID.

#### What are the account permissions required for this integration?

For the integration to be successful, make sure the customer account used for OAuth verification has **Standard** or higher (**Administrative**) access level permissions.

For more information on the access level permissions, refer to this [Google Ads support page](<https://support.google.com/google-ads/answer/9978556?visit_id=637611563637058259-4176462731&rd=1>).

To set the access level, follow these steps:

  1. Log in to your [Google Ads account](<https://ads.google.com/intl/en_IN/home/>).
  2. In the left navigation bar, click **Admin** > **Access and security**.
  3. Click the **+** symbol. Then, enter the email address of the account and from the list of permissions, select **Standard** or **Administrative**.

[![Specifying access levels](/docs/images/event-stream-destinations/gaoc/ga-access-security.webp)](</docs/images/event-stream-destinations/gaoc/ga-access-security.webp>)

  4. Click **Send invitation**.


The account will have the access level permissions once they accept the invitation.

#### How do I create custom variables in Google Ads dashboard? Which event properties can I map with these variables?

To create custom variables in Google Ads:

  1. Log in to your [Google Ads account](<https://ads.google.com/intl/en_IN/home/>).
  2. Click **Goals** in the left sidebar and select **Custom variables**.
  3. In **Custom Variables** section, click the **+** sign to create a new conversion custom variable:

[![Google Ads Offline Conversions custom variables](/docs/images/event-stream-destinations/gaoc/gaoc-custom-variable.webp)](</docs/images/event-stream-destinations/gaoc/gaoc-custom-variable.webp>)

You can map a `track` event property with a Google Ads custom variable. Suppose you send the following `track` payload to Google Ads via RudderStack:
    
    
    {
      "type": "track",
      ...
      "properties": {
        "gclid": "Cj0KCQjw6cKiBhD5ARIsAKXUdybqN7DV7ZFBelg7XMLZO-L1gCEXebkKQ7M73tQOdVNsxI_74J2grtIaAlRLEALw_wcB",
        "gbraid": null,
        "wbraid": null,
        "orderId": 1108829,
        "planName": "rudderstackTestingPlan",
        "orderUUID": "deaf39a0-c1ff-4e0d-aa6e-770deee66e85",
        "planPeriod": 0,
        "currencyCode": "USD",
        "conversionName": "annualized_revenue",
        "conversionValue": 70,
        "conversionDateTime": "2023-05-08 23:07:34+00:00"
      },
      "anonymousId": "deaf39a0-c1ff-4e0d-aa6e-770deee66e85"
    }
    

To send `planName` as a custom variable to Google Ads, create a custom variable in Google Ads dashboard, for example, `Plan Name`:

[![Google Ads Offline Conversions custom variable example](/docs/images/event-stream-destinations/gaoc/gaoc-custom-variable-example.webp)](</docs/images/event-stream-destinations/gaoc/gaoc-custom-variable-example.webp>)

Then, enter the following mapping in the **Map your variable names to custom Google Ads variables** RudderStack dashboard setting: `planName` → `Plan Name`

#### How to create the click and call conversions in Google Ads?

To create the click and call conversions in Google Ads:

  1. Log in to your [Google Ads account](<https://ads.google.com/intl/en_IN/home/>).
  2. In the left sidebar, click the **Create** (**+**) option and select **Conversion action**.

[![New conversion action in Google Ads dashboard](/docs/images/event-stream-destinations/gaoc/gaoc-new-conversion-action.webp)](</docs/images/event-stream-destinations/gaoc/gaoc-new-conversion-action.webp>)

  3. Under **Where do you want to measure conversions** , select **Conversions offline** and click **Add data source**.

[![Add data source in Google Ads dashboard](/docs/images/event-stream-destinations/gaoc/gaoc-add-data-source.webp)](</docs/images/event-stream-destinations/gaoc/gaoc-add-data-source.webp>)

  4. Under **Data source** , click **Skip this step and set up a data source later**. Also, make sure to enable the consent and data policies under **Customer data**.

[![Add data source later option](/docs/images/event-stream-destinations/gaoc/gaoc-add-data-later.webp)](</docs/images/event-stream-destinations/gaoc/gaoc-add-data-later.webp>)

  5. Select the conversion category from the list. Then, click **Save and continue**.
  6. Click **Edit settings** for the conversion action and specify settings like the conversion name, value, count, conversion window, etc. Then, click **Done** to save the settings.

[![Conversion settings in Google Ads dashboard](/docs/images/event-stream-destinations/gaoc/gaoc-conversion-settings.webp)](</docs/images/event-stream-destinations/gaoc/gaoc-conversion-settings.webp>)

  7. Set up your data source to finish the configuration.

[![Finalize conversion settings in Google Ads dashboard](/docs/images/event-stream-destinations/gaoc/gaoc-finish-setup.webp)](</docs/images/event-stream-destinations/gaoc/gaoc-finish-setup.webp>)

#### Why am I getting a 400 Bad Request error message while configuring the destination?

If you get a 400 Bad Request error while configuring the destination, make sure your customer account is allowlisted and configured to have **Standard** or **Administrative** access levels in Google Ads.

See the Google Ads Offline Conversions Account Settings section for steps on setting the required access level permissions for the account.