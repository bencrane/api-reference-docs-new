# Accoil Analytics Cloud Mode Integration Beta

Send events to Accoil Analytics in RudderStack cloud mode.

* * *

  * __4 minute read

  * 


After you have successfully instrumented Accoil Analytics as a destination in RudderStack, follow this guide to correctly send your events to Accoil Analytics in [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/cdk/v2/destinations/accoil_analytics>).

> ![info](/docs/images/info.svg)
> 
> Accoil simplifies event tracking by aggregating daily event counts.

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to identify a user and their associated attributes.

A sample `identify` call is shown below:
    
    
    rudderanalytics.identify("1hKOmRA4GRlm", {
      email: "alex@example.com",
      name: "Alex Keener",
      createdAt: '2023-05-12T08:00:00Z' // ISO 8601 or Unix timestamp format
    });
    

#### Supported mappings

RudderStack property| Accoil property| Notes  
---|---|---  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  
Required| `userId`| -  
`traits`  
`context.traits`| Sent as is to Accoil| See Supported traits for details.  
`timestamp`  
`originalTimestamp`  
Required| `timestamp`| ISO 8601 format datetime or UNIX timestamp. This field is automatically added by RudderStack while sending the final event payload to Accoil.  
  
#### Supported traits

RudderStack trait| Notes  
---|---  
`email`  
Recommended| Used to identify users across multiple platforms.  
`name`  
Recommended| Displays the user’s name in Accoil. If no name is provided, the email address is displayed instead.  
`createdAt`  
Recommended| Signifies when was the user created. Make sure to send this field in the ISO 8601 or UNIX timestamp format for accurate tenure tracking.  
`role`  
Suggested| Describes the user’s role in your product, for example, Admin, Owner, Team Member, etc.  
`accountStatus`  
Suggested| Captures the account status of the user - it can be helpful in segmenting users. Possible options include: `Free`, `Trial`, `Paid`, and `Cancelled`.  
  
## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record the user events along with their associated properties.

A sample `track` call is shown below:
    
    
    rudderanalytics.track("Product Added", {
      item: "Book",
      name: "Archies",
      price: 25.00
    });
    

> ![warning](/docs/images/warning.svg)
> 
> Accoil only stores traits sent with `identify` and `group` events - properties passed within the `track` events are not stored. Accoil records only the event names and counts.

#### Supported mappings

RudderStack property| Accoil property| Note  
---|---|---  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  
Required| `userId`| Persisted from the previously made `identify` call.  
`event`  
Required| Event name| -  
`timestamp`  
`originalTimestamp`  
Required| `timestamp`| ISO 8601 format datetime or UNIX timestamp. This field is automatically added by RudderStack while sending the final event payload to Accoil.  
  
## Group

You can use the [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) event to link identified users to accounts and records account-level attributes.

A sample `group` call is as shown below:
    
    
    rudderanalytics.group("group123", {
      name: "MyGroup",
      industry: "IT",
      employees: 450,
      plan: "basic",
      createdAt: '2021-03-15T09:00:00Z',  // ISO 8601 or UNIX timestamp format
      mrr: 3000,
      status: 'active'
    });
    

#### Supported mappings

RudderStack property| Accoil property| Note  
---|---|---  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  
Required| `userId`| -  
`groupId`  
Required| `groupId`| -  
`traits`| Sent as is to Accoil| See Supported group traits for details.  
`timestamp`  
`originalTimestamp`  
Required| `timestamp`| ISO 8601 format datetime or UNIX timestamp. This field is automatically added by RudderStack while sending the final event payload to Accoil.  
  
#### Supported group traits

RudderStack trait| Note  
---|---  
`name`  
Recommended| The account name. Without a name, accounts are displayed using a numeric ID, making them harder to identify.  
`createdAt`  
Recommended| Helps calculate the account’s tenure. If no `createdAt` is provided, the earliest `createdAt` from the associated users is used.  
  
**Note** : Make sure to send this field in the ISO 8601 or UNIX timestamp format for accurate tenure tracking.  
`status`  
Recommended| The status of the account subscription. Possible options include: `Free`, `Trial`, `Paid`, `Cancelled`  
`plan`  
Recommended| The plan type helps in segmenting accounts by their subscription tier (for example, starter, pro, enterprise).  
`mrr`  
Recommended| Monthly recurring revenue (MRR) used for segmenting accounts by value. It also allows Accoil to show the dollar value of different segments. Ideally this is passed in cents, for example, `$99` becomes `9900`.  
  
## Page

The [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call allows you to record your website’s page views, with the additional relevant information about the viewed page.

> ![info](/docs/images/info.svg)
> 
> RudderStack sends the `page` events as `track` events to Accoil for easier monitoring of user navigation.

A sample `page` call is as shown below:
    
    
    rudderanalytics.page("Cart", "Cart Viewed");
    

#### Supported mappings

RudderStack property| Accoil property| Note  
---|---|---  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  
Required| `userId`| Persisted from the previously made `identify` call.  
`name`  
Required| Name of the viewed page.| -  
`timestamp`  
`originalTimestamp`  
Required| `timestamp`| ISO 8601 format datetime or UNIX timestamp. This field is automatically added by RudderStack while sending the final event payload to Accoil.  
  
## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call lets you record your users’ mobile screen views with any additional information about the viewed screen.

> ![info](/docs/images/info.svg)
> 
> RudderStack sends the `screen` events as `track` events to Accoil for easier monitoring of user navigation.

A sample `screen` call is shown below:
    
    
    [[RSClient sharedInstance] screen:@"Main"
                    properties:@{@"category" : @"Home"}];
    

#### Supported mappings

RudderStack property| Accoil property| Note  
---|---|---  
`userId`  
`traits.userId`  
`traits.id`  
`context.traits.userId`  
`context.traits.id`  
Required| `userId`| Persisted from the previously made `identify` call.  
`name`  
Required| Name of the viewed screen.| -  
`timestamp`  
`originalTimestamp`  
Required| `timestamp`| ISO 8601 format datetime or UNIX timestamp. This field is automatically added by RudderStack while sending the final event payload to Accoil.