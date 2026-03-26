# Recommended Data Catalog and Tracking Plans Directory Structure Alpha

Learn about the recommended directory structure for organizing your Data Catalog resources and Tracking Plans as YAML files.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __7 minute read

  * 


This guide outlines a recommended directory structure for organizing your RudderStack Data Catalog resources and Tracking Plans as YAML files in a Git repository.

## How Rudder CLI works

The Rudder CLI tool (`rudder-cli`) is flexible in how it processes your YAML files:

  * **File discovery** : The CLI recursively scans the specified directory (or project root) for all `.yaml` and `.yml` files.
  * **Flexible organization** : You can organize files in any directory structure that makes sense for your project.
  * **No naming requirements** : File names and directory names are completely flexible—the CLI identifies resources by their `kind` and content, not file location.


## Important YAML file requirements

Before organizing your files, understand these critical requirements:

### Single YAML object per file

Each YAML file must contain exactly one YAML document/object with the standard structure:
    
    
    version: rudder/v0.1
    kind: [events|properties|custom-types|tp]
    metadata:
      name: [unique-name]
    spec:
      # Resource definitions
    

### Collection capabilities by kind

Kind| Description  
---|---  
`kind: events`| Can contain multiple event definitions in the `spec.events` array  
`kind: categories`| Can contain multiple event category definitions in the `spec.categories` array  
`kind: properties`| Can contain multiple property definitions in the `spec.properties` array  
`kind: custom-types`| Can contain multiple custom type definitions in the `spec.types` array  
`kind: tp`| Contains **exactly one** Tracking Plan definition  
  
### Unique resource identification

  * Each resource (event, property, custom type, Tracking Plan) must have a unique `id` across the entire project.
  * No duplicate `id` values are allowed, even across different YAML files.
  * Rudder CLI uses `kind` \+ `metadata.name` \+ resource `id` to create unique references.


> ![warning](/docs/images/warning.svg)
> 
> **Avoid resource duplication**
> 
> Do not define the same resource (event, property, or custom type) in multiple YAML files. Each resource should exist in only one file to prevent duplication and potential confusion.
> 
> If you need to reference a resource from another file, use the `$ref` syntax instead of redefining it.

### Tracking Plan limitation

  * Each Tracking Plan YAML file (`kind: tp`) can define only one Tracking Plan.
  * If you need multiple Tracking Plans, create separate YAML files for each.


## Recommended directory structure

