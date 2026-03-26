# Extole

Ingest your event data from Extole into RudderStack.

* * *

  * __2 minute read

  * 


[Extole](<https://www.extole.com/>) is a popular referral marketing tool. It enables you to offer an integrated, optimized, and effective customer experience for your audience.

You can now send your Extole events to RudderStack by adding a webhook that points to RudderStack. These events include the reward-specific events such as `reward_earned`,`reward_fulfilled`,`reward_sent`, etc. along with other Extole custom events.

This guide will help you in setting up Extole as a source in RudderStack.

## Get started

  1. Go to your [RudderStack dashboard](<https://app.rudderstack.com/>) and click **Add Source**. From the list of **Event Streams** sources, select **Extole**.
  2. Assign a name to your source and click **Continue**.
  3. Your Extole source is now configured. Go to the **Settings** tab of the source and note the **Webhook URL** :

[![Extole webhook URL](/docs/images/event-stream-sources/source-webhook-url.webp)](</docs/images/event-stream-sources/source-webhook-url.webp>)

  4. Go to your Extole account and select the **program** you want to use for RudderStack to ingest your data.
  5. Navigate to the **Tech Center** section from the sidebar and then select [Rewards WebHooks](<https://my.extole.com/tech-center/rewards-webhooks>).
  6. Click the **New Reward Webhook** option as seen in the following image:

[![Extole new webhook](/docs/images/event-stream-sources/extole-3.webp)](</docs/images/event-stream-sources/extole-3.webp>)

  7. In the **URL** text box, add the webhook URL obtained in **Step 3**. The URL should be of the following format:


    
    
    <DATA_PLANE_URL>/v1/webhook?writeKey=<WRITE_KEY>
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure to:
> 
>   * Replace `<DATA_PLANE_URL>` with the [data plane URL](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>) associated with your RudderStack workspace.
>   * Add the source write key obtained in **Step 3** as a query parameter to the URL. This is required to prevent the webhook from failing.
>   * Validate the endpoint before proceeding.
> 


  8. Save the endpoint.


## Event transformation

RudderStack ingests the Extole events and converts them to the RudderStack’s `track` call with the designated event name and associated properties. For example, Extole’s `event_id` is converted and set to `properties.eventId`.

> ![info](/docs/images/info.svg)
> 
> RudderStack retains the Extole event name during the mapping.

RudderStack populates the following properties from the Extole event payload to the RudderStack event:

**Extole Property**| **RudderStack Property**  
---|---  
`event_id`,| `properties.eventId`  
`event_time`| `originalTimestamp`  
`reward_id`| `properties.rewardId`  
`reward_supplier_name`| `properties.rewardSupplierName`  
`reward_supplier_id`| `properties.rewardSupplierId`  
`partner_reward_supplier_id`| `properties.partnerRewardSupplierId`  
`reward_supplier_type`| `properties.partnerRewardSupplierType`  
`person_id`| `properties.personId`  
`partner_user_id`| `properties.partnerUserId`, `userId`, `context.traits.userId`  
`face_value`| `properties.faceValue`  
`face_value_type`| `properties.faceValueType`  
`message`| `properties.message`  
`partner_reward_id`| `properties.partnerRewardId`  
`email`| `properties.email`  
`data`| `properties.data`  
`schema_version`| `properties.schemaVersion`  
  
> ![warning](/docs/images/warning.svg)
> 
> All the Extole event properties (except `reward_earned`, `reward_fulfilled`, and `reward_sent`) sent to RudderStack are directly mapped to the RudderStack event properties.