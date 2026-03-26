# Rudder CLI Use Cases

Learn about the different use cases for the Rudder CLI tool.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __3 minute read

  * 


Rudder CLI lets you manage multiple RudderStack resources as code using YAML configurations. It enables Git-based workflows for version control, collaboration, and CI/CD integration, bringing the same rigor to your data governance and pipeline configurations that you apply to your application code.

This guide gives a quick overview of the different use cases for the Rudder CLI tool.

## CLI-based Data Catalog and Tracking Plan Management

Rudder CLI lets you manage [Tracking Plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>) and [Data Catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>) as code using declarative YAML configurations.

You can define events, properties, and custom types with validation rules, then associate them with Tracking Plans using a structured referencing system. You can also validate configurations locally and sync them to your workspace through Git-based workflows.

See the [CLI-based Data Catalog and Tracking Plan Management](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/>) guide for more details.

**Key capabilities**

  * Define events, properties, and Tracking Plans in YAML files
  * Create reusable property definitions with advanced validation rules
  * Implement dynamic validation rules using conditional validation
  * Validate configurations locally before deployment
  * Integrate with GitHub Actions for automated CI/CD workflows


## Manage SQL Models

Rudder CLI lets you manage [Reverse ETL SQL model sources](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/>) as YAML configurations stored in Git repositories. You can create new SQL models or import existing ones from your workspace, validate SQL syntax and connectivity, and preview query results before deployment.

**Key capabilities**

  * Create new SQL model resources or import existing ones from your workspace
  * Define SQL queries inline in YAML or reference external `.sql` files
  * Validate SQL syntax, connectivity, and primary key constraints
  * Preview query results to ensure correctness
  * Support for multiple warehouse types (PostgreSQL, Snowflake, BigQuery, Redshift, Databricks, and more)


## Manage Event Stream Sources

Rudder CLI also supports managing [Event Stream sources](<https://www.rudderstack.com/docs/sources/event-streams/sdks/manage-sources-with-rudder-cli/>) as code using YAML configurations. You can also configure source-level data governance settings by associating Tracking Plans with sources, and control violation handling behavior for different event types through granular configuration options.

**Key capabilities**

  * Define and manage Event Stream sources in YAML files
  * Associate Tracking Plans with sources for data governance
  * Control violation handling behavior for different event types
  * Validate source configuration changes before deployment
  * Integrate with Git workflows and GitHub Actions for CI/CD


## Manage Transformations

Rudder CLI lets you manage [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) and [Transformation Libraries](<https://www.rudderstack.com/docs/transformations/libraries/>) as code using YAML configurations. You can define transformation logic, build reusable libraries for common operations, test changes locally, and apply updates to your workspace — bringing the same development rigor to transformations that you apply to your other application code.

See the [Manage Transformations using Rudder CLI](<https://www.rudderstack.com/docs/transformations/manage-transformations-with-rudder-cli/>) guide for more details.

**Key capabilities**

  * Define transformations and reusable transformation libraries in YAML files
  * Test transformation behavior locally before deploying changes to your workspace
  * Validate configurations to catch issues early in your development cycle
  * Apply only validated changes to your workspace through a controlled deployment workflow
  * Integrate with Git workflows and GitHub Actions for CI/CD automation