# Integrate JavaScript SDK v3 with your React App

* * *

  *  __4 minute read

  * 


This guide will help you integrate RudderStack with your React app using the [JavaScript SDK v3](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>). On successful integration, you can track and send real-time user events to your preferred destinations via RudderStack.

To set up the event stream on your React app, you need to perform the following steps:

  1. Integrate JavaScript SDK with your React app and set up the tracking code.
  2. Configure a destination in RudderStack.
  3. Deploy your React app and verify the events.


## Integrate JavaScript SDK with your React app

Integrating the JavaScript SDK with your React app involves the following steps:

  1. Creating a JavaScript source in RudderStack.
  2. Installing and configuring the JavaScript SDK in your React app.


### Create a JavaScript source

The RudderStack JavaScript source is required track the events from your React app. Follow these steps to set it up in your [RudderStack dashboard](<https://app.rudderstack.com/>):

  1. Note the data plane URL in your RudderStack dashboard. This is required to set up the JavaScript SDK in your React app.

[![Data Plane URL](/docs/images/rs-cloud/data-plane-url.webp)](</docs/images/rs-cloud/data-plane-url.webp>)

  2. Click the **Sources** button in the left navigation bar and select **New Source** to create a source. Under **Sources** , select **Event Streams** > **JavaScript**.
  3. Assign a name to your source and click **Continue**.
  4. Your JavaScript source is now configured. Note down the write key for this source:

[![JavaScript source write key](/docs/images/user-guides/jamstack-guides/js-write-key.webp)](</docs/images/user-guides/jamstack-guides/js-write-key.webp>)

### Install and configure the SDK in your app

You can integrate RudderStack with your React app and set up the tracking code by following the steps below:

  1. In your React project folder, create a `useRudderAnalytics.ts` file within the `src` folder, and add the following code:


    
    
    import { useEffect, useState } from 'react';
    import { RudderAnalytics } from '@rudderstack/analytics-js';
    
    const useRudderStackAnalytics = (): RudderAnalytics | undefined => {
      const [analytics, setAnalytics] = useState<RudderAnalytics>();
    
      useEffect(() => {
        if (!analytics) {
          const analyticsInstance = new RudderAnalytics();
          analyticsInstance.load('WRITE_KEY', 'DATA_PLANE_URL');
    
          analyticsInstance.ready(() => {
            console.log('We are all set!!!');
          });
          
          setAnalytics(analyticsInstance);
        }
      }, [analytics]);
    
      return analytics;
    };
    
    export default useRudderStackAnalytics;
    

  2. Replace `WRITE_KEY` and `DATA_PLANE_URL` with your JavaScript source write key and the data plane URL obtained in the Creating a JavaScript source in RudderStack section above.
  3. Add the following code in your `App.tsx` file:


    
    
    import { useEffect } from 'react';
    import useRudderStackAnalytics from './useRudderAnalytics';
    
    function App() {
      const analytics = useRudderStackAnalytics();
    
      useEffect(() => {
        if (analytics) {
          analytics.page('Auto track');
        }
      }, [analytics]);
    
      const page = () => {
        analytics?.page('Cart Viewed');
      };
      const identify = () => {
        analytics?.identify('sample-user-123');
      };
      const track = () => {
        analytics?.track('Order Completed');
      };
      
    
      return (
        <div className='App'>
          <header className='App-header'>
            <img src={logo} className='App-logo' alt='logo' />
            <p>
              Edit <code>src/App.tsx</code> and save to reload.
            </p>
            <div className='card'>
              <button onClick={page}>page</button>
              <button onClick={identify}>identify</button>
              <button onClick={track}>track</button>
            </div>
          </header>
        </div>
      );
    }
    

  4. To buffer the events triggered before the SDK is loaded, add the following script in the `index.html` file within the `public` folder:


    
    
    <script>
    window.rudderanalytics = [];
    var methods = [
      'setDefaultInstanceKey',
      'load',
      'ready',
      'page',
      'track',
      'identify',
      'alias',
      'group',
      'reset',
      'setAnonymousId',
      'startSession',
      'endSession',
      'consent'
    ];
    for (var i = 0; i < methods.length; i++) {
      var method = methods[i];
      window.rudderanalytics[method] = (function(methodName) {
        return function() {
          window.rudderanalytics.push([methodName].concat(Array.prototype.slice.call(arguments)));
        };
      })(method);
    }
    
    // Below line is only for demonstration purpose, SPA code is better place for auto page call
    
    window.rudderanalytics.page('sample page call');
    </script>
    

See the [sample React app](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/examples/reactjs/hooks/sample-app>) for more information.

## Configure a destination in RudderStack

This section details the steps required to set up a destination in RudderStack, where you can send all events tracked by the JavaScript SDK you set up above.

  1. In your RudderStack dashboard, click **Destinations** > **New destination**.
  2. Choose your preferred destination from the list.
  3. Assign a name to the destination and click **Continue**.
  4. Select the JavaScript source configured in the above section and click **Continue**.
  5. Configure the destination with the required settings.


Optionally, you can add a [user transformation](<https://www.rudderstack.com/docs/transformations/overview/>) to this destination to transform your events.

## Deploy your app and verify events

To verify if your event stream is working correctly, deploy your React app and test if the events are tracked and delivered correctly. To do so, follow these steps:

  1. From your terminal, navigate to the folder containing your React app and run following command:


    
    
    npm run start
    

  2. Open the local server URL(generally `http://localhost:3000/`) in your browser to view the app.
  3. Go to your browser’s developer tools and open the **Network** tab. Click the buttons in your app to trigger the RudderStack events.
  4. Verify in the **Network** tab if the events are sent successfully:

[![Verifying events](/docs/images/user-guides/jamstack-guides/angular-network-tab.webp)](</docs/images/user-guides/jamstack-guides/angular-network-tab.webp>)

  5. Go to the **Live Events** tab of your JavaScript source in the RudderStack dashboard to check if the events are tracked. Note that you may face a minor delay before the events start showing up in your dashboard.
  6. Go to your destination to verify if the events are received successfully.