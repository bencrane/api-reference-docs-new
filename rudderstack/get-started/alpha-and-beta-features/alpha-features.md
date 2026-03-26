# Alpha Features

Learn about the Alpha features available in RudderStack.

* * *

  * __3 minute read

  * 


This page lists the latest **Alpha** features supported by RudderStack. [Reach out](<mailto:support@rudderstack.com>) to the RudderStack team to get access before using them in production.

## Alpha features list

**Data Governance**

  * CLI-based data governance
  * Copy Tracking Plans across workspaces
  * Rudder CLI tool


**Sources**

  * Kafka source


**Reverse ETL**

  * Manage SQL models using Rudder CLI


The following sections explain each of these Alpha features in more detail.

## CLI-based data governance

  


You can now manage your Data Catalog and Tracking Plans as code. See the [demo](<https://www.rudderstack.com/docs/releases/git-based-data-governance/>) and check out [the documentation](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/>) to learn more about this feature.

With this feature, you can bring the same rigor and process to your Data Catalog and Tracking Plans that you apply to your application code, ensuring consistency and quality in your data collection strategy.

> ![success](/docs/images/tick.svg)
> 
> CLI-based workflows are a key focus area for the Product team, so please [reach out](<mailto:support@rudderstack.com>) with questions and feedback.

## Copy Tracking Plans across workspaces

[![](/docs/images/early-access-program/copy-tracking-plan-alpha-feature.png)](</docs/images/early-access-program/copy-tracking-plan-alpha-feature.png>)

The RudderStack team is actively working on a number of features that will help you version control Tracking Plans within the context of a full development workflow. In the meantime, we’ve built an basic feature you can use to copy Tracking Plans across workspaces in the RudderStack dashboard.

There are two options for copying a Tracking Plan:

  1. **Copy as a new Tracking Plan** : This will copy the Tracking Plan as a net new Tracking Plan in the target workspace. Any new events and properties will be copied into the the Data Catalog of the target workspace.
  2. **Copy and replace an existing Tracking Plan** : This will replace an existing Tracking Plan and connect the migrated plan to the same sources. The original Tracking Plan will be kept and renamed.


> ![warning](/docs/images/warning.svg)
> 
> **Use Option 2 with caution**
> 
> This is an alpha feature — the action **cannot** be rolled back.

[Reach out](<mailto:support@rudderstack.com?subject=I%20have%20a%20question%20about%20the%20Early%20Access%20Program>) and the team can enable this feature for you.

## Rudder CLI tool

The Rudder CLI tool is a part of RudderStack’s [CLI-based Tracking Plans Management](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/>) feature. It lets you manage your Tracking Plans and Data Catalog as code, providing a complete command-line interface for working with your YAML-defined tracking plan configuration.

See the [Rudder CLI tool documentation](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/>) for more information.

## Kafka source

**This feature is available in production.**

The Kafka Source enables you to ingest messages from a Kafka stream directly into RudderStack. This can be useful for:

  * Applying data governance for behavioral event data.
  * Streaming Kafka messages to out-of-the-box cloud integrations.


If you’re interested in streaming data from a system like Kafka, RedPanda, or other messaging queues into RudderStack, [reach out](<mailto:support@rudderstack.com?subject=I%20have%20a%20question%20about%20the%20Early%20Access%20Program>) to discuss your use case.

You can test this source today — [reach out](<mailto:support@rudderstack.com?subject=I%20have%20a%20question%20about%20the%20Early%20Access%20Program>) to enable the integration for your workspace and see the [Kafka Source documentation](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/kafka/>) for usage and more details.

## Manage SQL models using Rudder CLI

You can now use [Rudder CLI](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/>) to manage your [Reverse ETL SQL model sources](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/models/>) through a Git-based workflow. It lets you store your SQL model configurations as YAML files in Git repositories, and use standard Git workflows to collaborate on any changes.

See [Manage SQL Models using Rudder CLI](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/>) for more information.