# Conditional Validation YAML Reference Alpha

Complete reference for defining Event Rule and Custom Type variants using YAML configuration files.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __3 minute read

  * 


[Conditional validation](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/>) involves using two kinds of variants:

  * [Event Rule Variants](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/event-rule/>) within Tracking Plan event rules
  * [Custom Type Variants](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/custom-types/>) within [Custom Type](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/custom-types/>) definitions


Both types share a common structure but are used in different contexts. This reference details the YAML schema and configuration options for both types.

## Common variant structure

All variant definitions share the following structure:

Property| Type| Description  
---|---|---  
`type`  
Required| String| Must be `discriminator`  
`discriminator`  
Required| String| Full path of the property that determines which variant case applies. Must match a required property defined in the parent object.  
`cases`  
Required| Array of case definitions| Array of variant cases defining different validation rules.  
`default`| default case| Default validation rules when no case matches.  
  
### `cases` definition

Each case in the `cases` array has the following structure:

Property| Type| Description  
---|---|---  
`display_name`  
Required| String| Human-readable name for the case.  
`match`  
Required| Array| Array of values that trigger this case. Values must match the discriminator property’s type.  
`description`  
Required| String| Description explaining when this case applies.  
`properties`| Array of property references| Property requirements specific to this case.  
  
### `default` case

The optional default case has the following structure:

Property| Type| Description  
---|---|---  
`properties`  
Required| Array of property references| Property requirements for when no case matches.  
  
### Property references

Property references in both cases and default case have this structure:

Property| Type| Description  
---|---|---  
`$ref`  
Required| String| Reference to a property defined in the parent object’s properties section.  
`required`| Boolean| Whether the property is required. Defaults to `false`.  
  
## Supported types

This section lists the types supported for the `discriminator` and match properties.

### Discriminator types

The following types are supported for the `discriminator` property:

Type| Description| Example values| Notes  
---|---|---|---  
String| Text-based discrimination| `"search"`, `"US"`, `"clothing"`| Case-sensitive matching  
Boolean| True/false discrimination| `true`, `false`| Simple binary choices  
Number| Numeric discrimination| `500`, `1000`, `2000`| Exact value matching  
  
> ![info](/docs/images/info.svg)
> 
> The discriminator property must be:
> 
>   * Defined in the parent object’s properties section
>   * Marked as required
>   * Have a type matching your match values (string, boolean, or number)
> 


### Match values

The `match` array in each case supports:

Type| Format| Example  
---|---|---  
String| Array of strings| `["US", "USA", "United States"]`  
Boolean| Array of booleans| `[true]` or `[false]`  
Number| Array of numbers| `[500, 1000, 2000]`  
  
> ![info](/docs/images/info.svg)
> 
> Note that for `match` values:
> 
>   * RudderStack matches the values exactly (no pattern or range matching)
>   * String matches are case-sensitive
>   * Each case can have multiple match values
>   * All match values in a case must be of the same type as the discriminator
> 


## Variant structure examples

This section provides examples of how to define Event Rule and Custom Type variants using YAML configuration files.

### Event Rule variant
    
    
    variants:
      - type: discriminator
        discriminator: "page_type"
        cases:
          - display_name: "Search Results Page"
            match: ["search", "search_results"]
            description: "When user is on search pages"
            properties:
              - $ref: "#/properties/search_term"
                required: true
    

### Custom Type variant
    
    
    variants:
      - type: discriminator
        discriminator: "country"
        cases:
          - display_name: "US Address"
            match: ["US", "USA"]
            description: "US address format"
            properties:
              - $ref: "#/properties/state"
                required: true
    

## See also

  * [Event Rule Variants](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/event-rule/>)
  * [Custom Type Variants](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/custom-types/>)