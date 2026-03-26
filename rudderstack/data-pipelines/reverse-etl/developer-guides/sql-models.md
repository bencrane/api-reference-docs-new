# Manage SQL Models using Rudder CLI Alpha

Define and manage SQL models as YAML configurations using the Rudder CLI tool.

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
> This feature is in **Alpha** as part of RudderStack’s [Early Access Program](<https://www.rudderstack.com/docs/get-started/alpha-and-beta-features/alpha-features/>), where we work with early users and customers to test new features and get feedback before making them generally available.
> 
> Note that these features are functional but can change as we improve them. Make sure to [contact](<mailto:support@rudderstack.com>) the RudderStack team before using them in production.

The **SQL Models** feature in Rudder CLI lets you manage your [Reverse ETL SQL model sources](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/features/models/>) through a Git-based workflow. It lets you store your SQL model configurations as YAML files in Git repositories, and use standard Git workflows to collaborate on any changes.

This approach brings version control, collaboration, and review processes to your SQL model configurations, addressing key limitations of managing these resources solely through the UI.

## Key features

**Bi-directional management**

  * Create new SQL model resources directly from CLI
  * Import existing SQL model sources from your workspace into Git


**Validation and preview**

  * Validate SQL syntax and connectivity before deployment
  * Preview query results to ensure correctness
  * Check primary key constraints and column mappings


**Flexible configuration**

  * Define SQL queries inline in YAML files or reference external `.sql` files
  * Support for multiple warehouse types (listed below)


**Automation ready**

  * GitHub Actions integration for CI/CD workflows
  * Dry-run capabilities to preview changes before applying them
  * Cross-domain resource management alongside [Data Catalog and Tracking Plan resources](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/>)


## Supported warehouses

The SQL Models feature supports the following data warehouses:

  * PostgreSQL
  * MySQL
  * Snowflake
  * Amazon Redshift
  * Google BigQuery
  * Databricks
  * Trino


## Workflow overview

  1. Configure your Git repository and Rudder CLI project.
  2. Create new SQL models or import existing ones from your workspace.
  3. Make changes to your SQL models using your preferred editor.
  4. Validate your changes using the `validate` command and `apply` command in dry-run mode (via the `--dry-run` flag).
  5. Use the `preview` command for SQL validation and connection validation.
  6. Apply your changes using the `apply` command.
  7. Create pull requests for team review and approval.
  8. Automatically sync approved changes to your workspace via GitHub Actions.


## Get started

Before you begin, make sure you have:

  * [Rudder CLI](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/>) installed and configured locally
  * A Rudder CLI project directory for storing the SQL model YAML resources
  * [GitHub Actions](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/github-actions/>) configured for automated syncing
  * Generate a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) in the RudderStack dashboard with the following [permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) to manage SQL models:

Resource| Permissions  
---|---  
SQL Models| **Create & Delete**, **Edit**  
  
  * **For testing or development purposes only** : Generate a [Personal Access Token](<https://www.rudderstack.com/docs/access-management/personal-access-tokens/>) with **Read-Write** role


> ![warning](/docs/images/warning.svg)
> 
> **RudderStack recommends using a workspace-level Service Access Token for authentication.**
> 
> Any action authenticated by a Personal Access Token will break if the user is removed from the organization or a breaking change is made to their permissions.

#### Token permissions for legacy RBAC system

If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), your workspace-level Service Access Token should have minimum **Admin** permissions.

See [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for more information on generating the token.

[![workspace-level Service Access Token with Editor permission](/docs/images/access-management/permissions/legacy/admin.webp)](</docs/images/access-management/permissions/legacy/admin.webp>)

## Recommended project structure

The SQL model resources need to be in the location specified in the [`apply` command](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/create-new-resource/#apply-the-sql-model>). If you don’t specify a location, the current directory is used as the project location.

> ![info](/docs/images/info.svg)
> 
> The `apply` command is generic and it will sync all the available resources within the project (SQL models, Data Catalog, etc.).

A recommended directory structure for your CLI project is shown:
    
    
    my-rudder-project/
    ├── sql-models/
    │   ├── user-analytics.yaml
    │   ├── product-models.yaml
    │   └── sql/
    │       ├── user-analytics.sql
    │       └── product-views.sql
    ├── data-catalog/
    │   ├── events/
    │   │   └── product-events.yaml
    │   └── properties/
    │       └── user-properties.yaml
    └── README.md
    

**Key considerations**

  * **File discovery** : The CLI recursively scans the specified directory for all `.yaml` and `.yml` files.
  * **Flexible organization** : You can organize files in any directory structure that makes sense for your project.
  * **External SQL files** : When using the `file` option in your YAML configurations, ensure the SQL files are accessible relative to the YAML file location.
  * **Mixed resources** : The CLI can manage SQL models alongside Data Catalog resources (events, properties, custom types, Tracking Plans) from the same project directory.


## Next steps

See the following guides for working with SQL models using Rudder CLI:

  * [Create new SQL model resources](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/create-new-resource/>)
  * [Import existing SQL model resources](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/import-existing-resource/>)
  * [Validate and preview your models](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/validate/>)
  * [Understand the YAML reference](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sql-models/yaml-reference/>)