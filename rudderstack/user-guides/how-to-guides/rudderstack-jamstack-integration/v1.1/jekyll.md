# Integrate JavaScript SDK v1.1 with your Jekyll site

* * *

  *  __4 minute read

  * 


This guide will help you integrate RudderStack with your Jekyll site using the [RudderStack JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>). On successful integration, you can track and send real-time user events to your preferred destinations via RudderStack.

To set up the event stream on your Jekyll site, you need to perform the following steps:

  1. Integrate the JavaScript SDK with your Jekyll site and set up the tracking code
  2. Configure a destination in RudderStack
  3. Deploy your Jekyll site and verify the events


## Prerequisites

This guide assumes you have installed and set up your Jekyll site. Refer to the [Jekyll documentation](<https://jekyllrb.com/docs/installation/>) for more information.

## Integrating the JavaScript SDK with your Jekyll site

Integrating the JavaScript SDK with your Jekyll site involves the following steps:

  1. Creating a JavaScript source in RudderStack
  2. Installing and configuring the JavaScript SDK in your Jekyll site


### Creating a JavaScript source in RudderStack

The RudderStack JavaScript source is required track the events from your Jekyll app. Follow these steps to set it up in your [RudderStack dashboard](<https://app.rudderstack.com/>):

  1. Note the data plane URL in your RudderStack dashboard. This is required to set up the JavaScript SDK in your Jekyll app.

[![Data Plane URL](/docs/images/rs-cloud/data-plane-url.webp)](</docs/images/rs-cloud/data-plane-url.webp>)

  2. Click the **Sources** button in the left navigation bar and select **New Source** to create a source. Under **Sources** , select **Event Streams** > **JavaScript**.
  3. Assign a name to your source and click **Continue**.
  4. Your JavaScript source is now configured. Note down the write key for this source:

[![JavaScript source write key](/docs/images/user-guides/jamstack-guides/write-key.webp)](</docs/images/user-guides/jamstack-guides/write-key.webp>)

### Installing and configuring the JavaScript SDK in your Jekyll site

Jekyll has an extensive theme system that helps customize your site’s presentation. **Minima** is Jekyll’s default theme. You can check your default Jekyll theme using the following command:
    
    
    bundle info --path
    

The following command opens an explorer window showing the theme files and directories:
    
    
    open $(bundle info --path)
    

To integrate RudderStack with your Jekyll site and set up the tracking code, follow the steps below:

  1. Create a `rudder.html` inside the `_includes` folder in your Jekyll theme’s folder and include the following script:


    
    
    <script>
      rudderanalytics = window.rudderanalytics = [];
      var methods = [
        "load",
        "page",
        "track",
        "identify",
        "alias",
        "group",
        "ready",
        "reset",
        "setAnonymousId",
        "getAnonymousId",
      ];
      for (var i = 0; i < methods.length; i++) {
        var method = methods[i];
        rudderanalytics[method] = (function (methodName) {
          return function () {
            rudderanalytics.push(
              [methodName].concat(Array.prototype.slice.call(arguments))
            );
          };
        })(method);
      }
      rudderanalytics.load(
        "WRITE_KEY",
        "DATA_PLANE_URL"
      );
      rudderanalytics.ready(function () {
        console.log("Application is ready with JS");
      });
      rudderanalytics.track("Simple track call");
    </script>
    <script src="https://cdn.rudderlabs.com/v1.1/rudder-analytics.min.js"></script>
    

> ![info](/docs/images/info.svg)
> 
> If you are using an older version of the JavaScript SDK, see the [Version Migration Guide](<https://www.rudderstack.com/docs/archive/javascript-sdk/1.1/version-migration-guide/>) to migrate to SDK v1.1.

  2. Replace `<WRITE_KEY>` and `<DATA_PLANE_URL>` with your JavaScript source write key and the data plane URL obtained in the Creating a JavaScript source in RudderStack section above.
  3. Go to the `_includes/head.html` file of your theme folder and run the following command:


    
    
    {%- include rudder.html -%}
    

> ![info](/docs/images/info.svg)
> 
> See the sample Jekyll site in the [RudderStack Sample Applications](<https://github.com/rudderlabs/rudder-samples/tree/master/javascript/sample-jekyll-site>) repository for more information.

## Configuring a destination in RudderStack

This section details the steps required to set up a destination in RudderStack, where you can send all events tracked by the JavaScript SDK you set up above.

  1. In your RudderStack dashboard, click **Destinations** > **New destination**.
  2. Choose your preferred destination from the list.
  3. Assign a name to the destination and click **Continue**.
  4. Select the JavaScript source configured in the above section and click **Continue**.
  5. Configure the destination with the required settings.


> ![info](/docs/images/info.svg)
> 
> Optionally, you can add a [user transformations](<https://www.rudderstack.com/docs/transformations/overview/>) to this destination to transform your events.

## Deploying your Jekyll site and verifying the event stream

To verify if your event stream is working correctly, deploy your Jekyll site and test if the events are tracked and delivered correctly. Follow these steps:

  1. From your terminal, navigate to the folder containing your Jekyll site and run following command:


    
    
    bundle exec jekyll serve
    

  2. Open the local server URL(generally `http://localhost:4000/`) in your browser to view the site.
  3. Go to your browser’s developer tools and check the **Network** tab to verify if the RudderStack JavaScript SDK (`rudder-analytics.js`) is loaded correctly. The following image highlights this option for the Google Chrome browser:

[![Chrome Network tab](/docs/images/user-guides/browser-network-tab.webp)](</docs/images/user-guides/browser-network-tab.webp>)

  4. Click the various links or pages in your site for RudderStack to track these actions.
  5. Go to the **Live Events** tab of your JavaScript source in the RudderStack dashboard to check if the events are tracked. Note that you may face a minor delay before the events start showing up in your dashboard.
  6. Go to your destination to verify if the events are received successfully.