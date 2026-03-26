# Dynamic Yield

Send your event data from RudderStack to Dynamic Yield.

* * *

  * __3 minute read

  * 


[Dynamic Yield](<https://www.dynamicyield.com/>) is a personalization platform that lets you deliver personalized digital customer experiences. It lets you tailor content, products, and offers based on customer preferences.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/develop/src/cdk/v2/destinations/dynamic_yield>).

## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **Dynamic Yield**.
  2. Connect your source and click **Continue**.


### Connection settings

Configure the following settings to set up Dynamic Yield as a destination in RudderStack:

  * **Name** : Assign a name to uniquely identify the destination.
  * **API Key** : Enter your Dynamic Yield API key by logging in to your [Dynamic Yield dashboard](<https://adm.dynamicyield.com/users/sign_in>) and going to **Settings** > **API Keys**.


### Connection mode

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Dynamic Yield** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
### Configuration settings

After completing the initial setup, configure the following settings to receive your data in Dynamic Yield correctly:

  * **Hash Email** : If turned on, RudderStack hashes the email present in the `identify` call before sending it to Dynamic Yield.


> ![warning](/docs/images/warning.svg)
> 
> If your emails are already hash-encrypted, turning off this setting is recommended.

  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to identify known/unknown users in Dynamic Yield.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("user112", {
      email: "alex@example.com"
    }, {
      context: {
        sessionId: "16733896350494",
        ip: "54.100.200.255"
      }
    })
    

### Traits mapping

RudderStack maps the following event traits to the Dynamic Yield properties:

RudderStack trait| Dynamic Yield property  
---|---  
`userId`  
`anonymousId`  
Required| `user.id`  
`events[].properties.cuid`  
`session_id`  
`context.sessionId`  
Required| `session.custom`  
`traits.email`  
`context.traits.email`| `hashedEmail`  
  
## Track

You can use the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call for recording ecommerce and custom events in Dynamic Yield.

See the [Dynamic Yield documentation](<https://support.dynamicyield.com/hc/en-us/articles/4414379007633-Reporting-Events#h_01H05PX76HZDAW3W5Y6SB51NR9>) for a list of predefined events.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      order_id: "1234",
      currency: "USD",
      products: [{
        product_id: "345676543",
        price: 17.99,
        quantity: 20
      }, ],
    }, {
      context: {
        traits: {
          userId: "user123"
        },
        sessionId: "16733896350494",
      }
    })
    

## Supported mappings

RudderStack maps the following [ecommerce events](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>) from RudderStack to Dynamic Yield:

RudderStack event| Dynamic Yield event  
---|---  
`Product Added`| `Add to Cart`  
`Product Removed`| `Remove from Cart`  
`Product Added to Wishlist`| `Add to Wishlist`  
`Order Completed`| `Purchase`  
  
For the above events, RudderStack maps the following properties to the Dynamic Yield properties:

RudderStack property| Dynamic Yield property  
---|---  
`properties.value`  
`properties.revenue`  
`properties.price`  
`properties.products[].value`  
`properties.products[].revenue`  
`properties.products[].price`  
Required| `events[i].properties.value`  
`properties.sku`  
`properties.products[].sku`  
`properties.product_id`  
`properties.products[].product_id`  
Required| `events[].properties.productId`  
`events[].properties.cart[].productId`  
`properties.quantity`  
`properties.products[i].quantity`  
Required| `events[].properties.quantity`  
`events[].properties.cart[].quantity`  
`properties.products[].price`  
Required| `events[].properties.cart[].itemPrice`  
`context.traits.userId`  
Required| `user.id`  
`context.sessionId`  
Required| `session.custom`  
`properties.order_id`| `events[].properties.uniqueTransactionId`  
`properties.currency`| `events[i].properties.currency`  
  
> ![info](/docs/images/info.svg)
> 
> RudderStack considers any other event apart from the ones mentioned above as a custom event and sends it to Dynamic Yield, along with **all** the associated properties.

## Send experiments/campaigns related data

To capture the experiments/campaigns-related data rendered by Dynamic Yield and send it to other tools via RudderStack, use any of the following ways depending on your Dynamic Yield implementation:

  * For client-side rendered experiments (loaded via the Dynamic Yield tags), use one of the Dynamic Yield API methods:
    * `DYO.getRenderedObjectsOnPage()`: Gets a list of campaigns rendered on the page.
    * `DYO.getUserObjectsAndVariations()`: Gets a list of campaigns executed on the page.

[![ActiveCampaign hybrid mode connection setting](/docs/images/event-stream-destinations/dy-experiment.webp)](</docs/images/event-stream-destinations/dy-experiment.webp>)

  * For server-side rendered experiments rendered via the Dynamic Yield choose variations API, the chosen variation’s information is available in the API response.


Once done, you can send the returned experiment/variation data via RudderStack to other tools using a `track` call.