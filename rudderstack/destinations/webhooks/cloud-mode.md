# Webhook Cloud Mode Integration

Send events to your webhook destination in RudderStack cloud mode.

* * *

  * __5 minute read

  * 


After you have successfully instrumented your webhook destination in RudderStack, follow this guide to correctly send your events in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/webhook>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to associate a user to their actions. Apart from capturing a unique user ID, you can also send optional traits associated with that user, such as name, email, IP address, etc. using the RudderStack SDKs.

A sample `identify` payload is as shown:
    
    
    {
      "channel": "web",
      "context": {
        "app": {
          "build": "1.0.0",
          "name": "RudderLabs JavaScript SDK",
          "namespace": "com.rudderlabs.javascript",
          "version": "1.1.1-rc.2"
        },
        "traits": {
          "name": "User name",
          "email": "user@domain.com",
          "plan": "Enterprise",
          "company": { "id": "company-A" },
          "createdAt": "Thu Mar 24 2016 17:46:45 GMT+0000 (UTC)"
        },
        "library": { "name": "RudderLabs JavaScript SDK", "version": "1.1.1-rc.2" },
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "locale": "en-US",
        "os": { "name": "", "version": "" },
        "screen": { "density": 1.600000023841858 },
        "page": {
          "path": "/tests/html/script-test.html",
          "referrer": "http://localhost:1111/tests/html/",
          "search": "",
          "title": "",
          "url": "http://localhost:1111/tests/html/script-test.html"
        }
      },
      "type": "identify",
      "messageId": "508d5e8c-96e4-4301-bd46-1890dba5c866",
      "originalTimestamp": "2020-04-22T08:06:20.337Z",
      "anonymousId": "21b43de4-3b9b-423f-b51f-794eae31fc03",
      "userId": "my-user-id",
      "integrations": { "All": true },
      "sentAt": "2020-04-22T08:06:20.337Z"
    }
    

For each `identify` call, RudderStack sends the request as listed below, depending on the URL method configured in the dashboard:

Request| Note  
---|---  
`POST`| RudderStack sends the whole event payload (shown above) as the JSON body of the `POST` request.  
`PUT`| RudderStack sends the whole event payload (shown above) as the JSON body of the `PUT` request.  
`GET`| RudderStack sends the traits passed in the `identify` call as the query parameters of the `GET` request.  
  
If your traits contain nested values, RudderStack flattens these values and sends them as the query parameters. For example, the company ID specified in the above payload’s `traits` is sent as `"company.id": "company-A"`.  
`PATCH`| RudderStack sends the whole event payload (shown above) as the JSON body of the `PATCH` request.  
`DELETE`| RudderStack sends the traits passed in the `identify` call as the query parameters of the `DELETE` request.  
  
If your traits contain nested values, RudderStack flattens these values and sends them as the query parameters.  
  
## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call lets you record your website’s page views, with any additional relevant information about the viewed page.

A sample `page` payload is as shown:
    
    
    {
      "channel": "web",
      "context": {
        "app": {
          "build": "1.0.0",
          "name": "RudderLabs JavaScript SDK",
          "namespace": "com.rudderlabs.javascript",
          "version": "1.1.1-rc.2"
        },
        "traits": {},
        "library": { "name": "RudderLabs JavaScript SDK", "version": "1.1.1-rc.2" },
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "locale": "en-US",
        "os": { "name": "", "version": "" },
        "screen": { "density": 1.600000023841858 },
        "page": {
          "path": "/tests/html/script-test.html",
          "referrer": "http://localhost:1111/tests/html/",
          "search": "",
          "title": "",
          "url": "http://localhost:1111/tests/html/script-test.html"
        }
      },
      "type": "page",
      "messageId": "97114191-e2f2-42af-97db-14b358b1cfe1",
      "originalTimestamp": "2020-04-22T08:06:20.334Z",
      "anonymousId": "57d95a96-61dc-47bf-8f96-5d37543d7438",
      "userId": "user@domain.com",
      "properties": {
        "path": "/tests/html/script-test.html",
        "referrer": "http://localhost:1111/tests/html/",
        "search": "",
        "title": "",
        "url": "http://localhost:1111/tests/html/script-test.html",
        "experiment": {"variant": "old"}
      },
      "integrations": { "All": true },
      "sentAt": "2020-04-22T08:06:20.334Z"
    }
    

