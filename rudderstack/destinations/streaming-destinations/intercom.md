# Intercom Destination

Send your event data from RudderStack to Intercom.

* * *

  * __10 minute read

  * 


[Intercom](<https://www.intercom.com/>) is a real-time business messaging platform that lets you manage all your customer lifecycle activities in a single platform.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/intercom>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Intercom** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Device mode  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Intercom native SDK from the `https://widget.intercom.io/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Intercom SDK successfully.

## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **Intercom**.
  2. Connect your source and click **Continue**.


### Connection settings

Configure the following settings to set up Intercom as a destination in RudderStack:

Setting| Description  
---|---  
Name| Assign a name to uniquely identify the destination in the RudderStack dashboard.  
Access Token| Enter your Intercom API access token.  
  
You can obtain the token by going to your Intercom dashboard and navigating to **Settings** > **Apps & Integrations** > **Developer Hub**. Then, select your app and go to **Configure** > **Authentication**. For more information, see [Intercom documentation](<https://developers.intercom.com/building-apps/docs/authentication-types#how-to-get-your-access-token>).  
Intercom REST API Version| Select your Intercom REST API Version from the dropdown as **1.4** or **latest** (v2.10)  
API Server| 

> ![warning](/docs/images/warning.svg)This setting is visible only if you set **Intercom REST API Version** to **latest**.

  
Select your Intercom workspace server. By default, RudderStack sets it to **Standard** (US) and provides two other options - **EU** (Europe) and **AU** (Australia).  
Send Anonymous ID as Secondary User ID| Toggle on this setting to send the anonymous ID (`anonymousId`) as the secondary user ID.  
Update last seen to the current time| 

> ![warning](/docs/images/warning.svg)This setting is visible only if you set **Intercom REST API Version** to **1.4**.

  
Use this setting to turn on the `update_last_request_at` parameter in Intercom.  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
### Configuration settings

After completing the initial setup, configure the following settings to correctly receive your data in Intercom:

  * **Send AnonymousId as Secondary UserId** : Turn on this option to send `anonymousId` as the user ID to Intercom when the `userId` is absent from the event payload.


> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * This setting is applicable only when sending events in cloud mode.
>   * It is helpful for tracking anonymous users on your site. For more information on the scenario where this setting is useful, see FAQ section below.
> 


  * **Android API Key** / **iOS API Key** : This is required for sending events from your mobile apps to Intercom. You can get it from your Intercom dashboard by going to **Settings** > **Installation** and selecting the relevant platform. Note that this setting is applicable only when sending events in device mode.


#### **Other settings**

  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to Intercom. For more information on this setting, see [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>).
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Adding device mode integration

Depending on your platform of integration, follow the steps below to add Intercom to your project:

> ![info](/docs/images/info.svg)
> 
> Your Android app must be on **version 5.0 (API level 21) or higher** for RudderStack to be able to send events to Intercom.

Follow these steps to add Intercom to your Android project:

  1. In your app-level `build.gradle` file, add the following `repository`:


    
    
    repositories {
        mavenCentral()
    }
    

  2. Add the following under `dependencies`:


    
    
    // Rudder core sdk and intercom extension
    implementation 'com.rudderstack.android.sdk:core:1.0.2'
    implementation 'com.rudderstack.android.integration:intercom:0.1.1'
    
    // intercom core sdk
    implementation 'io.intercom.android:intercom-sdk-base:6.+'
    
    // gson
    implementation 'com.google.code.gson:gson:2.8.6'
    
    // FCM
    implementation 'com.google.firebase:firebase-messaging:20.2.0'
    

  3. Change the SDK initialization as follows:


    
    
    // initialize Rudder SDK
    val rudderClient: RudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withFactory(IntercomIntegrationFactory.FACTORY)
                .build()
        )
    

To add iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. to your project, follow these steps:

  1. Add the required pod followed by `pod install`:


    
    
    pod 'Rudder-Intercom'
    

  2. Initialize the SDK as follows:


    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [builder withFactory:[RudderIntercomFactory instance]];
    [builder withLoglevel:RSLogLevelDebug]; // optional
    [RSClient getInstance:WRITE_KEY config:[builder build]];
    

  3. Add a **Privacy - Photo Library Usage Description** entry to your `Info.plist`. This is [required by Apple](<https://developer.apple.com/library/content/qa/qa1937/_index.html>) for applications that can access the photo library.


> ![info](/docs/images/info.svg)
> 
> Users will be prompted for the permission to access the photo library only when they tap the button to upload their images.

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call captures the details about a visiting user.

A sample`identify` call is shown:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
      company: {
        id: "group01",
        name: "Tech Group",
      },
      createdAt: "Mon May 19 2019 18:34:24 GMT+0000 (UTC)",
    })
    

### Using `identify` calls

