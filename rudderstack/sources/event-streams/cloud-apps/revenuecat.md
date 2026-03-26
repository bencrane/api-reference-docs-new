# RevenueCat Source Beta

Ingest your event data from RevenueCat into RudderStack.

* * *

  * __3 minute read

  * 


[RevenueCat](<https://www.revenuecat.com/>) is an in-app subscription platform that lets you analyze and grow your cross-platform app subscriptions.

This guide will help you set up RevenueCat as a source in RudderStack.

## Get started

  1. Go to your [RudderStack dashboard](<https://app.rudderstack.com/>) and click **Add Source**. From the list of **Event Streams** sources, select **RevenueCat**.
  2. Assign a name to your source and click **Continue** *.
  3. Your RevenueCat source is now configured. Go to the **Settings** tab of the source and note the **Webhook URL** :

[![RevenueCat source webhook URL](/docs/images/event-stream-sources/source-webhook-url.webp)](</docs/images/event-stream-sources/source-webhook-url.webp>)

  4. Log in to your [RevenueCat dashboard](<https://app.revenuecat.com/>).
  5. Go to **Projects** in the top nav bar and select your project.

[![RevenueCat select project](/docs/images/event-stream-sources/revenuecat-select-project.webp)](</docs/images/event-stream-sources/revenuecat-select-project.webp>)

  6. In the left nav bar, click **\+ New** in the **Integrations** section. Under **Add an integration** , select **Webhooks**.


> ![info](/docs/images/info.svg)
> 
> If you are on a legacy RevenueCat plan without access to webhooks, migrating to their new [Pro plan](<https://www.revenuecat.com/pricing/>) to get webhook integration access is recommended.

  7. In the webhook configuration window, enter the name and URL obtained in Step 3 above. You can also configure the following settings as per your requirement:


  * **Authorization header value**
  * **Environment to send events for** (Production, Sandbox, or both)
  * **Events filter**

[![RevenueCat webhook configuration](/docs/images/event-stream-sources/revenuecat-webhook-configuration.webp)](</docs/images/event-stream-sources/revenuecat-webhook-configuration.webp>)

  8. Click **ADD WEBHOOK** to finish the configuration.


> ![warning](/docs/images/warning.svg)
> 
> Make sure to test the configuration by sending a few test webhook events.

## Event transformation

RudderStack ingests the events from RevenueCat as [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events after converting them into the appropriate event format.

RudderStack supports ingesting events related to the following [RevenueCat Event Types](<https://www.revenuecat.com/docs/event-types-and-fields>):

  * `TEST`
  * `INITIAL_PURCHASE`
  * `RENEWAL`
  * `CANCELLATION`
  * `UNCANCELLATION`
  * `NON_RENEWING_PURCHASE`
  * `SUBSCRIPTION_PAUSED`
  * `EXPIRATION`
  * `BILLING_ISSUE`
  * `PRODUCT_CHANGE`
  * `TRANSFER`
  * `SUBSCRIPTION_EXTENDED`


### Property mappings

RudderStack maps the following RevenueCat properties from the event payload to the RudderStack fields:

RevenueCat property| RudderStack property  
---|---  
`type`| `event`  
`id`| `messageId`  
`app_id`| `appId`  
`event_timestamp_ms`| `originalTimestamp`  
`app_user_id`| `externalId` of type `revenuecatAppUserId`  
`original_app_user_id`| `originalAppUserId`  
`aliases`| `aliases`  
`product_id`| `productId`  
`entitlement_ids`| `entitlementIds`  
`entitlement_id`| `entitlementId`  
`period_type`| `periodType`  
`purchased_at_ms`| `purchasedAtMs`  
`grace_period_expiration_at_ms`| `gracePeriodExpirationAtMs`  
`expiration_at_ms`| `expirationAtMs`  
`auto_resume_at_ms`| `autoResumeAtMs`  
`store`| `store`  
`environment`| `environment`  
`is_trial_conversion`| `isTrialConversion`  
`cancel_reason`| `cancelReason`  
`expiration_reason`| `expirationReason`  
`new_product_id`| `newProductId`  
`presented_offering_id`| `presentedOfferingId`  
`price`| `price`  
`currency`| `currency`  
`price_in_purchased_currency`| `priceInPurchasedCurrency`  
`tax_percentage`| `taxPercentage`  
`commission_percentage`| `commissionPercentage`  
`takehome_percentage`| `takehomePercentage`  
`subscriber_attributes`| `subscriberAttributes`  
`transaction_id`| `transactionId`  
`original_transaction_id`| `originalTransactionId`  
`is_family_share`| `isFamilyShare`  
`transferred_from`| `transferredFrom`  
`transferred_to`| `transferredTo`  
`country_code`| `countryCode`  
`offer_code`| `offerCode`  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack uses `uuid` as the `anonymousId` if it does not receive the `app_user_id`, and `original_app_user_id` fields from RevenueCat.

A sample input payload ingested by RudderStack and the corresponding RudderStack-transformed `track` event is shown below:
    
    
    {
      "api_version": "1.0",
      "event": {
        "aliases": [
          "f8e14f51-0c76-49ba-8d67-c229f1875dd9",
          "389ad6dd-bb40-4c03-9471-1353da2d55ec"
        ],
        "app_user_id": "f8e14f51-0c76-49ba-8d67-c229f1875dd9",
        "commission_percentage": null,
        "country_code": "US",
        "currency": null,
        "entitlement_id": null,
        "entitlement_ids": null,
        "environment": "SANDBOX",
        "event_timestamp_ms": 1698617217232,
        "expiration_at_ms": 1698624417232,
        "id": "8CF0CD6C-CAF3-41FB-968A-661938235AF0",
        "is_family_share": null,
        "offer_code": null,
        "original_app_user_id": "f8e14f51-0c76-49ba-8d67-c229f1875dd9",
        "original_transaction_id": null,
        "period_type": "NORMAL",
        "presented_offering_id": null,
        "price": null,
        "price_in_purchased_currency": null,
        "product_id": "test_product",
        "purchased_at_ms": 1698617217232,
        "store": "APP_STORE",
        "subscriber_attributes": {
          "$displayName": {
            "updated_at_ms": 1698617217232,
            "value": "Alex Keener"
          },
          "$email": {
            "updated_at_ms": 1698617217232,
            "value": "alex@example.com"
          },
          "$phoneNumber": {
            "updated_at_ms": 1698617217232,
            "value": "+19795551234"
          },
          "my_custom_attribute_1": {
            "updated_at_ms": 1698617217232,
            "value": "catnip"
          }
        },
        "takehome_percentage": null,
        "tax_percentage": null,
        "transaction_id": null,
        "type": "TEST"
      }
    }
    
    
    
    {
      "context": {
        "library": {
          "name": "unknown",
          "version": "unknown"
        },
        "integration": {
          "name": "RevenueCat"
        },
        "externalId": [
          {
            "type": "revenuecatAppUserId",
            "id": "f8e14f51-0c76-49ba-8d67-c229f1875dd9"
          }
        ]
      },
      "integrations": {
        "RevenueCat": false
      },
      "properties": {
        "aliases": [
          "f8e14f51-0c76-49ba-8d67-c229f1875dd9",
          "389ad6dd-bb40-4c03-9471-1353da2d55ec"
        ],
        "appUserId": "f8e14f51-0c76-49ba-8d67-c229f1875dd9",
        "commissionPercentage": null,
        "countryCode": "US",
        "currency": null,
        "entitlementId": null,
        "entitlementIds": null,
        "environment": "SANDBOX",
        "eventTimestampMs": 1698617217232,
        "expirationAtMs": 1698624417232,
        "id": "8CF0CD6C-CAF3-41FB-968A-661938235AF0",
        "isFamilyShare": null,
        "offerCode": null,
        "originalAppUserId": "f8e14f51-0c76-49ba-8d67-c229f1875dd9",
        "originalTransactionId": null,
        "periodType": "NORMAL",
        "presentedOfferingId": null,
        "price": null,
        "priceInPurchasedCurrency": null,
        "productId": "test_product",
        "purchasedAtMs": 1698617217232,
        "store": "APP_STORE",
        "subscriberAttributes": {
          "$displayName": {
            "updated_at_ms": 1698617217232,
            "value": "Alex Keener"
          },
          "$email": {
            "updated_at_ms": 1698617217232,
            "value": "alex@example.com"
          },
          "$phoneNumber": {
            "updated_at_ms": 1698617217232,
            "value": "+19795551234"
          },
          "my_custom_attribute_1": {
            "updated_at_ms": 1698617217232,
            "value": "catnip"
          }
        },
        "takehomePercentage": null,
        "taxPercentage": null,
        "transactionId": null,
        "type": "TEST"
      },
      "type": "track",
      "event": "TEST",
      "messageId": "8CF0CD6C-CAF3-41FB-968A-661938235AF0",
      "originalTimestamp": "2023-10-29T22:06:57.232Z",
      "sentAt": "2023-10-29T22:06:57.232Z"
    }