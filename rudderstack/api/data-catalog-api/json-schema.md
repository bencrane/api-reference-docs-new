# JSON Schema

JSON schema specification for upserting events to your Tracking Plan via Data Catalog API.

* * *

  * __6 minute read

  * 


[JSON schema](<https://json-schema.org/overview/what-is-jsonschema>) is a vocabulary used to annotate and validate JSON documents.

Follow this guide to standardize and define expectations for your events while [upserting them into your Tracking Plan](<https://www.rudderstack.com/docs/api/data-catalog-api/#upsert-event-to-tracking-plan>) via the Data Catalog API.

## Keywords

Keywords are properties appearing within a JSON [schema](<https://json-schema.org/learn/glossary#schema>) object.
    
    
    {
      "title": "Example Schema",
      "type": "object"
    }
    

In the above snippet, the `title` and `type` are keywords.

### Type-specific keywords

The `type` keyword specifies the data type for a JSON schema. RudderStack supports the following keywords:

#### Strings

The [`string`](<https://json-schema.org/understanding-json-schema/reference/string>) data type is used to represent strings of text and can contain Unicode characters.

RudderStack supports the following advanced keywords for strings:

  * `minLength`
  * `maxLength`
  * `pattern`
  * `format`


A sample schema definition for a string:
    
    
    {
      "type": "string",
      "minLength": 2,
      "maxLength": 5,
      "pattern": "^(\\([0-9]{3}\\))?[0-9]{3}-[0-9]{4}$"
    }
    

Some examples of data that are compliant and non-compliant to the above schema:
    
    
    - "Hello"
    - "42"
    - "555-1212"
    
    
    
    - "Welcome"
    - "A"
    - "(888)555-1212 ext. 532"
    

#### Integers and numbers

The JSON schema defines two [numeric data types](<https://json-schema.org/understanding-json-schema/reference/numeric>):

  * `integer`: Used for integral numbers.
  * `number`: Used for any numeric type like integers or floating point numbers.


RudderStack supports the following advanced keywords for numbers:

  * `multipleOf`
  * `minimum`
  * `maximum`
  * `exclusiveMinimum`
  * `exclusiveMaximum`


A sample schema definition for an integer and number:
    
    
    {
      "type": "integer"
    }
    
    
    
    {
      "type": "number",
      "minimum": 0,
      "maximum": 100,
      "multipleOf": 10,
      "exclusiveMaximum": 100
    }
    

Some examples of data that are compliant and non-compliant to the **Integer** schema:
    
    
    - 42
    - -1
    - 1.0
    
    
    
    - 3.1415926
    - "52"
    

Some examples of data that are compliant and non-compliant to the **Number** schema:
    
    
    - 40
    - 50
    
    
    
    - "41"
    - 24
    - 100
    

#### Objects

You can use JSON [objects](<https://json-schema.org/understanding-json-schema/reference/object>) to map specific keys to values.

While using the Data Catalog API, you can use the [`rules`](<https://www.rudderstack.com/docs/api/data-catalog-api/#upsert-event-to-tracking-plan>) object to specify the property mappings for the event to be upserted in the Tracking Plan. A sample `rules` object is shown:
    
    
    {
      "identify": {
        "type": "object",
        "$schema": "http://json-schema.org/draft-07/schema#",
        "properties": {
          "anonymousId": {
            "type": "string"
          },
          "userId": {
            "type": "string"
          }
        }
      }
    }
    

RudderStack supports the following keywords within an object:

Keyword| Data type| Description  
---|---|---  
`properties`| Object| Properties for the event to be upserted in Tracking Plan.  
`additionalProperties`| Boolean| Determines if RudderStack should allow any other properties apart from the ones defined in `properties`.  
`required`| Boolean| Determines if a property is required or optional for the event.  
  
A sample schema definition for an object:
    
    
    {
      "type": "object",
      "properties": {
        "number": {
          "type": "number"
        },
        "street_name": {
          "type": "string"
        },
        "street_type": {
          "enum": ["Street", "Avenue", "Boulevard"]
        }
      },
      "additionalProperties": false
    }
    

The following snippet highlights a JSON compliant with the above schema:
    
    
    {
      "number": 1600,
      "street_name": "Pennsylvania",
      "street_type": "Avenue"
    }
    

The above schema definition invalidates the following JSON as it contains an undefined property `direction` and `additionalProperties` is set to false:
    
    
    {
      "number": 1600,
      "street_name": "Pennsylvania",
      "street_type": "Avenue",
      "direction": "North-west"
    }
    

> ![warning](/docs/images/warning.svg)
> 
> RudderStack restricts usage of the following object data type keywords:
> 
>   * [`patternProperties`](<https://json-schema.org/understanding-json-schema/reference/object#patternProperties>)
>   * [`unevaluatedProperties`](<https://json-schema.org/understanding-json-schema/reference/object#unevaluatedproperties>)
>   * [`propertyNames`](<https://json-schema.org/understanding-json-schema/reference/object#propertyNames>)
>   * [`maxProperties`, `minProperties`](<https://json-schema.org/understanding-json-schema/reference/object#size>)
> 


#### Arrays

You can use [arrays](<https://json-schema.org/understanding-json-schema/reference/array>) for ordered elements.

> ![info](/docs/images/info.svg)
> 
> RudderStack expects only objects to be present within an array.

There are two ways of using arrays in JSON:

  * List validation: Sequence of arbitrary length where each item matches the same schema.
  * Tuple validation: Sequence of fixed length where each item can have a different schema.


> ![info](/docs/images/info.svg)
> 
> RudderStack supports only list validation and the [`items`](<https://json-schema.org/understanding-json-schema/reference/array#items>) keyword to validate the items in the array.

RudderStack supports the following advanced keywords for arrays:

  * `minItems`
  * `maxItems`
  * `uniqueItems`


A sample schema definition for an array:
    
    
    {
      "type": "array",
      "items": {
        "type": "number"
      },
      "minItems": 2,
      "maxItems": 3,
      "uniqueItems": true
    }
    

Some examples of data that are compliant and non-compliant to the above schema:
    
    
    - [1,2,3,4,5]
    - [1,2,3]
    
    
    
    - [1,2,"3",4,5]
    - []
    - [1]
    

> ![warning](/docs/images/warning.svg)
> 
> RudderStack restricts usage of the following keywords:
> 
>   * [`prefixItems`](<https://json-schema.org/understanding-json-schema/reference/array#additionalitems>)
>   * [`unevaluatedItems`](<https://json-schema.org/understanding-json-schema/reference/array#unevaluateditems>)
>   * [`contains`](<https://json-schema.org/understanding-json-schema/reference/array#contains>)
>   * [`maxContains`, `minContains`](<https://json-schema.org/understanding-json-schema/reference/array#mincontains-maxcontains>)
> 


##### **Nesting properties**

> ![info](/docs/images/info.svg)
> 
> This section is applicable to objects and array data types.

RudderStack supports defining complex nested properties within an object or array while defining the event properties.

A sample object highlighting the nested properties is shown:
    
    
    {
      "type": "object",
      "properties": {
        "traits": {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "industry": {
              "type": "string"
            },
            "plan": {
              "type": "string"
            }
          }
        }
      }
    }
    

Note that:

  * RudderStack supports up to three levels of nesting within an event property.
  * You can nest properties only within an object or an array.
  * Removing the parent object or array automatically removes all the nested properties.
  * If not explicitly declared, RudderStack allows all data types for a property by default. However, it **does not** support nesting for that property.
  * You **cannot** nest properties within a property having both array and object data types.


#### Enum

You can use the `enum` keyword to restrict a field to a fixed set of values.

Note that an `enum` must be an array satisfying the following conditions:

  * It contains at least one element.
  * Each element must be unique.


A sample schema definition for `enum`:
    
    
    {
     "enum": ["Red", "Green", "Amber", null, 100]
    }
    

Some examples of data that are compliant and non-compliant to the above schema:
    
    
    - "Red"
    - "Green"
    - null
    
    
    
    - "Blue"
    - 0
    

#### Boolean

The [boolean](<https://json-schema.org/understanding-json-schema/reference/boolean>) data type supports only two values - `true` and `false`. RudderStack does not support values that evaluate to `true` or `false`, like `1` and `0`.

A sample schema definition for a boolean:
    
    
    {
      "type": "boolean"
    }
    

#### Null

The [null](<https://json-schema.org/understanding-json-schema/reference/null>) data type accepts only one value - `null`.

A sample schema definition for null data type:
    
    
    {
      "type": "null"
    }
    

Some examples of data that are compliant and non-compliant to the **Null** schema shown above:
    
    
    - null
    
    
    
    - false
    - 0
    - ""
    

## Multi data types

RudderStack also supports specifying multi data types for the event properties along with the above data types.

A sample schema definition for multi data types:
    
    
    {
      "type": ["string", "integer", "boolean", "null"]
    }
    

Some examples of data that are compliant and non-compliant to the above schema:
    
    
    - "Hello"
    - 12
    - true
    - null
    
    
    
    - 3.1415926
    - [1,2,3,4,5]
    

## Metadata

You can use the `metadata` parameter to provide generic keywords such as [annotations](<https://json-schema.org/understanding-json-schema/reference/annotations>) and [comments](<https://json-schema.org/understanding-json-schema/reference/comments>) to provide additional context and meaning to your JSON schema.

RudderStack supports the below generic keywords:

Keyword| Description  
---|---  
`$id`| Unique identifier for the schema resource.  
`$schema`| JSON schema dialect identifier.  
`title`| String for the title of the data.  
`description`| String describing the data’s purpose.  
`default`| String specifying a default value  
`examples`| An array of examples that validate against the schema.  
`$comment`| String for the user-defined comments added to the schema.  
`readOnly`| Boolean indicating that the value is read-only and should not be modified.  
`writeOnly`| Boolean indicating that a value may be set but will remain hidden.  
`deprecated`| Boolean indicating that [instance](<https://json-schema.org/learn/glossary#instance>) value the keyword applies to may be deprecated in the future.  
  
## Restricted keyword structures

Apart from the data type-specific keywords, RudderStack also restricts usage of the following keyword structures:

  * [const](<https://json-schema.org/understanding-json-schema/reference/const>)
  * [Conditional subschemas](<https://json-schema.org/understanding-json-schema/reference/conditionals>)
  * [String encoding non-JSON data](<https://json-schema.org/understanding-json-schema/reference/non_json_data>)
  * [Complex schema structures](<https://json-schema.org/understanding-json-schema/structuring>)