# Setup Guide

Send your event data from RudderStack to LaunchDarkly Segments.

* * *

  * __2 minute read

  * 


This guide will help you set up LaunchDarkly Segments as a destination in RudderStack when connecting to a [Reverse ETL source](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/launchdarkly-segments/connect-retl-source/>).

> ![info](/docs/images/info.svg)
> 
> This guide assumes you have already set up a [Reverse ETL source](<https://www.rudderstack.com/docs/sources/reverse-etl/>) in RudderStack.

## Setup

In your [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Directory** > **Destinations** > **Cloud Destinations** and search for **LaunchDarkly Segments**.

### Connection settings

To successfully configure LaunchDarkly Segments as a destination, you need to configure the following settings:

  * **Name** : Specify a unique name to identify the destination in RudderStack.
  * **Access Token** : Enter the LaunchDarkly access token that RudderStack uses to sync the data.


> ![warning](/docs/images/warning.svg)
> 
> Make sure the access token has write access. See [LaunchDarkly documentation](<https://docs.launchdarkly.com/home/account-security/api-access-tokens#creating-api-access-tokens>) for more information on creating access tokens.

  * **Client Side ID** : Enter the client-side ID for your LaunchDarkly project and environment. See FAQ for more information on obtaining this ID.
  * **Audience ID** : Enter the Audience ID that you want to sync. RudderStack uses this ID to create or update a segment (or audience/cohort) in LaunchDarkly.
  * **Audience Name** : Enter the name of the audience that you want to sync.


### Destination settings

  * **Audience Type** : Enter the audience type. RudderStack maps this field to LaunchDarkly’s [context kind](<https://docs.launchdarkly.com/home/contexts/context-kinds>). If not specified, LaunchDarkly sets this field to `user` by default.


## `audienceList` event structure

The following code snippet shows a sample `audienceList` call made to LaunchDarkly:
    
    
    {
      "type": "audiencelist",
      "properties": {
        "listData": {
          "add": [{
            "id": "user-1234"
          }],
          "remove": [{
            "id": "user-5678"
          }]
        }
      }
    }
    

### Property mappings

RudderStack maps the following properties to specific LaunchDarkly fields:

RudderStack property| LaunchDarkly property  
---|---  
`audienceId`  
From RudderStack dashboard| `cohortId`  
`audienceName`  
From RudderStack dashboard| `cohortName`  
`audienceType`  
From RudderStack dashboard| `contextKind`  
`clientsideId`  
From RudderStack dashboard| `environmentId`  
Identifier  
Selected while setting the mappings ([**Choose identifier**](<https://www.rudderstack.com/docs/destinations/reverse-etl-destinations/launchdarkly-segments/connect-retl-source/#set-up-the-connection>) setting)| `userId`  
`add` or `remove` list| `batch`  
  
## FAQ

#### Where can I find the LaunchDarkly Client-side ID?

  1. Log in to your [LaunchDarkly dashboard](<https://app.launchdarkly.com/>).
  2. Select your project:

[![LaunchDarkly projects](/docs/images/event-stream-destinations/launchdarkly-projects.webp)](</docs/images/event-stream-destinations/launchdarkly-projects.webp>)

  3. Navigate to **Account settings** > **Projects**.
  4. You will see the client-side ID for your project here.

[![LaunchDarkly client-side ID](/docs/images/event-stream-destinations/launchdarkly-clientsideID.webp)](</docs/images/event-stream-destinations/launchdarkly-clientsideID.webp>)