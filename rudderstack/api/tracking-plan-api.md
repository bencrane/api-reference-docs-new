# RudderStack Tracking Plan API Deprecated

Use the RudderStack Tracking Plan API to programmatically manage your Tracking Plans.

* * *

  * __3 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> This API is deprecated. See [Data Catalog API](<https://www.rudderstack.com/docs/api/data-catalog-api/>) to create and manage your Tracking Plans programmatically.

The [Tracking plan API](<https://documenter.getpostman.com/view/16242548/TzeWFT6D#7df289e7-8758-4ec0-a86e-3aa08bd3260e>) lets you programmatically create and manage your [Tracking Plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>). You can use the API to:

  * Create/update/fetch Tracking Plans associated with your workspace
  * Define Tracking Plan rules
  * Create/update Tracking Plan configurations for a particular source
  * Link and unlink a source/events to a Tracking Plan
  * Delete a Tracking Plan


## Prerequisites

  * Set up a source-destination connection in RudderStack. See the [Quickstart](<https://www.rudderstack.com/docs/data-pipelines/event-stream/quickstart/>) guide for detailed steps.
  * Generate a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#generate-service-access-token>) in the RudderStack dashboard with **Admin** permissions to authenticate the API.

[![workspace-level Service Access Token with Admin permission](/docs/images/access-management/permissions/legacy/viewer.webp)](</docs/images/access-management/permissions/legacy/viewer.webp>)

## API authorization

The Tracking Plan API uses **Basic Authentication** for authenticating all requests.

If you’re using Postman, authenticate the API by including an empty string (`""`) as the username and your workspace-level Service Access Token as the password in the **Authorization** tab.

You can also pass your Service Access Token in the authorization header directly:
    
    
    Authorization: Basic {Base64Encoded(:<SERVICE_ACCESS_TOKEN>)}
    

An example is shown below:

  * Username: `""` (empty string)
  * Service Access Token: `<SERVICE_ACCESS_TOKEN>`
  * Header: `Basic {Base64Encoded(:<SERVICE_ACCESS_TOKEN>)}`


> ![tip](/docs/images/tip.svg)
> 
> **Tip:** Verify that the Service Access Token is valid if you get an **Invalid Authorization Header** error.

## Base URL

Use the base URL for your API requests depending on your region:
    
    
    https://api.rudderstack.com
    
    
    
    https://api.eu.rudderstack.com
    

## Tracking plan API usage

Tracking plan API| Description  
---|---  
[Tracking Plans](<https://documenter.getpostman.com/view/16242548/TzeWFT6D#2a5b999c-b417-4622-ad13-d212e4e211d1>)| This section contains all the requests and the examples related to:  
  


  * Creating a Tracking Plan
  * Fetching a single or all Tracking Plans
  * Updating a Tracking Plan
  * Upserting a Tracking Plan
  * Deleting a Tracking Plan

  
[Tracking Plan Rules](<https://documenter.getpostman.com/view/16242548/TzeWFT6D#dfa3156f-216f-4399-bd5d-c57e077ba406>)| This section contains all the requests and the examples related to setting the Tracking Plan rules like:  
  


  * Creating events
  * Fetching all events
  * Fetching all events linked to a Tracking Plan
  * Updating events by ID
  * Linking or unlinking events from a Tracking Plan
  * Deleting events

It also contains upsert and deletion requests for all non-track rules (applicable for `identify`, `group`, `page`, and `screen` events) like:  
  


  * Creating or updating a non-track rule for a Tracking Plan
  * Deleting a non-track rule mapped to a Tracking Plan

  
[Source Tracking Plan Connections](<https://documenter.getpostman.com/view/16242548/TzeWFT6D#4b74ffd2-de44-43c9-b2a4-2d65e4fb61c9>)| This section contains all the requests and the examples related to Tracking Plan configurations like:  
  


  * Creating or updating Tracking Plan configurations for a source ID
  * Fetching all Tracking Plan configurations by source ID
  * Fetching all sources connected to a Tracking Plan
  * Linking or unlinking a source to a Tracking Plan

  
  
### Event structure

To perform the Tracking Plan validation successfully, your event payload structure must conform to the standard [RudderStack event spec](<https://www.rudderstack.com/docs/event-spec/standard-events/>).

See the following sample event payloads for more information:

  * [Identify](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/#sample-payload>)
  * [Page](<https://www.rudderstack.com/docs/event-spec/standard-events/page/#sample-payload>)
  * [Screen](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/#sample-payload>)
  * [Track](<https://www.rudderstack.com/docs/event-spec/standard-events/track/#sample-payload>)
  * [Group](<https://www.rudderstack.com/docs/event-spec/standard-events/group/#sample-payload>)


You can also see the example request in the [Create Tracking Plan API](<https://documenter.getpostman.com/view/16242548/TzeWFT6D#7eec6c80-64e8-444d-bbe4-bd63fb1d886a>) for the event formatting structure.