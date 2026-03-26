# CLI Project Resources YAML Reference Alpha

Complete reference for defining your Data Catalog and Tracking Plan resources using YAML configuration files.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __10 minute read

  * 


This guide serves as a detailed reference for the CLI project YAML files that contain definitions of your Data Catalog and Tracking Plan resources.

## Overview

In the context of the Rudder CLI (`rudder-cli`) tool, a project typically consists of a root directory that contains all the project files. Within this root directory, each YAML file can contain definitions for resources of a particular type, for example, events, properties, custom data types, and Tracking Plans.

The location and naming of these YAML files is flexible, as you can store the YAML files anywhere within the project’s root directory or subdirectories.

You can also group some resources of the same type in the same file, allowing structures that can best serve your project’s requirements. For example, you could have:

  * A `events.yaml` file in the project’s root directory that defines multiple events.
  * Another file `subdirectory/user-events.yaml` that defines addtional events.


> ![info](/docs/images/info.svg)
> 
> The Rudder CLI tool processes all valid YAML files within the project structure to recognize the defined resources.

The following sections detail the specific YAML formats and parameter definitions for each resource type.

## Events

You can define one or more events in the YAML file by setting `kind` to `events`.

The `spec` parameter of the YAML file has the following structure:

Property| Type| Description  
---|---|---  
`events`  
Required| Array of event definitions| An array of event definitions grouped together in the same file.  
  
### Event definition

The event definitions have a structure that depends on the event type. All definitions share some common properties, as listed in the below table:

Property| Type| Description  
---|---|---  
`id`  
Required| String| Unique identifier for the event within the project. This parameter must be unique across all events.  
`event_type`  
Required| String| Event type. Acceptable values are `track`, `identify`, `page`, `screen`, and `group`.  
`description`| String| Event description.  
`category`| String| Reference to an existing event category.  
  
See [Manage Event Categories using Rudder CLI](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/events/categories/>) for more information.  
  
Additionally, `track` events (`event_type: track`) also support the following property:

Property| Type| Description  
---|---|---  
`name`  
Required| String| The `track` event name. In other words, this parameter corresponds to the `event` property of the corresponding RudderStack `track` event.  
  
### Example
    
    
    version: rudder/v0.1
    kind: events
    metadata:
      name: myeventgroup
    spec:
      events:
        - id: product_viewed
          name: "Product Viewed"
          event_type: track
          description: "This event is triggered every time a user views a product."
          category: "#/categories/event-categories/browsing_category" # Reference to the Browsing category
        - id: added_to_cart
          name: "Added To Cart"
          event_type: track
          description: "This event is triggered every time the user adds a product to their cart."
        - id: identify
          event_type: identify
          description: "An event that identifies the user."
        - id: page
          event_type: page
    

## Event categories

You can define event categories in the YAML file by setting `kind` to `categories`.

The `spec` parameter of the YAML file has the following structure:

Property| Type| Description  
---|---|---  
`categories`  
Required| Array of category definitions| An array of category definitions grouped together in the same file.  
  
### Category definition

All category definitions share the following properties:

Property| Type| Description  
---|---|---  
`id`  
Required| String| Unique identifier for the category within the project. This parameter must be unique across all categories in all the YAML files within the project.  
`name`  
Required| String| Display name of the category.  
  
### Example
    
    
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
    

## Properties

You can define one or more properties in the YAML file by setting `kind` to `properties`.

The `spec` parameter of the YAML file has the following structure:

Property| Type| Description  
---|---|---  
`properties`  
Required| Array of property definitions| An array of property definitions grouped together in the same file.  
  
### Property definition

A property definition has the following structure:

Property| Type| Description  
---|---|---  
`id`  
Required| String| Unique identifier for the property within the project. This parameter must be unique across all properties in all the YAML files within the project.  
`name`  
Required| String| This parameter corresponds to the field inside an event’s `properties` or `traits` JSON.  
`type`  
Required| String| Property type.  
  
Acceptable values are: `string`, `integer`, `number`, `object`, `array`, `boolean`, and `null`.  
`description`| String| Property description.  
`propConfig`| `propConfig` object| Additional validation rules for the property’s values.  
  
#### Property config

Property| Type| Description  
---|---|---  
`minLength`| Integer| Minimum length of the property’s string value.  
`maxLength`| Integer| Maximum length of the property’s string value.  
`pattern`| String| Regular expression that the property’s string values need to match with.  
`enum`| Array of strings| List of all valid values for the property.  
  
