# Migrating from Snowplow to RudderStack Beta

Migrate from Snowplow to RudderStack.

* * *

  * __13 minute read

  * 


This document covers the steps required to migrate from [Snowplow](<https://snowplow.io/>) to RudderStack and replace your instrumentation code. You can then start using the RudderStack SDKs to track your events with minimal code changes.

## Set up your RudderStack dashboard

  1. [Sign up](<https://app.rudderstack.com/signup>) for RudderStack Cloud.
  2. Set up the source-destination connections in the dashboard to facilitate event data flow. For more information on setting up connections, see the [Quickstart](<https://www.rudderstack.com/docs/data-pipelines/event-stream/quickstart/>) guide.


> ![success](/docs/images/tick.svg)
> 
> Note your [source write keyThe write key (or source write key) is a unique identifier for your source. RudderStack uses this key to send events from a source to the specified destination.](</docs/resources/glossary/#write-key>) and [data plane URLThe data plane URL is the location where events are routed and sent to the RudderStack backend for processing. You can find this URL in the home page of your RudderStack dashboard.](</docs/resources/glossary/#data-plane-url>) as they will be used in the next section.

## Update your SDK implementation

Depending on your target platform, follow these steps to move your existing Snowplow SDK implementation to RudderStack.

### Android (Java) — Legacy

RudderStack distributes the Rudder Snowplow adapter SDK through [Maven Central](<https://central.sonatype.com/artifact/com.rudderstack.android.snowplow/adapter/1.0.0.beta.1>). We recommended you add the SDK to your project through the Android Gradle build system.

  1. Add the following code in your project level `app/build.gradle` file:


    
    
    buildscript {
      repositories {
        mavenCentral()
      }
    }
    allprojects {
      repositories {
        mavenCentral()
      }
    }
    

  2. Add the following dependency under `dependencies` section in your `app/build.gradle` file:


    
    
    implementation 'com.rudderstack.android.snowplow:adapter:1.0.0.beta.1'
    

  3. Update your SDK initialization to any one of the following snippet (method 1, 2, or 3 in the following snippets). Also, replace the `WRITE_KEY` and `DATA_PLANE_URL` with your source write key and data plane URL obtained in the above section.


    
    
    //Method 1: Default values are considered for all configuration objects 
    //except networkConfiguration.
    RSTracker tracker = new RSTracker()
                .createTracker(
                    this, WRITE_KEY, networkConfiguration
                );
    
    //Method 2: Default values are considered for all configuration objects.
    RSTracker tracker = new RSTracker()
                .createTracker(
                    this, WRITE_KEY, DATA_PLANE_URL
                );
    
    //Method 3: Values for all configuration objects must be provided.
    RSTracker tracker = new RSTracker()
                .createTracker(
                    this, WRITE_KEY, networkConfiguration,
                    sessionConfiguration, trackerConfiguration,
                    subjectConfiguration
                );
    
    
    
    //Method 1: Default values are considered for all configuration objects 
    //except networkConfiguration.
    val tracker = RSTracker()
                .createTracker(
                    this, WRITE_KEY, networkConfiguration
                )
    
    //Method 2: Default values are considered for all configuration objects.
    val tracker = RSTracker()
                .createTracker(
                    this, WRITE_KEY, DATA_PLANE_URL
                )
    
    //Method 3: Values for all configuration objects must be provided.
    val tracker = RSTracker()
                .createTracker(
                    this, WRITE_KEY, networkConfiguration,
                    sessionConfiguration, trackerConfiguration,
                    subjectConfiguration
                )
    

> ![info](/docs/images/info.svg)
> 
> Refer to the Setting the configuration objects section for more information on using these configuration objects.

### iOS (Obj-C) — Legacy

Follow these steps to migrate to the RudderStack iOS (Obj-C) SDK:

  1. Add the SDK to your `Podfile`:


    
    
    pod 'RudderSnowplowMigrator', '1.0.0.beta.1'
    

  2. Run the following command:


    
    
    pod install
    

  3. Add the following code in all `.m` and `.h` files (for Objective-C) or `.swift` files(for Swift) where you want to refer or use RudderStack SDK classes:


    
    
    @import RudderSnowplowMigrator;
    
    
    
    import RudderSnowplowMigrator
    

  4. Update your SDK initialization to any one of the following snippet (method 1, 2, or 3). Also, replace the `WRITE_KEY` and `DATA_PLANE_URL` with your source write key and data plane URL obtained in the above section.


    
    
    //Method 1: Default values are considered for all configuration objects 
    //except networkConfiguration.
    RSTracker *tracker = [RSTracker createTrackerWithWriteKey:WRITE_KEY network:networkConfig];
    
    //Method 2: Default values are considered for all configuration objects.
    RSTracker *tracker = [RSTracker createTrackerWithWriteKey:WRITE_KEY dataPlaneUrl:DATA_PLANE_URL];
    
    //Method 3: Values for all configuration objects must be provided.
    RSTracker *tracker = [RSTracker createTrackerWithWriteKey:WRITE_KEY network:networkConfig configurations:@[trackerConfig]];
    
    
    
    //Method 1: Default values are considered for all configuration objects 
    //except networkConfiguration.
    let tracker = RSTracker.createTracker(
                writeKey: WRITE_KEY,
                network: networkConfig
            )
    
    //Method 2: Default values are considered for all configuration objects.
    let tracker = RSTracker.createTracker(
                writeKey: WRITE_KEY,
                dataPlaneUrl: DATA_PLANE_URL
            )
    
    //Method 3: Values for all configuration objects must be provided.
    let tracker = RSTracker.createTracker(
                writeKey: WRITE_KEY,
                network: networkConfig,
                configurations: [trackerConfig, sessionConfig]
            )
    

> ![info](/docs/images/info.svg)
> 
> Refer to the the Setting the configuration objects section for more information on using these configuration objects.

### JavaScript

To migrate to the RudderStack JavaScript SDK, add the following code snippet in the `<head>` section of your website. Also, replace the `WRITE_KEY` and `DATA_PLANE_URL` with your source write key and data plane URL obtained in the above section.
    
    
    <script>
      rs=window.rs=[],rs.snoplowAdapter=function(){rs.push(Array.prototype.slice.call(arguments))},rs.snoplowAdapter("newTracker",<WRITE_KEY>,<DATA_PLANE_URL>,{<Configurations>});
      //Optionally, use RudderStack JavaScript SDK load options
      rudderanalytics.load();
    </script>
    
    <script src="https://cdn.rudderlabs.com/adapter/sp/beta/v1/rs-sp-analytics.min.js"></script>
    

The `<Configurations>` parameter in the above snippet can be replaced by the following Snowplow properties which are mapped to the RudderStack properties as shown:

Snowplow property| RudderStack property  
---|---  
`cookieDomain`| `setCookieDomain`  
`cookieSameSite`| `sameSiteCookie`  
`cookieSecure`| `secureCookie`  
  
## Update mobile SDK configuration

RudderStack supports setting values for the following Snowplow configuration objects in the mobile SDKs (iOS (Obj-C)/Android (Java)). If not set, the default values are assigned.

### NetworkConfiguration

The [`NetworkConfiguration`](<https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/configuring-how-events-are-sent/>) class can be used to specify the collector endpoint:
    
    
    // 1
    RSNetworkConfiguration *networkConfig = [[RSNetworkConfiguration alloc] initWithDataPlaneUrl:DATA_PLANE_URL];
    // 2
    RSNetworkConfiguration *networkConfig = [[RSNetworkConfiguration alloc] initWithDataPlaneUrl:DATA_PLANE_URL controlPlaneUrl:CONTROL_PLANE_URL];
    
    
    
    // 1
    let networkConfig = NetworkConfiguration(dataPlaneUrl: DATA_PLANE_URL)
    // 2
    let networkConfig = NetworkConfiguration(dataPlaneUrl: DATA_PLANE_URL, controlPlaneUrl: CONTROL_PLANE_URL)
    
    
    
    // 1
    NetworkConfiguration networkConfiguration = new NetworkConfiguration(DATA_PLANE_URL);
    // 2
    NetworkConfiguration networkConfiguration = new NetworkConfiguration(DATA_PLANE_URL, CONTROL_PLANE_URL);
    
    
    
    // 1
    val networkConfiguration = NetworkConfiguration(DATA_PLANE_URL)
    // 2
    val networkConfiguration = NetworkConfiguration(DATA_PLANE_URL, CONTROL_PLANE_URL)
    

### SessionConfiguration

The [`SessionConfiguration`](<https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/#session>) class can be used to capture sessions to track the user activity in the app:
    
    
    RSSessionConfiguration *sessionConfig = [[RSSessionConfiguration alloc] initWithForegroundTimeout:[[NSMeasurement alloc] initWithDoubleValue:30 unit:NSUnitDuration.minutes] backgroundTimeout:[[NSMeasurement alloc] initWithDoubleValue:30 unit:NSUnitDuration.minutes]];
    
    // 2
    RSSessionConfiguration *sessionConfig = [[RSSessionConfiguration alloc] initWithForegroundTimeoutInSeconds:60 backgroundTimeoutInSeconds:60];
    
    
    
    // 1
    let sessionConfig = SessionConfiguration(
      foregroundTimeout: Measurement(value: 30, unit: .minutes),
      backgroundTimeout: Measurement(value: 30, unit: .minutes)
    )
    
    // 2
    let sessionConfig = SessionConfiguration(foregroundTimeoutInSeconds: 60, backgroundTimeoutInSeconds: 60)
    
    
    
    SessionConfiguration sessionConfiguration = new SessionConfiguration(
      new TimeMeasure(1, TimeUnit.MINUTES),
      new TimeMeasure(1, TimeUnit.MINUTES)
    );
    
    
    
    val sessionConfiguration = SessionConfiguration(
      TimeMeasure(1, TimeUnit.MINUTES),
      TimeMeasure(1, TimeUnit.MINUTES)
    );
    

> ![warning](/docs/images/warning.svg)
> 
> You need to pass both the arguments for the `SessionConfiguration` class as shown in the previous code snippets. However, RudderStack ignores the first argument (as it is a placeholder argument) and considers only the second argument (`backgroundTimeout`).

> ![info](/docs/images/info.svg)
> 
> For mobile SDKs, Snowplow’s default timeout session is 30 minutes whereas RudderStack’s default timeout session is 5 minutes. Refer to the [RudderStack Session Tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/session-tracking/#mobile-sdks>) documentation for more information.

### TrackerConfiguration

The [`TrackerConfiguration`](<https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/>) class can be used to configure contexts and automatic events of the tracker and the general behavior, as shown in the following snippets:
    
    
    RSTrackerConfiguration * trackerConfig = [
      [RSTrackerConfiguration alloc] init
    ];
    [trackerConfig base64Encoding: YES];
    [trackerConfig logLevel: LogLevelDebug];
    [trackerConfig sessionContext: YES];
    [trackerConfig deepLinkContext: YES];
    [trackerConfig applicationContext: YES];
    [trackerConfig platformContext: YES];
    [trackerConfig geoLocationContext: NO];
    [trackerConfig screenContext: YES];
    [trackerConfig screenViewAutotracking: YES];
    [trackerConfig lifecycleAutotracking: YES];
    [trackerConfig installAutotracking: YES];
    [trackerConfig exceptionAutotracking: YES];
    [trackerConfig diagnosticAutotracking: NO];
    [trackerConfig userAnonymisation: NO];
    [trackerConfig appId: APP_ID];
    
    
    
    let trackerConfig = TrackerConfiguration()
      .base64Encoding(false)
      .logLevel(.debug)
      .deepLinkContext(true)
      .applicationContext(true)
      .platformContext(true)
      .geoLocationContext(true)
      .lifecycleAutotracking(true)
      .diagnosticAutotracking(true)
      .screenViewAutotracking(true)
      .screenContext(true)
      .applicationContext(true)
      .exceptionAutotracking(true)
      .installAutotracking(true)
      .userAnonymisation(false)
      .appId(APP_ID)
    
    
    
    TrackerConfiguration trackerConfiguration = new TrackerConfiguration()
      .base64Encoding(false)
      .logLevel(LogLevel.VERBOSE)
      .deepLinkContext(true)
      .applicationContext(true)
      .platformContext(true)
      .geoLocationContext(true)
      .lifecycleAutotracking(true)
      .diagnosticAutotracking(true)
      .screenViewAutotracking(true)
      .screenContext(true)
      .applicationContext(true)
      .exceptionAutotracking(true)
      .installAutotracking(true)
      .userAnonymisation(false)
      .appId(APP_ID);
    
    
    
    val trackerConfiguration = TrackerConfiguration()
      .base64Encoding(false)
      .logLevel(LogLevel.VERBOSE)
      .deepLinkContext(true)
      .applicationContext(true)
      .platformContext(true)
      .geoLocationContext(true)
      .lifecycleAutotracking(true)
      .diagnosticAutotracking(true)
      .screenViewAutotracking(true)
      .screenContext(true)
      .applicationContext(true)
      .exceptionAutotracking(true)
      .installAutotracking(true)
      .userAnonymisation(false)
      .appId(APP_ID)
    

Snowplow automatically captures and tracks the following data. Refer to the [Auto-tracked events and entities](<https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/#auto-tracked-events-and-entities>) section for more information.

Variable name| Default value  
---|---  
`logLevel`| `LogLevel.OFF`  
`lifecycleAutotracking`| `true`  
`screenViewAutotracking`| `true`  
`sessionContext`| `true`  
  
> ![warning](/docs/images/warning.svg)
> 
> RudderStack ignores any variable other than the ones mentioned above.

### SubjectConfiguration

The [`SubjectConfiguration`](<https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/>) class can be used to capture basic user information which is attached to all events as the context entity.

> ![warning](/docs/images/warning.svg)
> 
> Snowplow does not provide any call to identify a user. However, RudderStack sends an [](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call if you initialize the `SubjectConfiguration` class while initializing the SDK. **Note that a user is not identified if the SDK is not initialized**.

The `userId` field is mapped to the RudderStack’s `userId`. All the other properties are mapped to RudderStack’s `traits` object.

> ![warning](/docs/images/warning.svg)
> 
> `userId` is a mandatory field. If not provided, the `identify` call is ignored.
    
    
    RSSubjectConfiguration * subjectConfig = [
      [RSSubjectConfiguration alloc] init
    ];
    [subjectConfig userId: @ "user_id"];
    [subjectConfig traits: @ {
      @ "key_1": @ "value_1", @ "key_2": @20, @ "key_3": @YES
    }];
    
    
    
    let subjectConfig = SubjectConfiguration()
      .userId("user_id")
      .traits(["key_1": "value_1", "key_2": 20, "key_3": true])
    
    
    
    Traits.Address address = new Traits.Address()
      .putCity("city value")
      .putCountry("country value")
      .putPostalCode("postalCode value")
      .putState("state value")
      .putStreet("street value");
    
    Traits.Company company = new Traits.Company()
      .putName("name value")
      .putId("id value")
      .putIndustry("industry value");
    
    Traits traits = new Traits()
      .putCompany(company)
      .putAddress(address)
      .putAge("age value")
      .putBirthday("birthday value")
      .putCreatedAt("createAt value")
      .putDescription("description value")
      .putEmail("email value")
      .putFirstName("fName value")
      .putGender("gender value")
      .putId("id value")
      .putLastName("lName value")
      .putName("name value")
      .putPhone("phone value")
      .putTitle("title value")
      .putUserName("userName value")
      .put("Key-1", "value-1")
      .put("Key-2", 20)
      .put("Key-3", true);
    
    SubjectConfiguration subjectConfiguration = new SubjectConfiguration()
      .userId("User-1")
      .traits(traits);
    
    
    
    val address: Traits.Address = Traits.Address()
      .putCity("city value")
      .putCountry("country value")
      .putPostalCode("postalCode value")
      .putState("state value")
      .putStreet("street value")
    
    val company: Traits.Company = Traits.Company()
      .putName("name value")
      .putId("id value")
      .putIndustry("industry value")
    
    val traits = Traits()
      .putCompany(company)
      .putAddress(address)
      .putAge("age value")
      .putBirthday("birthday value")
      .putCreatedAt("createAt value")
      .putDescription("description value")
      .putEmail("email value")
      .putFirstName("fName value")
      .putGender("gender value")
      .putId("id value")
      .putLastName("lName value")
      .putName("name value")
      .putPhone("phone value")
      .putTitle("title value")
      .putUserName("userName value")
      .put("Key-1", "value-1")
      .put("Key-2", 20)
      .put("Key-3", true)
    
    val subjectConfiguration = SubjectConfiguration()
      .userId("User-1")
      .traits(traits)
    

## Update class names

The following table lists the corresponding class names in Snowplow and RudderStack (mobile SDKs) which need to be updated based on your platform:

Snowplow| | RudderStack| |   
---|---|---|---|---  
| **Java**| **Kotlin**| **Objective-C**| **Swift**  
`NetworkConfiguration`| `NetworkConfiguration`| `NetworkConfiguration`| `RSNetworkConfiguration`| `NetworkConfiguration`  
`TrackerConfiguration`| `TrackerConfiguration`| `TrackerConfiguration`| `RSTrackerConfiguration`| `TrackerConfiguration`  
`SessionConfiguration`| `SessionConfiguration`| `SessionConfiguration`| `RSSessionConfiguration`| `SessionConfiguration`  
`SubjectConfiguration`| `SubjectConfiguration`| `SubjectConfiguration`| `RSSubjectConfiguration`| `SubjectConfiguration`  
`Structured`| `Structured`| `Structured`| `RSStructured`| `Structured`  
`ScreenView`| `ScreenView`| `ScreenView`| `RSScreenView`| `ScreenView`  
`Background`| `Background`| `Background`| `RSBackground`| `Background`  
`Foreground`| `Foreground`| `Foreground`| `RSForeground`| `Foreground`  
`SelfDescribing`| `SelfDescribing`| `SelfDescribing`| `RSSelfDescribing`| `SelfDescribing`  
`SelfDescribingJson`| `SelfDescribingJson`| `SelfDescribingJson`| `RSSelfDescribingJson`| `SelfDescribingJson`  
`TimeMeasure`| `TimeMeasure`| `TimeMeasure`| `N/A`| `N/A`  
`Snowplow`| `RSTracker`| `RSTracker`| `RSTracker`| `RSTracker`  
`LogLevel`| `LogLevel`| `LogLevel`| `LogLevel`| `LogLevel`  
  
## Send events

Migrate your existing events from Snowplow to RudderStack by following the below sections:

### Identify

#### iOS (Obj-C)/Android (Java)

Snowplow’s [`SubjectConfiguration`](<https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/>) class can be used to identify users. See the Setting configuration objects section for more information.

#### JavaScript

Snowplow supports identifying a user by passing the `setUserId` method. A Snowplow event including the `setUserId` method triggers the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call in the RudderStack JavaScript SDK.

> ![info](/docs/images/info.svg)
> 
> RudderStack supports only the `setUserId` method of the [Snowplow v2 JS tracker](<https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/javascript-trackers/javascript-tracker/javascript-tracker-v2/>).

In the following sample call, `alex@example.com` is the `userId`, while `firstName`, `lastName`, and `city` are the user traits.
    
    
    rs.snowplowAdapter('setUserId', 'alex@example.com', {
      firstName: 'Alex',
      lastName: 'Keener',
      city: 'New Orleans'
    });
    

### Track

#### iOS (Obj-C)/Android (Java)

##### Custom structured events

RudderStack sends a [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call for Snowplow events containing the [`Structured`](<https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/#creating-a-structured-event>) class.

In the following example, RudderStack maps `Action_example` to the RudderStack event name and the rest of the properties like `Category_example`, `label`, `value`, etc. to the RudderStack properties.
    
    
    RSStructured * structured = [
      [RSStructured alloc] initWithCategory: @ "Category_example"
      action: @ "Action_example"
    ];
    [structured label: @ "my-label"];
    [structured property: @ "my-property"];
    [structured value: @5];
    [structured properties: @ {
      @ "key_1": @ "value_1", @ "key_2": @ "value_2"
    }];
    
    [tracker track: structured];
    
    
    
    let structured = Structured(category: "Category_example", action: "Action_example")
      .label("my-label")
      .property("my-property")
      .value(5)
      .properties(["key_1": "value_1", "key_2": "value_2"])
    
    tracker.track(structured)
    
    
    
    HashMap  properties = new HashMap  ();
    properties.put("key-1", "value 1");
    properties.put("key-2", 123);
    properties.put("key-3", 123.45);
    properties.put("key-4", true);
    properties.put("key-5", false);
    
    Structured structured = new Structured("Category_example", "Action_example")
      .label("my-label")
      .value(1234.23)
      .property("my-property")
      .properties(properties);
    
    tracker.track(structured);
    
    
    
    val properties = mapOf<string any="">(
      "key-1" to "value 1",
      "key-2" to 123,
      "key-3" to 123.45,
      "key-4" to true,
      "key-5" to false
    )
    
    val structured = Structured("Category_example", "Action_example")
      .label("my-label")
      .value(1234.23)
      .property("my-property")
      .properties(properties)
    
    tracker.track(structured)
    

##### Custom self-described events

RudderStack sends a [track](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call for Snowplow events containing the [`SelfDescribing`](<https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/#creating-a-structured-event>) class.

In the following example, RudderStack maps `action` to the RudderStack event name.
    
    
    // 1
    RSSelfDescribingJson * selfDescribingJson = [
      [RSSelfDescribingJson alloc] initWithSchema: @ "schema"
      andDictionary: @ {
        @ "action": @ "Action_2", @ "key_2": @ "value_2"
      }
    ];
    RSSelfDescribing * selfDescribing = [
      [RSSelfDescribing alloc] initWithEventData: selfDescribingJson
    ];
    
    // 2
    RSSelfDescribing * selfDescribing = [
      [RSSelfDescribing alloc] initWithSchema: @ "schema"
      payload: @ {
        @ "action": @ "Action_2", @ "key_2": @ "value_2"
      }
    ];
    
    [tracker track: selfDescribing];
    
    
    
    // 1
    let selfDescribingJson = SelfDescribingJson(schema: "schema", andDictionary: ["action": "Action_2"])
    let selfDescribing = SelfDescribing(eventData: selfDescribingJson)
    
    // 2
    let selfDescribing = SelfDescribing(schema: "schema", payload: ["action": "Action_2"])
    
    tracker.track(selfDescribing)
    
    
    
    HashMap  properties = new HashMap  ();
    properties.put("action", "Action-2");
    properties.put("key-1", "value 1");
    
    // 1
    SelfDescribingJson selfDescribingJson = new SelfDescribingJson("schema", payload)
    SelfDescribing selfDescribing = new SelfDescribing(selfDescribingJson)
    
    // 2
    SelfDescribing selfDescribing = new SelfDescribing("schema", payload)
    
    tracker.track(selfDescribing);
    
    
    
    val payload = mapOf  (
    	  "action" to "Action-2",
    	  "key-2" to "value-2"
    	)
    
    // 1
    val selfDescribingJson = SelfDescribingJson("schema", payload)
    val selfDescribing = SelfDescribing(selfDescribingJson)
    
    // 2
    val selfDescribing = SelfDescribing("schema", payload)
    
    tracker.track(selfDescribing)
    

> ![info](/docs/images/info.svg)
> 
> `action` is a mandatory field. RudderStack does not send any call if it is absent.

##### Custom foreground events

RudderStack sends a [track](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call for Snowplow events containing the [`Foreground`](<https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/previous-versions/objective-c-tracker/objective-c-1-0-0/#foreground-and-background-events>) class.

RudderStack sends the event name as `Application Opened` and maps the rest of the properties like `index`, `properties`, etc. to the RudderStack properties.
    
    
    RSForeground * foreground = [
      [RSForeground alloc] initWithIndex: @1
    ];
    [foreground properties: @ {
      @ "key_1": @ "value_1"
    }];
    
    [tracker track: foreground];
    
    
    
    let foreground = Foreground(index: 1)
      .properties(["key_1": "value_1"])
    
    tracker.track(foreground)
    
    
    
    HashMap  properties = new HashMap  ();
    properties.put("key-1", "value 1");
    properties.put("key-2", 123);
    properties.put("key-3", 123.45);
    properties.put("key-4", true);
    properties.put("key-5", false);
    
    Foreground foreground = new Foreground(1234);
    foreground.setProperties(properties);
    
    tracker.track(foreground);
    
    
    
    val properties = mapOf<string any="">(
      "key-1" to "value 1",
      "key-2" to 123,
      "key-3" to 123.45,
      "key-4" to true,
      "key-5" to false
    )
    
    Foreground foreground = Foreground(1234)
    foreground.properties = properties
    
    tracker.track(background)
    

> ![info](/docs/images/info.svg)
> 
> This is not a default [application lifecycle event](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/>). Hence, the properties like `version`, `build`, etc. are not present under `properties`.

##### Custom background events

RudderStack sends a [track](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call for Snowplow events containing the [`Background`](<https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/previous-versions/objective-c-tracker/objective-c-1-0-0/#foreground-and-background-events>) class.

RudderStack sends the event name as `Application Backgrounded` and maps the rest of the properties, like `index`, `properties`, etc. to the RudderStack properties.
    
    
    RSBackground * background = [
      [RSBackground alloc] initWithIndex: @1
    ];
    [background properties: @ {
      @ "key_1": @ "value_1"
    }];
    
    [tracker track: background];
    
    
    
    let background = Background(index: 1)
      .properties(["key_1": "value_1"])
    
    tracker.track(background)
    
    
    
    HashMap  properties = new HashMap  ();
    properties.put("key-1", "value 1");
    properties.put("key-2", 123);
    properties.put("key-3", 123.45);
    properties.put("key-4", true);
    properties.put("key-5", false);
    
    Background background = new Background(1234);
    background.setProperties(properties);
    
    tracker.track(background);
    
    
    
    val properties = mapOf<string any="">(
      "key-1" to "value 1",
      "key-2" to 123,
      "key-3" to 123.45,
      "key-4" to true,
      "key-5" to false
    )
    
    Background background = Background(1234)
    background.properties = properties
    
    tracker.track(background)
    

> ![info](/docs/images/info.svg)
> 
> This is not a default [application lifecycle event](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/>). Hence, the properties like `version`, `build`, etc. are not present under `properties`.

#### JavaScript

The RudderStack JavaScript SDK supports Snowplow’s `trackStructEvent` and `trackSelfDescribingEvent` calls. These Snowplow calls capture user events along with their associated properties and trigger the [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call in the RudderStack JavaScript SDK.

A sample `trackSelfDescribingEvent` call:
    
    
    rs.snowplowAdapter('trackSelfDescribingEvent', {
      event: {
        data: {
          action: 'order completed',
          category: 'FCW',
          product_id: 'P1100DFG9766',
          revenue: 30,
          currency: 'USD',
          user_actual_id: 12345,
        },
      },
    }); 
    

In the previous code snippet, the `trackSelfDescribingEvent` method tracks the `Order Completed` event along with other information like `revenue`, `currency`, and `user_actual_id`, etc.

A sample `trackStructEvent` call:
    
    
    rs.snowplowAdapter('trackStructEvent', {
      action: 'order completed',
      category: 'FCW',
      label: 'Sample label',
      property: 'Some property',
      value: 40.0,
    });
    

In the previous code snippet, the `trackStructEvent` method tracks the `Order Completed` event along with other information like `label`, `property`, and `value`, etc.

> ![info](/docs/images/info.svg)
> 
> The `action` field is mandatory in both calls.

### Track page or screen views

#### iOS (Obj-C)/Android (Java)

Snowplow’s [`ScreenView`](<https://docs.snowplow.io/docs/collecting-data/collecting-from-own-applications/mobile-trackers/tracking-events/#creating-a-structured-event>) class captures whenever a new screen is loaded. A Snowplow event including the `ScreenView` class triggers the [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call in the RudderStack iOS (Obj-C) or Android (Java) SDK.

RudderStack maps the `name` property to RudderStack event name and the rest of the properties, like `screenId`, `previousName`, `previousId`, etc. to the RudderStack properties.
    
    
    RSScreenView * screen = [
      [RSScreenView alloc] initWithName: @ "DemoScreenName"
      screenId: [
        [NSUUID alloc] init
      ]
    ];
    [screen type: @ "type"];
    [screen previousName: @ "previousName"];
    [screen previousId: @ "previousId"];
    [screen previousType: @ "previousType"];
    [screen transitionType: @ "transitionType"];
    [screen viewControllerClassName: @ "viewControllerClassName"];
    [screen topViewControllerClassName: @ "topViewControllerClassName"];
    [screen properties: @ {
      @ "key_1": @ "value_1",
        @ "key_2": @ "value_2"
    }];
    
    [tracker track: screen];
    
    
    
    let screen = ScreenView(name: "DemoScreenName", screenId: UUID())
      .type("type")
      .previousName("previousName")
      .previousId("previousId")
      .previousType("previousType")
      .transitionType("transitionType")
      .viewControllerClassName("viewControllerClassName")
      .topViewControllerClassName("topViewControllerClassName")
      .properties: ([
        "key_1": "value_1",
        "key_2": "value_2"
      ])
    
    tracker.track(screen)
    
    
    
    ScreenView screenView = new ScreenView("MainActivity", UUID.randomUUID())
      .type("type")
      .previousName("previousName")
      .previousId("previousId")
      .previousType("previousType")
      .transitionType("transitionType");
    
    tracker.track(screenView);
    
    
    
    val screenView = ScreenView("MainActivity", UUID.randomUUID())
      .type("type")
      .previousName("previousName")
      .previousId("previousId")
      .previousType("previousType")
      .transitionType("transitionType")
    
    tracker.track(screenView)
    

#### JavaScript

Snowplow’s `trackPageView` call lets you record your website’s page views with any additional relevant information about the viewed page. A Snowplow event including the `trackPageView` call triggers the [screen](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call in the RudderStack JavaScript SDK.

A sample `trackPageView` call:
    
    
    rs.snowplowAdapter(
      'trackPageView',
      {
        title: 'Cart Viewed',
      },
      {
        path: '/best-seller/1',
        referrer: 'https://www.google.com/search?q=estore+bestseller',
        search: 'estore bestseller',
        title: 'The best sellers offered by EStore',
        url: 'https://www.estore.com/best-seller/1',
      },
    );
    

In the previous code snippet, the SDK captures the page title and other [contextual information](<https://www.rudderstack.com/docs/event-spec/standard-events/common-fields/#contextual-fields>).