# Split Cloud Mode Integration

Send events to Split using RudderStack cloud mode.

* * *

  * __2 minute read

  * 


After you have successfully instrumented Split as a destination in RudderStack, follow this guide to correctly send your events to Split in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/splitio>).

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) method lets you identify a user and associate them to their actions. It also lets you record any traits about them like their name, email, etc.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
      plan: "GOLD",
      age: 40,
    })
    

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to capture user events and the associated properties.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Clicked button", {
      color: "red",
      buttonText: "Get started",
    })
    

RudderStack sends the above `track` call as a `Clicked_button` event to Split along with the event properties.

Note that the event name (`Clicked button` in the above example) in the `track` event should:

  * Start with a letter or number.
  * Contain 80 characters or less.
  * Contain only letters, numbers, hyphen, underscore, or period.


## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) event lets you record your website’s page views with any additional information about the viewed page.

A sample `page` call is shown below:
    
    
    rudderanalytics.page("homepage", "home", {
      url: "https://abc.com",
      title: "Test",
      referrer: "https://google.com",
    })
    

RudderStack sends the above `page` call as a `Viewed_home_page` event to Split, along with the associated properties.

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call lets you record whenever your user views their mobile screen, with any additional relevant information about the screen.

A sample `screen` call is shown below:
    
    
    [[RSClient sharedInstance] screen:@"Main" properties:@{@"prop_key" : @"prop_value"}];
    

The above snippet captures information related to the viewed screen such as its name and category. RudderStack sends this call as a `Viewed_Main_screen` event with the associated properties.

## Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call lets you link an identified user with a group like a company, organization, or an account. You can also record any custom traits associated with that group like the company name, number of employees, etc.

A sample `group` call is shown below:
    
    
    rudderanalytics.group("group123", {
      company: 'Sample Company',
    });
    

## Specify traffic type in events

You can specify the Split traffic type in your events as follows:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
      plan: "GOLD",
      age: 40,
      trafficTypeName: "account"
    })
    

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * RudderStack automatically maps the `trafficTypeName` field present in your `traits`/`context.traits`/`properties` object to Split’s `trafficTypeName` field.
>   * The traffic type name specified at the event level takes precedence over the [Traffic Type](<https://www.rudderstack.com/docs/destinations/streaming-destinations/split/setup-guide/#connection-settings>) dashboard setting.
>