# Add Application Class to Initialize Android (Java) SDK

Add an Application class to initialize the RudderStack Android (Java) SDK.

* * *

  * __less than a minute

  * 


RudderStack recommends using a global [Application](<https://developer.android.com/reference/android/app/Application.html>) class to initialize our SDK. If you don’t have an Application class for your project, follow these steps:

  1. Create a class that extends `Application`.


    
    
    class MainApplication : Application() {
        override fun onCreate() {
            super.onCreate()
            // initialize Rudder SDK here
        }
    }
    
    
    
    import android.app.Application;
    public class MainApplication extends Application {
        @Override
        public void onCreate() {
            super.onCreate();
            // initialize Rudder SDK here
        }
    }
    

  2. Open `AndroidManifest.xml` file of your app and locate `<application>` tag.
  3. Add an attribute `android:name` and set it to your new application class.


    
    
    <application
        android:name=".MainApplication"
        <!-- ... -->
    </application>