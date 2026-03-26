# Sprig Device Mode Integration

Send events to Sprig using RudderStack device mode.

* * *

  * __3 minute read

  * 


RudderStack lets you send your event data to Sprig in web and mobile [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>), that is, using the native Sprig SDK.

Find the open source code for this integration below:

  * [Web device mode](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/Sprig>)
  * [Sprig-Android](<https://github.com/rudderlabs/rudder-integration-sprig-android>)
  * [Sprig-iOS](<https://github.com/rudderlabs/rudder-integration-sprig-ios>)


## Add mobile device mode integration

Once you add Sprig as a destination in the [RudderStack dashboard](<https://app.rudderstack.com/>), follow these steps to add it to your mobile project depending on your integration platform:

  1. Add the following line to your `Podfile`:


    
    
    pod 'Rudder-Sprig'
    

  2. Run the `pod install` command.
  3. Change the SDK initialization to the following:


    
    
    let configBuilder = RSConfigBuilder()
        .withDataPlaneUrl(DATA_PLANE_URL)
        .withFactory(RudderSprigFactory.instance)
    
    RSClient.getInstance(WRITE_KEY, config: configBuilder.build())
    

  4. Import `Rudder_Sprig` into `ViewController`:


    
    
    import Rudder_Sprig
    

  5. Pass the instance of `ViewController` to `RudderSprigFactory` as shown:


> ![info](/docs/images/info.svg)
> 
> Sprig requires this step to display the survey. You can also set it as `nil` to clear the values.
    
    
    class ViewController: UIViewController {
        override func viewDidLoad() {
            super.viewDidLoad()
        
            // Do any additional setup after loading the view.
            
            // Pass ViewController instance to RudderSprigFactory. As Sprig SDK requires this to display the survey.
            RudderSprigFactory.instance.setViewController(self)
        }
    }
    

  1. Add the following under the dependencies section:


    
    
    implementation 'com.rudderstack.android.sdk:core:[1.0,2.0)'
    implementation 'com.rudderstack.android.integration:sprig:[1.0.0,)'
    

  2. Change the SDK initialization to the following:


    
    
    // initialize Rudder SDK
    val rudderClient: RudderClient =
        RudderClient.getInstance(
            this,
            WRITE_KEY,
            RudderConfig.Builder()
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withFactory(SprigIntegrationFactory.FACTORY)
                .build()
        )
    

  3. Import the dependencies for Sprig:


    
    
    import com.rudderstack.android.integration.sprig.SprigIntegrationFactory
    

  4. Pass the `FragmentActivity` instance as shown:


> ![info](/docs/images/info.svg)
> 
> Sprig requires this step to display the survey. You can also set it as `null` to clear the values.
    
    
    class MainActivity: AppCompatActivity() {
    
        override fun onStart() {
            super.onStart()
            // pass the FragmentActivity instance, it is required by Sprig to display the survey.
            SprigIntegrationFactory.FACTORY.setFragmentActivity(this@MainActivity)
        }
    }
    

## Identify

You can use the [`identify`](<https://www.rudderstack.com/docs/event-spec/standard-events/identify/>) call to identify a user in Sprig.

A sample `identify` call is shown:
    
    
    rudderanalytics.identify('1hKOmRA4GRlm', {
      firstName: 'Alex',
      lastName: 'Keener',
      email: "alex@example.com"
    });
    

### Supported mappings

RudderStack maps the following **optional** user attributes in the `identify` events to the corresponding Sprig fields:

RudderStack property| Sprig property  
---|---  
`userId`| `userId`  
`context.traits`| `attributes`  
`context.traits.email`| `email`  
  
## Track

The [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) call lets you record any user actions along with the associated properties.

A sample `track` call is shown:
    
    
    rudderanalytics.track('Sample Survey', {
      plan: "Annual",
      accountType: "Pro"
    });
    

If you send a `track` event called `Signed Out`, then RudderStack automatically maps it to the `logoutUser` event before sending it to Sprig. Otherwise, it maps the following event/properties to the corresponding Sprig fields:

RudderStack property| Sprig property  
---|---  
`event`  
Required| `eventName`  
`userId`| `userId`  
`properties`| `properties`  
  
Sprig expects the event name to be present in the `eventName` key. Hence, if you send a `track` event named `Product Added`, RudderStack maps it to Sprig’s `eventName` key before sending it across to Sprig.

> ![info](/docs/images/info.svg)
> 
> To display the survey, you must pass the `ViewController` instance for iOS and the `FragmentActivity` instance for Android, otherwise the survey won’t be displayed.
> 
> If you do not want to display the survey, you can skip setting `FragmentActivity` or `ViewController`. RudderStack then forwards the call to the `Sprig.track` API instead of `Sprig.trackAndPresent`.

## Reset

The `reset` method resets the previously identified user and related information.

A sample `reset` call is shown:
    
    
    RSClient.getInstance().reset()
    
    
    
    RudderClient.getInstance()?.reset()