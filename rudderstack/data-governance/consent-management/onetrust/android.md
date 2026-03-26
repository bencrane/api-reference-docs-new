# OneTrust Consent Management for Android

Integrate the RudderStack Android (Java) SDK with OneTrust.

* * *

  * __4 minute read

  * 


The Android (Java) SDKAndroid (Java) refers to the legacy RudderStack Android SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the Android (Kotlin) SDK instead. lets you specify the user’s consent during initialization.

This guide lists the steps to develop a consent interceptor for the [Android (Java) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>) and use the interceptor to initialize the SDK **after** the user gives their consent.

## Overview

The consent management is designed to be a filter for the event destinations and the natively added factories. Since the SDK initializes the native integration factories during the startup, **you must first capture** the user’s consent to the cookie categories.

> ![info](/docs/images/info.svg)
> 
> You can add only one consent filter to the Android (Java) SDK.

For filtering, RudderStack uses the `getConsentStatusForGroupId` method of the OneTrust SDK.

## Install OneTrust consent

This setup assumes the [Android (Java) SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/#installing-the-sdk>) and the [OneTrust SDK](<https://developer.onetrust.com/onetrust/docs/android>) are already added to your application.

  1. Add OneTrust Consent Filter to your `build.gradle` (module level).


    
    
    dependencies {
        // add other dependencies
        ...
        implementation 'com.onetrust.cmp:native-sdk:202301.2.0.0'
        implementation ('com.rudderstack.android.sdk:core:1.12.0')
        implementation ('com.rudderstack.android.consentfilter:onetrustconsentfilter:1.1.0')
        ...
    }
    

  2. Move the RudderStack initialization consent callback. The following snippet shows a sample application file highlighting the initialization:


    
    
    class CustomApplication : Application() {
        var _rudderClient: RudderClient? = null;
        val rudderClient
            get() = _rudderClient
        private val oneTrustEventListener = object : OTEventListener() {
            override fun onShowBanner(p0: OTUIDisplayReason?) {
            }
            override fun onHideBanner() {
            }
            override fun onBannerClickedAcceptAll() {
                createRudderClientWithOneTrust()
            }
            override fun onBannerClickedRejectAll() {
                createRudderClientWithOneTrust()
            }
            override fun onShowPreferenceCenter(p0: OTUIDisplayReason?) {
            }
            override fun onHidePreferenceCenter() {
            }
            override fun onPreferenceCenterAcceptAll() {
                createRudderClientWithOneTrust()
            }
            override fun onPreferenceCenterRejectAll() {
                createRudderClientWithOneTrust()
            }
            override fun onPreferenceCenterConfirmChoices() {
                createRudderClientWithOneTrust()
            }
            override fun onShowVendorList() {}
            override fun onHideVendorList() {}
            override fun onVendorConfirmChoices() {
            }
            override fun allSDKViewsDismissed(p0: String?) {}
            override fun onVendorListVendorConsentChanged(p0: String?, p1: Int) {
            }
            override fun onVendorListVendorLegitimateInterestChanged(p0: String?, p1: Int) {}
            override fun onPreferenceCenterPurposeConsentChanged(p0: String?, p1: Int) {
            }
            override fun onPreferenceCenterPurposeLegitimateInterestChanged(p0: String?, p1: Int) {}
        }
        internal val otPublishersHeadlessSDK by lazy { OTPublishersHeadlessSDK(this) }
        override fun onCreate() {
            super.onCreate()
            setupOneTrust()
        }
        internal fun setupOneTrust() {
    		// set up one trust,
            // uncomment the following line and pass the credentials
    		// otPublishersHeadlessSDK.startSDK()
            otPublishersHeadlessSDK.addEventListener(oneTrustEventListener)
        }
        private fun createRudderClientWithOneTrust() {
            _rudderClient = RudderClient.getInstance(
                this,
                WRITE_KEY,
                RudderConfig.Builder()
                    .withDataPlaneUrl(DATA_PLANE_URL)
                    .withTrackLifecycleEvents(true)
                    .withRecordScreenViews(false)
                    .withConsentFilter(RudderOneTrustConsentFilter(otPublishersHeadlessSDK))
                    .build()
                )
        }
        private val otSdkParams
            get() = OTSdkParams.SdkParamsBuilder.newInstance()
                .build()
    }
    

## Create custom consent filter

  1. Create a new Android library project.
  2. Add the following to the `dependencies` section in the module-level `build.gradle` file:


    
    
    dependencies {
    	   // add other dependencies
    		...
        compileOnly 'com.rudderstack.android.sdk:core:1.12.0'
    		...
    }
    

  3. Create a class to implement `RudderConsentFilterWithCloudIntegration`:


    
    
    public final class MyConsentFilter implements RudderConsentFilterWithCloudIntegration {
    	@Override
    	public Map<String, Boolean> getConsentCategoriesMap() {
    		// return the category id to consent map.
    		// The map should have the category id as key and true if consented,
    		// false otherwise
    		// Rudderstack SDK will filter out the destinations corresponding to
    		// categories that are not consented.
    	}
    }
    

  4. Attach `MyConsentFilter` to the Android (Java) SDKAndroid (Java) refers to the legacy RudderStack Android SDK. **Note that it will be deprecated soon.**  
  
For new implementations, use the Android (Kotlin) SDK instead. similar to the OneTrust consent filter:


    
    
    _rudderClient = RudderClient.getInstance(
                this,
                WRITE_KEY,
                RudderConfig.Builder()
                    // other methods
                    .withConsentFilter(MyConsentFilter())
                    .build()
                )
    

## Additional settings for cloud mode

> ![info](/docs/images/info.svg)
> 
> RudderStack supports OneTrust integration in cloud mode from Android (Java) SDK v1.12.0 and above.

You can specify the OneTrust cookie categories when sending events from your Android (Java) source in the [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

  1. Set up your Android (Java) source in the RudderStack dashboard.
  2. Connect it to a destination.
  3. In the destination settings, enter the OneTrust category IDs in the **Enter consent category IDs** field. You can specify multiple consent category IDs by pressing the **Enter** key after each ID:


> ![info](/docs/images/info.svg)
> 
> You can find the category IDs in your OneTrust dashboard under **Preference & Consent Management** > **Cookie Compliance** > **Categorizations** > **Categories**.

[![OneTrust category IDs in consent settings](/docs/images/data-governance/consent-management/android-onetrust.webp)](</docs/images/data-governance/consent-management/android-onetrust.webp>)

Note that the settings for specifying multiple consent IDs vary slightly for some destinations. Click **Add more** after specifying each consent category ID.

[![](/docs/images/data-governance/consent-management/multiple-consent-ui.webp)](</docs/images/data-governance/consent-management/multiple-consent-ui.webp>)