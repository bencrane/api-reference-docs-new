# Google Tag Manager Web Device Mode Integration

Send events to Google Tag Manager using RudderStack web device mode.

* * *

  * __3 minute read

  * 


After you have successfully instrumented Google Tag Manager as a destination in RudderStack, follow this guide to correctly send your events to Google Tag Manager in [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).

Find the open source JavaScript SDK code for this integration in the [GitHub repository](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/GoogleTagManager>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to identify a user, and send their information like name, email, etc. to Google Tag Manager.

A sample `identify` call is shown:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm",{
    "name":"Alex Keener",
    "gender":"Male",
    "city":"New Orleans"
    })
    

The above call populates Google Tag Manager with a `traits` object containing all user traits (like `name`, `gender`, `city`, etc.)

## Page

> ![warning](/docs/images/warning.svg)
> 
> You must call the `page` event to load Google Tag Manager.

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call allows you to record whenever a user visits a page of your website, along with the properties associated with that page.

When you make a `page` call, RudderStack sends an object to the GTM data layer containing your page-related properties and an event name with its associated value. All properties you pass in the `page` call are spread into the data layer object.

### Event naming logic

The integration automatically generates an event name for the GTM data layer based on the page name and category you provide. The event naming logic is explained below:

Condition| Event name  
---|---  
Only page name is provided| `Viewed {name} page`  
Page name and category are provided| `Viewed {category} {name} page`  
No page name is provided| `Viewed a Page`  
  
Some examples of how event names are generated based on the above conditions are shown below:
    
    
    rudderanalytics.page("Home", {
      path: "/home",
      url: "https://example.com/home",
      title: "Home Page",
      search: "",
      referrer: "https://example.com"
    });
    

The above `page` call populates Google Tag Manager with the following properties:

  * `event` (`Viewed Home page`)
  * `userId`
  * `anonymousId`
  * `traits` (user traits persisted from previous `identify` calls, if any)
  * `path`
  * `url`
  * `title`
  * `search`
  * `referrer`
  * `messageId`


    
    
    rudderanalytics.page("Products", {
      category: "Electronics",
      path: "/products/electronics",
      url: "https://example.com/products/electronics",
      title: "Electronics Products"
    });
    

The above `page` call populates Google Tag Manager with the following properties:

  * `event` (`Viewed Electronics Products page`)
  * `userId`
  * `anonymousId`
  * `traits` (user traits persisted from previous `identify` calls, if any)
  * `category`
  * `path`
  * `url`
  * `title`
  * `messageId`


    
    
    rudderanalytics.page({
      path: "/about",
      url: "https://example.com/about",
      title: "About Us"
    });
    

This call populates Google Tag Manager with the following properties:

  * `event` (`Viewed a Page`)
  * `userId`
  * `anonymousId`
  * `traits` (user traits persisted from previous `identify` calls, if any)
  * `path`
  * `url`
  * `title`
  * `messageId`


## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record any user actions along with the properties associated with those actions.

> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Use the `track` events to populate the Google Tag Manager data layer once you have set up and enabled Google Tag Manager in RudderStack.

Calling the RudderStack SDK `track` method with the event and its properties similarly passes the data to GTM as seen in the `page` section above.
    
    
    rudderanalytics.track("Track Event", {
      category: "category",
      label: "label",
      value: "value",
    });
    

The above call populates Google Tag Manager with the following properties:

  * `event` (`Track Event`)
  * `userId`
  * `anonymousId`
  * `traits` (traits persisted from previous `identify` calls, if any)
  * `category`
  * `label`
  * `value`
  * `messageId`