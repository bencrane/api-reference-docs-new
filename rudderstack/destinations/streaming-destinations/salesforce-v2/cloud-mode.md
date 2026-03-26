# Salesforce v2 Cloud Mode Integration

Send events to Salesforce using RudderStack cloud mode.

* * *

  * __5 minute read

  * 


RudderStack lets you identify your leads in Salesforce without having to use the REST APIs.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/salesforce>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to create or update leads in Salesforce.

The following code snippet demonstrates a sample `identify` call:
    
    
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
    

When you make an `identify` call, RudderStack checks if the lead already exists using the `email` property. If yes, the lead/contact is updated with the traits passed in the `identify` event. If not, RudderStack creates a new lead in Salesforce.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * You don’t require a `userId` to create a lead in Salesforce.
>   * When you make an `identify` call with a set of user traits, RudderStack updates the appropriate record in Salesforce depending on whether it is a lead or a contact using its lead or contact ID.
> 


### Update custom fields in Salesforce

> ![warning](/docs/images/warning.svg)
> 
> **Before you update custom fields in Salesforce using RudderStack**
> 
> Make sure to create the custom fields in Salesforce before sending them via RudderStack.
> 
> See the [Salesforce Help](<https://help.salesforce.com/articleView?id=sf.adding_fields.htm&type=5>) guide for more information.

As the [Salesforce Leads API](<https://developer.salesforce.com/docs/atlas.en-us.api.meta/api/sforce_api_objects_lead.htm>) requires`lastName` and `company` to be present, absence of either of these fields results in RudderStack automatically appending the `'n/a'` to both the fields - even if you have specified them in some previous request.

For example, if you want to collect a custom trait in RudderStack named `newProp`, create a field label named `newProp`. This will generate an API name as `newProp__c`. RudderStack automatically appends the `__c` to any custom trait.

> ![warning](/docs/images/warning.svg)
> 
> **Make sure the casing is consistent**.
> 
> For example, if you create the custom fields in camel case, then you must send the traits to RudderStack in camel case only.

## Update Salesforce objects

You can create or update any [Salesforce object](<https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_list.htm>) using the `identify` event. To specify the object type, follow the below schema.

RudderStack looks for the key `externalId` under `context` and processes the `type` field as follows:

Field| Behavior  
---|---  
Standard Salesforce IDs| Removes the `Salesforce-` prefix from the `type` field to determine the object type (for example, `Salesforce-Contact` becomes `Contact`).  
External ID fields| When the `type` field contains a forward slash (for example, `Salesforce-EmailMessage/ExternalMessageId__c`), RudderStack removes the `Salesforce-` prefix, preserving the forward slash and the external ID field name. The resulting string (`EmailMessage/ExternalMessageId__c`) is used directly in the endpoint path.  
  
RudderStack makes a `PATCH` request if there is an `id` present in the request to update the record. Otherwise, it creates a new record in Salesforce.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * You cannot send an `id` property when creating new records as it will lead to an API failure.
>   * When creating new records, only provide the `type: "Salesforce-Contact"` portion of the `externalId` object.
> 


### Update records using standard Salesforce IDs

You can pass multiple object types in a single request and RudderStack creates that many requests to Salesforce, as shown:
    
    
    rudderanalytics.identify('123456',
        {
          FirstName: "John",
          LastName: "Gibbs",
          Email: "john@peterson.com"
        },
        {
          externalId: [
            {
              type: "Salesforce-Contact",
              id: "sf-contact-id"
            }
          ]
        });
    

In the above example, RudderStack updates the `Contact` object in Salesforce with `id` as `sf-contact-id` and sends the `traits` object to Salesforce.

> ![info](/docs/images/info.svg)
> 
> By default, RudderStack creates a `Lead` object in Salesforce and maps the `traits` object to it. RudderStack does not modify the traits for other objects — they are sent to Salesforce as is.

### Update records using external ID fields

To update records using external ID fields (custom fields marked as external IDs in Salesforce), include the external ID field name directly in the `type` field, separated by a forward slash. The `id` field should contain the actual external ID value for the record you want to update.

For example, to update an `EmailMessage` record using the `ExternalMessageId__c` external ID field:
    
    
    rudderanalytics.identify('123456',
        {
          Subject: "Updated Email Subject",
          TextBody: "Updated email body content"
        },
        {
          externalId: [
            {
              type: "Salesforce-EmailMessage/ExternalMessageId__c",
              id: "5f48f9285a6f48d78ef6b34d6fd17ffc12345"
            }
          ]
        });
    

In this example, RudderStack constructs the endpoint as `/sobjects/EmailMessage/ExternalMessageId__c/5f48f9285a6f48d78ef6b34d6fd17ffc12345?_HttpMethod=PATCH` to update the record.

#### Troubleshooting

If you encounter errors when trying to update records using external ID fields, ensure that you include the external ID field name in the `type` field, not in the `id` field.

**Issue**

When using external ID fields for `PATCH` operations, Salesforce rejects the request if the endpoint is incorrectly constructed.

**Error**

Salesforce returns an error indicating that `PATCH` is not allowed on the endpoint being used. For example, if you structure the `externalId` as follows:
    
    
    {
      externalId: [
        {
          type: "Salesforce-EmailMessage",
          id: "ExternalMessageId__c"
        }
      ]
    }
    

RudderStack constructs the endpoint as `/sobjects/EmailMessage/ExternalMessageId__c?_HttpMethod=PATCH`, which Salesforce rejects because the actual record ID value is missing from the URL.

**Solution**

Include the external ID field name in the `type` field and provide the actual external ID value in the `id` field, as shown:
    
    
    {
      externalId: [
        {
          type: "Salesforce-EmailMessage/ExternalMessageId__c",
          id: "5f48f9285a6f48d78ef6b34d6fd17ffc12345"
        }
      ]
    }
    

This way, RudderStack correctly constructs the endpoint as `/sobjects/EmailMessage/ExternalMessageId__c/5f48f9285a6f48d78ef6b34d6fd17ffc12345?_HttpMethod=PATCH`, and the `PATCH` request works.

## Supported mappings

RudderStack supports and maps the event properties to several standard fields in Salesforce, as listed in the following table:

RudderStack property| Salesforce field  
---|---  
`address.accuracy` / `accuracy`| `Accuracy`  
`company.annualRevenue`| `AnnualRevenue`  
`address.city` / `city`| `City`  
`company.name` / `company`| `Company`  
`address.country` / `country`| `Country`  
`address.countryCode` / `countryCode`| `CountryCode`  
`convertedAccountId`| `ConvertedAccountId`  
`convertedContactId`| `ConvertedContactId`  
`convertedDate`| `ConvertedDate`  
`convertedOpportunityId`| `ConvertedOpportunityId`  
`createdById`| `CreatedById`  
`createdAt` / `createddate`| `CreatedDate`  
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
`address.latitude` / `latitude`| `Latitude`  
`LeadSource`| `LeadSource`  
`address.longitude` / `longitude`| `Longitude`  
`masterRecordId`| `MasterRecordId`  
`name`| `Name`  
`company.employee_count`| `NumberOfEmployees`  
`ownerId`| `OwnerId`  
`phone`| `Phone`  
`photoUrl`| `PhotoUrl`  
`address.postalCode` / `postalCode`| `PostalCode`  
`rating`| `Rating`  
`salutation`| `Salutation`  
`address.state` / `state`| `State`  
`address.stateCode` / `stateCode`| `StateCode`  
`status`| `Status`  
`address.street` / `street`| `Street`  
`systemModstamp`| `SystemModstamp`  
`title`| `Title`  
`website`| `Website`