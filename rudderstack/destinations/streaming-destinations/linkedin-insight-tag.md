# LinkedIn Insight Tag

Send your event data from RudderStack to LinkedIn Insight Tag.

* * *

  * __5 minute read

  * 


The [LinkedIn Insight Tag](<https://business.linkedin.com/marketing-solutions/insight-tag>) is a JavaScript code for your website that lets you track your conversions and retarget your website visitors and customers who interact with your ads. You can use the resulting insights to learn more about your customers and optimize your marketing campaigns.

RudderStack supports integration with the LinkedIn Insight Tag where you can seamlessly send your event data to LinkedIn.

Find the open source code for this destination in the [GitHub repository](<https://github.com/rudderlabs/rudder-sdk-js/tree/develop/packages/analytics-js-integrations/src/integrations/LinkedInInsightTag>).

## Connection compatibility

Destination Information  
---  
  
  * **Status:** Generally Available
  * **Supported sources:** Web
  * Refer to it as **Linkedin Insight Tag** in the [Integrations object](</docs/sources/event-streams/sdks/rudderstack-javascript-sdk/filtering/#filtering-destinations>).

  
  
Connection Modes [__](</docs/destinations/rudderstack-connection-modes>)  
---  
Source|  Cloud mode| Device mode| Hybrid mode  
Web| ![supported](/docs/images/tick.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)  
  
Supported Message Types  
---  
Source| Identify| Page| Track| Screen| Group| Alias| Record| AudienceList  
Device mode  
Web| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![supported](/docs/images/tick.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)| ![not supported](/docs/images/no-image.svg)  
  
> ![info](/docs/images/info.svg)
> 
> In a web device mode integration, that is, using [JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>) as a source, the LinkedIn Insight Tag native SDK is loaded from `https://snap.licdn.com/` domain.
> 
> Based on your website’s content security policy, you might need to [allowlist this domain](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/load-js-sdk/#allowlist-destination-domain>) to load the LinkedIn Insight Tag SDK successfully.

## Getting started

> ![warning](/docs/images/warning.svg)
> 
> If you are already using LinkedIn Insight Tag on your website, removing it is highly recommended. This is because the RudderStack SDK automatically loads the Insight Tag tracking code and it may cause a conflict with the existing installation. For more information on the integration’s workflow, refer to the FAQ section below.

Once you have confirmed that the source platform supports sending events to LinkedIn Insight Tag, follow these steps:

  1. From your [RudderStack dashboard](<https://app.rudderstack.com/>), add a source. Then, from the list of destinations, select **LinkedIn Insight Tag**.
  2. Assign a name to the destination and click **Continue**.


### Connection settings

To successfully configure LinkedIn Insight Tag as a destination, you will need to configure the following settings:

[![LinkedIn Insight Tag connection settings](/docs/images/event-stream-destinations/insight-tag-connection-settings.webp)](</docs/images/event-stream-destinations/insight-tag-connection-settings.webp>)

  * **Partner ID** : Enter your LinkedIn partner ID.


> ![info](/docs/images/info.svg)
> 
> For more information on getting your LinkedIn partner ID, refer to the FAQ section below.

  * **Event Conversion IDs** : Enter the event name you want the Insight Tag to track and the corresponding conversion ID.


> ![warning](/docs/images/warning.svg)
> 
> The event names are case-sensitive. For example, RudderStack accepts `Order Completed`, `Order completed`, and `order completed` as three different events.

> ![info](/docs/images/info.svg)
> 
> For more information on getting the conversion ID, refer to the Tracking event-specific conversions section below.

  * **Client-side Events Filtering** : This setting lets you specify which events should be blocked or allowed to flow through to the LinkedIn Insight Tag.


> ![info](/docs/images/info.svg)
> 
> For more information on this setting, refer to the [Client-side Events Filtering](<https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/>) guide.

  * **Use device mode to send events** : As this is a [web device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>)-only destination, this setting is enabled by default and cannot be disabled.
  * **Consent management settings** : Configure the consent management settings for the specified source by choosing the **Consent management provider** from the dropdown and entering the relevant consent category IDs. See [Consent Management in RudderStack](<https://www.rudderstack.com/docs/data-governance/consent-management/overview/>) for more information on this feature.


## Tracking page loads

> ![info](/docs/images/info.svg)
> 
> For more information on the tracking methods supported by the Insight Tag, refer to the [LinkedIn support page](<https://www.linkedin.com/help/lms/answer/a425606?trk=hc-articlePage-peopleAlsoViewed>).

In this method, the Insight Tag automatically loads and tracks the conversions when users visit any pages on your website. Upon loading successfully, you can view the conversion status in your [Campaign Manager](<https://www.linkedin.com/campaignmanager/accounts>) dashboard:

[![LinkedIn Insight campaign manager dashboard](/docs/images/event-stream-destinations/insight-tag-campaign-manager.webp)](</docs/images/event-stream-destinations/insight-tag-campaign-manager.webp>)

## Tracking event-specific conversions

To track event-specific conversions, you need to first set up an Online Tracking conversion and define an event-specific conversion tracking. To do so, follow these steps:

  1. Sign into your [LinkedIn Campaign Manager](<https://www.linkedin.com/campaignmanager/accounts>).
  2. Click your account name and go to **Analyze** > **Conversion Tracking**.
  3. Click the **Create Conversion** button and select **Online Conversion**.

[![LinkedIn Insight online conversion option](/docs/images/event-stream-destinations/insight-tag-online-conversion.webp)](</docs/images/event-stream-destinations/insight-tag-online-conversion.webp>)

  4. Name your conversion and enter the relevant settings. For more information, refer to this [LinkedIn support page](<https://www.linkedin.com/help/lms/answer/a425606/set-up-linkedin-conversion-tracking?lang=en>).
  5. Click **Next step** and select the campaign to track your conversion.
  6. Under **Manually set up conversions** , go to **Define your conversion tracking method** and select **Event-specific**.
  7. Click **Copy code**. You will find the conversion ID listed here:

[![LinkedIn Insight online conversion ID](/docs/images/event-stream-destinations/insight-tag-conversion-id.webp)](</docs/images/event-stream-destinations/insight-tag-conversion-id.webp>)

> ![info](/docs/images/info.svg)
> 
> You will need to install this generated code in your website that automatically loads and tracks conversions for the specified event.

  8. Finally, specify the **Event Name** for which the Insight Tag automatically loads this snippet and the corresponding conversion ID in the **Event Conversion IDs** dashboard setting.


> ![info](/docs/images/info.svg)
> 
> The event names are case-sensitive.

#### Use-case

Suppose you add the following event name-conversion ID mapping in the RudderStack dashboard:

[![LinkedIn Insight event tracking use-case](/docs/images/event-stream-destinations/insight-tag-usecase.webp)](</docs/images/event-stream-destinations/insight-tag-usecase.webp>)

When you call the `Product Added` event, the LinkedIn Insight Tag automatically loads the snippet with the mapped conversion ID and tracks the conversion event.

A sample `Product Added` event is shown below:
    
    
    rudderanalytics.track("Product Added", {
      numberOfRatings: "12",
      name: "item 1",
    });
    

> ![warning](/docs/images/warning.svg)
> 
> RudderStack discards any `track` event that is not specified in the **Event Conversion IDs** dashboard setting.

## FAQ

#### How does this integration work?

The RudderStack-LinkedIn Insight Tag integration workflow is explained below:

  1. Configure **LinkedIn Insight Tag** as a destination in the [RudderStack dashboard](<https://app.rudderstack.com/>).
  2. Install the [RudderStack JavaScript SDK](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/quickstart/#step-1-install-javascript-sdk>) on your website.
  3. The JavaScript SDK automatically loads the Insight Tag tracking code.
  4. The Insight Tag starts tracking the user activities on your website.


#### What information can I track using the LinkedIn Insight Tag?

The LinkedIn Insight Tag lets you collect the data related to your users’ website visits, including the URL, IP address, referrer, device and browser characteristics, and timestamp.

#### Where can I find my LinkedIn partner ID?

To get the Partner ID, open the Insight Tag and get the value corresponding to the `_linkedin_partner_id` parameter:

[![LinkedIn Insight Tag partner ID](/docs/images/event-stream-destinations/insight-tag-partner-id.webp)](</docs/images/event-stream-destinations/insight-tag-partner-id.webp>)

Alternatively, you can follow the steps in this [LinkedIn support page](<https://www.linkedin.com/help/lms/answer/a417869/access-your-linkedin-partner-id?lang=en>) to access your LinkedIn partner ID.

> ![warning](/docs/images/warning.svg)
> 
> Each LinkedIn Insight Tag has a unique Partner ID. If the Partner ID of the tag on your website does not match the Partner ID in your account, the Insight Tag will be unable to collect the page loads and event-specific conversions.

### How can I verify if the event-specific conversions are tracked successfully?

Once you configure the **Event Conversion IDs** setting in the RudderStack dashboard, the LinkedIn Insight Tag automatically loads the code snippet and tracks the conversions for the specified events.

If the script has loaded correctly, it shows the label **Conversion status: Active** against the events in your dashboard:

[![LinkedIn Insight conversion status](/docs/images/event-stream-destinations/insight-tag-conversion-status.webp)](</docs/images/event-stream-destinations/insight-tag-conversion-status.webp>)

In case the script has not loaded correctly, you will see the **Conversion Status** as **Unverified** , **No recent activity** , or **Inactive**.

#### Will this integration slow my website down?

The RudderStack SDK loads asynchronously with your website. When loading the LinkedIn Insight Tag tracking snippet, it will not slow down your website’s performance at all.