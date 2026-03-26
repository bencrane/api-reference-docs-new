# Automatic Screen Tracking in Android (Kotlin) SDK

Learn about the automatic screen tracking feature available in the Android (Kotlin) SDK.

* * *

  * __2 minute read

  * 


This guide walks you through the automatic screen tracking feature available in the [Android (Kotlin) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>).

## Activity tracking

You can use the Android (Kotlin) SDK to automatically track activities (Android `Activity` class). By enabling this feature, the SDK sends `screen` events for any `Activity` opened by the client app.

### Usage

To enable automatic activity tracking, pass the `trackActivities` parameter as `true` in the `Configuration` object when initializing the SDK.
    
    
    analytics = Analytics(
        configuration = Configuration(
            writeKey = "YOUR_WRITE_KEY",
            application = application,
            dataPlaneUrl = "YOUR_DATA_PLANE_URL",
            trackActivities = true
        )
    )
    

## Navigation-Destination tracking

The Android (Kotlin) SDK provides a `setNavigationDestinationsTracking` API for automatically tracking user navigation within your Android application by leveraging a `NavController`.

The API listens to any screen changes and sends the corresponding [`screen`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/screen/>) events to RudderStack.

### Workflow

  * The `setNavigationDestinationsTracking` API utilizes `OnDestinationChangedListener` to detect any navigation changes.
  * It also integrates with the `onStart` lifecycle callback of the user activity to ensure `screen` events are captured when the app is foregrounded or when any configuration changes occur.
  * If multiple `NavController` instances are used in the Android app, you must call this API separately for each instance.


### Usage

This section explains how to use the `setNavigationDestinationsTracking` API depending on your app setup:

#### Jetpack Compose navigation

If your app uses Jetpack Compose with `NavController`, you can set up the navigation tracking as follows:
    
    
    @Composable
    fun MyApp() {
        val navController = rememberNavController()
    
        LaunchedEffect("first_launch") {
            analytics.setNavigationDestinationsTracking(navController, this@MainActivity)
        }
    
        MyNavHost(navController = navController)
    }
    

#### Fragments navigation

If your app uses Fragments with the navigation component, use the following setup in `MainActivity`:
    
    
    class MainActivity : AppCompatActivity() {
    
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
    
            val binding = ActivityMainBinding.inflate(layoutInflater)
            setContentView(binding.root)
    
            val navHostFragment = supportFragmentManager
                .findFragmentById(R.id.nav_host_fragment) as NavHostFragment
            val navController = navHostFragment.navController
    
            analytics.setNavigationDestinationsTracking(navController, this@MainActivity)
        }
    }
    

#### Parameter description

The key parameters covered in the above snippets are explained below:

Parameter| Description  
---|---  
`navController`| The `NavController` instance managing the navigation in the app.  
`activity`| The `Activity` that owns the `NavHostFragment` or is the parent of the composable in which `NavController` is used.