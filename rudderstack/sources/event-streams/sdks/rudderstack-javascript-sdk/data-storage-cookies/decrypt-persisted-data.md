# How to Read the RudderStack SDK Persisted Data

> Version: Latest (v3)v1.1

# How to Read the RudderStack SDK Persisted Data

Learn how to decrypt cookie values stored by the RudderStack SDK

* * *

  *  __4 minute read

  * 


Depending on your environment, use the below Decryption APIs to decrypt the RudderStack JavaScript cookie value encrypted using the [`storage`](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#storage>) load option.

## Browser environments

### Encrypt cookie value

You can use the `getEncryptedValueBrowser` API to encrypt the RudderStack cookie value that is recognized by the JavaScript SDK (v3).
    
    
    import { getEncryptedValueBrowser } from '@rudderstack/analytics-js-cookies';
    
    const cookieValue = 'test-data';
    const encryptedCookieValue = getEncryptedValueBrowser('test-data');
    console.log('Encrypted Cookie Value: ', encryptedCookieValue);
    // Output:
    // Encrypted Cookie Value: RS_ENC_v3_InRlc3QtZGF0YSI=
    

### Decrypt cookie value

The JavaScript SDK also provides some decryption APIs for the frontend (browser) environments based on your use case.

You can use the `getDecryptedValueBrowser` API to decrypt the RudderStack cookie value that is [encrypted](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#storage>) with `version` set to `v3`.
    
    
    import { getDecryptedValueBrowser } from '@rudderstack/analytics-js-cookies';
    
    const encryptedCookieValue = 'RS_ENC_v3_InRlc3QtZGF0YSI=';
    const decryptedCookieValue = getDecryptedValueBrowser(encryptedCookieValue);
    console.log('Decrypted Cookie Value: ', decryptedCookieValue);
    // Output:
    // Decrypted Cookie Value: test-data
    

Note that the API returns `null` in the following cases:

  * The provided input is not encrypted or properly encrypted.
  * There are errors during decryption.


### Decrypt cookie name

The `getDecryptedCookieBrowser` API takes the name of the JavaScript SDK cookie and returns the decrypted value. The return type is either a string or an object as some cookies like user ID, anonymous ID have string values while the user traits are objects.

You can use the following exported cookies with this API:

Cookie| Description  
---|---  
`userIdKey`| Key for the user ID cookie.  
`userTraitsKey`| Key for the user traits cookie.  
`anonymousUserIdKey`| Key for the anonymous user ID cookie.  
`groupIdKey`| Key for the group ID cookie.  
`groupTraitsKey`| Key for the group traits cookie.  
`pageInitialReferrerKey`| Key for the page initial referrer cookie.  
`pageInitialReferringDomainKey`| Key for the page initial referring domain cookie.  
`sessionInfoKey`| Key for the session ID cookie.  
`authTokenKey`| Key for the authentication token cookie.  
  
The following snippet highlights how to use the `getDecryptedCookieBrowser` API:
    
    
    import {
      getDecryptedCookieBrowser,
      anonymousUserIdKey,
      userTraitsKey,
    } from '@rudderstack/analytics-js-cookies';
    
    const anonymousId = getDecryptedCookieBrowser(anonymousUserIdKey);
    console.log('Anonymous User ID: ', anonymousId);
    // Output:
    // Anonymous User ID: 2c5b6d48-ea90-43a2-a2f6-457d27f90328
    
    const userTraits = getDecryptedCookieBrowser(userTraitsKey);
    console.log('User Traits: ', userTraits);
    // Output:
    // User Traits: {"email":"abc@xyz.com","name":"John Doe"}
    
    const invalidCookie = getDecryptedCookieBrowser('invalid-cookie-name');
    console.log('Invalid Cookie: ', invalidCookie);
    // Output:
    // Invalid Cookie: null
    

Note that the API returns `null` in the following cases:

  * If the cookie is absent.
  * If the cookie is not properly encrypted. It only decrypts the cookies that are encrypted with `version` set to `v3`.
  * If the decrypted cookie value is not a valid JSON string.
  * If the provided cookie name is not a valid RudderStack JavaScript SDK cookie.


## Node.js environments

The following decryption API is available for the backend (Node.js) environments:

### `getEncryptedValue`

You can use the `getEncryptedValue` API to encrypt the RudderStack cookie value that is recognized by the JavaScript SDK (v3).
    
    
    import { getEncryptedValue } from '@rudderstack/analytics-js-cookies';
    
    const cookieValue = 'test-data';
    const encryptedCookieValue = getEncryptedValue('test-data');
    console.log('Encrypted Cookie Value: ', encryptedCookieValue);
    // Output:
    // Encrypted Cookie Value: RS_ENC_v3_InRlc3QtZGF0YSI=
    

### `getDecryptedValue`

You can use the `getDecryptedValue` API to decrypt the RudderStack cookie value that is [encrypted](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#storage>) with `version` set to `v3`.
    
    
    import { getDecryptedValue } from '@rudderstack/analytics-js-cookies';
    
    const encryptedCookieValue = 'RS_ENC_v3_InRlc3QtZGF0YSI=';
    const decryptedCookieValue = getDecryptedValue(encryptedCookieValue);
    console.log('Decrypted Cookie Value: ', decryptedCookieValue);
    
    // Output:
    // Decrypted Cookie Value: test-data
    

Note that the API returns `null` in the following cases:

  * The provided input is not encrypted or properly encrypted.
  * There are errors during decryption.


> ![success](/docs/images/tick.svg)
> 
> See this [RudderStack blog](<https://www.rudderstack.com/blog/how-we-built-rudderstacks-real-time-personalization-engine/#:~:text=Intercept%20server%20requests%20to%20make%20real%2Dtime%20possible>) for a detailed use case on leveraging the `getDecryptedValue` API to fetch the `anonymousId` from the request cookie and use it to implement a real-time personalization engine.

## Debugging

All the above-mentioned APIs swallow any errors during the decryption process and return `null`. To log errors during the decryption process, you can set the `debug` parameter to `true` while using the APIs.

The following example highlights how to log errors using the `getDecryptedValue` API:
    
    
    import { getDecryptedValue } from '@rudderstack/analytics-js-cookies';
    
    const encryptedCookieValue = 'RS_ENC_v3_InRlc3QtZGF0YSI-some-random-data';
    
    // Set the debug flag to true
    const decryptedCookieValue = getDecryptedValue(encryptedCookieValue, true);
    console.log('Decrypted Cookie Value: ', decryptedCookieValue);
    
    // Output:
    // Error occurred during decryption: Unexpected non-whitespace character after JSON at position 11
    // Decrypted Cookie Value: null
    

  * [![](/docs/images/previous.svg)Previous](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/data-storage-cookies/specify-cookie-domain/>)
  * [Next ![](/docs/images/next.svg)](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/server-side-cookies/>)