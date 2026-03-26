# Sendinblue Web Device Mode Integration

Send events to Sendinblue using RudderStack web device mode.

* * *

  * __3 minute read

  * 


RudderStack lets you send your event data to Sendinblue via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>) using the native web SDK.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/Sendinblue>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to identify the users who visited your website. You can also use it to trigger a workflow in Sendinblue, for example, adding all identified contacts to a list.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4el9", {
      email: "alex@example.com",
      firstName: "Alex",
      lastName: "Keener",
      phone: "+12025550146",
      payment: 2,
      age: 21,
      location: "USA",
    });
    

> ![info](/docs/images/info.svg)
> 
> The Sendinblue tracker writes the `sib_cuid` cookie on your domain to track the user activity. As a result, you can create only one contact per session in Sendinblue using the `identify` call and update the same contact in that session. To create a new contact, you must clear the `sib_cuid` cookie first or use a different browser.

### Supported mappings

The following table details the property mappings between RudderStack and Sendinblue:

RudderStack property| Sendinblue property| Data type  
---|---|---  
`context.traits.email`  
`context.traits.Email`  
`context.traits.E-mail`  
Required| `email`| String  
`context.traits`| `properties`| Object  
`context.traits.firstName`  
`context.traits.firstname`  
`context.traits.first_name`| `properties.FIRSTNAME`| String  
`context.traits.lastName`  
`context.traits.lastname`  
`context.traits.last_name`| `properties.LASTNAME`| String  
`context.traits.phone`  
`context.traits.Phone`| `properties.SMS`| String (valid mobile number  
with country code)  
  
## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call to capture user events along with their associated properties.

A sample `track` call is as shown below:
    
    
    rudderanalytics.track(
      "Order Delivered", {
        orderId: "123",
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
      }, {
        integrations: {
          All: true,
          sendinblue: {
            propertiesIdKey: "orderId",
          },
        },
      }
    );
    }
    

### Supported mappings

The following table details the property mappings between RudderStack and Sendinblue:

RudderStack property| Sendinblue property| Data type  
---|---|---  
`event`  
Required| `event`| String  
`context.traits`| `properties`| Object  
`context.traits.firstName`  
`context.traits.firstname`  
`context.traits.first_name`| `properties.FIRSTNAME`| String  
`context.traits.lastName`  
`context.traits.lastname`  
`context.traits.last_name`| `properties.LASTNAME`| String  
`context.traits.phone`  
`context.traits.Phone`| `properties.SMS`| String  
`properties`| `event.data`| Object  
Value of `integrations.sendinblue.propertiesIdKey` in `properties`  
OR  
`messageId`| `event.id`| String  
  
> ![info](/docs/images/info.svg)
> 
> You can also send the user traits to Sendinblue via the `track` call by enabling the **Send user traits in track call** setting in the RudderStack dashboard.

## Contact attributes

> ![info](/docs/images/info.svg)
> 
> This section is applicable for the `identify` and `track` calls.

Sendinblue provides various [contact attributes](<https://help.sendinblue.com/hc/en-us/articles/209499605-What-are-the-different-types-of-contact-attributes->) which you can use to personalize your communication with your contacts. You can find them in the [Contact Attributes](<https://my.sendinblue.com/lists/add-attributes>) section in the Sendinblue dashboard where `FIRSTNAME`, `LASTNAME`, and `SMS` are the default contact attributes.

You can also map the traits in RudderStack’s payload to Sendinblue’s contact attributes using the **Map your traits to Sendinblue contact attributes** setting in the RudderStack dashboard.

If a contact attribute is **not** present in Sendinblue but you send it in the `identify` call’s traits, it can be used only in the [Automation app](<https://automation.sendinblue.com/>) unless you [add them as contact attributes](<https://my.sendinblue.com/lists/add-attributes>).

For example, the following sample code will create (or update) the user `alex@example.com` with firstname `Alex` and lastname `Keener`, and create three properties (`payment`, `age`, and `location`) that can be used only in the Marketing Automation workflows unless you also add them as your contact attributes.
    
    
    rudderanalytics.identify("1hKOmRA4el9", {
      email: "alex@example.com",
      firstName: "Alex",
      lastName: "Keener",
      payment: 2,
      age: 21,
      location: "USA",
    });
    

## Page

You can use the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call to send any page-related information to Sendinblue.

A sample `page` call is shown below:
    
    
    rudderanalytics.page("Home")
    

### Supported mappings

The following table details the property mappings between RudderStack and Sendinblue:

RudderStack property| Sendinblue property| Data type  
---|---|---  
`name`| `page_name`| String  
`properties`| `properties`| Object  
`properties.url`  
`context.page.url`| `ma_url`| String  
`properties.path`  
`context.page.path`| `ma_path`| String  
`properties.title`  
`context.page.title`| `ma_title`| String  
`properties.referrer`  
`context.page.referrer`| `ma_referrer`| String