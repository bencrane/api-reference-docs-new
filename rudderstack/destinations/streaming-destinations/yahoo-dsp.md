# Yahoo DSP

Send your event data from RudderStack to Yahoo DSP.

* * *

  * __3 minute read

  * 


[Yahoo demand-side platform (DSP)](<https://www.adtech.yahooinc.com/advertising/solutions/dsp>) (formerly Verizon Media) provides a unified solution to advertisers to programmatically monitor, create, and manage advertising campaigns.

RudderStack supports Yahoo DSP as a destination where you can send your event data seamlessly.

Find the open source transformer code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-transformer/tree/master/src/v0/destinations/yahoo_dsp>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Cloud, Warehouse, Shopify
  * Refer to it as **Yahoo DSP** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Shopify| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)  
  
## Get started

Once you have confirmed that the source platform supports sending events to Yahoo DSP, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Yahoo DSP**.
  2. Assign a name to your destination and click **Continue**.


## Connection settings

To successfully configure Yahoo DSP as a destination, you need to configure the following settings:

[![Yahoo DSP connection settings](/docs/images/event-stream-destinations/yahoo-dsp-connection-settings.webp)](</docs/images/event-stream-destinations/yahoo-dsp-connection-settings.webp>)[![Yahoo DSP connection settings](/docs/images/event-stream-destinations/yahoo-dsp-connection-settings-2.webp)](</docs/images/event-stream-destinations/yahoo-dsp-connection-settings-2.webp>)

  * **Client ID** : Enter the client ID from your Yahoo DSP account.
  * **Client Secret** : Enter the client secret from your Yahoo DSP account.


