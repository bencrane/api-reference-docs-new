# Campaign Manager 360 Beta

Send your event data from RudderStack to Campaign Manager 360.

* * *

  * __6 minute read

  * 


[Campaign Manager 360](<https://developers.google.com/doubleclick-advertisers/guides/conversions_overview>) is an ad management platform which optimizes your digital campaigns across websites and mobile. It provides many useful features for ad serving, targeting, verification, and reporting.

RudderStack supports sending the offline conversion events to Campaign Manager 360 by leveraging their [Conversions API](<https://developers.google.com/doubleclick-advertisers/rest/v4/conversions>).

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/campaign_manager>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Beta
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Campaign Manager 360** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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

  3. Select **Campaign Manager 360** from the list of destinations. Then, click **Continue**.


## Account settings

Before you set up Campaign Manager 360 as a destination in RudderStack, authenticate your account by following these steps:

  1. Click **Create Account** in the **Account Settings** section.
  2. From the modal, click the **Sign in with Google** button.
  3. Choose the required account and grant RudderStack the required permissions.
  4. Click **Save** to use the specified account:

[![Google Account authentication](/docs/images/event-stream-destinations/cm-360-account-connect-normal.webp)](</docs/images/event-stream-destinations/cm-360-account-connect-normal.webp>)

If you have authenticated multiple accounts, you can click **Edit Credentials** to select or delete any other authenticated account:

> ![warning](/docs/images/warning.svg)
> 
> RudderStack throws an error if you try to delete an account used by any other connection set up for the same destination.

[![Google Account authentication](/docs/images/event-stream-destinations/cm-360-edit-account-creds.webp)](</docs/images/event-stream-destinations/cm-360-edit-account-creds.webp>)

## Connection settings

Setting| Description  
---|---  
Profile ID| Enter the user profile ID required for the [`batchinsert`](<https://developers.google.com/doubleclick-advertisers/rest/v4/conversions/batchinsert>) and [`batchupdate`](<https://developers.google.com/doubleclick-advertisers/rest/v4/conversions/batchupdate>) methods of the Campaign Manager 360 Conversions API.  
  


> ![warning](/docs/images/warning.svg)Incorrect profile ID or insufficient permissions associated with the profile can lead to 403 errors in your pipeline.  
  
Limit ad tracking| Toggle on this setting to report a conversion but not target it, thus preventing remarketing.  
Child directed treatment| Toggle on this setting to allow requests from users under the age of 13 (required for COPPA compliance).  
Non personalized ad| Toggle on this setting if the conversion is intended for a non-personalized ad.  
Treatment for underage| Toggle on this setting to allow requests from users under the age of 16 (required for European Union’s GDPR compliance).  
Enhanced conversions| Toggle on this setting to send enhanced conversions to Campaign Manager 360.  
Hash user identifiers| This setting is visible if **Enhanced conversions** is toggled on. Enable it to hash user identifiers in your events before sending the data to Campaign Manager 360.  
  


> ![warning](/docs/images/warning.svg)Toggle off this setting if you are already sending hashed data in your events.  
  
Consent management settings| This setting lets you associate the cookie consent groups to Campaign Manager 360. Specify the consent management provider from the dropdown and enter the category IDs.  
  
See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
> ![info](/docs/images/info.svg)
> 
> You can also pass values for these settings in your Track events. However, note that these values will take precedence over the dashboard settings.

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to capture user events along with the associated properties and send them to Campaign Manager 360.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Product Reviewed", {
      "profileId": 437689,
      "floodlightConfigurationId": "213123123",
      "ordinal": "3",
      "floodlightActivityId": "456543345245",
      "mobileDeviceId": "mobileDeviceId",
      "value": 7,
      "encryptedUserId": "encrepyteduserId"
      "impressionId": "string",
      "limitAdTracking": false,
      "childDirectedTreatment": true,
      "encryptionInfo": {
        "kind": "dfareporting#encryptionInfo",
        "encryptionSource": "AD_SERVING",
        "encryptionEntityId": "3564523",
        "encryptionEntityType": "DCM_ACCOUNT"
      },
      "requestType": "batchinsert"
    })
    

### Send enhanced conversions

The Campaign Manager 360 Conversions API supports [sending enhanced website tag-based conversions](<https://developers.google.com/doubleclick-advertisers/guides/conversions_ec>) with user identifiers.

To use this feature, you must first accept the [Enhanced Conversions Terms of Service](<https://support.google.com/sa360/answer/12863936>) for your Floodlight configuration in Campaign Manager 360 by following these steps:

  1. Log in to your Campaign Manager 360 account.
  2. Select the advertiser for which you want to set up the enhanced conversions.
  3. Go to **Floodlight** > **Configuration** in the left sidebar and select the checkbox under the **Enhanced Conversion** section.


To send enhanced conversions to Campaign Manager 360, toggle on the **Enhanced conversions** setting in the dashboard and set `properties.requestType` to `batchupdate` in your `track` events, as shown:
    
    
    rudderanalytics.track(
      "Product Reviewed", {
        "profileId": "34245",
        "floodlightConfigurationId": "213123123",
        "ordinal": "string",
        "floodlightActivityId": "456543345245",
        "value": "756",
        "quantity": "455678",
        "gclid": "string",
        "encryptionSource": "AD_SERVING",
        "encryptionEntityId": "3564523",
        "encryptionEntityType": "DCM_ACCOUNT",
        "requestType": "batchupdate"
      }, {
        email: "alex@example.com",
        firstName: "Alex",
        lastName: "Keener",
        address: {
          street: "350 Blue Gum Street",
          city: "New Orleans",
          state: "Louisiana",
          country: "US",
          postalCode: "90009",
        },
      },
    );
    

Note that:

  * You must enhance the conversions with user identifiers within 24 hours after they are captured by the online tags.
  * A conversion can have a maximum of five user identifiers.


> ![info](/docs/images/info.svg)
> 
> For security purposes, RudderStack automatically hash-encrypts the user identifiers before sending them to Campaign Manager 360. Make sure to turn off the Hash user identifiers setting if you are already tracking hashed user data via RudderStack.

### Property mappings

The following table lists the event property mappings between RudderStack and Campaign Manager 360:

RudderStack property| Campaign Manager 360 property| Data type  
---|---|---  
`properties.floodlightActivityId`  
Required| `floodlightActivityId`| String  
`properties.floodlightConfigurationId`  
Required| `floodlightConfigurationId`| String  
`properties.ordinal`  
Required| `ordinal`| String  
`properties.quantity`  
Required| `quantity`| String  
`timestamp`  
Required| `timestampMicros`| Timestamp in ISO 8601 format  
`properties.profileId`  
`config.profileId`| `profileId`| Number  
`properties.encryptedUserId`| `encryptedUserId`| String  
`properties.encryptedUserIdCandidates[]`| `encryptedUserIdCandidates[]`| Array  
`properties.dclid`| `dclid`| String  
`properties.gclid`| `gclid`| String  
`properties.matchId`| `matchId`| String  
`properties.mobileDeviceId`| `mobileDeviceId`| String  
  
> ![warning](/docs/images/warning.svg)
> 
> Apart from the above-mentioned properties marked as required, you must also send the following:
> 
>   * `properties.requestType` in the conversion event with the value as [`batchinsert`](<https://developers.google.com/doubleclick-advertisers/rest/v4/conversions/batchinsert>) or [`batchupdate`](<https://developers.google.com/doubleclick-advertisers/rest/v4/conversions/batchupdate>).
>   * **At least one** of the optional fields.
> 


#### User identifier mappings for enhanced conversions

The following table lists the user identifier mappings between RudderStack and Campaign Manager 360:

RudderStack property| Campaign Manager 360 property  
---|---  
`traits.email`  
`context.traits.email`| `hashedEmail`  
`traits.phone`  
`context.traits.phone`| `hashedPhoneNumber`  
`traits.firstName`  
`context.traits.firstName`| `addressInfo.hashedFirstName`  
`traits.lastName`  
`context.traits.lastName`| `addressInfo.hashedLastName`  
`traits.street`  
`traits.address.street`  
`context.traits.street`  
`context.traits.address.street`| `addressInfo.hashedStreetAddress`  
`traits.city`  
`traits.address.city`  
`context.traits.city`  
`context.traits.address.city`| `addressInfo.city`  
`traits.country`  
`traits.address.country`  
`context.traits.country`  
`context.traits.address.country`| `addressInfo.countryCode`  
`traits.state`  
`traits.address.state`  
`context.traits.state`  
`context.traits.address.state`| `addressInfo.state`  
`traits.postalCode`  
`traits.address.postalCode`  
`context.traits.postalCode`  
`context.traits.address.postalCode`| `addressInfo.postalCode`  
  
Note that:

  * The fields mapped to `addressInfo.countryCode` (`traits.country` / `traits.address.country` /`context.traits.country` / `context.traits.address.country`) must contain a 2-letter [ISO-3166 Alpha-2](<https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>) country code of the user’s address. See the [Campaign Manager 360 documentation](<https://developers.google.com/doubleclick-advertisers/rest/v4/Conversion#offlineuseraddressinfo>) for more information.
  * The phone number (`traits.phone` or `context.traits.phone`) must contain a proper country code in it. If the phone number does not have a country code, make sure to provide the mapping for the `addressInfo.countryCode` field, given the Enhanced conversions and Hash user identifiers settings are toggled on.


## FAQ

#### Where can I find the Profile ID?

  1. Log in to your Campaign Manager 360 account.
  2. In the top right corner, click your account icon (the cicle with your initials or profile picture).
  3. A dropdown panel will appear with the following details:


  * Your name and email address
  * Account name
  * Account ID


  4. The **Profile ID** is displayed as a number below the account name.

[![Profile ID](/docs/images/event-stream-destinations/cm-360-profile-id.webp)](</docs/images/event-stream-destinations/cm-360-profile-id.webp>)