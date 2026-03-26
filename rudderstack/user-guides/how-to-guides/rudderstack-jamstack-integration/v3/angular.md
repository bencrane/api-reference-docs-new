# Integrate JavaScript SDK v3 with your Angular app

* * *

  *  __4 minute read

  * 


This guide will help you integrate RudderStack with your Angular app using the [JavaScript SDK v3](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>). On successful integration, you can track and send real-time user events to your preferred destinations via RudderStack.

To set up the event stream on your Angular app, you need to perform the following steps:

  1. Integrate the JavaScript SDK with your Angular app and set up the tracking code.
  2. Configure a destination in RudderStack.
  3. Deploy your Angular app and verify the events.


## Prerequisites

This guide assumes you have installed and set up your Angular app. Refer to the [Angular documentation](<https://angular.io/guide/setup-local>) for more information.

## Integrate JavaScript SDK with your Angular app

Integrating the JavaScript SDK with your Angular app involves the following steps:

  1. Creating a JavaScript source in RudderStack
  2. Installing and configuring the JavaScript SDK in your Angular app


### Create a JavaScript source

The RudderStack JavaScript source is required track the events from your Angular app. Follow these steps to set it up in your [RudderStack dashboard](<https://app.rudderstack.com/>):

  1. Note the data plane URL in your RudderStack dashboard. This is required to set up the JavaScript SDK in your Angular app.

[![Data Plane URL](/docs/images/rs-cloud/data-plane-url.webp)](</docs/images/rs-cloud/data-plane-url.webp>)

  2. Click the **Sources** button in the left navigation bar and select **New Source** to create a source. Under **Sources** , select **Event Streams** > **JavaScript**.
  3. Assign a name to your source and click **Continue**.
  4. Your JavaScript source is now configured. Note down the write key for this source:

[![JavaScript source write key](/docs/images/user-guides/jamstack-guides/js-write-key.webp)](</docs/images/user-guides/jamstack-guides/js-write-key.webp>)

### Install and configure the SDK in your app

To integrate RudderStack with your Angular app and set up the tracking code, follow the steps below:

  1. Navigate to the root of your Angular project and install the `@rudderstack/analytics-js` NPM package. For installation instructions, see [here](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/installation/#using-npm>).
  2. In the `src` folder of your project, open `app.component.ts`, and add the following:


a. Import the `RudderAnalytics` package:
    
    
    import { RudderAnalytics } from '@rudderstack/analytics-js';
    

b. Modify `AppComponent` as follows:
    
    
    export class AppComponent implements OnInit, OnDestroy {
      title = 'sample-app';
      analytics: RudderAnalytics | undefined;
      routerEventSubscription: Subscription | undefined;
    
      constructor(private _router: Router) {}
      ngOnInit() {
        this.initialize();
    
        this.routerEventSubscription = this._router.events.subscribe(event => {
          if (event instanceof NavigationStart) {
            this.analytics?.page(event.url);
          }
        });
      }
    
      initialize() {
        if (window.rudderanalytics as RudderAnalytics) {
          return;
        }
        this.analytics = new RudderAnalytics();
    
        this.analytics.load('WRITE_KEY', 'DATA_PLANE_URL');
    
        this.analytics.ready(() => {
          console.log('We are all set!!!');
        });
      }
    
      page() {
        this.analytics?.page('Cart Viewed');
      }
      identify() {
        this.analytics?.identify('sample-user-123');
      }
      track() {
        this.analytics?.track('Order Completed');
      }
    
      public ngOnDestroy(): void {
        this.routerEventSubscription?.unsubscribe();
      }
    }
    

c. Add buttons in the `app.component.html` file to trigger your `page`, `identify`, and `track` events:
    
    
    <button class="card" (click)="page()">
        <span>Page</span>
    </button>
    <button class="card" (click)="identify()">
        <span>Identify</span>
    </button>
    

  3. Replace `WRITE_KEY` and `DATA_PLANE_URL` with your JavaScript source write key and the data plane URL obtained in the Creating a JavaScript source in RudderStack section above.
  4. To buffer the events triggered before the SDK is loaded, add the following script in the `<head>` section of your `index.html` file within the `src` folder:


    
    
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
    

See the [sample Angular app](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/examples/angular/sample-app>) for more information.

## Configure a destination in RudderStack

This section details the steps required to set up a destination in RudderStack, where you can send all events tracked by the JavaScript SDK you set up above.

  1. In your RudderStack dashboard, click **Destinations** > **New destination**.
  2. Choose your preferred destination from the list.
  3. Assign a name to the destination and click **Continue**.
  4. Select the JavaScript source configured in the above section and click **Continue**.
  5. Configure the destination with the required settings.


Optionally, you can add a [user transformation](<https://www.rudderstack.com/docs/transformations/overview/>) to this destination to transform your events.

## Deploy your app and verify events

To verify if your event stream is working correctly, deploy your Angular app and test if the events are tracked and delivered correctly. To do so, follow these steps:

  1. From your terminal, navigate to your Angular project’s root folder and run the following command:


    
    
    ng serve
    

  2. Open the local server URL(generally `http://localhost:4200/`) in your browser to view the app.
  3. Go to your browser’s developer tools and open the **Network** tab. Click the buttons in your app (Step 2.c in Installing and configuring the JavaScript SDK in your Angular app) to trigger the RudderStack events.
  4. Verify in the **Network** tab if the events are sent successfully:

[![Verifying events](/docs/images/user-guides/jamstack-guides/angular-network-tab.webp)](</docs/images/user-guides/jamstack-guides/angular-network-tab.webp>)

  5. Go to the **Live Events** tab of your JavaScript source in the RudderStack dashboard to check if the events are tracked. Note that you may face a minor delay before the events start showing up in your dashboard.
  6. Go to your destination to verify if the events are received successfully.