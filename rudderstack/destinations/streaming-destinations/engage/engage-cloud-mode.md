# Engage Cloud Mode Integration

Send events to Engage using RudderStack cloud mode.

* * *

  * __4 minute read

  * 


RudderStack lets you send your event data to Engage via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create or update a user in Engage. To update a user’s email, you need to provide the [Engage Private Key](<https://www.rudderstack.com/docs/destinations/streaming-destinations/engage/setting-up-engage/#connection-settings>) in the dashboard settings.

RudderStack uses the [Create or update a User](<https://docs.engage.so/en-us/a/62bbdd015bfea4dca4834042-users>) API to add a new user to your Engage account.

The following table lists the RudderStack attributes and their mappings with the Engage properties:

RudderStack property| Engage property| Data type  
---|---|---  
`externalId.engageId`, `userId`, `traits.userid`, `traits.id`, `context.traits.userId`, `context.traits.id`  
Required| `uid`| Alphanumeric  
`traits.firstName`, `traits.firstname`, `traits.first_name`, `context.traits.firstName`, `context.traits.firstname`, `context.traits.first_name`| `first_name`| String  
`traits.lastName`, `traits.lastname`, `traits.last_name`, `context.traits.lastName`, `context.traits.lastname`, `context.traits.last_name`| `last_name`| String  
`traits.email`, `context.traits.email`, `properties.email`| `email`| String  
`traits.phone`, `context.traits.phone`, `properties.phone`| `number`| Number _(In`^[0-9]{7,15}$` format)_  
Other user traits| `meta`| String/Integer/Boolean  
`timestamp`, `originalTimestamp`| `createdAt`| Timestamp _(ISO 8601 format)_  
`externalId.engageListId`, `config.listIds`| `lists`| Array of List ID  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack uses `externalId.engageListId` or `config.listIds` as a fallback value in case `userId`, `externalId.engageId`, `traits.userId`, `traits.id`, or `context.traits.id` is absent in the event.

### Deleting a user

You can delete a user in Engage using the [Suppression with Delete regulation](<https://www.rudderstack.com/docs/api/user-suppression-api/#adding-a-suppression-with-delete-regulation>) of the RudderStack [User Suppression API](<https://www.rudderstack.com/docs/api/user-suppression-api/>).

> ![info](/docs/images/info.svg)
> 
> To delete a user in Engage, you need to specify the [Engage Private Key](<https://www.rudderstack.com/docs/destinations/streaming-destinations/engage/setting-up-engage/#connection-settings>) in the dashboard settings.

A sample regulation request body for deleting a user in Engage is shown below:
    
    
    {
      "regulationType": "suppress_with_delete",
      "destinationIds": [
        "2FIKkByqn37FhzczP23eZmURciA"
      ],
      "users": [{
        "userId": "1hKOmRA4GRlm",
        "phone": "+1-202-555-0146",
        "email": "alex@example.com"
      }]
    }
    

RudderStack deletes the user account in Engage using the [Delete User API](<https://docs.engage.so/en-us/a/62bbdd015bfea4dca4834042-users#delete-customer-or-account>).

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture user events along with the associated properties and send them to Engage.

RudderStack uses the [Add User events API](<https://docs.engage.so/en-us/a/62bbdd015bfea4dca4834042-users#track-user-event>) to send the user events to Engage.

A sample `track` call is shown below:
    
    
    rudderanalytics.track(
      "Order Completed", {
        revenue: 30,
        currency: "USD",
        userId: "1hKOmRA4el9Z" 
      })
    

The following table lists the RudderStack attributes and their mappings with the Engage properties:

RudderStack property| Engage property| Data type  
---|---|---  
`externalId.engageId`, `userId`, `traits.userid`, `traits.id`, `context.traits.userId`, `context.traits.id`  
Required| `uid`| Alphanumeric  
`event`  
Required| `event`| String  
`originalTimestamp`| `timestamp`| Timestamp _(ISO 8601 format)_  
`properties`| `properties`| Object  
  
> ![warning](/docs/images/warning.svg)
> 
> The event name must be less than 32 characters. Otherwise, Engage will reject the event.

## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views with any additional relevant information about the viewed page.

RudderStack sends the page-related information to Engage using their [Add User events API](<https://docs.engage.so/en-us/a/62bbdd015bfea4dca4834042-users#track-user-event>).

The following table lists the RudderStack event properties and their mappings with the Engage properties:

RudderStack property| Engage property| Data type  
---|---|---  
`externalId.engageId`, `userId`, `traits.userid`, `traits.id`, `context.traits.userId`, `context.traits.id`  
Required| `uid`| Alphanumeric  
`Visited {Category} {Name} Page`  
Required| `event`| String  
`originalTimestamp`| `timestamp`| Timestamp _(ISO 8601 format)_  
`properties`| `properties`| Object  
  
> ![warning](/docs/images/warning.svg)
> 
> The event name must be less than 32 characters. Otherwise, Engage will reject the event.

## Group

You can use the [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call to link an identified user to a specific Engage list.

RudderStack subscribes the user to the Engage list using their [Subscribe to a List API](<https://docs.engage.so/en-us/a/62bbdd2e5bfea4dca4834045-lists#subscribe-user-to-a-list>).

A sample `group` call is shown below:
    
    
    rudderanalytics.group("group01", {
    "userId": "1",
    "name": "Capsule Corp.",
    "subscriber_status": "false",
    "operation": "add"
    });
    

You can pass the following parameters in the `group` event along with the `userId` (if known):

RudderStack property| Engage property| Data type  
---|---|---  
`groupId`  
Required| `id`| String  
`externalId.engageId`, `userId`| `uid`| Alphanumeric  
`subscriber_status`  
 _(Default:`true`)_| `subscribed`| Boolean  
`traits.operation`  
 _(Acceptable values:`add`/`remove`)_| -| String  
  
The following table lists the additional property mappings with the Engage properties:

RudderStack property| Engage property| Data type  
---|---|---  
`traits.email`, `context.traits.email`, `properties.email`, `context.externalId.0.id`  
Required, if `phone` is not present| `email`| String  
`traits.phone`, `context.traits.phone`, `properties.phone`  
Required, if `email` is not present| `number`| Number _(In`^[0-9]{7,15}$` format)_  
`traits.firstName`, `traits.firstname`, `traits.first_name`, `context.traits.firstName`, `context.traits.firstname`, `context.traits.first_name`| `first_name`| String  
`traits.lastName`, `traits.lastname`, `traits.last_name`, `context.traits.lastName`, `context.traits.lastname`, `context.traits.last_name`| `last_name`| String  
Other user traits| `meta`| String / Integer / Boolean  
`timestamp`, `originalTimestamp`| `createdAt`| Timestamp _(ISO 8601 format)_  
  
When sending `group` events to Engage, it is important to note the following:

  * To remove a user from a group (`"operation": "remove"`), you need to provide the `userId` or `externalId` in the event.
  * If the user’s ID is not known, then either `email` or `phone` is required for looking up the user in Engage.
  * If a user is found with an associated `email` or `phone` (in that priority), then Engage links the user to the provided Engage List ID. Otherwise, it creates a new user with the provided details and then links them to the List ID.