You can use the `identify` call to create or update user information in Intercom, as explained below:

  * **Create/update a user** : When you make an`identify` call, RudderStack creates or updates the user in Intercom.
  * **Remove users from a company** : To remove users from a company, you can pass `remove: true` inside the `company` object:


    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
      company: {
        id: "group01",
        name: "Tech Group",
        remove: true
      },
      createdAt: "Mon May 19 2019 18:34:24 GMT+0000 (UTC)",
    })
    

  * **Unsubscribe users** : To unsubscribe users from emails, you can pass `unsubscribedFromEmails: true` inside the `context` object:


    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
      company: {
        id: "group01",
        name: "Tech Group",
      },
      unsubscribedFromEmails: true,
      createdAt: "Mon May 19 2019 18:34:24 GMT+0000 (UTC)",
    })
    

  * **Associate user with a company** : To link a user to a company, use the `group` call.


> ![warning](/docs/images/warning.svg)
> 
> RudderStack does not support Intercom’s [Last Seen](<https://community.intercom.com/customer-faq-28/how-do-you-define-last-seen-2396>) feature currently.

### Traits mapping

The following table lists the mapping of the RudderStack traits to the Intercom properties:

RudderStack trait| Intercom property  
---|---  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  
Required, if `email` is absent.| `external_id`  
`traits.email`  
`context.traits.email`  
Required, if `userId` is absent.| `email`  
`traits.phone`  
`context.traits.phone`| `phone`  
`traits.avatar`  
`context.traits.avatar`| `avatar`  
`traits.name`  
`context.traits.name`| `name`  
`traits.role`  
`context.traits.role`| `role`  
`traits.ownerId`  
`context.traits.ownerId`| `owner_id`  
`traits.createdAt`  
`context.traits.createdAt`| `signed_up_at`  
`traits.unsubscribedFromEmails`  
`context.traits.unsubscribedFromEmails`| `unsubscribed_from_emails`  
`context.traits.lastSeenAt`  
`last_seen_at`| `last_seen_at`  
  
### Identity verification

Intercom’s [identity verification](<https://www.intercom.com/help/en/articles/183-enable-identity-verification-for-web-and-mobile>) feature ensures the privacy of the conversations between you and your users. It also makes sure that one user cannot impersonate another.

> ![info](/docs/images/info.svg)
> 
> RudderStack supports the identity verification feature for the events sent through the **web device mode**.

To use the identity verification feature in web device mode, you can pass `user_hash` within the [integrations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#integrationopts>) object, as shown in the following snippet:
    
    
    rudderanalytics.identify(
      "1hKOmRA4GRlm", {
        name: "Alex Keener",
        country: "USA"
      }, {
        Intercom: {
          user_hash: "9c56cc51b374c3ba189210d5b6d4bf57790d351c96c47c02190ecf1e430635ab",
        },
      }
    );
    

> ![warning](/docs/images/warning.svg)
> 
> The `user_hash` is a SHA256 hash of your Intercom API secret and the `userId`. Note that this hash is **not** based on the user’s email.

> ![info](/docs/images/info.svg)
> 
> To obtain your Intercom API secret, go to your Intercom dashboard and navigate to **Settings** > **Apps & Integrations** > **Developer Hub**. Then select your app and go to **Configure** > **Basic information**. You will find the API secret listed here under **Client secret**.

### Delete a user

You can delete a user in Intercom using the [Suppression with Delete regulation](<https://www.rudderstack.com/docs/api/user-suppression-api/#adding-a-suppression-with-delete-regulation>) of the RudderStack [User Suppression API](<https://www.rudderstack.com/docs/api/user-suppression-api/>).

> ![warning](/docs/images/warning.svg)
> 
> While RudderStack forwards the deletion request, it **does not guarantee** deletion within a 30-day window. You will need to check with Intercom if the request is fulfilled.

To delete a user, specify their `userId` in the event. Additionally, you can specify a custom identifier (optional) in the event.

A sample regulation request body for deleting a user in Intercom is shown below:
    
    
    {
      "regulationType": "suppress_with_delete",
      "destinationIds": [
        "2FIKkByqn37FhzczP23eZmURciA"
      ],
      "users": [{
        "userId": "1hKOmRA4GRlm",
        "<customKey>": "<customValue>"
      }]
    }
    

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you track user’s actions along with any properties associated with those actions.

> ![warning](/docs/images/warning.svg)
> 
> You must identify a user with a valid `userId` or `email` before making any `track` calls to Intercom.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      order_id: "140021222",
      email: "alex@example.com",
      checkout_id: "EAP3211",
      products: "Sports Shoes",
      total: 145.99,
      currency: "USD"
    })
    

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * To send a `track` call to Intercom successfully, you must include any one of the `userId` or `email` fields.
>   * RudderStack converts and sends all `track` event properties as per the [Intercom API](<https://developers.intercom.com/intercom-api-reference/reference#event-metadata-types>).
> 


### Properties mapping

The following table lists the mapping of the RudderStack `track` properties to the Intercom properties:

RudderStack property| Intercom property  
---|---  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  
Required, if `email` is absent.| `user_id`  
`traits.email`  
`context.traits.email`  
Required, if `userId` is absent.| `email`  
`event`  
Required| `event_name`  
`timestamp`| `created`  
`properties`| metadata  
`properties.id`  
`traits.id`| `id`  
  
## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views with any additional relevant information about the viewed page.

> ![warning](/docs/images/warning.svg)
> 
> The `page` call is supported **only** for the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) when sending events via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>). It works by triggering Intercom’s `update` method, which looks for a list of new open conversations to be displayed to the current user.

A sample `page` call looks like the following code snippet:
    
    
    rudderanalytics.page("Best Seller")
    

## Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call lets you link an identified user to a group like a company, organization, or an account. Along with that, you can [add tags to a company](<https://developers.intercom.com/docs/references/rest-api/api.intercom.io/tags/createtag>).

RudderStack uses this information to [create or update a company](<https://developers.intercom.com/intercom-api-reference/reference/createorupdatecompany>) in Intercom using their `/companies` endpoint.

A sample `group` call is shown below:
    
    
    rudderanalytics.group("group123", {
      name: "companyName",
      industry: "IT",
      employees: 450
    })
    

> ![warning](/docs/images/warning.svg)
> 
> RudderStack requires a `groupId` (`group123` in the above example) to send `group` events to Intercom. It maps this field to Intercom’s `company_id` field.

### Supported mappings

The following table lists the mapping of the RudderStack `group` traits to the Intercom properties:

RudderStack trait| Intercom property  
---|---  
`groupId`  
Required| `company_id`  
`name`| `name`  
`website`| `website`  
`traits.plan`  
`context.traits.plan`| `plan`  
`traits.size`  
`context.traits.size`| `size`  
`traits.industry`  
`context.traits.industry`| `industry`  
`traits.monthlySpend`  
`context.traits.monthlySpend`| `monthly_spend`  
`traits.remoteCreatedAt`  
`context.traits.remoteCreatedAt`| `monthly_spend`  
`traits`| `custom_attributes`  
`context.traits.tags`| Maps to tag names in Intercom  
  
## Reset

The `reset` method resets the previously identified user and any related information.

To reset user identification in your Android app, run the following command:
    
    
    rudderClient.reset();
    

To reset user identification in your iOS app, run the following command:
    
    
    [[RSClient sharedInstance] reset];
    

## User lookup

RudderStack supports user lookup in `identify` and `group` calls. By default, it performs the lookup using the `email` field. However, you can provide a custom field for the lookup using the event’s `integrations` object.

> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * You can only send the [fields accepted by Intercom](<https://developers.intercom.com/docs/references/rest-api/api.intercom.io/contacts/searchcontacts#section/Accepted-Fields>) for user lookup. **These fields are case sensitive**.
>   * The field you are passing for lookup must be present in the event’s `context.traits` object.
> 


A sample `identify` event highlighting the user lookup feature is shown below:
    
    
    rudderanalytics.identify('1hKOmRA4el9Z', {
      email: 'alex@example.com',
      phone: '+1-202-555-0146',
    }, {
      integrations: {
        INTERCOM: {
          lookup: 'phone'
        }
      }
    });
    

## Troubleshooting

Error| Reason| Solution  
---|---|---  
Cannot have more than 120 active event names| You have sent more than 120 event names in your `track` calls.  
  
Once the event limit is reached, Intercom does not store any new events and returns this error.| Archive any unused events in your Intercom dashboard by going to **Settings** > **Intercom Data** > **Events**.  
  
See [Intercom documentation](<https://www.intercom.com/help/en/articles/5245634-event-limits-troubleshooting-and-f-a-q#h_9b866dcfb0>) for more information.  
  
## FAQ

#### Does RudderStack support Intercom’s push notification and deep linking features?

None of the RudderStack SDKs support push notifications and deep linking features currently. See [Intercom documentation](<https://developers.intercom.com/installing-intercom/docs>) for more information on configuring these features for your project.

#### What happens if both `userId` or `email` are missing in the `identify` / `track` calls sent to Intercom?

For both `identify` and `track` calls, either `userId` or `email` is a mandatory field. In case both these fields are missing, RudderStack will drop the event.

It is highly recommended to toggle on the Send AnonymousId as Secondary UserId setting in your RudderStack dashboard to avoid any event loss in such a scenario.

  


##### [Intercom API v2.10 Migration Guide](</docs/destinations/streaming-destinations/intercom/migration-guide/>)

Configuration changes and differences in sending events when migrating from Intercom API v1.4 to v2.10.