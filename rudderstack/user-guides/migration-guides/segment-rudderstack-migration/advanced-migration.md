# Phase 2: Advanced Migration Techniques

Advanced migration techniques to ensure a smooth and complete migration from Segment to RudderStack.

* * *

  * __10 minute read

  * 


This guide explores some more advanced techniques to ensure a smooth and complete migration from Segment to RudderStack.

One of the critical aspects of migrating from Segment to RudderStack is ensuring that historical user data is appropriately handled. RudderStack provides several options for migrating user data, depending on your specific requirements and the complexity of your data.

## Migrate user data

**Call the Segment SDK from RudderStack to migrate anonymous ID, user ID, and user traits**

If you have the Segment SDK implemented in your application, you can leverage it to migrate user data to RudderStack by following these steps:

  1. Implement the RudderStack SDK alongside the Segment SDK in your application.
  2. In the RudderStack SDK initialization code, add a callback function to the `load` method:


    
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
      onLoaded: function(rudderanalytics) {
        const segmentAnon = analytics.user().anonymousId();
        const segmentUserId = analytics.user().id();
        const rudderUserId = rudderanalytics.getUserId();
        if (segmentAnon) {
          rudderanalytics.setAnonymousId(segmentAnon)
        }
    
        if (segmentUserId && (!rudderUserId || (rudderUserId != segmentUserId))) {
          rudderanalytics.identify(segmentUserId)
        }
      }
    });
    

This code snippet retrieves the user’s anonymous ID, user ID, and traits from the Segment SDK and sends them to RudderStack using the `setAnonymousId` and `identify` methods.

  3. Deploy the updated code to your application and verify that user data is being sent to RudderStack.


