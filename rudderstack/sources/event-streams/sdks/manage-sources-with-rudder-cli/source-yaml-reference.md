# Event Stream Source YAML Reference Alpha

Complete reference for defining Event Stream sources using YAML configuration files.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __5 minute read

  * 


This guide serves as a detailed reference for the CLI project YAML files that contain definitions of your Event Stream source resources.

## Overview

In the context of the Rudder CLI (`rudder-cli`) tool, you can define Event Stream sources as YAML files within your project directory. The location and naming of these YAML files is flexible, as you can store the YAML files anywhere within the project’s root directory or subdirectories.

> ![info](/docs/images/info.svg)
> 
> The Rudder CLI tool processes all valid YAML files within the project structure to recognize the defined resources.

## Event Stream Sources

You can define an Event Stream source in the YAML file by setting `kind` to `event-stream-source`.

The `spec` parameter of the YAML file has the following structure:

Property| Type| Description  
---|---|---  
`id`  
Required| String| Unique identifier for the source within the project. This parameter must be unique across all sources in the project.  
`type`  
Required| String| Source type identifier. See Supported source types for the list of acceptable values.  
`name`  
Required| String| Name for the source. It must be non-empty.  
`enabled`| Boolean| Determines whether this source is accepting events.  
  
**Default value** : `true`  
`governance`| Data governance configuration object| Contains data governance-related settings for the source.  
  
### Data governance configuration

The `governance` object contains validation settings that control how the source handles any Tracking Plan violations:

Property| Type| Description  
---|---|---  
`validations`  
Required| Validation properties object| Contains validation configuration including Tracking Plan reference and violation rules.  
  
### Validation properties

The `validations` object contains the Tracking Plan reference and violation handling rules:

Property| Type| Description  
---|---|---  
`tracking_plan`  
Required| String| Reference to a Tracking Plan resource — the format is `#/tp/[metadata.name]/[tracking-plan.id]`, where `metadata.name` is the `metadata.name` value in your Tracking Plan YAML file and `tracking-plan.id` is the `spec.id` value of the Tracking Plan resource.  
`config`| Violation rules configuration object| Contains violation rules for all event types. If not specified, default violation rules apply to all event types.  
  
> ![info](/docs/images/info.svg)
> 
> You must have a [Tracking Plan defined in your CLI project](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/tracking-plans/>) before you can reference it in a source configuration.
> 
> See [CLI-based Tracking Plan Management](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/tracking-plans/create/>) for more information on creating Tracking Plans.

### Violation rules configuration

The `config` object contains violation handling rules for different event types. Each event type configuration is optional; if not specified, default violation rules apply:

Property| Type| Description  
---|---|---  
`track`| Violation rules object| Violation rules for `track` events.  
`identify`| Violation rules object| Violation rules for `identify` events.  
`group`| Violation rules object| Violation rules for `group` events.  
`page`| Violation rules object| Violation rules for `page` events.  
`screen`| Violation rules object| Violation rules for `screen` events.  
  
### Violation rules properties

Each violation rules object contains the following properties:

Property| Type| Description  
---|---|---  
`propagate_violations`| Boolean| Determines whether to add violations in event context. When enabled, violation information is included in the event payload’s context for downstream processing.  
  
**Default value** : `true`  
`drop_unplanned_events`| Boolean| **Only applies to`track` configuration.** Determines whether to drop events without a corresponding rule in the associated Tracking Plan.  
  
**Default value** : `false`  
`drop_unplanned_properties`| Boolean| Determines whether to drop properties that are not defined in the Tracking Plan for the event.  
  
**Default value** : `false`  
`drop_other_violations`| Boolean| Determines whether to drop events with any other validation violations.  
  
**Default value** : `false`  
  
> ![warning](/docs/images/warning.svg)
> 
> If you set `drop_unplanned_events`, `drop_unplanned_properties`, or `drop_other_violations` to `true`, events that violate these rules are dropped and not forwarded to destinations.
> 
> Make sure you understand the impact of these settings before deploying your source configuration.

