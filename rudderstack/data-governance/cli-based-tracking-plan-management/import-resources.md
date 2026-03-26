# Import Workspace Resources to Rudder CLI Project Alpha

Import existing RudderStack workspace resources into your CLI project to start managing them programmatically through Git workflows.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __6 minute read

  * 


This guide explains how to import existing workspace resources into your CLI project to start managing them programmatically through Git workflows.

## Overview

Rudder CLI lets you manage your Data Catalog and Tracking Plans programmatically through YAML files and Git workflows. However, if you already have resources configured in your RudderStack workspace, you need a way to import them into your CLI project rather than recreating them from scratch.

The `import workspace` command solves this problem by importing all existing workspace resources into your CLI project, allowing you to start managing them through Git-based workflows.

#### How it works

The import process consists of three key steps:

  1. **Generate YAML files** : The `import workspace` command creates YAML files containing your existing workspace resources.
  2. **Review and organize the files** : Review and organize the generated files in your project directory.
  3. **Apply changes** : You can then use the standard `apply` command to link the imported resources to your CLI project.


## Prerequisites

Before importing workspace resources, make sure you have:

  * A Rudder CLI project directory (can be empty)


  * Generate a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) in the RudderStack dashboard with the following [permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) to manage Data Catalog and Tracking Plans:

Resource| Permissions  
---|---  
Tracking Plans| **Create & Delete**, **Edit**  
Data Catalog| **Edit**  
  
  * **For testing or development purposes only** : Generate a [Personal Access Token](<https://www.rudderstack.com/docs/access-management/personal-access-tokens/>) with **Read-Write** role


> ![warning](/docs/images/warning.svg)
> 
> **RudderStack recommends using a workspace-level Service Access Token for authentication.**
> 
> Any action authenticated by a Personal Access Token will break if the user is removed from the organization or a breaking change is made to their permissions.

#### Token permissions for legacy RBAC system

If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), your workspace-level Service Access Token should have **Admin** permissions.

