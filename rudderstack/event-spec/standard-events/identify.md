# Identify

Get started with the RudderStack Identify API call.

* * *

  * __7 minute read

  * 


The `identify` call allows you to identify a visiting user and associate their actions to that identity. It also lets you record traits about the user like their name, email address, etc.

> ![info](/docs/images/info.svg)
> 
> As a best practice, make sure `identify` is called at the start of every session or page load for logged-in users, if possible. This will ensure all the latest traits are captured.

## When should I call identify?

Ideally, you should make an `identify` call in the following scenarios:

  * After a user registers on your website or app.
  * After a user logs in to your site or app.
  * When a user updates their information, for example, residential address, email ID, etc.
  * (Optional) When you load a page accessible by a logged-in user. This is required only when you have a downstream tool with such requirement (for example, Intercom).


## Sample payload

Here is a sample payload for an `identify` event after removing [Common fields](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/>):
    
    
    {
      "type": "identify",
      "context": {
        "traits": {
          "name": "Richard Hendricks",
          "email": "rhedricks@example.com",
          "logins": 2
        }
      },
      "userId": "27340af5c8819"
    }
    

The corresponding event that generates the above payload via the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) is:
    
    
    rudderanalytics.identify("27340af5c8819", {
      name: "Richard Hendricks",
      email: "rhedricks@example.com",
      logins: 2
    })
    

## Send a sample `identify` call

Use RudderStack’s **Event Playground app** to send sample events to RudderStack and test the data flow without any instrumentation.

Click **Send** to see the API call in the **Network** tab of your browser’s developer tools.

