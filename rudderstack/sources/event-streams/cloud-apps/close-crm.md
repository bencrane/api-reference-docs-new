# Close Source Beta

Ingest your event data from Close into RudderStack.

* * *

  * __3 minute read

  * 


[Close](<https://www.close.com/>) is a sales-focused customer relationship management software. It helps businesses manage leads, track communication, and automate sales processes to boost productivity and close more deals.

This guide will help you set up Close as a source in RudderStack.

## Get started

  1. Go to your [RudderStack dashboard](<https://app.rudderstack.com/>) and click **Add Source**. From the list of **Event Streams** sources, select **Close CRM**.
  2. Assign a name to your source and click **Continue**.
  3. Your Close source is now configured. Go to the **Settings** tab of the source and note the **Webhook URL** :

[![Close CRM webhook URL](/docs/images/event-stream-sources/source-webhook-url.webp)](</docs/images/event-stream-sources/source-webhook-url.webp>)

## Subscribe to the webhook

To receive events data successfully in RudderStack through Close, you must [subscribe to the webhook](<https://developer.close.com/resources/webhook-subscriptions/#create-new-webhook-subscription>) (noted in the above section).

A sample snippet to subscribe the webhook URL:
    
    
    curl --location 'https://api.close.com/api/v1/webhook/' \
    --header 'Content-Type: application/json' \
    --header 'Accept: application/json' \
    --header 'Authorization: Basic yEDZAvAraUJxZ1BmR3U4SVZEMWk5OTZnUjIuNWF3eEkyTW5vVzo=' \
    --data '{
        "url": "https://webhook.site/44541847-0141-4647-be05-4ff6b31d8d93",
        "events": [
            {
                "object_type": "lead",
                "action": "created"
            },
            {
                "object_type": "lead",
                "action": "updated"
            },
            {
                "object_type": "activity.call",
                "action": "created"
            },
            {
                "object_type": "activity.note",
                "action": "created"
            },
            {
                "object_type": "activity.note",
                "action": "updated"
            }
        ]
    }'
    

See [Close webhooks documentation](<https://developer.close.com/topics/webhooks/>) for more information.

## Event transformation

RudderStack ingests all the [Close events](<https://developer.close.com/resources/event-log/list-of-events/>) as [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events, after converting them into the appropriate event format.

### Property mappings

RudderStack maps the following Close properties from the event payload to the RudderStack fields:

Close Property| RudderStack Property| Note  
---|---|---  
`event.object_type` \+ `event.action`| `event`| -  
`event.lead_id`| `userId`| RudderStack does not use `user_id` as it is assigned to the user who creates the lead.  
`event.date_updated`| `originalTimestamp`| RudderStack converts it to the ISO 8601 date format yyyy-MM-ddTHH:mm:ss.SSSZ  
`event`| `properties`| Contains all the event data (even mapped to other fields).  
`subscriptionId`| `properties.subscription_id`| -  
`event.id`| `messageId`| -  
  
A sample input payload ingested by RudderStack:
    
    
    {
      "event": {
        "date_created": "2019-01-15T12:48:23.395000",
        "meta": {
          "request_method": "PUT",
          "request_path": "/api/v1/opportunity/oppo_7H4sjNso7FyBFaeR3RXi5PMJbilfo0c6UPCxsJtEhCO/"
        },
        "id": "ev_2sYKRjcrA79yKxi3S4Crd7",
        "action": "updated",
        "date_updated": "2019-01-15T12:48:23.395000",
        "changed_fields": [
          "confidence",
          "date_updated",
          "status_id",
          "status_label",
          "status_type"
        ],
        "previous_data": {
          "status_type": "active",
          "confidence": 70,
          "date_updated": "2019-01-15T12:47:39.873000+00:00",
          "status_id": "stat_3FD9DnGUCJzccBKTh8LiiKoyVPpMJsOkJdcGoA5AYKH",
          "status_label": "Active"
        },
        "organization_id": "orga_XbVPx5fFbKlYTz9PW5Ih1XDhViV10YihIaEgMEb6fVW",
        "data": {
          "contact_name": "Mr. Jones",
          "user_name": "Joe Kemp",
          "value_period": "one_time",
          "updated_by_name": "Joe Kemp",
          "date_created": "2019-01-15T12:41:24.496000+00:00",
          "user_id": "user_lAm7YqrzZj00t1GLK5eTOaRgdkNChswxydbhUhGRbcM",
          "updated_by": "user_lAm7YqrzZj00t1GLK5eTOaRgdkNChswxydbhUhGRbcM",
          "value_currency": "USD",
          "organization_id": "orga_XbVPx5fFbKlYTz9PW5Ih1XDhViV10YihIaEgMEb6fVW",
          "status_label": "Won",
          "contact_id": "cont_BwlwYQkIP6AooiXP1CMvc6Zbb5gGh2gPu4dqIDlDrII",
          "status_type": "won",
          "created_by_name": "Joe Kemp",
          "id": "oppo_8H4sjNso7FyBFaeR3RXi5PMJbilfo0c6UPCxsJtEhCO",
          "lead_name": "KLine",
          "date_lost": null,
          "note": "",
          "date_updated": "2019-01-15T12:48:23.392000+00:00",
          "status_id": "stat_wMS9M6HC2O3CSEOzF5g2vEGt6RM5R3RfhIQixdnmjf2",
          "value": 100000,
          "created_by": "user_lAm7YqrzZj00t1GLK5eTOaRgdkNChswxydbhUhGRbcM",
          "value_formatted": "$1,000",
          "date_won": "2019-01-15",
          "lead_id": "lead_zwqYhEFwzPyfCErS8uQ77is2wFLvr9BgVi6cTfbFM68",
          "confidence": 100
        },
        "request_id": "req_4S2L8JTBAA1OUS74SVmfbN",
        "object_id": "oppo_7H4sjNso7FyBFaeR3RXi5PMJbilfo0c6UPCxsJtEhCO",
        "user_id": "user_lAm7YqrzZj00t1GLK5eTOaRgdkNChswxydbhUhGRbcM",
        "object_type": "opportunity",
        "lead_id": "lead_zwqYhEFwzPyfCErS8uQ77is2wFLvr9BgVi6cTfbFM68"
      },
      "subscription_id": "whsub_8AmjKCZYT3zI8eZoi4HhFC"
    }
    

The RudderStack-transformed event payload is shown below:
    
    
    {
      "context": {
        "library": {
          "name": "unknown",
          "version": "unknown"
        },
        "integration": {
          "name": "CloseCRM"
        }
      },
      "integrations": {
        "CloseCRM": false
      },
      "type": "track",
      "event": "opportunity updated",
      "userId": "lead_zwqYhEFwzPyfCErS8uQ77is2wFLvr9BgVi6cTfbFM68",
      "messageId": "ev_2sYKRjcrA79yKxi3S4Crd7",
      "originalTimestamp": "2019-01-TuT12:48:23.395+00:00",
      "properties": {
        "date_created": "2019-01-15T12:48:23.395000",
        "meta": {
          "request_method": "PUT",
          "request_path": "/api/v1/opportunity/oppo_7H4sjNso7FyBFaeR3RXi5PMJbilfo0c6UPCxsJtEhCO/"
        },
        "id": "ev_2sYKRjcrA79yKxi3S4Crd7",
        "action": "updated",
        "date_updated": "2019-01-15T12:48:23.395000",
        "organization_id": "orga_XbVPx5fFbKlYTz9PW5Ih1XDhViV10YihIaEgMEb6fVW",
        "data": {
          "contact_name": "Mr. Jones",
          "user_name": "Joe Kemp",
          "value_period": "one_time",
          "updated_by_name": "Joe Kemp",
          "date_created": "2019-01-15T12:41:24.496000+00:00",
          "user_id": "user_lAm7YqrzZj00t1GLK5eTOaRgdkNChswxydbhUhGRbcM",
          "updated_by": "user_lAm7YqrzZj00t1GLK5eTOaRgdkNChswxydbhUhGRbcM",
          "value_currency": "USD",
          "organization_id": "orga_XbVPx5fFbKlYTz9PW5Ih1XDhViV10YihIaEgMEb6fVW",
          "status_label": "Won",
          "contact_id": "cont_BwlwYQkIP6AooiXP1CMvc6Zbb5gGh2gPu4dqIDlDrII",
          "status_type": "won",
          "created_by_name": "Joe Kemp",
          "id": "oppo_8H4sjNso7FyBFaeR3RXi5PMJbilfo0c6UPCxsJtEhCO",
          "lead_name": "KLine",
          "note": "",
          "date_updated": "2019-01-15T12:48:23.392000+00:00",
          "status_id": "stat_wMS9M6HC2O3CSEOzF5g2vEGt6RM5R3RfhIQixdnmjf2",
          "value": 100000,
          "created_by": "user_lAm7YqrzZj00t1GLK5eTOaRgdkNChswxydbhUhGRbcM",
          "value_formatted": "$1,000",
          "date_won": "2019-01-15",
          "lead_id": "lead_zwqYhEFwzPyfCErS8uQ77is2wFLvr9BgVi6cTfbFM68",
          "confidence": 100
        },
        "request_id": "req_4S2L8JTBAA1OUS74SVmfbN",
        "object_id": "oppo_7H4sjNso7FyBFaeR3RXi5PMJbilfo0c6UPCxsJtEhCO",
        "user_id": "user_lAm7YqrzZj00t1GLK5eTOaRgdkNChswxydbhUhGRbcM",
        "object_type": "opportunity",
        "lead_id": "lead_zwqYhEFwzPyfCErS8uQ77is2wFLvr9BgVi6cTfbFM68",
        "subscription_id": "whsub_8AmjKCZYT3zI8eZoi4HhFC"
      }
    }
    

## FAQ

#### Does Close retry event delivery in case of a failure?

Yes, Close retries failed event deliveries with a retry interval that exponentially backs off up to every 20 minutes. Further, Close retries sending events up to 72 hours before dropping them.

#### Does the Close support event ordering?

No, Close does not ensure event ordering due to [event consolidation](<https://developer.close.com/resources/event-log/#event-consolidation>), delivery parallelism/retries and other factors.