The recommended directory structure offers developers a clear organizational hierarchy for configuration files while maintaining high-level alignment with the Data Governance structure in the RudderStack UI:

  * The Data Catalog and Tracking Plans are managed in separate, dedicated folders
  * Business logic is reflected by grouping events and properties into business-specific folders (for example, `/product` and `/marketing`)
    * In complex environments, you can maintain clarity by using separate files for similar assets within a business-specific folder (for example, the `events/checkout` folder has separate files for `cart-events` and `purchase-events`)
  * Tracking Plans are grouped by source
    * In complex environments, you can create dedicated Tracking Plans for use cases within a source folder (for example, `/tracking-plans/web/checkout-flow.yaml`)


    
    
    project-root/
    ├── .github/
    │   └── workflows/
    │       ├── tracking-plan-validate.yml       # PR validation workflow
    │       └── tracking-plan-sync.yml           # Main branch deployment workflow
    ├── data-catalog/
    │   ├── custom-types/
    │   │   ├── identifiers.yaml                 # SKU, product IDs, etc.
    │   │   ├── user-types.yaml                  # User-related custom types
    │   │   ├── commerce-types.yaml              # E-commerce specific types
    │   │   └── analytics-types.yaml             # Analytics-specific types
    │   ├── properties/
    │   │   ├── common/
    │   │   │   ├── user-properties.yaml         # User ID, email, traits, etc.
    │   │   │   ├── session-properties.yaml      # Session ID, timestamp, etc.
    │   │   │   └── device-properties.yaml       # Device info, browser, etc.
    │   │   ├── product/
    │   │   │   ├── product-properties.yaml      # product_id, name, price, etc.
    │   │   │   └── catalog-properties.yaml      # category, brand, etc.
    │   │   ├── checkout/
    │   │   │   ├── cart-properties.yaml         # Cart-related properties
    │   │   │   ├── order-properties.yaml        # Order-related properties
    │   │   │   └── payment-properties.yaml      # Payment-related properties
    │   │   └── marketing/
    │   │       ├── campaign-properties.yaml     # UTM parameters, etc.
    │   │       └── attribution-properties.yaml  # Attribution parameters
    │   ├── categories/
    │   │   ├── user-categories.yaml             # User-related categories
    │   │   ├── product-categories.yaml          # Product-related categories
    │   │   ├── checkout-categories.yaml         # Checkout-related categories
    │   │   ├── marketing-categories.yaml        # Marketing-related categories
    │   │   └── analytics-categories.yaml        # Analytics-related categories
    │   └── events/
    │       ├── user/
    │       │   ├── authentication-events.yaml   # Signup, login, logout, etc.
    │       │   ├── profile-events.yaml          # Profile updates, preferences
    │       │   └── onboarding-events.yaml       # User onboarding flow
    │       ├── product/
    │       │   ├── catalog-events.yaml          # Product viewed, searched, etc.
    │       │   ├── engagement-events.yaml       # Product liked, shared, etc.
    │       │   └── comparison-events.yaml       # Product compared, listed, etc.
    │       ├── checkout/
    │       │   ├── cart-events.yaml             # Cart events
    │       │   ├── checkout-events.yaml         # Checkout flow events
    │       │   └── purchase-events.yaml         # Purchase and payment events
    │       ├── engagement/
    │       │   ├── page-events.yaml             # Page views, navigation
    │       │   ├── interaction-events.yaml      # Clicks, form submissions
    │       │   └── content-events.yaml          # Content engagement
    │       └── marketing/
    │           ├── campaign-events.yaml         # Campaign interactions
    │           └── conversion-events.yaml       # Goal completions
    ├── tracking-plans/
    │   ├── web/
    │   │   ├── main-website.yaml                # Main website Tracking Plan
    │   │   ├── checkout-flow.yaml               # Checkout-specific plan
    │   │   └── marketing-pages.yaml             # Landing pages, campaigns
    │   ├── mobile/
    │   │   ├── ios-app.yaml                     # iOS app Tracking Plan
    │   │   ├── android-app.yaml                 # Android app Tracking Plan
    │   │   └── mobile-shared.yaml               # Shared mobile events
    │   ├── backend/
    │   │   ├── api-events.yaml                  # Server-side events
    │   │   └── system-events.yaml               # System/operational events
    │   └── integrations/
    │       ├── crm-integration.yaml             # CRM-specific events
    │       ├── marketing-tools.yaml             # Marketing automation events
    │       └── analytics-platforms.yaml         # Analytics platform events
    

## Alternative organization approaches

Since the CLI is flexible, you could also organize files differently based on your team’s preferences:

### 1\. Flat structure
    
    
    tracking-plans/
    ├── all-events.yaml
    ├── all-properties.yaml
    ├── all-custom-types.yaml
    ├── web-tracking-plan.yaml
    └── mobile-tracking-plan.yaml
    

### 2\. Feature-based organization
    
    
    tracking-plans/
    ├── user-authentication/
    │   ├── events.yaml
    │   ├── properties.yaml
    │   └── tracking-plan.yaml
    ├── e-commerce/
    │   ├── events.yaml
    │   ├── properties.yaml
    │   ├── custom-types.yaml
    │   └── tracking-plan.yaml
    └── analytics/
        ├── events.yaml
        └── tracking-plan.yaml
    

### 3\. Platform-first organization
    
    
    tracking-plans/
    ├── web/
    │   ├── events.yaml
    │   ├── properties.yaml
    │   └── tracking-plan.yaml
    ├── mobile/
    │   ├── events.yaml
    │   ├── properties.yaml
    │   └── tracking-plan.yaml
    └── shared/
        ├── common-events.yaml
        ├── common-properties.yaml
        └── custom-types.yaml
    

## Reference system

When creating Tracking Plans, you can reference resources using the following format:
    
    
    # Reference to an event
    $ref: "#/events/[metadata.name]/[event.id]"
    
    # Reference to a property  
    $ref: "#/properties/[metadata.name]/[property.id]"
    
    # Reference to a custom type (in property definitions)
    type: "#/custom-types/[metadata.name]/[type.id]"
    

