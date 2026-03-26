# Sendinblue Cloud Mode Integration

Send events to Sendinblue using the RudderStack cloud mode.

* * *

  * __4 minute read

  * 


RudderStack lets you send your event data to Sendinblue via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to add a contact in Sendinblue. If a contact already exists, RudderStack updates the contact details.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify(
      "alex@example.com", {
        firstName: "Alex",
        lastName: "Keener",
        phone: "+12025550146",
        payment: 2,
        age: 21,
        location: "USA",
      }, {
        externalId: [{
            type: "sendinblueIncludeListIds",
            id: [1,2],
          },
        ],
      }
    );
    

### Supported mappings

This section explains the property mappings for `identify` call made to perform different operations on contacts such as their creation, deletion, updation, etc.

#### Create or update a contact

The following table details the property mappings between RudderStack and Sendinblue to [create or update a contact](<https://developers.sendinblue.com/reference/createcontact>):

RudderStack property| Sendinblue property| Data type  
---|---|---  
`traits.email`  
`context.traits.email`  
`properties.email`  
Required, if phone number is not present.| `email`| String  
`traits.phone`  
`context.traits.phone`  
`properties.phone`  
Required, if email is not present.| `attributes.SMS`| String  
`traits.newEmail`  
`context.traits.newEmail`| `attributes.EMAIL`| String  
`traits.firstName`  
`traits.firstname`  
`traits.first_name`  
`context.traits.firstName`  
`context.traits.firstname`  
`context.traits.first_name`| `attributes.FIRSTNAME`| String  
`traits.lastname`  
`traits.last_name`  
`context.traits.lastName`  
`context.traits.lastname`  
`context.traits.last_name`  
`traits.lastName`| `attributes.LASTNAME`| String  
`traits`  
`context.traits`| `attributes`| Object  
`integrations.sendinblue.emailBlacklisted`| `emailBlacklisted`| Boolean  
`integrations.sendinblue.smsBlacklisted`| `smsBlacklisted`| Boolean  
`context.externalId.id` _(when`context.externalId.type` = `sendinblueIncludeListIds`)_| `listIds`| Int64 Array  
  
#### Create contact via DOI (Double-opt-in) flow

The following table details the property mappings between RudderStack and Sendinblue to [create a contact via DOI flow](<https://developers.sendinblue.com/reference/createdoicontact>):

RudderStack property| Sendinblue property| Data type  
---|---|---  
`traits.email`  
`context.traits.email`  
`properties.email`  
Required| `email`| String  
`context.externalId.id` _(when`context.externalId.type` = `sendinblueIncludeListIds`)_ Required| `includeListIds`| Int64 Array  
`context.externalId.id` _(when`context.externalId.type` = `templateId`)_  
OR  
`templatedId` _(defined in RudderStack dashboard)_ Required| `templateId`| Int64 (DOI template’s ID)  
Redirection URL _(defined in RudderStack dashboard)_ Required| `redirectionUrl`| URL  
`traits.phone`  
`context.traits.phone`  
`properties.phone`| `attributes.SMS`| String  
`traits.firstName`  
`traits.firstname`  
`traits.first_name`  
`context.traits.firstName`  
`context.traits.firstname`  
`context.traits.first_name`| `attributes.FIRSTNAME`| String  
`traits.lastName`  
`traits.lastname`  
`traits.last_name`  
`context.traits.lastName`  
`context.traits.lastname`  
`context.traits.last_name`| `attributes.LASTNAME`| String  
`traits`  
`context.traits`| `attributes`| Object  
  
#### Update a DOI contact

The following table details the property mappings between RudderStack and Sendinblue to [update a DOI contact](<https://developers.sendinblue.com/reference/updatecontact>):

RudderStack property| Sendinblue property| Data type  
---|---|---  
`traits.email`  
`context.traits.email`  
`properties.email`  
`context.externalId.id` _(when`context.externalId.type` = `sendinblueContactId`)_  
Required| `identifier`| String  
`traits.phone`  
`context.traits.phone`  
`properties.phone`| `attributes.SMS`| String  
`traits.newEmail`  
`context.traits.newEmail`| `attributes.EMAIL`| String  
`traits.firstName`  
`traits.firstname`  
`traits.first_name`  
`context.traits.firstName`  
`context.traits.firstname`  
`context.traits.first_name`| `attributes.FIRSTNAME`| String  
`traits.lastName`  
`traits.lastname`  
`traits.last_name`  
`context.traits.lastName`  
`context.traits.lastname`  
`context.traits.last_name`| `attributes.LASTNAME`| String  
`traits`  
`context.traits`| `attributes`| Object  
`integrations.sendinblue.emailBlacklisted`| `emailBlacklisted`| Boolean  
`integrations.sendinblue.smsBlacklisted`| `smsBlacklisted`| Boolean  
`context.externalId.id` _(when`context.externalId.type` = `sendinblueIncludeListIds`)_| `listIds`| Int64 array  
`context.externalId.id` _(when`context.externalId.type` = `sendinblueUnlinkListIds`)_| `unlinkListIds`| Int64 array  
  
#### Delete contact from list

> ![warning](/docs/images/warning.svg)
> 
> RudderStack uses this API to delete a contact from a given list **if** the **Create contact via Double-opt-in** setting is disabled in the dashboard and `sendinblueUnlinkListIds` is provided in the event’s `externalId` field.

The following table details the property mappings between RudderStack and Sendinblue to [delete a contact from list](<https://developers.sendinblue.com/reference/removecontactfromlist>):

RudderStack property| Sendinblue property| Data type  
---|---|---  
`traits.email`  
`context.traits.email`  
`properties.email`  
`traits.phone`  
`context.traits.phone`  
`properties.phone`  
Required, if contactID is not present.| `emails`| String  
`context.externalId.id` _(when`context.externalId.type` = `sendinblueContactId`)_| `ids`| String  
  
## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to:

  * **[Track event](<https://tracker-doc.sendinblue.com/reference/trackevent-3>)** : Capture events on your website along with (optional) extra information about the event.
  * **[Track Link](<https://tracker-doc.sendinblue.com/reference/tracklink-3>)** : Capture clicks on your website along with (optional) extra information about the click.


A sample `track` call is shown below:
    
    
    // track events
    rudderanalytics.track("Card Created", {
      id: "a4123c72-c6f7-4d8e-b8cd-4abb8a807891",
      products: [{
          product_id: 1234,
          product_name: "Track Pants",
          amount: 1,
          price: 220,
        },
        {
          product_id: 5768,
          product_name: "T-Shirt",
          amount: 5,
          price: 1058,
        },
      ],
    });
    
    //track link
    rudderanalytics.track("trackLink", {
      link: "https://mail.google.com/mail/u/0/#inbox",
      subject: "Email confirmation",
    });
    

> ![info](/docs/images/info.svg)
> 
> RudderStack sends the track call to the **Track Link** endpoint if the event name is `trackLink` in the event payload. For any other event name, it sends the event to the **Track event** endpoint.

### Supported mappings

This section explains the property mappings for `track` call to capture events and links on your website.

#### Track event

The following table details the property mappings between RudderStack and Sendinblue for **Track event** endpoint:

RudderStack property| Sendinblue property| Data type  
---|---|---  
`traits.email`  
`context.traits.email`  
`properties.email`  
`traits.phone`  
`context.traits.phone`  
`properties.phone`  
Required| `email`| String  
`event`  
Required| `event`| String  
`traits`  
`context.traits`| `properties`| Object  
`properties`| `eventdata.data`| Object  
Value of `integrations.sendinblue.propertiesIdKey` in `properties`| `eventdata.id`| String  
  
#### Track Link

The following table details the property mappings between RudderStack and Sendinblue for **Track Link** endpoint:

RudderStack property| Sendinblue property| Data type  
---|---|---  
`traits.email`  
`context.traits.email`  
`properties.email`  
`traits.phone`  
`context.traits.phone`  
`properties.phone`  
Required| `email`| String  
`properties.link`  
Required| `link`| String  
`properties`| `properties`| Object  
  
## Page

You can use the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call to send any page-related information to Sendinblue.

A sample `page` call is shown below:
    
    
    rudderanalytics.page("Home")
    

### Supported mappings

The following table details the property mappings between RudderStack and Sendinblue:

RudderStack property| Sendinblue property| Data type  
---|---|---  
`traits.email`  
`context.traits.email`  
`properties.email`  
`traits.phone`  
`context.traits.phone`  
`properties.phone`  
Required| `email`| String  
`properties.url`  
`context.page.url`  
Required| `page`| String  
`properties.title`  
`context.page.title`| `properties.ma_title`| String  
`properties.path`  
`context.page.path`| `properties.ma_path`| String  
`properties.referrer`  
`context.page.referrer`| `properties.ma_referrer`| String  
`properties.name`  
`Page Viewed`| `properties.sib_name`| String  
`properties`| `properties`| Object