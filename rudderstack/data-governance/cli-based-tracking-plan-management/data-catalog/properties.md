# Manage Properties using Rudder CLI Alpha

Define and manage event properties in your Data Catalog project using YAML configuration files.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __4 minute read

  * 


Properties provide context to your events by capturing additional attributes and metadata. This guide shows you how to define and manage properties in your Data Catalog using YAML configuration files.

## Property types

RudderStack supports the following property types in your Data Catalog:

Property type| Description  
---|---  
String| Text values  
Integer/Number| Number values  
Boolean| True/False values  
Array| Lists of values  
Object| Nested structures  
Custom Types| User-defined types with specific validation rules  
  
## Define properties

Using your preferred text editor, create a YAML file in your [Data Catalog project](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/project-setup/>) and add the below content:

### Basic structure

You can define properties in YAML files with the `kind: properties` specification. See [Data Catalog YAML Reference](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/project-yaml-reference/>) for the detailed YAML spec containing property definitions.
    
    
    version: rudder/v0.1
    kind: properties
    metadata:
      name: mypropertygroup
    spec:
      properties:
        - id: user_email
          name: "Email"
          type: string
          description: "User's email address"
    

Each property definition requires:

  * A unique identifier (`id`)
  * A property name (`name`)
  * A data type (`type`)
  * Optional description (`description`) and validation rules


The following snippets highlight the YAML definitions for different property types:
    
    
    - id: product_price
      name: "Price"
      type: number
      description: "Product price in USD"
    
    - id: is_premium
      name: "isPremium"
      type: boolean
      description: "Whether the user has a premium subscription"
    
    
    
    - id: username
      name: "Username"
      type: string
      description: "User's name"
      propConfig:
        minLength: 3
        maxLength: 50
        pattern: "^[a-zA-Z0-9_-]+$"
    
    - id: age
      name: "Age"
      type: integer
      description: "User's age"
      propConfig:
        minimum: 13
        maximum: 120
    
    
    
    - id: categories
      name: "Categories"
      type: array
      description: "User's favorite product categories"
      propConfig:
        minItems: 1
        maxItems: 5
        uniqueItems: true
    
    
    
    - id: shipping_address
      name: "Address"
      type: object
      description: "User's shipping address"
      properties:
        - id: street
          type: string
          required: true
        - id: city
          type: string
          required: true
        - id: postal_code
          type: string
          required: true
        - id: country
          type: string
          required: true
    

> ![success](/docs/images/tick.svg)
> 
> RudderStack supports [nesting properties](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/tracking-plans/create/#nested-properties>) while defining Tracking Plan rules — this lets you validate hierarchical data structures that mirror your actual data model.

### Property groups

You can group related properties in a single YAML file based on business context (like user profiles or product details) or other logical categories. Define each group with a unique `metadata.name` and list related properties under `spec.properties`.

> ![info](/docs/images/info.svg)
> 
> When defining property groups, ensure that:
> 
>   * Properties in the same group share similar validation requirements
>   * Related properties that are often used together in Tracking Plans are grouped together
>   * Each property group has a clear, specific purpose (for example, `user_properties` for user-related attributes)
> 


The following examples show how to organize properties into meaningful groups:
    
    
    version: rudder/v0.1
    kind: properties
    metadata:
      name: user_properties
    spec:
      properties:
        - id: user_id
          name: "ID"
          type: string
          description: "Unique identifier for the user"
          propConfig:
            minLength: 1
            maxLength: 64
        
        - id: email
          name: "Email"
          type: string
          description: "User's email address"
          propConfig:
            format: "email"
        
        - id: account_type
          name: "Account Type"
          type: string
          description: "Type of user account"
          propConfig:
            enum:
              - "personal"
              - "business"
              - "enterprise"
    
    
    
    version: rudder/v0.1
    kind: properties
    metadata:
      name: product_properties
    spec:
      properties:
        - id: product_id
          name: "Product ID"
          type: string
          description: "Unique identifier for the product"
          propConfig:
            pattern: "^PRD-[0-9]{6}$"
        
        - id: price
          name: "Price"
          type: number
          description: "Product price in USD"
          propConfig:
            minimum: 0
            exclusiveMinimum: true
        
        - id: categories
          name: "Categories"
          type: array
          description: "Product categories"
          propConfig:
            minItems: 1
            maxItems: 3
            uniqueItems: true
    

### Best practices

Follow these best practices when defining properties and property groups:

  * **Naming conventions**

    * Use clear, descriptive names
    * Follow consistent casing
    * Use meaningful prefixes for grouping
  * **Organization**

    * Use property groups to group related properties together
    * Use meaningful names that reflect the group’s purpose
  * **Validation**

    * Add meaningful constraints
    * Document validation requirements
    * Test edge cases
  * **Avoid resource duplication**

    * Do not define the same property in multiple property YAML files. Each property should exist in only one file to prevent duplication and potential confusion.


## Validate and deploy properties

Before deploying your properties to the workspace, validate them to ensure they follow the correct structure and meet your requirements.

### Validate properties

Run the following command to validate your property definitions:
    
    
    rudder-cli validate -l ~/tutorial-catalog
    

The command checks your property definitions for:

  * Required fields and correct structure
  * Valid property types and validation rules
  * Unique identifiers across your catalog
  * Proper YAML syntax


If validation succeeds, the command returns no output. If it finds any issues, it displays specific error messages to help you fix them.

### Deploy properties

After validating your properties, deploy them to your RudderStack workspace:

  1. Review the changes before deploying:


    
    
    rudder-cli apply -l ~/tutorial-catalog --dry-run
    

  2. Deploy the validated properties:


    
    
    rudder-cli apply -l ~/tutorial-catalog
    

The above command:

  * Creates new properties in your workspace
  * Updates existing properties if you’ve modified them
  * Reports the status of each operation
  * Requires confirmation before making changes (unless you use `--confirm=false`)


> ![info](/docs/images/info.svg)
> 
> See the [End-to-end Walkthrough](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/walkthrough/>) for steps on validating and deploying properties along with other Data Catalog resources.

## Next steps

  * Create [custom types](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/custom-types/>) for complex validation
  * Associate properties with [events](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/events/>)
  * Build [Tracking Plans](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/tracking-plans/>) using your events and properties
  * Automate changes to Tracking Plans by leveraging [CLI-based workflows](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/github-actions/>)