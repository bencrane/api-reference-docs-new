# Slack

Send your event data from RudderStack to Slack.

* * *

  * __8 minute read

  * 


[Slack](<https://slack.com/intl/en-in/>) is a popular business communication platform that lets you organize all your business-related chats by specific topics, groups, or direct messaging.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/slack>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **Slack** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Slack, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Slack**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure Slack as a destination, you will need to configure the following settings:

### Event channel settings

Use the following settings to send an event to a particular Slack channel:

Setting| Description  
---|---  
Type of incoming webhooks| Select the API from the dropdown that RudderStack uses to send data to the particular Slack channel:  
  
| Setting| Description  
---|---  
**Legacy**|  RudderStack maps the channel based on the **Event Channel Name** setting. This method may be deprecated soon.  
**Modern (through app)**|  RudderStack maps the channel based on the **Event Channel Webhook** setting.  
Event Name| Enter the event name or regex to match the RudderStack event name. For example, the regex `^slack\.events\.[a-zA-Z_]+$` matches strings like:  
  


  * `slack.events.message`
  * `slack.events.reaction_added`
  * `slack.events.user_typing`


> ![info](/docs/images/info.svg)If an event matches a regex, then RudderStack uses the corresponding **Event Channel Webhook** and **Event Template** (if specified).  
  
Event Channel Webhook| Enter the webhook URL of the Slack channel where RudderStack sends the above event. This is a **required** field if you have set **Type of incoming webhooks** setting to **Modern**.  
  
**Note** : To get the URL for **Event Channel Webhook** setting, make sure to:  
  


  1. Create a Slack app with the **Incoming Webhooks** feature.
  2. Authorize the app to post to your specified Slack channel.

See [Sending messages using Incoming Webhooks](<https://api.slack.com/messaging/webhooks#getting_started>) for more information.  
Event Channel Name| Enter the Slack channel’s name where RudderStack should send the above event using the [legacy method](<https://api.slack.com/legacy/custom-integrations/messaging/webhooks>). You can specify `#channel_name` or `@user_name`.  
  
**Note** : If not specified, RudderStack sends the events to the Slack channel associated with the incoming webhook URL (see **Webhook URL** setting below).  
Regex Matching| Turn on this setting if you are specifying a regular expression in the **Event Name** setting.  
  


> ![info](/docs/images/info.svg)RudderStack adds the global `g` parameter implicitly. Hence, you need not add it with the regex.  
  
### Identify template settings

Setting| Description  
---|---  
Identify Template| Specify the template used to transform the `identify` event before sending it to Slack. RudderStack uses the following default template:  
  

    
    
    Identified {{name}} <traits_key>:<traits_value> <traits_key2>:<traits_value2> ….

  
  
**Note** : Here, the traits key and value are the key-value pairs in the `traits` object of the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) event payload.  
  
RudderStack determines the `{{name}}` field in the above template from either of the following:

  * `traits.name`
  * `traits.firstName + traits.lastName`
  * `traits.username`
  * `properties.email`
  * `traits.email`
  * `userId`
  * `anonymousId`


> ![info](/docs/images/info.svg)
> 
> RudderStack considers only the traits listed in the **Allowlisted Traits** setting as a part of the identify template and ignores any other traits.

### Event template settings

Use the following settings to transform an event before sending it to Slack:

Setting| Description  
---|---  
Event Name| Enter the event name or regex to match the RudderStack event name. For example, the regex `^slack\.events\.[a-zA-Z_]+$` matches strings like:  
  


  * `slack.events.message`
  * `slack.events.reaction_added`
  * `slack.events.user_typing`

  
Event Template| Specify the template used to transform the above event.  
  
**Note** : RudderStack uses the following template by default and determines `name` similar to the **Identify Template** setting described above.  
  

    
    
    {{name}} did {{event}}  
  
Regex Matching| Turn on this setting if you are specifying a regular expression in the **Event Name** setting.  
  
> ![success](/docs/images/tick.svg)
> 
> RudderStack also provides a `{{newline}}` helper for your Identify and Event templates to create multi-line Slack messages for better readability.
> 
> See the Built-in helpers section for more information on using this helper.

### Incoming webhook URL settings

> ![info](/docs/images/info.svg)
> 
> RudderStack sends all the events to the channel associated with the incoming webhook URL by default.

Setting| Description  
---|---  
Webhook URL| Enter your Slack’s [incoming webhook URL](<https://my.slack.com/services/new/incoming-webhook/>).  
  
See the FAQ section for more information on obtaining this URL.  
  
### Other settings

Setting| Description  
---|---  
Allowlisted Traits| Specify the user traits you want to allowlist.  
  
**Note** : If not specified, RudderStack sends **all** the user traits to Slack.  
Denylisted Events| Enter the events to add to your denylist, causing RudderStack to drop these events.  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs.  
  
See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
## Handlebar expressions

RudderStack supports [Handlebar expressions](<https://handlebarsjs.com/guide/expressions.html>) by leveraging the `handlebars.js` library for including the variables into your dynamic Slack messages.

### Accessible Variables

The following table lists the variables you can select in your template messages:

Handlebar expression| Output  
---|---  
`{{name}}`| Identity name of the user in the priority order listed above.  
`{{event}}`| Event name, for example, `Product Viewed` or `user login`.  
`{{key_1}}`  
`{{properties.key_1}}`| The property values from the event’s properties object.  
`{{propertiesList}}`| JSON stringified version of your `properties` object.  
`{{traits}}`| JSON stringified version of your traits object.  
`{{traitsList.key_1}}`| The trait values from the event’s `traits` object.  
  
### Built-in helpers

RudderStack also provides built-in Handlebars helpers to enhance your message formatting:

Helper| Description  
---|---  
`{{newline}}`| Inserts a line break in your Slack message.  
  
Some examples of using the Handlebars expressions with the `{{newline}}` helper **after** configuring the relevant dashboard settings are shown below:

  * **Handlebars expression**


    
    
     Identified {{name}}{{newline}}Email: {{traits.email}}{{newline}}Country: {{traits.country}}
    

  * **CorrespondingSlack message**


    
    
     Identified Alex Keener
    Email: alex@example.com
    Country: USA
    

  * **Handlebars expression**


    
    
    {{name}} completed purchase{{newline}}Order ID: {{properties.orderId}}
    

  * **Corresponding Slack message**


    
    
     Alex Keener completed purchase
    Order ID: 12345
    

  * **Handlebars expression**


    
    
     New Order Alert!{{newline}}{{newline}}Customer: {{name}}{{newline}}Event: {{event}}{{newline}}Amount: ${{properties.revenue}}{{newline}}Items: {{properties.item_count}}
    

  * **Corresponding Slack message**


    
    
     New Order Alert!
    
    Customer: Alex Keener
    Event: Order Completed
    Amount: $100
    Items: 2
    

### Escaped content

The values returned by `{{variable}}` are [HTML-escaped](<https://handlebarsjs.com/guide/expressions.html#html-escaping>).

For example, if a `variable` has a `&` in its value, then it will be returned as `&amp;`. To avoid this behavior, you can use the **triple curly braces** instead of double braces, like `{{{variable}}}` instead of `{{variable}}`—this will stop the handlebars from escaping a value if there is one. See the following example:

Expression| Variable| Result  
---|---|---  
`{{variable}}`| `"Marcia & Jan"`| `"Marcia &amp; Jan"`  
`{{{variable}}}`| `"Marcia & Jan"`| `"Marcia & Jan"`  
  
## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you identify a visiting user and associate them to their actions. It also lets you record the traits about them like their name, email address, etc.

#### End-to-end example

The following is an end-to-end example of how a `identify` call translates to a Slack message depending on your dashboard settings:

If you set the Identify template as follows:

  * Allowlisted traits: `email`, `city`, `country`
  * Identify template:


    
    
    Welcome {{name}}!{{newline}}Email: {{traits.email}}{{newline}}Plan: {{traits.plan}}{{newline}}Location: {{traits.city}}, {{traits.country}}
    

Then, for the following `identify` call:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
      plan: "Premium",  // This won't appear since it's not allowlisted
      city: "San Francisco",
      country: "USA",
      phone: "+1234567890"  // This won't appear since it's not allowlisted
    });
    

You will see the following message in your configured Slack channel:
    
    
    Welcome Alex Keener!
    Email: alex@example.com
    Location: San Francisco, USA
    

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record the user events, that is, the actions your users perform, along with any properties associated with these actions.

#### End-to-end example

The following is an end-to-end example of how a `track` call translates to a Slack message depending on your dashboard settings:

Suppose you configure the Event template settings as follows:

  * Event name: `Product Purchased`
  * Event template:


    
    
    {{name}} just bought something!{{newline}}Product: {{properties.product_name}}{{newline}}Price: ${{properties.price}}{{newline}}Order ID: {{properties.order_id}}{{newline}}Quantity: {{properties.quantity}}
    

  * Allowlisted traits: `name`, `email`, `city`, `country` (affects the `{{name}}` resolution and available traits)


Then, if you identify the user as follows:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      name: "Alex Keener",
      email: "alex@example.com",
      plan: "Premium",  // This won't appear since it's not allowlisted
      city: "San Francisco",
      country: "USA",
      phone: "+1234567890"  // This won't appear since it's not allowlisted
    });
    

And then, you send a `track` call as follows:
    
    
    rudderanalytics.track("Product Purchased", {
      product_name: "Wireless Headphones",
      price: 149.99,
      order_id: "ORD-2025-619",
      quantity: 1,
      category: "Electronics"  // This will be available as {{properties.category}}
    });
    

You will see the following message in your configured Slack channel:
    
    
    Alex Keener just bought something!
    Product: Wireless Headphones
    Price: $149.99
    Order ID: ORD-2025-619
    Quantity: 1
    Category: Electronics
    

## FAQ

#### How do I obtain the incoming webhook URL?

To obtain the webhook URL, follow the below steps:

  1. Click your Slack workspace name, then go to **Administration** > **Manage Apps**.
  2. Search for **Incoming webhooks** in the Slack app directory and add it to Slack by clicking on **Add to Slack**.
  3. Select a channel where you want to post the messages forwarded by the webhook and click **Add Incoming webhooks integration**.

[![Slack connection settings](/docs/images/event-stream-destinations/choose-channel-slack.webp)](</docs/images/event-stream-destinations/choose-channel-slack.webp>)

  4. Finally, copy the webhook URL and enter it in the RudderStack dashboard.

[![Slack connection settings](/docs/images/event-stream-destinations/webhook-url-slack.webp)](</docs/images/event-stream-destinations/webhook-url-slack.webp>)

#### Why am I getting Slack messages for all the incoming events in one channel?

By default, RudderStack sends all the events to the Slack channel associated with the incoming webhook URL (**Webhook URL** setting in the RudderStack dashboard).

To get specific events in a particular channel, make sure you specify the mappings using the **Event Name** and **Event Channel** settings.