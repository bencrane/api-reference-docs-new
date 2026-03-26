# Braze Cloud Mode Integration

Send events to Braze in RudderStack cloud mode.

* * *

  * __5 minute read

  * 


After you have successfully instrumented Braze as a destination in RudderStack, follow this guide to correctly send your events to Braze in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/braze>).

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to identify a user in Braze in any of the below cases:

  * When the user registers to the app for the first time.
  * When they log into their app.
  * When they update their information.


A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      email: "alex@example.com",
      name: "Alex Keener"
    });
    

### Set a custom user ID (`externalId`)

You can use the `externalId` field within your `identify` event to explicitly set a custom user ID in Braze.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * Braze gives first preference to the `externalId` field in the `identify` event to identify the user. If `externalId` is absent, it falls back to the `userId` field.
>   * RudderStack recommends sending the `identify` event containing the `externalId` object before sending any subsequent `track` events, so that it can persist the `externalId` information successfully.
> 


The following snippet shows how to add an `externalId` to your `identify` event using the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>), before sending it to Braze:
    
    
    rudderanalytics.identify(
      "1hKOmRA4GRlm", {
        firstName: "Alex",
        city: "New Orleans",
        country: "USA",
        phone: "+1-202-555-0146",
        email: "alex@example.com",
        favorite_flavor: "chocolate",
        externalId: [{
          id: "12323412432432",
          type: "brazeExternalId",
        }],
      }
    );
    

### Delete a user

You can delete a user in Braze using the [Suppression with Delete regulation](<https://www.rudderstack.com/docs/api/user-suppression-api/#adding-a-suppression-with-delete-regulation>) of the RudderStack [User Suppression API](<https://www.rudderstack.com/docs/api/user-suppression-api/>).

> ![warning](/docs/images/warning.svg)
> 
> While RudderStack forwards the deletion request, it **does not guarantee** deletion within a 30-day window. You will need to check with Braze if the request is fulfilled.

To delete a user:

  * Use a [REST API key](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/setup-guide/#connection-settings>) containing the [`users.delete` permission](<https://www.braze.com/docs/api/basics#rest-api-key-permissions>) for setting up the Braze destination in RudderStack.
  * Specify the `userId` in the event. You can also specify a custom identifier (optional) in the event.


A sample regulation request body for deleting a user in Braze is shown below:
    
    
    {
      "regulationType": "suppress_with_delete",
      "destinationIds": ["2FIKkByqn37FhzczP23eZmURciA"],
      "users": [
        {
          "userId": "1hKOmRA4GRlm",
          "<customKey>": "<customValue>"
        }
      ]
    }
    

### Send user traits as nested custom attributes

You can send the user traits to Braze as [nested custom attributes](<https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/>) and perform add, update, and remove operations on them. To do so, turn on the [Use Custom Attributes Operation](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/setup-guide/#event-settings>) dashboard setting while setting up the Braze destination.

You can send the user traits as nested custom attributes in your `identify` events in the following format:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      cars: {
        add: [{
          age: 27,
          id: 1,
          name: "Alex Keener"
        }],
        update: [{
            age: 30,
            id: 2,
            identifier: "id",
            name: "Alice"
          },
          {
            age: 27,
            id: 1,
            identifier: "id",
            name: "John"
          }
        ]
      },
      pets: [{
          breed: "Golden Retriever",
          id: 1,
          name: "Scooby",
          type: "Dog"
        },
        {
          breed: "German Shepherd",
          id: 2,
          name: "Milo",
          type: "Dog"
        }
      ]
      country: "USA",
      email: "alex@example.com",
      firstName: "Alex",
      gender: "M",
      properties: {
        mergeObjectsUpdateOperation: true
      }
    });
    

To deep merge the updated custom attributes with the existing attributes, set `mergeObjectsUpdateOperation` to `true` within the event’s `properties` object, as seen above.

You can also set the user traits as custom user attributes in the `track`, `page`, or `screen` events by pass `traits` as a contextual field in the event, as shown:
    
    
    rudderanalytics.track(
      "Product Viewed", {
        revenue: 8.99,
        currency: "USD"
      }, {
        traits: {
          cars: {
            add: [{
              age: 27,
              id: 1,
              name: "Alex Keener"
            }],
            update: [{
                age: 30,
                id: 2,
                identifier: "id",
                name: "Mike"
              },
              {
                age: 27,
                id: 1,
                identifier: "id",
                name: "Rowan"
              }
            ]
          },
          city: "Disney",
          country: "USA",
          email: "alexa@example.com",
          firstName: "Alexa",
          gender: "woman",
          pets: [{
              breed: "beagle",
              id: 1,
              name: "Scooby",
              type: "dog"
            },
            {
              breed: "calico",
              id: 2,
              name: "Garfield",
              type: "cat"
            }
          ]
        }
      }
    );
    

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * `identifier` is a required key for the `update` and `remove` operations.
>   * RudderStack uses the `create` operation to create the properties if `add`, `update`, or `remove` operations are not present in the nested array.
> 


See the [Braze documentation](<https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/>) for more information on sending nested custom attributes to Braze.

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record the customer events, that is, the actions that they perform, along with any properties associated with them.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Product Added", {
      numberOfRatings: "12",
      name: "item 1"
    });
    

