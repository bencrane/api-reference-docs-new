# Gainsight PX Source

Ingest your event data from Gainsight PX into RudderStack.

* * *

  * __5 minute read

  * 


[Gainsight PX](<https://www.gainsight.com/product-experience/>) is a popular product experience platform. It offers cutting-edge product analytics, product engagement features, and powers the product teams to optimize their customer adoption and onboarding flows.

This guide will help you set up Gainsight PX as a source in RudderStack.

## Get started

  1. Go to your [RudderStack dashboard](<https://app.rudderstack.com/>) and click **Add Source**. From the list of **Event Streams** sources, select **Gainsight PX**.
  2. Assign a name to your source and click **Continue**.
  3. Your Gainsight PX source is now configured. Go to the **Settings** tab of the source and note the **Webhook URL** :

[![Gainsight PX source webhook URL](/docs/images/event-stream-sources/source-webhook-url.webp)](</docs/images/event-stream-sources/source-webhook-url.webp>)

  4. Follow this [Gainsight PX user guide](<https://support.gainsight.com/PX/Integrations/01Technology_Partner_Integrations/Integrate_with_Gainsight_PX_Using_Webhooks#Configure_Webhook_in_Gainsight_PX>) to configure a custom webhook in Gainsight PX.
  5. In the **Callback URL** field, paste the RudderStack webhook URL copied in Step 3 above.

[![Gainsight PX source webhook URL configuration](/docs/images/event-stream-sources/gainsight-webhook-config.webp)](</docs/images/event-stream-sources/gainsight-webhook-config.webp>)

## Event transformation

In case of a signup event (`event.eventType == SIGN_UP`), RudderStack maps the event to an [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call as the signup event indicates that a new user is created in Gainsight PX. Otherwise, RudderStack maps the ingested event to a `track` event.

> ![warning](/docs/images/warning.svg)
> 
> Gainsight PX allows sending a maximum of 10000 webhook events per day.

### Identify

As mentioned above, RudderStack maps a Gainsight PX event to the `identify` event in case of a user signup.

A sample input payload is shown below:
    
    
    {
      "user": {
        "aptrinsicId": "XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXX",
        "identifyId": "New!",
        "type": "USER",
        "gender": "EMPTY_GENDER",
        "email": "userEmail@address.com",
        "firstName": "XXXXXX",
        "lastName": "XXXXX",
        "lastSeenDate": 1665582808669,
        "signUpDate": 1665582791753,
        "firstVisitDate": 1665582791753,
        "title": "Mr.",
        "score": 0,
        "accountId": "IBM",
        "numberOfVisits": 1,
        "location": {
          "countryName": "India",
        },
        "propertyKeys": [
          "AP-XXXXXXXXXXX-2-1"
        ],
        "createDate": 1685582808376,
        "lastModifiedDate": 1685582808717,
        "customAttributes": null,
        "globalUnsubscribe": false,
        "lastVisitedUserAgentData": null,
        "id": "New!",
        "lastInferredLocation": null
      },
      "account": {
        "id": "IBM",
        "name": "International Business Machine",
        "lastSeenDate": 1685582808669,
        "propertyKeys": [
          "AP-EOXPSEZGC5LA-2-1"
        ],
        "createDate": 1685578567565,
        "lastModifiedDate": 1685582808669
      },
      "event": {
        "eventType": "SIGN_UP",
        "eventId": "XXXXXXX-XXXX-XXX-XXX-XXXXXXXXX",
        "propertyKey": "AP-XXXXXXXXX-2-1",
        "date": 1665582808376,
        "sessionId": "XX-XXXXXXXXX-2-XXXXxXXXXXX-XXXXXXXX",
        "globalContext": {},
        "userType": "USER"
      },
      "configId": "XXXXXX-XXXXX-XXXX-XXXX-XXXXXX"
    }
    

RudderStack transforms this payload into the following event:
    
    
    "context": {
      "library": {
        "name": "unknown",
        "version": "unknown"
      },
      "integration": {
        "name": "GAINSIGHTPX"
      },
      "externalId": [{
        "type": "gainsightpxAptrinsicId",
        "id": "XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXX"
      }]
    },
    "integrations": {
      "GAINSIGHTPX": false
    },
    "type": "identify",
    "traits": {
      "type": "USER",
      "gender": "EMPTY_GENDER",
      "email": "userEmail@address.com",
      "firstName": "XXXXXX",
      "lastName": "XXXXX",
      "title": "Mr.",
      "score": 0,
      "globalUnsubscribe": false,
      "accountId": "IBM",
      "numberOfVisits": 1,
      "propertyKeys": [
        "AP-XXXXXXXXXXX-2-1"
      ],
      "id": "New!",
      "country": "India",
      "account": {
        "id": "IBM",
        "name": "International Business Machine",
        "numberOfEmployees": 0,
        "numberOfUsers": 0
      }
    },
    "userId": "New!",
    "createdAt": "20XX-XX-XXT13:53:11.753Z",
    "originalTimestamp": "20XX-XX-XXT13:53:11.753Z"
    

RudderStack also maps the following properties from the Gainsight PX event payload to the RudderStack properties:

Gainsight PX property| RudderStack property  
---|---  
`user`| `traits`  
`user.identifyId`| `userId`  
`user.aptrinsicId`| `context.externalId[]`  
`user.signUpDate`| `createdAt`  
`user.location.countryName`| `traits.country`  
`user.location.stateName`| `traits.state`  
`user.location`| `traits`  
`account`| `traits.account`  
`account.name`| `traits.companyName`  
`event.remoteHost`| `context.ip`  
`user.lastVisitedUserAgentData`| `context.userAgent`  
  
### Track

RudderStack ingests different event payloads depending on the Gainsight PX event type. It currently supports the following event types before mapping them to the `track` call:

  * Feature match
  * Engagement
  * Survey
  * Segment match
  * Custom event


A sample input payload is shown below:
    
    
    {
      "user": {
        "aptrinsicId": "XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXX",
        "identifyId": "New!",
        "type": "USER",
        "gender": "EMPTY_GENDER",
        "email": "userEmail@address.com",
        "firstName": "XXXXXX",
        "lastName": "XXXXX",
        "lastSeenDate": 1665582808669,
        "signUpDate": 1665582791753,
        "firstVisitDate": 1665582791753,
        "title": "Mr.",
        "score": 0,
        "accountId": "IBM",
        "numberOfVisits": 1,
        "location": {
          "countryName": "India",
        },
        "propertyKeys": [
          "AP-XXXXXXXXXXX-2-1"
        ],
        "createDate": 1685582808376,
        "lastModifiedDate": 1685582808717,
        "customAttributes": null,
        "globalUnsubscribe": false,
        "lastVisitedUserAgentData": null,
        "id": "New!",
        "lastInferredLocation": null
      },
      "account": {
        "id": "IBM",
        "name": "International Business Machine",
        "lastSeenDate": 1685582808669,
        "propertyKeys": [
          "AP-EOXPSEZGC5LA-2-1"
        ],
        "createDate": 1685578567565,
        "lastModifiedDate": 1685582808669
      },
      "event": {
        "eventType": "CUSTOM",
        "eventId": "XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX",
        "propertyKey": "AP-XXXXXXXXXXX-2-1",
        "date": 1665656881448,
        "sessionId": "AP-XXXXXXXXXXX-2-1XXXXXXXXXXXX-XXXXXXXXX",
        "globalContext": {},
        "userType": "USER",
        "eventName": "Product Clicked",
        "attributes": {
          "Audience Size": 5000,
          "name": "TESTing TRACK CALL FIRST",
          "Launched date": 1520532660000,
          "Launched": true
        },
        "url": "http://127.0.0.1:5501/GPXTEST2.html",
        "referrer": ""
      },
      "configId": "XXXXXX-XXXXX-XXXX-XXXX-XXXXXX"
    }
    

RudderStack transforms this payload into the following `track` payload:
    
    
    {
      "context": {
        "library": {
          "name": "unknown",
          "version": "unknown"
        },
        "integration": {
          "name": "GAINSIGHTPX"
        },
        "traits": {
          "type": "USER",
          "gender": "EMPTY_GENDER",
          "email": "userEmail@address.com",
          "firstName": "XXXXXX",
          "lastName": "XXXXX",
          "title": "Mr.",
          "score": 0,
          "globalUnsubscribe": false,
          "accountId": "IBM",
          "numberOfVisits": 1,
          "propertyKeys": [
            "AP-XXXXXXXXXXX-2-1"
          ],
          "id": "New!",
          "country": "India",
          "account": {
            "id": "IBM",
            "name": "International Business Machine",
            "numberOfEmployees": 0,
            "numberOfUsers": 0
          }
        },
        "externalId": [{
          "type": "gainsightpxAptrinsicId",
          "id": "XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXv"
        }]
      },
      "integrations": {
        "GAINSIGHTPX": false
      },
      "type": "track",
      "properties": {
        "propertyKey": "AP-XXXXXXXXXXX-2-1",
        "Audience Size": 5000,
        "name": "TESTing TRACK CALL FIRST",
        "Launched date": 1520532660000,
        "Launched": true,
        "url": "http://127.0.0.1:5501/GPXTEST2.html"
      },
      "userId": "New!",
      "category": "CUSTOM",
      "event": "Product Clicked",
      "sentAt": "20XX-XX-XXTXX:XX:XX.XXXZ",
      "originalTimestamp": "20XX-XX-XXTXX:XX:XX.XXXZ"
    }
    

The general property mappings for these events are listed in the below table:

Gainsight PX property| RudderStack property  
---|---  
`event.eventType`| `category`  
`event.attributes`| `properties`  
`event.date`| `sentAt`  
`user`| `context.traits`  
`event.url`| `properties.url`  
`event.remoteHost`| `properties.ip`  
`user.identifyId`| `userId`  
`user.aptrinsicId`| `context.externalId[]`  
`user.lastVisitedUserAgentData`| `userAgent`  
`event.globalContext`| `properties.globalContext`  
  
The specific property mappings based on the different Gainsight PX event types are listed as follows:

#### Feature match

Gainsight PX property| RudderStack property  
---|---  
`event.featureName`| `name`  
`event.featureId`| `properties.featureId`  
  
#### Engagement

Gainsight PX property| RudderStack property  
---|---  
`event.engagementName`| `name`  
`event.engagementId`| `properties.engagementId`  
`event.contentType`| `properties.contentType`  
`event.engagementType`| `properties.engagementType`  
`event.interaction`| `properties.interaction`  
`event.stepNumber`| `properties.engagement.stepNumber`  
`event.activation`| `properties.engagement.activation`  
  
#### Survey

Gainsight PX property| RudderStack property  
---|---  
`event.engagementName`| `name`  
`event.engagementId`| `properties.engagementId`  
`event.contentType`| `properties.contentType`  
`event.score`| `properties.survey.score`  
`event.stepNumber`| `properties.survey.stepNumber`  
`event.userInput`| `properties.survey.userInput`  
`event.questionType`| `properties.survey.questionType`  
`event.scoreType`| `properties.survey.scoreType`  
`event.surveyType`| `properties.survey.surveyType`  
`event.contactMeAllowed`| `properties.survey.contactMeAllowed`  
`event.questionText`| `properties.survey.questionText`  
`event.questionHtml`| `properties.survey.questionHtml`  
`event.answers`| `properties.survey.answers`  
`event.questionId`| `properties.survey.questionId`  
`event.activation`| `properties.engagement.activation`  
  
#### Segment

Gainsight PX property| RudderStack property  
---|---  
`event.segmentName`| `name`  
`event.segmentId`| `properties.segmentId`  
  
#### Custom event

Gainsight PX property| RudderStack property  
---|---  
`event.eventName`| `name`  
  
## FAQ

#### Why am I unable to view a new user event even after adding it in Gainsight PX?

Gainsight PX lets you track new user signups in your application, add them to your webhook queue, and send this data to your destination. However, this occurs only when Gainsight PX receives an `identify` event for the new user signed up in the last hour. For more information, refer to this [Gainsight PX webhook integration guide](<https://support.gainsight.com/PX/Integrations/01Technology_Partner_Integrations/Integrate_with_Gainsight_PX_Using_Webhooks>).