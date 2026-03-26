# Conditional Validation in Tracking Plans Alpha

Define flexible, context-aware validation rules for your Tracking Plan events and custom data types.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __5 minute read

  * 


> ![announcement](/docs/images/announcement.svg)
> 
> This feature is in **Alpha** as part of RudderStack’s [Early Access Program](<https://www.rudderstack.com/docs/get-started/alpha-and-beta-features/>), where we work with early users and customers to test new features and get feedback before making them generally available.
> 
> Note that these features are functional but can change as we improve them. [Contact the Product team](<mailto:product@rudderstack.com>) if you have any questions.

RudderStack’s **Conditional Validation** feature lets you define dynamic validation rules that adapt based on specific conditions or contexts. This powerful capability addresses a common challenge in data collection — maintaining strict data quality standards while accommodating legitimate variations in your event data structure.

## Overview

In real-world applications, the structure and requirements of your event data often need to change based on context. For example:

  * An ecommerce application that needs different product attributes for clothing versus electronics
  * A global application that needs to handle address formats that vary by country
  * A multi-tier service that needs to track different user properties based on subscription level


With the conditional validation feature, you can define different sets of property requirements based on a discriminating value. For example:

  * Different address formats based on the country
  * Varying product attributes based on the category
  * Dynamic event properties based on the page type


Without conditional validation, you would need to either:

  * Enforce all possible properties as optional, risking missing critical data
  * Create separate events for each variation, leading to event proliferation
  * Implement complex custom validation logic, increasing maintenance burden and complexity


Conditional validation solves these problems by letting you define context-aware validation rules directly in your Tracking Plan.

## Key features

  * **Discriminator-based validation** : Define different property requirements based on specific field values — RudderStack supports string and boolean discriminator types currently
  * **Flexible matching** : Support for exact match, multiple values, and array-based matching
  * **Default cases** : Define fallback requirements when no specific case matches
  * **Reusable custom type variants** : Create reusable custom types with variants that you can reference across your Tracking Plans


## When to use conditional validation

Use conditional validation when you need to:

  * **Handle regional variations** : Different requirements based on country, region, or locale
  * **Support multiple categories** : Varying attributes for different product types or user categories
  * **Context-specific validation** : Different requirements based on user context or application state
  * **Flexible event tracking** : Adapt event properties based on where or how the event occurs


## Variants

Conditional validation in RudderStack involves using two kinds of variants:

### Event rule variants

Event rule variants let you define different property requirements for the same event based on a discriminating property. For example, a `Page Viewed` event might require different properties when viewed on a product page versus a search results page.

See [Event Rule Variants](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/event-rule/>) for more information on defining these variants.

### Custom type variants

Custom type variants enable you to create reusable object definitions with varying property requirements. For example, an `address` object might have different required fields depending on the country.

See [Custom Type Variants](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/custom-types/>) for more information on defining these variants.

## Dashboard visibility

Once you define conditional validation variants using the CLI, you can view them in the RudderStack dashboard. The dashboard shows:

  * **Event variants** : Different validation rules for the same event based on discriminating properties
  * **Custom type variants** : Context-specific property requirements for reusable object types


As shown in the screenshot below, the dashboard displays the available variants for your events and properties, making it easy to understand the different validation contexts:

[![Conditional validation in Tracking Plans](/docs/images/data-governance/tracking-plans/conditional-validation-ui.webp)](</docs/images/data-governance/tracking-plans/conditional-validation-ui.webp>)

> ![warning](/docs/images/warning.svg)
> 
> While you can **view** event and custom type variants in the RudderStack dashboard, you **cannot** create, edit, or delete variants through the dashboard interface — these operations must be performed using [Rudder CLI](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/>).

## Get started

To implement conditional validation in your Tracking Plans:

  1. **Set up CLI access** : Ensure you have the [Rudder CLI installed and configured](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/installation/>).

  2. **Choose variant type** : Decide between event rule variants or custom type variants based on your requirement.

  3. **Review syntax** : See the [Conditional Validation YAML Reference](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/yaml-reference/>) guide for syntax and structure.

  4. **Define variants** : Create your variants using the appropriate YAML configuration — see the following guides for detailed instructions:

     * [Event Rule Variants](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/event-rule/>)
     * [Custom Type Variants](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/custom-types/>)
  5. **Validate and deploy** : Use Rudder CLI to validate your configuration and deploy changes using standard Git workflows.

  6. **View in dashboard** : Once deployed, your variants will be visible in the RudderStack dashboard for easy reference and monitoring.


## FAQ

#### What is the discriminator field seen next to the property name?

A **discriminator** is a specific property in your event or custom type that determines which validation rules apply. It acts as a “switch” that tells RudderStack which variant case to use based on its value.

For example:

  * In an ecommerce application, the `page_type` property can be a discriminator that determines different validation requirements for “product”, “search”, or “checkout” pages.
  * In a global application, the `country` property can discriminate between different address validation requirements.


The discriminator must be:

  * A required property in your event or custom type
  * Have a consistent, predictable set of possible values
  * Match the type of values defined in your variant cases (String, Boolean, or Number)


#### Why can’t I define variants in the dashboard?

Conditional validation requires complex YAML configuration with precise syntax for:

  * **Property references** : Exact paths to properties in your schema
  * **Discriminator definitions** : Specific field mappings and type matching
  * **Case logic** : Multiple match values, property requirements, and default fallbacks
  * **Schema validation** : Ensuring all references and dependencies are correct


This level of configuration complexity is better suited to code-based workflows where you can:

  * Use version control to track changes
  * Validate syntax before deployment
  * Review changes through pull requests
  * Maintain consistency across large schemas
  * Leverage IDE features like syntax highlighting and validation


The RudderStack dashboard currently focuses on providing clear visibility into your configured variants rather than complex configuration management.

## See also

  * [Conditional Validation using Rudder CLI](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/>)
  * [CLI-based Tracking Plan Management](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/>)