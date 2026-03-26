# Emarsys Cloud Mode Integration Beta

Send events to Emarsys using RudderStack cloud mode.

* * *

  * __2 minute read

  * 


After you have successfully instrumented Emarsys as a destination in RudderStack, follow this guide to correctly send your events to Emarsys in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

> ![info](/docs/images/info.svg)
> 
> RudderStack gives higher precedence to the contact list ID or custom identifier field ID specified in the `identify`/`track`/`group` events over the same fields configured in the RudderStack dashboard [configuration settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/emarsys/setup-guide/#configuration-settings>).

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) method lets you identify a user and associate them to their actions. It also lets you record any traits about them like their name, email, etc.

You can also send an ad hoc contact list ID or a custom identifier field ID via the `integrations` object in an `identify` call:
    
    
    rudderanalytics.identify("1hKOmRA4el9Z", {
      firstName: "Alex",
      lastName: "Keener",
      email: "alex@example.com"
      optin: 1,
    }, {
      integrations: {
        EMARSYS: {
          customIdentifierId: 1,
          contactListId: 'objectListId',
        },
      },
    })
    

## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to trigger an external event created in Emarsys. You must configure the external event mapping in the RudderStack dashboard first.

RudderStack currently supports single section variable type payload to trigger an external event. Follow [Emarsys documentation](<https://dev.emarsys.com/docs/core-api-reference/fl0xx6rwfbwqb-trigger-an-external-event>) for more information.

You can send the custom identifier and `trigger_id` in the `integrations` object in a `track` call:
    
    
    rudderanalytics.track('Order Completed', {
      company: 'testComp',
      data: {
        section_group1: [{
            section_variable1: 'some_value',
            section_variable2: 'another_value',
          },
          {
            section_variable1: 'yet_another_value',
            section_variable2: 'one_more_value',
          },
        ],
        global: {
          global_variable1: 'global_value',
          global_variable2: 'another_global_value',
        },
      },
      attachment: [{
        filename: 'example.pdf',
        data: 'ZXhhbXBsZQo=',
      }, ],
    }, {
      'EMARSYS': {
        trigger_id: 'EVENT_TRIGGER_ID',
        customIdentifierId: 'custom_id',
      }
    });
    

### Property mappings

The following table lists the property mappings between RudderStack and Emarsys:

RudderStack property| Emarsys property  
---|---  
`message.properties.data`| `data`  
`message.properties.attachment`| `attachment`  
`message.timestamp`  
`message.originalTimestamp`| `event_time`  
  
## Group

You can use the [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call to insert an already created contact in a contact list.

RudderStack maps the contact list ID from `groupId` and if `groupId` is absent, it maps it from the default contact list configured in the RudderStack dashboard.

You can send an adhoc custom identifier field ID in the `integrations` object in a `group` call:
    
    
    rudderanalytics.group("group123", {
      company: 'Sample Company',
    }, {
      integrations: {
        All: true,
        EMARSYS: {
          customIdentifierId: 'custom_id',
        },
      },
    });