### Example
    
    
    version: rudder/v0.1
    kind: properties
    metadata:
      name: ecommerce_properties
    spec:
      properties:
        - id: product_id
          name: "product_id"
          type: string
          description: "Unique identifier for the product."
          propConfig:
            minLength: 3
            maxLength: 64
        - id: product_name
          name: "product_name"
          type: string
          description: "Name of the product."
          propConfig:
            minLength: 2
            maxLength: 255
        - id: product_price
          name: "product_price"
          type: number
          description: "Price of the product in the store's currency."
        - id: product_category
          name: "product_category"
          type: string
          description: "Category the product belongs to."
          propConfig:
            enum:
            - "clothing"
            - "electronics"
            - "home_goods"
            - "beauty"
            - "accessories"
            maxLength: 60
        - id: cart_items
          name: "cart_items"
          description: "Items present in the cart."
          type: array
          propConfig:
            minItems: 1
            uniqueItems: false
    

## Custom data types

You can define custom data types in the YAML file by setting `kind` to `custom-types`.

The `spec` parameter of the YAML file has the following structure:

Property| Type| Description  
---|---|---  
`types`  
Required| Array of custom type definitions| An array of custom type objects grouped together in the same file.  
  
### Custom type definition

Property| Type| Description  
---|---|---  
`id`  
Required| String| Unique identifier for the custom type within the project. This parameter must be unique across all custom types in all the YAML files within the project.  
`name`  
Required| String| Display name of the custom type.  
`type`  
Required| String| Base data type for the custom type.  
  
Acceptable values are: `string`, `integer`, `number`, `object`, `array`, `boolean`.  
`config`  
Required| `config` object| Validation rules for the custom type. The configuration options vary depending on the `type` parameter.  
`description`| String| Description of the custom type.  
  
#### `config` options

The `config` object’s configuration varies depending on the `type` parameter.

Parameter| Description  
---|---  
`minLength`| Minimum string length  
`maxLength`| Maximum string length  
`pattern`| Regular expression pattern  
`format`| Predefined format like email, date, etc.  
`enum`| Array of allowed values  
  
Parameter| Description  
---|---  
`minimum`| Minimum value  
`maximum`| Maximum value  
`exclusiveMinimum`| Exclusive minimum value  
`exclusiveMaximum`| Exclusive maximum value  
`multipleOf`| Multiple of value  
  
Parameter| Description  
---|---  
`itemTypes`| List of acceptable types for array items  
`minItems`| Minimum number of items  
`maxItems`| Maximum number of items  
`uniqueItems`| Boolean requiring uniqueness of items  
  
### Example
    
    
    version: rudder/v0.1
    kind: custom-types
    metadata:
      name: email-types
    spec:
      types:
        - id: emailtype
          name: "EmailType"
          description: "Custom type for email validation"
          type: string
          config:
            format: "email"
            minLength: 5
            maxLength: 255
            pattern: "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
        - id: addresstype
          name: "AddressType"
          description: "Physical address information"
          type: object
          properties:
            - id: street
              type: string
              required: true
            - id: city
              type: string
              required: true
            - id: country
              type: string
              required: false
    

## Tracking Plans

You can define a Tracking Plan in the YAML file by setting `kind` to `tp`.

The `spec` parameter of the YAML file has the following structure:

Property| Type| Description  
---|---|---  
`id`  
Required| String| Unique identifier for the Tracking Plan within the project. This parameter must be unique across all the Tracking Plans in the project.  
`display_name`  
Required| String| A readable short name for the Tracking Plan.  
`description`| String| Tracking plan description.  
`rules`  
Required| Array of rules definitions| Contains the list of events in the Tracking Plan along with the rules for their expected properties.  
  
### Rules definition

Property| Type| Description  
---|---|---  
`type`  
Required| String| The rule type. The only acceptable value currently is `event_rule`.  
`id`  
Required| String| Rule ID.  
`event`  
Required| Rule event definition object| Event definition associated with the rule along with the validation rules for the Tracking Plan.  
`properties`  
Required| Array of rule property definitions| List of properties associated with the rule’s event along with the validation rules for the Tracking Plan.  
  
#### Rule event definition

Property| Type| Description  
---|---|---  
`$ref`  
Required| String| Reference to an existing event definition. See Reference catalog resources for more information on how to work with references.  
`allow_unplanned`| Boolean| Validation rule that checks if the event can have properties other than those defined in the rule’s `properties` section.  
  
**Default value** : `false`  
`identity_section`  
Required, for non-track events| String| Defines in which field of the corresponding RudderStack event payload the rule’s properties should be included.  
  
Acceptable values are: `properties`, `traits`, and `context.traits`.  
  
#### Rule property definition

