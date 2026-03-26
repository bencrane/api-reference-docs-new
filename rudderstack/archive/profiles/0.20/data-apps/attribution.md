# AttributionAlpha

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Attribution Alpha

Unify cross-platform campaign data, track conversions, and calculate key performance metrics.

* * *

  * __9 minute read

  * 


> ![announcement](/docs/images/announcement.svg)
> 
> This feature is in **Alpha** as part of RudderStack’s [Early Access Program](<https://www.rudderstack.com/docs/get-started/alpha-and-beta-features/>), where we work with early users and customers to test new features and get feedback before making them generally available. Note that these features are functional but can change as we improve them.
> 
> Make sure to [contact](<mailto:support@rudderstack.com>) the RudderStack team before using them in production.

Marketing teams struggle to build a centralized view of paid campaign performance because reporting is siloed in individual ad platforms. To build that cross-platform attribution, data teams are often required to manage complex, high-maintenance models in their data warehouse.

RudderStack’s **Attribution Data App** simplifies the generation of attribution data sets for first and last touch paid campaigns. As an extension of RudderStack Profiles, this feature provides you with an intuitive configuration for the attribution model, then generates and runs the complex SQL for you in your own warehouse.

## Key features

  * **Unified campaign performance data** : Consolidates campaign performance data from digital campaigns across ad platforms and ties it to user activity from your apps and websites.
  * **Cross-platform tracking** : Uses the Profiles ID stitcher, which reconciles individual entities from events across devices, sessions, and browsers.
  * **Complex entity support for accounts and households** : Reports on advertising ROI for complex business entities like accounts and households that often have multiple individual users participate in the customer journey.
  * **Multiple conversion goals** : Supports tracking multiple conversion types and multiple conversions for each campaign (purchases, subscriptions, signups, etc.)
  * **Paid performance metrics** : Calculates key metrics like Customer Acquisition Cost (CAC) and Return on Ad Spend (RoAS).
  * **Supports flexible, granular reporting** : Provides daily reports that can be aggregated to different time granularities for any dashboard use case.


## Prerequisites

  * An active RudderStack Profiles project (v0.18.0 or above).
  * Tables with the following data:
    * **Event Stream Data** : User activity touchpoints (usually the `page` and `track` call tables) to identify the first and last interaction points.
    * **Conversion Data** : Behavioral conversions you want to track, like `track` or `identify` tables for user signup or purchase events, or timestamped data points from other platforms, like an `Opportunity Created Date` from Salesforce.
      * **Revenue data** (optional): If you want to measure RoAS, your conversion data points must include a value like revenue, total cost, etc. This data does not necessarily have to be ingested via RudderStack but must have an associated timestamp.
    * **Ad Campaign Data** : ETL dataset (for example, cost, impressions, and engagement metrics) from platforms like Facebook, Google Ads, LinkedIn, etc.


## Project setup

This section guides you on setting up an `attribution` model within an existing Profiles project.

> ![info](/docs/images/info.svg)
> 
> You will first need to add several components to your core Profiles project if they don’t exist yet. These components are a part of the attribution model configuration.

### Add required components to your Profiles project

This section guide assumes you have already created a [business entity](<https://www.rudderstack.com/docs/archive/profiles/0.20/concepts/entities/>) (like `user`) and an [ID stitcher model](<https://www.rudderstack.com/docs/archive/profiles/0.20/concepts/identity-graph/>) for that entity as part of an existing Profiles project.

#### Step 1: Define a `campaign` entity

In addition to your business entity, define a `campaign` entity in `profiles.yaml`. This entity will consolidate campaign data from multiple campaign performance tables.

#### Step 2: Define inputs

Make sure you have all of the relevant tables from the Prerequisites section as input data sources in your Profiles project in the `inputs.yaml` file.

There are three types of inputs:

  * **Paid performance data from ad platforms** : This is the standard campaign performance data you would load from platforms like Google or Facebook using an ETL tool like Fivetran or Airbyte.

  * **Event data for entity touchpoints** : To compute an entity’s first and last touch, the attribution model reads from event tables to construct a chronological list of touchpoints. Hence, you must add event tables that represent your customer journey (if these are not already defined as inputs in your existing project).

  * **Event data for conversions** : The attribution model reports on conversions and uses the conversion’s timestamp to compute the end of the user journey. You must define these conversions as [`entity_vars`](<https://www.rudderstack.com/docs/archive/profiles/0.20/dev-docs/pb-project-yaml/entities/>) in the `profiles.yaml`. Common examples of conversions are `first_order_date` or `user_signup_date`.


#### Step 3: Create a `campaign` ID Stitcher model

Add an [ID Stitching](<https://www.rudderstack.com/docs/archive/profiles/0.20/dev-docs/profiles-yaml/id-stitcher/>) model for your `campaign` entity in the `profiles.yaml` file and configure it with following specifications:

  * Link various campaign identifiers like `utm_campaign`, `campaign_id`, etc.
  * Include user-journey tables (for example, `pages`, `tracks`) in this stitcher.
  * Ensure that the campaign identifier columns like `utm_campaign` contribute to the ID graph.


### Configure `attribution.yaml`

RudderStack recommends creating a new file `attribution.yaml` to keep your Profiles project organized. You can copy the sample model config code to get started.

#### Step 1: Configure touchpoints

Add your inputs as `touchpoints` in the `attribution.yaml` file.

Note that each table must satisfy the following conditions to be used as a part of the user journey that the attribution model creates:

  * It must be a part of both entities’ ID graph (user and campaign ID graph in this case).
  * It must have a timestamp column denoting the time when the user saw/clicked the campaign. This is defined as the `occured_at_col` key.


A sample `touchpoints` configuration is shown:
    
    
    touchpoints: 
        - from: inputs/pages
        - from: inputs/mobile_pages
          where: timestamp >= {{user.signup_date}} # optional
    

The `where` clause is optional and helps in filtering the parts of user journey that should not be considered for some conversions. For example, if you want to measure the efficiency of retargeting campaigns, you might not want to include the early parts of user journey. The `where` key takes a valid SQL where clause string, similar to the `where` clause in `entity_vars`. All the columns should be present in the same input table or can refer to the `entity_vars` of the model entity.

#### Step 2: Define conversions

Add the `entity_vars` that represent your conversions. Note that you can report on multiple conversions for each attribution model.

Optionally, you can define a `value` for each conversion, which the attribution model will use to compute total value generated and RoAS for each campaign.

A sample `conversion_vars` configuration is shown:
    
    
    conversion_vars:    
        - name: payer_conversion
          timestamp: user.first_paid_date
          value: user.first_order_amount # Optional - adding this creates an extra column called <conversion>_<model>_value (ex: signup_first_touch_value)
          conversion_window: 30d # Optional - takes values in minutes, hours, and days, 30m, 4h, 7d, etc. If provided, RudderStack considers the conversion to have happened if it is within this range only.
        - name: mql
          timestamp: user.user_mql_conversion_dt
    

#### Step 3: Configure campaigns

To configure your campaigns, add the start date, end date, and any columns generated by the campaign ID stitcher that you want to include in the attribution model output as campaign `entity_vars`.

The following snippet highlights a sample `campaign` configuration:
    
    
    campaign:
        entity_key: campaign
        campaign_start_date: campaign_start_date
        campaign_end_date: campaign_end_date
        campaign_vars: #These represent columns that will be repeated and are pulled from the campaign_var table
            - campaign_name
            - url
            - utm_source
            - utm_medium
            - utm_channel        
    

#### Step 4: Define campaign performance data

Lastly, define the campaign performance data points for `cost`, `impressions`, and `clicks`. RudderStack has standardized these for the campaign performance data loaded through Fivetran and Airbyte. [Reach out](<mailto:support@rudderstack.com>) to our team to request the templates.

A sample `cost` configuration is shown:
    
    
    campaign_details: #These represent columns that will be computed daily
        - cost:
            - from: inputs/ga_campaign_stats
              date: date 
              select: sum(cost_micros / 1000000 )
            - from: inputs/lkdn_ad_analytic_campaign
              date: day 
              select: sum(cost_in_usd)
            - from: inputs/fb_basic_campaign
              date: date 
              select: sum(spend)
    

> ![warning](/docs/images/warning.svg)
> 
> RudderStack will not be able to compute the RoAS and CAC fields if you do not provide the `cost` configuration.

#### Sample yaml for the attribution model

After completing the above steps, your `attribution.yaml` file will look similar to the following example:
    
    
        - name: campaign_performance_report
          model_type: attribution
          model_spec:
              entity_key: user
                  conversion: 
                      #entity_key: user
                      touchpoints: 
                          - from: inputs/pages
                          - from: inputs/mobile_pages
                      conversion_vars:    
                          - name: payer_conversion
                            timestamp: user.first_paid_date
                            value: user.first_order_amount # Optional - adding this creates an extra column called <conversion>_<model>_value (ex: signup_first_touch_value)
                            conversion_window: 30d
                          - name: mql
                            timestamp: user.user_mql_conversion_dt
                            # default lookback_value = 90 days
                  campaign:
                      entity_key: campaign
                      campaign_start_date: campaign_start_date
                      campaign_end_date: campaign_end_date
                      campaign_vars: #These represent columns that will be repeated and are pulled from the campaign_var table
                          - campaign_name
                          - url
                          - utm_source
                          - utm_medium
                          - utm_channel
                      campaign_details: #These represent columns that will be computed daily
                          - cost:
                              - from: inputs/ga_campaign_stats
                                date: date 
                                select: sum(cost_micros / 1000000 )
                              - from: inputs/lkdn_ad_analytic_campaign
                                date: day 
                                select: sum(cost_in_usd)
                              - from: inputs/fb_basic_campaign
                                date: date 
                                select: sum(spend)
                          - impressions:
                              - from: inputs/ga_campaign_stats
                                date: date 
                                select: sum(impressions)
                              - from: inputs/lkdn_ad_analytic_campaign
                                date: day 
                                select: sum(total_impressions)
                              - from: inputs/fb_basic_campaign
                                date: date 
                                select: sum(imp)
                          - clicks:
                              - from: inputs/ga_campaign_stats
                                date: date 
                                select: sum(clicks)
                              - from: inputs/lkdn_ad_analytic_campaign
                                date: day 
                                select: sum(total_clicks)
                              - from: inputs/fb_basic_campaign
                                date: date 
                                select: sum(clicks)                  
    

Note that:

  * The `touchpoints` section defines the user journey data sources.
  * The `conversion_vars` specify the conversion types and their associated data.
  * The `campaign` section outlines campaign-specific variables and daily performance metrics.
  * Ensure that all the referenced inputs and variables are properly set up in your Profiles configuration.


#### Step 5: Run your project

After configuring your project, you can run it using one of the following methods:

**Using Profile CLI**

If you have created your Profiles project locally, run it using the [`pb run` CLI command](<https://www.rudderstack.com/docs/archive/profiles/0.20/dev-docs/run-project/#run>) to generate output tables.

**Using Profiles UI**

Run your Profiles project by first uploading it to a Git repository and then [importing it in the RudderStack dashboard](<https://www.rudderstack.com/docs/archive/profiles/0.20/management/import-from-git/#steps>).

## Output

Once your project run is complete, Profiles generates an output table in your warehouse in the following format:

Column name| Description| Data source  
---|---|---  
REPORT_DATE| Report generation date. This is a constant value for all the rows in a table per output.  
  
**Example** : 19 July 2024| -  
CAMPAIGN_DATE| Actual interaction and spend date. For each campaign, RudderStack gets one row per date, from `campaign_start_date` till `campaign_end_date`, or current date, whichever is earliest.  
  
**Example** : 19 July 2024| -  
CAMPAIGN_PROFILE_ID| Unique campaign identifier created by the Profiles ID stitcher. The column name is not fixed and depends on the entity name.  
  
**Example** : rid033e88e4a945b710dab3e67c08391d65| Profiles  
IMPRESSIONS| Total daily impressions.  
  
**Example** : 364| Definition of `campaign_details`  
CLICKS| Total daily clicks.  
  
**Example** : 112| Definition of `campaign_details`  
COST (**A**)| Daily ad spend.  
  
**Example** : $119.27| Definition of `campaign_details`  
COUNT_DISTINCT_VIEWS| Unique users who clicked.  
  
**Example** : 76| Event stream  
COUNT_TOTAL_VIEWS| Total page views.  
  
**Example** : 102| Event stream  
[CONVERSION_TYPE]_FIRST_TOUCH_COUNT (**B**)| First-touch attributed conversions.  
  
**Example** : 3| Event stream  
[CONVERSION_TYPE]_LAST_TOUCH_COUNT (**C**)| Last-touch attributed conversions.  
  
**Example** : 2| Event stream  
[CONVERSION_TYPE]_FIRST_TOUCH_CONVERSION_VALUE (**D**)| First-touch conversion value.  
  
**Example** : $200.00| Event stream or payment platform  
[CONVERSION_TYPE]_LAST_TOUCH_CONVERSION_VALUE (**E**)| Last-touch conversion value.  
  
**Example** : $150.00| Event stream or payment platform  
[CONVERSION_TYPE]_FIRST_TOUCH_COST_PER_CONV| First-touch CAC (**A/B**)  
  
**Example** : $39.76| Calculated  
[CONVERSION_TYPE]_LAST_TOUCH_COST_PER_CONV| Last-touch CAC. (**A/C**)  
  
**Example** : $59.64| Calculated  
[CONVERSION_TYPE]_FIRST_TOUCH_ROAS| First-touch RoAS. (**D/A**)  
  
**Example** : $1.68| Calculated  
[CONVERSION_TYPE]_LAST_TOUCH_ROAS| Last-touch RoAS. (**E/A**)  
  
**Example** : $1.26| Calculated  
[CONVERSION_TYPE]_AVG_DAYS_TO_CONVERT_FROM_FIRST_TOUCH| Average days between the first touch date and conversion date for all users of that specific campaign whose first touch was on `campaign_date`.  
  
**Example** : 15| Calculated  
[CONVERSION_TYPE]_TOTAL_DAYS_TO_CONVERT_FROM_FIRST_TOUCH_ACROSS_USERS| Total days between the first touch date and conversion date for all users of that specific campaign whose first touch was on `campaign_date`. This is helpful if you roll the report to a different dimension, as average is not additive. Sum of this column, divided by the sum of the total conversions would give a new average at any granularity.  
  
**Example** : 30| Calculated  
  
If you define multiple conversions, the `[CONVERSION_TYPE]_` columns are repeated for each conversion, for example, `signup_first_touch_count`, `subscribed_first_touch_count`, etc.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.20/data-apps/overview/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.20/data-apps/propensity/>)