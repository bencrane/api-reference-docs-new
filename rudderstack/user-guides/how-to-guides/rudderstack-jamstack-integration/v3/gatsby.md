# Integrate JavaScript SDK v3 with your Gatsby website

* * *

  *  __4 minute read

  * 


You can quickly and easily get RudderStack up and running in your Gatsby application using RudderStack’s NPM package. It makes it easy to integrate your Gatsby website with the RudderStack API and easily track events.

To set up the event stream on your Gatsby app, you need to perform the following steps:

  1. Integrate JavaScript SDK with your Gatsby app and set up the tracking code.
  2. Configure a destination in RudderStack.
  3. Deploy your Gatsby app and verify the events.


## Integrate JavaScript SDK with your Gatsby app

Integrating the JavaScript SDK with your Gatsby app involves the following steps:

  1. Creating a JavaScript source in RudderStack.
  2. Installing and configuring the JavaScript SDK in your Gatsby app.


### Create a JavaScript source

The RudderStack JavaScript source is required track the events from your Gatsby app. Follow these steps to set it up in your [RudderStack dashboard](<https://app.rudderstack.com/>):

  1. Note the data plane URL in your RudderStack dashboard. This is required to set up the JavaScript SDK in your Gatsby app.

[![Data Plane URL](/docs/images/rs-cloud/data-plane-url.webp)](</docs/images/rs-cloud/data-plane-url.webp>)

  2. Click the **Sources** button in the left navigation bar and select **New Source** to create a source. Under **Sources** , select **Event Streams** > **JavaScript**.
  3. Assign a name to your source and click **Continue**.
  4. Your JavaScript source is now configured. Note down the write key for this source:

[![JavaScript source write key](/docs/images/user-guides/jamstack-guides/js-write-key.webp)](</docs/images/user-guides/jamstack-guides/js-write-key.webp>)

### Install and configure the SDK in your app

You can integrate RudderStack with your Gatsby app and set up the tracking code by following the steps below:

  1. Navigate to the root of your Gatsby project and install `@rudderstack/analytics-js` NPM package. For installation instructions, see [here](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/installation/#using-npm>).
  2. Go to the `pages` folder in `src` and add the following code in the `index.tsx` file:


    
    
    import { useEffect } from 'react';
    import { RudderAnalytics } from '@rudderstack/analytics-js';
    
    const page = () => {
      (window.rudderanalytics as RudderAnalytics).page('Cart Viewed');
    };
    const identify = () => {
      (window.rudderanalytics as RudderAnalytics).identify('sample-user-123');
    };
    const track = () => {
      (window.rudderanalytics as RudderAnalytics).track('Order Completed');
    };
    
    const buttons = [
      {
        text: 'Page',
        color: '#E95800',
        action: page,
      },
      {
        text: 'Identify',
        color: '#1099A8',
        action: identify,
      },
      {
        text: 'Track',
        color: '#BC027F',
        action: track,
      }
    ];
    
    const IndexPage: React.FC<PageProps> = () => {
      useEffect(() => {
        if (window.rudderanalytics as RudderAnalytics) {
          return;
        }
        const analytics = new RudderAnalytics();
    
        analytics.load('WRITE_KEY', 'DATA_PLANE_URL');
    
        analytics.ready(() => {
          console.log('We are all set!!!');
        });
      }, []);
    
      return (
        <main style={pageStyles}>
          <ul style={listStyles}>
            {buttons.map(btn => (
              <button onClick={btn.action} style={{ ...listItemStyles, color: btn.color }}>
                {btn.text}
              </button>
            ))}
            <span></span>
          </ul>
        </main>
      );
    };
    
    export default IndexPage;
    
    export const Head: HeadFC = () => <title>Home Page</title>;
    

  2. Replace `WRITE_KEY` and `DATA_PLANE_URL` with your JavaScript source write key and the data plane URL obtained in the Creating a JavaScript source in RudderStack section above.


See the [sample Gatsby app](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/examples/gatsby/sample-gatsby-site>) for more information.

## Configure a destination in RudderStack

This section details the steps required to set up a destination in RudderStack, where you can send all events tracked by the JavaScript SDK you set up above.

  1. In your RudderStack dashboard, click **Destinations** > **New destination**.
  2. Choose your preferred destination from the list.
  3. Assign a name to the destination and click **Continue**.
  4. Select the JavaScript source configured in the above section and click **Continue**.
  5. Configure the destination with the required settings.


Optionally, you can add a [user transformation](<https://www.rudderstack.com/docs/transformations/overview/>) to this destination to transform your events.

## Deploy your app and verify events

To verify if your event stream is working correctly, deploy your Gatsby app and test if the events are tracked and delivered correctly. To do so, follow these steps:

  1. From your terminal, navigate to the folder containing your Gatsby app and run following command:


    
    
    npm run develop
    

  2. Open the local server URL(generally `http://localhost:8000/`) in your browser to view the app.
  3. Go to your browser’s developer tools and open the **Network** tab. Click the buttons in your app to trigger the RudderStack events.
  4. Verify in the **Network** tab if the events are sent successfully:

[![Verifying events](/docs/images/user-guides/jamstack-guides/angular-network-tab.webp)](</docs/images/user-guides/jamstack-guides/angular-network-tab.webp>)

  5. Go to the **Live Events** tab of your JavaScript source in the RudderStack dashboard to check if the events are tracked. Note that you may face a minor delay before the events start showing up in your dashboard.
  6. Go to your destination to verify if the events are received successfully.