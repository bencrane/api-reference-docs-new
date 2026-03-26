# Setup Automated Features

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Setup Automated Features

Set up RudderStack to build automated features in the RudderStack UI

* * *

  *  __6 minute read

  * 


Setting up automated features in the RudderStack UI is a straight-forward process. Predictive features are configured within a Profiles project and automatically added to the feature table output when the project is run.

## Project setup

Follow the steps below to set up a project and build predictive features:

### Log into RudderStack

You can log-in [here](<https://app.rudderstack.com/login>).

### Navigate to Profiles screen

[![Predictive features in Snowflake](/docs/images/profiles/predictive-features-snowflake/Navigation.webp)](</docs/images/profiles/predictive-features-snowflake/Navigation.webp>)

### Enter a name and description

Enter a unique name and description for the Profiles Project where you want to build the predictive features.

[![Predictive features in Snowflake](/docs/images/profiles/predictive-features-snowflake/Profiles-Name.webp)](</docs/images/profiles/predictive-features-snowflake/Profiles-Name.webp>)

### Select sources

[![Predictive features in Snowflake](/docs/images/profiles/predictive-features-snowflake/Sources.webp)](</docs/images/profiles/predictive-features-snowflake/Sources.webp>)

Select your Snowflake warehouse. If you have not configured the Snowflake warehouse, set up an event stream connection to Snowflake in RudderStack ([see details here](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/>)) and refer to the setup steps above.

Once you select the warehouse, you will be able to choose from RudderStack event sources that are connected to Snowflake. In this example, the JavaScript source created above is used to write to the same schema as the sample data. Profiles will use the `PAGES`, `TRACKS`, `IDENTIFIES`, and `ORDER_COMPLETED` tables from that schema to build automated and predictive features.

## Map ID fields

[![Predictive features in Snowflake](/docs/images/profiles/predictive-features-snowflake/Map-ID.webp)](</docs/images/profiles/predictive-features-snowflake/Map-ID.webp>)

Map the fields from the source table(s) to the correct type of ID. The standard ID types are:

  * `user_id`
  * `anonymous_id`
  * `email`


**Note that for RudderStack event sources, standard ID column names will be mapped for you automatically**. If you have included additional identifiers in your payloads, you can map those custom column names to standard identifiers by clicking **Add mapping** at the bottom of the table.

### Map `Order_Completed` table

Click on **Add mapping** and map the `USER_ID` and `ANONYMOUS_ID` columns to standard identifiers to include the `ORDER_COMPLETED` table as a source for the identity graph and user features.

Source| Event| Property| ID Type  
---|---|---|---  
QuickStart Test Site| ORDER_COMPLETED| USER_ID| user_id  
QuickStart Test Site| ORDER_COMPLETED| ANONYMOUS_ID| anonymous_id  
[![Predictive features in Snowflake](/docs/images/profiles/predictive-features-snowflake/map-id-orders.webp)](</docs/images/profiles/predictive-features-snowflake/map-id-orders.webp>)

## Create default features in the UI

There are two types of automated features you can define in the UI:

  * Default features
  * Custom features


This guide focuses on the default features that are automatically generated.

### Set up default features

Default features are features commonly used in Profiles projects. RudderStack provides a template library for these features to make them easy to add to your project. Templated features give you access to over 40 different standard and predictive features, which are generated in Snowflake automatically.

[![Predictive features in Snowflake](/docs/images/profiles/predictive-features-snowflake/feature-categories.webp)](</docs/images/profiles/predictive-features-snowflake/feature-categories.webp>)

Default features are divided into 4 categories:

  * **Attribution** \- campaign, source, and churn features
  * **Demographics** \- user trait features
  * **Engagement** \- user activity features
  * **Predictive ML Features** \- predictive features


You can open the drop down menu for each category and select as many as you would like for your project.

[![Predictive features in Snowflake](/docs/images/profiles/predictive-features-snowflake/feature-attribution.webp)](</docs/images/profiles/predictive-features-snowflake/feature-attribution.webp>)

For this guide, select:

  * Attribution
    * `first_source_name`
    * `is_churned_30_days`
    * `is_churned_90_days`
  * Demographics
    * `first_name`
    * `last_name`
    * `state`
  * Engagement
    * `first_date_seen`
    * `last_date_seen`
    * `total_sessions_90_days`
    * `total_sessions_last_week`
  * Predictive ML Features
    * `percentile_churn_score_30_days`


It is important to remember that RudderStack runs all of the feature-generation code transparently in Snowflake. For any of the default features, other than Predictive ML Features, you can click on **Preview Code** and get a yaml code snippet defining that feature (the yaml definition is used to generate SQL). This is helpful for technical users who want a deeper understanding of feature logic (and a running start for coding their own features).

[![Predictive features in Snowflake](/docs/images/profiles/predictive-features-snowflake/churn-code-snippet.webp)](</docs/images/profiles/predictive-features-snowflake/churn-code-snippet.webp>)

#### Churn definition

RudderStack Predictions automatically generates a binary churn value for every user based on inactivity over a 7, 30, or 90-day period.

For example, to calculate the `is_churned_7_days` value, RudderStack looks for any activity timestamp for a particular user in the `TRACKS` and `PAGES` tables over the previous 7 day period. Practically, this means that RudderStack executes a ‘max timestamp’ query against those tables to see if users have viewed a page or performed other tracked actions (like clicks, form submits, add to carts, etc.) and then calculates the difference from today. If the query returns 7 or more, that means they haven’t performed any activity over the last 7 days and their `is_churned_7_days` trait is set to `1`.

#### How Predictions models percentile churn scores

Using the standard definition (no activity over a defined period), RudderStack Predictions automatically runs a python-based churn model in Snowpark that predicts whether users will become inactive (churn) over the next 7, 30, or 90-day period. This model is trained on existing user data, using the Profiles identity graph, so it is recommended that you have a minimum of 5,000-10,000 unique users to achieve accurate output for business use cases.

**How Predictions automates ML with Snowpark**

Predictions streamlines integration with Snowpark by using the authentication from your existing Snowflake integration in RudderStack.

In order to run models in Snowpark, there is one additional set of permissions required. To run Predictions jobs, you must have permission to create stages within your schema. For more information see the **CREATE STAGE** [documentation](<https://docs.snowflake.com/en/sql-reference/sql/create-stage#access-control-requirements>).

Once permissions are granted, you will be able to run jobs that produce predictive features. **If you have followed the steps in[Prerequisite](<https://www.rudderstack.com/docs/archive/profiles/0.13/example/predictive-features-snowflake/prerequisite/>) guide, that permission has already been granted.**

## Create custom features in the UI

If a needed feature is not in the template library, you can define a custom feature in the UI. Custom features can be standard or predictive features.

### Add Custom Features

[![Predictive features in Snowflake](/docs/images/profiles/predictive-features-snowflake/custom-feature.webp)](</docs/images/profiles/predictive-features-snowflake/custom-feature.webp>)

Click on **Add a custom feature** at the top of the page and build an `average_order` feature with the following values:

Field| Value  
---|---  
**Name**|  average_order  
**Description**|  Average Order Size including shipping, taxes, and discounts  
**Function Type**|  AGGREGATE  
**Function**|  AVG  
**Event**|  EVENTS.ORDER_COMPLETED  
**Property or Trait**|  TOTAL  
[![Predictive features in Snowflake](/docs/images/profiles/predictive-features-snowflake/custom-feature-define.webp)](</docs/images/profiles/predictive-features-snowflake/custom-feature-define.webp>)

Once complete click **Save**. The custom feature will be added to the top of the page.

## Set Schedule

There are three options to set a schedule for how often the feature generation job runs:

  * Basic
  * Cron
  * Manual


### Basic

[![Predictive features in Snowflake](/docs/images/profiles/predictive-features-snowflake/schedule-basic.webp)](</docs/images/profiles/predictive-features-snowflake/schedule-basic.webp>)

Schedule on a predetermined interval.

The frequency can be every:

  * 30 minutes
  * 1 hour
  * 3 hours
  * 6 hours
  * 12 hours
  * 24 hours


Then select a starting time for the initial sync.

### Cron

[![Predictive features in Snowflake](/docs/images/profiles/predictive-features-snowflake/schedule-cron.webp)](</docs/images/profiles/predictive-features-snowflake/schedule-cron.webp>)

Schedule using cron expressions for more specific scheduling (i.e. Daily on Tuesdays and Thursdays).

If you are not familiar with cron expressions, you can use the builder in the UI.

### Manual

Only runs when manually triggered within the UI. For this guide, select **Manual**.

## Save, review, and create project

### Save project

[![Predictive features in Snowflake](/docs/images/profiles/predictive-features-snowflake/save-project.webp)](</docs/images/profiles/predictive-features-snowflake/save-project.webp>)

Fill in the **Schema** field with `PROFILES` (to match what we created earlier). This is where the feature table will be written to in Snowflake.

### Review and create project

[![Predictive features in Snowflake](/docs/images/profiles/predictive-features-snowflake/review-create.webp)](</docs/images/profiles/predictive-features-snowflake/review-create.webp>)

Finally, review all the settings and when ready, click `Create user 360`.

## Review created features

Once the initial project run is initiated, it may take up to 25-30 minutes to complete. Once the job is done, you are able to explore the data in RudderStack’s UI, including model fit charts for predictive features and individual user records with all features.

[![Predictive features in Snowflake](/docs/images/profiles/predictive-features-snowflake/ui-predictive.webp)](</docs/images/profiles/predictive-features-snowflake/ui-predictive.webp>)[![Predictive features in Snowflake](/docs/images/profiles/predictive-features-snowflake/ui-predictive-graphs.webp)](</docs/images/profiles/predictive-features-snowflake/ui-predictive-graphs.webp>)[![Predictive features in Snowflake](/docs/images/profiles/predictive-features-snowflake/ui-explorer.webp)](</docs/images/profiles/predictive-features-snowflake/ui-explorer.webp>)

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.13/example/predictive-features-snowflake/prerequisite/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.13/example/predictive-features-snowflake/custom-code/>)