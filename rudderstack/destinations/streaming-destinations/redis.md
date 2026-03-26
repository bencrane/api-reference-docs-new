# Redis

Send events from RudderStack to Redis.

* * *

  * __4 minute read

  * 


[Redis](<https://redis.io/>) is an open source, in-memory data structure store. You can use it as a database and a message broker.

RudderStack stores all traits of your user as a [Redis hash](<https://redis.io/commands/hset>), allowing you to access user profiles in real-time.

> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * This integration only accepts [Identify](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) calls. RudderStack ignores all other event types.
>   * It is highly recommended that you keep your Redis instance within a private network and make it accessible to RudderStack.
> 


Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/redis>).

## Getting started

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Redis**.
  2. Assign a name to the destination and click **Continue**.


### Connection settings

To successfully configure Redis as a destination, you will need to configure the following settings:

  * **Address** : Enter the address of your Redis instance.
  * **Password** : Enter the password for your Redis instance.
  * **Database** : Enter the database name of your Redis instance where RudderStack should store the user traits. You can use this setting to configure a different database in your Redis instance.
  * **Cluster Mode** : Enable this setting if you’re connecting to a Redis cluster within a multi-node RudderStack setup.


> ![warning](/docs/images/warning.svg)
> 
> Note that if you enable **Cluster Mode** :
> 
>   * You need to specify multiple host addresses in a comma separated format in the **Address** field.
>   * RudderStack automatically disables the **Database** option.
> 


  * **Secure** : Enable this setting to secure the TLS communication between RudderStack Redis client and your Redis server.
    * **Skip verify** : Enable this option to skip the client’s verification of the server’s certificate chain and host name. In this mode, TLS is susceptible to man-in-the-middle attacks. Use this option **only** for testing.
    * **CA certificate** : Enter the certificate which needs to be verified while establishing a secure connection. Skip this setting if the Root CA of your server can be verified with any client, for example, Elasticache.
  * **Prefix** : By default, RudderStack stores user traits with the key `user:<user_id>`. You can specify an extra prefix to distinguish all RudderStack-stored keys.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to identify a visiting user and associate them to their actions. It also lets you record the traits about them like their name, email address, etc.

RudderStack stores the user traits in the Redis instance configured in the connection settings. You can access the latest user traits by querying Redis for the key `user:<user_id>`.

A sample `identify` call is shown below:
    
    
    // Identify a user with name and title as traits
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      title: "CEO",
    })
    

> ![warning](/docs/images/warning.svg)
> 
> `userId` is a required field for RudderStack to successfully send the `identify` events to Redis.

The following snippet highlights how it is stored in Redis:
    
    
    // redis-cli
    redis> HGETALL user:1hKOmRA4GRlm
    1) "name"
    2) "Alex Keener"
    3) "title"
    4) "CEO"
    

### Nested properties

If your user traits have nested properties, RudderStack flattens them with `.` as the separator.

Consider the following event:
    
    
    // Identify a user with location as a trait
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      location: {
        state: "Texas",
        city: "Austin",
      },
    })
    

RudderStack flattens the properties as follows:
    
    
    // redis-cli
    redis> HGETALL user:1hKOmRA4GRlm
    1) "location.state"
    2) "Texas"
    3) "location.city"
    4) "Austin"
    

### Custom prefix

If you specify a prefix while setting up your Redis destination, RudderStack uses it to prefix all the keys.

For example, if you specify the prefix `rudderstack` in the RudderStack dashboard setting and send the following call:
    
    
    // Identify a user with name and title as traits
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      age: 23,
    })
    

The corresponding Redis CLI output is prefixed with `rudderstack` as shown below:
    
    
    // redis-cli
    redis> HGETALL rudderstack:user:1hKOmRA4GRlm
    1) "age"
    2) 23
    

### Delete a user

You can delete a user in Redis using the [Suppression with Delete regulation](<https://www.rudderstack.com/docs/api/user-suppression-api/#adding-a-suppression-with-delete-regulation>) of the RudderStack [User Suppression API](<https://www.rudderstack.com/docs/api/user-suppression-api/>).

> ![warning](/docs/images/warning.svg)
> 
> While RudderStack forwards the deletion request, it **does not guarantee** deletion within a 30-day window. You will need to check with Redis if the request is fulfilled.

To delete a user, specify the `userId` in the event. A sample regulation request body for deleting a user in Redis is shown:
    
    
    {
      "regulationType": "suppress_with_delete",
      "destinationIds": ["2FIKkByqn37FhzczP23eZmURciA"],
      "users": [
        {
          "userId": "1hKOmRA4GRlm",
          "<customKey>": "<customValue>"
        }
      ]
    }
    

## FAQ

#### How do I set up Redis on Docker with TLS support?

To enable a TLS endpoint for accessing Redis, run a `redis-stunnel` container with a link to your Redis container and expose the TLS port. For more details, see [redis-stunnel usage](<https://hub.docker.com/r/runnable/redis-stunnel/>).

> ![info](/docs/images/info.svg)
> 
>   * Set **Common Name** to `localhost` while generating the CA certificate and server certificates.
>   * Set the TLS endpoint of the `redis-stunnel` container as the **Address** in your destination settings.
> 


For example, see the following Redis destination settings:

[![](/docs/images/event-stream-destinations/redis-example-settings.webp)](</docs/images/event-stream-destinations/redis-example-settings.webp>)

Here, `127.0.0.1:6380` is the address used while running containers locally with default values. You can specify the contents of the [generated `ca.pem` file](<https://hub.docker.com/r/runnable/redis-stunnel/#:~:text=for%20accessing%20Redis.-,Usage,-The%20easiest%20setup>) in the **CA certificate** field.