> ![success](/docs/images/tick.svg)
> 
> **Trace data flow from sources to destinations**
> 
> You can leverage the [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) feature or the [Events tab](<https://www.rudderstack.com/docs/dashboard-guides/event-metrics/>) of the specific resource to trace data flowing into your downstream destinations. This helps you understand how your data is being transformed and consumed and identify any potential issues or bottlenecks in your data pipelines.

**Include previously used Segment anonymous IDs**

If you rely heavily on anonymous user tracking and don’t have access to the Segment SDK, you can migrate anonymous user data using RudderStack’s `anonymousIdOptions` feature.

  1. Enable the `anonymousIdOptions` feature in the RudderStack SDK initialization code:


    
    
    rudderanalytics.load("WRITE_KEY", "DATA_PLANE_URL", {
      anonymousIdOptions: {
        localStorage: true,
        cookie: {
          name: "ajs_anonymous_id",
          domain: "your-domain.com",
          path: "/"
        }
      }
    });
    

This code snippet instructs RudderStack to retrieve the anonymous ID from the `ajs_anonymous_id` cookie set by Segment and store it in local storage.

  2. Deploy the updated code to your application and verify that anonymous user data is being sent to RudderStack.


**Retrieve user data from local storage or cookies**

If you have stored user data in local storage or cookies, you can migrate that data to RudderStack using a custom script:

  1. Retrieve the user data from local storage or cookies:


    
    
    // Just like in the Segment SDK example above but from local storage
    
    rudderanalytics.load(WRITE_KEY, DATA_PLANE_URL, {
          onLoaded: function(rudderanalytics) {
              const segAnonymousId = localStorage.getItem("ajs_anonymous_id");
              const segmentUserId = localStorage.getItem("ajs_user_id");
              ....
    

  2. Send the user data to RudderStack using the SDK methods as before:


    
    
    rudderanalytics.setAnonymousId(segAnonymousId);
    rudderanalytics.identify(segmentUserId, segmentTraits);
    

  3. Deploy the custom script to your application and verify that user data is being sent to RudderStack.
  4. Once the data migration is complete, clean up the local storage or cookies to remove the Segment-related data when you are ready.


> ![warning](/docs/images/warning.svg)
> 
> Remember to thoroughly test your data migration to ensure all user data is accurately migrated to RudderStack. Monitor your RudderStack dashboard for any data discrepancies or anomalies during the migration process.

## Incrementally migrate high-traffic applications

For some customers with high-traffic applications or especially complex environments, an incremental migration approach may be preferable to minimize disruption and risk. Here’s how you can incrementally migrate from Segment to RudderStack:

  1. Identify a subset of your application or user base to start the migration process, such as a specific geographic region, user cohort, or product area.
  2. Set up a parallel tracking implementation where you send data to both Segment and RudderStack for the selected subset of users or application components. This can be achieved by conditionally loading both the Segment and RudderStack SDKs based on user or application criteria.
  3. Monitor the data flow and consistency between Segment and RudderStack for the migrated subset, ensuring that events and user traits are being correctly captured and forwarded by RudderStack.
  4. Gradually expand the scope of the migration by adding more users, regions, or product areas to the RudderStack implementation while continuously monitoring data quality and consistency.
  5. Once you have migrated all of your applications and are confident in the RudderStack implementation, you can complete the migration by removing the Segment SDK and updating any remaining downstream systems to use the RudderStack data.
  6. Continuously monitor your RudderStack data pipelines for any anomalies or discrepancies, and address any issues promptly to ensure a smooth post-migration experience.


By adopting an incremental migration approach, you can minimize the risk of data loss or disruption and ensure a seamless transition from Segment to RudderStack.

## Migrate legacy app versions running the Segment SDK

Companies who offer apps across multiple platforms often have a subset of users running outdated app versions. This is often due to users not updating their apps or using older devices that do not support newer operating systems. These cases are most common for apps on mobile and TV devices (for example, iOS devices or Roku OTT devices).

When migrating from Segment to RudderStack, only the latest version of an app will include the RudderStack SDK. Older app versions will still be running the Segment SDK.

If users running older app versions represent a meaningful percentage of overall users, you can use RudderStack’s Segment source integration to maintain full data capture across your user base during the migration. Because this data will be ingested into RudderStack, you can manage data quality and destinations integrations in a single platform (RudderStack), simplifying the migration process.

Here’s the high level process for incrementally migrating legacy app versions off of Segment:

  1. Identify the data sources in Segment that represent older app versions.
  2. Configure [Segment as a source](<https://www.rudderstack.com/docs/sources/event-streams/cloud-apps/segment/#getting-started>) in RudderStack. This will require setting up a webook destination in Segment. We recommend setting up a dedicated RudderStack Segment source (and related Segment webhook destination) for legacy app versions.
  3. Point the Segment sources that represent legacy apps at the webhook destination. At this point, that data will be flowing to RudderStack and sent to all RudderStack destinations, fully centralizing your data management.
  4. **Once you have completed the migration of new app versions to RudderStack SDKs, you can significantly decrease your Segment bill by only using Segment to collect data from legacy app version sources.**
  5. Monitor the percentage of total users that are running legacy app versions.
  6. When the percentage of total users reaches your desired threshold (often a few percent), you can fully migrate off of Segment and close your Segment account.


## Ensure data governance during migration

Data governance and data quality are essential aspects of any successful customer data platform migration. RudderStack provides a range of features and best practices to help you maintain high-quality data throughout the migration process and beyond.

### Data catalog for data definitions, and discovery

RudderStack’s [Data Catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>) feature provides a centralized view of your event schema, making it easy to discover, understand, and govern your customer data.

Here’s how you can leverage the data catalog for data discovery:

  * **Explore event schemas and properties** : The data catalog allows you to browse and search your event schemas, helping you understand the structure and content of your event data. You can view event names, properties, and sample payloads, making identifying relevant data for analysis and activation easier.
  * **Collaborate with teams using data catalog documentation** : The data catalog provides a collaborative platform for documenting and sharing knowledge about your event data. You can add descriptions, tags, and annotations to your event schemas, making it easier for teams across your organization to understand and use your customer data effectively.


By leveraging RudderStack’s data catalog, you can improve data discovery, and collaboration, ensuring that your teams have a shared understanding of your customer data and can use it effectively for analysis and activation. Using a data catalog can also help you prevent issues you may have had in your Segment implementation with bad data or inconsistent naming.

### Tracking plans for data quality and violation management

[Tracking Plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>) are a powerful tool for standardizing and governing your event data, ensuring that your data is consistent, accurate, and aligned with your business objectives. Here’s how you can implement tracking plans in RudderStack:

  * **Define standard events and properties in tracking plans** : Create a tracking plan that defines your standard event names, properties, and data types. This helps ensure that your event data is consistent across your sources and destinations, making it easier to analyze and activate.
  * **Validate event implementation against tracking plans** : Use RudderStack’s tracking plan validation feature to automatically compare your incoming event data against your defined tracking plan. This helps identify discrepancies or errors in your event implementation, such as missing properties or incorrect data types.
  * **Monitor data quality and identify discrepancies** : Set up data quality monitoring in RudderStack to continuously track the quality and consistency of your event data. Use RudderStack’s data quality reports and alerts to identify any discrepancies or anomalies in your data, such as sudden changes in event volume or property values.
  * **Evolve tracking plans to support new use cases and data needs** : As your business evolves and new use cases emerge, update your tracking plans to reflect your changing data requirements. This helps ensure that your event data remains relevant and actionable and supports your ongoing analytics and activation needs.


By implementing tracking plans and data quality monitoring in RudderStack, you can standardize your event data, ensure data cleanliness, consistency, and accuracy, and evolve your data governance practices to support your growing business needs.

### Transformations for data cleansing and enrichment

RudderStack’s [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) feature allows you to clean, enrich, and transform your event data in real-time, ensuring that your downstream systems receive high-quality, actionable data.

> ![success](/docs/images/tick.svg)
> 
> RudderStack also provides some [pre-built JavaScript functions](<https://www.rudderstack.com/docs/transformations/templates/>) that you can use to create transformations and implement a variety of use cases on your event data.

Some common use cases for RudderStack transformations are listed below:

**Fix bad data**

If you have violations in your tracking plan, you can quickly fix them using a transformation to rename the events. Renaming events is one of the most popular transformations when migrating from Segment to RudderStack.
    
    
    /***
     * This transformation renames properties to conform with the appropriate naming convention,e.g, rename "first_name" to "firstName." This allows you to change property names to those expected by downstream destinations.
     ***/
    
    export function transformEvent(event, metadata) {
      const firstName = event.context?.traits?.first_name;
      if (firstName) {
        event.context.traits.firstName = firstName;
        delete event.context.traits.first_name;
      }
      return event;
    }
    

**Mask sensitive PII**

If your event data contains sensitive personally identifiable information (PII), such as email addresses or phone numbers, you can use transformations to mask or hash that data before forwarding it to downstream destinations.
    
    
    /***
     * This transformation hashes sensitive personal data, e.g., email, birthday,social security number. This reduces the risk of accidentally disclosing personally identifiable information (PII). It uses the standard RudderStack 'sha256' library.
     ***/
    
    import {
      sha256
    } from "@rs/hash/v1";
    
    export function transformEvent(event, metadata) {
      const email = event.context?.traits?.email;
      if (email) event.context.traits.email = sha256(email);
      return event;
    }
    

**Enrich events with additional context**

You can use transformations to enrich your event data with additional context, such as user attributes, device information, or external API data.
    
    
    /***
    This transformation enriches events with geolocation data using an IP-to-geolocation API.This allows you to easily query events based on geolocation data, e.g., country, city.
    ***/
    
    export async function transformEvent(event, metadata) {
      if (event.request_ip) {
        try {
          const res = await fetchV2("<YOUR_API_ENDPOINT>" + event.request_ip); // Use your paid IP-to-geolocation API endpoint.
          event.context.geolocation = res.body;
        } catch {}
      }
      return event;
    }
    

By leveraging RudderStack transformations, you can ensure clean and consistent event data enriched with valuable context, enabling more accurate analysis and activation.

## Next steps

[Phase 3: Test and validate your migration](<https://www.rudderstack.com/docs/user-guides/migration-guides/segment-rudderstack-migration/migration-testing-validation/>)