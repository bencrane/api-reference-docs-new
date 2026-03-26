# Violation Management

Learn about the different tracking plan violation types.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __2 minute read

  * 


This guide walks you through the different tracking plan violation types in detail. You can use this information to avoid any tracking plan violations in the future by:

  * Updating your tracking plan configuration
  * Fixing your event instrumentation to comply with the tracking plan rules


## Violation types

Violation type| Description  
---|---  
`Unplanned-Event`| Event is not defined in the tracking plan.  
`Required-Missing`| Properties defined as **Required** are missing in the event.  
`Datatype-Mismatch`| Data type of the event property does not match the **Property Type** defined in the tracking plan.  
`Additional-Properties`| Occurs if:  
  


  * **Additional Properties** field in the tracking plan is set to `False`.
  * New event properties are received that are not defined in the tracking plan.

  
`Unknown-Violation`| Any other violation.  
  
## Sample violations object
    
    
    {
      "violationErrors": [{
          "message": "must have required property 'apiPath'",
          "meta": {
            "instancePath": "/properties",
            "schemaPath": "#/properties/properties/required"
          },
          "type": "Required-Missing"
        },
        {
          "message": "must have required property 'ipAddress'",
          "meta": {
            "instancePath": "/properties",
            "schemaPath": "#/properties/properties/required"
          },
          "type": "Required-Missing"
        },
        {
          "message": "must NOT have additional properties 'val'",
          "meta": {
            "instancePath": "/properties",
            "schemaPath": "#/properties/properties/additionalProperties"
          },
          "type": "Additional-Properties"
        },
        {
          "message": "no schema for event: Demo Track - New",
          "meta": {},
          "type": "Unplanned-Event"
        },
        {
          "message": "must be string",
          "meta": {
            "instancePath": "/properties/userId",
            "schemaPath": "#/properties/properties/properties/userId/type"
          },
          "type": "Datatype-Mismatch"
        }
      ]
    },
    

## FAQ

#### Does RudderStack propagate the context related to any tracking plan violations?

RudderStack propagates any context related to the tracking plan violations to your destinations.

You can use this context in your [transformations](<https://www.rudderstack.com/docs/transformations/overview/>) for filtering or modifying the events before they reach the destination.