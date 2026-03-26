# Control Plane Setup

Set up your RudderStack Open Source control plane to manage your connections.

* * *

  * __2 minute read

  * 


RudderStack’s [control plane](<https://www.rudderstack.com/docs/resources/rudderstack-architecture/#control-plane>) provides a UI that lets you manage your source and destination configurations.

The easiest way to set up your control plane and manage your configurations is through the RudderStack-hosted control plane, that is, [RudderStack Open Source](<https://app.rudderstack.com/signup?type=opensource>).

## Control plane setup options

RudderStack gives you two options to set up your control plane:

  1. RudderStack-hosted control plane (RudderStack Open Source).
  2. Self-host control plane using Control Plane Lite.


> ![danger](/docs/images/danger.svg)
> 
> [Control Plane Lite](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/>) is now deprecated and does not work with the latest [`rudder-server`](<https://github.com/rudderlabs/rudder-server>) versions.
> 
> To set up and manage your connections, using the RudderStack-hosted control plane is strongly recommended.

The following sections list the steps to set up your control plane using these options.

### RudderStack Open Source

  1. Sign up for [RudderStack Open Source](<https://app.rudderstack.com/signup?type=opensource>).
  2. You will be presented with a **Getting started checklist**. Follow the instructions to set up your connection.

[![Getting started checklist](/docs/images/rudderstack-open-source/get-started-checklist.webp)](</docs/images/rudderstack-open-source/get-started-checklist.webp>)

  3. In the dashboard, go to **Settings** > **Workspace** and copy the **Workspace token**. This token is required to [set up your data plane](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/data-plane-setup/>).

[![Workspace Token](/docs/images/rs-cloud/workspace-token.webp)](</docs/images/rs-cloud/workspace-token.webp>)

> ![info](/docs/images/info.svg)
> 
> The workspace token is a unique identifier of your RudderStack workspace. RudderStack uses this token to automatically read your source-destination configurations when you run the data plane.

### Self-host control plane

Use the [Control Plane Lite](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/>) utility to self-host the control plane. It lets you manage your data pipelines locally by exporting or importing your source-destination configurations from a JSON file.

## Usage

You can use RudderStack Open Source to set up your source-destination connections and manage your data pipelines.

#### Sources

RudderStack Open Source supports only [Event Stream sources](<https://www.rudderstack.com/docs/sources/event-streams/>). It does not support [Reverse ETL](<https://www.rudderstack.com/docs/sources/reverse-etl/>) sources.

> ![success](/docs/images/tick.svg)
> 
> You can set up Reverse ETL sources by signing up for [RudderStack Cloud](<https://app.rudderstack.com/signup/>).

#### Destinations

RudderStack Open Source supports the following destination types:

  * [Cloud destinations](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>)
  * [Warehouse destinations](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/>)


See the destination-specific documentation for detailed setup steps.

#### Features

RudderStack Open Source supports the following features:

  * [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) for better observability into your event flow.
  * [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) to enhance your in-transit events.


> ![info](/docs/images/info.svg)
> 
> [Tracking Plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>) is a paid feature. To use it, upgrade your RudderStack account by reaching out to the Sales team.