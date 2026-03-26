# Group

Get started with the RudderStack Group API call.

* * *

  * __3 minute read

  * 


The `group` call lets you link an identified user with a group like a company, organization, or an account. You can also record any custom traits associated with that group like the company name, number of employees, etc.

> ![info](/docs/images/info.svg)
> 
> An identified user can be linked to multiple groups.

## Sample payload

Here is a sample payload for the `group` event after removing the [Common fields](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/>):
    
    
    {
      "type": "group",
      "groupId": "5e8a78ba9d32d3b1898a6247",
      "traits": {
        "name": "Hooli",
        "industry": "Technology",
        "employees": 4500,
        "plan": "basic"
      }
    }
    

The corresponding event that generates the above payload via the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) is:
    
    
    rudderanalytics.group("5e8a78ba9d32d3b1898a6247", {
      name: "Hooli",
      industry: "Technology",
      employees: 4500,
      plan: "basic"
    })
    

## Group fields

The `group` call has the following fields in addition to the [Common fields](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/>):

**Field**| **Type**| **Presence**| **Description**  
---|---|---|---  
`groupId`| String| Required| Your group’s unique identifier which lets you identify the group in your database.  
`traits`| Object| Optional| Includes the traits of the group such as `name`, `email`, `employees`, etc. For more more information, check the Traits section below.  
  
> ![warning](/docs/images/warning.svg)
> 
> The field names can change slightly depending on the SDK. However, the functionality remains the same.
> 
> See the [SDK-specific documentation](<https://www.rudderstack.com/docs/sources/event-streams/sdks/>) for the implementation specifics and details on the above fields.

> ![success](/docs/images/tick.svg)
> 
> Identity data (user traits) will be automatically added to `group` calls from the most recent `identify` call, so you do not need to add it manually. This information will be included in a `traits` object in the `context` fields of the payload. Note that `group` calls also automatically handle `anonymousId` values associated with the user.
> 
> See our [Identify](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) doc for more details.

## Traits

Traits are additional information included in a `group` call that adds more context to the group. Some example of traits include the number of employees, name of the industry, or the website of the group.

RudderStack has some reserved traits that it handles in special ways. These are listed in the table below:

**Trait**| **Type**| **Description**  
---|---|---  
`id`| String| Fallback parameter used only for mapping data **if** `groupId` is not available in the event payload.  
`name`| String| The group name  
`email`| String| The group's email address  
`phone`| String| Phone number associated with the group  
`address`| Object| The group's street address. This can optionally contain any or all of the following fields:

  * `city`
  * `country`
  * `postalCode`
  * `state`
  * `street`

  
`industry`| String| The name of the industry that the group is a part of  
`createdAt`| Date| Date of the group's account creation. We recommend using the **ISO-8601** date string format.  
`description`| String| The group's description  
`employees`| String| Number of the employees in the group. This is typically used for companies.  
`plan`| String| The plan that the group is subscribed to  
`website`| String| The group's website  
`avatar`| String| URL of the group's avatar image  
  
> ![success](/docs/images/tick.svg)
> 
> Different destinations recognize some of the above data points differently.
> 
> With RudderStack, you don’t have to worry about these inconsistencies across destinations. Our open source destination transformer code handles these destination-specific conversions automatically.