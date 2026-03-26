# Screen

Get started with the RudderStack Screen API call.

* * *

  * __less than a minute

  * 


The `screen` call lets you record whenever your user views their mobile screen, with any additional relevant information about the screen.

> ![success](/docs/images/tick.svg)
> 
> The `screen` call is the mobile equivalent of the [page](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call.

## Sample payload

A sample payload of a `screen` event after removing most of the [Common fields](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/>) is shown below:
    
    
    {
      "type": "screen",
      "name": "Main",
      "properties": {
        "title": "Home | RudderStack"
      }
    }
    

The corresponding `screen` call that generates the above payload via the [iOS (Obj-C) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>) is as follows:
    
    
    [[RSClient sharedInstance] screen:@"Main"
                    properties:@{
                      @"title" : "Home | RudderStack"}
                    ];
    

## Screen fields

The `screen` call supports the following fields in addition to the [Common fields](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/>):

Field| Type| Presence| Description  
---|---|---|---  
`name`| String| Optional| Screen name  
`properties`| Object| Optional| Properties of the screen such as the `url`, `referrer`, etc. For more more information, check the Properties section below.  
  
## Properties

Properties are additional information that describe the viewed screen.

RudderStack has reserved some standard properties listed in the table below and handles them in special ways.

Property| Type| Description  
---|---|---  
`name`| String| You can tag each screen with a `name`. This is a reserved property for future use.