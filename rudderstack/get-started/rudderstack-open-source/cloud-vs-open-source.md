# RudderStack Cloud vs. Open Source

Compare features and setup options in RudderStack’s two product offerings—Cloud and Open Source.

* * *

  * __4 minute read

  * 


If you are evaluating RudderStack in a [build vs. buy](<https://www.rudderstack.com/blog/when-to-build-vs-buy-data-pipelines>) context, it’s important to understand the components and features that make up the RudderStack service as they relate to your current and future needs.

This guide will help you decide the right setup based on your environment and data needs: [RudderStack Cloud](<https://app.rudderstack.com/signup?type=freetrial>) or [RudderStack Open Source](<https://app.rudderstack.com/signup?type=opensource>).

## Comparison overview

Advanced RudderStack features are not supported in the open source version of the product.

Feature| Description| RudderStack Cloud| RudderStack Open Source  
---|---|---|---  
Events| Features related to tracking, collecting, and routing your events.| __| __  
Reverse ETL|  Send data from your warehouse to third-party platforms.| __| __  
Data governance|  Investigate and troubleshoot inconsistencies in your event data.| __| __  
Deployment and security|  Scale and secure your RudderStack deployment.| __| __  
Monitoring and observability|  Monitor your data pipelines using different tools and alerting mechanisms.| __| __  
Audits and user management|  Manage users and set access controls for various RudderStack features.| __| __  
  
## Cloud and open source setup

To understand the effort involved in setting up RudderStack, it’s useful to take a look at RudderStack’s architecture which comprises the [control plane](<https://www.rudderstack.com/docs/resources/rudderstack-architecture/#control-plane>) and the [data plane](<https://www.rudderstack.com/docs/resources/rudderstack-architecture/#data-plane>). These two services work together to govern the data flow between your event sources and destinations.

> ![info](/docs/images/info.svg)
> 
>   * The **control plane** refers to the front-end RudderStack dashboard where you can manage the configuration of your sources and destinations.
>   * The **data plane** is RudderStack’s core engine responsible for receiving event data and transforming it into the required destination format before relaying events to the destination.
> 


### RudderStack Cloud

With [RudderStack Cloud](<https://app.rudderstack.com/signup/>), you get a RudderStack-hosted data plane and control plane so you need not worry about the setup. You can set up a source and destination and see the events flow within minutes.

RudderStack’s free cloud tier offers multiple sources, destinations and delivery of 1 million events per month. It provides key features like [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) and [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>). If you start on the cloud free tier, it’s much easier to convert to a [paid plan](<https://www.rudderstack.com/pricing>) as your needs evolve over time.

### RudderStack open source

For [RudderStack Open Source](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/>), you have the following data plane and control plane setup options:

  1. [Set up the data plane](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/data-plane-setup/>) on Docker, Kubernetes, or in your own development environment. **RudderStack will not host the data plane for you**.

  2. Set up the control plane using one of the following options:


  * Use the [RudderStack-hosted control plane](<https://app.rudderstack.com/signup?type=opensource>) (**recommended**).
  * Self-host your source-destination configurations by setting up your own control plane using [Control Plane Lite](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/>).


> ![warning](/docs/images/warning.svg)
> 
> Cloud-based features like [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) and [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) are not available if you use the _Control Plane Lite_ utility. If you are unsure, it is highly recommended you use RudderStack Cloud to get started.

## Detailed feature comparison

### Events-related features

Feature| RudderStack Cloud| RudderStack Open Source| Notes  
---|---|---|---  
Event metrics|  __| ❗| 

  * Get information on the number of events ingested during a specified timeframe.
  * Applicable only for [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) destinations.
  * For Open Source users, this feature is available only in the [RudderStack-hosted control plane](<https://app.rudderstack.com/signup?type=opensource>).

  
[Event backup in your own bucket](<https://www.rudderstack.com/docs/user-guides/administrators-guide/bucket-configuration-settings/>)|  __| __| RudderStack can manage it for you as a part of the[Enterprise plan](<https://www.rudderstack.com/enterprise-quote/>).  
[Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>)|  __| ❗| 

  * For Open Source users, this feature is available only in the [RudderStack-hosted control plane](<https://app.rudderstack.com/signup?type=opensource>).
  * Applicable only for [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>) destinations.

  
RudderStack-managed object storage|  __| __| Use the RudderStack-hosted object storage to**temporarily** store your events before forwarding them to your warehouse destination. **RudderStack does not persist any of this data**.  
[Event Replay](<https://www.rudderstack.com/docs/user-guides/administrators-guide/event-replay/>)|  __| __| This is a[RudderStack Enterprise](<https://www.rudderstack.com/enterprise-quote/>) feature.  
Maintaining event ordering|  __| __| 

  * For Cloud, this is a[RudderStack Enterprise](<https://www.rudderstack.com/enterprise-quote/>) feature.
  * Crucial for a multi-node RudderStack setup

  
[Transformations](<https://www.rudderstack.com/docs/transformations/overview/>)|  __| __| 

  * For Open Source users, transformations are available only in the[RudderStack-hosted control plane](<https://app.rudderstack.com/signup?type=opensource>) and users can set up to **5 transformations**.
  * RudderStack Cloud Free and Starter plan users can set up to **5 transformations** in the **cloud mode**. Growth and Enterprise plan users can create unlimited transformations.
  * Only [Enterprise](<https://www.rudderstack.com/enterprise-quote>) users can create transformations in the **device mode**.

  
  
### Reverse ETL

Feature| RudderStack Cloud| RudderStack Open Source| Notes  
---|---|---|---  
[Reverse ETL](<https://www.rudderstack.com/docs/sources/reverse-etl/>)|  __| __| RudderStack Cloud Free and Starter plan users can set up 1 Reverse ETL source. Growth and Enterprise users can set up unlimited sources.  
Data syncs scheduling|  __| __| -  
[Models](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/models/>)|  __| __| -  
  
### Data governance

Feature| RudderStack Cloud| RudderStack Open Source| Notes  
---|---|---|---  
[Data governance](<https://www.rudderstack.com/docs/data-governance/>)|  __| __| This is a[RudderStack Enterprise](<https://www.rudderstack.com/enterprise-quote/>) feature.  
[Tracking plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>)|  __| __| This is a[RudderStack Enterprise](<https://www.rudderstack.com/enterprise-quote/>) feature.  
[Data regulation and suppression](<https://www.rudderstack.com/docs/api/user-suppression-api/>)|  __| __| This is a[RudderStack Enterprise](<https://www.rudderstack.com/enterprise-quote/>) feature.  
  
### Deployment and security

Feature| RudderStack Cloud| RudderStack Open Source| Notes  
---|---|---|---  
Multi-node scaling|  __| __| This is a[RudderStack Enterprise](<https://www.rudderstack.com/enterprise-quote/>) feature.  
Single sign-on (SSO)| __| __| This is a[RudderStack Enterprise](<https://www.rudderstack.com/enterprise-quote/>) feature.  
VPC deployment|  __| __| This is a[RudderStack Enterprise](<https://www.rudderstack.com/enterprise-quote/>) feature.  
  
### Monitoring and observability

Feature| RudderStack Cloud| RudderStack Open Source| Notes  
---|---|---|---  
Grafana dashboards for monitoring|  __| __| Available for RudderStack Starter, Growth, and Enterprise users.  
Alerting and error notifications|  __| __| This is a[RudderStack Enterprise](<https://www.rudderstack.com/enterprise-quote/>) feature.  
  
### Auditing and user management

Feature| RudderStack Cloud| RudderStack Open Source| Notes  
---|---|---|---  
Ability to add other team members in the workspace|  __| __| You can invite up to 10 members to your workspace in RudderStack Cloud Free and Starter plan, and unlimited members in the Growth and Enterprise plan.  
Audit logs|  __| __| This is a[RudderStack Enterprise](<https://www.rudderstack.com/enterprise-quote/>) feature.