# Serve Source Configuration on Custom Domains

Use your own domain for fetching the source configuration.

* * *

  * __4 minute read

  * 


This guide covers the steps to use your own domain instead of the RudderStack domains for fetching the source configuration response.

## Setup overview

When the RudderStack SDK is loaded, it uses the source write key to fetch the required source configuration from RudderStack. For this reason, the distribution settings in this scenario are slightly different as you need to explicitly allowlist the **Authorization** header to make sure it is sent along with each request.

> ![info](/docs/images/info.svg)
> 
> The SDK makes a `GET` request to the `https://api.rudderstack.com/sourceConfig` URL to fetch the source configuration and uses the write key as the authorization header.

Create a new distribution by following these steps:

  1. Log in to your [AWS console](<https://aws.amazon.com/console/>).
  2. Click **Services** and go to **Network & Content Delivery** > **CloudFront**.
  3. Click **Create a CloudFront distribution**.


The following table gives a high-level overview of the required cache policy, origin request policy, and response headers policy for fetching the source configuration response:

Cache policy| Origin request policy| Response headers policy (optional)  
---|---|---  
Cache policy settings| Origin request policy settings| `CORS-With-Preflight`  
  
## Step 1: Configure distribution

[![Custom domains distribution settings](/docs/images/user-guides/custom-domains/source-config-distribution-settings.webp)](</docs/images/user-guides/custom-domains/source-config-distribution-settings.webp>)

The following sections highlight the required distribution settings.

#### Origin

Field| Setting  
---|---  
Origin domain| `api.rudderstack.com`  
Protocol| `HTTPS Only`  
HTTPS port| `443`  
Minimum origin SSL protocol| `TLSv1.2`  
Name| `api.rudderstack.com`  
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

Field| Setting  
---|---  
Cache policy| See Cache policy settings  
Origin request policy| See Origin request policy settings  
Response headers policy| `CORS-With-Preflight`  
  
#### Cache policy settings

Create a cache policy with the following settings:

[![Custom domains cache policy settings](/docs/images/user-guides/custom-domains/custom-domains-4-latest.webp)](</docs/images/user-guides/custom-domains/custom-domains-4-latest.webp>)Field| Setting  
---|---  
Name| `<CACHE_POLICY_NAME>`  
Description| `<CACHE_POLICY_DESCRIPTION>`  
Minimum TTL| `1`  
Maximum TTL| `86400`  
Default TTL| `300`  
Headers| `Include the following headers`  
Add header| `Authorization`  
`Origin`  
Query strings| `All`  
Cookies| `None`  
  
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
  
> ![warning](/docs/images/warning.svg)
> 
> For non-AWS setups, you may also need to add the `Authorization` header to the origin request policy.

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

## Step 3: Fetch source configuration

To use a custom URL to fetch the source configuration, add it as an option when loading the SDK.

An example of how to use a custom URL to fetch the JavaScript SDK source configuration is shown below:
    
    
    rudderanalytics.load(
      SOURCE_WRITE_KEY,
      DATA_PLANE_URL, {
        configUrl: "https://<YOUR_CUSTOM_DOMAIN>",
      }
    )
    

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