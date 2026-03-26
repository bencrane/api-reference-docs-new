# RudderStack Event Specification

Learn the fields and properties associated with the standard RudderStack API methods.

* * *

  * __3 minute read

  * 


The **RudderStack Event Spec** outlines how to send event data to RudderStack’s APIs and the proper format to capture events using [RudderStack’s SDKs](<https://www.rudderstack.com/docs/sources/event-streams/sdks/>).

The RudderStack Event Spec supports multiple API calls that make it easy to identify users and track their specific actions as events. Using the correct format to capture events ensures that RudderStack can automatically forward those events to any of our supported [destinations](<https://www.rudderstack.com/docs/destinations/overview/>).

## Supported API calls

The RudderStack API spec supports the following calls, each gathering important data about the user:

**API call**| **Description**  
---|---  
[Identify](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>)| The user’s identity  
[Page](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>)| Web page details of the user’s current page  
[Screen](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>)| App screen details  
[Track](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>)| Details of user actions (for example, Clicks, Sign ups, and Purchases)  
[Group](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>)| Group or organization details  
[Alias](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>)| Merge identities to a known user  
**Reset**|  Resets the information related to the previously identified user  
  
> ![warning](/docs/images/warning.svg)
> 
> Refer to the corresponding [SDK documentation](<https://www.rudderstack.com/docs/sources/event-streams/sdks/>) for the implementation specifics of the above calls.

## Send sample events

Use RudderStack’s **Event Playground app** to send sample events to RudderStack and test the data flow without any instrumentation.

Select the relevant **API method** from the dropdown and click **Send** to see the API call in the **Network** tab of your browser’s developer tools.

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


## How the API calls work

Here’s a quick overview of how the API calls work:

  1. A customer interacts with your website/app triggering an event.
  2. When an API is called, the event data is sent to the RudderStack backend.
  3. RudderStack transforms the event data into a destination-specific format.
  4. The transformed data is then sent to all requested destinations.


## Event data format

The event data is collected in JSON and includes the [Common Fields](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/>) along with API-specific fields.

**It is strongly recommended large integer values be passed as strings**. This ensures that the values are correctly transmitted to all systems (including various downstream destinations) without any issues.

RudderStack follows the [RFC 7159 standard](<https://www.rfc-editor.org/rfc/rfc7159#section-6>) which has an upper limit of 253 for integers. If the values passed exceed this number, **you may lose precision**. Furthermore, certain downstream destinations have their own limitations on parsing large integer values.

## Industry Specs

  * **Mobile**
    * [Screen](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>)
    * [Application Lifecycle Events](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/>)
  * [Ecommerce](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>)
  * [Video](<https://www.rudderstack.com/docs/event-spec/standard-events/video-events-spec/>)