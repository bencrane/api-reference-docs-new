# Optimizely Feature Experimentation Cloud Mode Integration

Send events to Optimizely Feature Experimentation using RudderStack’s cloud mode.

* * *

  * __3 minute read

  * 


RudderStack lets you send your web experimentation data to Optimizely Feature Experimentation via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to send decision events to Optimizely using their [Event API](<https://docs.developers.optimizely.com/experimentation-data/reference/post_events>) and activating the user for an experiment variation.

> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * You must call `identify` before the `track`/`page`/`screen` calls.
>   * Make sure to pass the same `userId` that you are passing in the `identify` call to all other calls (`track`/ `page`/`screen`).
> 


A sample `identify` call sent to Optimizely:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      firstName: "Alex",
      lastName: "Keener",
    });
    

To send `campaignId`, `experimentId`, and `variationId` in your `identify` events, use the `integrations` object in your calls:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      firstName: "Alex",
      lastName: "Keener",
      integrations: {
        Optimizely Fullstack: {
          campaignId: "<campaign_id>";
          experimentId: "<experiment_id>";
          variationId: "<variation_id>";
        }
      }
    });
    

#### Supported mappings

RudderStack maps the following event properties to the corresponding Optimizely properties:

RudderStack property| Optimizely property| Note  
---|---|---  
`userId`  
`anonymousId`  
Required| `visitor_id`| Determined based on the **Track known users** [dashboard setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/optimizely-feature-experimentation/setup-guide/#destination-settings>).  
`session_id`  
`context.sessionId`| `session_id`| -  
  
You can also map the RudderStack user traits to specific Optimizely attributes. See [Attribute mappings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/optimizely-feature-experimentation/setup-guide/#attribute-mappings>) for more information.

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to send the experiment-related information to Optimizely. RudderStack then sends the event name associated with an active experiment to Optimizely using their [Event API](<https://docs.developers.optimizely.com/experimentation-data/reference/post_events>).

To map your `track` event to specific Optimizely events, use the **RudderStack to Optimizely event mappings** dashboard setting. See [Track settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/optimizely-feature-experimentation/setup-guide/#track-settings>) for more information.

A sample `track` call is shown below:
    
    
    rudderanalytics.track(
      "Product Added", {
        item: "Tshirt",
        currency: "USD"
      })
    

### Supported mappings

RudderStack maps the following event properties to the corresponding Optimizely properties:

RudderStack property| Optimizely property| Note  
---|---|---  
`userId`  
`anonymousId`  
Required| `visitor_id`| Determined based on the **Track known users** [dashboard setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/optimizely-feature-experimentation/setup-guide/#destination-settings>).  
`session_id`  
`context.sessionId`| `session_id`| -  
`properties.quantity`| `quantity`| -  
`properties.revenue`| `revenue`| RudderStack converts the value of `revenue` to cents before passing it to Optimizely. For example, $5 will be converted to 500 cents.  
`properties`| `tags`| Other properties except `quantity` and `revenue`.  
  
## Page

You can use the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call to record your website’s page views with any additional relevant information about the viewed page.

RudderStack sends a `page` call to Optimizely using their [Event API](<https://docs.developers.optimizely.com/experimentation-data/reference/post_events>) with a valid event name associated with an active experiment.

A sample `page` call is shown:
    
    
    rudderanalytics.page("Home");
    

#### Send page name and category

To send the page category/name details to Optimizely:

  1. Enable **Track Categorized Pages** , **Track Named Pages** , or both, in your [dashboard settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/optimizely-feature-experimentation/setup-guide/#page-settings>).
  2. Map your `page` event to a specific Optimizely event using the **RudderStack Page Name/Category to Optimizely event mappings** setting.


See [Page settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/optimizely-feature-experimentation/setup-guide/#page-settings>) for more information.

#### Supported mappings

RudderStack property| Optimizely property| Note  
---|---|---  
`userId`  
`anonymousId`  
Required| `visitor_id`| Determined based on the **Track known users** [dashboard setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/optimizely-feature-experimentation/setup-guide/#destination-settings>).  
`session_id`  
`context.sessionId`| `session_id`| -  
`properties`| `tags`| -  
  
## Screen

You can use the [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call to record your users’ mobile screen views with any additional relevant information about the screen.

RudderStack sends a `screen` call to Optimizely using their [Event API](<https://docs.developers.optimizely.com/experimentation-data/reference/post_events>) with a valid event name associated with an active experiment.

A sample `screen` call is shown:
    
    
    rudderanalytics.screen("Main");
    

#### Send screen name and category

To send the screen category/name details to Optimizely:

  1. Enable **Track Categorized Pages** , **Track Named Pages** , or both, in your [dashboard settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/optimizely-feature-experimentation/setup-guide/#page-settings>).
  2. Map your `screen` event to a specific Optimizely event using the **RudderStack Page Name/Category to Optimizely event mappings** setting.


See [Page settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/optimizely-feature-experimentation/setup-guide/#page-settings>) for more information.

#### Supported mappings

RudderStack property| Optimizely property| Note  
---|---|---  
`userId`  
`anonymousId`  
Required| `visitor_id`| Determined based on the **Track known users** [dashboard setting](<https://www.rudderstack.com/docs/destinations/streaming-destinations/optimizely-feature-experimentation/setup-guide/#destination-settings>).  
`session_id`  
`context.sessionId`| `session_id`| -  
`properties`| `tags`| -  
  
## View experimentation results

To view the experimentation-related metrics, go to the [Results page](<https://support.optimizely.com/hc/en-us/articles/4410284017421-The-Experiment-Results-page>) page of your Optimizely dashboard. You can also view the results as a [data export](<https://docs.developers.optimizely.com/web-experimentation/docs/data-export>).