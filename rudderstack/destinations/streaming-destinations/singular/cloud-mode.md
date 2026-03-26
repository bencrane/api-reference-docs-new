# Singular Cloud Mode Integration

Send events from RudderStack to Singular via cloud mode.

* * *

  * __8 minute read

  * 


RudderStack supports server-to-server (S2S) API integration with Singular. See the [Singular API endpoint reference](<https://support.singular.net/hc/en-us/articles/360048588672-Server-to-Server-S2S-API-Endpoint-Reference>) for more information.

RudderStack supports two types of [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events that you can send to Singular via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>):

  * Session events
  * Custom events


## Session events

RudderStack lets you specify the event names to be used as session events in the [Session Event Name](<https://www.rudderstack.com/docs/destinations/streaming-destinations/singular/setup-guide/#connection-settings>) dashboard setting.

RudderStack sends the session events to Singular via its [`launch`](<https://s2s.singular.net/api/v1/launch>) API.

> ![info](/docs/images/info.svg)
> 
> RudderStack considers an event as a session event only if it is specified in the dashboard settings or if any of the following three [lifecycle events](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/>) occur:
> 
>   * Application Installed
>   * Application Opened
>   * Application Updated
> 

> 
> RudderStack automatically tracks the above three lifecycle events if lifecycle event tracking is enabled.

### Supported mappings

This section lists the mappings of the RudderStack event properties to the relevant Singular fields.

The following table lists the mapping of the attributes **automatically captured** by RudderStack for the **mobile platforms** ([Android (Java)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>) and [iOS (Obj-C)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>)):

RudderStack property| Singular attribute| Description  
---|---|---  
`context.os.name`  
Required| `p`| The source platform (Android or iOS).  
`context.app.namespace`  
Required| `i`| The package name (Android) or bundle ID (iOS) of your app.  
`context.app.version`  
Required| `app_v`| The app version.  
`context.ip`  
`request_ip` (in that order)  
Required| `ip`| The user’s IP address. Refer to the note below for information on anonymizing your IP.  
`context.os.version`  
Required| `ve`| The device OS version at session time.  
`context.device.model`  
Required| `mo`| The device model. This parameter must be used with the `ma` parameter.  
`context.device.manufacturer`  
Required| `ma`| The make of the device hardware. This parameter must be used with the `mo` parameter.  
`context.locale`  
Required| `lc`| The device’s IETF local tag using two-lettered language and country code, separated by an underscore.  
`context.device.id`  
Required| `idfv`| The raw [`IdentifierForVendor`](<https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIDevice_Class/Reference/UIDevice.html#//apple_ref/occ/instp/UIDevice/identifierForVendor>) in upper case with dashes. **This is applicable for iOS apps only**.  
`context.device.id`  
Required, if `context.device.advertisingId` and `properties.asid` is absent.| `andi`| The raw [`Android ID`](<http://developer.android.com/reference/android/provider/Settings.Secure.html#ANDROID_ID>) in lower case. **This is applicable for Android apps only** and is required only when the Android advertising ID is unavailable on the device. See [FAQ](<https://www.rudderstack.com/docs/destinations/streaming-destinations/singular/cloud-mode/#which-device-id-attributes-are-required-for-android>) for more information.  
`context.app.build`  
Required| `bd`| The device build (URL encoded).  
`context.device.adTrackingEnabled`  
Required| `dnt`| Pass `true` if do not track(`dnt`) is disabled (`dnt=0`), else pass `false`(`dnt=1`). This is automatically captured if you pass the advertising ID to the SDK.  
`context.app.name`| `n`| The human-readable app name as displayed in the UI.  
[`timestamp`](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/#clock-skew-considerations>)  
`originalTimestamp`| `utime`| Optional  
`context.network.wifi`| `c`| The connection type (WiFi or carrier).  
`context.network.carrier`| `cn`| The carrier name of the internet provider.  
  
> ![success](/docs/images/tick.svg)
> 
> To anonymize your IP, you can send a placeholder IP in the `context.ip` field. RudderStack uses it as the IP address instead of capturing it automatically from the backend.
> 
> For mobile SDKs, you can leverage the [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) feature to when sending events via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

The following table lists the mapping of the attributes that **must be passed via the event properties** :

> ![warning](/docs/images/warning.svg)
> 
> These properties are not persisted in the SDK and must be passed with every event.

RudderStack property| Singular attribute| Description  
---|---|---  
`properties.install_ref`  
Required| `install_ref`| The Google Install Referrer Information.  
`properties.referring_application`  
Required| `install_source`| The install source package name in Android. Use [`getInitiatingPackageName()`](<https://developer.android.com/reference/android/content/pm/InstallSourceInfo#getInitiatingPackageName%28%29>) to retrieve this.  
`properties.install_receipt`  
Required| `install_receipt`| The receipt received from the install. To retreive this, follow the [iOS Install Receipt](<https://support.singular.net/hc/en-us/articles/360037640812#Reference_Retrieving_the_iOS_Install_Receipt>) guide.  
`properties.asid`  
Required, if `context.device.advertisingId` and `context.device.id` is absent.| `asid`| The App Set ID for Android v12+ devices. See [FAQ](<https://www.rudderstack.com/docs/destinations/streaming-destinations/singular/cloud-mode/#which-device-id-attributes-are-required-for-android>) for more information.  
`properties.url`  
Required| `openui`| If the app is opened via a deep link/universal link, the value of the encoded deep link URL.  
`context.device.attTrackingStatus`  
Required| `att_authorization_status`| The [App Tracking Transparency authorization status](<https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/authorizationstatus>).  
`userId`| `custom_user_id`| The user ID passed through the `identify` call.  
`properties.attribution_token`| `attribution_token`| Used to attribute Apple Search Ads for iOS 14.3 and above. More information [here](<https://support.singular.net/hc/en-us/articles/360037640812#asa_adservices>).  
`properties.skan_conversion_value`| `skan_conversion_value`| The latest `SkAdNetwork` value at the time of the session notification.  
`properties.skan_first_call_timestamp`| `skan_first_call_timestamp`| UNIX timestamp of the first call made to the `SkAdNetwork` API.  
`properties.skan_last_call_timestamp`| `skan_last_call_timestamp`| UNIX timestamp of the last call made to the `SkAdNetwork` API at the time of the session notification.  
`properties.install`| `install`| The install flag. Set to `true` on the first session after app install, or `false` otherwise. Required for reinstall tracking capability.  
`properties.install_time`  
`timestamp`  
`originalTimestamp`| `install_time`| The install time (in UNIX).  
`properties.update_time`  
`timestamp`  
`originalTimestamp`| `update_time`| The update time (in UNIX).  
  
The following table lists the mapping of the attributes that **must be passed via the event properties just once** :

> ![info](/docs/images/info.svg)
> 
> These properties are persisted in the SDK.

RudderStack property| Singular attribute| Description  
---|---|---  
`context.device.advertisingId`  
Required| `idfa`| The raw [advertising ID](<https://developer.apple.com/library/ios/documentation/AdSupport/Reference/ASIdentifierManager_Ref/index.html>) in upper case with dashes. **This is applicable for iOS apps only**.  
`context.device.advertisingId`  
Required, if `properties.asid` and `context.device.id` is absent.| `aifa`| This is the lower case raw [advertising ID](<http://support.google.com/googleplay/android-developer/answer/6048248?hl=en>) with dashes. **This is applicable for Android apps only**. See [FAQ](<https://www.rudderstack.com/docs/destinations/streaming-destinations/singular/cloud-mode/#which-device-id-attributes-are-required-for-android>) for more information.  
`context.device.token`| `fcm`| The Firebase Cloud Messaging Device Token. It is required for uninstall tracking in Android.  
  


> ![info](/docs/images/info.svg)RudderStack supports only `fcm` for mapping the device token.  
  
`context.device.token`| `apns_token`| The Apple Push Notification Service Device Token. It is required for uninstall tracking in iOS.  
  
For more information on setting the device token, see the [Android (Java)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/#setting-the-android-device-token>) or [iOS (Obj-C)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/#setting-the-device-token>) SDK documentation.

## Custom events

RudderStack sends all events other than the session events as custom events via Singular’s `evt` API endpoint.

### Supported mappings

The following table lists the mapping of the attributes **automatically captured** by RudderStack for the **mobile platforms** ([Android (Java)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>) and [iOS (Obj-C)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>)):

RudderStack property| Singular attribute| Description  
---|---|---  
`context.os.name`  
Required| `p`| The source platform (Android or iOS).  
`context.app.namespace`  
Required| `i`| The package name (Android) or bundle ID (iOS) of your app.  
`context.ip`  
`request_ip` (in same order)  
Required| `ip`| The user’s IP address.  
`context.device.advertisingId`  
Required| `idfa`| The raw [`IdentifierForVendor`](<https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIDevice_Class/Reference/UIDevice.html#//apple_ref/occ/instp/UIDevice/identifierForVendor>) in upper case with dashes. **This is applicable for iOS apps only**.  
`context.device.advertisingId`  
Required, if `properties.asid` and `context.device.id` are absent.| `aifa`| This is the lower case raw [advertising ID](<http://support.google.com/googleplay/android-developer/answer/6048248?hl=en>) with dashes. **This is applicable for Android apps only**. See [FAQ](<https://www.rudderstack.com/docs/destinations/streaming-destinations/singular/cloud-mode/#which-device-id-attributes-are-required-for-android>) for more information.  
`context.device.id`  
Required| `idfv`| The raw [`IdentifierForVendor`](<https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIDevice_Class/Reference/UIDevice.html#//apple_ref/occ/instp/UIDevice/identifierForVendor>) in upper case with dashes. **This is applicable for iOS apps only**.  
`context.device.id`  
Required, if `context.device.advertisingId` and `properties.asid` are absent.| `andi`| The raw [`Android ID`](<http://developer.android.com/reference/android/provider/Settings.Secure.html#ANDROID_ID>) in lower case. **This is applicable for Android apps only** and is required only when the Android Advertising ID is unavailable on the device. See [FAQ](<https://www.rudderstack.com/docs/destinations/streaming-destinations/singular/cloud-mode/#which-device-id-attributes-are-required-for-android>) for more information.  
`context.os.version`  
Required| `ve`| The device OS version at session time.  
[`timestamp`](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/#clock-skew-considerations>)  
`originalTimestamp`| `utime`| Optional  
  
> ![info](/docs/images/info.svg)
> 
> Singular prefers `aifa` over `andi` (in Android) and `idfa` over `idfv` (in iOS).

The following table lists the mapping of the attributes that **must be passed via the event properties** :

RudderStack property| Singular attribute| Description  
---|---|---  
`event`  
Required| `n`| The name of the event. **This is user-defined**.  
`context.device.attTrackingStatus`  
Required| `att_authorization_status`| The [App Tracking Transparency authorization status](<https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/authorizationstatus>).  
`userId`| `custom_user_id`| The user ID passed through the `identify` call.  
`properties.skan_conversion_value`| `skan_conversion_value`| The latest `SkAdNetwork` value at the time of the session notification.  
`properties.skan_first_call_timestamp`| `skan_first_call_timestamp`| UNIX timestamp of the first call made to the `SkAdNetwork` API.  
`properties.skan_last_call_timestamp`| `skan_last_call_timestamp`| UNIX timestamp of the last call made to the `SkAdNetwork` API at the time of the session notification.  
`properties.eventAttributes`| `e`| The custom event attributes in JSON format. You need to pass these with every event as they are not persisted in the SDK.  
`properties.is_revenue_event`| `is_revenue_event`| Determines if an event is a revenue event. You need to pass this through the properties with every event as it is not persisted in the SDK.  
  
The following table lists the mapping of the **user-defined attributes specific to revenue events** :

RudderStack property| Singular attribute| Description  
---|---|---  
`properties.total`  
`properties.value`  
`properties.revenue`| `amt`| The currency amount.  
`properties.currency`| `cur`| The ISO 4217 three-lettered currency code. This should be in conjunction with the `amt` parameter.  
`properties.purchase_receipt`| `purchase_receipt`| The receipt received from a purchase.  
`properties.product_id`  
`properties.sku`| `purchase_product_id`| The product SKU identifier.  
`properties.orderId`  
`properties.purchase_transaction_id` (in that order)| `purchase_transaction_id`| The transaction identifier.  
  
> ![info](/docs/images/info.svg)
> 
> If you set any one out of the `value`, `revenue`, or `total` properties, RudderStack automatically considers the event as a revenue event, unless it is explicitly mentioned by the `is_revenue_event` property.

A few important considerations in case of custom events are listed below:

  * RudderStack takes the user agent from `context.userAgent` for Android and from the event properties in case of iOS.
  * RudderStack stores the extra attributes passed in the custom event in Singular’s `e` field.


## FAQ

#### How can I verify if the events are successfully delivered to Singular?

To verify if the events are successfully delivered to Singular, you can use RudderStack’s [Destination live events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/#destination-live-events>) feature.

You can also verify the event delivery by going to your [Singular dashboard](<https://app.singular.net/login?redir=%2F#/>) and following these steps:

  1. Go to **Settings** > **Console**. You should see a list of tracked devices:

[![Singular event delivery settings](/docs/images/event-stream-destinations/singular-event-delivery-1.webp)](</docs/images/event-stream-destinations/singular-event-delivery-1.webp>)

  2. To add a new device, click the **Add Device** option and choose the relevant settings:

[![Singular event delivery settings](/docs/images/event-stream-destinations/singular-event-delivery-2.webp)](</docs/images/event-stream-destinations/singular-event-delivery-2.webp>)

  3. Finally, click the eye icon associated with the tracked device to start seeing the events in real-time.

[![Singular event delivery settings](/docs/images/event-stream-destinations/singular-event-delivery-3.webp)](</docs/images/event-stream-destinations/singular-event-delivery-3.webp>)

You should be able to see a real-time log of all events sent to Singular:

[![Singular event delivery settings](/docs/images/event-stream-destinations/singular-event-delivery-4.webp)](</docs/images/event-stream-destinations/singular-event-delivery-4.webp>)

> ![info](/docs/images/info.svg)
> 
> For more customizable and granular reports, you can go to **Attribution** > **Export Logs** in the Singular dashboard. Note that this report is not real-time and takes some time to generate.

#### Which device ID attributes are required for Android?

For Android requests, Singular requires either of the following attributes in the mentioned order of preference:

  * `aifa`
  * `asid`
  * `andi`


If none of them are available, you must send at least one with the empty value (instead of `null` or `undefined`). If you send all of them, RudderStack discards the `andi` attribute as per Google’s data policies.