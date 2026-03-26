# VWO (Visual Website Optimizer)

Send data from RudderStack to VWO.

* * *

  * __5 minute read

  * 


[VWO](<https://vwo.com/>) (Visual Website Optimizer) is an A/B testing and product optimization platform. It provides an intuitive visual editor where you can run A/B tests without the need to write any HTML code.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/VWO>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **VWO** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the VWO native SDK from the `http://visualwebsiteoptimizer.com` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the VWO SDK successfully.

## Get started

Once you have confirmed that the source platform supports sending events to VWO, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **VWO**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

  * **Account ID** : Enter your VWO account ID. For more information on obtaining your VWO account ID, refer to the FAQ section below.
  * **Single Page Application(SPA)?** : Enable this setting if you’re loading the native VWO SDK on a single page application.
  * **Send experiment viewed as track** : Enable this setting to record your VWO experiment as a `track` event with the name `Experiment Viewed`. For more information on this setting, refer to the Sending experiment viewed from VWO section below.
  * **Send experiment viewed as identify traits** : Enable this setting to send your experiment data within the [traits](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/#identify-traits>) of your `identify` event.


> ![info](/docs/images/info.svg)
> 
> If you enable both the **Send experiment viewed as track** and **Send experiment viewed as identify traits** settings, then RudderStack independently captures the experiment details and sends them as `track` and `identify` events, respectively.

  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to VWO. For more information, refer to the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.
  * **Library Tolerance** : Specify the maximum time (in ms) RudderStack should wait for the VWO library to load before displaying your web page.
  * **Setting Tolerance** : Specify the maximum time (in ms) RudderStack should wait for the test settings before VWO displays your original web page.
  * **Use Existing jQuery** : Enable this setting if your page already includes jQuery. Otherwise, VWO will include jQuery on the page for you.


> ![warning](/docs/images/warning.svg)
> 
> To function correctly, VWO requires jQuery to be present in the web page.

  * **Use device mode to send events** : As this is a [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)-only destination, this setting is enabled by default and cannot be disabled.


## Loading the VWO SDK

By default, RudderStack **does not** load the VWO SDK automatically. To do so, you must [load the web SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/>) as follows:
    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      integrations: {
        VWO: {
          loadIntegration: true
        }
      }
    });
    

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to identify a user and send the information to VWO.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      "name": "Alex Keener",
      "email": "alex@example.com"
    });
    

### Sending user traits

RudderStack lets you send the experiment-related data like the user’s traits via an [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call, so that the other destinations have the necessary user-related context of the variations.

To do so, enable the **Send experiment viewed as identify traits** dashboard setting and include the user traits in the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) event.
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      "name": "Alex Keener",
      "email": "alex@example.com",
      "Experiment: 1234": "Signup as default landing"
    });
    

> ![info](/docs/images/info.svg)
> 
> RudderStack prefixes all the `identify` traits with `rudder.` before sending them to VWO. For example, RudderStack sends `email` as `rudder.email` to VWO.

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to send user events and their associated properties to VWO.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Item Purchased", {
      category: "MyCategory",
      currency: "INR",
      value: 500
    })
    

> ![info](/docs/images/info.svg)
> 
> RudderStack prefixes the event name with `rudder.` before sending it to VWO. For example, `Item Purchased` event is sent as `rudder.Item Purchased` to VWO.

### Sending `Experiment Viewed` as `track` event

When you enable the **Send experiment viewed as track** dashboard setting, RudderStack automatically sends a [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) event whenever an experiment variation is loaded for a user. It sets `Experiment Viewed` as the event name along with the experiment and variation details as the event properties.

You can then send this `track` event to the other destinations (connected to the same source in RudderStack) to analyze the experimentation results.

A sample code snippet for this activity is as shown:
    
    
    rudderanalytics.track("Experiment Viewed", {
      experimentId: "Signup",
      variationName: "Signup as a default landing"
    });
    

### Tracking revenue goals

RudderStack also lets you forward the revenue amount to VWO when the [`Order Completed`](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/ordering/#order-completed>) event is called.

> ![info](/docs/images/info.svg)
> 
> RudderStack uses the `revenue` or `total` property for tracking the revenue goals.

A sample code snippet for this activity is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      revenue: 125
    });
    

## FAQ

#### How do I add the VWO JavaScript snippet to my website?

To configure VWO SmartCode(JavaScript snippet) on all web pages where you plan to run your A/B tests, you can refer to this [VWO Knowledge Base](<https://help.vwo.com/hc/en-us/articles/360019422834>) article.

> ![warning](/docs/images/warning.svg)
> 
> Make sure you add the VWO snippet inside the `HEAD` tag of your web page, **above** the [RudderStack JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/quickstart/#step-1-install-rudderstack-javascript-sdk>) snippet.

#### Where can I find my VWO Account ID?

You can obtain the VWO Account ID by following these steps:

  1. Log into your [VWO dashboard](<https://app.vwo.com/#/login>).
  2. Click the settings icon on the top right and go to **Account**.


You will find your account ID listed under **Account Details**.

For more information, refer to the [VWO Knowledge Base](<https://help.vwo.com/hc/en-us/articles/360008469173-How-to-find-your-account-ID>).

#### How can I disable loading the VWO SDK for certain events?

By default, RudderStack **does not** load the VWO SDK automatically. However, if you have loaded the VWO SDK using this approach, you can disable it for certain events by setting `VWO` to `false` in the event’s `integrations` object:
    
    
    rudderanalytics.track(
      "Experiment Viewed", {
        revenue: 30,
        currency: "USD",
      }, {
        integrations: {
          VWO: false
        },
      }
    );