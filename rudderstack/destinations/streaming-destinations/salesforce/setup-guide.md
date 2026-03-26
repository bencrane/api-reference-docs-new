# Salesforce Setup Guide Deprecated

Set up and configure Salesforce as a destination in RudderStack.

* * *

  * __4 minute read

  * 


> ![danger](/docs/images/danger.svg)
> 
> **This destination is deprecated**.
> 
> To send events from RudderStack to Salesforce, use the [Salesforce v2](<https://www.rudderstack.com/docs/destinations/streaming-destinations/salesforce-v2/>) destination integration instead.

This guide will help you set up Salesforce as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Salesforce.

> ![warning](/docs/images/warning.svg)
> 
> **Before you begin:**
> 
>   * Note that RudderStack **does not** support dev instances of Salesforce. See FAQ for more information.
> 
>   * RudderStack recommends creating a new Salesforce account to protect any confidential information in your existing Salesforce account. However, this is completely **optional**.
> 
>   * Give RudderStack the required API permissions by creating a new user account in your Salesforce dashboard.
> 
>     * Go to **Setup** > **Administration Setup** > **Users** > **New User** and select **System Administrator** as the profile type.
>     * For the above user, make sure the password policy is set to **Never expires** to avoid event delivery issues due to password expiration. See the [Salesforce documentation](<https://help.salesforce.com/s/articleView?id=sf.users_profiles_password_policies.htm&type=5>) for more information.
>   * **Turn off** two-factor authentication for your Salesforce account. RudderStack will be unable to authenticate while making requests if 2FA is enabled.
> 
>   * Make sure the Salesforce objects are searchable and fields are creatable before sending events. Otherwise, it can result in errors during event transformation or delivery.
> 
> 


## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Android (Java) , Android (Kotlin) , iOS (Obj-C) , iOS (Swift) , Web, Unity, AMP , Cloud, Warehouse, React Native , Flutter, Cordova
  * Refer to it as **Salesforce V2** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
AMP| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Java)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Android (Kotlin)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cloud| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Cordova| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Flutter| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Obj-C)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
iOS (Swift)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
React Native| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Unity| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Warehouse| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
Web| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Cloud mode  
Supported sources| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
## Setup

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add the source. Then, from the list of destinations, select **Salesforce**.
  2. Assign a name to your destination and click **Next**.


### Connection settings

Setting| Description  
---|---  
User Name| Enter your Salesforce username in this field.  
  


> ![warning](/docs/images/warning.svg)The Salesforce API does not support certain special characters in the username.  
>   
> For example, if you create a secondary user with the email `alex.keener+rudder@domain.com`, Salesforce sets the username to that email address by default. However, to work with the Salesforce API you will need to remove the `+` sign from the username.  
  
Password| Enter the password associated with the Salesforce account.  
  


> ![info](/docs/images/info.svg)OAuth 2.0 username-password flow is blocked by default in new orgs to avoid any security risks.

  
Make sure to toggle on the **Allow OAuth Username-Password Flows** setting to enable this flow for your organization. See the [Salesforce documentation](<https://help.salesforce.com/s/articleView?id=release-notes.rn_security_username-password_flow_blocked_by_default.htm&release=244&type=5>) for more information.  
  
![Salesforce OAuth flow setting](/docs/images/event-stream-destinations/salesforce-oauth-flow.webp)  
Security Token| Enter your [Salesforce security token](<https://help.salesforce.com/s/articleView?id=sf.user_security_token.htm&language=en_US&r=https%3A%2F%2Fwww.google.com%2F&type=5>). You can find it under **Setup** > **Personal Setup** > **My Personal Information** > [Reset My Security Token](<https://na15.salesforce.com/_ui/system/security/ResetApiTokenEdit>).  
Map Rudder Properties to Salesforce Properties| This setting is toggled on by default and lets you map the RudderStack event properties to the corresponding Salesforce fields.  
Sandbox mode| Toggle on this setting if you are using a [Sandbox environment](<https://help.salesforce.com/articleView?id=sf.deploy_sandboxes_parent.htm&type=5>) for the integration.  
Use contact ID for converted leads| Toggle on this setting if both the lead and contact field mappings are the same.  
  
## FAQ

#### Which Salesforce Edition should I use to access the API?

Before connecting to the Salesforce API with RudderStack, make sure you are using the right Salesforce edition. You must have either the **Enterprise** , **Unlimited** , **Developer** , or **Performance** editions to access the API.

Follow this [Salesforce help article](<https://help.salesforce.com/articleView?id=000326486&type=1&mode=1>) for more information.

#### Does RudderStack support dev instances of Salesforce?

No, RudderStack does not support Salesforce dev instances currently.

Note that the dev environments (for example, `https://companyabc-dev-ed-develop.lightning.force.com/`) are different from Salesforce’s sandbox environments.

#### How do I check the number of Salesforce API calls left for the day?

To check the number of Salesforce API calls, go to **Setup** > **Administration Setup** > **Company Profile** > **Company Information**. You should then be able to see a field called **API Requests, Last 24 Hours** , which contains the number of API calls left for the day.

## Next steps

  * [Send events to Salesforce in cloud mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/salesforce/cloud-mode/>)