# Setup Guide

Set up Salesforce as a destination in RudderStack.

* * *

  * __4 minute read

  * 


This guide will help you set up Salesforce as a destination in the RudderStack dashboard. It also lists the configuration settings required to correctly send data from the supported sources to Salesforce.

> ![announcement](/docs/images/announcement.svg)
> 
> **This integration does not support dev instances of Salesforce**. See FAQ for more information.

## Important: Prerequisites

Before you get started, note the following:

  * **Optional but recommended** : Create a new Salesforce account to use with RudderStack to protect any confidential information in your existing Salesforce account.

    * To give RudderStack the required API permissions, add a new user account in your Salesforce dashboard by going to **Setup** > **Administration Setup** > **Users** > **New User** and select **System Administrator** as the profile type.


> ![warning](/docs/images/warning.svg)
> 
> The user account you create must have the [Approve Uninstalled Connected Apps](<https://help.salesforce.com/s/articleView?id=005132365&type=1#:~:text=New%20Approve%20Uninstalled%20Connected%20Apps%20user%20permission>) permission. Alternatively, reach out to your admin to install the app.
> 
> Otherwise, you might encounter an OAuth error during setup.

  * Make sure to **turn off** two-factor authentication for your Salesforce account so that RudderStack can authenticate successfully.
  * Make sure the Salesforce objects are searchable and fields are creatable before sending events. Otherwise, it can result in errors during event transformation or delivery.


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

In your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **Salesforce v2**.

### Connection settings

Setting| Description  
---|---  
Account settings| Click **Create Account** > **Connect with Salesforce v2** and grant RudderStack the necessary permissions to access your Salesforce account.  
Map RudderStack properties to Salesforce properties| This setting is toggled on by default and lets you map the RudderStack event properties to the corresponding Salesforce fields.  
Use contact ID for converted leads| Toggle on this setting if both the lead and contact fields are the same.  
Consent management settings| Specify the **Consent management provider** from the dropdown and enter the corresponding consent category IDs.  
  
See the [Consent Management](<https://www.rudderstack.com/docs/data-governance/consent-management/>) guide for more information on configuring the consent settings.  
  
> ![warning](/docs/images/warning.svg)
> 
> Contact [RudderStack Support](<mailto:support@rudderstack.com>) to use the Salesforce integration in your sandbox environment.

## Next steps

  * [Send events in cloud mode](<https://www.rudderstack.com/docs/destinations/streaming-destinations/salesforce-v2/cloud-mode/>)


## FAQ

#### Why am I getting an OAuth error during setup?

If you are getting the below OAuth error while connecting to Salesforce, make sure the user account you created has the [Approve Uninstalled Connected Apps](<https://help.salesforce.com/s/articleView?id=005132365&type=1#:~:text=New%20Approve%20Uninstalled%20Connected%20Apps%20user%20permission>) permission.

[![Salesforce OAuth error](/docs/images/event-stream-destinations/salesforce-v2/salesforce-v2-oauth-error.webp)](</docs/images/event-stream-destinations/salesforce-v2/salesforce-v2-oauth-error.webp>)

#### Which Salesforce Edition should I use to access the API?

Before connecting to the Salesforce API with RudderStack, make sure you are using the right Salesforce edition. You must have either the **Enterprise** , **Unlimited** , **Developer** , or **Performance** editions to access the API.

See this [Salesforce help article](<https://help.salesforce.com/articleView?id=000326486&type=1&mode=1>) for more information.

#### How do I check the number of Salesforce API calls left for the day?

To check the number of Salesforce API calls, go to **Setup** > **Administration Setup** > **Company Profile** > **Company Information**. You should then be able to see a field called **API Requests, Last 24 Hours** , which contains the number of API calls left for the day.

#### Does RudderStack support dev instances of Salesforce?

No, RudderStack does not support Salesforce dev instances (for example, `https://companyabc-dev-ed-develop.lightning.force.com/`) currently.

#### How to fix “No such column ‘X’ on object of type Y” errors?

If event delivery to Salesforce fails due to the non-existence of a provided field - even though the field does exist - check the field-level security settings for that field in Salesforce.

When the field is **not** marked as visible to the role your RudderStack Salesforce user is using, you will get this error. To fix it, make the field visible to the appropriate role.