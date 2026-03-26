# MoEngage Source

Ingest your event data from MoEngage into RudderStack.

* * *

  * __3 minute read

  * 


[MoEngage](<https://moengage.com>) is an intelligent customer engagement platform. It lets you personalize every customer interaction and drive better engagement, retention, loyalty and lifetime value.

This guide will help you set up MoEngage as a source in RudderStack. By leveraging [MoEngage Streams](<https://help.moengage.com/hc/en-us/articles/360045896572-MoEngage-Streams#introduction-0-0>), you can automatically forward your users’ engagement and activity events to RudderStack.

## Get started

  1. Go to your [RudderStack dashboard](<https://app.rudderstack.com/>) and click **Add Source**. From the list of **Event Streams** sources, select **MoEngage**.
  2. Assign a name to your source and click **Continue**.
  3. Your MoEngage source is now configured. Go to the **Settings** tab of the source and note the **Webhook URL** :

[![MoEngage source webhook URL](/docs/images/event-stream-sources/source-webhook-url.webp)](</docs/images/event-stream-sources/source-webhook-url.webp>)

  4. Log in to your [MoEngage dashboard](<https://dashboard-01.moengage.com/>). Go to **App Marketplace** , search for **RudderStack** , and click **Add Integration**.
  5. In the **Integrate** tab, add a name for your connection, enter the webhook URL obtained in Step 3 and select the events you want to forward to RudderStack.

[![MoEngage App Marketplace](/docs/images/event-stream-sources/moengage-1.webp)](</docs/images/event-stream-sources/moengage-1.webp>)

  6. Click **Connect** to save your details.


## Supported events

RudderStack ingests the following MoEngage events as [`track`](<https://www.rudderstack.com/docs/event-spec/standard-events/track/>) events, **without** any transformation:

  * [Lifecycle](<https://help.moengage.com/hc/en-us/articles/207836953-Derived-Events-Attributes#lifecycle-0-1>)
  * [Acquisition & Uninstall](<https://help.moengage.com/hc/en-us/articles/207836953-Derived-Events-Attributes#acquisition-uninstall-0-2>)
  * [Reachability](<https://help.moengage.com/hc/en-us/articles/207836953-Derived-Events-Attributes#reachability-0-4>)
  * [Campaign Activity](<https://help.moengage.com/hc/en-us/articles/207836953-Derived-Events-Attributes#campaign-activity-0-6>)


> ![success](/docs/images/tick.svg)
> 
> RudderStack also supports ingesting custom events defined in the MoEngage dashboard.

## Supported properties

RudderStack automatically ingests the following properties present in the above events:

Name| Description  
---|---  
App Version| The mobile application version on which the event is tracked. This property is tracked with all events.  
SDK Version| The version of the MoEngage SDK on which the event is tracked. This property is tracked with all events.  
Platform| The OS on which the event is tracked, for example, Android, iOS, or Web. This property is tracked with all events.  
Campaign Id| The campaign ID associated with the event.  
Campaign Name| Represents the name of the campaign of which the message was a part.  
Campaign Type| Represents the type of the campaign of which the message was a part.  
Readable Campaign Id| Represents the ID of the the campaign of which the message was a part.  
Parent Campaign id| Represents the campaign ID of parent periodic campaign; the child instances of which are re-run on a recurring basis. Tracked when a periodic campaign is run.  
Parent Flow Id| Represents the Flow ID of the parent journey campaign. Tracked when the journey campaign is run.  
Parent Flow Name| Represents the flow name of the parent journey campaign. Tracked when the journey campaign is run.  
Locale Id| Represents the ID of message locale. Tracked when the campaign is sent using Localization.  
Locale Name| Represents the name of the message locale. Tracked when the campaign is sent using Localization.  
Variation Id| Represents the ID of a message variation. Tracked when a campaign is sent using A/B Testing.  
URL| Tracked when display filter is selected in the in-app campaign.  
timestamp| The user’s time while performing the event in ISO 8601 timestamp format.  
First Session| Generated for all the events tracked with the MoEngage web SDK. The value is `True` only for the first user session.  
Logged In Status| Generated for all the events tracked with the MoEngage web SDK. The value is `True` only if the user has logged in on the device.  
Exit Reason| Tracked when a user exits the flow. This is tracked as an attribute of the **User Exited Flow** event.  
  
> ![info](/docs/images/info.svg)
> 
> Refer to MoEngage’s [Derived Events & Attributes](<https://help.moengage.com/hc/en-us/articles/207836953-Derived-Events-Attributes>) to know which attributes you can forward to RudderStack.