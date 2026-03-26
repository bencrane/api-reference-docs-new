# Data Plane Setup

Install and set up the RudderStack data plane (backend) in your preferred environment.

* * *

  * __less than a minute

  * 


The data plane is RudderStack’s core engine for processing and routing the events. For more information on how the data plane works, see [RudderStack’s data plane architecture](<https://www.rudderstack.com/docs/resources/rudderstack-architecture/#data-plane-architecture>).

## Setup instructions

Depending on the platform where you want to set up RudderStack, see the following data plane setup instructions:

  * [Docker](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/data-plane-setup/docker/>)
  * [Kubernetes](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/data-plane-setup/kubernetes/>) (**recommended** , if you plan to use RudderStack in production)
  * [Developer machine setup](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/data-plane-setup/developer-machine-setup/>)


> ![warning](/docs/images/warning.svg)
> 
> RudderStack **recommends** using the latest `rudder-server` and `rudder-transformer` versions to avoid any breaking changes to your pipelines.
> 
> See the [Server-Transformer Compatibility](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/server-transformer-compatibility/>) guide for more information.

## Troubleshooting

See [FAQ](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/faq/#data-plane-setup>) for quick solutions to some common problems you might encounter while setting up your RudderStack data plane.