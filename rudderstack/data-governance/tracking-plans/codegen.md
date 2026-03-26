# Code Generation (Codegen) Beta

Generate language-specific code snippets based on your defined event schemas.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __2 minute read

  * 


> ![announcement](/docs/images/announcement.svg)
> 
> This feature is in **Public Beta** as part of RudderStack’s [Early Access Program](<https://www.rudderstack.com/docs/get-started/alpha-and-beta-features/beta-features/public-beta/>), where we work with early users and customers to test new features and get feedback before making them generally available.
> 
> [Contact the Product team](<mailto:product@rudderstack.com>) if you have any questions.

The **Code Generation** (Codegen) feature in Tracking Plans automatically generates language-specific code snippets based on your defined event schemas. This streamlines the instrumentation process by providing accurate code represents the schema definition, including:

  * Clear structure of the `properties` object
  * Correct keys
  * Examples that represent the correct data type
  * Comments that specify whether properties are optional


## Access codegen

  1. Go to **Govern** > **Tracking Plans**.
  2. Click the tracking plan and select the event to view the generated code snippet.

[![Tracking plan codegen](/docs/images/data-governance/codegen.webp)](</docs/images/data-governance/codegen.webp>)

## Supported languages

Currently, the Codegen feature **only generates snippets for the JavaScript SDK**. Support for additional languages is coming soon.

## RudderTyper

Generated code snippets are helpful, but the best way to make it easy for instrumenting events correctly is to use [RudderTyper](<https://www.rudderstack.com/docs/dev-tools/ruddertyper/>) in your IDE.

> ![info](/docs/images/info.svg)
> 
> RudderTyper is a linting tool that generates and autocompletes typesafe code from tracking plan schemas.

#### Example

The below image shows how RudderStack translates the schema definition into the code snippet:

[![Code generation example screenshot](/docs/images/data-governance/tracking-plans/code-generation-example.png)](</docs/images/data-governance/tracking-plans/code-generation-example.png>)

In this example:

  * The value of `price` is set to an example integer.
  * The `category` property is followed by `// optional`, denoting that it is not required.
  * The `product_details` property is structured as an object.
  * Value of the `sale` property is set to an example for a Boolean type.