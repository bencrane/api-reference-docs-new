# Predictive features

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Predictive features

Create predictive features with RudderStack and Snowflake without using MLOps

* * *

  *  __2 minute read

  * 


Predictive features like future LTV and churn propensity can be game changing for a business. If your marketing, customer success, and other teams want to use them, though, your company often faces a binary choice: use a one-size-fits-all solution within an existing SaaS platform (i.e., marketing automation tool), or build out ML and MLOps capabilities internally.

Both options have significant drawbacks. First, templated SaaS-based solutions can’t leverage all of your customer data and aren’t configurable, which results in low accuracy and impact. On the other hand, hiring data scientists and setting up MLOps is expensive and complex.

Modern data teams need an option in the middle: the ability to deploy model templates on all of their customer data, but without additional tooling, processes and headcount.

With RudderStack Predictions and Snowflake, you can create predictive features directly in your warehouse, without the need to set up MLOps processes and infrastructure. Predictions leverages the full power of Snowpark to run ML models within your existing data engineering workflow.

In this section, you will learn about two ways to build predictive features in RudderStack Predictions:

  1. [Set up automated features in the RudderStack UI](<https://www.rudderstack.com/docs/archive/profiles/0.12/example/predictive-features-snowflake/setup-automated-features/>) \- You can setup and run the jobs within the RudderStack UI. This process makes it easy for less technical users to implement basic predictive features.
  2. [Code your own custom predictions](<https://www.rudderstack.com/docs/archive/profiles/0.12/example/predictive-features-snowflake/custom-code/>) \- Predictions also supports a code-based approach that gives technical users full control to define custom predictive features that match their unique business logic.


It’s important to note that Predictions runs on top of RudderStack [Profiles](<https://www.rudderstack.com/docs/profiles/overview/>), a product that automates identity resolution and user feature development in Snowflake.

Predictions leverages the Profiles identity graph to train and run ML models. Because Predictions is part of Profiles, project outputs include an identity graph, standard user featuers (i.e., `last_seen`) and predictive user features (i.e., `percentile_churn_score_30_days`). Both types of features are built using RudderStack data sources and standardized feature definitions.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.12/example/sql-model/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.12/example/predictive-features-snowflake/prerequisite/>)