## Supported source types

The following table lists all supported source types and their corresponding `type` values:

Source| `type` value  
---|---  
Java| `java`  
.NET| `dotnet`  
PHP| `php`  
Flutter| `flutter`  
Cordova| `cordova`  
Rust| `rust`  
React Native| `react_native`  
Python| `python`  
iOS| `ios`  
Android| `android`  
JavaScript| `javascript`  
Go| `go`  
Node| `node`  
Ruby| `ruby`  
Unity| `unity`  
  
## Examples

#### Basic source configuration

This example shows a minimal source configuration without governance settings:
    
    
    version: rudder/v0.1
    kind: event-stream-source
    metadata:
      name: ios-source
    spec:
      id: "my-ios-source"
      type: "ios"
      name: "iOS Source"
      enabled: true
    

#### Source with governance configuration

This example shows a source with governance configuration that links to a Tracking Plan and defines violation rules for different event types:
    
    
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
          tracking_plan: "#/tp/my-tracking-plan/ecommerce-tracking-plan"
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
            group:
              propagate_violations: true
              drop_unplanned_properties: true
              drop_other_violations: true
            page:
              propagate_violations: true
              drop_unplanned_properties: true
              drop_other_violations: true
            screen:
              propagate_violations: true
              drop_unplanned_properties: true
              drop_other_violations: true
    

#### Source with partial governance configuration

This example shows a source that only defines violation rules for `track` events, letting other event types use default rules:
    
    
    version: rudder/v0.1
    kind: event-stream-source
    metadata:
      name: web-source
    spec:
      id: "my-web-source"
      type: "javascript"
      name: "Web Source"
      enabled: true
      governance:
        validations:
          tracking_plan: "#/tp/web-tracking-plan/web-tracking-plan"
          config:
            track:
              propagate_violations: false
              drop_unplanned_events: false
              drop_unplanned_properties: false
              drop_other_violations: false
    

#### Disabled source

This example shows a source that is disabled and does not accept events:
    
    
    version: rudder/v0.1
    kind: event-stream-source
    metadata:
      name: test-source
    spec:
      id: "test-source"
      type: "python"
      name: "Test Source"
      enabled: false
    

## Reference Tracking Plans

When configuring data governance validation, you can reference [Tracking Plans](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/tracking-plans/>) using the following format:
    
    
    tracking_plan: "#/tp/[metadata.name]/[tracking-plan.id]"
    

Where:

  * `metadata.name` is the `metadata.name` value in your Tracking Plan YAML file
  * `tracking-plan.id` is the `spec.id` value of the Tracking Plan


For example, if your Tracking Plan YAML file looks like this:
    
    
    version: rudder/v0.1
    kind: tp
    metadata:
      name: ecommerce-tracking-plan
    spec:
      id: product-tracking-plan
      display_name: "Product Tracking Plan"
      # ... rest of the configuration
    

You would reference it in your source configuration as:
    
    
    tracking_plan: "#/tp/ecommerce-tracking-plan/product-tracking-plan"
    

> ![info](/docs/images/info.svg)
> 
> References must always start with a `#` character followed by the path using the `/` delimiter. The path points to a unique Tracking Plan resource within a project’s file and uses the `kind` value (`tp`), `metadata.name` value, and `spec.id` value to create the reference.

## See more

  * See [Event Stream Sources Quickstart](<https://www.rudderstack.com/docs/sources/event-streams/sdks/manage-sources-with-rudder-cli/quickstart/>) for a quick guide to creating your first Event Streamsource.
  * See [CLI-based Tracking Plan Management](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/tracking-plans/>) to create the Tracking Plans that you can reference in your Event Stream source configurations.
  * See [Tracking Plan YAML Reference](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/project-yaml-reference/#tracking-plans>) for information about Tracking Plan YAML structure.