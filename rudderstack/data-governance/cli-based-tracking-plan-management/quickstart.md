# CLI-based Tracking Plan Management Quickstart Alpha

Get started with creating and deploying a Tracking Plan using the Rudder CLI tool.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __4 minute read

  * 


This quickstart guide shows you how to use the [Rudder CLI tool](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/>) to create and deploy a Tracking Plan to your workspace.

> ![info](/docs/images/info.svg)
> 
> See [End-to-End Walkthrough](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/walkthrough/>) for a detailed, step-by-step walkthrough of this feature.

## Prerequisites

  * Rudder CLI tool (`rudder-cli`) [installed locally](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/installation/>)


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

## 1\. Authenticate the CLI tool

Run the following command and enter your Service Access Token when prompted:
    
    
    rudder-cli auth login
    

## 2\. Create a project directory

Create a project directory to store your Data Catalog YAML files:
    
    
    mkdir ~/tutorial-catalog
    

## 3\. Review the YAML reference

Before defining your Data Catalog resources, review the [Project YAML Reference](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/project-yaml-reference/>) to understand:

  * The complete YAML structure for events, properties, custom types, and Tracking Plans
  * Required and optional fields for each resource type
  * Validation rules and constraints
  * Reference syntax for linking resources together


> ![success](/docs/images/tick.svg)
> 
> Understanding the YAML reference will help you create properly structured files and avoid common validation errors when defining your resources.

## 4\. Define events, properties, and custom types

Create the following YAML files in your project directory:

  * **Events (`~/tutorial-catalog/events.yaml`)**


    
    
    version: rudder/v0.1
    kind: events
    metadata:
      name: myevents
    spec:
      events:
        - id: product_viewed
          name: "Product Viewed"
          event_type: track
          description: "Triggered when a user views a product"
          category: "#/categories/event-categories/browsing_category" # Reference to the Browsing category (see below)
        - id: user_identify
          event_type: identify
          description: "Captures user profile information"
          category: "#/categories/event-categories/signup_category"
        - id: homepage_viewed
          event_type: page
          description: "Tracks homepage views"
          category: "#/categories/event-categories/browsing_category"
    

  * **Event categories (`~/tutorial-catalog/event-categories.yaml`)**


    
    
    version: rudder/v0.1
    kind: categories
    metadata:
      name: event-categories
    spec:
      categories:
        - id: browsing_category
          name: Browsing
        - id: signup_category
          name: Signup
    

  * **Properties (`~/tutorial-catalog/properties.yaml`)**


    
    
    version: rudder/v0.1
    kind: properties
    metadata:
      name: myproperties
    spec:
      properties:
        - id: product_sku
          name: "SKU"
          type: string
          description: "Product SKU"
        - id: price
          name: "Price"
          type: integer
          description: "Product price"
        - id: email
          name: "Email"
          type: string
          description: "User's email address"
        - id: first_name
          name: "First Name"
          type: string
          description: "User's first name"
        - id: last_name
          name: "Last Name"
          type: string
          description: "User's last name"
        - id: page_url
          name: "Page URL"
          type: string
          description: "URL of the viewed page"
        - id: referrer
          name: "Referrer"
          type: string
          description: "Page referrer URL"
    

> ![info](/docs/images/info.svg)
> 
> See [Nested properties](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/tracking-plans/create/#nested-properties>) for more information on defining and using nested properties in your Tracking Plans.

  * **Custom Types (`~/tutorial-catalog/custom-types.yaml`)**


    
    
    version: rudder/v0.1
    kind: custom-types
    metadata:
      name: identifier-types
    spec:
      types:
        - id: sku_type
          name: "SKUType"
          description: "Custom type for SKU validation"
          type: string
          config:       # Validation rules for the custom data type
            minLength: 5
            maxLength: 255
            pattern: "^SKU-[0-9]+$"
    
    
    
    version: rudder/v0.1
    kind: properties
    metadata:
      name: myproperties
    spec:
      properties:
        - id: product_sku
          name: "SKU"
          type: "#/custom-types/identifier-types/sku_type" # Reference to custom type
          description: "Product SKU"
    

> ![success](/docs/images/tick.svg)
> 
> You can also define [Custom Type Variants](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/custom-types/>) in your custom type definitions that define different property requirements for reusable object types based on a discriminating property value.

## 5\. Create a Tracking Plan

Create a Tracking Plan that references your events and properties (`~/tutorial-catalog/tracking-plan.yaml`):
    
    
    version: rudder/v0.1
    kind: tp
    metadata:
      name: ecomm-tracking-plan
    spec:
      id: ecomm-tracking-plan
      display_name: "Product Tracking Plan"
      description: "Tracking plan for product-related events"
      rules:
        - type: event_rule
          id: product_viewed_rule
          event:
            $ref: "#/events/myevents/product_viewed"
          allow_unplanned: false
          properties:
            - $ref: "#/properties/myproperties/product_sku"
              required: true
            - $ref: "#/properties/myproperties/price"
              required: true
            - $ref: "#/properties/myproperties/user_profile" # Nested property of object type
              properties:
                - $ref: "#/properties/myproperties/user_profile/personal_info/first_name"
                - $ref: "#/properties/myproperties/user_profile/personal_info/last_name"
    
    
    
    version: rudder/v0.1
    kind: tp
    metadata:
      name: user-tracking-plan
    spec:
      id: user-tracking-plan
      display_name: "User Tracking Plan"
      description: "Tracking plan for user identification and page view events"
      rules:
        - type: event_rule
          id: user_identify_rule
          event:
            $ref: "#/events/myevents/user_identify"
            allow_unplanned: false
            identity_section: "traits"  # Properties go in traits section
          properties:
            - $ref: "#/properties/myproperties/email"
              required: true
            - $ref: "#/properties/myproperties/first_name"
              required: true
            - $ref: "#/properties/myproperties/last_name"
              required: false
        - type: event_rule
          id: homepage_viewed_rule
          event:
            $ref: "#/events/myevents/homepage_viewed"
            allow_unplanned: true
            identity_section: "context.traits"  # Properties go in context.traits section
          properties:
            - $ref: "#/properties/myproperties/page_url"
              required: true
            - $ref: "#/properties/myproperties/referrer"
              required: false
    

> ![success](/docs/images/tick.svg)
> 
> You can also define [Event Rule Variants](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/event-rule/>) in your Tracking Plan that define dynamic event validation rules that adapt based on context.

## 6\. Validate and deploy

  1. Validate your files:


    
    
    rudder-cli validate -l ~/tutorial-catalog
    

  2. **Optional** : Review changes before deploying:


    
    
    rudder-cli apply -l ~/tutorial-catalog --dry-run
    

  3. Deploy changes to your workspace:


    
    
    rudder-cli apply -l ~/tutorial-catalog
    

## Next steps

  * See the [Data Catalog YAML Reference](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/project-yaml-reference/>) for detailed YAML definitions of the various Data Catalog resources.
  * Use [Custom Data Types](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/custom-types/>) to define reusable data validation patterns that can be referenced across multiple properties in your Tracking Plans.
  * See the [End-to-End Walkthrough](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/walkthrough/>) for detailed explanation of the above steps.