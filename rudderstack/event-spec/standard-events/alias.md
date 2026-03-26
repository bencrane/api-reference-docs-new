# Alias

Get started with the RudderStack Alias API call.

* * *

  * __2 minute read

  * 


The `alias` call lets you merge different identities of a known user.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * You can use the `alias` event only for merging user identities. It does not update the user’s `traits` or other common properties.
>   * RudderStack supports sending `alias` events only to select downstream destinations. See the [destination-specific documentation](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) for more details.
> 


## Alias fields

In addition to the [Common Fields](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/>), the `alias` call accepts the following fields:

Field| Description| Data type| Presence  
---|---|---|---  
`userId`| A unique identifier for the user in the database. Either `userId` or `anonymousId` should be present.| String| Optional, if `anonymousId` is already set.  
`previousId`| The user’s previous identifier.| String| Required  
  
> ![warning](/docs/images/warning.svg)
> 
> The field names can change slightly depending on the SDK. However, the functionality remains the same.
> 
> See the [SDK-specific documentation](<https://www.rudderstack.com/docs/sources/event-streams/sdks/>) for the implementation specifics and details on the above fields.

See the [Warehouse Schema](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/#alias>) guide for more information on how RudderStack records the information in the warehouse table for an `alias` event.

### User ID vs Previous ID

  * The `previousId` attribute refers to the previous user identifier. It could be either:
    * An `anonymousId` assigned to the user (for more details see [Identify API documentation](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>)).
    * A previously set `userId` to identify the user via the `identify` call - this could be an email address, a database ID, device ID, or any other unique user identifier.
  * The `userId` is the user’s new identity or an existing identity that you want to merge with `previousId`. As mentioned above, it could be a new email address, database ID, device ID, or any other unique user identifier.


## Sample payload

Here is a sample payload of an `alias` call:
    
    
    {
      "type": "alias",
      "previousId": "gbelson@example.com",
      "userId": "13bd56c84a562"
    }
    

The corresponding event that generates the above payload via the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) is:
    
    
    rudderanalytics.alias("13bd56c84a562")
    

> ![info](/docs/images/info.svg)
> 
> The RudderStack SDK automatically passes the user’s `anonymousId` as `previousId` in the payload.

> ![warning](/docs/images/warning.svg)
> 
> When instrumenting your website with the JavaScript SDK, the `alias` call must be made from the client-side as the `anonymousId` is generated via the browser. Similarly, if you’re using a server-side SDK, the `alias` call must be made from the server-side as the session ID is set as the `anonymousId`.