# RudderStack Open Source

Use RudderStack Open Source to instrument your data pipelines.

* * *

  * __less than a minute

  * 


The guides in this section will help you set up and use RudderStack Open Source in your preferred development environment.

## What is RudderStack Open Source?

The open source version of RudderStack is a standalone system dependent only on a database (**PostgreSQL**). It consists of 2 major components: **data plane** and **control plane** :

  * The [data plane](<https://github.com/rudderlabs/rudder-server>) is RudderStack’s core engine for processing and routing the events. It is written in Go.
  * The [control plane](<https://app.rudderstack.com/signup?type=opensource>) offers an intuitive UI to help you instrument and manage your connections.

[![RudderStack Architecture](/docs/images/get-started/rudderstack-architecture-new.webp)](</docs/images/get-started/rudderstack-architecture-new.webp>)

For more information, see [RudderStack architecture](<https://www.rudderstack.com/docs/resources/rudderstack-architecture/>).

## Setup overview

Installing and setting up open-source RudderStack involves the following steps:

  1. [Data plane setup](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/data-plane-setup/>): Set up the RudderStack data plane(backend) to track, process, and route your events.
  2. [Control plane setup](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/>): Set up the RudderStack control plane(frontend) to manage your sources, destinations, and connections between them.
  3. [Verify installation](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/sending-test-events/>): Verify your RudderStack installation by sending test events.


> ![warning](/docs/images/warning.svg)
> 
> RudderStack **recommends** using the latest `rudder-server` and `rudder-transformer` versions to avoid any breaking changes to your pipelines.
> 
> See the [Server-Transformer Compatibility](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/server-transformer-compatibility/>) guide for more information.

## Troubleshooting

See [FAQ](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/faq/>) for quick solutions to some common problems you might encounter while setting up and using RudderStack.