# Event Rule Variants Alpha

Define dynamic property requirements for events based on contextual values using event rule variants.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __5 minute read

  * 


This guide shows you how to define and use event rule variants in your Tracking Plans.

## Overview

Event rule variants let you define different property requirements for the same event based on a discriminating property value. This feature is particularly useful when an event needs different validation rules depending on the context in which it occurs.

> ![info](/docs/images/info.svg)
> 
> Event rule variants use a `discriminator` field to determine which set of property requirements apply. The discriminator is a property whose value determines which variant case to use.

## Define event rule variants

Using your preferred text editor, add variants to your event rules in the [Tracking Plan YAML file](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/tracking-plans/create/#define-tracking-plans>):

### Basic structure

Event rule variants are defined within event rules in Tracking Plans. See [Variants YAML Reference](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/yaml-reference/>) for the detailed variant specification.

The following snippet is a simplified example to demonstrate the structure. See the Examples section below for real-world use cases with complete implementations.
    
    
    version: rudder/v0.1
    kind: tp
    metadata:
      name: mytrackingplan
    spec:
      rules:
        - type: event_rule
          id: example_rule
          event:
            $ref: "#/events/example_events/example_event"
            allow_unplanned: false
          
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
>   * Defined in the event rule’s properties section
>   * Marked as required
>   * Have a type matching your match values (string, boolean, or number)
> 


## Supported discriminator types

You can use the following discriminator types in your event rule variants:

Type| Description| Example values  
---|---|---  
String| Match against text values| `"search"`, `"product"`, `"category_search"`  
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

**Use Case** : Different property requirements based on page type

This example shows how to validate different properties based on which type of page the user is viewing (search, product, or checkout):
    
    
    version: rudder/v0.1
    kind: tp
    metadata:
      name: ecommerce_tracking_plan
    spec:
      rules:
        - type: event_rule
          id: page_viewed_rule
          event:
            $ref: "#/events/ecommerce_events/page_viewed"
            allow_unplanned: false
          
          properties:
            - $ref: "#/properties/ecommerce_properties/page_type"
              required: true
            - $ref: "#/properties/ecommerce_properties/page_url"
              required: false
          
          variants:
            - type: discriminator
              discriminator: "#/properties/ecommerce_properties/page_type"
              cases:
                - display_name: "Search Results Page"
                  match: 
                    - "search"
                    - "search_results"
                    - "category_search"
                  description: "When user is on search or category pages"
                  properties:
                    - $ref: "#/properties/ecommerce_properties/search_term"
                      required: true
                    - $ref: "#/properties/ecommerce_properties/search_filters"
                      required: false
                      
                - display_name: "Product Detail Page"
                  match: 
                    - "product"
                    - "product_detail"
                  description: "When user is viewing a specific product"
                  properties:
                    - $ref: "#/properties/ecommerce_properties/product_id"
                      required: true
                    - $ref: "#/properties/ecommerce_properties/product_category"
                      required: true
                    - $ref: "#/properties/ecommerce_properties/product_price"
                      required: true
                    - $ref: "#/properties/ecommerce_properties/recommendation_source"
                      required: false
                      
                - display_name: "Checkout Flow Pages"
                  match:
                    - "checkout"
                    - "payment"
                    - "review_order"
                  description: "When user is in checkout process"
                  properties:
                    - $ref: "#/properties/ecommerce_properties/checkout_step"
                      required: true
                    - $ref: "#/properties/ecommerce_properties/payment_method"
                      required: false
              
              default:
                - $ref: "#/properties/ecommerce_properties/page_url"
                  required: true
    

#### Key takeaways

  * Uses string-based page type discrimination
  * Handles multiple match values per case (for example, `search`, `search_results`, `category_search`)
  * Shows required and optional properties for each page type
  * Includes a default case for unmatched page types


**Use Case** : Different requirements based on user subscription status

This example demonstrates how to validate different properties based on whether a user has premium access or not:
    
    
    version: rudder/v0.1
    kind: tp
    metadata:
      name: user_management_plan
    spec:
      rules:
        - type: event_rule
          id: feature_accessed_rule
          event:
            $ref: "#/events/user_events/feature_accessed"
            allow_unplanned: false
          
          properties:
            - $ref: "#/properties/user_properties/user_id"
              required: true
            - $ref: "#/properties/user_properties/is_premium"
              required: true
          
          variants:
            - type: discriminator
              discriminator: "#/properties/user_properties/is_premium"
              cases:
                - display_name: "Premium Users"
                  match: 
                    - true
                  description: "Premium subscribers with full access"
                  properties:
                    - $ref: "#/properties/user_properties/subscription_tier"
                      required: true
                    - $ref: "#/properties/user_properties/feature_access_level"
                      required: true
                      
                - display_name: "Free Users"
                  match:
                    - false
                  description: "Free tier users with limitations"
                  properties:
                    - $ref: "#/properties/user_properties/trial_days_remaining"
                      required: false
                    - $ref: "#/properties/user_properties/usage_limit"
                      required: true
    

#### Key takeaways

  * Uses simple boolean discrimination (`true`/`false`)
  * Shows different property requirements for premium vs. free users
  * Demonstrates required user identification for all cases
  * Shows how to handle optional properties like trial information


**Use Case** : Different requirements based on order total amount

This example shows how to validate different properties based on the order value, with special handling for high-value orders:
    
    
    version: rudder/v0.1
    kind: tp
    metadata:
      name: order_tracking_plan
    spec:
      rules:
        - type: event_rule
          id: order_placed_rule
          event:
            $ref: "#/events/order_events/order_placed"
            allow_unplanned: false
          
          properties:
            - $ref: "#/properties/order_properties/order_details"
              required: true
            - $ref: "#/properties/order_properties/order_total"
              required: true
          
          variants:
            - type: discriminator
              discriminator: "#/properties/order_properties/order_total"
              cases:
                - display_name: "High Value Orders"
                  match:
                    - 500
                    - 1000
                    - 2000
                  description: "Orders above $500 threshold"
                  properties:
                    - $ref: "#/properties/order_properties/loyalty_points_earned"
                      required: true
                    - $ref: "#/properties/order_properties/vip_handling"
                      required: true
                      
                - display_name: "Standard Orders"
                  match:
                    - 50
                    - 100
                    - 200
                  description: "Regular value orders"
                  properties:
                    - $ref: "#/properties/order_properties/loyalty_points_earned"
                      required: false
    

#### Key takeaways

  * Uses numeric value discrimination
  * Shows different thresholds for order value categories
  * Demonstrates special handling for high-value orders
  * Shows how to handle loyalty points based on order value


## Best practices

Follow these best practices when defining event rule variants:

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

To update your Tracking Plans with the newly-added variants, make sure to [validate and deploy the changes](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/tracking-plans/create/#validate-and-deploy-tracking-plans>) using Rudder CLI.

> ![info](/docs/images/info.svg)
> 
> See the [End-to-end Walkthrough](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/walkthrough/>) for detailed steps on validating and deploying Tracking Plans.

## See also

  * [Custom Type Variants](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/custom-types/>)
  * [Conditional Validation YAML Reference](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/yaml-reference/>)
  * Automated validation and deployment using [CLI-based Workflows](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/github-actions/>)