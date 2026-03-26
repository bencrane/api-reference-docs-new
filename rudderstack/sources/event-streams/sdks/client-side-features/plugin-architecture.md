# Plugin Architecture in Mobile SDKs

Learn about the plugin architecture in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __3 minute read

  * 


This guide covers RudderStack’s plugin architecture available for the RudderStack [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) and [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDKs.

## Overview

RudderStack’s plugin architecture lets you extend and customize event processing without modifying the core SDK. It provides flexibility by allowing you to add custom plugins at different stages of event handling.

Using this architecture, you can filter, enhance, or modify events (`identify`, `track`, `screen`, `group`, and `alias`) based on your requirement. Whether it’s pre-processing data, transforming events, or applying integration-specific modifications, you have full control over how events are handled - making the integration seamless and ensuring events are processed exactly as required.

> ![info](/docs/images/info.svg)
> 
> In this architecture, the plugins execute in a defined sequence, with each stage refining the data before passing it to the next.

## Supported plugin types

Plugin type| Description  
---|---  
`PreProcess`| Executes at the beginning to prepare data, like adding context.  
`OnProcess`| Executes while applying transformations or validations early in the pipeline.  
`Terminal`| Executes just before sending the events to the integrations or RudderStack backend (server).  
`Utility`| Executes only when manually triggered, like with a lifecycle plugin.  
  
## Plugin

A plugin is a modular component that lets you customize, enhance, or modify event processing at different stages without changing the core SDK. The plugin interface provides three **optional** methods that you can override as per your requirement:

Method| Parameter and return type| Description  
---|---|---  
`setup`| **Parameter type** : `Analytics`| Initializes the plugin by associating it with an `Analytics` instance. Use this method to also set up any plugin-specific logic, like configuring internal variables or loading the necessary data.  
`intercept`| **Parameter type** : `Event`  
**Return type** : `Event?`| Processes and (optionally) modifies the event before it moves through the pipeline. Returns the updated event or `null` to discard it.  
  
**Note** : This method is not applicable for the `Utility` plugin type.  
`teardown`| -| Handles cleanup when the plugin is removed or when `Analytics` shuts down. You can override this method to reset or clear any internal states.  
  
## Custom plugins

Custom plugins are user-defined plugins that provide flexibility in extending and modifying event processing within the SDK. Unlike built-in plugins, which are predefined within the SDK, custom plugins are entirely developed, managed, and added or removed by you after the SDK initialization.

See the following guides for more information on the various use cases for custom plugins and how to create them:

  * [Custom Plugin Use Cases](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/use-cases/>)
  * [Create Custom Plugin](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/create-custom-plugin/>)


### How custom plugins work

  * You can create and register a custom plugin at runtime, allowing for dynamic modifications without altering the core SDK.
  * These plugins can belong to any of the existing plugin types (`PreProcess`, `OnProcess`, `Terminal`, or `Utility`) and are executed at their respective stages.
  * By leveraging custom plugins, you gain greater control over event handling, making it possible to apply transformations, enrich events with additional data, filter out unwanted events, or customize behavior for specific use cases.