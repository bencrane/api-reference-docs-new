# Google Ads Remarketing Lists Setup Guide

Send your event data from RudderStack to Google Ads Remarketing Lists.

* * *

  * __3 minute read

  * 


This guide will help you set up Google Ads Remarketing Lists as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Google Ads Remarketing Lists.

## Prerequisites: Google Ads permissions

This integration relies on the authorizing Google Ads user’s [underlying permissions](<https://support.google.com/google-ads/answer/9978556>).

Note that the API calls to Google Ads will fail if you authorize this integration without the **Standard** or **Admin** permissions.

## Setup

  1. Set up a [Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) in the RudderStack dashboard.
  2. In the **Overview** tab, click **Add destination** > **Create new destination**.

[![Connect new destination to Reverse ETL source](/docs/images/reverse-etl-destinations/add-destination.webp)](</docs/images/reverse-etl-destinations/add-destination.webp>)

  3. From the list of destinations, search for **Google Ads Remarketing Lists (Customer Match)** and click **Continue**.


### Connection settings

Setting| Description  
---|---  
Name| Specify a unique name to identify the destination in RudderStack.  
oAuth settings| 

  1. Click **Create Account** > **Sign in with Google** and give RudderStack the required permissions to access your Google Ads account.
  2. Select the account and click **Save**.

  
Customer ID| Enter the Customer ID associated with your Google Ads account. You can find it by clicking on the **Help** option in your Google Ads dashboard.  
  
See this [guide](<https://support.google.com/google-ads/answer/1704344?hl=en>) for more information on obtaining the customer ID.  
Subaccount| Turn on this setting if you are using a Google Ads subaccount.  
  
**Note** : See this [guide](<https://support.google.com/campaignmanager/answer/2829448?hl=en#zippy=%2Cwhat-are-subaccounts>) for more information on subaccounts in Campaign Manager 360.  
Login customer ID| If **Subaccount** is toggled on, enter the customer ID of the parent account associated with the subaccount. This field is required only when you want to send data to a customer list of a subaccount.  
  
## Next steps

  * [Connect Reverse ETL source to Google Ads Remarketing Lists](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/google-ads-remarketing-lists/connect-retl-source/>)


## FAQ

#### How do I create a Google Ads customer list?

  1. Open your Google Ads account.
  2. Go to **Tools and settings**.
  3. Under **Shared Library** , go to **Audience Manager**.
  4. Click the + button and select **Customer list**.
  5. Under **Segment name** , assign a name to the list.
  6. From the dropdown, select the list type of data to upload.
  7. Upload the CSV containing the user data. You can also download the template and upload the data.
  8. Click **UPLOAD AND CREATE**.


#### Where can I find my Google Ads customer ID?

The Google Ads customer ID is a unique number used to identify your Google Ads account. To get this ID:

  1. Sign in to your [Google Ads account](<https://ads.google.com/home/>).
  2. Click your profile picture in the top right corner — the customer ID is listed under **Account Information**.


See the [Google Ads Help Center](<https://support.google.com/google-ads/answer/1704344?hl=en>) for more information on finding your Google Ads customer ID.

#### Can I set up the Enhanced Conversions and Remarketing Lists destinations using the same Google Ads account?

Yes, you can. As both the integrations are Google Ads features, it is possible to use the same Google Ads account to configure both the Enhanced Conversions and Remarketing Lists destinations in RudderStack.

#### What are the account permissions required for the Google Ads Remarketing Lists integration?

Make sure the customer account used for OAuth verification adheres to Google’s [Customer Match policy](<https://support.google.com/google-ads/answer/6299717>) and has **Standard** or higher (**Administrative**) access level permissions.

For more information on the access level permissions, refer to this [Google Ads support page](<https://support.google.com/google-ads/answer/9978556?visit_id=637611563637058259-4176462731&rd=1>).

Follow these steps to set the access level:

  1. Sign into to your Google Ads account and go to **TOOLS AND SETTINGS** > **Access and security** :

[![Access and Security option in Google Ads dashboard](/docs/images/event-stream-destinations/gads-access-security.webp)](</docs/images/event-stream-destinations/gads-access-security.webp>)

  2. Enter the email address of the account. From the list of permissions, select **Standard** or **Administrative**. Then, click **SEND INVITATION** :

[![Specifying access levels](/docs/images/event-stream-destinations/gads-specify-access-level.webp)](</docs/images/event-stream-destinations/gads-specify-access-level.webp>)

The account will have the required access-level permissions once they accept the invitation.

#### Why am I getting a 400 Bad Request error message while setting up the Google Ads Remarketing Lists destination?

If you get a 400 Bad Request error while configuring the destination, make sure your customer account is allowlisted and configured to have **Standard** or **Administrative** access levels in Google Ads.

See the above FAQ for steps on setting the access level permissions for the account.