# RudderStack Feature Walkthrough

Understand the different RudderStack features and how they help you collect, transform, and activate your customer data.

* * *

  * __3 minute read

  * 


This guide walks you through the different RudderStack features from a data activation lifecycle standpoint - from data collection to unification and activation. It also highlights how RudderStack helps you in monitoring and ensuring good system health.

## Collect

> ![success](/docs/images/tick.svg)
> 
> RudderStack’s data pipelines simplify customer data collection and integration across your entire stack, eliminating expensive data wrangling and custom pipelines.

### Event Stream

RudderStack’s [Event Stream](<https://www.rudderstack.com/docs/data-pipelines/event-stream/>) feature helps you collect behavioral data from your websites, track user engagements from your mobile apps, and complement client-side tracking with events from your backend.

With over 200 pre-built integrations, including 16 SDKs, you can stream data directly to your warehouse and route events in real-time to all the downstream tools.

See the [Event Stream Quickstart](<https://www.rudderstack.com/docs/data-pipelines/event-stream/quickstart/>) guide to set up a Event Stream pipeline in less than 15 minutes.

### Transformations

RudderStack’s [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) feature lets you write custom functions in JavaScript or Python to implement specific use cases on your event data.

Transformations are easy to build, debug, and reuse. RudderStack also provides some prebuilt [templates](<https://www.rudderstack.com/docs/transformations/templates/>) to help you write custom functions for filtering, cleaning, enriching, and removing sensitive user information from events **before** they are routed to downstream tools.

### Data quality and compliance

RudderStack provides a holistic [data governance toolkit](<https://www.rudderstack.com/docs/data-governance/overview/>) to streamline data quality and compliance across your customer data stack.

You can leverage [Tracking Plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>) to enforce strict data quality checks on your inbound source events and standardize the events and properties sent to downstream tools using [Data Catalogs](<https://www.rudderstack.com/docs/data-governance/data-catalog/>) and real-time schema fixes.

RudderStack’s client-side SDKs offer integrated [consent management](<https://www.rudderstack.com/docs/data-governance/consent-management/>) and user deletion features so your business can comply with various data regulation laws like GDPR, CCPA, and others. You can also ensure data privacy by [enforcing custom rules](<https://www.rudderstack.com/docs/transformations/templates/#pii-management-and-privacy>) in your transformations to mask, encrypt, or remove sensitive PII from the events.

## Unify

> ![success](/docs/images/tick.svg)
> 
> RudderStack lets you unify every data point across user journeys and accelerate the time to value by automating identity resolution and creating comprehensive user profiles in your data warehouse.

### Profiles

RudderStack [Profiles](<https://www.rudderstack.com/docs/profiles/overview/>) lets you leverage the real-time events and user traits collected in your warehouse to establish a comprehensive identity graph to create a customer 360 view.

## Activate

> ![success](/docs/images/tick.svg)
> 
> RudderStack helps you activate real-time data and comprehensive user profiles across every downstream tool and team.

### Reverse ETL

With RudderStack’s [Reverse ETL](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/>) feature, your teams can send the enriched warehouse data and unified customer profiles to any downstream tool for activation use cases like personalization, engagement, and more.

See the [Reverse ETL Quickstart](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/quickstart/>) guide to set up and activate your Reverse ETL pipeline.

### Data Apps

RudderStack’s [Data Apps](<https://www.rudderstack.com/docs/profiles/data-apps/>) are ideal for data teams looking to leverage their customer 360 data for key use cases like:

  * [Attribution](<https://www.rudderstack.com/docs/profiles/data-apps/attribution/>): Generate attribution data sets for your paid campaigns.
  * [Propensity scores](<https://www.rudderstack.com/docs/profiles/data-apps/propensity/>): Predict the likelihood of specific user actions (churn, purchases, etc.) by leveraging machine learning algorithms.
  * [Real-time personalization](<https://www.rudderstack.com/docs/profiles/data-apps/real-time-personalization/>): Combine RudderStack’s API and integration features to make the customer 360 data available for your personalization use cases.


## Monitor

Monitoring the health of your data pipelines can be challenging. RudderStack provides a comprehensive [Health dashboard](<https://www.rudderstack.com/docs/data-governance/health-dashboard/>) that helps you track event volume trends, errors, and data violations across your [Event Stream](<https://www.rudderstack.com/docs/data-pipelines/event-stream/>) and [Reverse ETL](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/>) pipelines.

It also provides a robust [alerting system](<https://www.rudderstack.com/docs/data-governance/alerts/>) that gives real-time notifications for critical data issues, allowing you to take timely, proactive measures before they escalate into major problems.

RudderStack also provides a [Syncs](<https://www.rudderstack.com/docs/dashboard-guides/overview/#syncs>) feature that gives you observability into the syncs set up for your warehouse destinations.