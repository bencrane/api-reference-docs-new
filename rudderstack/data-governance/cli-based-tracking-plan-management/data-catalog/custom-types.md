# Use Custom Data Types in Rudder CLI Alpha

Define, manage, and reference custom data types in your RudderStack Tracking Plans using YAML files and Rudder CLI.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __6 minute read

  * 


This guide walks you through creating and managing custom data types as YAML files in Rudder CLI.

## Overview

**Custom Data Types** extend RudderStack’s [CLI-based Tracking Plan management](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/>) capabilities, allowing you to define reusable data validation patterns that can be referenced across multiple properties in your RudderStack Tracking Plans, improving consistency and reducing duplication.

With custom data types, you can:

  * Define custom data types in YAML files with specific validation rules
  * Reference these custom data types in property definitions
  * Validate and sync using existing Rudder CLI commands
  * Version control your data types along with events, properties, and Tracking Plans
  * Deploy to your RudderStack workspace through your established Git workflow


## Use cases

This section highlights some common scenarios where custom data types can be helpful.

#### Standardizing validation

Alice is a Product Manager responsible for maintaining data quality across her organization. She needs to ensure that email properties consistently follow the same validation rules regardless of which team implements them.

With custom data types, she creates an `EmailType` with specific validation rules once, and then teams throughout the organization can reference this type in their property definitions, ensuring consistency.

#### Simplifying implementation

Bob is a Product Engineer implementing event tracking for a new feature.

Instead of figuring out the correct validation rules for each property, he references custom types defined by Alice. This ensures his implementation follows company standards without requiring detailed knowledge of validation patterns.

## Define custom types

You can define [custom data types](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/custom-types/>) in your Rudder CLI project as YAML files with the required validation rules.

A sample YAML file `~/tutorial-catalog/my-custom-types.yaml` that defines two custom data types (`SKU Type` and `Category Type`) is shown:
    
    
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
        - id: category_type
          name: "CategoryType"
          description: "Custom type for product identifiers"
          type: string
          config:       # Validation rules for the custom data type
            minLength: 10
            maxLength: 20
            pattern: "^PROD-[0-9]+$"
    

You can then reference these custom data types in your property definitions.

### YAML spec

You can define custom data types in the YAML file by setting `kind` to `custom-types`.

The `spec` parameter of the YAML file has the following structure:

Property| Type| Description  
---|---|---  
`types`  
Required| Array of custom type definitions| An array of custom type objects grouped together in the same file.  
  
#### Custom type definition

Property| Type| Description  
---|---|---  
`id`  
Required| String| Unique identifier for the custom type within the project. This parameter must be unique across all custom types in all the YAML files within the project.  
`name`  
Required| String| Display name of the custom type.  
  
**Note** : The custom type name must be between 2 and 65 characters long. It must start with a capital letter and contain only letters, numbers, underscores and dashes. Spaces are **not** allowed.  
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
`pattern`| Regular expression patterns. RudderStack supports the following patterns:  
  


  * Email
  * Date-time
  * Date
  * Time
  * URL
  * IPv4
  * IPv6
  * Custom (define a custom pattern)

  
`format`| Predefined format in which the values should be captured. RudderStack accepts the following formats:  
  


  * date-time
  * date
  * time
  * email
  * hostname
  * ipv4
  * ipv6
  * uuid

  
`enum`| Array of acceptable values  
  
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
  
### Best practices

Follow these best practices when defining custom types:

  * **Naming conventions**

    * Use clear, descriptive names
    * Follow consistent capitalization
    * Use meaningful prefixes for grouping
  * **Organization**

    * Group related custom types together in the same file
    * Use meaningful names that reflect the type’s purpose
  * **Validation**

    * Add meaningful constraints
    * Document validation requirements
    * Test edge cases
  * **Avoid resource duplication**

    * Do not define the same custom type in multiple custom type YAML files. Each custom type should exist in only one file to prevent duplication and potential confusion.


## Reference custom types in properties

Properties can reference custom types using the standard reference format consistent with how events and properties are referenced in Tracking Plans.

The following snippet references two custom types (`SKU Type` and `Category Type`) in the properties `SKU` and `Category`, respectively:
    
    
    version: rudder/v0.1
    kind: properties
    metadata:
      name: mypropertygroup
    spec:
      properties:
        - id: product_sku
          name: "SKU"
          type: "#/custom-types/identifier-types/sku_type" # Reference to custom type
          description: "Product SKU"
        - id: category
          name: "Category"
          type: "#/custom-types/identifier-types/category_type" # Reference to custom type
          description: "Product's category"
    

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * Custom types can reference other custom types, allowing for complex type hierarchies. See Advanced custom type features for more information.
>   * While there’s no limit on nesting depth, circular references are not supported currently.
> 


## Advanced features

This section covers some advanced use cases where you can leverage custom types.

### Array of custom types

You can define arrays of custom types, as shown:
    
    
    version: rudder/v0.1
    kind: custom-types
    metadata:
      name: advanced-types
    spec:
      types:
        - id: "emails_array_type"
          name: "EmailArrayType"
          description: "Array of email addresses"
          type: array
          config:
            itemTypes:
              - "#/custom-types/email-types/email_type" # Reference to another custom type
            minItems: 1
            maxItems: 10
            uniqueItems: true
    

### Object custom types

You can define object types with specific properties:
    
    
    version: rudder/v0.1
    kind: custom-types
    metadata:
      name: object-types
    spec:
      types:
        - id: address_type
          name: "AddressType"
          description: "Physical address information"
          type: object
          properties:
            - $ref: "#/properties/address/street"
              required: true
            - $ref: "#/properties/address/city"
              required: true
            - $ref: "#/properties/address/zip"
              required: true
            - $ref: "#/properties/address/country"
              required: false
    

## Validate and deploy custom types

Before deploying your custom types to the workspace, validate them to ensure they follow the correct structure and meet your requirements.

### Validate custom types

Run the following command to validate your custom type definitions:
    
    
    rudder-cli validate -l ~/tutorial-catalog
    

The command checks your custom type definitions for:

  * Required fields and correct structure
  * Valid custom type definitions
  * Proper YAML syntax


If validation succeeds, the command returns no output. If it finds any issues, it displays specific error messages to help you fix them.

### Deploy custom types

After validating your custom types, deploy them to your RudderStack workspace:

  1. Review the changes before deploying:


    
    
    rudder-cli apply -l ~/tutorial-catalog --dry-run
    

  2. Deploy the validated changes:


    
    
    rudder-cli apply -l ~/tutorial-catalog
    

The above command:

  * Creates new custom types in your workspace
  * Updates existing custom types if you’ve modified them
  * Reports the status of each operation
  * Requires confirmation before making changes (unless you use `--confirm=false`)


> ![info](/docs/images/info.svg)
> 
> See the [End-to-end Walkthrough](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/walkthrough/>) for steps on validating and deploying custom types along with other Data Catalog resources.

## Limitations

  * Circular reference checks are not currently performed.
  * When modifying a custom type that’s already in use, the changes will propagate to all properties that reference this custom type, potentially affecting validation behavior across all related properties.


## FAQ

#### How do custom types differ from property definitions?

Custom types are reusable type definitions that can be referenced by multiple properties. They encapsulate validation rules that can be consistently applied across multiple properties.

#### Will new custom data types work with existing Tracking Plans?

Yes, existing Tracking Plans will continue to work without modification. Custom types are an enhancement that you can adopt gradually.