# Setup Guide

Send your event data from RudderStack to Criteo Audience.

* * *

  * __2 minute read

  * 


This guide will help you set up Criteo Audience as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Criteo Audience.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Warehouse
  * Refer to it as **Criteo Audience** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Criteo Audience, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Criteo Audience**.
  2. Assign a name to the destination and click **Continue**.


## Connection settings

To successfully configure Criteo Audience as a destination, you need to configure the following settings:

  * **Create Account** : Click **Create Account** > **Connect with Criteo Audience** and enter your login credentials for Criteo Audience.
  * **Audience Id** : Enter the audience ID for which you want to sync the data. Refer to the FAQ section for more information on obtaining the audience ID.
  * **Audience Type** : Select the audience type from the dropdown for which you want to add or remove the users. If you select `gum`, then **Gum Caller Id** is a required field. Refer to the [Criteo documentation](<https://developers.criteo.com/marketing-solutions/docs/contact-list#adding-and-removing-users-in-an-audience>) for more information on different audience types.


## `audienceList` event structure

RudderStack supports [adding and removing users in an audience list](<https://developers.criteo.com/marketing-solutions/docs/contact-list#adding-and-removing-users-in-an-audience>).

The following code snippet shows a sample `audienceList` call for `email` audience type:
    
    
    {
      "type": "audiencelist",
      "properties": {
        "listData": {
          "add": [{
              "email": "alex@example.com"
            },
            {
              "email": "john@example.com"
            }
          ]
        }
      }
    }
    

The following code snippet shows a sample `audienceList` call for `madid` audience type:
    
    
    {
      "type": "audiencelist",
      "properties": {
        "listData": {
          "add": [{
              "madid": "sample_madid"
            },
            {
              "madid": "sample_madid_1"
            }
          ]
        }
      }
    }
    

> ![warning](/docs/images/warning.svg)
> 
> Criteo’s API implements [rate limits](<https://developers.criteo.com/marketing-solutions/docs/rate-limits>) to limit the number of requests you’re able to make on any API endpoint per minute.

## FAQ

#### How do I obtain my Criteo audience segment ID?

  1. Log in to your [Criteo marketing account](<https://marketing.criteo.com/>).
  2. In the left navigation bar, go to **Assets** > **Audiences**.
  3. You can find the relevant audience segment ID under the **Segments** tab:

[![Criteo Audience Segment ID](/docs/images/event-stream-destinations/criteo-audience-segment-id.webp)](</docs/images/event-stream-destinations/criteo-audience-segment-id.webp>)