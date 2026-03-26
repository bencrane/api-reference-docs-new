# Sprig Cloud Mode Integration

Send events to Sprig using RudderStack cloud mode.

* * *

  * __2 minute read

  * 


RudderStack lets you send your event data to Sprig via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/main/src/cdk/v2/destinations/sprig>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create a user in Sprig.

A sample `identify` call is shown:
    
    
    rudderanalytics.identify('1hKOmRA4GRlm', {
      firstName: 'Alex',
      lastName: 'Keener',
      email: "alex@example.com"
    });
    

### Traits mapping

RudderStack maps the following user attributes in the `identify` events to the corresponding Sprig fields:

RudderStack property| Sprig property  
---|---  
`userId`  
Required| `userId`  
`email`| `emailAddress`  
`context.traits`| `attributes`  
  
### Deleting a user

You can delete a user in Sprig using the [Suppression with Delete regulation](<https://www.rudderstack.com/docs/api/user-suppression-api/#adding-a-suppression-with-delete-regulation>) of RudderStack’s [User Suppression API](<https://www.rudderstack.com/docs/api/user-suppression-api/>).

> ![info](/docs/images/info.svg)
> 
> To delete a user, you must specify their `userId` and the [Sprig API key](<https://www.rudderstack.com/docs/destinations/streaming-destinations/sprig/setup/#connection-settings>) in the event.

A sample regulation request body for deleting a user in Intercom is shown below:
    
    
    {
      "regulationType": "suppress_with_delete",
      "destinationIds": [
        "2FIKkByqn37FhzczP23eZmURciA"
      ],
      "users": [{
        "userId": "1hKOmRA4GRlm",
        "apiKey": "<your_sprig_apiKey>"
      }]
    }
    

See the [Destinations](<https://www.rudderstack.com/docs/dashboard-guides/destinations/#destination-details>) guide for more information on obtaining the `destinationId`.

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record any user events along with the associated properties and send the information to Sprig.

A sample `track` call is shown:
    
    
    rudderanalytics.track('Signup', {
      firstName: "Alex",
      lastName: "Keener",
      email: "alex@example.com"
    });
    

### Property mapping

RudderStack maps the following event properties in the `track` events to the corresponding Sprig fields:

RudderStack property| Sprig property  
---|---  
`userId`  
Required| `userId`  
`event`  
Required| `events[0].event`  
`timestamp`  
Required| `events[0].timestamp`  
`email`| `emailAddress`