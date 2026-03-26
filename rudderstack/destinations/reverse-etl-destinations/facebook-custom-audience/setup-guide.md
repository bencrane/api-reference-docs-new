# Setup Guide

Send your event data from RudderStack to Facebook Custom Audience.

* * *

  * __4 minute read

  * 


This guide will help you set up Facebook Custom Audience as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Facebook Custom Audience.

> ![info](/docs/images/info.svg)
> 
> Make sure you have already set up a [Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) in RudderStack before following the steps in this guide.

## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **Facebook Custom Audience**.

### Connection settings

Configure the following settings to set up Facebook Custom Audience as a destination in RudderStack:

Setting| Description  
---|---  
Name| Specify a unique name to identify the destination in RudderStack.  
Access Token| Enter the access token of your business application set up for accessing the Facebook Marketing API.  
Ad Account ID| Enter the Ad Account ID of your business application.  
  
## Next steps

  * [Connect Reverse ETL source to Facebook Custom Audience](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/facebook-custom-audience/connect-retl-source/>)


## Configuration settings

Once you have [specified the mappings](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/facebook-custom-audience/connect-retl-source/>), configure the below advanced settings to receive the data correctly in Facebook Custom Audience:

Setting| Description  
---|---  
App Secret| Enter the [app secret](<https://developers.facebook.com/docs/facebook-login/security/#appsecret>) from the **Basic app settings** page of your [Facebook Developer account](<https://developers.facebook.com/>).  
  
## FAQ

#### What are the prerequisites for creating an audience list?

Before creating a new audience list, make sure that:

  * You are an [admin system user](<https://en-gb.facebook.com/business/help/327596604689624?id=2190812977867143>). To check, go to **Users** > **System users** in your [Facebook business](<https://business.facebook.com/>) account.

[![Facebook Ads system user](/docs/images/event-stream-destinations/fb-system-user.webp)](</docs/images/event-stream-destinations/fb-system-user.webp>)

  * The ad account under which the audience list is created should be added as an asset for the system user, with manage permissions.
  * The app for which you are creating the access token should be added as an asset of the system user with full control.


#### How do I add an app as a system user asset with manage permissions?

  1. Log in to your [Facebook Business Manager](<https://business.facebook.com/>) account.
  2. Click **Business settings**.

[![Business Settings](/docs/images/event-stream-destinations/fb-custom-audience-business-settings.webp)](</docs/images/event-stream-destinations/fb-custom-audience-business-settings.webp>)

  3. Under **Users** , click **System users**.

[![System users setting](/docs/images/event-stream-destinations/fb-custom-audience-system-users.webp)](</docs/images/event-stream-destinations/fb-custom-audience-system-users.webp>)

  4. Choose the system user from the opened list.
  5. Click **Add Assets** for the above user.

[![Add Assets option](/docs/images/event-stream-destinations/fb-custom-audience-add-assets.webp)](</docs/images/event-stream-destinations/fb-custom-audience-add-assets.webp>)

  6. Under **Select asset type** , click **Apps** and choose your app from the **Select assets** tab.

[![Asset type](/docs/images/event-stream-destinations/fb-custom-audience-asset-type.webp)](</docs/images/event-stream-destinations/fb-custom-audience-asset-type.webp>)

  7. In the right-most **App** tab, enable the **Manage app** setting. Then, click **Save Changes**.

[![Manage app setting](/docs/images/event-stream-destinations/fb-custom-audience-manage-app.webp)](</docs/images/event-stream-destinations/fb-custom-audience-manage-app.webp>)

#### How do I create a new audience list?

  1. Log in to your [Facebook business](<https://business.facebook.com/>) account.
  2. Click **All tools** in the left panel.

[![Facebook custom audience creation](/docs/images/event-stream-destinations/fb-custom-audience-2.webp)](</docs/images/event-stream-destinations/fb-custom-audience-2.webp>)

  3. Hover over **Create Audience** and select **Custom Audience**.

[![Facebook custom audience creation](/docs/images/event-stream-destinations/fb-custom-audience-3.webp)](</docs/images/event-stream-destinations/fb-custom-audience-3.webp>)

  4. Select **Customer List** and click **Next**.

[![Facebook custom audience creation](/docs/images/event-stream-destinations/fb-custom-audience-4.webp)](</docs/images/event-stream-destinations/fb-custom-audience-4.webp>)

  5. Prepare your customer list by selecting and mapping the identifiers. Make sure you have enough identifiers before uploading the list.

[![Facebook custom audience creation](/docs/images/event-stream-destinations/fb-custom-audience-5.webp)](</docs/images/event-stream-destinations/fb-custom-audience-5.webp>)

  6. Upload the CSV file you want to use for your new custom audience. Under the **Does your list include a column for customer value?** setting, make sure to select **No, continue with a customer list that doesn’t include customer value**.


> ![info](/docs/images/info.svg)
> 
> You can also download the file template CSV and upload it.

[![Facebook custom audience add customer list](/docs/images/event-stream-destinations/fb-custom-audience-add-customer-list.webp)](</docs/images/event-stream-destinations/fb-custom-audience-add-customer-list.webp>)

  7. Finally, click **Import and create** to create the audience.


> ![warning](/docs/images/warning.svg)
> 
> The custom audience you create should have edit permissions. Otherwise, RudderStack will not be able to add or remove users from the list.

#### How do I check if the custom audience has edit permissions?

To check if the audience has edit permissions enabled, go to the **Audiences** tab, select your custom audience, and check the **Actions** dropdown. You should see the **Edit** option as seen below:

[![Customer audience edit permissions](/docs/images/event-stream-destinations/fb-custom-audience-edit-permissions.webp)](</docs/images/event-stream-destinations/fb-custom-audience-edit-permissions.webp>)

#### How do I obtain the Ad Account ID?

Go to your Facebook [Ads Manager account](<https://www.facebook.com/adsmanager/manage/>) where you can find the Ad Account ID in the account’s drop-down menu:

[![Audience source](/docs/images/event-stream-destinations/ads-account-id-fb.webp)](</docs/images/event-stream-destinations/ads-account-id-fb.webp>)

You can click on **See More Ad Accounts** if the required Ad account is not visible.

#### Where can I find the user Access Token for the application?

> ![warning](/docs/images/warning.svg)
> 
> To generate the user access token for your application, you must first add it as a system user asset with manage permissions.

Follow these steps to generate a user access token required to use the Facebook Marketing API:

  1. Under the system user, click the **Generate New Token** button and select the app from the dropdown.

[![Generate new token](/docs/images/event-stream-destinations/fb-custom-audience-generate-new-token.webp)](</docs/images/event-stream-destinations/fb-custom-audience-generate-new-token.webp>)[![Select app for the token](/docs/images/event-stream-destinations/fb-custom-audience-token-select-app.webp)](</docs/images/event-stream-destinations/fb-custom-audience-token-select-app.webp>)

  2. Choose the **Token expiration** time.

[![Token settings](/docs/images/event-stream-destinations/fb-custom-audience-token-settings.webp)](</docs/images/event-stream-destinations/fb-custom-audience-token-settings.webp>)

  3. Under **Available permissions** , select `ads_read` and `ads_management`.


[![Token permissions](/docs/images/event-stream-destinations/fb-custom-audience-available-permissions-1.webp)](</docs/images/event-stream-destinations/fb-custom-audience-available-permissions-1.webp>)[![Token permissions](/docs/images/event-stream-destinations/fb-custom-audience-available-permissions-2.webp)](</docs/images/event-stream-destinations/fb-custom-audience-available-permissions-2.webp>)

  4. Click the **Generate Token** button and copy the token credentials.


#### Should I use `sessionIdAdd` or `sessionIdDelete` before adding or removing users in Custom Audience?

`sessionIdAdd` and `sessionIdDelete` helps you track and use a particular session ID while adding or removing users. This is useful when you are sending data in chunks. If you do not include these fields, Facebook creates a session ID itself.

See the [Facebook documentation](<https://developers.facebook.com/docs/marketing-api/audiences/guides/custom-audiences#step-2--specify-a-list-of-users>) for more information.