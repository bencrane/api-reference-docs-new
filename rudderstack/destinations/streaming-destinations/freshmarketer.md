# Freshmarketer

Send your event data from RudderStack to Freshmarketer.

* * *

  * __7 minute read

  * 


[Freshmarketer](<https://www.freshworks.com/crm/marketing/>) is a [Freshsales](<https://www.freshworks.com/>) ecommerce CRM platform. It is a marketing automation tool that offers a unified marketing, sales, and CRM platform to engage your customer base and grow your business.

RudderStack supports Freshmarketer as a destination where you can seamlessly send your event data.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** AMP , Android (Java) , Android (Kotlin) , Cordova, Cloud, Flutter, iOS (Obj-C) , iOS (Swift) , React Native , Unity, Warehouse, Web, Shopify
  * Refer to it as **Freshmarketer** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Freshmarketer, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Freshmarketer**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure Freshmarketer as a destination, you will need to configure the following settings:

[![Freshmarketer connection settings](/docs/images/event-stream-destinations/freshmarketer-connection-settings.webp)](</docs/images/event-stream-destinations/freshmarketer-connection-settings.webp>)

  * **API Key** : Enter your Freshmarketer API key.


> ![info](/docs/images/info.svg)
> 
> For more information on obtaining your Freshmarketer API key, refer to the FAQ section below.

  * **Domain** : Enter the full organization URL associated with your Freshsales account. For example, `testcompany.myfreshworks.com`.


> ![info](/docs/images/info.svg)
> 
> For more information on your organization URL and how to change it, refer to this [Freshmarketer support guide](<https://support.freshworks.com/en/support/solutions/articles/50000002731-what-is-and-how-can-i-change-my-organization-url->).

  * **Map your events with Freshmarketer Standard Events** : Use this setting to map the standard Freshmarketer events with the custom event names.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create or update your Freshmarketer contact.

RudderStack uses the Freshmarketer [Upsert a Contact](<https://developers.freshworks.com/crm/api/#upsert_a_contact>) API to pass the relevant user information via the following parameters:

Attribute| Type| Description  
---|---|---  
`unique_identifier`| String| RudderStack passes the user’s `email`.  
`contact`| Hashed Object| RudderStack passes the other relevant user details required to create or update the user in Freshmarketer.  
  
> ![info](/docs/images/info.svg)
> 
> If `email` already exists, the contact details are updated. Otherwise, RudderStack creates a new user in Freshmarketer.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      email: "alex@example.com",
      firstName: "Alex",
      lastName: "Keener",
      state: "Louisiana",
      country: "USA",
      postalCode: "90009",
    });
    

The following table lists the mappings between the RudderStack and Freshmarketer properties:

RudderStack property| Freshmarketer property  
---|---  
`traits.email`  
`context.traits.email`  
Required| `emails`  
`traits.firstname`  
`traits.first_name`  
`traits.firstName`  
  
`context.traits.firstname`  
`context.traits.first_name`  
`context.traits.firstName`| `first_name`  
`traits.lastname`  
`traits.last_name`  
`traits.lastName`  
  
`context.traits.lastname`  
`context.traits.last_name`  
`context.traits.lastName`| `last_name`  
`traits.subscriptionStatus`  
`context.traits.subscriptionStatus`| `subscription_status`  
`traits.job_title`  
`traits.jobTitle`  
`context.traits.job_title`  
`context.traits.jobTitle`| `job_title`  
`traits.phone`  
`context.traits.phone`| `work_number`  
`userId`| `external_id`  
`traits.mobileNumber`  
`context.traits.mobileNumber`| `mobile_number`  
`traits.address`  
`context.traits.address`| `address`  
`traits.address.city`  
`traits.city`  
`context.traits.address.city`  
`context.traits.city`| `city`  
`traits.address.state`  
`traits.state`  
`context.traits.address.state`  
`context.traits.state`| `state`  
`traits.address.postalCode`  
`traits.zip`  
`traits.zipcode`  
`context.traits.zip`  
`context.traits.zipcode`  
`context.traits.address.postalCode`| `zipcode`  
`traits.address.country`  
`traits.country`  
`context.traits.address.country`  
`context.traits.country`| `country`  
`traits.salesAccounts`  
`context.traits.salesAccounts`| `sales_accounts`  
`traits.territoryId`  
`context.traits.territoryId`| `territory_id`  
`traits.leadSourceId`  
`context.traits.leadSourceId`| `lead_source_id`  
`traits.ownerId`  
`context.traits.ownerId`| `owner_id`  
`traits.subscriptionTypes`  
`context.traits.subscriptionTypes`| `subscription_types`  
`traits.medium`  
`context.traits.medium`| `medium`  
`traits.campaignId`  
`traits.campaign_id`  
`context.traits.campaignId`  
`context.traits.campaign_id`  
`context.campaign.name`| `campaign_id`  
`traits.keyword`  
`context.traits.keyword`  
`context.campaign.term`| `keyword`  
`traits.timeZone`  
`context.traits.timeZone`| `time_zone`  
`traits.facebookUserName`  
`context.traits.facebookUserName`| `facebook`  
`traits.twitterUserName`  
`context.traits.twitterUserName`| `twitter`  
`traits.linkedinUserName`  
`context.traits.linkedinUserName`| `linkedin`  
`createdAt`| `created_at`  
`timestamp`| `updated_at`  
`traits.contactStatusId`  
`context.traits.contactStatusId`| `contact_status_id`  
`traits.salesAccountId`  
`context.traits.salesAccountId`| `sales_account_id`  
`traits.lifecycleStageId`  
`context.traits.lifecycleStageId`| `lifecycle_stage_id`  
  
## Track

You can use the RudderStack [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to track the user activities in Freshmarketer.

> ![info](/docs/images/info.svg)
> 
> To make a `track` call successfully, you must map the event to be sent in the `track` call in the **Map your events with Freshmarketer Standard Events** dashboard setting.

RudderStack supports the following `track` events:

### Lifecycle stage

Lifecycle stage events capture the decision journey of a customer. Refer to the [Freshsales documentation](<https://support.freshsales.io/en/support/solutions/articles/50000003344-how-to-manage-lifecycle-stages-and-status-for-contacts->) to create lifecycle stages in Freshmarketer.

RudderStack lets you update the status of a contact in their lifecycle stage by using either the `lifecycleStageId` or `lifecycleStageName`.

> ![info](/docs/images/info.svg)
> 
> `lifecycleStageName` is a case-sensitive field and throws an error if not used in the intended manner.

A sample `track` call for a lifecycle stage event is shown below:
    
    
    rudderanalytics.track("eventName", {
      email: "alex@example.com",
      lifecycleStageId: 71010794467,
      phone: "+1-202-555-0146",
      owner_id: "70000090119",
    });
    

The following table lists the property mappings betweeen RudderStack and Freshmarketer for lifecycle stage events:

RudderStack property| Freshmarketer property  
---|---  
`email`  
Required| `email`  
`lifecycleStageName`  
Required, if lifecycleStageId is absent.| `lifecycleStageName`  
`lifecycleStageId`  
Required, if lifecycleStageName is absent.| `lifecycle_stage_id`  
  
### Sales activities

[Sales activities](<https://developers.freshworks.com/crm/api/#sales-activities>) events can be used to track any activity related to a contact/deal/account. Refer to the [Freshsales documentation](<https://support.freshsales.io/en/support/solutions/articles/230199-how-to-configure-different-sales-activities-in-freshsales->) to create sales activities in Freshmarketer.

RudderStack lets you create the status of a contact by using either the `salesActivityTypeId` or `salesActivityName`.

A sample `track` call for a sales activity event is shown below:
    
    
    rudderanalytics.track("eventName", {
      salesActivityTypeId: "70000663932",
      title: "new contact",
      startDate: "2021-05-04T17:00:00+05:30",
      endDate: "2022-06-04T17:30:00+05:30",targetable_type
      ownerId: "70054866612",
    });
    

The following table lists the property mappings betweeen RudderStack and Freshmarketer for sales activity events:

RudderStack property| Freshmarketer property  
---|---  
`properties.title`  
Required| `title`  
`properties.salesActivityName`  
Required, if properties.salesActivityTypeId is absent.| `sales_activity_name`  
`properties.salesActivityTypeId`  
Required, if properties.salesActivityName is absent.| `sales_activity_type_id`  
`properties.startDate`  
Required| `start_date`  
`properties.endDate`  
Required| `end_date`  
`context.externalId.type`  
Required| `targetable_type`  
`properties.ownerId`  
Required| `owner_id`  
`salesActivityOutcomeId`| `sales_activity_outcome_id`  
`properties.notes`| `notes`  
`context.externalId.id`| `targetable_id`  
`properties.createrId`| `creater_id`  
`originalTimestamp`| `created_at`  
`timestamp`| `updated_at`  
`properties.location`| `location`  
`latitude`  
`context.address.latitude`  
`context.location.latitude`| `latitude`  
`longitude`  
`context.address.longitude`  
`context.location.longitude`| `longitude`  
`properties.checkedinAt`| `checkedin_at`  
  
> ![info](/docs/images/info.svg)
> 
> The `targetable_type` field denotes the entity for which the sales activity has been created and can take `Contact`/`SalesAccount`/`Deal` as its value. However, if its value is set to `contact`, then either the `targetable_id` or `email` is required.

## Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call lets you link an identified Freshmarketer contact with a company, organization, or an account. You can also record any custom group traits like the company name, number of employees, etc.

> ![info](/docs/images/info.svg)
> 
> To make a `group` call successfully, you must pass the `groupType` field with value as `accounts` or `marketing_lists`.

### Accounts

RudderStack uses the [Upsert an Account](<https://developers.freshworks.com/crm/api/#upsert_an_account>) API to create or update a [sales account](<https://developers.freshworks.com/crm/api/#accounts>) via the following parameters:

Attribute| Type| Description  
---|---|---  
`unique_identifier`| String| RudderStack passes the account `name`.  
`sales_account`| Hashed Object| RudderStack passes the other relevant details associated with the Freshmarketer account.  
  
> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * If `name` already exists, RudderStack updates the Freshmarketer account details. Otherwise, it creates a new account in Freshmarketer.
>   * RudderStack also checks if the contact’s `email` is present in the `context.traits` object. If yes, RudderStack links the contact to the Freshmarketer account.
> 


A sample `group` call is shown below:
    
    
    rudderanalytics.group(
      "group01", {
        groupType: "accounts",
        name: "Alex Keener",
        phone: "1234567890",
        numberOfEmployees: 51,
        annualRevenue: 10000,
        zipcode: 90009,
        street: "6649 N Blue Gum Street",
        city: "New Orleans",
        state: "Louisiana",
        country: "USA"
      }, {
        context: {
          traits: {
            email: "alex@example.com"
          }
        }
      }
    );
    

The following table lists the mappings between the RudderStack and Freshmarketer properties to create or update an account:

RudderStack property| Freshmarketer property  
---|---  
`name`  
Required| `name`  
`traits.industryTypeId`  
`context.traits.industryTypeId`| `industry_type_id`  
`traits.businessTypeId`  
`context.traits.businessTypeId`  
`traits.business_type_id`  
`context.traits.business_type_id`| `business_type_id`  
`phone`| `phone`  
`traits.numberOfEmployees`  
`context.traits.numberOfEmployees`| `number_of_employees`  
`traits.annualRevenue`  
`context.traits.annualRevenue`| `annual_revenue`  
`traits.address`  
`context.traits.address`| `address`  
`traits.city`  
`traits.address.city`  
`context.traits.city`  
`context.traits.address.city`| `city`  
`traits.state`  
`traits.address.state`  
`context.traits.state`  
`context.traits.address.state`| `state`  
`traits.country`  
`traits.address.country`  
`context.traits.country`  
`context.traits.address.country`| `country`  
`zipcode`| `zipcode`  
`traits.website`  
`context.traits.website`| `website`  
`traits.territoryId`  
`context.traits.territoryId`| `territory_id`  
`traits.parentSalesAccountid`  
`context.traits.parentSalesAccountid`| `parent_sales_account_id`  
`traits.ownerId`  
`context.traits.ownerId`| `ownerId`  
`traits.facebookUserName`  
`context.traits.facebookUserName`| `facebook`  
`traits.twitterUserName`  
`context.traits.twitterUserName`| `twitter`  
`traits.linkedinUserName`  
`context.traits.linkedinUserName`| `linkedin`  
`createdAt`| `created_at`  
`timestamp`| `updated_at`  
  
### Marketing lists

[Marketing lists](<https://developers.freshworks.com/crm/api/#marketing-lists>) help you group contacts into lists which you can quickly invoke for marketing campaigns and bulk emailing.

RudderStack lets you add one or more contacts to a specified marketing list. To do so, you need to provide the contact’s `email` and `listId`/`listName`. Also, RudderStack creates a new marketing list if the `listName` (case-sensitive) does not exist already.

A sample `group` call to add a contact to a marketing list is shown below:
    
    
    rudderanalytics.group("group01", {
      groupType: "marketing_lists",
      email: "alex@example.com",
      listName: "listIdX123",
    });
    

The following table lists the property mappings between RudderStack and Freshmarketer to create marketing lists:

RudderStack property| Freshmarketer property  
---|---  
`email`  
Required| `email`  
`listId`  
Required, if listName is absent.| `listId`  
`listName`  
Required, if listId is absent.| `listName`  
  
## Type conversion and invalid format error

The following event properties accept only the number data type:

  * `territoryId`
  * `leadSourceId`
  * `ownerId`
  * `campaignId`
  * `contactStatusId`
  * `lifecycleStageId`
  * `industryTypeId`
  * `businessTypeId`
  * `numberOfEmployees`
  * `parentSalesAccountid`


If any of the above properties are present in any `identify` or `group` call in a different format, RudderStack will try to convert them into the number data type. If the type conversion is unsuccessful, RudderStack will give an “invalid format” error.

## FAQ

#### Where can I find the Freshmarketer API key?

To obtain your Freshmarketer API key, follow these steps:

  1. Log into your [Freshmarketer dashboard](<https://www.freshworks.com/crm/login/>).
  2. Go to **Personal Settings** > **API Settings**.
  3. Enable the captcha to complete the authentication process.
  4. You will find your Freshmarketer API key listed under the **API Authentication** section:

[![Freshmarketer API key](/docs/images/event-stream-destinations/freshmarketer-api-key.webp)](</docs/images/event-stream-destinations/freshmarketer-api-key.webp>)

> ![info](/docs/images/info.svg)
> 
> For more information, refer to this [Freshmarketer support guide](<https://crmsupport.freshworks.com/en/support/solutions/articles/50000002503-how-to-find-my-api-key->).