# Python Models

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Python Models

Profiles model for generating predictive features.

* * *

  * __2 minute read

  * 


Predictive features are generated using a new type of Profiles models called `python_model`.

## Using a Python model

There are two key steps involved in using a Python model - **train** and **predict**.

To use a Python model, you need to modify the `train` and `predict` blocks in your `profiles.yaml` file. The following snippet highlights these blocks:
    
    
    # This is a sample file, for detailed reference see: https://rudderlabs.github.io/pywht/
    models:
      - name: shopify_churn
        model_type: python_model
        model_spec:
          occurred_at_col: insert_ts
          entity_key: user
          validity_time: 24h # 1 day
          py_repo_url: https://github.com/rudderlabs/rudderstack-profiles-classifier.git
          predict:
            inputs:
              - packages/feature_table/models/shopify_user_features
            config:
              outputs:
                column_names:
                  percentile: &percentile_name percentile_churn_score_7_days
                  score: churn_score_7_days
                feature_meta_data: &feature_meta_data
                  features:
                    - name: *percentile_name
                      description: 'Percentile of churn score. Higher the percentile, higher the probability of churn'
          train:
            file_extension: .json
            file_validity: 60m
            inputs:
              - packages/feature_table/models/shopify_user_features
            config:
              data:
                label_column: is_churned_7_days
                label_value: 1
                prediction_horizon_days: 7
                model_name: 'shopify_user_features'
                
          <<: *feature_meta_data
    

In a Python model, the actual logic resides in a remote location defined by the key `py_repo_url`. This need not be modified for setting up a predictive feature.

In the `train` block, you can define the label columns by pointing to the `entity_var` defined in the feature table model. You also need to define the following:

  * Expected label value for users who performed the event.
  * Horizon days, that is, number of days in advance when the predictions need to be made.
  * Feature table model name defined for your predictive features project. See [Set up a feature table model](<https://www.rudderstack.com/docs/archive/profiles/0.11/predictions/#set-up-a-feature-table-model>) for more information.
  * Criteria for eligible users so the model need not be used to predict for all users. You can set this criteria by defining a SQL statement referring to the different `entity_vars`. For example:


    
    
    eligible_users: lower(country) = 'us' and amount_spent_overall > 0
    

The above example ensures that the model is trained only on the paying users from the US. Also, the model makes predictions only on this set of users.

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * The `eligible_users` key should be added as one more parameter in the data configuration.
>   * To build a model based on all available users, you can leave the `eligible_users` parameter blank.
> 


## Optional: Run Python model locally

> ![info](/docs/images/info.svg)
> 
> If you are using the RudderStack dashboard for running the models, you can skip this step. However, note that RudderStack runs the models locally a few time to get the correct setup.

To run Python models locally, you need to set up a Python environment with the required packages and add the Python path to the [`siteconfig.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.11/developer-guides/site-configuration/>) file.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.11/predictions/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.11/predictions/predictive-features-snowflake/>)