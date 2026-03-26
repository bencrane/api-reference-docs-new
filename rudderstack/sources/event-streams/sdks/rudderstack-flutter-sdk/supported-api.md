# Flutter SDK API

Track and send events using the various Flutter SDK API.

* * *

  * __8 minute read

  * 


The Flutter SDK provides a comprehensive API that lets you track and send your event data to any destination.

## Identify

The [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call lets you identify a visiting user and associate them to their actions. It also lets you record the traits about them like their name, email address, etc.

A sample `identify` event is shown below:
    
    
    RudderTraits traits = RudderTraits();
    traits.putBirthdayDate(DateTime.now());
    traits.putEmail("alex@example.com");
    traits.putFirstName("Alex");
    traits.putLastName("Keener");
    traits.putGender("Male");
    traits.putPhone("5555555555");
    
    Address address = Address();
    address.putCity("City");
    address.putCountry("USA");
    traits.putAddress(address);
    
    traits.put("boolean", true);
    traits.put("integer", 50);
    traits.put("float", 120.4);
    traits.put("long", 1234);
    traits.put("string", "hello");
    traits.put("date", DateTime.now().millisecondsSinceEpoch);
    
    rudderClient.identify("1hKOmRA4GRlm", traits: traits, options: null);
    

The `identify` method has the following signature:

Name| Data Type| Description  
---|---|---  
`userId`  
Required| String| Unique identifier for a user in your database.  
`traits`| `RudderTraits`| An optional dictionary of the user’s traits like `name` or `email`.  
`options`| `RudderOption`| Extra options for the `identify` event.  
  
Once a user is identified, the SDK persists all user information and passes it to the successive `track` or `screen` calls. To reset the user identification, you can use the `reset` method.

> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * For older SDK versions (< v2.5.0), the Flutter SDK captures the device ID and uses that as `anonymousId` for identifying the user. This helps the SDK to track the users across the application installation.
>   * Starting from v2.5.0 the SDK uses a UUID as `anonymousId` instead of the device ID. If you are upgrading from a previous SDK version, see How RudderStack sets anonymous ID for more information on how the SDK collects and sets `anonymousId`.
> 


## Setting a custom anonymous ID

You can use the following method to override and set your own `anonymousId`:
    
    
    rudderClient.putAnonymousId(<ANONYMOUS_ID>);
    

### How device ID is set for Android and iOS

  * On Android devices, the `deviceId` is assigned during the first boot. It remains consistent across the applications and installs and changes only after factory reset.
  * According to [Apple documentation](<https://developer.apple.com/documentation/uikit/uidevice/1620059-identifierforvendor>), multiple apps from the same vendor are assigned the same `deviceId`. If all applications from the vendor are uninstalled and then reinstalled, then they are assigned a new `deviceId`.


### Disabling device ID collection

Starting from v2.5.0, you can disable the collection of device ID by setting `collectDeviceId` in the `MobileConfig` object to `false`.

You will observe the following changes when this property is set to false:

  * The SDK does not send `context.device.id` as a part of the event payload.
  * The SDK replaces the existing `anonymousId` (if it is equal to the device ID) with a UUID.


> ![info](/docs/images/info.svg)
> 
> These changes are introduced to make the SDK more compliant with all policies around the device ID collection.
    
    
    MobileConfig mc = MobileConfig(collectDeviceId: false);
        RudderConfigBuilder builder = RudderConfigBuilder();
        builder
          ..withMobileConfig(mc)
          ..withDataPlaneUrl('DATA_PLANE_URL')
          ..withDataResidencyServer(DataResidencyServer.US);
        rudderClient.initialize('WRITE_KEY', config: builder.build(), options: null);
    

> ![warning](/docs/images/warning.svg)
> 
> If you are upgrading to the latest SDK from a previous version (< v2.5.0) **and** disabling device ID collection using `collectDeviceId:false`:
> 
>   * Make sure your user transformations are not dependent on `context.device.id` as the SDK will not send this value in the event payload.
>   * The `context.device.id` column in your warehouse destination will not be populated henceforth (it will still contain data populated by the previous SDK version).
> 


### How SDK sets anonymous ID

#### **For direct/fresh SDK installation**

RudderStack uses UUID as `anonymousId` regardless of whether `collectDeviceId` is set to `true` or `false`.

#### **For updating SDK from older version**

If you are updating your Flutter SDK from an older version (< v2.5.0), then:

  * RudderStack will continue to use the device ID as `anonymousId` \- it will not break the existing SDK behavior **until** you set `collectDeviceId` to `false`.
  * If you set `collectDeviceId` to `false`, the SDK checks if the existing `anonymousId` is a device ID. If yes, it sets a new UUID as the `anonymousId`.
  * If you have used the `putAnonymousId` method to set your own `anonymousId`, then the SDK will **not** modify it even if you set `collectDeviceId` to `false`.


### Obtaining user traits

The following snippet shows how you can obtain the user traits after making an `identify` call:
    
    
    Map context = await rudderClient.getRudderContext();
    print(context["traits"]);
    

For the web apps, the `getRudderContext` API returns the user’s `traits` and `anonymousId`.

### Setting a custom ID

You can pass a custom ID along with the standard `userId` in your `identify` calls. RudderStack adds this value under `context.externalId`.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack supports passing `externalId` only in the `identify` events. You must not pass this ID in other API calls like `track`, `page`, etc.

The following code snippet shows how to add `externalId` to your `identify` event:
    
    
    RudderOption option = RudderOption();
    option.putExternalId("externalId", "some_external_id_1");
    rudderClient.identify("1hKOmRA4GRlm", options: option);
    

## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you track the user actions along with any properties associated with them.

A sample `track` event is shown below:
    
    
    RudderProperty property = RudderProperty();
    property.put("test_key_1", "test_key_1");
    RudderProperty childProperty = RudderProperty();
    childProperty.put("test_child_key_1", "test_child_value_1");
    property.put("test_key_2",childProperty);
    rudderClient.track("Test Event", properties: property);
    

The `track` method has the following signature:

Name| Type| Description  
---|---|---  
`eventName`  
Required| String| Name of the tracked event.  
`properties`| `RudderProperty`| An optional dictionary of the properties associated with the event.  
`options`| `RudderOption`| Extra options for the `track` event.  
  
### Lifecycle events

The Flutter SDK automatically tracks the following **optional** [application lifecycle events](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/>):

  * [`Application Installed`](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-installed>)
  * [`Application Updated`](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-updated>)
  * [`Application Opened`](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-opened>)
  * [`Application Backgrounded`](<https://www.rudderstack.com/docs/event-spec/standard-events/application-lifecycle-events-spec/#application-backgrounded>)


You can disable these events by setting `trackLifecycleEvents: false` in the `MobileConfig` object passed to `withMobileConfig()` while initializing the SDK. However, it is **highly recommended** to keep them enabled.
    
    
    MobileConfig mc = MobileConfig( trackLifecycleEvents: false );
    RudderConfigBuilder builder = RudderConfigBuilder();
    builder
      ..withMobileConfig(mc)
      ..withDataPlaneUrl('DATA_PLANE_URL');
    rudderClient.initialize('WRITE_KEY', config: builder.build());
    

## Screen

The [`screen`](<https://www.rudderstack.com/docs/event-spec/standard-events/screen/>) call is the mobile equivalent of the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) call. It lets you record the screen views on your mobile app along with other relevant information about the screen.

For the web apps, the SDK internally calls the [`page`](<https://www.rudderstack.com/docs/event-spec/standard-events/page/>) API with the provided parameters.

A sample `screen` event is shown below:
    
    
    RudderProperty screenProperty = RudderProperty();
      screenProperty.put("browser", "Chrome");
      screenProperty.put("device", "Macbook Pro");
      rudderClient.screen("Walmart Cart",
          category: "home",
          properties: screenProperty,
          options: null);
    

The `screen` method has the following signature:

Name| Type| Description  
---|---|---  
`screenName`  
Required| String| Name of the viewed screen.  
`category`| String| Category of the viewed page (web) or screen (mobile).  
`properties`| `RudderProperty`| An optional dictionary of the properties associated with the event.  
`options`| `RudderOption`| Extra options for the `screen` event.  
  
### Automatic screen recording

> ![info](/docs/images/info.svg)
> 
> The `recordScreenViews` parameter records the screen views of the native [Android activities](<https://developer.android.com/guide/components/activities/intro-activities>) or the [iOS view controllers](<https://developer.apple.com/documentation/uikit/view_controllers>) only and **not** of the Flutter screen views.

To track the screen views of your Flutter app screens, follow these steps:

  1. Define the `routes` with their names to the `Material App` constructor of the entry widget.
  2. Register an instance of the custom navigation observer to the `Material App` constructor of the entry widget.


The following snippet includes the code for the above two steps:
    
    
    import 'package:flutter/material.dart';
    import 'home_screen.dart';
    import 'screen2.dart';
    import 'screen3.dart';
    import 'my_route_observer.dart';
    
    class MyApp extends StatelessWidget {
      const MyApp({Key? key}) : super(key: key);
    
      @override
      Widget build(BuildContext context) {
        return MaterialApp(
          theme: ThemeData(
            primarySwatch: Colors.blue,
          ),
    // Step 2. Registering an instance of our custom navigation observer.
          navigatorObservers: [
            MyRouteObserver(),
          ],
          home: const HomeScreen(),
    // Step 1. Defining the named routes
          routes: {
            'screen2': (context) => const Screen2(),
            'screen3': (context) => const Screen3(),
          },
        );
      }
    }
    
    Future<void> main() async {
      runApp(const MyApp());
    }
    

  3. Finally, add the below code for the custom navigation observer used above:


    
    
    import 'package:flutter/material.dart';
    import 'package:rudder_sdk_flutter/RudderController.dart';
    
    class MyRouteObserver extends RouteObserver<PageRoute<dynamic>> {
      @override
      void didPush(Route<dynamic> route, Route<dynamic>? previousRoute) {
        super.didPush(route, previousRoute);
        if (route is PageRoute && route.settings.name != null) {
          RudderController.instance.screen(route.settings.name!);
        }
      }
    
      @override
      void didPop(Route<dynamic> route, Route<dynamic>? previousRoute) {
        super.didPop(route, previousRoute);
        if (previousRoute is PageRoute && route is PageRoute) {
          RudderController.instance.screen(previousRoute.settings.name!);
        }
      }
    }
    

## Group

The [`group`](<https://www.rudderstack.com/docs/event-spec/standard-events/group/>) call lets you link an identified user with a group, such as a company, organization, or an account. It also lets you record any custom traits or properties associated with that group.

> ![info](/docs/images/info.svg)
> 
> RudderStack does not persist the group traits across the sessions.

A sample `group` event is shown below:
    
    
    RudderTraits groupTraits = RudderTraits();
    groupTraits.put("foo", "bar");
    groupTraits.put("foo1", "bar1");
    rudderClient.group("sample_group_id",
        groupTraits: groupTraits, options: null);
    

The `group` method has the following signature:

Name| Type| Description  
---|---|---  
`groupId`  
Required| String| Unique identifier of the group in your database.  
`groupTraits`| `RudderTraits`| An optional dictionary of the group’s traits like `name` or `email`.  
`options`| `RudderOption`| Extra options for the `group` event.  
  
## Alias

The [`alias`](<https://www.rudderstack.com/docs/event-spec/standard-events/alias/>) call lets you merge different identities of a known user. It is an advanced method that lets you change the tracked user’s ID explicitly. You can use `alias` for managing the user’s identity in some of the downstream destinations.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack supports sending `alias` events only to select downstream destinations. Refer to the [destination-specific documentation](<https://www.rudderstack.com/docs/destinations/streaming-destinations/>) for more details.

When you make an `alias` call, RudderStack replaces the old user ID with the new user ID and persists this identification across the sessions.

A sample `alias` call is shown below:
    
    
    rudderClient.alias("new_user_id", options: null);
    

The `alias` method has the following signature:

Name| Type| Description  
---|---|---  
`newId`  
Required| String| The new user identifier.  
`options`| `RudderOption`| Extra options for the `alias` event.  
  
## Reset

You can use the `reset` method to clear the persisted user traits. It also resets the `anonymousId` with a new UUID if you call it with `clearAnonymousId: true` (for SDK v2.5.0 and later).
    
    
    rudderClient.reset(clearAnonymousId: true);
    

To clear only user traits, call `reset` with `clearAnonymousId: false`.

## FAQ

#### How does the Flutter SDK handle events larger than 32KB?

The Flutter SDK drops any events greater than 32KB.