Follow these steps to use the **Event Playground app** to send test events to your account:

  1. Sign in to the [RudderStack dashboard](<https://app.rudderstack.com/>). Note the [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) at the top of the default **Connections** page.

[![Data plane URL](/docs/images/general/data-plane-url.webp)](</docs/images/general/data-plane-url.webp>)

  2. Set up a [source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#add-a-source>) and note its [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination. ](</docs/resources/glossary/#write-key>).

[![JavaScript SDK source write key](/docs/images/get-started/quickstart/js-write-key.webp)](</docs/images/get-started/quickstart/js-write-key.webp>)

  3. Click **Use My Account** in the **Event Playground app** below and specify the write key and data plane URL obtained in the above steps.


  4. Click **Save**.
  5. Select the required **API Method** from the dropdown. You can also edit the relevant fields or traits/properties.
  6. Click **Send to my account** to send the event.
  7. Go to the [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/#view-source-live-events>) viewer of your source (set up in Step 2) to verify that the event is successfully received.


## Identify fields

The `identify` call has the following fields in addition to the [Common fields](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/>):

**Field**| **Type**| **Presence**| **Description**  
---|---|---|---  
`userId`| String| Optional, **if** `anonymousId` is set| Your user’s unique identifier. Every `identify` call requires a `userId` or an `anonymousId`.  
`traits`| Object| Optional| Includes the traits of the user such as their `name`, `email`, etc. For more more information, check the Traits section below.  
  
> ![warning](/docs/images/warning.svg)
> 
> The field names can change slightly depending on the SDK. However, the functionality remains the same.
> 
> See the [SDK-specific documentation](<https://www.rudderstack.com/docs/sources/event-streams/sdks/>) for the implementation specifics and details on the above fields.

## User ID vs Anonymous ID

RudderStack requires every `identify` call to have either a `userId` or an `anonymousId`. This section highlights the differences between the two.

### User ID

A user ID (`userId`) uniquely identifies your user in your database. It is a permanent identifier of your customer which never changes - like a database ID.

> ![info](/docs/images/info.svg)
> 
> For `identify` calls, include a `userId` as often as possible to identify the most up to date traits of the customer.

> ![success](/docs/images/tick.svg)
> 
> It is recommended to use a database ID as the `userId` instead of usernames or email addresses. This is because users may update their username or email address at any point in the future. Instead, pass these attributes as **traits**.

### Anonymous ID

There are instances where you may get a visitor on your website/app who may or may not be your customer. Nonetheless, you still want to track their actions and tie them to various events, page views, and traits. In such cases, you should use an Anonymous ID (`anonymousId`) to identify this user.

> ![info](/docs/images/info.svg)
> 
> An anonymousId can be any identifier. For instance, a session ID corresponding to the visitor’s session. If you don’t have a readily available identifier, we recommend generating a **UUID**.

> ![success](/docs/images/tick.svg)
> 
> RudderStack’s web and mobile [SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/>) automatically use anonymous IDs to track unknown users on your website or mobile apps, so you don’t have to worry about including an `anonymousId` explicitly.

### Set a custom user ID (`externalId`)

You can pass a custom ID (`externalId`) along with the standard `userId` in your `identify` call. RudderStack adds this value under `context.externalId`.

The following code snippet shows how to add an `externalId` to your `identify` event using the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>), before sending it to the [Braze](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/>) destination:
    
    
    rudderanalytics.identify(
      "1hKOmRA4GRlm", {
        firstName: "Alex",
        city: "New Orleans",
        country: "Louisiana",
        phone: "+1-202-555-0146",
        email: "alex@example.com",
        custom_flavor: "chocolate",
      } {
        externalId: [{
          id: "<external_id>",
          type: "brazeExternalId",
        }, ],
      }
    );
    

## Identify traits

Traits are additional user information included in an `identify` call. Some examples of traits include age, gender, or some specific details - for example, a user’s product plan (basic, premium, and so on).

> ![info](/docs/images/info.svg)
> 
> There are some differences in the way RudderStack captures and sends the user traits across different SDKs. While RudderStack ideally sends the user traits in the [`context.traits`](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/#contextual-fields>) object (as in case of [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>)), for some SDKs it also sends the user traits in the root-level `traits` object (for backward compatibility).
> 
> Refer to the [SDK-specific documentation](<https://www.rudderstack.com/docs/sources/event-streams/sdks/>) for more details on sending user traits.

After making an `identify` call, user traits are not required in subsequent calls. You only need to include changed/updated traits since the last `identify` call.

RudderStack has some reserved traits that it handles in special ways. These are listed in the table below:

**Trait**| **Type**| **Description**  
---|---|---  
`id`| String| Fallback parameter used only for mapping data **if** `userId` is not available in the event payload.  
`firstName`| String| User's first name  
`lastName`| String| User's last name  
`name`| String| Full name of the user. If you already passed the `firstName` and `lastName`, RudderStack will automatically fill this field.  
`age`| Number| User's age  
`email`| String| User's email address  
`phone`| String| User's phone number  
`address`| Object| User's street address. This can optionally contain either/all of the following fields:

  * `city`
  * `country`
  * `postalCode`
  * `state`
  * `street`

  
`birthday`| Date| User's date of birth  
`company`| Object| User's company. This can optionally contain either/all of the following fields:

  * `name` (String)
  * `id` (String / Number)
  * `industry` (String)
  * `employee_count` (Number)
  * `plan` (String)

  
`createdAt`| Date| Date of user's account creation. We recommend using the **ISO-8601** date string format.  
`description`| String| User's description  
`gender`| String| User's gender  
`title`| String| User's title related to their position in their company  
`username`| String| User's username. This should be unique for every user.  
`website`| String| User's website  
`avatar`| String| URL of the user's avatar image  
  
> ![success](/docs/images/tick.svg)
> 
> Different destinations recognize some of the above traits differently. For example, Mixpanel recognizes `createdAt` as `$created`, while Intercom recognizes it as `created_at`.
> 
> With RudderStack, you don’t have to worry about these inconsistencies, it handles these destination-specific conversions automatically.

## Pass traits to an identify call

When you pass traits to an `identify` call, they will be stored in a cookie on the user’s browser or mobile device and will be passed automatically to all subsequent calls.

Below is an example of how to pass traits to an `identify` call from our [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>). For more examples, check our other [SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/>).
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      gender: "male",
    })
    

In the above example, `{name: "Richard Hendricks", gender: "male"}` are stored in a cookie and passed along with all subsequent calls.

## FAQ

##### How can I achieve consistent identity tracking for users across different top-level domains?

You can leverage the JavaScript SDK’s [Query string API](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/supported-api/#query-string-api>) to pass the user ID (`userId` or `anonymousId`) from one domain to the other so that the user journeys can be stitched together.