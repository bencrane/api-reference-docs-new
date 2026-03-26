# Update Tracking Plans using Rudder CLI Alpha

Update existing Tracking Plans in your Data Catalog project as YAML configuration files using the Rudder CLI tool.

* * *

  * __3 minute read

  * 


This guide shows you how to update existing Tracking Plans in your Data Catalog using Rudder CLI.

## Prerequisites

Before updating a Tracking Plan, ensure you have:

  1. [Rudder CLI tool](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/>) installed and [authenticated](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/walkthrough/#1-authenticate-the-cli-tool>)
  2. An existing Tracking Plan in your workspace
  3. [Events](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/events/>) and [properties](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/properties/>) defined in your [Data Catalog project](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/project-setup/>)
  4. Optional [custom types](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/custom-types/>) for validation


## Update tracking plans

You can update your Tracking Plans by modifying the YAML files in your Data Catalog project. These updates can include:

  * Adding new events and properties
  * Modifying validation rules
  * Removing obsolete tracking


### Add new events

Add new events to your Tracking Plan by including additional event rules:
    
    
    version: rudder/v0.1
    kind: tp
    metadata:
      name: mytrackingplan
    spec:
      id: mytrackingplan
      display_name: "Product Tracking Plan"
      description: "Contains all the events and properties for the Product Tracking Plan"
      rules:
        # Existing rules remain unchanged
        - type: event_rule
          id: product_viewed_rule
          event:
            $ref: "#/events/myeventgroup/product_viewed"
          properties:
            - $ref: "#/properties/mypropertygroup/product_sku"
              required: true
        
        # New event rule added
        - type: event_rule
          id: add_to_cart_rule
          event:
            $ref: "#/events/myeventgroup/add_to_cart"
          properties:
            - $ref: "#/properties/mypropertygroup/product_sku"
              required: true
            - $ref: "#/properties/mypropertygroup/quantity"
              required: true
    

### Modify properties

Update property requirements or add new properties to existing events:
    
    
    rules:
      - type: event_rule
        id: product_viewed_rule
        event:
          $ref: "#/events/myeventgroup/product_viewed"
        properties:
          # Existing properties
          - $ref: "#/properties/mypropertygroup/product_sku"
            required: true
          # New properties added
          - $ref: "#/properties/mypropertygroup/category"
            required: false
          # Modified requirement
          - $ref: "#/properties/mypropertygroup/price"
            required: true  # Changed from false
    

> ![info](/docs/images/info.svg)
> 
> You can also remove events or properties by deleting their entries from the YAML file.

## Example updates

The following examples show how to update Tracking Plans for different scenarios:
    
    
    version: rudder/v0.1
    kind: tp
    metadata:
      name: ecommerce_tracking
    spec:
      id: ecommerce_tracking
      display_name: "Ecommerce Tracking"
      description: "Updated Tracking Plan for ecommerce events"
      rules:
        # Existing product view tracking
        - type: event_rule
          id: product_viewed_rule
          event:
            $ref: "#/events/ecommerce/product_viewed"
          properties:
            - $ref: "#/properties/product/sku"
              required: true
            - $ref: "#/properties/product/category"
              required: false
          # name and price are removed from the properties
        
        # New wishlist tracking
        - type: event_rule
          id: wishlist_add_rule
          event:
            $ref: "#/events/myeventgroup/wishlist_add"
          properties:
            - $ref: "#/properties/mypropertygroup/product_sku"
              required: true
            - $ref: "#/properties/mypropertygroup/list_id"
              required: true
    
    
    
    version: rudder/v0.1
    kind: tp
    metadata:
      name: user_auth_tracking
    spec:
      id: user_auth_tracking
      display_name: "User Authentication Tracking"
      description: "Updated Tracking Plan for user authentication events"
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
              # referral_source is updated to required
            - $ref: "#/properties/user/referral_source"
              required: true # Changed from false
    

## Validate and deploy updates

Before deploying your Tracking Plan updates, validate them to ensure they follow the correct structure and meet your requirements.

### Validate updates

Run the following command to validate your Tracking Plan updates:
    
    
    rudder-cli validate -l ~/tutorial-catalog
    

The command checks your Tracking Plan updates for:

  * Required fields and correct structure
  * Valid event and property references
  * Unique identifiers across your catalog
  * Proper YAML syntax


If validation succeeds, the command returns no output. If it finds any issues, it displays specific error messages to help you fix them.

### Deploy updates

After validating your updates, deploy them to your RudderStack workspace:

  1. Review the changes before deploying:


    
    
    rudder-cli apply -l ~/tutorial-catalog --dry-run
    

  2. Deploy the validated updates:


    
    
    rudder-cli apply -l ~/tutorial-catalog
    

The above command:

  * Updates existing Tracking Plans in your workspace
  * Reports the status of each operation
  * Requires confirmation before making changes (unless you use `--confirm=false`)


> ![info](/docs/images/info.svg)
> 
> See the [End-to-end Walkthrough](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/walkthrough/>) for steps on validating and deploying Tracking Plan updates along with other Data Catalog resources.

## Best practices

Follow these best practices when updating Tracking Plans:

  * **Change management**

    * Review with stakeholders
    * Test thoroughly
    * Deploy gradually
  * **Backward compatibility**

    * Consider existing implementations
    * Plan deprecation periods
    * Communicate changes
  * **Testing**

    * Validate all changes
    * Test integrations
    * Monitor implementation


## Next steps

  * Set up [GitHub Actions](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/github-actions/>) for automated Tracking Plan management