# June Cloud Mode Integration

Send events to June using RudderStack cloud mode.

* * *

  * __3 minute read

  * 


RudderStack lets you send your event data to June via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open-source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/june>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create a new user or update an existing user’s details in June. RudderStack sends the `identify` call to June using their [`identify`](<https://www.june.so/docs/tracking/http-api/identify>) API.

> ![warning](/docs/images/warning.svg)
> 
> Make sure that you make an `identify` call before making a `track` or `group` call.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4el9Z", {
      name: "Alex Keener",
      email: "alex@example.com"
    })
    

#### **Property mapping**

The following table lists the property mappings between RudderStack and June for the `identify` call:

RudderStack property| Data type| June property  
---|---|---  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  
Required| String| `userId`  
`originalTimestamp`  
`timestamp`  
Required| Timestamp in ISO 8601 format  
(`yyyy-MM-ddTHH:mm:ss.SSSZ`)| `timestamp`  
`anonymousId`| String| `anonymousId`  
`traits`  
`context.traits`| Object| `traits`  
`context`| Object| `context`  
  
## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture user events along with the properties associated with them. RudderStack sends the `track` call to June using their [`track`](<https://www.june.so/docs/tracking/http-api/track>) API.

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
    

#### **Property mapping**

The following table lists the property mappings between RudderStack and June for the `track` call:

RudderStack property| Data type| June property  
---|---|---  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  
Required| String| `userId`  
`event`  
Required| String| `event`  
`originalTimestamp`  
`timestamp`  
Required| Timestamp in ISO 8601 format  
(`yyyy-MM-ddTHH:mm:ss.SSSZ`)| `timestamp`  
`anonymousId`| String| `anonymousId`  
`properties`| Object| `properties`  
  
  * `context.externalId.id` (when `context.externalId.type` = `juneGroupId`)
  * `properties.groupId`

| String| `context.groupId`  
`context`| Object| `context`  
  
## Group

You can use the [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call to create a new company or update an existing company’s details in June. Refer to the [June documentation](<https://www.june.so/docs/tracking/http-api/group>) for more information.

> ![warning](/docs/images/warning.svg)
> 
> If you are using a `group` call to identify a company, it is recommended to pass the `groupId` in the `track` call. It allows you to specify which company performed that specific event.

A sample `group` call is shown below:
    
    
    rudderanalytics.group("23Np893Z6", {
      name: "ABC company",
      employees: 100,
      Industry: "Video game publisher",
      Founded: 1979
    });
    

#### **Property mapping**

The following table lists the property mappings between RudderStack and June for the `group` call:

RudderStack property| Data type| June property  
---|---|---  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  


  * Required for creating a company.
  * Optional for updating the company details.

| String| `userId`  
`originalTimestamp`  
`timestamp`  
Required| Timestamp in ISO 8601 format  
(`yyyy-MM-ddTHH:mm:ss.SSSZ`)| `timestamp`  
`groupId`  
`traits.groupId`  
Required| String| `groupId`  
`anonymousId`| String| `anonymousId`  
`traits`  
`context.traits`| Object| `traits`  
`context`| Object| `context`  
  
## Page

You can use the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call to record and send page views to June.

A sample `page` event:
    
    
    rudderanalytics.page("Home");
    

#### **Property mapping**

RudderStack property| Data type| June property  
---|---|---  
`properties`  
Required| Object| `properties`  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`| String| `userId`  
`timestamp`  
`originalTimestamp`| Timestamp in ISO 8601 format  
(`yyyy-MM-ddTHH:mm:ss.SSSZ`)| `timestamp`  
`anonymousId`| String| `anonymousId`  
`groupId`| String| `context.groupId`  
`context`| Object| `context`  
  
## FAQ

#### Can I make an `identify` or `track` call using `anonymousId`?

No, you cannot. June does not stitch identities together or support merging anonymous users. It is best used to measure user activation and retention when the user is logged in.

#### My user is created as `Unknown` in June dashboard. What might be the reason?

June categorizes a user as `Unknown` if the `firstName`, `lastName`, `name`, `username`, or `email` is not present in the `traits` object of the `identify` call.