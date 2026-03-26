# Integrate JavaScript SDK v3 with your Next.js App

* * *

  *  __5 minute read

  * 


This guide will help you integrate RudderStack with your Next.js app using the [JavaScript SDK v3](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>). On successful integration, you can track and send real-time user events to your preferred destinations via RudderStack.

To set up the event stream on your Next.js app, you need to perform the following steps:

  1. Integrate JavaScript SDK with your Next.js app and set up the tracking code.
  2. Configure a destination in RudderStack.
  3. Deploy your Next.js app and verify the events.


## Prerequisites

This guide assumes you have installed and set up your Next.js app. Refer to the [Next.js documentation](<https://nextjs.org/docs/getting-started>) for more information.

## Integrate JavaScript SDK with your Next.js app

Integrating the JavaScript SDK with your Next.js app involves the following steps:

  1. Creating a JavaScript source in RudderStack.
  2. Installing and configuring the JavaScript SDK in your Next.js app.


### Create a JavaScript source

The RudderStack JavaScript source is required track the events from your Next.js app. Follow these steps to set it up in your [RudderStack dashboard](<https://app.rudderstack.com/>):

  1. Note the data plane URL in your RudderStack dashboard. This is required to set up the JavaScript SDK in your Next.js app.

[![Data Plane URL](/docs/images/rs-cloud/data-plane-url.webp)](</docs/images/rs-cloud/data-plane-url.webp>)

  2. Click the **Sources** button in the left navigation bar and select **New Source** to create a source. Under **Sources** , select **Event Streams** > **JavaScript**.
  3. Assign a name to your source and click **Continue**.
  4. Your JavaScript source is now configured. Note down the write key for this source:

[![JavaScript source write key](/docs/images/user-guides/jamstack-guides/js-write-key.webp)](</docs/images/user-guides/jamstack-guides/js-write-key.webp>)

### Install and configure the SDK in your app

You can integrate RudderStack with your Next.js app and set up the tracking code by following the steps below:

  1. In your Next.js project folder, create a `useRudderAnalytics.ts` file with the following code:


    
    
    import { useEffect, useState } from 'react';
    import type { RudderAnalytics } from '@rudderstack/analytics-js';
    
    const useRudderStackAnalytics = (): RudderAnalytics | undefined => {
      const [analytics, setAnalytics] = useState<RudderAnalytics>();
    
      useEffect(() => {
        if (!analytics) {
          const initialize = async () => {
            const { RudderAnalytics } = await import('@rudderstack/analytics-js');
            const analyticsInstance = new RudderAnalytics();
    
            analyticsInstance.load('WRITE_KEY', 'DATA_PLANE_URL');
    
            analyticsInstance.ready(() => {
              console.log('We are all set!!!');
            });
            
            setAnalytics(analyticsInstance);
          };
    
          initialize().catch(e => console.log(e));
        }
      }, [analytics]);
    
      return analytics;
    };
    
    export default useRudderStackAnalytics;
    

  2. Replace `WRITE_KEY` and `DATA_PLANE_URL` with your JavaScript source write key and the data plane URL obtained in the Creating a JavaScript source in RudderStack section above.
  3. To buffer the events triggered before the SDK is loaded, add the following script in the `layout.tsx` file within the `src` folder:


    
    
    import Script from 'next/script';
    
    export default function RootLayout({ children }: { children: React.ReactNode }) {
      return (
        <html lang='en'>
          <head>
            <Script id='bufferEvents'>
              {`
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
                  window.rudderanalytics[method] = (function (methodName) {
                    return function () {
                      window.rudderanalytics.push([methodName].concat(Array.prototype.slice.call(arguments)));
                    };
                  })(method);
                }
                // Below line is only for demonstration purpose, SPA code is better place for auto page call
                window.rudderanalytics.page('sample page call');
            `}
            </Script>
          </head>
          <body className={inter.className}>{children}</body>
        </html>
      );
    }
    

  4. If you are using an app router, go to the `app` folder and open the `page.tsx` file. If you are using a page router, go to the `pages` folder and open the `index.tsx` file. Then, add the following code:


    
    
    import { useEffect } from "react";
    import useRudderStackAnalytics from './useRudderAnalytics';
    
    export default function Home() {
      const analytics = useRudderStackAnalytics();
    
      const page = () => {
        analytics?.page('Cart Viewed');
      };
      const identify = () => {
        analytics?.identify('sample-user-123');
      };
      const track = () => {
        analytics?.track('Order Completed');
      };
    
      useEffect(() => {
        if(analytics) {
          analytics.page('Auto track');
        }
      }, [analytics])
    
    return (
        <main className='flex min-h-screen flex-col items-center justify-between p-24'>
          <div className='mb-32 grid text-center lg:max-w-5xl lg:w-full lg:mb-0 lg:grid-cols-4 lg:text-left'>
            <button
              onClick={page}
              className='group rounded-lg border border-transparent px-5 py-4 transition-colors hover:border-gray-300 hover:bg-gray-100 hover:dark:border-neutral-700 hover:dark:bg-neutral-800/30'>
              <h2 className={`mb-3 text-2xl font-semibold`}>Page </h2>
              <p className={`m-0 max-w-[30ch] text-sm opacity-50`}>
                Clicking this tile will trigger a page event.
              </p>
            </button>
         </div>
    	</main>
     );
    }
    

See the [sample Next.js app](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/examples/nextjs/hooks/sample-app>) for more information.

## Configure a destination in RudderStack

This section details the steps required to set up a destination in RudderStack, where you can send all events tracked by the JavaScript SDK you set up above.

  1. In your RudderStack dashboard, click **Destinations** > **New destination**.
  2. Choose your preferred destination from the list.
  3. Assign a name to the destination and click **Continue**.
  4. Select the JavaScript source configured in the above section and click **Continue**.
  5. Configure the destination with the required settings.


Optionally, you can add a [user transformation](<https://www.rudderstack.com/docs/transformations/overview/>) to this destination to transform your events.

## Deploy your app and verify events

To verify if your event stream is working correctly, deploy your Next.js app and test if the events are tracked and delivered correctly. To do so, follow these steps:

  1. From your terminal, navigate to the folder containing your Next.js app and run following command:


    
    
    npm run dev
    

  2. Open the local server URL(generally `http://localhost:3000/`) in your browser to view the app.
  3. Go to your browser’s developer tools and open the **Network** tab. Click the buttons in your app to trigger the RudderStack events.
  4. Verify in the **Network** tab if the events are sent successfully:

[![Verifying events](/docs/images/user-guides/jamstack-guides/angular-network-tab.webp)](</docs/images/user-guides/jamstack-guides/angular-network-tab.webp>)

  5. Go to the **Live Events** tab of your JavaScript source in the RudderStack dashboard to check if the events are tracked. Note that you may face a minor delay before the events start showing up in your dashboard.
  6. Go to your destination to verify if the events are received successfully.