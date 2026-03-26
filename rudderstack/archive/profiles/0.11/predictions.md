# Predictions (Early Access)

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Predictions (Early Access)

Use Profiles’ predictive features to train machine learning models.

* * *

  * __7 minute read

  * 


Predictions extends Profiles’ standard [feature development](<https://www.rudderstack.com/docs/archive/profiles/0.11/feature-development/>) functionality and lets you easily create predictive features in your warehouse. You can predict features like:

  * Is a customer likely to churn in the next 30 days?
  * Will a user make a purchase in the next 7 days?
  * Is a lead going to convert?
  * How much is a user likely to spend in the next 90 days?


Finally, you can add the predicted feature to user profiles in your warehouse automatically and deliver ML-based segments and audiences to your marketing, product, and customer success teams.

The following self-guided tour shows you how to build the predictive traits. You can follow the guide and build the project yourself, including sample data, in our [Predictions sample project](<https://www.rudderstack.com/docs/archive/profiles/0.11/predictions/predictive-features-snowflake/>).

## Use cases

This section covers some common Predictions use cases.

### Churn prediction

Predicting churn is one of the crucial initiatives across businesses. Without a predicted churn score, your actions are reactive, whereas you can act proactively with a user trait like `is_likely_to_churn`. Once you have such features, you can activate them with the appropriate outreach programs to prevent user churn.

### Customer LTV prediction

Predictions helps you understand your customers’ purchasing behavior over time. You can predict how much amount a particular customer is likely to spend within the prediction time range.

## Prerequisites

  * You must be using a [Snowflake](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/>) or [Redshift](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/redshift/>) warehouse.
  * You must set up a standard Profiles project with a [feature table model](<https://www.rudderstack.com/docs/archive/profiles/0.11/example/feature-table/>).
  * **Optional** : If you are using Snowflake, you might need to create a [Snowpark](<https://www.snowflake.com/en/data-cloud/snowpark/>)-optimized warehouse if your dataset is significantly large.


## Project setup

This section highlights the project setup steps for the churn prediction and LTV models.

### Churn prediction

Setting up Predictions for predicting churn involves four easy-to-follow steps:

  1. Set up a feature table with labels
  2. Configure training parameters to generate the predictive features.
  3. Configure prediction parameters to generate the predictive features.
  4. Schedule periodic Predictions to generate the predictive features.


### 1\. Set up a `feature_table_model`

Follow the [Feature table](<https://www.rudderstack.com/docs/archive/profiles/0.11/example/feature-table/>) guide to start with a basic Profiles project. The feature you want to predict should be a part of the feature table in the project.

For example, to predict 30-day inactive churn in advance, you should define it in the feature table so that the model knows how to compute this for historic users.
    
    
    entity_var:
      name: churn_30_days
      select: case when days_since_last_seen >= 30 then 1 else 0 end
    

### 2\. Training

RudderStack simplifies your training configuration to a set of parameters. Start with a [`python_model`](<https://www.rudderstack.com/docs/archive/profiles/0.11/predictions/python-models/>) type and mention the following parameters:
    
    
    train:
        file_extension: .json
        file_validity: 168h
        inputs: &inputs
          - packages/feature_table/models/shopify_user_features
        config:
          data: &model_data_input_configs
            label_column: churn_30_days
            label_value: 1
            prediction_horizon_days: 30
            output_profiles_ml_model: *model_name
            eligible_users: ''
            inputs: *inputs
            entity_column: user_main_id
            recall_to_precision_importance: 1.0
          preprocessing: 
            ignore_features: [name, gender, device_type]
    

Parameter| Description  
---|---  
`file_extension`  
Required| The file extension. This is a static value and does not need to be modified.  
`file_validity`  
Required| If the last trained model is older than this duration, then the model is trained again.  
`inputs`  
Required| Path to the base features project.  
`label_column`  
Required| Column for which we want the Predictions.  
`prediction_horizon_days`  
Required| Number of days in advance when the prediction should be made.  
  
See [Prediction horizon days](<https://www.rudderstack.com/docs/profiles/glossary/#prediction-horizon-days>) for more information.  
`output_profiles_ml_model`  
Required| Name of the model.  
`eligible_users`| Definition of the feature that needs to be defined only for a segment of users.  
  
For example, `country='US' and is_payer=true`  
`config.data.inputs`| Path to the referenced project. The `inputs` key above should have `&inputs` added to it.  
`entity_column`| If the value of`id_column_name` in the ID stitcher is changed, it should be referenced here too. This field is optional otherwise.  
`recall_to_precision_importance`| Also referred to as **beta** in f-beta score, this field is used in classification models to fine-tune the model threshold and give more weight to recall against precision.  
  
**Note** : This is an optional parameter. If not specified, it defaults to `1.0`, giving equal weight to precision and recall.  
`ignore_features`| List of columns from the feature table which the model ignores for training.  
  
#### 3\. Prediction

In your `python_model`, mention the following parameters:
    
    
    predict:
        inputs:
          - packages/feature_table/models/shopify_user_features
        config:
          data: *model_data_input_configs
          outputs:
            column_names:
              percentile: &percentile_name percentile_churn_score_7_days
              score: churn_score_7_days
            feature_meta_data: &feature_meta_data
              features:
                - name: *percentile_name
                  description: 'Percentile of churn score. Higher the percentile, higher the probability of churn'
    

Parameter| Description  
---|---  
`inputs`  
Required| Path to the base features project.  
`percentile`  
Required| Column in the output table having the percentile score.  
`score`  
Required| Column in the output table having the probabilistic score.  
`description`  
Required| Custom description to give for the feature.  
  
#### 4\. Scheduling

> ![info](/docs/images/info.svg)
> 
> [Contact us](<https://www.rudderstack.com/contact/>) to enable this feature for your account.

  1. Upload your project to a GitHub repository.
  2. Create a Profiles project in the [RudderStack dashboard](<https://app.rudderstack.com/>). Use the GitHub repository to set up the project.
  3. Schedule your project with the required cadence. Note that this schedule is for prediction.


Trainings are scheduled as per your configuration of the `file_validity` parameter in the `training` section of your project.

### LTV models

While the default labels in the churn prediction model are Boolean, Profiles also lets you predict a continuous variable like revenue or LTV. The configuration is almost similar to churn prediction with some minor adjustments.

#### Set up a `feature_table_model`

The steps are similar to the setup for churn prediction.

#### Training

Start with a [`python_model`](<https://github.com/rudderlabs/rudderstack-profiles-base-features-git-flow/blob/feature/prml-319-add-ltv-specific-predictive-feature-in-base-features/models/profiles-ml.yaml>) type and specify the following parameters:
    
    
    train:
        file_extension: .json
        file_validity: 168h
        inputs: &inputs
          - packages/feature_table/models/shopify_user_features
        config:
          data: &model_data_input_configs
            label_column: amount_spent_past_7_days
            task: regression
            prediction_horizon_days: 7
            output_profiles_ml_model: *model_name
            eligible_users: ''
            inputs: *inputs
            entity_column: user_main_id
          preprocessing: 
            ignore_features: [name, gender, device_type]
    

Parameter| Description  
---|---  
`file_extension`  
Required| The file extension. This is a static value and does not need to be modified.  
`file_validity`  
Required| If the last trained model is older than this duration, then the model is trained again.  
`inputs`  
Required| Path to the base features project.  
`label_column`  
Required| Column for which we want the Predictions.  
`task`| Set to `regression`. Unless specified explicitly, Profiles sets it to `classification` by default.  
`prediction_horizon_days`  
Required| Number of days in advance when the prediction should be made.  
  
See [Prediction horizon days](<https://www.rudderstack.com/docs/profiles/glossary/#prediction-horizon-days>) for more information.  
`output_profiles_ml_model`  
Required| Name of the model.  
`eligible_users`| Definition of the feature that needs to be defined only for a segment of users.  
  
For example, `country='US' and is_payer=true`  
`config.data.inputs`| Path to the referenced project. The `inputs` key above should have `&inputs` added to it.  
`entity_column`| If the value of`id_column_name` in the ID stitcher is changed, it should be referenced here too. This field is optional otherwise.  
`ignore_features`| List of columns from the feature table which the model ignores for training.  
  
> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * Unlike churn prediction, you should not specify the `label_value` and `recall_to_precision_importance` labels.
>   * The LTV model introduces a new parameter called `task` which you must set to `regression`. Profiles assumes a classification model by default, unless explicitly specified otherwise.
> 


#### Prediction

The `python_model` for the LTV use case remains almost the same as churn prediction, except some minor changes:
    
    
    predict:
        inputs:
          - packages/feature_table/models/shopify_user_features
        config:
          data: *model_data_configs
          preprocessing: *model_prep_configs
          outputs:
            column_names:
              percentile: &percentile_name percentile_predicted_amount_spent
              score: predicted_amount_spent
            feature_meta_data: &feature_meta_data
              features:
                - name: *percentile_name
                  description: 'Percentile of predicted future LTV. Higher the percentile, higher the expected LTV.'
    

Parameter| Description  
---|---  
`inputs`  
Required| Path to the base features project.  
`percentile`  
Required| Column in the output table having the percentile score.  
`score`  
Required| Column in the output table having the probabilistic score.  
`description`  
Required| Custom description to give for the feature.  
  
> ![info](/docs/images/info.svg)
> 
> The label column is missing in the above `predict` block as the `score` parameter captures the actual prediction value and a Boolean flag is not meaningful in regression use cases.

#### Scheduling

The steps are similar to the setup for churn prediction.

## Results

Final output or the predicted features are pushed to your customer360 table. Use the **Explorer** tab to check the predicted value for any given user along with the historical values up to last 5 runs.

> ![info](/docs/images/info.svg)
> 
> To check the predicted value for a given user:
> 
>   1. In the **Preview** section, go to the **Predictive features** tab.
>   2. Check the user profile for which the predictive feature has a value.
>   3. Search the **USER_MAIN_ID** of the profile in **Profile viewer**.
> 


[![Predictions predictive feature value](/docs/images/profiles/profilesml-predictivefeaturevalue.webp)](</docs/images/profiles/profilesml-predictivefeaturevalue.webp>)

The value of the predictive feature is a probability. You can consider it as `true` or `false` based on your threshold.

All your predictive features are listed separately in the **Overview** tab of your Profiles project. You can check the logs of each run in the `artifacts` directory (available in the **History** tab of your Profiles project).

[![ProfilesML artifacts](/docs/images/profiles/profilesml-artifacts.webp)](</docs/images/profiles/profilesml-artifacts.webp>)

## FAQ

#### **Is there a project to understand Predictions further?**

You can check the [Shopify churn model](<https://github.com/rudderlabs/rudderstack-profiles-shopify-churn/>) that builds a churn prediction score on top of the Shopify library project.

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.11/feature-development/sql-models/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.11/predictions/python-models/>)