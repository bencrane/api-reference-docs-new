# Cookieless Tracking

Control what user information you collect and where to store it.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __less than a minute

  * 


RudderStack’s centralized cookie management tools let you manage your cookie settings across websites and apps in a user-centric, privacy-compliant manner.

The [JavaScript SDK v3](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) supports [cookieless tracking](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/persistent-data-storage/>) that allows you to gather valuable user insights while adhering to the stringent data privacy and regulation norms.

With this feature, you can specify what type of user information you want to collect and where (or not) to store it while loading the JavaScript SDK.

## How cookieless tracking works

While [loading the JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/>), you can:

  * Specify what user information you want to store like `userId`, `anonymousId`, session information, etc.
  * Define the storage for your user information, like browser cookies, local storage, in-memory storage, or not store it at all.


You can also set storage for specific information type. For example, you can store `userId` in the browser cookies, `anonymousId` in the in-memory storage, session information in local storage, and so on.

See [Configure Persistent Data Storage](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/persistent-data-storage/>) for more information.