# Mouseflow

Send your event data from RudderStack to Mouseflow.

* * *

  * __5 minute read

  * 


[Mouseflow](<https://mouseflow.com/>) is a [behavioral analytics](<https://www.rudderstack.com/learn/data-analytics/what-is-behavioral-analytics/>) platform that gives you deeper insights into your users’ product journey.

RudderStack supports Mouseflow as a destination where you can send your event data seamlessly.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Mouseflow** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
> In the web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Mouseflow native SDK from the`https://cdn.mouseflow.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Mouseflow SDK successfully.

## Get started

Once you have confirmed that the source platform supports sending events to Mouseflow, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Mouseflow**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure Mouseflow as a destination, you need to configure the following settings:

[![Mouseflow connection settings](/docs/images/event-stream-destinations/mouseflow-connection-settings.webp)](</docs/images/event-stream-destinations/mouseflow-connection-settings.webp>)

  * **Website ID** : Enter your Mouseflow website ID.


> ![info](/docs/images/info.svg)
> 
> For more information on obtaining your Mouseflow website ID, refer to the [FAQ](<>) section below.

  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to Mouseflow.


> ![info](/docs/images/info.svg)
> 
> For more information on this setting, refer to the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.

  * **Use device mode to send events** : As this is a [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)-only destination, this setting is enabled by default and cannot be disabled.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you identify a visiting user and associate them to their actions. It also lets you record their traits like name, email address, etc. and send this information to Mouseflow.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      "email": "alex@example.com",
      "city": "New Orleans",
      "favouriteColor": "Red"
    })
    

### Supported mappings

RudderStack maps the following user traits to the corresponding Mouseflow properties:

RudderStack property| Mouseflow property| Presence  
---|---|---  
`userId` / `traits.email` / `anonymousId`| `_userName`| Required  
`traits`| `setVariable`| Optional  
  
### Identifying a user

RudderStack sends the `userId` / `email` / `anonymousId` to Mouseflow as `_userName` via the [`identifying a user`](<https://js-api-docs.mouseflow.com/#identifying-a-user>) method:
    
    
    mouseflow.identify(_userName)
    

### Setting custom variables

You can also send the user details present in the `traits` as key-value pair to Mouseflow. RudderStack passes them as [custom variables](<https://js-api-docs.mouseflow.com/#identifying-a-user:~:text=include%20%22product%2Dadded%22%2C%20...-,Setting%20a%20custom%20variable,-_mfq.push>) to Mouseflow:
    
    
    _mfq.push(["setVariable", _key, _value])
    

> ![warning](/docs/images/warning.svg)
> 
> The values in the key-value pairs passed as custom variables should be either strings or numbers. RudderStack will not pass the values with any other data type, for example, Boolean.

> ![info](/docs/images/info.svg)
> 
> You can also set custom variables by passing them via the event’s `integrations` object. Refer to the Setting custom variables via the section below for more information.

The following snippets highlight how the data in the sample `identify` call above is sent to Mouseflow:
    
    
    // Sending userId
    mouseflow.identify("1hKOmRA4GRlm");
    
    // Sending user traits as custom variables
    _mfq.push(["setVariable", "city", "New Orleans"]);
    _mfq.push(["setVariable", "email", "alex@example.com"]);
    _mfq.push(["setVariable", "favouriteColor", "Red"]);
    

## Track

You can use the RudderStack [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to [set tags or custom variables](<https://js-api-docs.mouseflow.com/#adding-custom-data>) in Mouseflow.

A sample `track` call is as shown:
    
    
    rudderanalytics.track("Product Clicked",{
    	"price": 100,
    	"quantity": 10,
    })
    

### Setting custom tags

RudderStack lets you set a custom tag to a user recording by using Mouseflow’s [Tagging a recording](<https://js-api-docs.mouseflow.com/#tagging-a-recording>) method.

> ![info](/docs/images/info.svg)
> 
> RudderStack automatically sets the `track` event name as the custom tag.

The below table highlights the property mapping:

RudderStack property| Mouseflow property| Presence  
---|---|---  
`event`| `_tag`| Required  
  
> ![warning](/docs/images/warning.svg)
> 
> A Mouseflow tag must always be of the String data type.

In the sample `track` call above, RudderStack sets `Product Clicked` as the custom tag by passing it to Mouseflow in the following way:
    
    
    _mfq.push(["tag", "Product Clicked"]);
    

### Setting custom variables

RudderStack also lets you pass the `track` event properties as custom variables to Mouseflow in the form of key-value pairs.

> ![warning](/docs/images/warning.svg)
> 
> The values in the key-value pairs should be either strings or numbers. RudderStack will not pass the values with any other data type, for example, Boolean.

In the sample `track` call above, RudderStack sets `price` and `quantity` as the custom variables:
    
    
    _mfq.push(["setVariable", "price", "100"]);
    _mfq.push(["setVariable", "quantity", "10"]);
    

> ![info](/docs/images/info.svg)
> 
> You can also set custom variables by passing them via the event’s `integrations` object. Refer to the Setting custom variables via the section below for more information.

## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you send the path of the web page viewed by the user to Mouseflow.

A sample `page` call is shown below:
    
    
    rudderanalytics.page({
      path: "/test_browser.html",
    });
    

RudderStack sends the page-related information like the path or the page URL to Mouseflow using the [Adding a virtual pageview](<https://js-api-docs.mouseflow.com/#virtual-paths-and-pageviews:~:text=%2C%20_virtualPath%5D>)%3B-,Adding%20a%20virtual%20pageview,-_mfq.push) method:
    
    
    _mfq.push(["newPageView", _virtualPath]);
    

### Supported mappings

You can customize the page-related details sent to Mouseflow by passing the values in the `properties.path` field. RudderStack then maps these details to the `_virtualPath` parameter before sending them to Mouseflow, as highlighted in the below table:

RudderStack property| Mouseflow property| Presence  
---|---|---  
`properties.path` / `context.path`| `_virtualPath`| Required  
  
The following snippet highlights how RudderStack sends the data in the sample `page` call above to Mouseflow:
    
    
    _mfq.push(["newPageView", "/test_browser.html"]);
    

## Setting custom variables via the `integrations` object

RudderStack enables you to send custom variables to Mouseflow via the `identify` and `track` calls by passing them via the [`integrations`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#loading-options>) object.

A sample `identify` call highlighting this feature is shown below:
    
    
    rudderanalytics.identify(
      "1hKOmRA4GRlm", {
        name: "Test User",
        gender: "Male",
      }, {
        integrations: {
          All: true,
          Mouseflow: {
            customVariables: {
              conversionRate: "100",
              total: 4,
            },
          },
        },
      }
    );
    

The corresponding Mouseflow dashboard view containing these custom variables is shown below:

[![Mouseflow custom variables in dashboard view](/docs/images/event-stream-destinations/mouseflow-dashboard-variables.webp)](</docs/images/event-stream-destinations/mouseflow-dashboard-variables.webp>)

> ![info](/docs/images/info.svg)
> 
> RudderStack uses Mouseflow’s [Setting a custom variable](<https://js-api-docs.mouseflow.com/#identifying-a-user:~:text=include%20%22product%2Dadded%22%2C%20...-,Setting%20a%20custom%20variable,-_mfq.push>) method to send the tags.

## FAQ

#### Where can I find the website ID in Mouseflow?

To get the website ID in Mouseflow, follow these steps:

  1. Log into your [Mouseflow dashboard](<https://app.mouseflow.com/sign-in>).
  2. Click the **Website Settings** icon:

[![Mouseflow website ID](/docs/images/event-stream-destinations/mouseflow-website-id-5.webp)](</docs/images/event-stream-destinations/mouseflow-website-id-5.webp>)

  3. You will find your website ID listed here.

[![Mouseflow website ID](/docs/images/event-stream-destinations/mouseflow-website-id-6.webp)](</docs/images/event-stream-destinations/mouseflow-website-id-6.webp>)

**Alternate method**

You can also fetch the website ID by clicking on the **Installation** icon present in your website’s card:

[![Mouseflow website ID](/docs/images/event-stream-destinations/mouseflow-website-id-1.webp)](</docs/images/event-stream-destinations/mouseflow-website-id-1.webp>)

Then, choose your installation method from **Google Tag Manager** , **Wordpress** , and **HTML**.

  * If you choose **Google Tag Manager** as your installation method, you can find the website ID as seen below:

[![Mouseflow website ID GTM](/docs/images/event-stream-destinations/mouseflow-website-id-2.webp)](</docs/images/event-stream-destinations/mouseflow-website-id-2.webp>)

  * If you choose **Wordpress** , you can find the website ID in the following line of the code snippet:


    
    
    mf.src = "//cdn.mouseflow.com/projects/<website_id>.js"
    

[![Mouseflow website ID Wordpress](/docs/images/event-stream-destinations/mouseflow-website-id-3.webp)](</docs/images/event-stream-destinations/mouseflow-website-id-3.webp>)

  * If you choose **HTML** , you can find the website ID in the in the following line of the tracking code:


    
    
    mf.src = "//cdn.mouseflow.com/projects/<website_id>.js"
    

[![Mouseflow website ID HTML](/docs/images/event-stream-destinations/mouseflow-website-id-4.webp)](</docs/images/event-stream-destinations/mouseflow-website-id-4.webp>)