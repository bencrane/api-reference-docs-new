# Use Custom Domains

Use your own domain to serve the RudderStack JavaScript SDK and send events to RudderStack.

* * *

  * __2 minute read

  * 


This guide covers the steps to use your own domain instead of RudderStack domains for the following use cases:

  * [Serving the JavaScript SDK](<https://www.rudderstack.com/docs/user-guides/how-to-guides/custom-domains/serve-js-sdk/>)
  * [Source configuration response](<https://www.rudderstack.com/docs/user-guides/how-to-guides/custom-domains/fetch-source-config/>)
  * [Sending events to the RudderStack backend (data plane)](<https://www.rudderstack.com/docs/user-guides/how-to-guides/custom-domains/send-events/>)


Setting up custom domains for the above use cases can help you adhere to your Content Security Policy (CSP), reduce the impact of adblockers, and satisfy any compliance-related requirements.

> ![info](/docs/images/info.svg)
> 
> The steps and examples in this guide are applicable for [AWS CloudFront](<https://aws.amazon.com/cloudfront/>). However, the settings should be similar regardless of your CDN.

## Setup overview

> ![warning](/docs/images/warning.svg)
> 
> You must have access to your domain’s DNS settings and your CDN settings.

Create a new distribution by following these steps:

  1. Log in to your [AWS console](<https://aws.amazon.com/console/>).
  2. Click **Services** and go to **Network & Content Delivery** > **CloudFront**.
  3. Click **Create a CloudFront distribution**.


The following table gives a high-level overview of the required cache policy, origin request policy, and response headers policy:

Scenario| Cache policy| Origin request policy| Response headers policy (optional)  
---|---|---|---  
[Serve the JavaScript SDK](<https://www.rudderstack.com/docs/user-guides/how-to-guides/custom-domains/serve-js-sdk/>)| `CachingOptimized`| [Origin request policy settings](<https://www.rudderstack.com/docs/user-guides/how-to-guides/custom-domains/serve-js-sdk/#sdk-origin-request-policy-settings>).| `None`  
[Serve source configuration](<https://www.rudderstack.com/docs/user-guides/how-to-guides/custom-domains/fetch-source-config/>)| See [Cache policy settings](<https://www.rudderstack.com/docs/user-guides/how-to-guides/custom-domains/fetch-source-config/#cache-policy-settings>)| See [Origin request policy settings](<https://www.rudderstack.com/docs/user-guides/how-to-guides/custom-domains/fetch-source-config/#source-origin-request-policy-settings>).| `CORS-With-Preflight`  
[Send events to data plane](<https://www.rudderstack.com/docs/user-guides/how-to-guides/custom-domains/send-events/>)| `CachingDisabled`| See [Origin request policy settings](<https://www.rudderstack.com/docs/user-guides/how-to-guides/custom-domains/send-events/#event-origin-request-policy-settings>).| `CORS-With-Preflight`  
  
## Domains to proxy

The following table lists the three domains that you need to proxy via your own domain to successfully load the SDK and route the events to the RudderStack backend (data plane).

Domain| Use case  
---|---  
`cdn.rudderlabs.com`| To load the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>).  
`api.rudderstack.com`| To fetch the source configuration based on the source [write key](<https://www.rudderstack.com/docs/resources/glossary/#write-key>).  
`DATA_PLANE_URL`| To send events to RudderStack. See the [Dashboard Overview](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>) guide for more information on obtaining your data plane URL.  
  
For each domain, you will need to create a CDN distribution and add a CNAME record in your domain for the distribution domain.

> ![warning](/docs/images/warning.svg)
> 
> To use your own domain for the above endpoints, you will need to route the traffic through your CDN for which you will incur charges.

## FAQ

#### Can I overcome ad blockers by serving the JavaScript SDK on my domain?

Many popular ad blockers block specific SDK-related downloads and API calls based on the domain name and URL. You can serve the SDK on your CDN to circumvent this issue.