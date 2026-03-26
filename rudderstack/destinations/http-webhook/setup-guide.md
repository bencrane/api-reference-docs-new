# Setup Guide Beta

Set up and configure a HTTP Webhook destination in RudderStack.

* * *

  * __6 minute read

  * 


This guide will help you set up a HTTP Webhook destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to your HTTP Webhook destination.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova, Shopify
  * Refer to it as **HTTP Webhook** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
  
## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **HTTP Webhook**.

Assign a name to uniquely identify your destination in the RudderStack dashboard and click **Continue**.

### Connection settings

Setting| Description  
---|---  
Base URL| Specify the endpoint where RudderStack sends the events. RudderStack supports both `HTTP` and `HTTPS` URLs.  
  
Note that:  
  


  * For successful event delivery in case of an `HTTPS` URL, you must have a valid TLS certificate.
  * To configure the path parameters for this URL, see Request URL settings.

  
Authentication| Select the authentication method used while configuring your HTTP webhook endpoint. RudderStack supports the below authentication types:  
  


  * No Auth
  * Basic Auth
  * Bearer Token
  * API Key

Depending on the selected authentication type, configure the below settings:  
  
| Auth type| Setting  
---|---  
No Auth| Not applicable  
Basic Auth| 

  * Username
  * Password

  
Bearer Token| Token  
API Key| 

  * Key
  * Value

  
Method| Select the HTTP method of the request sent to the configured endpoint from the dropdown. By default, RudderStack uses the `POST` method to send the events.  
Body Format| Select the body format for your HTTP webhook endpoint. RudderStack supports the following body formats:  
  


  * JSON
  * XML
  * FORM

  
  
### Event configuration settings

Click **Set up mapping** to configure the event mappings, query parameters, and headers sent to the HTTP webhook endpoint.

RudderStack uses the in-house [JSON template engine](<https://github.com/rudderlabs/rudder-json-template-engine>) for mapping the fields.

> ![warning](/docs/images/warning.svg)
> 
> If you define multiple mappings for the same key, RudderStack only considers the first mapping and ignores the subsequent mappings for that key.

#### Request URL

This setting lets you configure the **Path** and **Query** parameters that RudderStack appends to your configured HTTP URL.

[![HTTP request URL configuration](/docs/images/event-stream-destinations/http-request-url-settings.webp)](</docs/images/event-stream-destinations/http-request-url-settings.webp>)

Note the following while specifying the path and query parameters:

  * The values specified as path parameters must be either JSONPath or constants. Some examples of valid and invalid values for these parameters are shown below:

Path| Notes  
---|---  
`$.event.customerId`| Valid path  
`order`| Valid path  
`"order"`| Invalid path  
  
  * For query parameters, the values specified in the **Key** field must be strictly a constant, whereas the values specified in the **Value** field can be either a JSONPath or constant. Some examples of valid and invalid values for these parameters are shown below:

Key| Value| Notes  
---|---|---  
`key`| `value`| Valid key and value  
`name`| `$traits.firstName`| Valid key and value  
`$.messageType`| `100`| Invalid key, valid value  
`key`| `"value"`| Valid key, invalid value  
  
##### **Example**

Suppose the base URL configured in the RudderStack dashboard is `https://example.com/` and you specify the path and query parameters, as follows:

  * **Path parameters in sequence** : `path`, `$.userId`
  * **Query parameters** : `key`, `value`


Then, the final generated URL is `https://example.com/path/$.userId?key=value`, as seen below:

[![HTTP request URL configuration](/docs/images/event-stream-destinations/http-request-url-settings.webp)](</docs/images/event-stream-destinations/http-request-url-settings.webp>)

#### Headers

This setting lets you add custom headers to your events as per your requirement.

[![HTTP custom header configuration](/docs/images/event-stream-destinations/http-header-settings.webp)](</docs/images/event-stream-destinations/http-header-settings.webp>)

Note that the values specified in the **Key** field must be strictly a constant, whereas the values specified in the **Value** field can be either a JSONPath or constant. Some examples of valid and invalid values are shown below:

Key| Value| Notes  
---|---|---  
`content-type`| `application/json`| Valid key and value  
`"content_type"`| `$.content_type`| Invalid key, valid value  
`properties.value`| `100`| Invalid key, valid value  
`Authorization`| `"event.apiKey"`| Valid key, invalid value  
  
RudderStack also adds the below header for all the requests by default:

Key| Value  
---|---  
`user-agent`| `RudderLabs`  
  
#### Request Body

This section lets you map the RudderStack event properties to specific destination fields. To do so, toggle off the **Send the event payload as is** setting and map the fields in the **Map your request payload** section:

[![HTTP request body configuration](/docs/images/event-stream-destinations/http-webhook-request-body-settings.webp)](</docs/images/event-stream-destinations/http-webhook-request-body-settings.webp>)

> ![warning](/docs/images/warning.svg)
> 
> The **Send the event payload as is** setting is toggled on by default, meaning the source event is sent to the webhook as is, without any modification.
> 
> If you have set the Body Format to **XML** , then toggling on this setting causes RudderStack to send the payload as is - under the root key.

Note that:

  * The fields defined in the **Value** column corresponds to the field present in the source event payload, whereas the fields defined in the **Key** column represents the field names sent to the HTTP webhook destination.
  * The values specified in the **Key** field must be strictly a [JSONPath](<https://en.wikipedia.org/wiki/JSONPath>), whereas the values specified in the **Value** field can be either a JSONPath or constant. Some examples of valid and invalid values are shown below:

Key| Value| Notes  
---|---|---  
`$.messageType`| `$.type`| Valid key and value  
`$.properties.firstName`| `$traits.fn`| Valid key and value  
`properties.value`| `100`| Invalid key, valid value  
`$.properties.currency`| `"EUR"`| Valid key, invalid value  
  
##### **XML Root Key setting**

If you set the Body Format to **XML** , then you can specify the root key used as a common prefix for all the field mappings defined in this section.

[![HTTP request body configuration for XML body format](/docs/images/event-stream-destinations/http-request-body-settings-xml.webp)](</docs/images/event-stream-destinations/http-request-body-settings-xml.webp>)

See the [end-to-end example](<https://www.rudderstack.com/docs/destinations/http-webhook/send-events/#example>) more information on how this setting translates into the final event payload sent to the destination.

### Configuration settings

Configure the below settings to receive your data correctly in your HTTP Webhook destination.

Setting| Description  
---|---  
Enable Batching| Toggle on this setting to let RudderStack batch the number of requests specified in the **Maximum Batch Size** setting before sending them to the configured endpoint.  
  
Note that:  
  


  * RudderStack supports this feature for the JSON body format only. It sends the batched events in the JSON array format, for example, `[{Event1},{Event2},....{EventN}]`.
  * The maximum batch size **must not** exceed 100.
  * RudderStack sends the batches to the endpoint when either the batch limit is reached or after 5 seconds (even if batch size is less than the specified limit) - whichever comes first.

  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.  
  
## Next steps

  * [Send events to HTTP Webhook destination](<https://www.rudderstack.com/docs/destinations/http-webhook/send-events/>)


## FAQ

**How do I check for delivery failures while sending events to the HTTP Webhook destination?**

Log in to your [RudderStack dashboard](<https://app.rudderstack.com>) and go to the **Live Events** tab of your destination to check for any delivery failures. In case there are any, you can check the **Error Response** by clicking the event to get more details.