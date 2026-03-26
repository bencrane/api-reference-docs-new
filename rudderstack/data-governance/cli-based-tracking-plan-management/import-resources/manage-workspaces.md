# Manage Workspaces with Rudder CLI Alpha

Manage your workspaces with Rudder CLI to streamline your development and production workflows.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __2 minute read

  * 


This page explains how workspace management works with Rudder CLI and how you can use import metadata to streamline your development and production workflows.

## Overview

When you run the `import workspace` command, the generated YAML files contain special [import metadata](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/import-resources/#import-metadata>) that tells Rudder CLI how to link local resources to workspace resources.

This metadata also includes `workspace_id`, the ID of the workspace where resources were imported from. This means that if you import resources from a development workspace, you can [apply the same project](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/import-resources/#apply-imported-resources>) to a production workspace and have the resources treated as new resources to be created rather than imported.

> ![success](/docs/images/tick.svg)
> 
> This feature allows you to experiment with new resources in a development workspace and then promote them to a production workspace.

## Streamline import process with production deployment

For production environments, you can streamline the import and deployment process by integrating Rudder CLI with your CI/CD pipeline. This approach allows you to import resources once and then have your automated pipeline handle subsequent deployments.

### Workflow

  1. **Import resources** : Run the `import workspace` command to generate YAML files from your workspace resources.
  2. **Organize files** : Place the imported files in the correct locations within your project structure.
  3. **Commit to version control** : Commit the organized YAML files to your repository.
  4. **Automated deployment** : Your CI/CD pipeline automatically applies changes using the `rudder-cli apply` command.


#### CI/CD integration prerequisites

To apply changes automatically, your CI/CD pipeline must use a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) in the RudderStack dashboard with the following [permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) to manage Data Catalog and Tracking Plans:

Resource| Permissions  
---|---  
Tracking Plans| **Edit**  
Data Catalog| **Edit**  
  
  * **For testing or development purposes only** : Generate a [Personal Access Token](<https://www.rudderstack.com/docs/access-management/personal-access-tokens/>) with **Read-Write** role


> ![warning](/docs/images/warning.svg)
> 
> **RudderStack recommends using a workspace-level Service Access Token for authentication.**
> 
> Any action authenticated by a Personal Access Token will break if the user is removed from the organization or a breaking change is made to their permissions.

#### Token permissions for legacy RBAC system

If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), your workspace-level Service Access Token should have minimum **Editor** permissions.

See [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for more information on generating the token.

[![workspace-level Service Access Token with Editor permission](/docs/images/access-management/permissions/legacy/editor.webp)](</docs/images/access-management/permissions/legacy/editor.webp>)

### Benefits

  * **Automated deployments** : Changes are applied automatically through your CI/CD pipeline.
  * **Version control** : All resource changes are tracked in Git.
  * **Consistency** : You can ensure the same resources are deployed across different environments.
  * **Rollback capability** : Any changes are easy to revert by leveraging Git history.