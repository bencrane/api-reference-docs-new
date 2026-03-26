# Manage Tracking Plans using Rudder CLI Alpha

Define and manage Tracking Plans as YAML configurations using the Rudder CLI tool.

* * *

  * __2 minute read

  * 


This section explains how to define and manage Tracking Plans in your Data Catalog project using Rudder CLI.

> ![info](/docs/images/info.svg)
> 
> **Important**
> 
> Tracking Plan management via Rudder CLI is a push-only feature, meaning you can only push changes to your RudderStack workspace. You cannot pull changes from your workspace to your local system.

## Overview

Tracking Plans help you maintain consistent event tracking across your applications by defining which events to track, what properties to include, and how to validate the data. They serve as a contract between different teams in your organization and allows them to:

  * Enforce consistent event tracking across all platforms
  * Ensure required properties are always included
  * Validate incoming data against expected formats and rules
  * Track changes through version control
  * Maintain alignment between the Tracking Plan specification and its implementation


## How it works

Rudder CLI lets you manage Tracking Plans through YAML configuration files in your Data Catalog project. Each Tracking Plan defines:

  * [Events](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/events/>) to track from your Data Catalog project
  * [Properties](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/properties/>) associated with each event
  * References to [Custom Types](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/custom-types/>) for advanced validation
  * Validation rules for data quality


You can then use Rudder CLI to:

  * Validate Tracking Plan definitions
  * Deploy plans to your workspace
  * Update existing plans
  * Manage changes through version control


## In this section

See the following guides to learn how to create, update, and deploy Tracking Plans to your workspace using Rudder CLI:

Topic| Description  
---|---  
[Create a Tracking Plan](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/tracking-plans/create/>)| Learn how to define and deploy your first Tracking Plan using Rudder CLI.  
[Update a Tracking Plan](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/tracking-plans/update/>)| Update existing Tracking Plans and manage changes.  
  
See the [End-to-end Walkthrough](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/walkthrough/>) for a complete example of creating and managing Tracking Plans from scratch.