### Order Completed

When you call the `track` method for an `Order Completed` event, RudderStack sends the product information present in the event to Braze as **purchases**.

A sample `Order Completed` event is shown below:
    
    
    rudderanalytics.track("Order Completed", {
      userId: "1hKOmRA4GRlm",
      currency: "USD",
      products: [
        {
          product_id: "123454387",
          name: "Game",
          price: 15.99
        }
      ]
    });
    

## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call allows you to record your website’s page views, with the additional relevant information about the viewed page.

A sample `page` call is as shown below:
    
    
    rudderanalytics.page("Cart", "Cart Viewed", {
      path: "/cart",
      referrer: "test.com",
      search: "term",
      title: "test_item",
      url: "http://test.in"
    });
    

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call lets you record your users’ mobile screen views with any additional information about the viewed screen.

A sample `screen` call is shown below:
    
    
    [[RSClient sharedInstance] screen:@"Main"
                    properties:@{@"prop_key" : @"prop_value"}];
    

## Group

You can use the [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) event to link an identified user with a group, such as a company, organization, or an account.
    
    
    rudderanalytics.group("12345", {
      name: "MyGroup",
      industry: "IT",
      employees: 450,
      plan: "basic"
    });
    

Note that once you send a `group` event, RudderStack sends a custom attribute to Braze with the name as `ab_rudder_group_<groupId>` and the value as `true`.

For example, if the `groupId` is `12345`, then RudderStack creates a custom attribute with the name `ab_rudder_group_12345` and sends it to Braze with its value to `true`.

### Subscription group status

To update the subscription group status, enable the [Enable subscription groups in group call](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/setup-guide/#event-settings>) dashboard setting and send the [subscription group](<https://www.braze.com/docs/api/endpoints/subscription_groups>) status in the `group` call:
    
    
    rudderanalytics.group("12345", {
      subscriptionState: "subscribed",
      email: "alex@example.com"
    });
    

> ![warning](/docs/images/warning.svg)
> 
> Either `email` or `phone` is mandatory to send the subscription group in a `group` call.

## Alias

You can use the [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) event to merge different identities of a known user.

A sample `alias` call is shown below:
    
    
    rudderanalytics.alias("newUserId", "previousUserId");
    

When you send the above event, RudderStack removes the user with `previousUserId` from Braze and merges all the associated fields with the user having `newUserId`.

## Delta management for `identify` and `track` calls

You can save costs by deduplicating the data sent to Braze via `identify` and `track` calls. To do so, enable the [Deduplicate Traits](<https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/setup-guide/#deduplication-settings>) dashboard setting. RudderStack then sends only the changed or modified attributes (traits) to Braze.

> ![info](/docs/images/info.svg)
> 
> RudderStack recommends reviewing Braze’s [data points policy](<https://www.braze.com/docs/user_guide/onboarding_with_braze/data_points/>) to fully understand how this functionality can help you avoid data overages.