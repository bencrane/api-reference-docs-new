# OneTrust Consent Management for iOS

Integrate the RudderStack iOS (Obj-C) SDK with OneTrust.

* * *

  * __3 minute read

  * 


The iOS (Obj-C) SDKiOS (Obj-C) refers to the legacy RudderStack iOS SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the iOS (Swift) SDK instead. lets you specify the user’s consent during initialization.

> ![warning](/docs/images/warning.svg)
> 
> The SDK supports the OneTrust consent management feature only in v1.9.0 and above.

This guide lists the steps to develop a consent interceptor for the [iOS (Obj-C) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>) and use the interceptor to initialize the SDK **after** the user gives their consent.

## Overview

The consent management is designed to be a filter for the event destinations and the natively added factories. Since the SDK initializes the native integration factories during the startup, **you must first capture** the user’s consent to the cookie categories.

> ![info](/docs/images/info.svg)
> 
> You can add only one consent filter to the iOS (Obj-C) SDK.

For filtering, RudderStack uses the `getConsentStatus(forCategory categoryId: String)` method of the OneTrust SDK.

## Install OneTrust consent

This setup assumes the [iOS (Obj-C) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/#installing-the-rudderstack-ios-sdk>) and the [OneTrust SDK](<https://developer.onetrust.com/onetrust/docs/ios-tvos>) are already added to your application.

  1. Install `RudderOneTrustConsentFilter` by adding the following line to your `Podfile`:


    
    
    pod 'RudderOneTrustConsentFilter', '~> 1.0.0'
    

  2. Import the iOS (Obj-C) SDK:


    
    
    @import RudderOneTrustConsentFilter;
    
    
    
    import RudderOneTrustConsentFilter
    

  3. Add the imports to your `AppDelegate` file under the `didFinishLaunchingWithOptions` method, as shown:


    
    
    @interface AppDelegate ()<OTEventListener>
    
    @end
    
    - (BOOL)application:(UIApplication *)application didFinishLaunchingWithOptions:(NSDictionary *)launchOptions {
        [[OTPublishersHeadlessSDK shared] startSDKWithStorageLocation:STORAGE_LOCATION domainIdentifier:DOMAIN_IDENTIFIER languageCode:@"en" params:nil loadOffline:NO completionHandler:^(OTResponse *response) {
            if (response.status) {
            
            }
        }];
        
        [[OTPublishersHeadlessSDK shared] addEventListener:self];
    }
    
    - (void)initializeRudderSDK {
        RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
        [builder withLoglevel:RSLogLevelDebug];
        [builder withDataPlaneUrl:DATA_PLANE_URL];
        [builder withConsentFilter:[[RudderOneTrustConsentFilter alloc] init]];
    
        [RSClient getInstance:rudderConfig.WRITE_KEY config:builder.build];
    }
    
    - (void)onPreferenceCenterConfirmChoices {
        [self initializeRudderSDK];
    }
    
    
    
    class AppDelegate {
        func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
            OTPublishersHeadlessSDK.shared.startSDK(
                storageLocation: STORAGE_LOCATION,
                domainIdentifier: DOMAIN_IDENTIFIER,
                languageCode: "en"
            ) { response in
                if response.status {
            
                }
            }
            
            OTPublishersHeadlessSDK.shared.addEventListener(self)
        }
        
        func initializeRudderSDK() {
            let builder: RSConfigBuilder = RSConfigBuilder()
                .withLoglevel(RSLogLevelDebug)
                .withDataPlaneUrl(DATA_PLANE_URL)
                .withConsentFilter(RudderOneTrustConsentFilter())
    
            RSClient.getInstance(rudderConfig.WRITE_KEY, config: builder.build())
        }
    }
    
    extension AppDelegate: OTEventListener {
        func onPreferenceCenterConfirmChoices() {
            initializeRudderSDK()
        }
    }
    

> ![warning](/docs/images/warning.svg)
> 
> Make sure you load the SDK only if the user provides their consent.

## Create custom consent filter

  1. Create a `CustomConsentIFilter.h` file by extending `RSConsentFilter`:


    
    
    #import <Foundation/Foundation.h>
    #import <Rudder/Rudder.h>
    NS_ASSUME_NONNULL_BEGIN
    @interface CustomConsentFilter : NSObject<RSConsentFilter>
    @end
    NS_ASSUME_NONNULL_END
    

  2. Create a `CustomConsentFilter.m` file.


    
    
    #import "CustomConsentFilter.h"
    
    @implementation CustomConsentFilter
    
    - (NSDictionary <NSString *, NSNumber *> * __nullable)filterConsentedDestinations:(NSArray <RSServerDestination *> *)destinations {
        NSDictionary <NSString *, NSNumber *> *filteredConsentedDestinations;
        // Do someting
        return filteredConsentedDestinations;
    }
    
    @end
    

  1. Create a `CustomConsentFilter` file by extending `RSConsentFilter`.


    
    
    @objc
    open class OneTrustInterceptor: NSObject, RSConsentFilter {
        @objc
        public override init() {
            super.init()
        }
    
        public func filterConsentedDestinations(_ destinations: [RSServerDestination]) -> [String: NSNumber]? {
            let filteredConsentedDestinations: [String: NSNumber]
            // Your code
            return filteredConsentedDestinations
        }
    }
    

### Register consent filter with iOS (Obj-C) SDK

You can register `CustomConsentFilter` with the iOS (Obj-C) SDK during its initialization, as shown:
    
    
    RSConfigBuilder *builder = [[RSConfigBuilder alloc] init];
    [builder withLoglevel:RSLogLevelDebug];
    [builder withDataPlaneUrl:DATA_PLANE_URL];
    [builder withConsentInterceptor:[[CustomConsentFilter alloc] init]];
    [RSClient getInstance:WRITE_KEY config:builder.build];
    
    
    
    let builder: RSConfigBuilder = RSConfigBuilder()
        .withLoglevel(RSLogLevelDebug)
        .withDataPlaneUrl(DATA_PLANE_URL)
        .withConsentFilter(CustomConsentFilter())
    RSClient.getInstance(rudderConfig.WRITE_KEY, config: builder.build())
    

## Additional settings for cloud mode

> ![info](/docs/images/info.svg)
> 
> RudderStack supports OneTrust integration in cloud mode from iOS (Obj-C) SDK v1.12.0 and above, and `RudderOneTrustConsentFilter` 1.1.0.

You can specify your OneTrust cookie categories when sending events from your iOS (Obj-C) source in the [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

  1. Set up your iOS (Obj-C) source in the RudderStack dashboard.
  2. Connect it to a destination.
  3. In the destination settings, enter the OneTrust category IDs in the **Enter consent category IDs** field. You can specify multiple consent category IDs by pressing the **Enter** key after each ID.


> ![info](/docs/images/info.svg)
> 
> You can find the category IDs in your OneTrust dashboard under **Preference & Consent Management** > **Cookie Compliance** > **Categorizations** > **Categories**.

[![OneTrust category ID in consent settings](/docs/images/data-governance/consent-management/ios-onetrust.webp)](</docs/images/data-governance/consent-management/ios-onetrust.webp>)

Note that the settings for specifying multiple consent IDs vary slightly for some destinations. Click **Add more** after specifying each consent category ID.

[![](/docs/images/data-governance/consent-management/multiple-consent-ui.webp)](</docs/images/data-governance/consent-management/multiple-consent-ui.webp>)