# June Web Device Mode Integration

Send events to June using RudderStack web device mode.

* * *

  * __3 minute read

  * 


RudderStack lets you send your event data to June destination via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) using the native web SDK.

Find the open-source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/June>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create new users or update existing users’ details in June. RudderStack sends the `identify` call to June as an [`identify`](<https://www.june.so/docs/tracking/web/browser>) event.

> ![info](/docs/images/info.svg)
> 
> Make sure that you make an `identify` call before making a `track`, `group`, or `page` call.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4el9Z", {
      name: "Alex Keener",
      email: "alex@example.com"
    })
    

### Property mappings

The following table lists the property mappings between RudderStack and June for the `identify` call:

RudderStack property| June property| Data type| Presence  
---|---|---|---  
`userId`/`context.traits.userId`/`context.traits.id`| `userId`| String| Required  
`context.traits`| `traits`| Object| Optional  
  
## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture user events along with the properties associated with them. RudderStack sends the `track` call to June as a [`track`](<https://www.june.so/docs/tracking/web/browser>) event.

A sample `track` call is shown below:
    
    
    // groupId using properties object
    rudderanalytics.track("Product Reviewed", {
      review_id: "12345",
      product_id: "123",
      rating: 3.0,
      review_body: "Average product, expected much more.",
      groupId: "5H7ASAIEQO",
    });
    
    // groupId using context.externalId array
    rudderanalytics.track(
      "Product Reviewed", {
        review_id: "12345",
        product_id: "123",
        rating: 3.0,
        review_body: "Average product, expected much more.",
      }, {
        externalId: [{
          type: "juneGroupId",
          id: "5H7ASAIEQO",
        }, ],
      }
    );
    

### Property mappings

The following table lists the property mappings between RudderStack and June for the `track` call:

RudderStack property| June property| Data type| Presence  
---|---|---|---  
`event`| `event`| String| Required  
`properties`| `properties`| Object| Optional  
  
  * If `context.externalId.id` (when `context.externalId.type` = `juneGroupId`) is present.
  * Otherwise, `properties.groupId`.

| `context.groupId`| String| Optional  
  
## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views with any additional relevant information about the viewed page. RudderStack sends the `page` call to June as a `PageView` event.

A sample `page` call is shown below:
    
    
    rudderanalytics.page("Home")
    

### Property mappings

The following table lists the property mappings between RudderStack and June for the `page` call:

RudderStack property| June property| Data type| Presence  
---|---|---|---  
`name`| `name`| String| Optional  
`properties`| `properties`| Object| Optional  
  
## Group

You can use the [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call to create a new company or update an existing company’s details in June.

> ![warning](/docs/images/warning.svg)
> 
> If you are using a `group` call to identify a company, it is recommended to pass the `groupId` in the `track` call. It allows you to specify which company performed that specific event. For more information, refer to the [June documentation](<https://www.june.so/docs/tracking/web/browser>).

A sample `group` call is shown below:
    
    
    rudderanalytics.group("23Np893Z6", {
      name: "ABC company",
      employees: 100,
      Industry: "Video game publisher",
      Founded: 1979
    });
    

### Property mappings

The following table lists the property mappings between RudderStack and June for the `group` call:

RudderStack property| June property| Data type| Presence  
---|---|---|---  
`groupId`/`traits.groupId`| `groupId`| String| Required  
`traits`| `traits`| Object| Optional  
  
## FAQ

#### Can I make an `identify` or `track` call using `anonymousId`?

No, you can’t. June does not stitch identities together or support merging anonymous users. Rather, it is best used to measure user activation and retention when the user is logged in.

#### My user is created as `Unknown` in June dashboard. What might be the reason?

June categorizes a user as `Unknown` if the `firstName`, `lastName`, `name`, `username`, or `email` is not present in the `traits` object of the `identify` call.