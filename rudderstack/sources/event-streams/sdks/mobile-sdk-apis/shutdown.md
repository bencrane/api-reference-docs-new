# Shutdown API in Mobile SDKs

Learn about the Shutdown API available in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __less than a minute

  * 


This guide walks you through the `shutdown` API provided by the RudderStack [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) and [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDKs.

## Overview

The RudderStack Android (Kotlin) and iOS (Swift) SDKs provide a `shutdown` API that lets you:

  * Stop all the operations
  * Remove all plugins, and
  * Free up the resources associated with the analytics instance initialized by the SDK


## Method definition

The following sections highlight how to use the `shutdown` API:

### Android (Kotlin)
    
    
    analytics.shutdown()
    
    
    
    analytics.shutdown();
    

### iOS (Swift)
    
    
    analytics.shutdown()
    
    
    
    [self.analytics shutdown];
    

## Considerations

Note the following before using the `shutdown` API:

  * **The shutdown operation is irreversible** — the `Analytics` instance cannot be used further once it is shut down.
  * All SDK APIs will stop working once the `Analytics` instance is shut down and any API call will log an error. Also, any getter API call will return `null`.
  * All events recorded up to the shutdown point are written to disk but they are only flushed after the next initialization.
  * No saved data is lost — any data that persists on disk is processed upon the next SDK initialization.