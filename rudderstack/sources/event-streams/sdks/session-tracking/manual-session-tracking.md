# Manual Session Tracking in RudderStack SDKs

Learn about the manual session tracking feature in RudderStack SDKs.

* * *

  * __4 minute read

  * 


This guide explains the manual session tracking feature available in the supported RudderStack SDKs ([JavaScript](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>), [Android (Java)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>), [iOS (Obj-C)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>), [React Native](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-react-native-sdk/>), and [Flutter](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-flutter-sdk/>)).

## Overview

You can use the manual session tracking feature to define the start and end of a user session.

> ![warning](/docs/images/warning.svg)
> 
> Manual session tracking overrides the [automatic session tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/automatic-session-tracking/>).

RudderStack supports the following manual session tracking methods:

Method| Parameters| Description  
---|---|---  
`startSession()`| -| RudderStack creates a new session and passes the current `timestamp` as the `sessionId` if you don't pass any parameter.  
`sessionId`  
Long integer with minimum length of 10 characters.| RudderStack triggers a new user session if you pass a custom `sessionId` parameter.  
  
RudderStack **does not recommend** using a decimal number as the `sessionId`.  
`endSession()`| -| RudderStack clears the `sessionId` and ends the session.  
  
## Persistence scope

The following sections list the persistence scope of manual session tracking in the JavaScript and mobile SDKs.

### JavaScript

The persistence scope of manual session tracking in the JavaScript SDK **does not depend** on whether [automatic session tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/automatic-session-tracking/javascript/>) is enabled.

If you call `startSession()`, the manual session continues even if you refresh or reopen the web page. To end the session, you must call `endSession()`.

> ![warning](/docs/images/warning.svg)
> 
> If you identify a user with a new `userId` in an existing session, RudderStack triggers a `reset()` call. This ends the existing session and generates a new one, irrespective of whether `endSession()` is called or not.

### Mobile SDKs

The persistence scope of manual session tracking in the mobile SDKs (Android (Java), iOS (Obj-C), React Native, and Flutter) **depends** on whether [automatic session tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/automatic-session-tracking/mobile-sdks/>) is enabled:

  * If automatic session tracking is enabled and you call `startSession()`, then RudderStack disables automatic session tracking **until the app is closed completely**. Once you restart the app, the SDKs resume automatic session tracking.
  * If automatic session tracking is disabled and you call `startSession()`, the manual session is active until you end it by calling `endSession()`.


## Sample snippets

The following snippets highlight the use of the manual session tracking methods:
    
    
    rudderanalytics.startSession() // Starts a new user session and automatically assigns a session ID.
    
    rudderanalytics.startSession(sessionId) // Passes a custom session ID while creating a new session.
    
    rudderanalytics.endSession() // Ends the user session and clears the session ID.
    

The manual session tracking methods in the Android (Java) SDK are available in the following languages:

  * Java
  * Kotlin


The following snippets highlight the use of the manual session tracking methods:
    
    
    rudderClient.startSession(); // Starts a new user session and automatically assigns a session ID.
    
    rudderClient.startSession(sessionId); // Passes a custom session ID while creating a new session.
    
    rudderClient.endSession(); // Ends the user session and clears the session ID.
    

The corresponding Kotlin code is as follows:
    
    
    // Starts a new user session and automatically assigns a session ID.
    rudderClient.startSession()
    
    // Passes a custom session ID while creating a new session.
    rudderClient.startSession(sessionId)
    
    // Ends the user session and clears the session ID.
    rudderClient.endSession()
    

The manual session tracking methods in the iOS (Obj-C) SDK are available in the following languages:

  * Swift
  * Objective-C


The following snippets highlight the use of the manual session tracking methods:
    
    
    RSClient.sharedInstance()?.startSession() // Starts a new user session and automatically assigns a session ID.
    
    RSClient.sharedInstance()?.startSession(sessionId) // Passes a custom session ID while creating a new session.
    
    RSClient.sharedInstance()?.endSession() // Ends the user session and clears the session ID.
    

The corresponding Objective-C code is as follows:
    
    
    [[RSClient sharedInstance] startSession]; // Starts a new user session and automatically assigns a session ID.
    
    [[RSClient sharedInstance] startSession:sessionId]; // Passes a custom session ID while creating a new session.
    
    [[RSClient sharedInstance] endSession]; // Ends the user session and clears the session ID.
    
    
    
    // Starts a new user session and automatically assigns a session ID.
    rudderClient.startSession();
    
    // Passes a custom session ID while creating a new session.
    rudderClient.startSession(sessionId);
    
    // Ends the user session and clears the session ID.
    rudderClient.endSession();
    
    
    
    // Starts a new user session and automatically assigns a session ID.
    rudderClient.startSession();
    
    // Passes a custom session ID while creating a new session.
    rudderClient.startSession(sessionId);
    
    // Ends the user session and clears the session ID.
    rudderClient.endSession();
    

## FAQ

See the [Session Tracking FAQ](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/faq/>) guide for answers to some commonly-asked questions on session tracking.