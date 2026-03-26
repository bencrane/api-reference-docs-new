# Adjust Integration FAQ

Answers to some of the commonly asked questions related to the Adjust integration.

* * *

  * __3 minute read

  * 


This guide answers some of the commonly asked questions related to setting up and using the Adjust integration with RudderStack.

## Destination configuration

#### Where can I find the Adjust app token?

To get your Adjust app token, follow these steps:

  1. Log into your [Adjust dashboard](<https://dash.adjust.com/#/>).
  2. Find your app and select the app options caret (^):

[![Adjust app token](/docs/images/event-stream-destinations/adjust-app-token-1.webp)](</docs/images/event-stream-destinations/adjust-app-token-1.webp>)

  3. You will find your app token listed here.

[![Adjust app token](/docs/images/event-stream-destinations/adjust-app-token-2.webp)](</docs/images/event-stream-destinations/adjust-app-token-2.webp>)

#### How can I create a new event token in Adjust?

To create a new event token, follow these steps:

  1. Log into your [Adjust dashboard](<https://dash.adjust.com/#/>).
  2. Find your app and select the app options caret (^):

[![Adjust app token](/docs/images/event-stream-destinations/adjust-app-token-1.webp)](</docs/images/event-stream-destinations/adjust-app-token-1.webp>)

  3. Go to **All Settings** > **Events** :

[![Adjust event token](/docs/images/event-stream-destinations/adjust-event-token.webp)](</docs/images/event-stream-destinations/adjust-event-token.webp>)

  4. Under **CREATE NEW EVENT** , enter the name of the event token and click **CREATE**.


#### How can I set up new partners in Adjust?

Adjust lets you provide additional data to certain [integrated partners](<https://help.adjust.com/en/integrated-partners>). To set up a new partner in Adjust, follow these steps:

  1. Log in to your [Adjust dashboard](<https://dash.adjust.com/#/>).
  2. Find your app and select the app options caret (^):

[![Adjust app token](/docs/images/event-stream-destinations/adjust-app-token-1.webp)](</docs/images/event-stream-destinations/adjust-app-token-1.webp>)

  3. Go to **All Settings** > **Partner Setup** > **ADD PARTNERS** :

[![Adjust partner setup](/docs/images/event-stream-destinations/adjust-partner-setup.webp)](</docs/images/event-stream-destinations/adjust-partner-setup.webp>)

  4. Select the partner from the list and click the **+** option on the right to add.
  5. Enter the relevant details to complete the configuration and click **SAVE** to complete the setup.


## Supported events and features

#### What events are supported in cloud mode vs device mode?

Cloud mode supports only [Track](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events, whereas device mode supports both [Identify](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) and [Track](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events.

#### Does app install attribution work in cloud mode?

No, the app install attribution feature is only available in device mode. The **Enable Install Attribution** [dashboard setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/setup-guide/#connection-settings>) applies only to device mode integrations on Android (Java) and iOS (Obj-C).

See the [App install attribution](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/device-mode/#app-install-attribution>) section for more information.

## Install attribution

#### Why are the `Install Attributed` events not appearing in my Adjust dashboard?

  * Verify that the Adjust destination is correctly configured in your RudderStack dashboard.
  * Check your Adjust **App Token** is correctly specified in the [dashboard configuration](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/setup-guide/#connection-settings>).
  * Make sure the `Install Attributed` event is properly mapped to the corresponding Adjust event token. See the [App install attribution](<https://www.rudderstack.com/docs/destinations/streaming-destinations/adjust/device-mode/#app-install-attribution>) section for more information.


#### Why is the `Install Attributed` event not triggering?

If you load Adjust’s SDK natively alongside the Rudder-Adjust integration, the `Install Attributed` event callback may not trigger correctly. You need to remove the native Adjust implementation to avoid any conflicts.

> ![warning](/docs/images/warning.svg)
> 
> If your device is already registered with Adjust, make sure to unregister it first, as attribution **will not change** for registered devices.

The device unregistration process is listed below:

> ![info](/docs/images/info.svg)
> 
> This process is required because Adjust only triggers install attribution on the first genuine app installation for each device ID.

  1. **Find the device identifier** :

     * Get the IDFA (iOS) or Advertising ID (Android) from the raw view of an event in your RudderStack dashboard.
     * Or check your device settings:
       * iOS: **Settings** > **Privacy & Security** > **Apple Advertising** > **View Ad ID**
       * Android: **Settings** > **Google** > **Ads** > **View Ad ID**
  2. **Uninstall app** : Remove the app completely from your test device.

  3. **Unregister in Adjust Console** :

     * Go to Adjust Testing Console.
     * Navigate to your app.
     * Find and delete the IDFA (iOS) or Advertising ID (Android) from your registered test devices.
  4. **Clean reinstall** :

     * Reinstall the app on the device.
     * Launch the app fresh — this should trigger the `Install Attributed` event.
     * You should now see the device register in Adjust with a new `Install Attributed` event.


See the [Adjust documentation](<https://help.adjust.com/en/article/testing-console#forget-device>) for more information.