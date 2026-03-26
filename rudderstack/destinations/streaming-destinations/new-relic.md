# New Relic

Send your event data from RudderStack to New Relic.

* * *

  * __3 minute read

  * 


[New Relic](<https://newrelic.com/>) is a leading observability platform that lets you monitor, debug, and enhance your tech stack.

RudderStack supports New Relic as a destination to which you can seamlessly send your event data.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/cdk/v1/new_relic>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **New Relic** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to New Relic, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **New Relic**.
  2. Assign a name to the destination and click **Continue**.


### Connection settings

To successfully configure New Relic as a destination, you will need to configure the following settings:

[![New Relic connection settings](/docs/images/event-stream-destinations/new-relic-connection-settings.webp)](</docs/images/event-stream-destinations/new-relic-connection-settings.webp>)

  * **Account ID** : Enter your [New Relic account ID](<https://docs.newrelic.com/docs/accounts/accounts-billing/account-structure/account-id/>).


> ![info](/docs/images/info.svg)
> 
> For more information on finding the account ID based on your New Relic user model, refer to the FAQ section below.

  * **Insert Key** : Enter your New Relic insert key.


> ![info](/docs/images/info.svg)
> 
> For more information on getting your New Relic insert key, refer to the FAQ section below.

  * **Data Center** : Choose the data center associated with your New Relic account. By default, it is set to **US**.
  * **Custom Default Event Type** : Use this field to define any custom `eventType` for any unmapped `track` calls. By default, RudderStack sets the `eventType` as `rudderstack`.
  * **Send Device Context** : If this setting is enabled, RudderStack flattens all contextual fields delimited by a period (`.`) before sending them to New Relic.


> ![success](/docs/images/tick.svg)
> 
> Enabling this setting is recommended as getting rich device context is very useful in New Relic.

  * **Send User ID and Anonymous ID** : Enable this option to send `userId` and `anonymousId` in your events to New Relic.


## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) method lets you capture user events along with the properties associated with them.

RudderStack uses the `track` calls to send custom events to New Relic via the [Event API](<https://docs.newrelic.com/docs/data-apis/ingest-apis/event-api/introduction-event-api/>).

A sample `track` call is shown below:
    
    
    rudderanalytics.track(
      "Email Opened", {
        subject: "Resume validation",
        sendtime: "2022-01-01",
        sendlocation: "alex@example.com"
      }, {
        context: {
          traits: {
            email: "alex@example.com"
          }
        }
      }
    );
    

RudderStack applies the following rules to the event properties before sending them to New Relic:

  * Booleans are transformed into strings.
  * [NRQL words](<https://docs.newrelic.com/docs/data-apis/custom-data/custom-events/data-requirements-limits-custom-event-data/#:~:text=to%20the%20logs.-,NRQL%20syntax%20terms,-If%20you%20need>) are wrapped with backticks.
  * [Reserved words](<https://docs.newrelic.com/docs/data-apis/custom-data/custom-events/data-requirements-limits-custom-event-data/#reserved-words>) are removed.


## FAQ

#### Where can I find the New Relic account ID?

To find the New Relic account ID, log into your [New Relic dashboard](<https://one.newrelic.com>).

Depending on your [user model](<https://docs.newrelic.com/docs/accounts/original-accounts-billing/original-users-roles/overview-user-models/>), the steps are listed below:

  * **New Relic One user model** : In the top right section of the dashboard, go to your account settings and navigate to **Administration** > **Organization and access** > **Accounts**. You can find your account ID here.
  * **Original user model** : In the top right section of your New Relic dashboard, go to your account settings and click **API keys**. Your account ID will be displayed here.


#### Where can I find the New Relic insert key?

To find your New Relic insert key, follow these steps:

  1. Log into your [New Relic dashboard](<https://one.newrelic.com>).
  2. Go to **API Keys**.
  3. Find the key of type **INGEST-LICENSE** (used as insert key):

[![New Relic insert key](/docs/images/event-stream-destinations/new-relic-insert-key.webp)](</docs/images/event-stream-destinations/new-relic-insert-key.webp>)