Property| Type| Description  
---|---|---  
`$ref`  
Required| String| Reference to an existing property definition.  
  
See Reference catalog resources for more information on how to work with references.  
`required`| Boolean| Validation rule that determines whether the property should always be present in the RudderStack event.  
  
**Default value** : `false`  
`properties`  
Applicable only for properties of `object` type| Array of rule property definitions| Defines which [nested properties](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/tracking-plans/create/#nested-properties>) should be included when this property is used in the Tracking Plan.  
  
### Example
    
    
    version: rudder/v0.1
    kind: tp
    metadata:
      name: ecommerce_tracking_plan
    spec:
      id: ecommerce_tracking_plan
      display_name: "E-commerce Tracking Plan"
      description: "Tracking plan for an e-commerce application."
      rules:
        - type: event_rule
          id: product_viewed_rule
          event:
            $ref: "#/events/myeventgroup/product_viewed"
            allow_unplanned: false
          properties:
            - $ref: "#/properties/ecommerce_properties/product_id"
              required: true
            - $ref: "#/properties/ecommerce_properties/product_name"
              required: true
            - $ref: "#/properties/ecommerce_properties/product_price"
              required: true
            - $ref: "#/properties/ecommerce_properties/product_category"
              required: false
        - type: event_rule
          id: user_registered_rule
          event:
            $ref: "#/events/myeventgroup/user_registered"
            allow_unplanned: false
          properties:
            - $ref: "#/properties/ecommerce_properties/user_profile"  # Object property
              required: true
              properties:
                - $ref: "#/properties/ecommerce_properties/personal_info"  # Object property
                  required: true
                  properties:
                    - $ref: "#/properties/ecommerce_properties/first_name"
                      required: true
                    - $ref: "#/properties/ecommerce_properties/last_name"
                      required: true
                    - $ref: "#/properties/ecommerce_properties/contact"  # Object property
                      required: true
                      properties:  # Deepest nesting level in this example
                        - $ref: "#/properties/ecommerce_properties/email"
                          required: true
                        - $ref: "#/properties/ecommerce_properties/phone"
                          required: false
    

## Reference Catalog resources

Definitions in a YAML file can refer to definitions in other files by using the resource reference (`$ref`) strings — this is useful while defining resources like Tracking Plans which need to be associated with events and properties defined in other files.

Note that references must always start with a `#` character followed by the path using the `/` delimiter. The path can point to a unique resource within a project’s file and is expected to have the following components in order:

  * `kind` value of the target resource’s file, that is, `events`, `properties`, or `tp`.
  * `metadata.name` value of the target resource’s file.
  * `id` value of the target resource.


For example, you can refer an event inside a file with `metadata.name` set to `examples` and having `id` as `example_id` as follows:
    
    
    - $ref: "#/events/examples/example_id"
    

## Import metadata

When you import resources from a workspace using the [`import workspace`](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/import-resources/#import-workspace-resources>) command, the generated YAML files contain special import metadata that tells Rudder CLI how to link local resources to workspace resources.

### Structure

The import metadata is located in the `metadata.import` section of the YAML file:
    
    
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
    

### Properties

The `metadata.import` section contains the following properties:

Property| Type| Description  
---|---|---  
`workspaces`  
Required| Array| Array of workspace import configurations. Each workspace configuration contains the workspace ID and resource mappings.  
  
#### Workspace configuration

Each workspace configuration in the `workspaces` array has the following structure:

Property| Type| Description  
---|---|---  
`workspace_id`  
Required| String| The ID of the workspace where resources were imported from.  
`resources`  
Required| Array| Array of mappings between local resource IDs and their corresponding workspace IDs.  
  
#### Resource mapping

Each resource mapping in the `resources` array has the following structure:

Property| Type| Description  
---|---|---  
`local_id`  
Required| String| The local resource ID used within your CLI project. This corresponds to the `id` field in the resource definition.  
`remote_id`  
Required| String| The remote resource ID from the workspace where the resource was imported from.  
  
> ![info](/docs/images/info.svg)
> 
> The import metadata serves two key purposes:
> 
>   * **Resource linking** : Enables Rudder CLI to link local resource definitions to existing workspace resources when you run the [`apply`](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/import-resources/#apply-imported-resources>) command. **Workspace-aware operations** : Tracks which workspace resources were imported from, allowing you to apply the same project to different workspaces. When you apply a project to a workspace different from the one specified in `workspace_id`, resources are treated as new resources to be created rather than imported.
> 

> 
> See [Manage Workspaces with Rudder CLI](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/import-resources/manage-workspaces/>) for more information about how to use import metadata in workspace management workflows.