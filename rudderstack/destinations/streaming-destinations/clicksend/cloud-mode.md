# ClickSend Cloud Mode Integration Beta

Send events to ClickSend using RudderStack cloud mode.

* * *

  * __3 minute read

  * 


After you have successfully instrumented ClickSend as a destination in RudderStack, follow this guide to correctly send your events to ClickSend in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/main/src/cdk/v2/destinations/clicksend>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to [create a new contact or update an existing one](<https://developers.clicksend.com/docs/rest/v3/#create-new-contact>) in ClickSend.

A sample `identify` call is shown:
    
    
    rudderstack.identify("userId123", {
      "email": "alex@example.com",
      "firstName": "Alex",
      "lastName": "Keener",
      "phone": "1234567890",
      "address": {
        "city": "New York",
        "country": "USA",
        "pinCode": "123456"
      },
      "integrations": {
        "All": true
      },
      "externalId": [{
        "type": "CLICKSEND_CONTACT_LIST_ID",
        "id": "<dummy-id>"
      }]
    }
    });
    

### Supported mappings

RudderStack maps the following `identify` fields to the corresponding ClickSend properties:

RudderStack event/property| ClickSend event/property| Note  
---|---|---  
`message.traits.phone`  
`context.traits.phone`  
Required, if `fax_number` and `email` are absent.| `phone_number`| Phone number in [E.164](<https://en.wikipedia.org/wiki/E.164>) format.  
`traits.email`  
`context.traits.email`  
Required, if `fax_number` and `phone_number` are absent.| `email`| -  
`traits.fax_number`  
`context.traits.fax_number`  
Required, if `email` and `phone_number` are absent.| `fax_number`| -  
`CLICKSEND_CONTACT_LIST_ID` from `externalId` Required| Sent as a part of the API URL.| Rudderstack uses this `list_id` to create contacts in it.  
`traits.firstName`  
`context.traits.firstName`| `first_name`| -  
`traits.address`  
`traits.address_line_1`  
`context.traits.address`  
`context.traits.address_line_1`| `address_line_1`| -  
`traits.address_line_2`  
`context.traits.address_line_2`| `address_line_2`| -  
`traits.address.city`  
`context.traits.address.city`| `address_city`| -  
`traits.address.state`  
`context.traits.address.state`| `address_state`| -  
`traits.address.address_postal_code`  
`context.traits.address.address_postal_code`| `address_postal_code`| -  
`traits.country`  
`context.traits.country`| `address_country`| -  
`traits.organization_name`  
`context.traits.organization_name`| `organization_name`| -  
`traits.lastName`  
`context.traits.lastName`| `last_name`| -  
`CLICKSEND_CONTACT_ID` from `externalId`| `contact_id`| Use this property to send the `contact_id` if you want to update an existing contact.  
If absent, Rudderstack creates a new contact which can lead to the duplication.  
  
## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to send text messages to ClickSend.

A sample `track` call to trigger an SMS campaign for the entire list:
    
    
    rudderanalytics.track(
      "event1", {
        "name": "new campaign",
        "body": "message",
        "from": "alex@example.com",
        "from_email": "keener@sample.com"
      }, {
        externalId: [{
          type: 'CLICKSEND_CONTACT_LIST_ID',
          id: '12345',
        }, ],
      }
      () => {
        console.log("track call");
      }
    );
    

A sample `track` call to send SMS to a single contact:
    
    
    rudderanalytics.track("event1", {
        "name": "new campaign",
        "body": "message",
        "from": "alex@example.com",
        "from_email": "keener@sample.com",
        "custom_string": "test string"
      },
      () => {
        console.log("track call");
      }
    );
    

### Supported mappings

RudderStack maps the following `track` fields to the corresponding ClickSend properties:

RudderStack property| ClickSend property| Note  
---|---|---  
`externalId.clicksend.From`  
`config.defaultSenderEmail`  
Required| `from`| Sender ID.  
`context.traits.phone`  
Required| `to`| Recipient’s phone number in [E.164](<https://en.wikipedia.org/wiki/E.164>) format.  
`properties.body`  
Required| `body`| Your message.  
`properties.channel`  
`config.channel`| `channel`| Method of sending the text message. For example, wordpress, php, c#, etc.  
`properties.schedule`  
`config.schedule`| `schedule`| Schedule time in [UNIX format](<http://help.clicksend.com/what-is-a-unix-timestamp>). Set it as `0` for immediate delivery.  
`properties.custom_string`| `custom_string`| Your reference which is passed back with all the replies and delivery reports.  
`externalId.clicksend.list_id`| `list_id`| List ID if sending to a whole list. You can use this instead of `context.traits.phone`.  
  
**If using this, ensure that a particular list does not exceed 20000 contacts.**  
`context.traits.country`| `country`| ISO alpha-2 character country code. For example, `US` \- It is used to format the recipient number if it’s not in international format.  
`properties.from_email`| `from_email`| Email address to send the reply. If omitted, the reply is emailed back to the user who sent the outgoing SMS.