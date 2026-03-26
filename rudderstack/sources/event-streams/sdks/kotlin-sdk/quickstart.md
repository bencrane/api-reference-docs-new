# Android (Kotlin) SDK Quickstart

Install and use the RudderStack Android (Kotlin) SDK on your Android apps.

* * *

  * __3 minute read

  * 


This guide will walk you through setting up the Android (Kotlin) SDK and sending your first events to RudderStack.

[![Maven Central](https://img.shields.io/maven-central/v/com.rudderstack.sdk.kotlin/android?style=flat&color=blue)](<https://central.sonatype.com/artifact/com.rudderstack.sdk.kotlin/android>)

## Prerequisites

  * You must have **Android Studio** installed on your system.
  * Sign up for [RudderStack](<https://app.rudderstack.com/signup>).
  * Set up a new Android (Kotlin) source in the RudderStack dashboard and note its [write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination. ](</docs/resources/glossary/#write-key>).
  * You will also need the [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) associated with your RudderStack workspace.


## Step 1: Install Android (Kotlin) SDK

The steps covered in the below sections will help you integrate the RudderStack Android (Kotlin) SDK into your Android project:

### Add dependencies
    
    
    dependencies {
        implementation("com.rudderstack.sdk.kotlin:android:<latest-version>")
    }
    
    
    
    dependencies {
        implementation 'com.rudderstack.sdk.kotlin:android:<latest-version>'
    }
    

Add the dependency to your `libs.versions.toml` file:
    
    
    [versions]
    rudderstack = "<latest-version>"
    
    [libraries]
    rudderstack-kotlin = { module = "com.rudderstack.sdk.kotlin:android", version.ref = "rudderstack" }
    

Then, include it in your `build.gradle.kts`:
    
    
    dependencies {
        implementation(libs.rudderstack.kotlin)
    }
    

### Configure Maven Central

Make sure that Maven Central is included in your `settings.gradle.kts` file:
    
    
    pluginManagement {
        repositories {
            google()
            mavenCentral()
            gradlePluginPortal()
        }
    }
    dependencyResolutionManagement {
        repositories {
            google()
            mavenCentral()
        }
    }
    

For Groovy (`settings.gradle`), add:
    
    
    pluginManagement {
        repositories {
            google()
            mavenCentral()
            gradlePluginPortal()
        }
    }
    dependencyResolutionManagement {
        repositories {
            google()
            mavenCentral()
        }
    }
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure that your app has the necessary permissions to send network requests.

## Step 2: Initialize the SDK

Before tracking any events, initialize the Android (Kotlin) SDK in your `Application` class, as shown:
    
    
    import android.app.Application
    import com.rudderstack.sdk.kotlin.android.Analytics
    import com.rudderstack.sdk.kotlin.android.Configuration
    
    class MyApplication : Application() {
        lateinit var analytics: Analytics
    
        override fun onCreate() {
            super.onCreate()
            analytics = Analytics(
                configuration = Configuration(
                    writeKey = "WRITE_KEY",
                    application = this,
                    dataPlaneUrl = "DATA_PLANE_URL",
                )
            )
        }
    }
    
    
    
    import com.rudderstack.sdk.kotlin.android.Configuration;
    import com.rudderstack.sdk.kotlin.android.javacompat.ConfigurationBuilder;
    import com.rudderstack.sdk.kotlin.android.javacompat.JavaAnalytics;
    
    public class MyApplication extends Application {
    
        public JavaAnalytics analytics;
    
        @Override
        public void onCreate() {
            super.onCreate();
    
            Configuration configuration = new ConfigurationBuilder(this, "WRITE_KEY", "DATA_PLANE_URL")
                    .setTrackApplicationLifecycleEvents(true)
                    .setGzipEnabled(true)
                    .build();
    
            analytics = new JavaAnalytics(configuration);
        }
    }
    

Replace the `WRITE_KEY` and `DATA_PLANE_URL` parameters with the Android (Kotlin) source write key and the data plane URL obtained in Prerequisites.

## Step 3: Identify users

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) event to identify a user and associate them with their actions. It also enables you to record any traits about them like their name, email, etc.

You can use the `identify` method as follows:
    
    
    import kotlinx.serialization.json.buildJsonObject
    import kotlinx.serialization.json.put
    
    analytics.identify(
        userId = "1hKOmRA4el9Zt1WSfVJIVo4GRlm",
        traits = buildJsonObject {
            put("name", "Alex Keener")
            put("email", "alex@example.com")
        }
    )
    
    
    
    import java.util.HashMap;
    
    HashMap<String, Object> traits = new HashMap<>();
    traits.put("name", "Alex Keener");
    traits.put("email", "alex@example.com");
    
    analytics.identify("1hKOmRA4el9Zt1WSfVJIVo4GRlm", traits);
    

## Step 4: Track user actions

Once the Android (Kotlin) SDK is initialized, you can send track user actions and send them as events.

A sample [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) event triggered once the order is completed successfully is shown:
    
    
    import kotlinx.serialization.json.buildJsonObject
    import kotlinx.serialization.json.put
    analytics.track(
        name = "Order Completed",
        properties = buildJsonObject {
            put("revenue", 30)
            put("currency", "USD")
        }
    )
    
    
    
    import java.util.HashMap;
    
    HashMap<String, Object> properties = new HashMap<>();
    properties.put("revenue", 30);
    properties.put("currency", "USD");
    
    analytics.track("Order Completed", properties);
    

In the above snippet, the `track` method logs an event called `Order Completed` along with two event properties `revenue` and `currency` that provide additional context to the event.