# RudderStack Glossary

Familiarize yourself with the RudderStack-specific features and terminology.

* * *

  * __8 minute read

  * 


This guide lists the definitions of the RudderStack-related terms that you are likely to encounter throughout the documentation and while using RudderStack.

### Access management

RudderStack’s [Access Management](<https://www.rudderstack.com/docs/access-management/>) feature lets you manage users and their permissions in your RudderStack workspace. It lets you set access controls and collaborate with other members of your organization.

### Airflow Provider

[Airflow Provider](<https://www.rudderstack.com/docs/data-pipelines/orchestration/airflow/>) is a tool that lets you programmatically schedule and trigger your Reverse ETL syncs from outside RudderStack and integrate them with your existing Airflow workflows.

### Anonymous ID

An anonymous ID is an auto-generated **UUID** (Universally Unique Identifier) that gets assigned to each unique and unidentified visitor to your website.

### Audit logs

[Audit Logs](<https://www.rudderstack.com/docs/dashboard-guides/audit-logs/>) give you a detailed log of all user activities happening within your RudderStack. These include various operations related to sources, destinations, transformations, user management, and more.

[![](/docs/images/audit-logs.webp)](</docs/images/audit-logs.webp>)

### Cloud mode

In this [connection mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/>), the RudderStack SDKs track and send the event data to RudderStack for processing. RudderStack then routes this data to the specified destination. Use this mode when you want to use RudderStack’s [Transformations](<https://www.rudderstack.com/docs/transformations/>) feature to transform your events before sending them to your destination.

### Connection

A connection is a one-to-one directional event flow between a RudderStack source and a destination.

You can set up different types of connections in RudderStack to send your events:

  * [Event Stream](<https://www.rudderstack.com/docs/sources/event-streams/>): One source to many destinations
  * [Reverse ETL](<https://www.rudderstack.com/docs/sources/reverse-etl/>): One warehouse source to multiple event stream destinations


### Control plane

The control plane manages the configuration of your sources and destinations. The interface for the control plane is the [RudderStack dashboard](<https://app.rudderstack.com/>) (web app).

### Control Plane Lite

The [Control Plane Lite](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/>) utility lets you self-host your source and destination configurations. You can manage these configurations by locally exporting to or importing them from a JSON file.

### Customer Data Platform (CDP)

A Customer Data Platform (CDP) is software or a collection of tools that unifies and persists all customer records across multiple data sources in a centralized location. It is accessible to other tools in your tech stack and lets you build a comprehensive customer profile for a variety of use cases.

### Data governance

RudderStack’s [Data Governance](<https://www.rudderstack.com/docs/data-governance/overview/>) capabilities let you access all your events and their metadata programmatically and identify any inconsistencies in them. This includes vital information related to the event schema, event payload versions, data types, and more.

### Data plane

RudderStack’s core engine responsible for receiving, processing, and relaying your event data to the specified destination. For more information, refer to the [Architecture](<https://www.rudderstack.com/docs/resources/rudderstack-architecture/>) guide.

### Data plane URL

RudderStack requires the [data plane URL](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>) for routing and processing events in the backend. You can find the URL in the home page of your RudderStack dashboard.

[![Data Plane URL](/docs/images/data-plane-url.webp)](</docs/images/data-plane-url.webp>)

### Data retention

RudderStack’s data retention settings let you define and manage your event data storage. You can disable event data storage completely, store the events in your own cloud storage, or store them in the RudderStack-hosted cloud storage. For more information, refer to the [Data Management](<https://www.rudderstack.com/docs/dashboard-guides/data-management/>) guide.

### Destination

A destination is a tool or platform where you want to send the event data via RudderStack. RudderStack currently supports over 150 [Cloud destinations](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) and [Warehouse destinations](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>).

[![](/docs/images/destinations.webp)](</docs/images/destinations.webp>)

### Device mode

In this connection mode, you can send the source events to the destinations using the native client-specific libraries present on your website/mobile app. These libraries allow RudderStack to use the data you collect on your device to call the destination APIs without sending it to the RudderStack server first.

Use device mode when you want to send events to a destination directly, without any transformation. For more information, see the [Connection Modes](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/>) guide.

### ELT

The ELT (Extract, Load, Transform) process involves obtaining the data from the source, replicating it into the target system (typically data warehouse or data lake), and transforming it depending on the use case.

### Event

Events are the fundamental components of clickstream data. They correspond to the user actions on websites or mobile apps such as clicks, page or screen views, logins, registrations, etc. Tracking events in real-time helps businesses to better understand the users and their product journey.

### Event spec

The [RudderStack Event Spec](<https://www.rudderstack.com/docs/event-spec/standard-events/>) helps you plan your event data and provides various options for tracking your events across all the RudderStack SDKs and APIs. RudderStack has a unified event semantic for different destination platforms, so you can easily translate your event data to different downstream tools by following this spec.

### Event Stream

RudderStack’s [Event Streams](<https://www.rudderstack.com/docs/sources/event-streams/>) feature lets you collect your event data from all of your web and mobile apps and route it to a wide array of customer tools and data warehouses.

### Identity stitching

[Identity Stitching](<https://www.rudderstack.com/docs/profiles/concepts/identity-graph/>) is the process of matching different identifiers across multiple devices and digital touchpoints to build a cohesive and omnichannel customer profile. With RudderStack’s warehouse-first architecture, you can send all your cross-platform data to your warehouse and perform identity stitching on it.

### Live events

RudderStack’s [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) feature lets you view the live events collected from your sources and sent to the connected destinations in real-time. With this feature, you can easily debug any errors in the failing events at a destination level and reduce your troubleshooting time and efforts.

[![Live Events](/docs/images/rs-cloud/source-live-events.webp)](</docs/images/rs-cloud/source-live-events.webp>)

### Models

RudderStack’s [Models](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/models/>) feature lets you create models by defining custom SQL queries. You can then run these queries on your warehouse and send the resulting data to specific destinations.

### Personal Access Token

[Personal Access Token](<https://www.rudderstack.com/docs/access-management/personal-access-tokens/>) is a unique key associated with your RudderStack account. You can use it to consume all the public RudderStack APIs.

> ![info](/docs/images/info.svg)
> 
> For production use cases, RudderStack recommends using a Service Access Token over a Personal Access Token.

[![New Personal Access Token in RudderStack dashboard](/docs/images/rudderstack-api/personal-access-token-1.webp)](</docs/images/rudderstack-api/personal-access-token-1.webp>)

### Profiles

[Profiles](<https://www.rudderstack.com/docs/profiles/overview/>) are the collection of all the events associated with a user. RudderStack lets you create and manage these profiles in your warehouse.

### Properties

Properties are additional contextual information you can add to a `track` call to further describe the action a user takes. RudderStack has reserved some standard properties listed in the following table and handles them in a special manner.

### Reverse ETL

[Reverse ETL](<https://www.rudderstack.com/docs/sources/reverse-etl/>) is the process of routing the data residing in your data warehouse to various downstream tools within your customer data stack. This includes various SaaS marketing, analytics, sales, and customer support tools.

### Source

A [source](<https://www.rudderstack.com/docs/sources/overview/>) is a platform or an application (web, mobile, server-side, or a third-party cloud app) from where RudderStack tracks and collects your event data.

[![](/docs/images/sources.webp)](</docs/images/sources.webp>)

### Service Access Token

A [Service Access Token (SAT)](<https://www.rudderstack.com/docs/access-management/service-access-tokens/>) is a unique key that lets you authenticate and gain access to another RudderStack service or API. It provides organizations with a flexible and secure way to manage access to services and resources within RudderStack without requiring you to repeatedly log in.

Unlike [Personal Access Tokens](<https://www.rudderstack.com/docs/access-management/personal-access-tokens/>) which are tied to individual users, SATs are accessible to different users within an organization allowing access to shared resources. They ensure continuity and reduce the risk of disruptions when members leave the organization or their [roles](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) change.

RudderStack provides two types of Service Access Tokens:

  * **Workspace-level Service Access Tokens** : Tied to a specific RudderStack workspace — their usage is restricted to workspace-level resources (sources, destinations, transformations, etc.) and APIs.
  * **Organization-level Service Access Tokens** : Used for authenticating only [SSO SCIM](<https://www.rudderstack.com/docs/user-guides/sso-setup/>) and [Audit Logs API](<https://www.rudderstack.com/docs/api/audit-logs-api/>).


### Tracking Plans

[Tracking Plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>) is a RudderStack feature that lets you proactively monitor and act on non-compliant event data coming into your RudderStack sources based on predefined plans. This can help you prevent or de-risk situations where missing or improperly configured event data can break your downstream destinations.

[![Create blank tracking plan](/docs/images/data-governance/blank-tracking-plan.webp)](</docs/images/data-governance/blank-tracking-plan.webp>)

### Traits

[Traits](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/#identify-traits>) are attributes that describe a user. They can be added to an identify call in the `traits` object. Some examples of traits include age, gender, or some specific details - for example, a user’s product plan (basic, premium, and so on). After making an identify call, you don’t need to include all the user traits in the subsequent calls every time. You can include only the changed/updated traits since the last identify call.

### Transformations

[Transformations](<https://www.rudderstack.com/docs/transformations/overview/>)is a RudderStack feature that lets you leverage custom JavaScript functions to implement a variety of use cases like event filtering, sampling, removing sensitive PII, or implementing custom logic to enrich your events.

[![](/docs/images/transformations-glossary.webp)](</docs/images/transformations-glossary.webp>)

### User suppression API

The [User Suppression API](<https://www.rudderstack.com/docs/api/user-suppression-api/>) is RudderStack’s enterprise feature. It lets you programmatically suppress user data identified by a user ID. With this feature, you can block all the user data for all the sources and destinations in RudderStack.

### Visual data mapper

[Visual Data Mapper](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/visual-data-mapper/>) (VDM) is RudderStack’s Reverse ETL feature. It offers an intuitive UI to map your data warehouse columns to specific destination fields without any second-guessing.

### Warehouse schema

When sending your events to a data warehouse via RudderStack, you don’t need to define a schema. RudderStack automatically does that for you by following a predefined warehouse schema that defines the different tables and columns created based on different event types. For more information, refer to the [Warehouse Schema](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/warehouse-schema/>) guide.

### Workspace ID

RudderStack uses the workspace ID for tracking the data internally. You can find your workspace ID by navigating to **Settings** > **Company** in the RudderStack dashboard.

[![](/docs/images/workspace-id.webp)](</docs/images/workspace-id.webp>)

### Workspace token

The workspace token uniquely identifies your RudderStack workspace. You can find your workspace ID by navigating to **Settings** > **Workspace** in the RudderStack dashboard. The workspace token is hidden by default - you must have administrative privileges to access the token.

[![Workspace Token](/docs/images/rs-cloud/workspace-token.webp)](</docs/images/rs-cloud/workspace-token.webp>)

### Write key

The write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.

[![JavaScript SDK source write key](/docs/images/get-started/quickstart/js-write-key.webp)](</docs/images/get-started/quickstart/js-write-key.webp>)