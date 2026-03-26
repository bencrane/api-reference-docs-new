# Logging APIs in Mobile SDKs

Learn about the different logging APIs available in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __5 minute read

  * 


This guide walks you through the logging APIs available in the RudderStack [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) and [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDKs.

## Overview

The RudderStack Android (Kotlin) and iOS (Swift) SDKs provide a flexible and configurable logging mechanism that helps you:

  * Monitor and debug the SDK’s behavior.
  * Get fine-grained control over the amount of information to be recorded by leveraging multiple log levels.
  * Set up and use a custom logging mechanism and log your own messages by leveraging the SDK’s logging APIs.


## Set the log level

You can define the log level using `LoggerAnalytics` by passing the value for the `logLevel` parameter. It controls the verbosity of the logs printed by the SDK and helps filter out logs based on their importance.

The Android (Kotlin) and iOS (Swift) SDKs support the following log levels:

Log level| Description  
---|---  
`VERBOSE`| Logs all the messages, including detailed internal operations. It is useful for deep debugging.  
`DEBUG`| Logs detailed information relevant for debugging and omits the additional internal logs.  
`INFO`| Logs general operational information about the SDK’s execution and helps track high-level flow.  
`WARN`| Logs potentially problematic situations that may not cause immediate failures. It is useful for detecting any unusual SDK behavior.  
`ERROR`| Logs only serious issues that impact the SDK’s functionality and require attention.  
`NONE`| Disables all logging. Use it when logging is unnecessary or needs to be disabled in production.  
  
The following sections show you how to set a `VERBOSE` log level in Android (Kotlin) and iOS (Swift) SDKs.

### Android (Kotlin)
    
    
    LoggerAnalytics.logLevel = Logger.LogLevel.VERBOSE
    
    
    
    LoggerAnalytics.INSTANCE.setLogLevel(Logger.LogLevel.VERBOSE);
    

### iOS (Swift)
    
    
    LoggerAnalytics.logLevel = LogLevel.VERBOSE
    
    
    
    [RSSLoggerAnalytics setLogLevel: RSSLogLevelVerbose];
    

## Set custom logs

The Android (Kotlin) and iOS (Swift) SDKs provide a `LoggerAnalytics` instance that you can use to set custom logs for the SDK. It is helpful when the SDK logs need to be printed in a [custom plugin](<https://www.rudderstack.com/docs/sources/event-streams/sdks/client-side-features/plugin-architecture/#custom-plugins>).

The SDKs provide the following methods for printing different levels of log messages:

### Android (Kotlin)
    
    
    // Verbose log message
    LoggerAnalytics.verbose("This is a verbose log message providing detailed internal information.")
    
    // Debug log message
    LoggerAnalytics.debug("Debugging info: API request started.")
    
    // Info log message
    LoggerAnalytics.info("SDK initialized successfully.")
    
    // Warn log message
    LoggerAnalytics.warn("Low memory warning detected.")
    
    // Error log message
    LoggerAnalytics.error("Failed to fetch user data: Network error.")  
    
    
    
    // Verbose log message
    LoggerAnalytics.INSTANCE.verbose("This is a verbose log message providing detailed internal information.")
    
    // Debug log message
    LoggerAnalytics.INSTANCE.verbose("Debugging info: API request started.")
    
    // Info log message
    LoggerAnalytics.INSTANCE.verbose("SDK initialized successfully.")
    
    // Warn log message
    LoggerAnalytics.INSTANCE.verbose("Low memory warning detected.")
    
    // Error log message
    LoggerAnalytics.INSTANCE.verbose("Failed to fetch user data: Network error.") 
    

### iOS (Swift)
    
    
    // Verbose log message
    LoggerAnalytics.verbose(log: "This is a verbose log message providing detailed internal information.")
    
    // Debug log message
    LoggerAnalytics.debug(log: "Debugging info: API request started.")
    
    // Info log message
    LoggerAnalytics.info(log: "SDK initialized successfully.")
    
    // Warn log message
    LoggerAnalytics.warn(log: "Low memory warning detected.")
    
    // Error log message
    LoggerAnalytics.error(log: "Failed to fetch user data: Network error.")
    
    
    
    // Verbose log message
    [RSSLoggerAnalytics verbose: @"This is a verbose log message providing detailed internal information."];
        
    // Debug log message
    [RSSLoggerAnalytics debug: @"Debugging info: API request started."];
        
    // Info log message
    [RSSLoggerAnalytics info: @"SDK initialized successfully."];
        
    // Warn log message
    [RSSLoggerAnalytics warn: @"Low memory warning detected."];
        
    // Error log message
    [RSSLoggerAnalytics error:@"Failed to fetch user data: Network error." error:nil];
    

## Use a custom logger

You can create and use a custom logger that is used by the Kotlin and iOS (Swift) SDKs to log messages — this is helpful in cases where you don’t want to rely on the SDK’s default logger.

### Android (Kotlin)

For the Android (Kotlin) SDK, you can inherit the `Logger` interface to create a custom `Logger` class and then pass its instance to the `setLogger` API.

For example, follow these steps to use the [Timber](<https://github.com/JakeWharton/timber>) library for logging:

  1. Create a custom logger class:


    
    
    class MyCustomLogger : Logger {
        private val tag = "MyCustomTag"
    
        override fun verbose(log: String) {
            Timber.tag(tag).v(log)
        }
    
        override fun debug(log: String) {
            Timber.tag(tag).d(log)
        }
    
        override fun info(log: String) {
            Timber.tag(tag).i(log)
        }
    
        override fun warn(log: String) {
            Timber.tag(tag).w(log)
        }
    
        override fun error(log: String, throwable: Throwable?) {
            Timber.tag(tag).e(throwable, log)
        }
    }
    
    
    
    import androidx.annotation.NonNull;
    import com.rudderstack.sdk.kotlin.core.internals.logger.Logger;
    public class JavaCustomLogger implements Logger {
        private final String TAG = "MyCustomTag";
        @Override
        public void verbose(@NonNull String log) {
            System.out.println(TAG + ": Verbose: " + log);
        }
        @Override
        public void debug(@NonNull String log) {
            System.out.println(TAG + ": Debug: " + log);
        }
        @Override
        public void info(@NonNull String log) {
            System.out.println(TAG + ": Info: " + log);
        }
        @Override
        public void warn(@NonNull String log) {
            System.out.println(TAG + ": Warn: " + log);
        }
        @Override
        public void error(@NonNull String log, Throwable throwable) {
            System.out.println(TAG + ": Error: " + log);
        }
    }
    

  2. Add the custom logger class to `LoggerAnalytics`, as shown:


    
    
    LoggerAnalytics.setLogger(MyCustomLogger())
    
    
    
    LoggerAnalytics.INSTANCE.setLogger(new JavaCustomLogger());
    

### iOS (Swift)

For the iOS (Swift) SDK, you can inherit the `Logger` protocol to create a custom `Logger` class and then pass its instance to the `setLogger` API of `LoggerAnalytics`.

  1. Create a custom logger, as shown:


    
    
    class MyCustomLogger: Logger {
        private let tag = "MyCustomTag"
        
        func verbose(log: String) {
            print("\(tag) :: Verbose :: \(log)")
        }
        
        func debug(log: String) {
            print("\(tag) :: Debug :: \(log)")
        }
        
        func info(log: String) {
            print("\(tag) :: Info :: \(log)")
        }
        
        func warn(log: String) {
            print("\(tag) :: Warn :: \(log)")
        }
        
        func error(log: String, error: (any Error)?) {
            print("\(tag) :: Error :: \(log)")
            if let error {
                print("\(tag) :: Error Details :: \(error)")
            }
        }
    }
    
    
    
    @implementation MyCustomLogger {
        NSString *tag;
    }
    
    - (instancetype)init {
        self = [super init];
        if (self) {
            tag = @"MyCustomTag";
        }
        return self;
    }
    
    - (void)verbose:(NSString *)log {
        NSLog(@"%@ :: Verbose :: %@", tag, log);
    }
    
    - (void)debug:(NSString *)log {
        NSLog(@"%@ :: Debug :: %@", tag, log);
    }
    
    - (void)info:(NSString *)log {
        NSLog(@"%@ :: Info :: %@", tag, log);
    }
    
    - (void)warn:(NSString *)log {
        NSLog(@"%@ :: Warn :: %@", tag, log);
    }
    
    - (void)error:(NSString *)log error:(NSError * _Nullable)error {
        NSLog(@"%@ :: Error :: %@", tag, log);
        if (error) {
            NSLog(@"%@ :: Error Details :: %@", tag, error);
        }
    }
    
    @end
    

  2. Add `MyCustomLogger` to the `LoggerAnalytics` instance, as shown:


    
    
    LoggerAnalytics.setLogger(MyCustomLogger())
    
    
    
    [RSSLoggerAnalytics setLogger: [MyCustomLogger new]];