> ![info](/docs/images/info.svg)
> 
> Refer to the [Yahoo DSP documentation](<https://developer.yahooinc.com/dsp/api/docs/authentication/vmdn-auth-overview.html#get-your-id>) for more information on how to obtain the Client ID and Client Secret.

  * **Account ID** : Enter the Advertiser ID linked with your audience type.

  * **Audience Type** : Specify the type of the audience you want to update by choosing `email`, `device ID`, or `IP Address` from the dropdown. The default audience type is `email`.

If you select the audience type as `device ID`, also choose the **Seed List Type** as shown:[![Yahoo DSP connection settings](/docs/images/event-stream-destinations/yahoo-dsp-connection-settings-3.webp)](</docs/images/event-stream-destinations/yahoo-dsp-connection-settings-3.webp>)

  * **Audience ID** : Enter the ID of the created audience.


> ![info](/docs/images/info.svg)
> 
> Refer to the FAQ section for more information on how to obtain Account ID and Audience ID.

  * **Hash Required** : This setting hash-encodes the user data and is enabled by default. However, you can disable it to prevent hashing.


## `audiencelist` event structure

The following code snippet shows a sample `audienceList` call for `email` audience type:
    
    
    {
        "type": "audiencelist",
        "properties": {
            "listData": {
                "add": [{
                        "email": 'alex@example.com'
                    },
                    {
                        "email": 'john@example.com'
                    }
                ]
            }
        }
    }
    

The following code snippet shows a sample `audienceList` call for `deviceId` audience type:
    
    
    {
        "type": "audiencelist",
        "properties": {
            "listData": {
                "add": [{
                        "deviceId": '34A668B2-03CF-11E5-8418-1697F925EC7B'
                    },
                    {
                        "deviceId": '34a66c5e-03cf-11e5-8418-1697f925ec7b'
                    }
                ]
            }
        }
    }
    

The following code snippet shows a sample `audienceList` call for `ipAddress` audience type:
    
    
    {
        "type": "audiencelist",
        "properties": {
            "listData": {
                "add": [{
                        "ipAddress": '10.1.7.237'
                    },
                    {
                        "ipAddress": '10.1.7.238'
                    }
                ]
            }
        }
    }
    

> ![info](/docs/images/info.svg)
> 
> You can send up to 50,000 `email`, `deviceId`, or `ipAddress` fields within one API call.

> ![warning](/docs/images/warning.svg)
> 
> `remove` method is not supported in the `listData`.

## Rate limit

The Yahoo DSP Traffic API is rate-limited and allows only a limited number of requests per user account:

Type| Limit  
---|---  
Requests per minute| 10  
Requests per hour| 300  
Requests per day| 5000  
  
> ![info](/docs/images/info.svg)
> 
> Refer to the [Rate Limits documentation](<https://developer.yahooinc.com/dsp/api/docs/traffic/info/rate-limits.html>) for more information.

## FAQ

#### How do I obtain the Account ID?

The Account ID in the connection settings is the Advertiser ID associted with your Yahoo DSP account. To obtain it:

  1. Log into your [Yahoo DSP](<https://id.b2b.yahooinc.com/identity/XUI/#login/&realm=%2Fdsp&goto=https%3A%2F%2Fid.b2b.yahooinc.com%2Fidentity%2Foauth2%2Fauthorize%3Frealm%3D%252Fdsp%26nonce%3Dm2uitpzW4R1xm6GezTdVpNRD%26state%3DZ5D6wc5CvqnlYm0pZsv4f8t5%26response_type%3Dcode%26scope%3Dopenid%2520profile%2520email%26client_id%3Db743c250-2149-4c47-aed1-31a477359099%26redirect_uri%3Dhttps%253A%252F%252Fdeveloper.yahooinc.com%252Foidc%252Fredirect>) account.
  2. Select **Advertisers** and click the relevant advertiser to get the Advertiser ID as shown:

[![Yahoo DSP connection settings](/docs/images/event-stream-destinations/yahoo-dsp.webp)](</docs/images/event-stream-destinations/yahoo-dsp.webp>)

### How do I create an audience?

To create an audience, follow these steps:

  1. Log into your [Yahoo DSP](<https://id.b2b.yahooinc.com/identity/XUI/#login/&realm=%2Fdsp&goto=https%3A%2F%2Fid.b2b.yahooinc.com%2Fidentity%2Foauth2%2Fauthorize%3Frealm%3D%252Fdsp%26nonce%3Dm2uitpzW4R1xm6GezTdVpNRD%26state%3DZ5D6wc5CvqnlYm0pZsv4f8t5%26response_type%3Dcode%26scope%3Dopenid%2520profile%2520email%26client_id%3Db743c250-2149-4c47-aed1-31a477359099%26redirect_uri%3Dhttps%253A%252F%252Fdeveloper.yahooinc.com%252Foidc%252Fredirect>) account
  2. Select **Advertisers** and choose the relevant advertiser.
  3. Select **Targeting Library** > **New Custom Audience** to create the required audience as shown:

[![Yahoo DSP connection settings](/docs/images/event-stream-destinations/yahoo-dsp-3.webp)](</docs/images/event-stream-destinations/yahoo-dsp-3.webp>)

### How do I obtain the Audience ID?

To obtain the Audience ID, follow these steps:

  1. Log into your [Yahoo DSP](<https://id.b2b.yahooinc.com/identity/XUI/#login/&realm=%2Fdsp&goto=https%3A%2F%2Fid.b2b.yahooinc.com%2Fidentity%2Foauth2%2Fauthorize%3Frealm%3D%252Fdsp%26nonce%3Dm2uitpzW4R1xm6GezTdVpNRD%26state%3DZ5D6wc5CvqnlYm0pZsv4f8t5%26response_type%3Dcode%26scope%3Dopenid%2520profile%2520email%26client_id%3Db743c250-2149-4c47-aed1-31a477359099%26redirect_uri%3Dhttps%253A%252F%252Fdeveloper.yahooinc.com%252Foidc%252Fredirect>) account.
  2. Select **Audiences** and use the ID for relevant audience.

[![Yahoo DSP connection settings](/docs/images/event-stream-destinations/yahoo-dsp-2.webp)](</docs/images/event-stream-destinations/yahoo-dsp-2.webp>)