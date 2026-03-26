# Salesforce Cloud Mode Integration Deprecated

Send events to Salesforce using RudderStack cloud mode.

* * *

  * __5 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **This destination is deprecated**.
> 
> To send events from RudderStack to Salesforce, use the [Salesforce v2](<https://www.rudderstack.com/docs/destinations/streaming-destinations/salesforce-v2/>) destination integration instead.

After you have successfully instrumented Salesforce as a destination in RudderStack, follow this guide to correctly send your events to Salesforce in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/salesforce>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create or update leads in Salesforce.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify('1hKOmRA4GRlm', {
      name: 'Alex Keener',
      title: 'Mr.',
      email: 'alex@example.com',
      company: 'Google Inc.',
      phone: '+1-202-555-0146',
      rating: 'Hot',
      city: 'New Orleans',
      postalCode: '90002',
      country: 'US',
      street: 'Blue Gum Street',
      state: 'LA'
    });
    

Note the following:

  * You don’t require a `userId` to create a lead in Salesforce.
  * When you call `identify`, RudderStack checks if the lead already exists in Salesforce using the `email` property. If yes, the lead/contact is updated with the traits passed in the `identify` call. Otherwise, a new lead is created.
  * When you make an `identify` call with a set of user traits, RudderStack updates the appropriate record in Salesforce depending on whether it is a lead or a contact using its lead or contact ID.


### Update custom fields

> ![info](/docs/images/info.svg)
> 
> To update custom fields in Salesforce using RudderStack, make sure to first create those fields in Salesforce before sending the data through RudderStack.
> 
> For more information, see this [Salesforce Help article](<https://help.salesforce.com/articleView?id=sf.adding_fields.htm&type=5>).

As the [Salesforce Leads API](<https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_lead.htm>) requires`lastName` and `company` to be present, absence of either of these fields will result in RudderStack automatically appending the `'n/a'` to both the fields—even if they have been specified in some previous request.

For example, to collect a custom trait in RudderStack named `newProp`, you must create a field label named `newProp`. This will generate an API name as `newProp__c`. RudderStack automatically appends the `__c` to any custom trait.

> ![warning](/docs/images/warning.svg)
> 
> Make sure the casing across the custom fields and `identify` traits is consistent.
> 
> For example, if the custom fields are created in the camel case, then the traits must be sent to RudderStack in the camel case only.

### Update Salesforce objects

You can create or update any [Salesforce object](<https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_list.htm>) using the `identify` events. To do so, include an `externalId` object within your `identify` call containing the Salesforce object `type` (for example, `Salesforce-Contact`, `Salesforce-Lead`, etc.) and the corresponding `id`.

RudderStack looks for the `externalId` object within your `identify` event and determines the Salesforce object type by removing `Salesforce-` from the field `type`. Then, it makes a `PATCH` request if there is an `id` present in the request and updates the record accordingly.

> ![info](/docs/images/info.svg)
> 
> A new record is created in Salesforce if:
> 
>   * The `id` field is not present in the `externalId` object, or
>   * The `id` does not exist in Salesforce.
> 


A sample `identify` call highlighting the `externalId` object schema is shown below:
    
    
    rudderanalytics.identify('1hKOmRA4GRlm', {
      FirstName: "Alex",
      LastName: "Keener",
      Email: "alex@example.com"
    }, {
      externalId: [{
        type: "Salesforce-Contact",
        id: "sf-contact-id"
      }]
    });
    

In the above example, RudderStack updates the Salesforce `Contact` object with `id` as `sf-contact-id` and sends the user’s traits (first name, last name, and email) to Salesforce.

#### Create new records

To create new records, include only the `type` field in the `externalId` object within your `identify` call.

> ![warning](/docs/images/warning.svg)
> 
> Do not include the `id` property when creating new records as it will cause an API failure.
    
    
    rudderanalytics.identify('1hKOmRA4GRlm', {
      FirstName: "Alex",
      LastName: "Keener",
      Email: "alex@example.com"
    }, {
      externalId: [{
        type: "Salesforce-Contact"
      }]
    });
    

If you do not specify the `type` field, RudderStack creates a `Lead` object in Salesforce by default and maps the `traits` to it. For other objects, RudderStack does not modify the `traits`—they are sent to Salesforce as is.

#### Create multiple objects

You can also pass multiple object types in a single request and RudderStack will create that many requests to Salesforce.

> ![info](/docs/images/info.svg)
> 
> You can use this technique to create multiple Salesforce leads with the same email address.
    
    
    rudderanalytics.identify('1hKOmRA4GRlm', {
      FirstName: "Alex",
      LastName: "Keener",
      Email: "alex@example.com"
    }, {
      externalId: [{
          type: "Salesforce-Contact"
        },
        {
          type: "Salesforce-Lead"
        },
        {
          type: "Salesforce-Lead"
        }
      ]
    });
    

## Supported mappings

RudderStack supports and maps the event properties to several standard fields in Salesforce, as listed in the following table:

RudderStack property| Salesforce field  
---|---  
`address.accuracy`  
`accuracy`| `Accuracy`  
`company.annualRevenue`| `AnnualRevenue`  
`address.city`  
`city`| `City`  
`company.name`  
`company`| `Company`  
`address.country`  
`country`| `Country`  
`address.countryCode`  
`countryCode`| `CountryCode`  
`convertedAccountId`| `ConvertedAccountId`  
`convertedContactId`| `ConvertedContactId`  
`convertedDate`| `ConvertedDate`  
`convertedOpportunityId`| `ConvertedOpportunityId`  
`createdById`| `CreatedById`  
`createdAt`  
`createddate`| `CreatedDate`  
`description`| `Description`  
`email`| `Email`  
`emailBouncedDate`| `EmailBouncedDate`  
`emailBouncedReason`| `EmailBouncedReason`  
`firstName`| `FirstName`  
`geocodeAccuracy`| `GeocodeAccuracy`  
`id`| `Id`  
`company.industry`| `Industry`  
`individualId`| `IndividualId`  
`isConverted`| `IsConverted`  
`isDeleted`| `IsDeleted`  
`isUnreadByOwner`| `IsUnreadByOwner`  
`jigsaw`| `Jigsaw`  
`jigsawContactId`| `JigsawContactId`  
`lastActivityDate`| `LastActivityDate`  
`lastModifiedById`| `LastModifiedById`  
`lastModifiedDate`| `LastModifiedDate`  
`lastName`| `LastName`  
`lastReferencedDate`| `LastReferencedDate`  
`lastViewedDate`| `LastViewedDate`  
`address.latitude`  
`latitude`| `Latitude`  
`LeadSource`| `LeadSource`  
`address.longitude`  
`longitude`| `Longitude`  
`masterRecordId`| `MasterRecordId`  
`name`| `Name`  
`company.employee_count`| `NumberOfEmployees`  
`ownerId`| `OwnerId`  
`phone`| `Phone`  
`photoUrl`| `PhotoUrl`  
`address.postalCode`  
`postalCode`| `PostalCode`  
`rating`| `Rating`  
`salutation`| `Salutation`  
`address.state`  
`state`| `State`  
`address.stateCode`  
`stateCode`| `StateCode`  
`status`| `Status`  
`address.street`  
`street`| `Street`  
`systemModstamp`| `SystemModstamp`  
`title`| `Title`  
`website`| `Website`  
  
## FAQ

#### How do I check the number of Salesforce API calls left for the day?

To check the number of Salesforce API calls, go to **Setup** > **Administration Setup** > **Company Profile** > **Company Information**.

You should then be able to see a field called **API Requests, Last 24 Hours** , which contains the number of API calls left for the day.

#### How to fix “No such column ‘X’ on sobject of type Y” errors?

If event delivery to Salesforce fails due to a provided field not existing even though the field exists, check the field-level security settings for that field in Salesforce.

You will likely get this error when the field is **not** marked as visible to the role your RudderStack Salesforce user is using. To fix it, make the field visible to the appropriate role.