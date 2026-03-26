# Rudder CLI Tool Alpha

Use RudderStack’s CLI tool to manage Tracking Plans, Data Catalog, and SQL models as code.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __4 minute read

  * 


> ![announcement](/docs/images/announcement.svg)
> 
> This feature is in **Alpha** as part of RudderStack’s [Early Access Program](<https://www.rudderstack.com/docs/get-started/alpha-and-beta-features/alpha-features/>), where we work with early users and customers to test new features and get feedback before making them generally available. Note that these features are functional but can change as we improve them.
> 
> Make sure to [contact](<mailto:support@rudderstack.com>) the RudderStack team before using them in production.

The Rudder CLI tool lets you manage multiple RudderStack resources as code, including [Tracking Plans and Data Catalog](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/>) and [SQL models for Reverse ETL](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/>). It provides a complete command-line interface for working with your YAML-defined configurations, enabling Git-based workflows for collaboration and version control.

## Key features

This section highlights the key Rudder CLI features in terms of its core capabilities and usability.

### Core capabilities

  * **Initialize and configure** : Set up your [Tracking Plan project structure](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/tracking-plans/>) with the necessary YAML templates.
  * **Create, update, and delete** : Manage Data Catalog, Tracking Plan, and SQL model resources directly from your terminal.
  * **Bi-directional management** : Create new resources from CLI or import existing resources from your workspace into Git.
  * **Validation and preview** : Verify your YAML configurations locally, validate SQL syntax, and preview query results before pushing changes to production.
  * **Remote synchronization** : Maintain consistency between your local files and your RudderStack workspace.


### Supported resource types

The Rudder CLI tool manages different types of resources through YAML configurations:

### Data governance

  * **Event definitions** : Your events with names, descriptions, and categories
  * **Property definitions** : Reusable properties with [validation rules](<https://www.rudderstack.com/docs/data-governance/data-catalog/properties/#advanced-rules>) like minimum/maximum length, patterns, enums, etc.
  * **Tracking plan rules** : Associations between events and their required properties
  * **Cross-references** : Reuse properties across multiple events using the path reference system


See [CLI-based Tracking Plans Management](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/>) for more details.

### SQL models

  * **SQL model definitions** : [Reverse ETL SQL model sources](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/models/>) with query logic, primary keys, and warehouse connections
  * **External SQL files** : Reference external `.sql` files or define queries inline in YAML
  * **Import existing resources** : Import existing SQL model resources from your workspace into Git


See [Manage SQL Models using Rudder CLI](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/>) for more details.

### Event Stream sources

  * **Event Stream source definitions** : [Event Stream sources](<https://www.rudderstack.com/docs/sources/event-streams/>) with source type, name, and enabled status
  * **Governance validation settings** : Associate [Tracking Plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>) with sources for data governance
  * **Violation handling rules** : Control violation handling behavior for different event types (`track`, `identify`, `group`, `page`, `screen`) through granular configuration options


See [Manage Event Stream Sources using Rudder CLI](<https://www.rudderstack.com/docs/sources/event-streams/sdks/manage-sources-with-rudder-cli/>) for more details.

### CI/CD integration

  * **GitHub Actions support** : Integrate validation and deployment steps in your GitHub workflows.
  * **Automated validation** : Run configuration checks as part of your CI pipeline.
  * **Deployment automation** : Push validated Tracking Plans to production.


## Get started

Choose your workflow based on the resources you want to manage:

  1. [Install the Rudder CLI tool](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/installation/>) in your preferred environment.
  2. Authenticate the tool and configure access to your RudderStack workspace by creating a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) with the [relevant permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) to manage Data Catalog and Tracking Plans.
  3. [Initialize a new Tracking Plan project](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/tracking-plans/>) with [YAML definitions](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/project-yaml-reference/>). Then, sync the changes to your workspace.
  4. Automate Tracking Plan management using [GitHub Actions](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/github-actions/>).


See [CLI-based Tracking Plans and Data Catalog Management](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/>) for more details.

  1. [Install the Rudder CLI tool](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/installation/>) in your preferred environment.
  2. Authenticate the tool and configure access to your RudderStack workspace by creating a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) with the [relevant permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) to manage SQL models.
  3. Set up your project directory and [create new SQL model resources](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/create-new-resource/>) or [import existing ones](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/import-existing-resource/>) from your workspace.
  4. [Validate and preview](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/validate/>) your SQL models before deployment.
  5. Automate SQL model management using [GitHub Actions](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/github-actions/>).


See [Manage SQL Models using Rudder CLI](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/>) for more details.

  1. [Install the Rudder CLI tool](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/installation/>) in your preferred environment.
  2. Authenticate the tool and configure access to your RudderStack workspace by creating a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) with the [relevant permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) to manage Event Stream sources.
  3. [Create new Event Stream sources](<https://www.rudderstack.com/docs/sources/event-streams/sdks/manage-sources-with-rudder-cli/quickstart/>) in your workspace.
  4. [Validate and preview](<https://www.rudderstack.com/docs/sources/event-streams/sdks/manage-sources-with-rudder-cli/quickstart/#6-validate-and-deploy>) your Event Stream sources before deployment.


See [Manage Event Stream Sources using Rudder CLI](<https://www.rudderstack.com/docs/sources/event-streams/sdks/manage-sources-with-rudder-cli/>) for more details.