## Example file contents

The following are some example file contents for the recommended directory structure:
    
    
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
          config:
            minLength: 5
            maxLength: 255
            pattern: "^SKU-[0-9]+$"
    
    
    
    version: rudder/v0.1
    kind: categories
    metadata:
      name: product-categories
    spec:
      categories:
        - id: product_viewed_category
          name: "Product Viewed"
          description: "Category for product viewing events"
        - id: product_interaction_category
          name: "Product Interaction"
          description: "Category for product interaction events"
        - id: product_purchase_category
          name: "Product Purchase"
          description: "Category for product purchase events"
    
    
    
    version: rudder/v0.1
    kind: events
    metadata:
      name: product-events
    spec:
      events:
        - id: product_viewed
          name: "Product Viewed"
          event_type: track
          description: "User viewed a product"
          category: "#/categories/product-categories/product_viewed_category"
        - id: product_added_to_cart
          name: "Product Added to Cart"
          event_type: track
          description: "User added product to cart"
          category: "#/categories/product-categories/product_interaction_category"
        - id: product_purchased
          name: "Product Purchased"
          event_type: track
          description: "User completed a product purchase"
          category: "#/categories/product-categories/product_purchase_category"
    
    
    
    version: rudder/v0.1
    kind: properties
    metadata:
      name: product-properties
    spec:
      properties:
        - id: product_sku
          name: "product_sku"
          type: "#/custom-types/identifier-types/sku_type"
          description: "Product SKU"
        - id: product_name
          name: "product_name"
          type: string
          description: "Product name"
        - id: product_price
          name: "product_price"
          type: number
          description: "Product price"
        - id: product_quantity
          name: "product_quantity"
          type: integer
          description: "Product quantity"
    
    
    
    version: rudder/v0.1
    kind: tp
    metadata:
      name: web-ecommerce-plan
    spec:
      id: web_ecommerce_tracking_plan
      display_name: "Web E-commerce Tracking Plan"
      description: "Tracking Plan for web e-commerce events"
      rules:
        - type: event_rule
          id: product_viewed_rule
          event:
            $ref: "#/events/product-events/product_viewed"
          allow_unplanned: false
          properties:
            - $ref: "#/properties/product-properties/product_sku"
              required: true
            - $ref: "#/properties/product-properties/product_name"
              required: true
            - $ref: "#/properties/product-properties/product_price"
              required: false
        - type: event_rule
          id: product_added_to_cart_rule
          event:
            $ref: "#/events/product-events/product_added_to_cart"
          allow_unplanned: false
          properties:
            - $ref: "#/properties/product-properties/product_sku"
              required: true
            - $ref: "#/properties/product-properties/product_name"
              required: true
            - $ref: "#/properties/product-properties/product_quantity"
              required: true
        - type: event_rule
          id: product_purchased_rule
          event:
            $ref: "#/events/product-events/product_purchased"
          allow_unplanned: false
          properties:
            - $ref: "#/properties/product-properties/product_sku"
              required: true
            - $ref: "#/properties/product-properties/product_name"
              required: true
            - $ref: "#/properties/product-properties/product_price"
              required: true
            - $ref: "#/properties/product-properties/product_quantity"
              required: true
    

## Benefits of the recommended structure

  * **Scalability** : It is easy to add new domains, platforms, or resource types.
  * **Maintainability** : Clear organization makes finding and updating resources simple.
  * **Reusability** : Common properties and custom types can be easily referenced across different Tracking Plans.
  * **Collaboration** : Team members can work on different domains without merge conflicts.
  * **Flexibility** : While providing structure, allows teams to adapt the organization to their specific needs.


## Get started

  1. Choose an organizational approach that fits your team’s workflow.
  2. Ensure all resource `id` values are unique across your entire project.
  3. Set up [GitHub Actions workflows](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/github-actions/>) for validation and deployment.
  4. Start with a simple structure and evolve as your needs grow.


> ![info](/docs/images/info.svg)
> 
> The most important aspect is consistency within your chosen approach, not following any specific directory structure.