For each `page` call, RudderStack sends the request as listed below, depending on the URL method configured in the dashboard:

Request| Note  
---|---  
`POST`| RudderStack sends the whole event payload (shown above) as the JSON body of the `POST` request.  
`PUT`| RudderStack sends the whole event payload (shown above) as the JSON body of the `PUT` request.  
`GET`| RudderStack sends the properties passed in the `page` call as the query parameters of the `GET` request.  
  
If your properties contain nested values, RudderStack flattens these values and sends them as the query parameters. For example, the experiment variant specified in the above payload’s properties is sent as `"experiment.variant": "old"`.  
`PATCH`| RudderStack sends the whole event payload (shown above) as the JSON body of the `PATCH` request.  
`DELETE`| RudderStack sends the traits passed in the `page` call as the query parameters of the `DELETE` request.  
  
If your traits contain nested values, RudderStack flattens these values and sends them as the query parameters.  
  
## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call captures all activities that the user performs, along with any other properties that are associated with those activities. Each of these activities or actions is considered as an **event**.

A sample `track` payload is as shown:
    
    
    {
      "channel": "web",
      "context": {
        "app": {
          "build": "1.0.0",
          "name": "RudderLabs JavaScript SDK",
          "namespace": "com.rudderlabs.javascript",
          "version": "1.1.1-rc.2"
        },
        "traits": {
          "name": "User name",
          "email": "user@doamin.com",
          "plan": "Enterprise",
          "company": { "id": "comapny-A" },
          "createdAt": "Thu Mar 24 2016 17:46:45 GMT+0000 (UTC)"
        },
        "library": { "name": "RudderLabs JavaScript SDK", "version": "1.1.1-rc.2" },
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "locale": "en-US",
        "os": { "name": "", "version": "" },
        "screen": { "density": 1.600000023841858 },
        "page": {
          "path": "/tests/html/script-test.html",
          "referrer": "http://localhost:1111/tests/html/",
          "search": "",
          "title": "",
          "url": "http://localhost:1111/tests/html/script-test.html"
        }
      },
      "type": "track",
      "messageId": "04a303b1-a466-4e66-9022-2a24edaca4fc",
      "originalTimestamp": "2020-04-22T08:06:20.338Z",
      "anonymousId": "21b43de4-3b9b-423f-b51f-794eae31fc03",
      "userId": "my-user-id",
      "event": "Product Purchased",
      "properties": {
        "order_ID": "1",
        "category": "boots",
        "product_name": "new_boots",
        "price": 60,
        "currency": "USD"
      },
      "integrations": { "All": true },
      "sentAt": "2020-04-22T08:06:20.338Z"
    }
    

For each `track` call, RudderStack sends the request as listed below, depending on the URL method configured in the dashboard:

Request| Note  
---|---  
`POST`| RudderStack sends the whole event payload (shown above) as the JSON body of the `POST` request.  
`PUT`| RudderStack sends the whole event payload (shown above) as the JSON body of the `PUT` request.  
`GET`| RudderStack sends the properties passed in the `track` call as the query parameters of the `GET` request.  
  
If your properties contain nested values, RudderStack flattens these values and sends them as the query parameters.  
`PATCH`| RudderStack sends the whole event payload (shown above) as the JSON body of the `PATCH` request.  
`DELETE`| RudderStack sends the traits passed in the `track` call as the query parameters of the `DELETE` request.  
  
If your traits contain nested values, RudderStack flattens these values and sends them as the query parameters.  
  
To view the detailed event structure for the other event types, see the [RudderStack Event Spec](<https://www.rudderstack.com/docs/event-spec/standard-events/>) guide.