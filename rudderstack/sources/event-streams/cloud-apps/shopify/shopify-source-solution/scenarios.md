# Shopify Store Setup Scenarios

Use the RudderStack Shopify Source Solution to track events depending on your Shopify store setup.

* * *

  * __9 minute read

  * 


This guide lists the different methods for setting up and using the RudderStack Shopify Source Solution based on your Shopify store setup.

## 1\. Store fully hosted on Shopify template

Follow the guidelines in this section if your online store is hosted entirely on a Shopify template.

### Products used

  * [RudderStack Pixel](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/products/#rudderstack-pixel>)


### Event tracking methods

  * [RudderStack Pixel events](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/event-tracking/#rudderstack-pixel-events>)
  * [Webhook events](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/event-tracking/#webhook-events>)


### Setup: RudderStack

  1. Log in to your [RudderStack dashboard](<https://app.rudderstack.com/>) and click **Add Source**.
  2. From the list of **Event Streams** sources, select **Shopify**.
  3. Assign a name to your source and click **Continue**.


> ![warning](/docs/images/warning.svg)
> 
> Ignore the **Disable client side identifier in the Legacy Shopify Tracker App** setting as it only pertains to the [Legacy Shopify integration](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/legacy-app/>).

Your Shopify source is now configured. Go to the **Setup** tab and note the source **Write key**. Also, note your workspace’s data plane URL. These are required while configuring the RudderStack Pixel app in your Shopify store.

[![Shopify source write key](/docs/images/event-stream-sources/shopify-source-write-key.webp)](</docs/images/event-stream-sources/shopify-source-write-key.webp>)

### Setup: Shopify

  1. Go to the RudderStack Pixel app in the Shopify App Store. Then, download it to your Shopify store.
  2. Enter the data plane URL and the source write key obtained above in the app’s settings page.


> ![info](/docs/images/info.svg)
> 
> The **Subscribed to Webhook Events** setting will be turned on by default.

  3. Turn on the **Track Events via Shopify App Pixel** setting. It is required to successfully trigger events from the web pixel.
  4. Enable the theme app extension by clicking the **Connect** button next to **RudderStack App Embed Script**. You will then be directed to a new tab which opens the theme app editor screen.

[![RudderStack Pixel app settings](/docs/images/event-stream-sources/shopify/rudderstack-pixel-app-settings.webp)](</docs/images/event-stream-sources/shopify/rudderstack-pixel-app-settings.webp>)

  5. On the left side in the **App embeds** section, turn on the toggle for script and then click **Save** button on the top right hand side.

[![RudderStack Pixel app embeds script toggle](/docs/images/event-stream-sources/shopify/rudderstack-pixel-app-embeds.webp)](</docs/images/event-stream-sources/shopify/rudderstack-pixel-app-embeds.webp>)

The setup is complete once you save the changes. You can close the tab and return to the RudderStack Pixel app screen.

### Pros and cons

**Pros**

  * As your store is fully based on a Shopify template, using the RudderStack Pixel app is the quickest way to set up comprehensive tracking for both app pixel events and webhook events.
  * RudderStack automatically handles the [identity stitching](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/id-stitching/>) between the pixel events from the client and the webhook events from the Shopify backend.


**Cons**

  * You cannot customize any of the event tracking done through the app. Also, you cannot add any custom events.
  * Because this solution leverages the RudderStack Pixel app, you cannot load the [RudderStack JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) on your Shopify store. Therefore, you cannot use [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) integrations. Only [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) integrations are supported with this solution.
  * You will not be able to leverage other features available in the JavaScript SDK.


## 2\. Hybrid headless store with Shopify-hosted checkout

Follow the guidelines in this section to set up your Shopify Source Solution if your store meets the following conditions:

  * Your online store is partly a custom site and not hosted by Shopify.
  * Your online checkout is hosted by Shopify.
  * You manage customers, orders, and inventories through Shopify’s backend.


### Products used

  * [RudderStack Pixel](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/products/#rudderstack-pixel>)
  * [Shopify Custom Pixel](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/products/#shopify-custom-pixel>)


### Event tracking methods

  * [Custom pixel events](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/event-tracking/#custom-pixel-events>)
  * [Webhook events](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/event-tracking/#webhook-events>)


### Setup: RudderStack

  1. Log in to your [RudderStack dashboard](<https://app.rudderstack.com/>) and click **Add Source**.
  2. From the list of **Event Streams** sources, select **Shopify**.
  3. Assign a name to your source and click **Continue**.


> ![warning](/docs/images/warning.svg)
> 
> Ignore the **Disable client side identifier in the Legacy Shopify Tracker App** setting as it only pertains to the [Legacy Shopify integration](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/legacy-app/>).

Your Shopify source is now configured. Go to the **Setup** tab and note the source **Write key**. Also, note your workspace’s data plane URL. These are required while configuring the RudderStack Pixel app in your Shopify store.

[![Shopify source write key](/docs/images/event-stream-sources/shopify-source-write-key.webp)](</docs/images/event-stream-sources/shopify-source-write-key.webp>)

### Setup: Shopify

  1. Go to the RudderStack Pixel app in the Shopify App Store. Then, download it to your Shopify store.
  2. Enter the data plane URL and the source write key obtained above in the app’s settings page.


> ![info](/docs/images/info.svg)
> 
> The **Subscribed to Webhook Events** setting will be turned on by default.

  3. Turn off the **Track Events via Shopify App Pixel** and verify the **Off** label.

[![RudderStack Pixel app settings](/docs/images/event-stream-sources/shopify/hybrid-rudderstack-pixel-app-settings.webp)](</docs/images/event-stream-sources/shopify/hybrid-rudderstack-pixel-app-settings.webp>)

> ![info](/docs/images/info.svg)
> 
> You **do not** need to connect the **RudderStack App Embed Script** as this setting is applicable only for the Fully Shopify-hosted store setup.

  4. Click the **Submit** button to complete the app installation process.


#### Custom pixel setup

  1. Click the **Settings** icon at the bottom left of the dashboard.
  2. In the resulting **Settings** pop-up, click **Customer Events**.

[![RudderStack Pixel settings Customer Events](/docs/images/event-stream-sources/shopify/shopify-settings-customer-events.webp)](</docs/images/event-stream-sources/shopify/shopify-settings-customer-events.webp>)

  3. Click the **Add custom pixel** button at the top.

[![Add custom pixel button](/docs/images/event-stream-sources/shopify/add-custom-pixel.webp)](</docs/images/event-stream-sources/shopify/add-custom-pixel.webp>)

  4. Assign a name of your choice to this pixel. Then, click **Add pixel**.

[![Name and add custom pixel](/docs/images/event-stream-sources/shopify/name-add-custom-pixel.webp)](</docs/images/event-stream-sources/shopify/name-add-custom-pixel.webp>)

  5. In the code section, paste the [RudderStack Custom Pixel script](<https://github.com/rudderlabs/shopify-custom-pixel/blob/main/src/index.js>).


> ![warning](/docs/images/warning.svg)
> 
> Make sure to update the data plane URL and source write key in the script before pasting it.

  6. Click **Connect** to connect the custom pixel to your store.


### Pros and cons

**Pros**

  * Because of the relaxed permissions for the custom pixels, you can load the [RudderStack JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) on your Shopify store. Also, your first-party cookies that RudderStack loads and uses in the non-Shopify part of the site are accessible from the Shopify-hosted checkout part as well.
  * You can add custom events to the custom pixel code script and edit the tracking script as required.
  * This solution supports sending pixel events to both cloud mode and device mode integrations.


**Cons**

  * Identity stitching between the pixel events from the client and the webhook events from the Shopify backend is not guaranteed. You must deploy a manual HTTP request so that these events can be stitched together. See the [Identity Stitching](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/id-stitching/>) guide for more information on how to do this.


## 3\. Fully headless store with Shopify backend

Follow the guidelines in this section to set up your Shopify Source Solution if your store meets the following conditions:

  * If your store is completely custom and not hosted by Shopify.
  * You manage customers, orders, and inventories through Shopify’s backend.


> ![info](/docs/images/info.svg)
> 
> This is a rare scenario given the recent Checkout Extensibility changes by Shopify.

### Products used

  * [RudderStack Pixel](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/products/#rudderstack-pixel>)


### Event tracking methods

  * [Webhook events](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/event-tracking/#webhook-events>)


### Setup: RudderStack

  1. Log in to your [RudderStack dashboard](<https://app.rudderstack.com/>) and click **Add Source**.
  2. From the list of **Event Streams** sources, select **Shopify**.
  3. Assign a name to your source and click **Continue**.


> ![warning](/docs/images/warning.svg)
> 
> Ignore the **Disable client side identifier in the Legacy Shopify Tracker App** setting as it only pertains to the [Legacy Shopify integration](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/legacy-app/>).

Your Shopify source is now configured. Go to the **Setup** tab and note the source **Write key**. Also, note your workspace’s data plane URL. These are required while configuring the RudderStack Pixel app in your Shopify store.

[![Shopify source write key](/docs/images/event-stream-sources/shopify-source-write-key.webp)](</docs/images/event-stream-sources/shopify-source-write-key.webp>)

> ![warning](/docs/images/warning.svg)
> 
> This Shopify source must be different from the source collecting events from your online store.

### Setup: Shopify

  1. Go to the RudderStack Pixel app in the Shopify App Store. Then, download it to your Shopify store.
  2. Enter the data plane URL and the source write key obtained above in the app’s settings page.


> ![info](/docs/images/info.svg)
> 
> The **Subscribed to Webhook Events** setting will be turned on by default.

  3. Turn off the **Track Events via Shopify App Pixel** and verify the **Off** label.

[![RudderStack Pixel app settings](/docs/images/event-stream-sources/shopify/headless-rudderstack-pixel-app-settings.webp)](</docs/images/event-stream-sources/shopify/headless-rudderstack-pixel-app-settings.webp>)

> ![info](/docs/images/info.svg)
> 
> You **do not** need to connect the **RudderStack App Embed Script** as this setting is applicable only for the Fully Shopify-hosted store setup.

  4. Click the **Submit** button.


### Pros and cons

**Pros**

  * You can track your customer events through your own implementation with the [RudderStack JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>)
  * This solution gives you access to the reliable backend events from the Shopify [webhook topics](<https://shopify.dev/docs/api/webhooks?reference=toml#list-of-topics>).


**Cons**

  * Because this solution only sends webhook events, it only supports [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) integrations. However, your fully headless website will likely have a normal setup and can leverage device mode integrations and all the features from the RudderStack JavaScript SDK.
  * Identity stitching between the pixel events from the client and the webhook events from the Shopify backend is not guaranteed. You must deploy a manual HTTP request so that these events can be stitched together. See the [Identity Stitching](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/id-stitching/>) guide for more information on how to do this.


## Additional scenarios

This section covers some more scenarios around setting up and using the RudderStack Shopify Source Solution based on your store setup and event tracking requirements.

### Custom pixel only

You may have a scenario where you only want to track client-side events via the [Shopify Custom Pixel](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/products/#shopify-custom-pixel>).

You may want to do this for the following reasons:

  * You require the RudderStack JavaScript SDK to be loaded on the website to leverage the SDK’s features.
  * You may not want to track any webhook events due to the additional event volume or complexity when it comes to stitching user identities.


If your situation fits into any of the above scenarios, you can follow [these instructions](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/scenarios/#setup-shopify-hybrid>) (starting from **Step 4**) to set up the custom pixel on your store.

Note that:

  * If your store is based on a fully-hosted Shopify template, then this custom pixel will be able to load the RudderStack JavaScript SDK and track all the standard pixel events that Shopify offers for the customer’s ecommerce journey.
  * If you are using a hybrid headless Shopify store setup, then the custom pixel will only track the checkout events. You will need to instrument event tracking for the part of the website that is not hosted by Shopify.


> ![warning](/docs/images/warning.svg)
> 
> As the [RudderStack Pixel](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/products/#rudderstack-pixel>) app is not loaded in this scenario, you will **not** receive any server-side webhook events.

#### Pros and cons

**Pros**

  * You gain access to the advantages of the Shopify Custom Pixel, like having the flexibility to customize event tracking and add/remove events from being tracked. Also, you have the ability to load the RudderStack JavaScript SDK on your website and utilize all its features.
  * You do not need to be concerned about identity stitching for any webhook events.


**Cons**

  * As server-side webhook events are not tracked, your solution lacks the enhanced data that these events provide.


### Fully-hosted Shopify template with custom pixel and RudderStack Pixel

This scenario is similar to Store fully hosted on Shopify template. However, instead of leveraging the [RudderStack Pixel](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/products/#rudderstack-pixel>) app to track the client-side events, you may want to track client side events via [Shopify Custom Pixel](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/shopify/shopify-source-solution/products/#shopify-custom-pixel>) for the following reasons:

  * You require the RudderStack JavaScript SDK to be loaded on the website to leverage the SDK’s features.
  * You may also want to change how the events are tracked, add additional custom events, or even remove some of the standard events.


If your situation fits into any of the above scenarios, you can follow the instructions listed in Hybrid headless store with Shopify-hosted checkout to set up the solution on your store.

> ![warning](/docs/images/warning.svg)
> 
> Make sure that your custom pixel points to the JavaScript source set up in RudderStack and **not** the Shopify source.

#### Pros and cons

**Pros**

  * You gain access to the advantages of the Shopify Custom Pixel, like having the flexibility to customize event tracking and add/remove events from being tracked.
  * You have the ability to load the RudderStack JavaScript SDK on your website and utilize all its features.


**Cons**

  * As you are using the Shopify Custom Pixel for this implementation, you will need to maintain the code for any future updates.