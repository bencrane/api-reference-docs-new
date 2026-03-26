# Automate Project Management with Rudder CLI and GitHub Actions Alpha

Leverage GitHub Actions for automating management of your Rudder CLI projects.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __3 minute read

  * 


This guide explains how to validate and manage your Rudder CLI projects directly via GitHub workflows.

## Key features

By leveraging the [Rudder CLI Project Manager Action](<https://github.com/rudderlabs/rudder-cli-action>), you can:

  * Validate your Rudder CLI project files
  * Perform a dry run of any changes to your project files
  * Apply the changes to your RudderStack workspace


## Prerequisites

  * A GitHub repository containing your Tracking Plan YAML files


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

## Setup

Follow the steps in the below sections in the exact order to set up the GitHub Actions workflow.

### Step 1: Configure repository secrets

  1. In your GitHub repository, go to **Settings** > **Secrets and variables** > **Actions**.
  2. Add a new repository secret as follows:


  * **Name** : `RUDDERSTACK_ACCESS_TOKEN`
  * **Value** : The Service Access Token generated in the Prerequisites section


> ![warning](/docs/images/warning.svg)
> 
> RudderStack recommends storing this token in GitHub Secrets and referencing it in your workflow using `${{ secrets.YOUR_SECRET_NAME }}`.
> 
> **Do not expose the token directly in your workflow files**.

### Step 2: Create Actions workflow

Create the following workflow in your `.github/workflows/` directory:
    
    
    name: Manage Rudder CLI projects
    
    on:
      push:
        branches: [main]
      pull_request:
        branches: [main]
    
    jobs:
      validate:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - name: Validate Project Files
            uses: rudderlabs/rudder-cli-action@v1.0.1
            env:
              RUDDERSTACK_ACCESS_TOKEN: ${{ secrets.RUDDER_ACCESS_TOKEN }}
            with:
              location: "<path_to_root_project_folder>/"
              mode: "validate"
    
      apply:
        runs-on: ubuntu-latest
        needs: validate
        if: github.ref == 'refs/heads/main'
        steps:
          - uses: actions/checkout@v4
          - name: Apply Project Files
            uses: rudderlabs/rudder-cli-action@v1.0.1
            env:
              RUDDERSTACK_ACCESS_TOKEN: ${{ secrets.RUDDER_ACCESS_TOKEN }}
            with:
              location: "<path_to_root_project_folder>/" #Required
              mode: "apply" #Required
    

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * The previous Action `rudderlabs/rudder-tracking-plan-action@v1.0.0` is now deprecated.
>   * You can update the CLI action version by modifying the `uses` parameter in the workflow file — see the [Rudder CLI Project Manager Action releases](<https://github.com/rudderlabs/rudder-cli-action/releases>) for the latest version.
> 


Some of the key inputs are described below:

Input| Description| Default value  
---|---|---  
`location`  
Required| Path to the folder containing the Rudder CLI project files.| -  
`mode`  
Required| Operation mode — acceptable values are `validate`, `dry-run`, and `apply`.  
  
See Modes for more information.| -  
`cli_version`| Version of the Rudder CLI tool to use.| `v0.10.0`  
`RUDDERSTACK_ACCESS_TOKEN`  
Required| The access token for the RudderStack workspace.| -  
  
#### Modes

The `mode` parameter defines the operation mode of the GitHub Action. You can specify either of the following values:

Value| Notes  
---|---  
`validate`| 

  * Validates Tracking Plan syntax and structure.
  * No changes are applied to your configuration.

  
`dry-run`| 

  * Simulates the application of changes.
  * Shows what would be modified without actually making the changes.

  
`apply`| Applies the relevant changes to your RudderStack workspace.  
  
## How it works

This section explains the GitHub Actions workflow:

  * The action only triggers when files in your root project directory are modified.
  * The action automatically syncs the changes with RudderStack when you merge them with the `main` branch. It uses the `apply` mode (`mode: apply`) to push the relevant changes.