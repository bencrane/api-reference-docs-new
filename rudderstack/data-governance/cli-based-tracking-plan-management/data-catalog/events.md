# Manage Events using Rudder CLI Alpha

Define and manage events in your Data Catalog project using YAML configuration files.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __4 minute read

  * 


Events are the foundation of your tracking implementation in RudderStack. This guide shows you how to define and manage events in your Data Catalog using YAML configuration files.

## Event types

You can define the following event types in your Data Catalog project using Rudder CLI:

Event type| Description  
---|---  
Track| Record user actions and behaviors  
Identify| Capture user identification and associated traits  
Page| Track web page views  
Screen| Monitor mobile app screen views  
Group| Associate users with organizations  
  
## Define events

Using your preferred text editor, create a YAML file in your [Data Catalog project](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/project-setup/>) and add the below content:

### Basic structure

You can define events in YAML files with the `kind: events` specification. See [Data Catalog YAML Reference](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/project-yaml-reference/>) for the detailed YAML spec containing event definitions.
    
    
    version: rudder/v0.1
    kind: events
    metadata:
      name: myeventgroup
    spec:
      events:
        - id: product_viewed
          name: "Product Viewed"  // Only applicable for track events
          event_type: track
          description: "Triggered when a user views a product"
          category: "#/categories/event-categories/browsing_category" # Reference to the Browsing category
    

Each event definition requires:

  * A unique identifier (`id`)
  * The event type (`event_type`)
  * A descriptive name (`name`) (applicable **only** for `track` events)
  * Optional description (`description`)
  * Optional event category (`category`) — see [Manage Event Categories using Rudder CLI](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/events/categories/>) for more information.


> ![warning](/docs/images/warning.svg)
> 
> Do not include the `name` parameter for `identify`, `page`, or `group` events as they will not pass validation and result in an error.

The following snippets highlight the YAML definitions for different event types:
    
    
    - id: user_identify
      event_type: identify
      description: "Captures user profile information"
      category: "#/categories/event-categories/signup_category" # Reference to the Signup category
    
    
    
    spec:
      events:
        - id: checkout_completed
          name: "Checkout Completed"
          event_type: track
          description: "Triggered when a user completes the checkout process"
          category: "#/categories/event-categories/checkout_category" # Reference to the Checkout category
    
    
    
    - id: homepage_viewed
      event_type: page
      description: "Tracks homepage views"
      category: "#/categories/event-categories/browsing_category" # Reference to the Browsing category
    - id: settings_screen
      event_type: screen
      description: "Tracks settings screen views"
      category: "#/categories/event-categories/miscellaneous_category" # Reference to the Miscellaneous category
    
    
    
    - id: org_association
      event_type: group
      description: "Associates users with their organization"
      category: "#/categories/event-categories/association_category" # Reference to the Association category
    

### Event groups

You can group related events in a single YAML file based on business context (like ecommerce or user management) or other logical categories. Define each group with a unique `metadata.name` and list related events under `spec.events`.

> ![info](/docs/images/info.svg)
> 
> When defining event groups, ensure that:
> 
>   * Events in the same group share similar validation requirements.
>   * Related events that are often used together in Tracking Plans are grouped together.
>   * Each event group has a clear, specific purpose (for example, `ecommerce_events` for ecommerce-related tracking).
> 


The following examples show how to organize events into meaningful groups, along with their YAML definitions:
    
    
    version: rudder/v0.1
    kind: events
    metadata:
      name: ecommerce_events
    spec:
      events:
        - id: product_viewed
          name: "Product Viewed"
          event_type: track
          description: "Triggered when a user views a product"
          category: "#/categories/event-categories/browsing_category"
        
        - id: add_to_cart
          name: "Add to Cart"
          event_type: track
          description: "Triggered when a user adds a product to cart"
        
        - id: checkout_started
          name: "Checkout Started"
          event_type: track
          description: "Triggered when a user starts checkout"
    
    
    
    version: rudder/v0.1
    kind: events
    metadata:
      name: user_events
    spec:
      events:
        - id: user_registered
          name: "User Registered"
          event_type: track
          description: "Triggered when a new user registers"
          category: "#/categories/event-categories/signup_category"
        
        - id: user_login
          name: "User Login"
          event_type: track
          description: "Triggered when a user logs in"
    
        - id: profile_updated
          name: "Profile Updated"
          event_type: track
          description: "Triggered when a user updates their profile"
          category: "#/categories/event-categories/miscellaneous_category"
    

### Best practices

Follow these best practices when defining events and event groups:

  * **Naming conventions**

    * Use clear, descriptive names
    * Follow consistent capitalization
    * Avoid special characters
  * **Organization**

    * Use event groups to group related events together
    * Use meaningful names that reflect the group’s purpose
  * **Validation**

    * Use unique identifiers
    * Validate event definitions
    * Test before deployment
  * **Avoid resource duplication**

    * Do not define the same event in multiple event YAML files. Each event should exist in only one file to prevent duplication and potential confusion.


## Validate and deploy events

Before deploying your events to the workspace, validate them to ensure they follow the correct structure and meet your requirements.

### Validate events

Run the following command to validate your event definitions:
    
    
    rudder-cli validate -l ~/tutorial-catalog
    

The command checks your event definitions for:

  * Required fields and correct structure
  * Valid event types and property references
  * Unique identifiers across your catalog
  * Proper YAML syntax


If validation succeeds, the command returns no output. If it finds any issues, it displays specific error messages to help you fix them.

### Deploy events

After validating your events, deploy them to your RudderStack workspace:

  1. Review the changes before deploying:


    
    
    rudder-cli apply -l ~/tutorial-catalog --dry-run
    

  2. Deploy the validated events:


    
    
    rudder-cli apply -l ~/tutorial-catalog
    

The above command:

  * Creates new events in your workspace
  * Updates existing events if you’ve modified them
  * Reports the status of each operation
  * Requires confirmation before making changes (unless you use `--confirm=false`)


> ![info](/docs/images/info.svg)
> 
> See the [End-to-end Walkthrough](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/walkthrough/>) for steps on validating and deploying properties along with other Data Catalog resources.

## Next steps

  * Define [properties](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/properties/>) for your events
  * Create [custom types](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/custom-types/>) for validation
  * Build [Tracking Plans](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/tracking-plans/>) using your events and properties
  * Automate changes to Tracking Plans by leveraging [CLI-based workflows](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/github-actions/>)