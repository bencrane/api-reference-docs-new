# Mautic

Send your event data from RudderStack to Mautic.

* * *

  * __5 minute read

  * 


[Mautic](<https://www.mautic.org/>) is an open-source marketing automation platform. It enables you to segment your contacts based on business requirements, personalize your marketing strategy, and create personalized campaigns for better customer engagement.

RudderStack supports Mautic as a destination where you can seamlessly send your event data.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Mautic** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Mautic, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Mautic**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure Mautic as a destination, you will need to configure the following settings:

  * **Username** : Enter the username associated with your Mautic account.
  * **Password** : Enter the password for the above username.
  * **Domain Method** : Choose the preferred domain method from **Domain** or **Subdomain**. It is recommended to use **Domain** if you have a self-hosted Mautic instance.
    * **Domain Name** : Specify the domain name if you have chosen **Domain** above.  
OR
    * **Subdomain Name** : Specify the subdomain associated with your Mautic instance if you have chosen **SubDomain** above. For example, if the root URL of your Mautic instance is `customdomain.domain.com`, then your subdomain name will be `customdomain`.
  * **Mautic property name to used as lookup field** : Enter a unique Mautic user property which RudderStack will use for contact lookup.


> ![info](/docs/images/info.svg)
> 
> RudderStack will retrieve this property from the user traits in the event.

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to [create](<https://developer.mautic.org/?json#create-contact>) or update a user in Mautic.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      state: "Louisiana",
      firstName: "Alex",
      lastName: "Keener",
      title: "Mr",
      zipcode: "90009",
      prospectOrCustomer: "Customer",
      country: "USA",
      website: "www.alex.com",
      subscriptionStatus: "New",
      phone: "12025550146",
    });
    

### Supported mappings

The following table lists the mappings between the **optional** RudderStack and Mautic properties:

RudderStack property| Mautic property| Data type  
---|---|---  
`context.traits.email` / `traits.email` / `properties.email`/`context.externalId.id`| `email`| String  
`traits.title` / `context.traits.title`| `title`| String  
`traits.firstName` / `traits.firstname` / `traits.first_name` / `context.traits.firstName` / `context.traits.firstname` / `context.traits.first_name`| `firstname`| Any  
`traits.lastName` / `traits.lastname` / `traits.last_name` / `context.traits.lastName` / `context.traits.lastname` / `context.traits.last_name`| `lastname`| Any  
`timestamp` / `originalTimestamp`| `last_active`| Timestamp in ISO 8601 format  
`phone`| `phone` / `mobile`| Any  
`traits.address.city`| `city`| String  
`traits.address.addressLine1`/ `context.traits.address.addressLine1`| `address1`| String  
`traits.address.addressLine2`/ `context.traits.address.addressLine2`| `address2`| String  
`traits.address`/ `context.traits.address`| `address1` \+ `address2`| String  
`traits.company.employeeCount`| `company_size`| Integer  
`traits.role` / `context.traits.role`| `role`| String  
`traits.website` / `context.traits.website` / `properties.website`| `website`| String  
`context.ip`| `IP`| String  
`context.timezone`| `timezone`| String  
`traits.subscriptionStatus` / `context.traits.subscriptionStatus`| `subscription_status`| String  
`traits.prospectOrCustomer` / `context.traits.prospectOrCustomer`| `prospect_or_customer`| String  
`traits.hasPurchased` / `context.traits.hasPurchased`| `haspurchased`| String  
`traits.state`/ `context.traits.state`| `state`| String  
`traits.zipcode` / `context.traits.zipcode` / `traits.zip` / `context.traits.zip`| `zipcode`| String  
`traits.country` / `context.traits.country`| `country`| String (Starting with a capital letter)  
  
### Getting contact details

The easiest way to retrieve contact details of an existing user in Mautic is by specifying the unique user trait in the **Mautic property name to used as lookup field** dashboard setting. RudderStack will look for this property in the event’s `traits` or `context.traits` and use the value for contact lookup.

If the events do not contain the property specified in the above setting, then:

  * RudderStack uses the `email` property in the event.
  * If `email` is not present, RudderStack then [creates a new contact](<https://developer.mautic.org/?json#create-contact>) in Mautic.


Optionally, you can also pass the contact ID in your event’s `externalId`:
    
    
    {
      "context": {
        "externalId": [{
          "type": "mauticContactId",
          "id": "1hKOmRA4GRlm"
        }]
      }
    }
    

> ![info](/docs/images/info.svg)
> 
> RudderStack checks if `externalId.type` is set to `mauticContactId` before using the `id` field for contact lookup.

> ![warning](/docs/images/warning.svg)
> 
> The contact ID passed in your event’s `externalId` takes precedence over the user property specified in the **Mautic property name to used as lookup field** dashboard setting.

## Group

You can use the [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call to link or delink a Mautic contact with a segment, campaign, or a company.

A sample `group` call is shown below:
    
    
    rudderanalytics.group("group01", {
      "name": "Alex Keener",
      "type": "Segments",
      "operation": "add"
    });
    

RudderStack uses the `type` trait present in the `group` call to link or delink a Mautic user to a segment, campaign, or company. You can add or remove a user to a group using the `operation` trait. If this field is not explicitly set, RudderStack sets it to `add` by default.

The following table lists the supported `group` traits:

RudderStack property| Presence| Notes  
---|---|---  
`traits.type`| Required| You can set it to `Segments`, `Campaigns`, or `Companies`.  
`traits.operation`| Optional| If not set, RudderStack sets it to `add` by default.  
  
Similar to the `identify` call above, RudderStack retrieves the contact ID from the `group` call in the following order of precedence:

  1. If `externalId` is present, RudderStack checks if the `type` is set to `mauticContactId`. If yes, it uses the `id` field for the contact lookup.
  2. If you have specified a unique user property in the **Mautic property name to used as lookup field** dashboard setting, RudderStack will look for this property in the event’s `traits` or `context.traits` and use it for the contact lookup.
  3. If the events do not contain the property specified in the above setting, then:
     * RudderStack uses the `email` property in the event.
     * If `email` is not present, RudderStack then gives an error.


### Supported mappings

The following table lists the mappings between the RudderStack and Mautic properties:

  * [Assigning a single contact to a segment](<https://developer.mautic.org/?json#add-contact-to-a-segment>)

RudderStack property| Mautic property  
---|---  
`groupId`  
`traits.groupId`  
Required| `SegmentId`  
`traits.email`  
`context.traits.email`  
Required, if `externalId` and `lookupField` are absent.| `email`  
`message.context.externalId[x].id` for type `mauticContactId`| `CONTACT_ID`  
  
  * [Assigning a contact to a campaign](<https://developer.mautic.org/?json#add-contact-to-a-campaign>)

RudderStack property| Mautic property  
---|---  
`groupId`  
`traits.groupId`  
Required| `CampaignId`  
`traits.email`  
`context.traits.email`  
Required, if `externalId` and `lookupField` are absent.| `email`  
`message.context.externalId[x].id` for type `mauticContactId`| `CONTACT_ID`  
  
  * [Assigning a contact to a company](<https://developer.mautic.org/?json#add-contact-to-a-company>)

RudderStack property| Mautic property  
---|---  
`groupId`  
`traits.groupId`  
Required| `company_id`  
`traits.email`  
`context.traits.email`  
Required, if `externalId` and `lookupField` are absent.| `email`  
`message.context.externalId[x].id` for type `mauticContactId`| `CONTACT_ID`