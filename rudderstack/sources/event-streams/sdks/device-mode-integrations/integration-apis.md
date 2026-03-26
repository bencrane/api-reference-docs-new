# Device Mode Integration APIs

Complete API reference for device mode integration APIs in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __4 minute read

  * 


This reference provides the complete API specifications for device mode integration APIs in the RudderStack [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) and [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDKs.

## `onDestinationReady()`

`onDestinationReady()` registers a callback to be invoked when the destination for an integration plugin is ready. Use this method to perform actions **only after** the destination has been successfully configured and initialized. For example, fetching an ID from the destination instance or initializing resources.

### Behavior

  * If the destination is ready, the callback is invoked immediately with the destination instance and a success result.
  * If the destination is not ready, the callback is stored and invoked once initialization completes (or fails).


### Android (Kotlin)

This section covers the `onDestinationReady()` method signature, parameters, and return type applicable for the Android (Kotlin) SDK.

#### Method signature
    
    
    fun onDestinationReady(callback: (Any?, Result<Any>) -> Unit)
    

#### Parameters

  * `callback`: A lambda function that receives:

    * `instance`: The destination instance (`Any?`) - `null` if initialization failed
    * `result`: A `Result<Any>` indicating success or failure


#### Return type

  * `Unit`


#### Example
    
    
    integrationPlugin.onDestinationReady { instance, result ->
        if (result is Result.Success) {
            // Destination is ready
            println("Destination is ready: $instance")
        } else {
            // Handle initialization failure
            println("Destination initialization failed: ${(result as Result.Failure).exception.message}")
        }
    }
    
    
    
    integrationPlugin.onDestinationReady((instance, result) -> {
        if (result instanceof Result.Success) {
            // Destination is ready
            System.out.println("Destination is ready: " + instance);
        } else if (result instanceof Result.Failure) {
            // Handle initialization failure
            Exception exception = ((Result.Failure) result).getException();
            System.out.println("Destination initialization failed: " + exception.getMessage());
        }
    });
    

### iOS (Swift)

This section covers the `onDestinationReady()` method signature, parameters, and return type applicable for the iOS (Swift) SDK.

#### Method signature
    
    
    func onDestinationReady(_ callback: @escaping (Any?, Result<Any, Error>) -> Void)
    

#### Parameters

  * `callback`: A closure that receives:
    * `instance`: The destination instance (`Any?`) - `nil` if initialization failed
    * `result`: A `Result<Any, Error>` indicating success or failure


#### Return type

  * `Void`


#### Example
    
    
    integrationPlugin.onDestinationReady { instance, result in
        switch result {
        case .success:
            // Destination is ready, safe to send events
            print("Destination is ready: \(String(describing: instance))")
        case .failure(let error):
            // Handle initialization failure
            print("Destination initialization failed: \(error.localizedDescription)")
        }
    }
    
    
    
    [self.analytics onDestinationReadyForKey:integration.key :^(id _Nullable destination, NSError * _Nullable error) {
        if (error == nil) {
            // Destination is ready, safe to send events
            [RSSLoggerAnalytics debug:[NSString stringWithFormat:@"Destination is ready: %@", destination]];
        } else {
            // Handle initialization failure
            [RSSLoggerAnalytics debug:[NSString stringWithFormat:@"Destination initialization failed: %@", [error localizedDescription]]];
        }
    }];
    

## `getDestinationInstance()`

`getDestinationInstance()` returns the destination instance that was created and initialized by the integration plugin. This allows direct access to the destination object for advanced use cases like interacting with the destination SDK, accessing APIs, or implementing install attribution.

### Behavior

  * Returns the destination instance if available
  * Returns `null` or `nil` if not yet initialized


### Android (Kotlin)

This section covers the `getDestinationInstance()` method signature, parameters, and return type applicable for the Android (Kotlin) SDK.

#### Method signature
    
    
    fun getDestinationInstance(): Any?
    

#### Parameters

  * None


#### Return type

  * `Any?`: The destination instance, or `null` if not initialized


#### Example
    
    
    val destination = integrationPlugin.getDestinationInstance()
    if (destination != null) {
        // Interact with the destination SDK
        println("Destination instance: $destination")
        // Cast to specific destination type if needed
        // val firebaseDestination = destination as? FirebaseAnalytics
    }
    
    
    
    Object destination = integrationPlugin.getDestinationInstance();
    if (destination != null) {
        // Interact with the destination SDK
        System.out.println("Destination instance: " + destination);
        // Cast to specific destination type if needed
        // FirebaseAnalytics firebaseDestination = (FirebaseAnalytics) destination;
    }
    

### iOS (Swift)

This section covers the `getDestinationInstance()` method signature, parameters, and return type applicable for the iOS (Swift) SDK.

#### Method signature
    
    
    func getDestinationInstance() -> Any?
    

#### Parameters

  * None


#### Return type

  * `Any?`: The destination instance, or `nil` if not initialized


#### Example
    
    
    if let destination = integrationPlugin.getDestinationInstance() {
        // Interact with the destination SDK
        print("Destination instance: \(destination)")
        // Cast to specific destination type if needed
        // let firebaseDestination = destination as? Analytics
    }
    
    
    
    id destination = [integration getDestinationInstance];
    if (destination != nil) {
        // Interact with the destination SDK
        [RSSLoggerAnalytics debug:[NSString stringWithFormat:@"Destination instance: %@", destination]];
        // Cast to specific destination type if needed
        // Analytics *firebaseDestination = [integration getDestinationInstance];
    }
    

## When to use each API

Use `onDestinationReady()` when:

  * You need to perform critical startup logic that requires the destination to be ready
  * You want guaranteed access to a non-null instance via an asynchronous callback
  * You need to handle initialization failures explicitly


Use `getDestinationInstance()` when:

  * You need on-demand access later in the app lifecycle
  * You want to avoid callback overhead
  * You can handle a `null` or `nil` return value if the instance isn’t ready yet


## Error conditions

This section covers the error conditions for the `onDestinationReady()` and `getDestinationInstance()` APIs.

### `onDestinationReady()`

The callback receives a failure result in the following cases:

  * The destination SDK initialization throws an exception
  * The destination plugin fails to create the destination instance
  * The destination configuration is invalid or missing required parameters


> ![info](/docs/images/info.svg)
> 
> You can access the error details through the `Result.Failure` object (Android) or `Error` parameter (iOS) in the callback.

### `getDestinationInstance()`

Returns `null` (Android) or `nil` (iOS) when:

  * The destination has not been initialized yet
  * The destination initialization failed
  * The integration plugin was not added to the `Analytics` instance


## See more

  * [How to Use Device Mode Integrations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/device-mode-integrations/usage/>): Add and use device mode integrations in your mobile apps
  * [How to Build Custom Device Mode Integrations](<https://www.rudderstack.com/docs/sources/event-streams/sdks/device-mode-integrations/custom-integrations/>): Create custom device mode integrations