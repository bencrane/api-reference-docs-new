# Custom Type Variants Alpha

Define reusable object types with context-specific property requirements using custom type variants.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __7 minute read

  * 


This guide shows you how to define and use custom type variants in your [Data Catalog](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/>).

## Overview

Custom type variants let you define different property requirements for reusable object types based on a discriminating property value. This feature is particularly useful when an object type needs different validation rules depending on the context in which it is used.

> ![success](/docs/images/tick.svg)
> 
> Custom type variants work similarly to [Event Rule Variants](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/event-rule/>) but are defined at the custom type level rather than the event level. This makes them reusable across multiple events and Tracking Plans.

## Define custom type variants

Using your preferred text editor, add variants to your custom types in the [Custom Types YAML file](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/custom-types/#create-custom-types>):

### Basic structure

Custom type variants are defined within custom type definitions. See [Variants YAML Reference](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/yaml-reference/>) for the detailed variant specification.

The following snippet is a simplified example to demonstrate the structure. See the Examples section below for real-world use cases with complete implementations.
    
    
    version: rudder/v0.1
    kind: custom-types
    metadata:
      name: mycustomtypes
    spec:
      types:
        - id: custom_object
          name: "CustomObject"
          type: object
          description: "Object with context-specific requirements"
          
          # Common properties for all variants
          properties:
            - $ref: "#/properties/common_props/property_1"
              required: true    # Discriminator property must be required
            - $ref: "#/properties/common_props/property_2"
              required: false   # Common property that may be required by variants
            - $ref: "#/properties/common_props/property_3"
              required: false   # Property used in default case
          
          variants:
            - type: discriminator
              discriminator: "#/properties/common_props/property_1"    # Must match the property defined above
              cases:
                - display_name: "Case A"
                  match: 
                    - "value1"
                    - "value2"
                  description: "Description of Case A"
                  properties:
                    - $ref: "#/properties/common_props/property_2"
                      required: true
                
                - display_name: "Case B"
                  match:
                    - "value3"
                  description: "Description of Case B"
                  properties:
                    - $ref: "#/properties/common_props/property_2"
                      required: true
              
              # Default case for unmatched values
              default:
                - $ref: "#/properties/common_props/property_3"
                  required: true
    

Each variant definition requires:

  * The discriminator type (`type: discriminator`)

  * The discriminating property name (`discriminator`)

  * One or more cases with:

    * A display name (`display_name`)
    * Match values (`match`)
    * Description (`description`) explaining when this case applies
    * Property requirements (`properties`) specific to this case
  * Optional default case (`default`) for when no cases match


> ![warning](/docs/images/warning.svg)
> 
> The discriminator property must be:
> 
>   * Defined in the custom type’s properties section
>   * Marked as required
>   * Have a type matching your match values (string, boolean, or number)
> 


## Supported discriminator types

You can use the following discriminator types in your custom type variants:

Type| Description| Example values  
---|---|---  
String| Match against text values| `"US"`, `"UK"`, `"Japan"`  
Boolean| Match true/false conditions| `true`, `false`  
Number| Match against numeric thresholds| `500`, `1000`, `2000`  
  
> ![info](/docs/images/info.svg)
> 
> Note that for each type:
> 
>   * You can specify multiple match values in an array
>   * Values are matched exactly (no range or pattern matching)
>   * String matches are case-sensitive
> 


## Examples

The following examples show variant definitions for different use cases:

**Use Case** : Different address requirements based on country/region

This example shows how to validate different properties based on the country code, with specific requirements for each region:
    
    
    version: rudder/v0.1
    kind: custom-types
    metadata:
      name: address_types
    spec:
      types:
        - id: address_object
          name: "AddressObject"
          type: object
          description: "Address with region-specific requirements"
          
          properties:
            - $ref: "#/properties/address_props/country"
              required: true
            - $ref: "#/properties/address_props/street_address"
              required: true
            - $ref: "#/properties/address_props/city"
              required: true
            - $ref: "#/properties/address_props/postal_code"
            - $ref: "#/properties/address_props/state_province"
            - $ref: "#/properties/address_props/prefecture"
            - $ref: "#/properties/address_props/district"
          
          variants:
            - type: discriminator
              discriminator: "#/properties/address_props/country"
              cases:
                - display_name: "US Address"
                  match:
                    - "US"
                    - "USA" 
                    - "United States"
                  description: "US address format with state and ZIP"
                  properties:
                    - $ref: "#/properties/address_props/state_province"
                      required: true
                    - $ref: "#/properties/address_props/postal_code"
                      required: true
                      
                - display_name: "UK Address"
                  match:
                    - "UK"
                    - "GB"
                    - "United Kingdom"
                  description: "UK address format with postcode"
                  properties:
                    - $ref: "#/properties/address_props/postal_code"
                      required: true
                      
                - display_name: "Japan Address"
                  match:
                    - "JP"
                    - "Japan"
                  description: "Japanese address format with prefecture"
                  properties:
                    - $ref: "#/properties/address_props/prefecture"
                      required: true
                    - $ref: "#/properties/address_props/district"
                      required: false
              
              default:
                - $ref: "#/properties/address_props/postal_code"
                  required: false
    

#### Key takeaways

  * Uses string-based country code discrimination
  * Handles multiple country codes per case (for example, `US`, `USA`, `United States`)
  * Shows region-specific address requirements
  * Includes optional fields like district for specific regions


**Use Case** : Different product attributes based on category

This example shows how to validate different properties based on the product category:
    
    
    version: rudder/v0.1
    kind: custom-types
    metadata:
      name: product_types
    spec:
      types:
        - id: product_object
          name: "ProductObject"
          type: object
          description: "Product with category-specific attributes"
          
          properties:
            - $ref: "#/properties/product_props/product_id"
              required: true
            - $ref: "#/properties/product_props/product_name"
              required: true
            - $ref: "#/properties/product_props/category"
              required: true
            - $ref: "#/properties/product_props/price"
              required: true
            - $ref: "#/properties/product_props/size"
            - $ref: "#/properties/product_props/color"
            - $ref: "#/properties/product_props/material"
            - $ref: "#/properties/product_props/brand"
            - $ref: "#/properties/product_props/model"
            - $ref: "#/properties/product_props/screen_size"
            - $ref: "#/properties/product_props/storage_capacity"
            - $ref: "#/properties/product_props/author"
            - $ref: "#/properties/product_props/isbn"
            - $ref: "#/properties/product_props/page_count"
          
          variants:
            - type: discriminator
              discriminator: "#/properties/product_props/category"
              cases:
                - display_name: "Clothing & Apparel"
                  match:
                    - "clothing"
                    - "apparel"
                    - "fashion"
                    - "shoes"
                    - "accessories"
                  description: "Clothing items with size, color, material"
                  properties:
                    - $ref: "#/properties/product_props/size"
                      required: true
                    - $ref: "#/properties/product_props/color"
                      required: true
                    - $ref: "#/properties/product_props/material"
                      required: false
                    - $ref: "#/properties/product_props/brand"
                      required: true
                      
                - display_name: "Electronics"
                  match:
                    - "electronics"
                    - "computers"
                    - "phones"
                    - "tablets"
                    - "gadgets"
                  description: "Electronic devices with technical specs"
                  properties:
                    - $ref: "#/properties/product_props/brand"
                      required: true
                    - $ref: "#/properties/product_props/model"
                      required: true
                    - $ref: "#/properties/product_props/screen_size"
                      required: false
                    - $ref: "#/properties/product_props/storage_capacity"
                      required: false
                      
                - display_name: "Books & Literature"
                  match:
                    - "books"
                    - "ebooks"
                    - "literature"
                    - "textbooks"
                  description: "Books with author and publishing details"
                  properties:
                    - $ref: "#/properties/product_props/author"
                      required: true
                    - $ref: "#/properties/product_props/isbn"
                      required: false
                    - $ref: "#/properties/product_props/page_count"
                      required: false
              
              default:
                - $ref: "#/properties/product_props/brand"
                  required: false
    

#### Key takeaways

  * Uses category-based discrimination
  * Shows different property sets for each product type
  * Handles optional technical specifications
  * Demonstrates category-specific validation rules
  * Includes default case for brand property


**Use Case** : Different profile requirements based on account type

This example shows how to validate different properties based on the user’s account type:
    
    
    version: rudder/v0.1
    kind: custom-types
    metadata:
      name: user_profile_types
    spec:
      types:
        - id: user_profile_object
          name: "UserProfileObject"
          type: object
          description: "User profile with subscription-based requirements"
          
          properties:
            - $ref: "#/properties/profile_props/user_id"
              required: true
            - $ref: "#/properties/profile_props/email"
              required: true
            - $ref: "#/properties/profile_props/account_type"
              required: true
            - $ref: "#/properties/profile_props/first_name"
            - $ref: "#/properties/profile_props/last_name"
            - $ref: "#/properties/profile_props/company_name"
            - $ref: "#/properties/profile_props/job_title"
            - $ref: "#/properties/profile_props/phone_number"
            - $ref: "#/properties/profile_props/billing_address"
            - $ref: "#/properties/profile_props/tax_id"
            - $ref: "#/properties/profile_props/contract_start_date"
            - $ref: "#/properties/profile_props/account_manager"
          
          variants:
            - type: discriminator
              discriminator: "#/properties/profile_props/account_type"
              cases:
                - display_name: "Individual Account"
                  match:
                    - "individual"
                    - "personal"
                    - "consumer"
                  description: "Personal individual accounts"
                  properties:
                    - $ref: "#/properties/profile_props/first_name"
                      required: true
                    - $ref: "#/properties/profile_props/last_name"
                      required: true
                    - $ref: "#/properties/profile_props/phone_number"
                      required: false
                      
                - display_name: "Enterprise Account"
                  match:
                    - "enterprise"
                    - "premium"
                    - "platinum"
                  description: "Enterprise accounts with full details"
                  properties:
                    - $ref: "#/properties/profile_props/company_name"
                      required: true
                    - $ref: "#/properties/profile_props/job_title"
                      required: true
                    - $ref: "#/properties/profile_props/phone_number"
                      required: true
                    - $ref: "#/properties/profile_props/billing_address"
                      required: true
                    - $ref: "#/properties/profile_props/tax_id"
                      required: true
                    - $ref: "#/properties/profile_props/contract_start_date"
                      required: true
                    - $ref: "#/properties/profile_props/account_manager"
                      required: true
              
              default:
                - $ref: "#/properties/profile_props/first_name"
                  required: false
                - $ref: "#/properties/profile_props/last_name"
                  required: false
    

#### Key takeaways

  * Uses account type discrimination
  * Shows progressive property requirements (individual > business > enterprise)
  * Demonstrates enterprise-specific fields like contract details
  * Includes comprehensive profile validation with default case
  * Shows how to handle optional vs. required fields per account type


## Best practices

Follow these best practices when defining custom type variants:

  * **Discriminator selection**

    * Choose properties that clearly indicate different contexts
    * Ensure the discriminator property is always available
    * Use simple, predictable property values
  * **Case definition**

    * Use clear, descriptive display names
    * Group related match values in the same case
    * Include helpful descriptions
  * **Property requirements**

    * Include only relevant properties for each case
    * Consider required vs. optional carefully
    * Use default case for common requirements
  * **Validation**

    * Test all variant cases
    * Verify property references
    * Check for edge cases


## Validate and deploy variants

To update your custom types with the newly-added variants, make sure to [validate and deploy the changes](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/custom-types/#validate-and-deploy-custom-types>) using Rudder CLI.

## Reference custom types in properties

Once defined, you can use custom types with variants in your properties:
    
    
    version: rudder/v0.1
    kind: properties
    metadata:
      name: integration_properties
    spec:
      properties:
        - id: customer_profile
          name: "customer_profile"
          type: "#/custom-types/user_profile_types/user_profile_object"
          description: "Customer profile information"
        - id: purchased_product
          name: "purchased_product" 
          type: "#/custom-types/product_types/product_object"
          description: "Product that was purchased"
        - id: shipping_address
          name: "shipping_address"
          type: "#/custom-types/address_types/address_object"
          description: "Where to ship the order"
    

You can then reference these properties in your [Tracking Plan](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/tracking-plans/create/#define-tracking-plans>):
    
    
    version: rudder/v0.1
    kind: tp
    metadata:
      name: integrated_tracking_plan
    spec:
      id: integrated_plan
      display_name: "Integrated Plan with Custom Types"
      description: "Tracking plan demonstrating custom type usage"
      rules:
        - type: event_rule
          id: purchase_completed_rule
          event:
            $ref: "#/events/ecommerce_events/purchase_completed"
            allow_unplanned: false
          
          properties:
            - $ref: "#/properties/integration_properties/customer_profile"
              required: true
            - $ref: "#/properties/integration_properties/purchased_product"
              required: true
            - $ref: "#/properties/integration_properties/shipping_address"
              required: true
    

## See also

  * [Event Rule Variants](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/event-rule/>)
  * [Conditional Validation YAML Reference](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/yaml-reference/>)
  * Automated validation and deployment using [CLI-based Workflows](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/github-actions/>)