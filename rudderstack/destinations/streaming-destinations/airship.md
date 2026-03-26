# Airship

Send your event data from RudderStack to Airship.

* * *

  * __7 minute read

  * 


[Airship](<https://www.airship.com/>) is an app experience platform that lets you create and deliver powerful in-app experiences with the help of engaging, personalized content and actionable customer insights.

RudderStack supports Airship as a destination to which you can seamlessly send your event data.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/airship>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, React Native , Flutter, Cordova, Warehouse, Shopify
  * Refer to it as **Airship** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
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

> ![warning](/docs/images/warning.svg)
> 
> You must install the [Airship SDK](<https://docs.airship.com/guides/messaging/getting-started/developers/sdk-api/>) on your website/app to use this integration successfully. See the [Airship documentation](<https://docs.airship.com/platform/>) for more information on setting up the Airship SDK on your preferred platform.
> 
> Also, note that:
> 
>   * Before sending events to Airship through RudderStack, make sure to first create the [channel](<https://docs.airship.com/guides/messaging/getting-started/developers/channels-intro/>) and [named user](<https://docs.airship.com/guides/messaging/user-guide/audience/segmentation/named-users/>) in Airship via the Airship SDK.
>   * RudderStack supports enhancing the existing user profiles and sending custom events in cloud mode.
> 


## Setup

  1. In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Airship**.
  2. Assign a name to your destination and click **Next**.


### Connection settings

Setting| Description  
---|---  
API Key| Enter your Airship token required by RudderStack to communicate with your Airship project and authenticate all supported event calls, that is, `identify`, `track`, and `group`.  
App Key| Enter your Airship project’s app key which RudderStack requires for the `track` calls. You can obtain the app key by going to **Settings** > **Project Details** in your Airship dashboard.  
Enter timestamp attributes| Specify the timestamp attributes to send to Airship in the [Airship date time format](<https://docs.airship.com/api/ua/#date-time-format>). Note that the values for these attributes must be in UTC and should follow the [ISO 8601 format](<https://www.iso.org/iso-8601-date-and-time-format.html>).  
  
**Note** : RudderStack converts the attributes in the Airship format only if you specify them in this setting.  
EU data center| Turn on this setting if you have implemented your app in Airship’s European data center. If you’re unsure which data center you are on, reach out to [Airship support](<mailto:%20docs@rudderstack.com>).  
Consent management settings| Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/>) for more information on this feature.  
  
## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you uniquely identify a user and record any associated traits about them like their name, email, etc.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4el9Zt1WSfVJIVo4GRlm", {
      likes_movies: true,
      favorite_color: "purple",
      age: 13
    });
    

In the above code snippet, RudderStack sends the Boolean values to Airship as [tags](<https://docs.airship.com/api/ua/#operation-api-named_users-tags-post>), whereas the non-Boolean values are sent as [attributes](<https://docs.airship.com/api/ua/#operation-api-named_users-named_user_id-attributes-post>).

RudderStack maps some reserved traits to the predefined Airship attributes. See the Traits mapping section below for more information.

### Tags

To successfully assign tags to Airship using the RudderStack `identify` events, you must create a tag group with the group key set to `rudderstack_integration` in Airship.

Note that this integration supports `identify` traits of Boolean data type only. Airship adds tags for the traits that are set to `true` and removes tags for the traits set to `false`.

### Attributes

For `identify` traits that are not mapped to any predefined or custom-defined Airship attributes, you must create and enable those attributes in the Airship dashboard.

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you capture user events along with the properties associated with them.

RudderStack sends the `track` events to Airship via their [Custom Events API](<https://docs.airship.com/api/ua/#operation-api-custom-events-post>). You can use the event properties to personalize and trigger specific messages for your audience.

> ![info](/docs/images/info.svg)
> 
> You need the Airship project’s **App Key** for authenticating the `track` calls.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Product Clicked", {
      description: "Shoes viewed",
      brand: "Sneakers",
      colors: ["red", "blue"],
      items: [
        {
          text: "New Balance Sneakers",
          price: "$69.95"
        },
        {
          text: "G.I. Joe Sneakers",
          price: "$99.95"
        }
      ]
    });
    

In the above snippet, the event name `Product Clicked` is automatically converted to `product_clicked` before sending to Airship.

> ![info](/docs/images/info.svg)
> 
> The event name sent to Airship must not contain any upper case characters. Otherwise, Airship rejects it with a `400` status code.
> 
> RudderStack handles this scenario internally by converting any upper case characters to lower case and replacing any spaces with an underscore(`_`).

RudderStack also maps some event properties to the Airship properties before sending them over to Airship. See the Supported mappings section below for more information.

## Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call lets you link an identified user with a group such as a company, organization, or an account, and record any traits associated with that group, e.g., company name, number of employees, etc.

A sample `group` call is shown below:
    
    
    rudderanalytics.group("5ea6247", {
      name: "Company Inc.",
      in_tecnology_domain: true,
      plan: "basic"
    })
    

In the above code snippet, RudderStack sends the Boolean values to Airship as [tags](<https://docs.airship.com/api/ua/#operation-api-named_users-tags-post>) and the non-Boolean values as [attributes](<https://docs.airship.com/api/ua/#operation-api-named_users-named_user_id-attributes-post>).

> ![warning](/docs/images/warning.svg)
> 
> To successfully assign tags to Airship using the RudderStack `group` events, you must create a tag group with the group key set to `rudderstack_integration_group` in Airship. Similarly, you need to create the relevant attribute identifiers in Airship to set the attributes for the named users.

This integration supports `group` traits of type Boolean only. Airship adds tags for the traits that are set to `true` and removes tags for the traits set to `false`.

## Supported mappings

RudderStack maps the following event properties to the Airship properties before sending them over to Airship.

See the [Airship documentation](<https://docs.airship.com/api/ua/#operation-api-custom-events-post>) for more information on how the externally-generated custom events are mapped.

RudderStack property| Airship property  
---|---  
`userId`  
Required| `named_user_id`  
`event`  
Required| `name`  
`properties`| `properties`  
`value`| `value`  
`interactionId`| `interaction_id`  
`interactionType`| `interaction_type`  
`sessionId`| `session_id`  
  
**Note** : RudderStack transforms this field based on the [UUID v5 format](<https://www.npmjs.com/package/uuid>) using DNS as the reference namespace.  
`transaction`| `transaction`  
`timestamp`| `occurred`  
  
### Traits mapping

RudderStack trait| Airship attribute  
---|---  
`address.city`| `city`  
`address.country`| `country`  
`address.postalcode`| `zipcode`  
`address.state`| `region`  
`createdAt`| `account_creation`  
`firstName`| `first_name`  
`lastName`| `last_name`  
`name`| `full_name`  
`phone`| `mobile_phone`  
  
## Send user traits of array type

In case of the `identify` and `group` events, RudderStack supports sending user traits of string and integer types via the `traits` object, by default.

You can also send traits of array data type by including them in the event’s `integrations` object. For example, to send the below traits to Airship:
    
    
    {
      ...
      "traits": {
        ...
        "widget_notifications": [
          "widget1_clicked",
          "widget2_viewed"
        ],
        ...
      }
    }
    

Include them in the event’s `integrations` object within the `JSONAttributes` key in the `<attribute_id>#<instance_id>` format, as shown:
    
    
    {
      ...
      "integrations": {
        "All": true,
        "Airship": {
          "JSONAttributes": {
              "widget_notifications#r0123": [
                "widget1_clicked",
                "widget2_viewed"
              ]
          }
        }
      },
    }
    

RudderStack leverages Airship’s [Attributes assignment API](<https://docs.airship.com/api/ua/#schemas-attributesobject>) to send these attributes.

You can also remove any attributes by specifying them in the `integrations` object within the `removeAttributes` key, as shown:
    
    
    {
      ...,
      "integrations": {
        "All": true,
        "Airship": {
          "removeAttributes": [
            "widget_notification1",
            "widget_notification2"
          ]
        }
      },
    }
    

## FAQ

#### Where can I find the Airship API key?

RudderStack requires the Airship API key to communicate with your Airship project. This is a **mandatory** field to set up the integration.

  1. In your Airship dashboard, go to **Settings**.
  2. In the **Project configuration** window, go to **Tokens** and click **Manage**.
  3. Click **Create token**.
  4. Assign a name for your token. Under **Role** , select **All access** from the dropdown:

[![Airship project token](/docs/images/event-stream-destinations/airship-create-new-token.webp)](</docs/images/event-stream-destinations/airship-create-new-token.webp>)

  5. Once the token is created, copy and secure the credentials and click **Got it**.


#### Where can I obtain the Airship App Key?

  1. In your Airship dashboard, go to **Settings**.
  2. In the **Project configuration** window, look for the **Project Details** pane on the right side. You will find your project’s app key listed here.


#### How do I create a custom tag group in Airship?

  1. Go to **Settings** > **Project configuration** > **Tag Groups** and click **Manage**.

  2. Click **Create Tag Group** and enter the following settings:

     * **Name** : Enter the name for the tag group.
     * **Description** : Set additional information about the tag group in this field.
     * **Group Key** : Assign a unique ID for the tag group in this field. For example, to assign tags using the RudderStack `identify` events, you can set this to `rudderstack-integration`. For assigning tags using the `group` events, set this to `rudderstack-integration-group`.


See the [Airship documentation](<https://docs.airship.com/guides/messaging/user-guide/audience/segmentation/tags/#creating-custom-tag-groups>) for more information.

#### How do I create and enable attributes in Airship?

For `identify` traits that are not mapped to any predefined or custom-defined Airship attributes, you must create and enable those attributes in the Airship dashboard.

  1. Go to your Airship dashboard.
  2. Navigate to **Audience** > **Attributes**.
  3. Click **Create Attribute**.
  4. Enter the **Attribute ID** , **Name** , and select the attribute **Type**.
  5. Finally, click **Add**.

[![Airship new attributes](/docs/images/event-stream-destinations/new-attribute-airship.webp)](</docs/images/event-stream-destinations/new-attribute-airship.webp>)