# Iterable Cloud Mode Integration

Send events to Iterable using RudderStack cloud mode.

* * *

  * __5 minute read

  * 


RudderStack lets you send your event data to Iterable via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/iterable>).

> ![info](/docs/images/info.svg)
> 
> RudderStack batches the events together before sending them to Iterable. This reduces the number of API calls and enables faster event delivery.

## Identify

When you make an `identify` call, RudderStack calls Iterable’s [Update User](<https://api.iterable.com/api/docs#users_updateUser>) API to send the data.

Note that:

  * Iterable identifies a user by `email` or `userId` — it gives precedence to `email` over `userId` in case both are present in the `identify` call.
  * If both `email` and `userId` are absent, RudderStack will **not** send the event to Iterable.


A sample `identify` call is as shown:
    
    
    rudderanalytics.identify(
      "userId",
      {
        city: "New Orleans",
        name: "Alex Keener",
        email: "alex@example.com",
        country: "USA"
      }
    );
    

### Deleting a user

You can delete a user in Iterable using the [Suppression with Delete regulation](<https://www.rudderstack.com/docs/api/user-suppression-api/#adding-a-suppression-with-delete-regulation>) of RudderStack’s [User Suppression API](<https://www.rudderstack.com/docs/api/user-suppression-api/>).

For more information on deleting users in Iterable, see [Iterable’s API documentation](<https://api.iterable.com/api/docs#users_delete>).

To delete a user, you must specify their `userId` in the event.

> ![info](/docs/images/info.svg)
> 
> RudderStack uses the [Iterable API key](<https://www.rudderstack.com/docs/destinations/streaming-destinations/iterable/setting-up-iterable/#connection-settings>) for deleting users.

A sample regulation request body for deleting a user in Iterable:
    
    
    {
      "regulationType": "suppress_with_delete",
      "destinationIds": [
        "2FIKkByqn37FhzczP23eZmURciA"
      ],
      "users": [{
          "userId": "1hKOmRA4GRlm",
        }
      ],
    }
    

### Push notification registration

RudderStack uses Iterable’s [device registration API](<https://api.iterable.com/api/docs#users_registerDeviceToken>) to send the token information from a device. It also sets the `platform` parameter to `APNS` and `GCM` for iOS and Android devices respectively.

Similarly, RudderStack uses Iterable’s [browser token registration API](<https://api.iterable.com/api/docs#users_registerBrowserToken>) for the web platform.

If the `deviceToken` associated with the push notification is present in `context` of the event payload, then RudderStack will map the user with the device to register for push. This will add the data if it doesn’t exist yet. It will also update data fields on the device.

See the following Iterable documentation references for more information on their push notification registration feature for mobile devices:

  * [Android](<https://support.iterable.com/hc/en-us/articles/115000331943#_2-create-a-mobile-app-in-iterable>)
  * [iOS](<https://support.iterable.com/hc/en-us/articles/115000315806#_4-create-a-mobile-app-in-iterable>)


## Page

When you call the `page` method, the RudderStack sends a `track` event to Iterable with the `userId`, `email`, and `eventName` parameters. If the user does not already exist in Iterable, RudderStack will add them to the system as long as `email` is present in the event. If `email` is not present, Iterable will reject the event.

> ![info](/docs/images/info.svg)
> 
> Iterable requires `email` for the first time you call `page` for a given user. The subsequent events can contain `userId`.

For example, if the name of your page is `Application Home`, then RudderStack sends the event to Iterable as `Application Home Page`.

> ![warning](/docs/images/warning.svg)
> 
> The event name will differ according to the settings you specify in the RudderStack dashboard. Refer to the [Connection settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/iterable/setting-up-iterable/#other-settings>) section above for more information.

A sample `page` call is shown below:
    
    
    rudderanalytics.page({
      path: "home",
      url: "https://www.example.com/home",
      title: "Home Page",
      search: "home",
      referrer: "https://www.example.com/previous",
    })
    

## Screen

The `screen` event is the mobile equivalent of the `page`. When you make a `screen` call, RudderStack sends a `track` event to Iterable with the `userId`,`email`, and `eventName` parameters . If a user corresponding to the email ID is absent, Iterable will create a new user.

If the name of your screen is `Main Activity`, RudderStack sends the event to Iterable as `Main Activity Screen`.

> ![warning](/docs/images/warning.svg)
> 
> The event name will differ according to the settings you specify in the RudderStack dashboard. Refer to the [Connection settings](<https://www.rudderstack.com/docs/destinations/streaming-destinations/iterable/setting-up-iterable/#other-settings>) section above for more information.

A sample `screen` call is as shown:
    
    
    [[RSClient sharedInstance] screen:@"Main"];
    

## Alias

The `alias` call lets you merge different identities of a known user. The format of an `alias` call is shown below:
    
    
    rudderanalytics.alias("userId","previousId");
    

To send an `alias` event to Iterable, you must set `previousId` to the current email and `userId` as new email:
    
    
    rudderanalytics.alias("new@email.com", "current@email.com");
    

## Track

When you make a `track` call, RudderStack uses Iterable’s [Track API](<https://api.iterable.com/api/docs#events_track>) to send the events. The event properties are sent as data fields in the request, while the name of the event is sent as a custom event.

> ![warning](/docs/images/warning.svg)
> 
> Iterable requires `email` for the first time you send a `track` event for a given user. If a user does not exist, Iterable creates new users for those `track` calls which have `email`.

A sample`track` call is shown below:
    
    
    rudderanalytics.track(
      "Email Opened", {
        "subject": "Resume validation",
        "sendtime": "2022-01-01",
        "sendlocation": "alex@example.com"
      }, {
        traits: {
          email: "alex@example.com"
        }
      }
    );
    

## Ecommerce

You can find the relevant details of the ecommerce events in the [Ecommerce Events Specification](<https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/>).

### Order Completed

RudderStack supports the ecommerce event `Order Completed` and sends the other events as generic `track` events. Refer to the corresponding Iterable endpoint details in the [Track a purchase API](<https://api.iterable.com/api/docs#commerce_trackPurchase>).

> ![info](/docs/images/info.svg)
> 
> RudderStack requires the user properties, item properties, and `total` to successfully send the **Order Completed** event.

The following snippet highlights a sample `Order Completed` event:
    
    
    rudderanalytics.track("Order Completed", {
      total: 1000,
      products: [
        {
          product_id: "507f1f77bcf86cd799439011",
          sku: "45790-32",
          name: "Monopoly: 3rd Edition",
          price: "19",
          position: "1",
          category: "Games,Gifts,Entertainment,Toys",
          url: "https://www.example.com/product/path",
          image_url: "https://www.example.com/product/path.jpg",
        },
        {
          product_id: "507f1f77bcf86cd799439011",
          sku: "45790-32",
          name: "Monopoly: 3rd Edition",
          price: "19",
          quantity: "2",
          position: "1",
          category: "Games,Gifts,Entertainment,Toys",
          url: "https://www.example.com/product/path",
          image_url: "https://www.example.com/product/path.jpg",
        },
      ],
    })
    

### Product Added / Product Removed

RudderStack supports the ecommerce event `Product Added` or `Product Removed` and sends the information to Iterable via the [updateCart endpoint](<https://api.iterable.com/api/docs#commerce_updateCart>), corresponding to updating a user’s shopping cart items.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack requires the user and item properties to successfully send the **Product Added** and **Product Removed** events to Iterable. Also, you must send the whole updated cart details and not just the updated individual items added/removed from the cart.

A sample snippet highlighting the `Product Added` event is shown below:
    
    
    rudderanalytics.track("Product Added", {
      total: 1000,
      products: [
        {
          product_id: "507f1f77bcf86cd799439011",
          sku: "45790-32",
          name: "Monopoly: 3rd Edition",
          price: "19",
          position: "1",
          category: "Games,Gifts,Entertainment,Toys",
          url: "https://www.example.com/product/path",
          image_url: "https://www.example.com/product/path.jpg",
        },
        {
          product_id: "507f1f77bcf86cd799439011",
          sku: "45790-32",
          name: "Monopoly: 3rd Edition",
          price: "19",
          quantity: "2",
          position: "1",
          category: "Games,Gifts,Entertainment,Toys",
          url: "https://www.example.com/product/path",
          image_url: "https://www.example.com/product/path.jpg",
        },
      ],
    })