See [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for more information on generating the token.

[![workspace-level Service Access Token with Admin permission](/docs/images/access-management/permissions/legacy/admin.webp)](</docs/images/access-management/permissions/legacy/admin.webp>)

## Import workspace resources

> ![warning](/docs/images/warning.svg)
> 
> **Before you import workspace resources**
> 
> Before starting the import process, make sure:
> 
>   * You have no unsynced changes in your project — make sure to apply any existing changes first by running the `apply` command.
>   * You don’t have an existing directory named `imported` in your CLI project
> 

> 
> Otherwise, the import process will fail.

To import all resources from your current workspace into a CLI project, run the `import workspace` command — replace `<project-directory>` with the path to your CLI project directory.
    
    
    rudder-cli import workspace -l <project-directory>
    

The above command will:

  * Scan your workspace for all resources not yet managed by Rudder CLI
  * Generate YAML files in an `imported` directory within your project
  * Create import metadata that maps local resource IDs to their corresponding workspace IDs


### Supported resource types

You can use the `import workspace` command to import all resources from your workspace into your CLI project. This includes events, properties, categories, custom types, Event Stream sources, and Tracking Plans (created via the [RudderStack dashboard](<https://www.rudderstack.com/docs/data-governance/tracking-plans/create-tracking-plans/>) and [Data Catalog API](<https://www.rudderstack.com/docs/api/data-catalog-api/>)).

Note that:

  * The `import workspace` command does not support importing [non-migrated](<https://www.rudderstack.com/docs/data-governance/tracking-plans/migration-guide/>) legacy Tracking Plans created via Google Sheets or the deprecated [Tracking Plan API](<https://www.rudderstack.com/docs/api/tracking-plan-api/>).
  * RudderStack supports importing only the [SDK sources](<https://www.rudderstack.com/docs/sources/event-streams/sdks/>) (client-side and server-side) currently. Cloud and webhook sources are not supported.


## Generated file structure

After running the `import workspace` command, you will find an `imported` directory within your project directory with the following structure:
    
    
    project/
    ├── imported/
    │   └── data-catalog/
    │       ├── events/
    │       ├── properties/
    │       ├── categories/
    │       ├── trackingplans/
    │       └── custom-types/
    

> ![info](/docs/images/info.svg)
> 
> Each subdirectory contains YAML files for the corresponding resource types. If no resources exist for a particular type, the directory will be empty.

## Import metadata

The generated YAML files contain special import metadata that tells Rudder CLI how to link local resources to workspace resources. This metadata enables you to manage resources across different workspaces.

Here’s an example of what the import metadata looks like:
    
    
    version: "rudder/v0.1"
    kind: "categories"
    metadata:
      import:
        workspaces:
          - workspace_id: "3NrueK2Hu7ooXVQqQJhKqKlnofE"
            resources:
              - local_id: "abc"
                remote_id: "cat_343HNkcWRt8YXHphthHwa8QEdXE"
              - local_id: "webapp"
                remote_id: "cat_2ohsVV9iKuw7GfLFITwsVLn6Nhy"
      name: "categories"
    spec:
      categories:
        - id: "abc"
          name: "ABC"
        - id: "webapp"
          name: "Webapp"
    

The `metadata.import` section contains the following information:

Property| Type| Description  
---|---|---  
`workspace_id`| String| The ID of the workspace where resources were imported from.  
`resources`| Array| Array of mappings between local resource IDs and their corresponding remote workspace IDs.  
  


> ![warning](/docs/images/warning.svg)Do not change the `remote_id` values in the imported YAML files as it will result in an error.  
  
For detailed information about the import metadata structure and properties, see the [CLI Project Resources YAML Reference](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/project-yaml-reference/#import-metadata>).

## Review and organize imported resources

After generating the YAML files, you should:

  * **Review the generated files** to ensure they contain the expected resources.
  * **Move files to your desired location** within your project structure.
  * **Modify resource configurations** like names, descriptions, etc. as needed.


> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * You can move files out of the `imported` directory to organize them according to your project structure preferences.
>   * You can change the `local_id` values in the imported YAML files **before** applying them to your CLI project.
>   * If you change the `local_id` values in the imported YAML files, make sure to also update those values in the import metadata mapping.
> 


## Apply imported resources

The `import workspace` command reads the upstream resource information and generates YAML files. However, it does not link the resources to your CLI project. To complete the import process, you need to run the `apply` command, which links the imported resources to your CLI project.

To apply the resources to your CLI project, run the following command — replace `<project-directory>` with the path to your CLI project directory:
    
    
    rudder-cli apply -l <project-directory>
    

The `apply` command:

  * Identifies resources marked for import
  * Links them to your CLI project
  * Shows you a summary of resources to be imported
  * Prompts for confirmation before applying changes


A sample output of the `apply` command is shown below:
    
    
    $ rudder-cli apply -l ./my-rudder-project
    
    Importable resources:
      - category:abc
      - category:webapp
    
    ? Do you want to apply these changes? (y/N)
    

After confirming the changes, you can manage the resources via Rudder CLI going forward.

## Key considerations

Keep the following points in mind while using the import process for your CLI project:

#### Dos

  * Before you run the `import workspace` command, make sure:

    * You have applied any existing changes in your project using the `apply` command
    * You don’t have an existing directory named `imported` in your CLI project
  * **Use Rudder CLI as the source of truth**. For CLI-managed resources, use only Rudder CLI to manage them instead of the dashboard or APIs. Otherwise, you will be prompted to delete the changes made outside of Rudder CLI.


> ![info](/docs/images/info.svg)
> 
> After applying the imported resources to your CLI project, Rudder CLI becomes the source of truth for those resources.

#### Don’ts

  * Do not change the `remote_id` values in the imported YAML files as it will result in an error.

  * Do not change the `local_id` values in the imported YAML files after applying them to your CLI project. However, you can change them **before** applying them to your CLI project.

    * If you change the `local_id` values in the imported YAML files, make sure to also update those values in the import metadata mapping.
  * Do not delete any resources in your RudderStack dashboard before applying the changes to your workspace via CLI. Otherwise, you will get an `Resource with ID not found` error.


## Best practices

  * **Review before applying** : Always review generated YAML files before applying them.
  * **Organize your structure** : Move imported files to locations that match your project organization.
  * **Test in development** : Consider importing in a development workspace first to test the process.
  * **Version control** : Commit your imported YAML files to version control for proper tracking.


## Next steps

After successfully importing and applying workspace resources, you can now leverage Rudder CLI to manage these resources programmatically, through Git workflows.

  * See [CLI-based Tracking Plan Management](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/>) for more information about managing resources with Rudder CLI.
  * See [Manage Workspaces with Rudder CLI](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/import-resources/manage-workspaces/>) to learn how import metadata enables workspace-specific workflows and production deployment strategies.