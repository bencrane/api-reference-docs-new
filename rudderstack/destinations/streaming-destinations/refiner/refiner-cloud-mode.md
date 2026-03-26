# Refiner Cloud Mode Integration

Send events to Refiner using RudderStack cloud mode.

* * *

  * __2 minute read

  * 


RudderStack lets you send your event data to Refiner via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/refiner>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create or update a contact in Refiner.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com"
    })
    

> ![warning](/docs/images/warning.svg)
> 
> To make an `identify` call successfully, either the `email` or `userId` is required.

### Supported mappings

The following table lists the RudderStack attributes and their mappings with the Refiner properties:

RudderStack property| Refiner property  
---|---  
`userId`  
Required, if email is absent.| `id`  
`properties.email`  
Required, if userId is absent.| `email`  
`traits`  
`context.traits`| traits  
  
## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture user events and send them to Refiner as `trackEvent` events. If a `track` event contains a `userId`, then Refiner updates the corresponding user’s information. Otherwise, it creates a new user.

> ![warning](/docs/images/warning.svg)
> 
> Refiner does not store any additional properties sent with the `track` event.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      orderId: "ORD122",
      price: "5.67",
      currency: "USD",
    });
    

The following table lists the RudderStack properties and their mappings with the Refiner properties:

RudderStack property| Refiner property  
---|---  
`userId`| `id`  
event name| event  
  
## Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call lets you link an identified user with a group, such as a company, organization, or an account. Note that Refiner associates all `group` traits with the `account` object associated with the user.

A sample `group` call is shown below:
    
    
    rudderanalytics.group("group@123", {
      name: "Sample Company",
      employees: 1000,
      industry: "Software",
    })
    

The following table lists the RudderStack properties and their mappings with the Refiner properties:

RudderStack property| Refiner property  
---|---  
`userId`  
Required| `id`  
`traits.email`| `account.email`  
`context.traits.email`| `email`  
`groupId`| `account.id`  
`traits`| `account`  
  
## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views with any additional relevant information about the viewed page and send this information to Refiner.

> ![info](/docs/images/info.svg)
> 
> The behavior of the `page` call is the same as the  call described above. However, note that if you do not set the event name, RudderStack sets `pageView` as the event name by default.

A sample `page` event is shown below:
    
    
    rudderanalytics.page("Cart", "Cart Viewed", {
      path: "/cart",
      referrer: "samplewebsite.com",
      search: "some item",
      title: "New Item",
      url: "http://samplewebsite.in",
    })