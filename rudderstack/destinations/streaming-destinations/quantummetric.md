# Quantum Metric

Send your event data from RudderStack to Quantum Metric.

* * *

  * __2 minute read

  * 


[Quantum Metric](<https://www.quantummetric.com/>) is a continuous product design platform that lets you leverage real-time digital insights to improve your product. It gives you complete visibility into your customers’ product experience and helps you prioritize the most important product features that have the most impact on your brand.

RudderStack helps you integrate your website with Quantum Metric to auto-track all your user data.

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Quantum Metric** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In the web device mode integration, that is, using the [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, RudderStack loads the Quantum Metric native SDK from the `https://cdn.quantummetric.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the Quantum Metric SDK successfully.

## Get started

Once you have confirmed that Quantum Metric supports the source type, follow these steps:

  * From your [RudderStack dashboard](<https://app.rudderlabs.com/>), add the source. Then, select **Quantum Metric** from the list of destinations.
  * Assign a name to your destination, and then click **Next**. You should then see the following screen:

[![Quantum Metric Connection Settings](/docs/images/quantum-metric.webp)](</docs/images/quantum-metric.webp>)

### Connection Settings

To set up Quantum Metric as a destination in RudderStack you will need your **Site ID**.

  1. Log into the [IAM Quantum Metric dashboard](<https://iam.quantummetric.com/>).
  2. Select the **Account** button in the top-right corner.
  3. Click **Install** to inspect the installation tag.


Your Site ID will be found in the following line:
    
    
    qtm.src = 'https://cdn.quantummetric.com/qscripts/quantum-<SITE_ID>.js';
    

  4. Click **Next** to complete the configuration. Quantum Metric will now be added and enabled as a device-mode destination in RudderStack.


> ![info](/docs/images/info.svg)
> 
> As this is a web device mode-only integration, the **Use native SDK to send events** option cannot be disabled. For more information on web device mode, refer to the [RudderStack Connection Modes](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/>) guide.

## Sending events to Quantum Metric

Quantum Metric auto-tracks your user data. There is **no need** to call any of `identify`, `page` or `track` methods explicitly.