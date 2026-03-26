# Koala Cloud Mode Integration Beta

Send events to Koala using RudderStack cloud mode.

* * *

  * __2 minute read

  * 


After you have successfully instrumented Koala as a destination in RudderStack, follow this guide to correctly send your events to Koala in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/main/src/cdk/v2/destinations/koala>).

> ![info](/docs/images/info.svg)
> 
> Note the following when sending `identify` and `track` events to Koala:
> 
>   * You must include either `email` or the user’s Koala profile id (`ko_profile_id`) as Koala uses one of these fields to associate the user with their profile.
>   * Send the `ko_profile_id` in the UUID v4 format.
> 


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create or update a Lead object in Koala.

A sample `identify` call is shown:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
      ko_profile_id: "12345"
    })
    

### Supported mappings

RudderStack maps the following `identify` fields to the corresponding Koala properties:

RudderStack property| Koala property  
---|---  
`traits.email`  
`context.traits.email`  
`properties.email`  
Required, if `ko_profile_id` is absent.| `email`  
`traits.ko_profile_id`  
`context.traits.ko_profile_id`  
`properties.ko_profile_id`  
Required, if `email` is absent.| `profile_id`  
`type`| `identifies.$.type`  
`traits`  
`context.traits`| `events.$.traits`  
`timestamp`  
`originalTimeStamp`| `events.$.sent_at`  
  
## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to capture events like `Account Created`, `Account Deleted`, and their related properties.
    
    
    rudderanalytics.track("User Signed Up", {
      plan: "Pro Annual",
      firstName: "Alex",
      lastName: "Keener",
      ko_profile_id: "12345"
      email: "alex@example.com"
    })
    

### Supported mappings

RudderStack maps the following `track` fields to the corresponding Koala properties:

RudderStack property| Koala property  
---|---  
`event`  
Required| `events.$.event`  
`traits.email`  
`context.traits_email`  
`properties.email`  
Required, if `ko_profile_id` is absent.| `email`  
`traits.ko_profile_id`  
`context.traits.ko_profile_id`  
`properties.ko_profile_id`  
Required, if `email` is absent.| `profile_id`  
`context.ip`  
`request_ip`| `ip`  
`context`| `event.$.context`  
`properties`| `events.$.properties`  
`type`| `events.$.type`  
`messageId`| `events.$.message_id`  
`timestamp`  
`originalTimeStamp`| `events.$.sent_at`