# Event Stream Source Management using Rudder CLI Quickstart Alpha

Get started with creating and deploying an Event Stream source using the Rudder CLI tool.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __3 minute read

  * 


This quickstart guide shows you how to use the [Rudder CLI tool](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/>) to create and deploy an Event Stream source to your workspace.

## Prerequisites

  * Rudder CLI tool (`rudder-cli`) [installed locally](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/installation/>)
  * An existing [Tracking Plan](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/quickstart/>) defined in your CLI project (optional, but **recommended** for [Data Governance](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/>))
  * In your RudderStack workspace, create a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) with the following [permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) to manage Event Stream sources:

Resource| Permissions| Description  
---|---|---  
Event Stream Sources| **Create & Delete**| Create or delete Event Stream sources in the workspace  
Event Stream Sources| **Edit**|  Make changes to the configuration of Event Stream sources  
Event Stream Sources| **Connect**|  Connect an Event Stream source to a Tracking Plan  
Tracking Plans| **Edit** , **Connect**|  Connect a Tracking Plan to an Event Stream source  
  
**Click here to see how these permissions appear in the workspace policy**.  
![Permissions to manage Event Stream sources in RudderStack dashboard](/docs/images/access-management/rudder-cli-event-stream.webp)  


#### Token permissions for legacy RBAC system

If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), your workspace-level Service Access Token should have minimum **Admin** permissions.

See [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for more information on generating the token.

[![workspace-level Service Access Token with Admin permission](/docs/images/access-management/permissions/legacy/admin.webp)](</docs/images/access-management/permissions/legacy/admin.webp>)

## 1\. Authenticate the CLI tool

Run the following command and enter your access token when prompted:
    
    
    rudder-cli auth login
    

## 2\. Create a project directory

Create a project directory to store your source YAML files:
    
    
    mkdir ~/tutorial-sources
    

> ![info](/docs/images/info.svg)
> 
> If you are already managing Tracking Plans or Data Catalog resources via CLI, you can add source definitions to the same project directory. The CLI processes all YAML files in the directory recursively.

## 3\. Review the YAML reference

Before defining your Event Stream source, review the [Source YAML Reference](<https://www.rudderstack.com/docs/sources/event-streams/sdks/manage-sources-with-rudder-cli/source-yaml-reference/>) to understand:

  * The complete YAML structure for Event Stream sources
  * Required and optional fields for source configuration
  * Governance validation settings and violation rules
  * Reference syntax for linking sources to Tracking Plans


> ![success](/docs/images/tick.svg)
> 
> Understanding the YAML reference will help you create properly structured files and avoid common validation errors when defining your sources.

## 4\. Define an Event Stream source

Create a YAML file for your Event Stream source (`~/tutorial-sources/ios-source.yaml`):
    
    
    version: rudder/v0.1
    kind: event-stream-source
    metadata:
      name: ios-source
    spec:
      id: "my-ios-source"
      type: "ios"
      name: "iOS Source"
      enabled: true
    

This example creates a basic iOS source without governance configuration. The source accepts events and is enabled by default.

## 5\. Optional: Add governance configuration

If you want to associate a Tracking Plan with your source for data governance, update the YAML file to include governance settings:
    
    
    version: rudder/v0.1
    kind: event-stream-source
    metadata:
      name: ios-source
    spec:
      id: "my-ios-source"
      type: "ios"
      name: "iOS Source"
      enabled: true
      governance:
        validations:
          tracking_plan: "#/tp/my-tracking-plan/my-tracking-plan"
          config:
            track:
              propagate_violations: true
              drop_unplanned_events: true
              drop_unplanned_properties: true
              drop_other_violations: true
            identify:
              propagate_violations: true
              drop_unplanned_properties: true
              drop_other_violations: true
    

In this example:

  * The source is linked to a Tracking Plan referenced as `#/tp/my-tracking-plan/my-tracking-plan`.
  * For `track` events, violations are propagated, unplanned events are dropped, unplanned properties are dropped, and other violations are dropped.
  * For `identify` events, violations are propagated, unplanned properties are dropped, and other violations are dropped.


> ![info](/docs/images/info.svg)
> 
> The Tracking Plan reference follows the format `#/tp/[metadata.name]/[tracking-plan.id]`, where `metadata.name` is the `metadata.name` value in your Tracking Plan YAML file and `tracking-plan.id` is the `spec.id` value of the Tracking Plan.
> 
> See [Source YAML Reference](<https://www.rudderstack.com/docs/sources/event-streams/sdks/manage-sources-with-rudder-cli/source-yaml-reference/#governance-validation-properties>) for detailed information about these configuration options.

## 6\. Validate and deploy

  1. Validate your files:


    
    
    rudder-cli validate -l ~/tutorial-sources
    

  2. **Optional** : Review changes before deploying:


    
    
    rudder-cli apply -l ~/tutorial-sources --dry-run
    

  3. Deploy changes to your workspace:


    
    
    rudder-cli apply -l ~/tutorial-sources
    

## Supported sources

You can define Event Stream source YAMLs only client-side and server-side SDK sources.

> ![warning](/docs/images/warning.svg)
> 
> Rudder CLI does not support cloud apps and webhook sources currently.

**Click here to view the full list of sources**.  


**Web**

  * JavaScript


**Mobile**

  * Android
  * iOS
  * React Native
  * Flutter
  * Cordova
  * Unity


**Server**

  * Java
  * .NET
  * PHP
  * Rust
  * Python
  * Go
  * Node
  * Ruby
  * Unity


## Next steps

  * See the [Source YAML Reference](<https://www.rudderstack.com/docs/sources/event-streams/sdks/manage-sources-with-rudder-cli/source-yaml-reference/>) for detailed YAML definitions of Event Stream source resources.
  * See [CLI-based Tracking Plan Management](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/>) to create the Tracking Plans you reference in your source configurations.