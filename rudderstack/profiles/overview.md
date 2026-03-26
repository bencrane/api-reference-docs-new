# Profiles Overview

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# Profiles Overview

Introduction to RudderStack’s Profiles feature.

* * *

  * __4 minute read

  * 


Modern data teams rely on their warehouse as a single source of truth for customer data. RudderStack’s **Profiles** is a declarative framework that transforms configuration into optimized SQL — letting you define **what** a customer looks like (identity rules, features, cohorts) rather than **how** to compute it.

Unlike traditional semantic layers that abstract SQL, Profiles inverts the paradigm: you declare entities and their attributes in version-controlled YAML, and the system generates warehouse-native SQL that handles identity resolution, incremental computation, and feature aggregation automatically.

With Profiles, data teams can stop maintaining thousands of lines of brittle SQL and start maintaining clean, reviewable configurations that compile to a comprehensive customer 360 table.

> ![success](/docs/images/tick.svg)
> 
> Check the comprehensive [12-part video series on RudderStack Profiles](<https://www.youtube.com/playlist?list=PLmlCAvdaZkW6dbdgkYPDP8ybIZcSlVBGx>) to build an end-to-end Profiles project that helps you:
> 
>   * Solve identity resolution at the root
>   * Create an identity graph with all your customer data
>   * Model powerful Customer 360 views in your data warehouse
> 


## Why use Profiles?

Data teams typically choose between two painful paths: maintaining sprawling SQL codebases with complex dependencies, or locking into rigid SaaS platforms that can’t model their unique business logic.

Profiles offers a third way — **declarative customer data modeling** :

Traditional approach| Profiles approach  
---|---  
Write complex SQL joins across identity tables| Declare identity types and stitching rules in YAML  
Build and maintain aggregation pipelines| Define features as `select` expressions; system handles grouping  
Manage incremental logic manually| Declare once; incremental computation is automatic  
Debug SQL across dozens of files| Review diffs in version-controlled configuration  
  
This declarative DNA means your team defines the **semantics** — what constitutes a user, what “lifetime value” means for your business — while Profiles handles the **mechanics** of [Identity Graphs](<https://www.rudderstack.com/docs/profiles/concepts/identity-graph/>), table scans, and efficient computation.

#### Move faster with an end-to-end platform

Profiles integrates directly with RudderStack’s other pipelines:

  * [Event Stream](<https://www.rudderstack.com/docs/sources/event-streams/>) pipelines have known schemas and unique identifiers through the ingested customer data. Profiles can produce a baseline identity graph, and user features out of the box. Data teams can then augment the graph and features using any other data in their warehouse.
  * [Reverse ETL](<https://www.rudderstack.com/docs/sources/reverse-etl/>) pipelines make it easy to send data from the customer 360 table directly to the downstream tools used by marketing, customer success, product, and other teams.


#### Enrich user profiles with features

You can [enhance user profiles](<https://www.rudderstack.com/docs/profiles/concepts/features/>) with additional data points and features. When new data sources are added, discovered, or calculated, data teams can add them to their Profiles configuration without having to clean data and update complex models and dependencies.

The features/traits can include demographic information, preferences, purchase history, browsing behavior, or other static or computed data points.

You can define the associated properties or attributes that provide detailed information for each new feature. For example, if the feature is `purchase_history`, its properties can include the date of purchase, product category, or order value.

#### Unlock deeper insights

Profiles extends its capabilities to support features derived from complex concepts such as funnels, organizational metrics, and machine learning models. You can understand your customer’s journey through your sales funnel or locate each user across the histogram of customer metric values by simply defining a trait.

#### Deliver personalization and recommendations

Using Profiles, you can ship [projects like personalization](<https://www.rudderstack.com/docs/profiles/data-apps/real-time-personalization/>) significantly faster by focusing entirely on activating key user features instead of cleaning and modeling data to build them.

#### Predict user conversions and churn

You can leverage [Propensity Scores](<https://www.rudderstack.com/docs/profiles/data-apps/propensity/>) to build predictive features that help you predict in advance whether a lead is likely to convert, or a customer is likely to churn or make a purchase.

## Who can leverage Profiles?

Profiles is built for data engineers, data scientists, and technical marketers who want **configuration over code**.

You define [identity stitching](<https://www.rudderstack.com/docs/profiles/concepts/identity-graph/>) rules, entity relationships, and user features in YAML—no hand-written SQL for identity resolution or feature computation. The declarative model means:

  * **Reviewable changes** : Pull request diffs show **what** changed in your customer model, not SQL syntax changes buried in logic.
  * **Composable features** : Entity vars reference each other naturally; the system resolves dependencies.
  * **Portable definitions** : Your customer model is decoupled from warehouse-specific SQL dialects.

  


  * [![](/docs/images/previous.svg)Previous](</docs/profiles/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/overview/how-profiles-works/>)