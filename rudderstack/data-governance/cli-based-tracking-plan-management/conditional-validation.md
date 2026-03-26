# Conditional Validation in CLI-based Tracking Plan Management Alpha

Define flexible, context-aware validation rules for your Tracking Plan events and custom data types.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __3 minute read

  * 


> ![announcement](/docs/images/announcement.svg)
> 
> This feature is in **Alpha** as part of RudderStack’s [Early Access Program](<https://www.rudderstack.com/docs/get-started/alpha-and-beta-features/alpha-features/>), where we work with early users and customers to test new features and get feedback before making them generally available.
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

See the demo video below for more information:

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

### 1\. Event rule variants

Event rule variants let you define different property requirements for the same event based on a discriminating property. For example, a `Page Viewed` event might require different properties when viewed on a product page versus a search results page.

See [Event Rule Variants](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/event-rule/>) for more information.

### 2\. Custom type variants

Custom type variants enable you to create reusable object definitions with varying property requirements. For example, an `address` object might have different required fields depending on the country.

See [Custom Type Variants](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/custom-types/>) for more information.

## Get started

  1. Choose between event rule variants or custom type variants based on your needs.
  2. Review the [Conditional Validation YAML Reference](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/yaml-reference/>) guide for syntax and structure.
  3. Define your variants using the appropriate YAML configuration.
  4. Validate your configuration using the Rudder CLI.
  5. Deploy your changes using standard Git workflows.


## See also

  * [Event Rule Variants](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/event-rule/>)
  * [Custom Type Variants](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/custom-types/>)
  * [Conditional Validation YAML Reference](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/yaml-reference/>)