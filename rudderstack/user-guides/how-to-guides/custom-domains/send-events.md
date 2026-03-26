# Send Events via Custom Domains

Use your custom domain as a data plane for routing events.

* * *

  * __3 minute read

  * 


This guide covers the steps to use your own domain instead of the RudderStack domains for sending events to the RudderStack backend (data plane).

## Setup overview

Usually, all tracked events are sent to RudderStack via your data plane URL. To have events routed through your own domain, you need to set up a proxy and then use it as the data plane URL while initializing the SDK.

Create a new distribution by following these steps:

  1. Log in to your [AWS console](<https://aws.amazon.com/console/>).
  2. Click **Services** and go to **Network & Content Delivery** > **CloudFront**.
  3. Click **Create a CloudFront distribution**.


The following table gives a high-level overview of the required cache policy, origin request policy, and response headers policy for routing the events through your own domain:

Cache policy| Origin request policy| Response headers policy (optional)  
---|---|---  
`CachingDisabled`| Origin request policy settings| `CORS-With-Preflight`  
  
## Step 1: Configure distribution

[![Custom domains distribution settings](/docs/images/user-guides/custom-domains/send-events-distribution-settings.webp)](</docs/images/user-guides/custom-domains/send-events-distribution-settings.webp>)

The following sections highlight the required distribution settings:

#### Origin

Field| Setting  
---|---  
Origin domain| `DATA_PLANE_URL`  
Protocol| `HTTPS Only`  
HTTPS port| `443`  
Minimum origin SSL protocol| `TLSv1.2`  
Name| `<YOUR_ORIGIN_NAME>`  
Enable Origin Shield| `No`  
  
#### Default cache behavior settings

[![Custom domains distribution settings](/docs/images/user-guides/custom-domains/custom-domains-2-new.webp)](</docs/images/user-guides/custom-domains/custom-domains-2-new.webp>)Field| Setting  
---|---  
Compress objects automatically| `Yes`  
Viewer protocol policy| `Redirect HTTP to HTTPS`  
Allowed HTTP methods| `GET`, `HEAD`, `OPTIONS`, `PUT`, `POST`, `PATCH`, `DELETE`  
Restrict viewer access| `No`  
  
#### Cache key and origin requests

Select **Cache policy and origin request policy (recommended)** and configure the following settings:

[![Cache and origin request policy](/docs/images/user-guides/custom-domains/custom-domains-sending-events-1.webp)](</docs/images/user-guides/custom-domains/custom-domains-sending-events-1.webp>)Field| Setting  
---|---  
Cache policy| `CachingDisabled`  
Origin request policy| See Origin request policy settings.  
Response headers policy| `CORS-With-Preflight`  
  
#### Origin request policy settings

Create a new origin request policy with the following settings:

[![Origin request policy settings](/docs/images/user-guides/custom-domains/custom-domains-origin-request-policy.webp)](</docs/images/user-guides/custom-domains/custom-domains-origin-request-policy.webp>)Field| Setting  
---|---  
Name| `rudderstack-allow-headers`  
Headers| `Include the following headers`  
Add header| 

  * `Access-Control-Request-Headers`
  * `Access-Control-Request-Method`
  * `Origin`
  * `Content-Encoding`

  
Query strings| `All`  
Cookies| `None`  
  
#### Additional distribution settings

The following table summarizes the settings:

Field| Setting  
---|---  
Price class| `Use all edge locations(best performance)`  
Alternate domain name(CNAME)| `<YOUR_CUSTOM_DOMAIN>`  
SSL Certificate| Add your custom SSL Certificate.  
  
See Use custom SSL certificates for more information.  
Supported HTTP versions| `HTTP/2`  
Standard logging| `Off`  
IPv6| `On`  
[![Custom domains distribution settings](/docs/images/user-guides/custom-domains/custom-domains-3.webp)](</docs/images/user-guides/custom-domains/custom-domains-3.webp>)

## Step 2: Deploy distribution

Click **Create distribution** and wait for CloudFront to be deployed:

[![CloudFront deployment](/docs/images/user-guides/custom-domains/custom-domains-deploy-distribution.webp)](</docs/images/user-guides/custom-domains/custom-domains-deploy-distribution.webp>)

#### Add CNAME Record to DNS

Once your distribution is deployed, create a CNAME record for the subdomain you wish to use along with the distribution URL.

Name| Value  
---|---  
Subdomain you wish to use (used in the creation of the distribution).  
  
**Note** : This will vary based on your DNS provider but will typically be just the subdomain. For example: for `cdn.yourdomain.com` you would use `cdn`.| The CDN URL for the created distribution. Example: `<prefix>.cloudfront.net`  
[![CDN distribution URL](/docs/images/user-guides/custom-domains/custom-domains-6.webp)](</docs/images/user-guides/custom-domains/custom-domains-6.webp>)

## Step 3: Send events

Once the setup and DNS propagation is completed, you can use the newly created URL as the data plane URL when initializing the SDK:

Before:
    
    
    rudderanalytics.load( 
      WRITE_KEY ,
      DATA_PLANE_URL
    )
    

After:
    
    
    rudderanalytics.load(
      WRITE_KEY,
      "https://<YOUR_CUSTOM_DOMAIN>"
    )
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure that the events are routed through your own domain and not the `rudderstack.com` domain in the network tab of your browser console.
> 
> See [JavaScript SDK FAQ](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/faq/#how-can-i-verify-if-the-sdk-is-sending-data-to-the-specified-destinations>) for more information.

## Use custom SSL certificates

To use a custom domain for your use case, you can request or import an SSL certificate with your CDN provider. Note that this is an **optional** setting.

To use the AWS Certificate Manager with CloudFront, choose the relevant ACM/IAM certificate in the **Custom SSL certificate** field:

[![Custom SSL certificate](/docs/images/user-guides/custom-domains/custom-domains-8.webp)](</docs/images/user-guides/custom-domains/custom-domains-8.webp>)

> ![info](/docs/images/info.svg)
> 
> You can choose your subdomain or use a wildcard domain `*.yourdomain.com` to set up multiple subdomains.

The AWS Certificate Manager will guide you through the verification by email or DNS TXT records. You will be able to choose your own domain for SSL certificates once verified.

## Custom request header for GCP external load balancer

If you’re setting up a custom domain using the [GCP External HTTPS Load Balancer](<https://cloud.google.com/load-balancing/docs/https>), make sure to [add a custom request header](<https://cloud.google.com/load-balancing/docs/https/custom-headers#working-with-request>) in your backend service configuration:

Header| Value  
---|---  
`Host`| `cdn.rudderlabs.com`