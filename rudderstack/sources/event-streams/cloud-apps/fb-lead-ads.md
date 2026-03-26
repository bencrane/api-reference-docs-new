# Facebook Lead Ads Source Beta

Ingest your event data from Facebook Lead Ads into RudderStack.

* * *

  * __3 minute read

  * 


> ![announcement](/docs/images/announcement.svg)
> 
> This feature is in **Closed Beta** as part of RudderStack’s [Early Access Program](<https://www.rudderstack.com/docs/get-started/alpha-and-beta-features/beta-features/closed-beta/>), where we work with early users and customers to test new features and get feedback before making them generally available.
> 
> [Contact the Product team](<mailto:product@rudderstack.com>) if you have any questions.

Facebook Lead Ads lets you natively capture lead generation events from your Facebook Lead Ad campaigns directly into RudderStack.

This guide will help you set up Facebook Lead Ads as a source in RudderStack.

> ![info](/docs/images/info.svg)
> 
> This integration leverages the RudderStack Lead Ads CRM application linked to your Facebook business account.
> 
>   * **RudderStack Lead Ads US** : For US-based accounts
>   * **RudderStack Lead Ads EU (coming soon)** : For EU-based accounts
> 

> 
> Based on your RudderStack workspace region, your OAuth account (used for authentication) will be created with the appropriate region-based CRM application

## Prerequisites

  * **Prepare your Facebook lead campaign** : Ensure you have a Facebook Lead Ad campaign set up and running. If you don’t have one, create a campaign before proceeding with this integration.


## Setup

  1. Go to your [RudderStack dashboard](<https://app.rudderstack.com/>) and click **Add Source**. From the list of sources, select **Facebook Lead Ads**.
  2. Specify a name for your source.
  3. Under **Account** , click **Create account**.
  4. Select **OAuth** and click **Next**.
  5. Configure the OAuth account — specify the preferred account name and click **Connect account**. Then, authorize RudderStack to access your Facebook business account.


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Grant your OAuth account access to all Facebook pages for which you want to receive lead events with valid OAuth scopes. Then, reuse the same account across multiple Facebook Lead Ads sources created in RudderStack.

  6. After the authorization is complete, select the required Facebook page from the dropdown. Note that:


  * Each Facebook Lead Ads source can ingest events from only one Facebook page.
  * Upon creation, the source automatically listens for any `leadgen` events from the selected page.


  7. After the setup is complete, connect a destination to start receiving events from your Facebook Lead Ads campaign.


## OAuth permissions

The following OAuth scopes are required for the integration to function correctly:

  * `pages_show_list`
  * `ads_management`
  * `business_management`
  * `leads_retrieval`
  * `pages_read_engagement`
  * `pages_manage_metadata`
  * `pages_manage_ads`


## Event structure

RudderStack emits an `identify` event for every incoming `leadgen` event from the Facebook page:

  * `anonmyousId` is set to the `leadgen_id` from Facebook

  * `context.traits` contain the following information:

    * `pageId`: The Facebook page ID
    * `formId`: The lead form ID
    * All custom fields configured in the Facebook Lead Ads campaign form


A sample `identify` event payload is shown below:
    
    
    {
      "anonymousId": "leadgen_123456789",
      "type": "identify",
      "messageId": "messageId_123456789",
      "context": {
        "traits": {
          "pageId": "987654321",
          "formId": "form_12345",
          "email": "alex@example.com",
          "phone": "+1234567890",
          "full_name": "Alex Keener"
        }
      },
      "originalTimestamp": "2025-02-01T10:20:00.000Z",
      "sentAt": "2025-02-01T10:20:05.000Z"
    }
    

> ![warning](/docs/images/warning.svg)
> 
> **PII visibility in incoming lead events**
> 
> The [Source Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/#source-live-events>) view in the RudderStack dashboard only displays metadata for incoming lead events. The actual PII (like email, phone, and name) appears only in the [Destination Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/#destination-live-events>) view **after** RudderStack processes the events.

## Troubleshooting

Issue| Solution  
---|---  
Events fail after changing credentials| 

  1. Go the **Settings** tab of the Facebook Lead Ads source in RudderStack.
  2. Click **Reauthorize the OAuth account** setting to restore the connection.

  
  
## FAQ

#### Why do I see duplicate events in the Live Events view?

[Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) view shows raw webhook deliveries from Facebook. Due to Facebook’s **at-least-once delivery** behavior, the same event may be delivered multiple times in transient conditions, which can briefly appear as duplicates.

#### Will this result in duplicate data in my destinations?

No — RudderStack deduplicates events using the `messageId` field, ensuring each event is ingested only once, thereby preventing duplicate records in downstream destinations.