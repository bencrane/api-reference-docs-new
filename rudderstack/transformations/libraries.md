# Transformation Libraries

Reuse transformation code with transformation libraries.

* * *

  * __6 minute read

  * 


RudderStack’s transformation libraries feature lets you reuse the same code in multiple transformations.

> ![success](/docs/images/tick.svg)
> 
> RudderStack supports writing transformation libraries in Python for the RudderStack Cloud [Growth](<https://rudderstack.com/pricing/>) and [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plans.

[![](https://img.shields.io/badge/Node.js%20Version-18.x-7447fc.svg?logo=data:image/png;base64,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&logoColor=&logoWidth=&style=)](<>) ![](https://img.shields.io/badge/Python%20Version-3.11-7447fc.svg?logo=data:image/png;base64,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&logoColor=&logoWidth=&style=)

## Required permissions

  * [Admins](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) have full access to manage transformation libraries.
  * [Members](<https://www.rudderstack.com/docs/access-management/member-management/#member-roles>) must have the [**Transformation Libraries**](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) permission in their workspace policy.


**Click here to see how these permissions appear in the workspace policy**.  
![Permissions to manage transformation libraries in RudderStack dashboard](/docs/images/access-management/transformation-libraries.webp)  


#### Permissions for legacy RBAC system

In the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>):

  * [Org Admins](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/#organization-roles>) can edit transformation libraries
  * Members must have the **Grant edit access** permission in **Transformations and Library** toggled on to edit transformation libraries

[![Transformations permissions in the legacy framework](/docs/images/access-management/permissions/legacy/transformations.webp)](</docs/images/access-management/permissions/legacy/transformations.webp>)

## Add transformation library

  1. In the [RudderStack dashboard](<https://app.rudderstack.com/>), go to **Collect** > **Transformations** and click the **Libraries** tab. Then, click **Create Library**.

[![Adding a library](/docs/images/features/transformations/create-library.webp)](</docs/images/features/transformations/create-library.webp>)

  2. Add the library **Name** , **Description** and select the language to write the library function. You can also add multiple functions in a single library.


> ![info](/docs/images/info.svg)
> 
> RudderStack supports Python libraries only in the RudderStack Cloud [Growth](<https://rudderstack.com/pricing/>) and [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plans.

> ![warning](/docs/images/warning.svg)
> 
> JavaScript transformation libraries run in an isolated environment — no Node.js modules (like `fs`, `require`) or browser APIs (like `window`, `btoa`) are available. Only standard JavaScript features are supported.

[![Adding a library](/docs/images/features/transformations/add-new-library.webp)](</docs/images/features/transformations/add-new-library.webp>)

  3. Click **Run Test** to ensure the library code has the correct syntax. A **Test Passed** message pops up once the test runs successfully.

[![Library test passed](/docs/images/features/transformations/library-test-passed.webp)](</docs/images/features/transformations/library-test-passed.webp>)

## Use libraries in transformations

To use the libraries in your existing transformations, note the library name listed in the **Import library name** column in the RudderStack dashboard:

[![Using libraries in transformations](/docs/images/features/transformations/libraries-in-transformations.webp)](</docs/images/features/transformations/libraries-in-transformations.webp>)

> ![info](/docs/images/info.svg)
> 
> RudderStack converts the library name into **camel case without spaces** ; this becomes your **library handle** which you can use across multiple transformations. For example, if your library name is `Sample Transformation Library`, then the library handle would be `sampleTransformationLibrary`.

You can then use the library in a transformation with a simple `import` statement. Refer to the below use case for more information.

#### Use case

Suppose you want to filter the events that don’t contain an email address with the RudderStack domain. To do so, you can import a `rudderEmail` function from the transformation library `isRudderEmail`.

The `rudderEmail` function containing the filtering logic is shown below:
    
    
    export function rudderEmail(email) {
        return /@(rudderlabs|rudderstack)| \+ruddertest/.test(email);
    }
    
    
    
    import re
    
    def rudderEmail(email):
      match = re.search('@(rudderlabs|rudderstack)|\+ruddertest', email)
      if match:
        return True
      return False
    

The following snippets demonstrate how you can import this function in a transformation:
    
    
    import { rudderEmail } from "isRudderEmail";
    export function transformEvent(event) {
      const email =
        event.context && event.context.traits && event.context.traits.email;
      if (email) {
        if (!rudderEmail(email)) return;
      }
      return event;
    }
    
    
    
    from isRudderEmail import rudderEmail
    
    def transformEvent(event, metadata):
        email = event.get("context", {}).get("traits", {}).get("email")
        if email:
            if not rudderEmail(email):
                return
        return event
    

On clicking **Run Test** , a sample event not containing the RudderStack email domain is filtered out:

[![Filtering out events using libraries in transformation](/docs/images/features/libraries-in-transformations-run-test.webp)](</docs/images/features/libraries-in-transformations-run-test.webp>)

## Import multiple functions from single library

The following snippets highlight how to **correctly** import functions from a library:
    
    
    // ---------------
    import { getLoss } from "getFinanceData";
    
    // OR
    
    import { getLoss, getRevenue, getProfit } from "getFinanceData";
    import {
      getLoss,
      getRevenue,
      getProfit
    } from "getFinanceData";
    
    // For default getPrice import
    import getPrice, { getRevenue, getProfit } from "getFinanceData";
    
    // alias imports
    import getPrice as gp, { getRevenue as gr, getProfit } from "getFinanceData";
    // usage: gp(event), gr(event), getProfit(ev)
    
    import * as GFD from "getFinanceData";
    // usage: GFD.getRevenue(ev), GFD.getProfit(ev)
    // for default import: GFD.default(ev)
    
    
    
    from getFinanceData import getRevenue, getProfit
    // usage: getRevenue(event), getProfit(event)
    
    from getFinanceData import getRevenue as gr, getProfit
    // usage: gr(event), getProfit(ev)
    
    import getFinanceData
    // usage: getFinanceData.getRevenue(event), getFinanceData.getProfit(event)
    

The following snippets highlight the **incorrect** way of importing the library functions:
    
    
    // -----------------
    import * from "getFinanceData";
    getPrice(ev)
    
    // OR
    
    import getPrice as gp from "getFinanceData";
    getPrice(ev)
    
    
    
    import getRevenue, getProfit from getFinanceData
    import { getRevenue, getProfit } from getFinanceData
    
    from getFinanceData import *
    

## Delete library

> ![warning](/docs/images/warning.svg)
> 
> You cannot delete a library that is referenced or imported in a transformation.

To delete a library, go to **Collect** > **Transformations** > **Libraries** and click the **Delete** button next to the library that you want to delete.

## Default RudderStack libraries

RudderStack provides some default libraries that you can import in your transformations for implementing various use cases like encrypting, decrypting, or hashing PII, parsing user agent, and using the localized version of Apple’s device mode information in your events.

See the [GitHub codebase](<https://github.com/rudderlabs/rudder-libraries>) for the code and implementation-specific details for these libraries.

> ![warning](/docs/images/warning.svg)
> 
> Currently, these predefined RudderStack libraries are available only for JavaScript.

Use the following structure to import the RudderStack libraries:
    
    
    @rs/<libraryname>/v1
    

A sample import statement is shown below:
    
    
    import { JSEncrypt } from "@rs/encrypt/v1";
    

The following table lists the default RudderStack libraries and their usage:

RudderStack library name| Usage  
---|---  
`encrypt`| Used in the [Encryption](<https://www.rudderstack.com/docs/transformations/templates/#encryption>) / [Decryption](<https://www.rudderstack.com/docs/transformations/templates/#decryption>) transformation template.  
  
Lets you encrypt or decrypt PII, including PII stored in cookies.  
`hash`| Used in the [Hash PII](<https://www.rudderstack.com/docs/transformations/templates/#hash-pii>) transformation template.  
  
Hides sensitive PII like the user’s email, birthday, social security number, etc. You can use either **MD5** , **SHA256** , or **cyrb53** to hash your PII.  
`userAgentParser`| Used in the [Parse User Agent](<https://www.rudderstack.com/docs/transformations/templates/#parse-user-agent>) transformation template.  
  
Adds the user’s browser, engine, OS, device, and CPU-related information to the events.  
`localizeAppleDeviceModel`| Used in the [Localize Apple Device Model](<https://www.rudderstack.com/docs/transformations/templates/#localize-apple-device-model>) transformation template.  
  
Lets you use the localized version of Apple’s device model information present in your event’s `context.device.model`.  
  
## FAQ

#### How can I use a npm package not provided by RudderStack in my transformations?

To use a different library (other than the default libraries provided by RudderStack) in your transformations:

  1. Add a pure vanilla script as a transformation library.


> ![warning](/docs/images/warning.svg)
> 
> All the imports and functions referenced in the code must have their implementation in the same file — essentially, a self-sufficient minified JavaScript implementation of the required package.

  2. Import the library in your transformation.


##### **Example**

Suppose you want to use the [blueimp/JavaScript-MD5](<https://github.com/blueimp/JavaScript-MD5/blob/master/js/md5.min.js>) library to hash your PII.

  1. Your [MD5 function](<https://github.com/blueimp/JavaScript-MD5/blob/master/js/md5.min.js>) looks as follows:


    
    
    ! function(n) {"use strict";function d(n, t) {var r = (65535 & n) + (65535 & t);return (n >> 16) + (t >> 16) + (r >> 16) << 16 | 65535 & r} ... ... module.exports = t : n.md5 = t}(this);
    

> ![warning](/docs/images/warning.svg)
> 
> For this example, note that:
> 
>   * The `min.js` file is readily available — hence no other action is required. Otherwise, you will need to write a `.js` file separately.
> 
>   * The method used as the entry point method is `md5` and it uses the MD5 (hexadecimal), MD5 (raw), HMAC-MD5 (hexadecimal), and HMAC-MD5 (raw) functions — make sure to include these function implementations in the file.
> 
>     * The above functions may also reference other methods — make sure to include their implementations in the file, and so on.
>   * Include only minimal and relevant code in the file to avoid performance issues.
> 
> 


  2. Add the above code in a new transformation library, for example, `md5Library`.
  3. Import the above library in your transformation to hash sensitive PII:


    
    
    // Import the MD5 function from your library
    // Assuming the library handle is 'md5Library'
    
    import { md5 } from "md5Library";
    
    export function transformEvent(event) {
      // Get email from event properties
      const email = event.properties?.email;
      
      if (email) {
        // Hash the email using MD5
        event.properties.email = md5(email);
      }
      
      return event;
    }
    

This transformation will hash any email address in the event properties using the provided MD5 algorithm.