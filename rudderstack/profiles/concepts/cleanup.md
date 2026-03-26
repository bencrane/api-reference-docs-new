# Cleanup

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# Cleanup

Learn about the cleanup command in Profiles.

* * *

  * __4 minute read

  * 


This guide introduces you to the concept of cleanup in Profiles.

## Overview

You can use the `pb cleanup materials` command in RudderStack Profiles to remove any outdated materials (tables, views) from the data warehouse - thereby optimizing storage and ensuring that unnecessary historical materials do not accumulate over time.

There are two ways to perform a material cleanup - old and new.

## Old version

This version of cleanup decides which materials to delete depending on the time when PB last accessed it.

This is the default mode now, meaning running `pb cleanup materials` triggers this mode automatically.

You can also specify a retention period in the above command by adding any of the following three flags:

  * `-r`
  * `--retention_time_in_ms`
  * `--retention_time_in_hours`


> ![info](/docs/images/info.svg)
> 
> If no flag is passed, RudderStack considers a default retention period of 180 days.

### Usage

Some examples of using the cleanup command are shown:
    
    
    $pb cleanup materials # Deletes materials whose last access time is greater than 30 days.
    
    $pb cleanup materials -r 1 # Deletes materials whose last access time is greater than 1 day.
    
    $pb cleanup materials --retention_time_in_ms 5 # Deletes materials whose last access time is greater than 5 milliseconds.
    
    $pb cleanup materials --retention_time_in_hours 3 # Deletes materials whose last access time is greater than 3 hours.
    

### Limitations

Note that the old version create issues while performing cleanups in cases where you are using timegrains.

Suppose you have a Profiles project which has:

  * A weekly timegrain model that runs once per week and no other models of a finer timegrain depend on it.
  * An hourly timegrain model that runs more frequently.
  * Some models with a default timegrain of tick.


When you run this project daily, models only with timegrain finer than or equal to a day run everyday. However, the weekly model runs only once per week.

If you run the cleanup on the fourth day after the weekly model was run with a retention period of 3 days, then the cleanup will delete its materials, even though the [frontier views](<https://www.rudderstack.com/docs/profiles/additional-resources/glossary/#frontier-views>) still need them.

A project run after this incident will again run the weekly timegrain model because it is deleted - this is inefficient. Also, the frontier views become useless as underlying materials are deleted.

A new version of cleanup is available to overcome the above limitations.

## New version

> ![warning](/docs/images/warning.svg)
> 
> Use this mode if you are using timegrains in your Profiles project.

When PB runs, the `retention_period` parameter defined in the `pb_project.yaml` is recorded in the material registry against the models. The new cleanup version uses this value and also does dependency tracking when deciding which materials to delete.

You can specify the `retention_period` in the project as follows:

  * In the [`pb_project.yaml`](<https://www.rudderstack.com/docs/profiles/dev-docs/pb-project-yaml/>):


    
    
    name: profiles_project
    schema_version: 85
    connection: wh_connection_dev
    
    retention_period: 24h # 1 day
    

You can also specify `retention_peroid` at the model level as well:
    
    
    models:
      - name: user_id_stitcher
        model_type: id_stitcher
        model_spec:
          entity_key: user
          retention_period: 24h
          edge_sources:
            - from: inputs/rsIdentifies
            - from: inputs/rsPages
    

Note that:

  * `retention_period` should be strictly a non-zero positive value.
  * RudderStack considers a default retention period of 30 days if not explicitly defined in the YAML using the `retention_period` key.


> ![warning](/docs/images/warning.svg)
> 
> If you have set up the Profiles project in the RudderStack dashboard, then the retention period specified in the project’s settings will be used during cleanup.

### Usage

Pass the `--expired` flag in the `pb cleanup materials` command to trigger this mode.
    
    
    pb cleanup materials --expired
    

### Deletion criteria

The criteria this cleanup mode uses to determine which materials to delete is explained below:

#### Expiration criteria

  * Every model has a **retention period** , which you can set at the **model level** or for the **entire project**.

  * A material is considered **expired** if all of the below conditions are met:

    * Its **last access/reference time** is before the current time - retention period.
    * There exists a **newer run of the same model**.
    * No other **non-expired material depends on this material**.


#### Preventing accidental deletion

This mode ensures that cleanup happens safely without unintentionally deleting materials that are still in use.

  * [![](/docs/images/previous.svg)Previous](</docs/profiles/concepts/sql-models/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/dev-docs/>)