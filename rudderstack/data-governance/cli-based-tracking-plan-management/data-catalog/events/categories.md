# Manage Event Categories using Rudder CLI Alpha

Define and manage event categories in your Data Catalog project using YAML configuration files.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __4 minute read

  * 


Event categories help you organize and classify events in your RudderStack Data Catalog based on business context, functionality, or any other logical classification system. This guide shows you how to define event categories and associate them with events using YAML configuration files.

## Overview

In the RudderStack dashboard, you can use the [Data Catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>) to:

  * Define custom categories for your events
  * Assign predefined categories to your events

[![Event categories in the RudderStack dashboard](/docs/images/data-governance/event-categories.webp)](</docs/images/data-governance/event-categories.webp>)

You can also use Rudder CLI to define event categories as YAML configuration files in your [Data Catalog project](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/project-setup/>) and reference them in your event definitions.

## Define event categories

Using your preferred text editor, create a YAML file in your [Data Catalog project](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/project-setup/>) and add the below content:

### Basic structure

You can define event categories in YAML files with the `kind: categories` specification.See [Data Catalog YAML Reference](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/project-yaml-reference/>) for the detailed YAML spec containing event definitions.
    
    
    version: rudder/v0.1
    kind: categories
    metadata:
      name: event-categories
    spec:
      categories:
        - id: signup_category
          name: Signup
        - id: login_category
          name: Login
        - id: browsing_category
          name: Browsing
        - id: miscellaneous_category
          name: Miscellaneous
    

Each event category definition requires:

  * A unique identifier (`id`)
  * A descriptive name (`name`)


### Best practices

Follow these best practices when defining event categories:

  * **Naming conventions**

    * Use clear, descriptive category names that reflect their purpose
    * Follow consistent capitalization (for example, `Marketing` instead of `marketing`)
    * Keep names concise but meaningful
  * **Organization**

    * Create categories that align with your business objectives
    * Consider your team’s workflow and how events will be used
    * Avoid creating too many categories that could complicate organization
  * **Uniqueness**

    * Ensure each category has a unique identifier
    * Avoid duplicate category names within the same configuration
    * Use descriptive IDs that relate to the category name (for example, `marketing_category` for “Marketing”)


## Reference categories in events

Once you’ve defined your categories, you can associate them with events in your event definitions.

> ![warning](/docs/images/warning.svg)
> 
> Each event can have only one category assigned to it. See Limitations for the other key points to consider while referencing categories in events.

To reference a category in an event definition, use the `category` field with a `$ref` pointer to your category:
    
    
    version: rudder/v0.1
    kind: events
    metadata:
      name: categorized-events
    spec:
      events:
        - id: product_viewed
          event_type: track
          name: "Product Viewed"
          category: "#/categories/event-categories/browsing_category"
        
        - id: signup_completed
          event_type: track
          name: "Signup Completed"
          category: "#/categories/event-categories/signup_category"
    

The `$ref` format follows the below syntax:
    
    
    "#/categories/{categories-metadata-name}/{category-id}"
    

Where:

  * `categories-metadata-name` is the name specified in your categories file’s metadata.
  * `category-id` is the unique identifier of the specific category.


## Validate and deploy event categories

Before deploying your event categories to the workspace, validate them to ensure they follow the correct structure and meet your requirements.

### Validate categories

Run the following command to validate your category definitions and event associations:
    
    
    rudder-cli validate -l ~/tutorial-catalog
    

The command checks your category definitions for:

  * Required fields and correct structure
  * Unique category identifiers and names
  * Valid category references in event definitions
  * Proper YAML syntax and formatting
  * No duplicate categories within the same configuration


If validation succeeds, the command returns no output. If it finds any issues, it displays specific error messages to help you fix them.

### Deploy categories

After validating your categories and events, deploy them to your RudderStack workspace:

  1. Review the changes before deploying:


    
    
    rudder-cli apply -l ~/tutorial-catalog --dry-run
    

  2. Deploy the validated categories:


    
    
    rudder-cli apply -l ~/tutorial-catalog
    

The above command:

  * Creates new categories in your workspace
  * Updates existing categories if you’ve modified them
  * Associates events with their specified categories
  * Reports the status of each operation
  * Requires confirmation before making changes (unless you use `--confirm=false`)


> ![info](/docs/images/info.svg)
> 
> Categories are applied alongside other Data Catalog resources. When you deploy, both your categories and the events that reference them will be updated in your workspace.

See the [End-to-end Walkthrough](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/walkthrough/>) for steps on validating and deploying event categories along with other Data Catalog resources.

## Limitations

The current Rudder CLI implementation of event categories has the following limitations:

  * **Event-only support** : Categories can only be assigned to events. Other Data Catalog assets like properties or custom types do not support categories in this version.
  * **Single category per event** : Each event can be assigned to only one category. Multiple categories per event are not supported.
  * **No duplicate categories** : You cannot create duplicate categories with the same name, regardless of whether they are defined within the same configuration file or across different configuration files.


## Next steps

  * Create [events](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/events/>) and reference the event categories in them
  * Define [properties](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/properties/>) for your categorized events
  * Build [Tracking Plans](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/tracking-plans/>) using your categorized events
  * Explore the [Data Catalog YAML Reference](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/project-yaml-reference/>) for advanced configuration options
  * Automate changes to categories and events by leveraging [CLI-based workflows](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/github-actions/>)