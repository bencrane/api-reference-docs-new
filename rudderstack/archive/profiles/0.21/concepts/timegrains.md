# Timegrains

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Timegrains

Learn about Timegrains in Profiles.

* * *

  * __3 minute read

  * 


This guide introduces you to the concept of Timegrains in Profiles and shows how to define them in your Profiles project.

## Overview

Timegrains gives you the ability to control the frequency at which certain models run irrespective of the frequency at which you trigger the project runs.

You can define the following timegrains in your model’s `model_spec` file:
    
    
    tick, tenminutes, hour, day, week, month, year
    

For example, suppose you have defined a feature for which you do not need the most updated data, for example, computing a feature for each user every month. You can then set the `time_grain` : `month` and run the project. Profiles Builder ensures that this feature is computed only once a month. The computed values from the month boundary are used in all the subsequent `feature_views`. Any new identified user identified after the start of the month boundary will have the value of that feature set to `null`.

Note that:

  * You will get the same output if you specify a model’s `time_grain` to be `day` and you run this model multiple times a day.
  * If a model’s `time_grain` is specified to be `day`, it will only consider input data until that day’s boundary (`00:00 UTC`). Any data ingested after this timestamp is not considered in the computation.
  * The boundary for a particular month is the first Monday of that month. For example, if March 1 is a Friday, then it’s boundary will be March 4th. Similarly, the boundary for the year is the first Monday of that year.


## Usage

You can specify the timegrain in model_spec of any model. An example is shown below:
    
    
    models:
      - name: users_with_valid_email
        model_type: entity_cohort
        model_spec:
          extends: user/all
          time_grain: "day"
          filter_expression:
            AND:
              - "NOT {{ user.Var('id_type_email_count') }} = 0"
          feature_views:
            name: users_with_valid_email_feature_view
    

You can also specify it at `var_group` level. For example:
    
    
      - name: weekly_user_vars
          entity_cohort: models/new_users
          time_grain: "week"
          vars:
            - entity_var:
                name: campaign_sources
                select: "{{list_agg('context_campaign_source', ',')}}"
                from: inputs/rsTracks
    

Note if you have specified `time_grain` on any of the model, PB will need you to specify a `default_time_grain` in your `pb_project.yaml` file. Its value should be equal to or lower than the finest `time_grain` you have used in any of the models. This `default_time_grain` will be applied to all the models which don’t have a specified `time_grain`.
    
    
    default_time_grain: day
    

For example, if you have specified `day`, `week`, and `month` as your timegrains for all your models, you will need to specify `default_time_grain: day` . You can also set `default_time_grain` to `tick`, `tenminutes`, or `hour` \- however, this is **not** recommended as it may negatively impact the performance.

As a general rule, note that you should specify the `default_time_grain` to match with your run schedule. If you are scheduling PB to run daily, its best to keep `default_time_grain: day`. You can then accordingly schedule the run at `00:00 UTC` so that the latest data is considered in the run.

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.21/concepts/cohort/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.21/concepts/sql-models/>)