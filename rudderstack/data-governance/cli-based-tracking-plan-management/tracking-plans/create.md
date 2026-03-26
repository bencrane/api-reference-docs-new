# Create Tracking Plans using Rudder CLI Alpha

Define and create Tracking Plans in your Data Catalog project as YAML configuration files using the Rudder CLI tool.

* * *

  * __6 minute read

  * 


This guide shows you how to define and create Tracking Plans in your Data Catalog using Rudder CLI.

## Prerequisites

Before creating a Tracking Plan, ensure you have:

  1. [Rudder CLI tool](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/>) installed and [authenticated](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/walkthrough/#1-authenticate-the-cli-tool>)
  2. [Events](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/events/>) and [properties](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/properties/>) defined in your [Data Catalog project](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/project-setup/>)
  3. Optional [custom types](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/custom-types/>) created for validation


## Define Tracking Plans

Using your preferred text editor, create a YAML file in your [Data Catalog project](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/project-setup/>) and add the below content:

### Basic structure

You can define Tracking Plans in YAML files with the `kind: tp` specification.
    
    
    version: rudder/v0.1
    kind: tp
    metadata:
      name: mytrackingplan
    spec:
      id: mytrackingplan
      display_name: "Product Tracking Plan"
      description: "Contains all the events and properties for the Product Tracking Plan."
      rules:
        - type: event_rule
          id: product_viewed_rule
          event:
            $ref: "#/events/myeventgroup/product_viewed"
          allow_unplanned: false
          properties:
            - $ref: "#/properties/mypropertygroup/product_sku"
              required: true
    

Each Tracking Plan definition requires:

  * A unique identifier (`id`)
  * A display name (`display_name`)
  * A description (`description`)
  * Rules (`rules`) that reference events and their properties


See [Data Catalog YAML Reference](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/project-yaml-reference/>) for the detailed YAML spec containing Tracking Plan definitions.

### Event rules

Event rules define which events to track and their associated properties. Each rule requires:

  * A unique rule identifier (`id`)
  * A reference to the event (`event.$ref`)
  * Property references with validation requirements
  * Optional `allow_unplanned` flag to control unplanned event tracking
  * **For non-track events** : `identity_section` parameter to specify where properties should be placed


#### Track events

Track events use the standard `properties` section for their event properties:
    
    
    rules:
      - type: event_rule
        id: product_viewed_rule
        event:
          $ref: "#/events/myeventgroup/product_viewed"
        allow_unplanned: false
        properties:
          - $ref: "#/properties/mypropertygroup/product_sku"
            required: true
          - $ref: "#/properties/mypropertygroup/category"
            required: false
          - $ref: "#/properties/mypropertygroup/product_details"  # Object property with nested properties
            required: true
            properties:
              - $ref: "#/properties/mypropertygroup/product_name"
                required: true
              - $ref: "#/properties/mypropertygroup/product_price"
                required: true
    

#### Non-track events (identify, page, screen, group)

For non-track events, you must specify the `identity_section` parameter to define where the properties should be placed in the RudderStack event payload:
    
    
    rules:
      - type: event_rule
        id: user_identify_rule
        event:
          $ref: "#/events/userevents/user_identify"
          allow_unplanned: false
          identity_section: "traits"  # Properties go in traits section
        properties:
          - $ref: "#/properties/userproperties/email"
            required: true
          - $ref: "#/properties/userproperties/first_name"
            required: true
          - $ref: "#/properties/userproperties/last_name"
            required: false
    
    
    
    rules:
      - type: event_rule
        id: homepage_viewed_rule
        event:
          $ref: "#/events/pageevents/homepage_viewed"
          allow_unplanned: true
          identity_section: "context.traits"  # Properties go in context.traits section
        properties:
          - $ref: "#/properties/pageproperties/page_url"
            required: true
          - $ref: "#/properties/pageproperties/referrer"
            required: false
          - $ref: "#/properties/pageproperties/user_segment"
            required: false
    
    
    
    rules:
      - type: event_rule
        id: org_association_rule
        event:
          $ref: "#/events/groupevents/org_association"
          allow_unplanned: false
          identity_section: "traits"  # Properties go in traits section
        properties:
          - $ref: "#/properties/orgproperties/company_id"
            required: true
          - $ref: "#/properties/orgproperties/company_name"
            required: true
          - $ref: "#/properties/orgproperties/company_size"
            required: false
    

#### Identity section options

The `identity_section` parameter accepts the following values:

Value| Description| Use case  
---|---|---  
`properties`| Properties are placed in the main properties section| Track events (default)  
`traits`| Properties are placed in the traits section| Identify and Group events  
`context.traits`| Properties are placed in the context.traits section| Page and Screen events  
  
> ![info](/docs/images/info.svg)
> 
> The `identity_section` parameter is required for all non-track events (identify, page, screen, group).
> 
> Track events automatically use the `properties` section and do not need this parameter.

### Nested properties

RudderStack supports nesting properties within a property of `array`, `object`, or `array of object` type while defining Tracking Plan rules — this lets you validate hierarchical data structures that mirror your actual data model.

When referencing properties of `array`, `object`, or `array of object` type with nested properties in your Tracking Plans, add the `properties` key underneath the property reference, as shown:
    
    
    version: rudder/v0.1
    kind: tp
    metadata:
      name: ecommTrackingPlan
    spec:
      id: ecommPlan
      display_name: "Checkout Tracking Plan"
      description: "Contains all the events and properties for the checkout flow."
      rules:
        - type: event_rule
          id: page_viewed_rule
          event:
            $ref: "#/events/myeventgroup/page_viewed"
          allow_unplanned: true
          properties:
            - $ref: "#/properties/mypropertygroup/page"
              required: true
            - $ref: "#/properties/mypropertygroup/categories" # Object type property
              properties: # Nesting level 1
                - $ref: "#/properties/mypropertygroup/category_id"
                - $ref: "#/properties/mypropertygroup/category_object" # Object type property
                  properties: # Nesting level 2
                    - $ref: "#/properties/mypropertygroup/category_object_1"
                    - $ref: "#/properties/mypropertygroup/category_object_2"
                    properties: # Nesting level 3
                      - $ref: "#/properties/mypropertygroup/category_object_3"
                      - $ref: "#/properties/mypropertygroup/category_object_4"
    

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * You can use the `properties` key only with properties that have a type of `array`, `object`, or `array of object`. The validation will fail if you add nested properties to other property types like `string` or `integer`.
>   * You can nest properties up to **3 levels** , as seen in the above snippet.
>   * As a best practice, avoid circular dependencies when using custom types as nested properties.
> 


### Examples

The following examples show how to define Tracking Plans for different use cases:
    
    
    version: rudder/v0.1
    kind: tp
    metadata:
      name: ecommerce_tracking
    spec:
      id: ecommerce_tracking
      display_name: "Ecommerce Tracking"
      description: "Tracking Plan for ecommerce events"
      rules:
        - type: event_rule
          id: product_viewed_rule
          event:
            $ref: "#/events/ecommerce/product_viewed"
          properties:
            - $ref: "#/properties/product/sku"
              required: true
            - $ref: "#/properties/product/product_details"  # Object property with nested properties
              required: true
              properties:
                - $ref: "#/properties/product/product_name"
                  required: true
                - $ref: "#/properties/product/product_price"
                required: true
    
    
    
    version: rudder/v0.1
    kind: tp
    metadata:
      name: user_auth_tracking
    spec:
      id: user_auth_tracking
      display_name: "User Authentication Tracking"
      description: "Tracking Plan for user authentication events"
      rules:
        - type: event_rule
          id: user_registered_rule
          event:
            $ref: "#/events/auth/user_registered"
          properties:
            - $ref: "#/properties/user/email"
              required: true
            - $ref: "#/properties/user/signup_method"
              required: true
            - $ref: "#/properties/user/referral_source"
              required: false
    
    
    
    version: rudder/v0.1
    kind: tp
    metadata:
      name: user_identification_tracking
    spec:
      id: user_identification_tracking
      display_name: "User Identification Tracking"
      description: "Tracking Plan for user identification and page view events"
      rules:
        - type: event_rule
          id: user_identify_rule
          event:
            $ref: "#/events/user/user_identify"
            allow_unplanned: false
            identity_section: "traits"
          properties:
            - $ref: "#/properties/user/email"
              required: true
            - $ref: "#/properties/user/first_name"
              required: true
            - $ref: "#/properties/user/last_name"
              required: false
            - $ref: "#/properties/user/company"
              required: false
        - type: event_rule
          id: homepage_viewed_rule
          event:
            $ref: "#/events/pages/homepage_viewed"
            allow_unplanned: true
            identity_section: "context.traits"
          properties:
            - $ref: "#/properties/page/page_url"
              required: true
            - $ref: "#/properties/page/referrer"
              required: false
            - $ref: "#/properties/page/user_segment"
              required: false
    

## Validate and deploy Tracking Plans

Before deploying your Tracking Plans to the workspace, validate them to ensure they follow the correct structure and meet your requirements.

### Validate Tracking Plans

Run the following command to validate your Tracking Plan definitions:
    
    
    rudder-cli validate -l ~/tutorial-catalog
    

The command checks your Tracking Plan definitions for:

  * Required fields and correct structure
  * Valid event and property references
  * Unique identifiers across your catalog
  * Proper YAML syntax


If validation succeeds, the command returns no output. If it finds any issues, it displays specific error messages to help you fix them.

### Deploy Tracking Plans

After validating your Tracking Plans, deploy them to your RudderStack workspace:

  1. Review the changes before deploying:


    
    
    rudder-cli apply -l ~/tutorial-catalog --dry-run
    

  2. Deploy the validated Tracking Plans:


    
    
    rudder-cli apply -l ~/tutorial-catalog
    

The above command:

  * Creates new Tracking Plans in your workspace
  * Updates existing plans if you’ve modified them
  * Reports the status of each operation
  * Requires confirmation before making changes (unless you use `--confirm=false`)


> ![info](/docs/images/info.svg)
> 
> See the [End-to-end Walkthrough](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/walkthrough/>) for steps on validating and deploying Tracking Plans along with other Data Catalog resources.

## Best practices

Follow these best practices when defining Tracking Plans:

  * **Organization**

    * Group related events
    * Use clear rule IDs
    * Maintain consistent naming
  * **Properties**

    * Mark critical properties as required
    * Document property purposes
    * Use appropriate validation
  * **Validation**

    * Test all rules
    * Verify references
    * Check property constraints


## Next steps

  * [Update your Tracking Plan](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/tracking-plans/update/>) with new events, properties, and validation rules
  * Set up [GitHub Actions](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/github-actions/>) for automated Tracking Plan management