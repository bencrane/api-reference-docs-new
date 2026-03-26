# Google Ads Enhanced Conversions (Cloud Mode)

Send your event data from RudderStack to Google Ads Enhanced Conversions.

* * *

  * __7 minute read

  * 


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** **Choose the right Google Ads destination**
> 
> RudderStack offers two Google Ads destinations that can support enhanced conversions:
> 
>   * Use this destination to send events in **cloud mode** (server-to-server integration) using the Google Ads API
>   * Use the [Google Ads (gtag.js)](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-ads/>) destination if you’re sending events in **web device mode** and want to enable enhanced conversions for your setup
> 


[Google Ads Enhanced Conversions](<https://developers.google.com/google-ads/api/docs/conversions/enhance-conversions>) lets you improve your conversion measurement accuracy by securely sending first-party conversion data from your website to Google.

RudderStack supports Google Ads Enhanced Conversions as a destination to which you can send your audience list.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Google Ads Enhanced Conversions** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
  
## Prerequisites

To use this destination correctly, you must:

  * [Set up Enhanced Conversions](<https://support.google.com/google-ads/answer/11062876>) with the Google Ads API.

  * Accept the Google Ads data terms to receive the enhanced conversions events successfully. To accept the terms:

    1. Log in to your Google Ads dashboard.
    2. Go to **Conversions** > **Settings** > **Customer Data Terms**.
    3. Carefully read and accept the customer data terms.

[![Google Ads Enhanced Conversions data terms](/docs/images/event-stream-destinations/g-ads-conversions-data-terms.webp)](</docs/images/event-stream-destinations/g-ads-conversions-data-terms.webp>)

## Get started

Once you have confirmed that the source platform supports sending events to Google Ads Enhanced Conversions, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Google Ads Enhanced Conversions**.
  2. Assign a name to your destination and click **Continue**.


### Connection settings

To successfully configure Google Ads Enhanced Conversions as a destination, first authenticate your account by following the below steps:

  1. Click **Create Account** in the **Account Settings** section.
  2. From the modal, click the **Sign in with Google** button.
  3. Choose the required account and grant RudderStack the required permissions.
  4. Click **Save** to use the specified account:

[![Google Account authentication](/docs/images/event-stream-destinations/cm-360-account-connect-normal.webp)](</docs/images/event-stream-destinations/cm-360-account-connect-normal.webp>)

> ![info](/docs/images/info.svg)
> 
> In case you have authenticated multiple accounts, you can click **Edit Credentials** to select or delete any other authenticated account:
> 
> ![Google Account authentication](/docs/images/event-stream-destinations/cm-360-edit-account-creds.webp)
> 
> RudderStack **gives an error** if you try to delete an account used by any other connection set up for the same destination.

Next, configure the following settings:

  * **Customer ID** : Enter the ID associated with your Google Ads account. You can find it by clicking the **Help** option in your dashboard. For more information on obtaining the customer ID, refer to the [Google Ads Help Center](<https://support.google.com/google-ads/answer/1704344?hl=en>) page.
  * **Subaccount** : Enable this setting if you are using a Google Ads subaccount. For more information on subaccounts, refer to the [Google Ads Help Center](<https://support.google.com/campaignmanager/answer/2829448?hl=en#zippy=%2Cwhat-are-subaccounts>) page.
  * **Login Customer ID** : Enter the customer ID of the manager account (associated with the subaccount). This field is required only when you want to send data to a customer list of a subaccount.
  * **List of Conversion** : Enter the list of events on which you want to perform enhanced conversions. RudderStack will discard any events that are not specified in this list.
  * **Hashing Required** : This setting is enabled by default and hash encrypts the user identifiers like email, phone number, first name, last name, and street address using the SHA256 encryption method.


## Google Ads permissions

This integration relies on the authorizing Google Ads user’s [underlying permissions](<https://support.google.com/google-ads/answer/9978556>) and must be at least **Standard** or **Admin**.

If you authorize the integration without the **Standard** or **Admin** permissions, the API calls will fail and a “RudderStack Admin” user will disable the integration. If you encounter an entry in your [audit logs](<https://www.rudderstack.com/docs/dashboard-guides/audit-logs/>) from a `Rudder Admin/admin@rudderstack.com` user, it means that RudderStack disabled the integration on account of insufficient user permissions.

To avoid this, ensure that the authorizing user has the **Standard** permissions, at minimum.

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record and send the conversion events along with any properties associated with them. RudderStack uses the [`ConversionAdjustment`](<https://developers.google.com/google-ads/api/reference/rpc/v12/ConversionAdjustment>) method to send the `track` events to Google Ads.

> ![info](/docs/images/info.svg)
> 
> You must create the [conversion actions](<https://support.google.com/google-ads/answer/12216226?hl=en>) in Google Ads before sending the associated conversion events from RudderStack. Also, the conversion names should match in Rudderstack (**List of Conversion** dashboard setting) and Google Ads dashboards.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      checkout_id: "12345",
      orderId: "123",
      affiliation: "Apple Store",
      gclid: "abcd1234",
      conversionDateTime: "2019-01-01 12:32:45-08:00",
      adjustedValue: 100,
      currencyCode: "INR",
      adjustmentDateTime: "2019-01-01 12:32:45-08:00",
      total: 20,
      revenue: 15.0,
      shipping: 22,
      tax: 1,
      discount: 1.5,
      coupon: "SAVE45",
      currency: "USD",
      products: [
        {
          product_id: "FS247",
          sku: "G-32",
          name: "Monopoly",
          price: 14,
          quantity: 1,
          category: "Games",
          url: "https://www.estore.com/product/funskool-monopoly",
        },
      ],
    })
    

> ![warning](/docs/images/warning.svg)
> 
> `orderId` is a required field to send a `track` call successfully.

### Supported mappings

The following table details the mapping of the fields specified in the RudderStack dashboard and Google Ads Enhanced Conversions, along with the relevant guidelines:

RudderStack field| Google Ads Enhanced Conversions field| Guidelines  
---|---|---  
`gclid`| `gclid`| This is the Google click ID associated with the original conversion.  
`conversionDateTime`| `conversionDateTime`| The datetime at which the conversion for the adjustment occurred. You must specify the timezone in the format `yyyy-mm-dd hh:mm:ss+  
`adjustedValue`| `adjustedValue`| The value of the conversion after restatement. To change the value of a conversion from `100` to `75`, for example, you should report an adjusted value of `75`.  
`currencyCode`| `currencyCode`| Use the ISO 4217 3-character currency code, e.g. `USD`/`EUR`.  
`orderId`| `orderId`| If a conversion was reported with a specific order ID, then that order ID must be used as the identifier.  
`adjustmentDateTime`| `adjustmentDateTime`| The datetime at which the adjustment occurred. You must specify the timezone in the format `yyyy-mm-dd hh:mm:ss+  
`userAgent`| `userAgent`| User agent should only be specified in enhancements with the user identifiers and it should match the user agent of the request that sent the original conversion. This is so that the conversion and the enhancement both are either attributed as same or cross-device.  
`email`| `hashedEmail`| Include a domain name for all email addresses. Remove any spaces in between the addresses.  
`phone`| `hashedPhone`| Format the phone number using the [E.164 format](<https://en.wikipedia.org/wiki/E.164>). Include the country code as well.  
`firstName`| `hashedFirstName`| Do not include any prefixes (e.g., `Mrs.`).  
`lastName`| `hashedLastName`| Do not include any suffixes (e.g., `Sr.`).  
`city`| `city`| This field accepts any string.  
`state`| `state`| This field accepts any string.  
`country` / `countryCode`| `countryCode`| Use the ISO two-letter/three-letter [country codes](<https://developers.google.com/google-ads/api/reference/data/codes-formats#expandable-16>). Include the country code even if all your users belong to the same country.  
`postalCode`| `postalCode`| Both the US and international zip and postal codes are allowed. For the US, 5 digit codes followed by 4 digit extensions are also allowed. For the rest of the countries, do not include the postal code extensions.  
  
## FAQ

#### According to my audit logs, a “Rudder Admin” user updated my destination. Why is this?

This is a Google Ads permissions issue. See Google Ads Permissions for details.

#### Can I set up the Enhanced Conversions and Remarketing Lists destinations using the same Google Ads account?

Yes, you can. Both the integrations are the sub-features of Google Ads. Hence, you can use the same Google Ads account to configure both the destinations in RudderStack.

#### Where can I find my Google Ads customer ID?

The Google Ads customer ID is a unique number used to identify your Google Ads account. To get this ID:

  1. Sign in to your [Google Ads account](<https://ads.google.com/home/>).
  2. Click your profile picture in the top right corner — the customer ID is listed under **Account Information**.


See the [Google Ads Help Center](<https://support.google.com/google-ads/answer/1704344?hl=en>) for more information on finding your Google Ads customer ID.

#### What are the account permissions required for this integration?

For the integration to be successful, make sure the customer account used for OAuth verification adheres to Google’s [Customer Match policy](<https://support.google.com/google-ads/answer/6299717>) and has **Standard** or higher (**Administrative**) access level permissions. For more information on the access level permissions, refer to this [Google Ads support page](<https://support.google.com/google-ads/answer/9978556?visit_id=637611563637058259-4176462731&rd=1>).

To set the access level, follow these steps:

  1. Log in to your [Google Ads account](<https://ads.google.com/intl/en_IN/home/>).
  2. In the left navigation bar, click **Admin** > **Access and security**.
  3. Click the **+** symbol. Then, enter the email address of the account and from the list of permissions, select **Standard** or **Administrative**.

[![Specifying access levels](/docs/images/event-stream-destinations/gaoc/ga-access-security.webp)](</docs/images/event-stream-destinations/gaoc/ga-access-security.webp>)

  4. Click **Send invitation**.


The account will have the access level permissions once they accept the invitation.

#### Why am I getting a 400 Bad Request error message while configuring the destination?

If you get a 400 Bad Request error while configuring the destination, make sure your customer account is allowlisted and configured to have **Standard** or **Administrative** access levels in Google Ads.

See the above FAQ for steps on setting the access level permissions for the account.