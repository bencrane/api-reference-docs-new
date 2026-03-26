# Profiles Changelog

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Profiles Changelog

[ __](<index.xml> "RSS")

Changelog for all the Profiles versions.

* * *

  * __59 minute read

  * Last modified: Mar 18, 2026


## Version 0.19.3

 _9 January 2025_

**Bug Fixes**

  * Properly sets the Snowflake connection parameter `application` to `Rudderstack_Warehouse`.


## Version 0.19.2

 _6 December 2024_

**Bug Fixes**

  * Fixed a common tables migration bug where PB may go into an unrecoverable state when you run it in two parallel processes.
  * Fixed an inconsistency in incremental ID stitching due to differences in how warehouses treat NULL values sorting.
  * Fixed a bug in incremental ID stitching related to occasional changes in the main IDs when you add new edges to the cluster.


## Version 0.19.1

 _29 November 2024_

**Bug Fixes**

  * Fixed a bug causing an unexpected change in the profiles ID when the ID stitcher is running in incremental mode.
  * Fixed a crash that occurs while parsing a YAML which starts with a list at the root level.


## Version 0.19

 _14 November 2024_  
 _Schema version: 84_

**What’s New**

  * Schema has been updated from 80 to 84.
  * Project created using `pb init pb-project` now locks the PB version.
  * Task summary is now shown at the end of each run, including relevant command details like start time, end time, sequence number, and total models processed (if any).
  * The number of iterations/loops during ID stitching are now logged.
  * A new tool named [**Profiles ID Stitcher Audit tool**](<https://www.rudderstack.com/docs/archive/profiles/0.19/additional-resources/profiles-audit/>) is introduced. It is embedded within the core PB CLI tool and helps you analyze the health of your ID graph by giving you a high level aggregate analysis of your ID graph across entities. You can also analyze a single cluster by visualizing all IDs and their connections, along with highlighting the most important IDs that form connections in that group.
  * A key named `carry_forward_privileges` (type Boolean) is added in the `pb_project.yaml` file. This key determines whether the privileges granted on the views should be retained after the view definitions are updated. This resolves the issue where recreating views for each model in the project led to revoked privileges. **Note that using this key can lead to some performance overhead**.
  * A new column named `pb_version` is added to the `material_registry` table in the database which denotes the PB version that created the entry.
  * A new flag `pb show idstitcher-report --seed_clusters_csv` is added which you can use to pass a CSV file with two columns - `id` and `id_type`. The cluster ID can be either `rudder_id` or `other_id`. Each row specifies an ID to be mapped to a cluster main ID, which is then included in the report.


**Improvements**

  * An error is now thrown if a model has a feature without any IDs.
  * User-friendly messages are shown in case a package isn’t installed.
  * Error is now thrown if duplicate feature names are present for a cohort.


**Bug fixes**

  * Resolved the cleanup issue where some materials cleanup failed due to dependencies.
  * Fixed an issue where a non-existent folder inside `model_folders` caused the project to fail.


**Known Issues**

**BigQuery**

  * `pb validate access` command does not work for BigQuery.


**Redshift**

  * If two different users create material objects on the same schema, RudderStack gives an error during cleanup when trying to drop views created by the other user, like `user_var_table`.
  * Cross database references can fail on Redshift for a few clusters.
  * While creating Activations, validation for Redshift does not work correctly in the RudderStack dashboard.


**Other issues**

  * Linux users might see this warning for all command runs - you can ignore it: `WARN[0000]log.go:228 gosnowflake.(*defaultLogger).Warn DBUS_SESSION_BUS_ADDRESS envvar looks to be not set, this can lead to runaway dbus-daemon processes. To avoid this, set envvar DBUS_SESSION_BUS_ADDRESS=$XDG_RUNTIME_DIR/bus (if it exists) or DBUS_SESSION_BUS_ADDRESS=/dev/null`.
  * `pb insert` does not work for Redshift, Databricks, and BigQuery.
  * If you are referring a public package in the project and get `ssh: handshake failed error`, then you’ll have to manually remove the entire folder from `WhtGitCache` to make it work.
  * Timegrains is an experimental feature. There might be some undiscovered issues.


## Version 0.18.5

 _9 January 2025_

**Bug Fixes**

  * Properly sets the Snowflake connection parameter `application` to `Rudderstack_Warehouse`.


## Version 0.18.4

 _25 October 2024_

**Bug Fixes**

  * The schema name has been prepended to the drop statements executed during cleanup. This ensures that deletions are always performed in the correct schema.


## Version 0.18.3

 _16 October 2024_

**Bug Fixes**

  * Fixed a bug that causes cleanup of materials fail due to `current transaction is aborted` error. With the fix, if cleanup of one material fails (for some reason, ex: other objects depend on it), the cleanup of other expired materials should continue.


## Version 0.18.2

 _4 October 2024_

**Bug Fixes**

  * Resolved a migration bug which occurs when there are nested model folders containing non yaml files.
  * Cleanup with flag `--remove_latest_view_ptrs` was not respecting retention time period set in pb_project.yaml. This is fixed.


## Version 0.18.1

 _3 October 2024_

**Bug Fixes**

  * Fixed issue in default ID stitcher for `run_type: discrete`.
  * Resolved a bug that occurs when a project contains multiple entities with same cohort name.
  * During migration, pb was skipping non-YAML files, which caused scheduled runs to fail. This is fixed.


## Version 0.18

 _27 September 2024_  
 _Schema version: 80_

**What’s New**

  * Cohort model now lets you perform filtering using a `filter_expression` followed by AND/OR list of expressions, for example:


    
    
    models:
       - name: high_value_us_residents
         model_type: cohort
         model_spec:
           ...
           filter_expression:
             AND:
               - {{ user.Var('country') }} = 'US'
               - {{ user.Var('salary') }} > 10000
    

  * You can define the `retention_period` for each model of a project. Further, the `pb cleanup materials --expired` command cleans up the materials beyond the defined retention period.
  * Referring other `entity_vars`/`input_vars` is now simplified. You can use `{{entityName.entity_varName}}` instead of the earlier one `{{entityName.Var("entity_varName")}}`. Note that the earlier syntax also works fine.
  * You can use features of an SQL model while using a cohort. To do so, specify the `entity_key` or `entity_cohort` in the `model_spec` of an SQL model.
  * `pb cleanup materials --concurrency` \- A new command which enables concurrency for cleanup, by defining the number of concurrent workers for cleanup. The default value is 1.
  * The default offset value while executing `pb run` command is now updated to 0. It was 30 minutes earlier.
  * A new flag `--end_time_offset` is added to the compile/run commands for adding an offset to the end timestamp, in a human readable format. It means that RudderStack **does not use** any data you load in the warehouse after the offset time has elapsed for that run. For example, `pb run --end_time_offset=45m` ensures that RudderStack does not use any data older than 45 minutes from the run’s start time. Note that you can’t use this new flag with the `seq_no` or `end_time` flags.
  * You can now import Packages starting with SSH URLs, for example, `ssh://git@host:port/path.git`.
  * You can run or import projects hosted on S3 as packages by adding `block_store_creds` in your [site configuration](<https://www.rudderstack.com/docs/archive/profiles/0.19/dev-docs/site-configuration-file/>) file. To run the project, execute `pb run -p s3://<url>` command.
  * Running a project with the `--migrate_on_load` flag now stores generated artifacts in the output subfolder instead of migrations.
  * For an `entity_var`/`input_var`, the `default` key has been renamed to `default_value`.
  * Simplified the project created using `pb init pb-project` by removing the dependency on corelib package , sample SQL model, model contracts and CSV’s in the inputs file.
  * RudderStack now uses `INNER JOIN` instead of `RIGHT JOIN` when calculating `entity_vars`. This results in performance improvement and also prevents some values from getting lost.
  * Feature view model with `main_id` as an identifier is created by default.
  * Schema has been updated from 72 to 80.


**Improvements**

  * By default, RudderStack ignores all the blank values in the ID stitcher model.
  * There is a slight aesthetic improvement in HTML reports generated using `pb show idstitcher-report` command.
  * Relevant errors are now thrown if you specify an unknown YAML key in the model definition.


**Bug Fixes**

  * `validity_time` key has been removed.
  * The `pb validate access` command, for Databricks, now checks only for the necessary permissions and not for ALL the privileges.


**Known Issues**

**BigQuery**

  * `pb validate access` command does not work for BigQuery.


**Redshift**

  * If two different users create material objects on the same schema, RudderStack gives an error during cleanup when trying to drop views created by the other user, like `user_var_table`.
  * Cross database references can fail on Redshift for a few clusters.
  * While creating Activations, validation for Redshift does not work correctly in the RudderStack dashboard.


**Databricks**

  * Concurrency does not work for cleanup.


**Other issues**

  * Linux users might see this warning for all command runs - you can ignore it: `WARN[0000]log.go:228 gosnowflake.(*defaultLogger).Warn DBUS_SESSION_BUS_ADDRESS envvar looks to be not set, this can lead to runaway dbus-daemon processes. To avoid this, set envvar DBUS_SESSION_BUS_ADDRESS=$XDG_RUNTIME_DIR/bus (if it exists) or DBUS_SESSION_BUS_ADDRESS=/dev/null`.
  * `pb insert` does not work for Redshift, Databricks, and BigQuery.
  * If you are referring a public package in the project and get `ssh: handshake failed error`, then you’ll have to manually remove the entire folder from `WhtGitCache` to make it work.
  * Timegrains is an experimental feature. There might be some undiscovered issues.


## Version 0.17.1

 _9 January 2025_

**Bug Fixes**

  * Properly sets the Snowflake connection parameter `application` to `Rudderstack_Warehouse`.


## Version 0.17

 _14 August 2024_  
 _Schema version: 72_

**What’s New**

  * [`pb show plan`](<https://www.rudderstack.com/docs/archive/profiles/0.19/dev-docs/commands/#plan>): A new subcommand is added to show detailed information about the materials with different timegrains along with their dependencies in the order of execution.
  * The casing for the input tables names defined using double quotes is preserved in the warehouse. For example, the table defined as `table: "TableName"` will be referred as `TableName` in the warehouse.
  * Schema has been updated from 71 to 72.


**Improvements**

  * Relevant error message is shown if the computed status for a material is not possible.
  * An error is thrown if multiple feature views are defined with the same name.


**Bug Fixes**

  * Fixed the issue where `input_vars` was not getting defined on the packages.
  * Resolved the bug where the project was failing due to empty or commented YAML files.


**Known Issues**

**BigQuery**

  * `pb validate access` command does not work for BigQuery.


**Redshift**

  * If two different users create material objects on the same schema, RudderStack gives an error during cleanup when trying to drop views created by the other user, like `user_var_table`.
  * Cross database references can fail on Redshift for a few clusters.
  * While creating Activations, validation for Redshift does not work correctly in the RudderStack dashboard.


**Other issues**

  * Linux users might see this warning for all command runs - you can ignore it: `WARN[0000]log.go:228 gosnowflake.(*defaultLogger).Warn DBUS_SESSION_BUS_ADDRESS envvar looks to be not set, this can lead to runaway dbus-daemon processes. To avoid this, set envvar DBUS_SESSION_BUS_ADDRESS=$XDG_RUNTIME_DIR/bus (if it exists) or DBUS_SESSION_BUS_ADDRESS=/dev/null`.
  * `pb insert` does not work for Redshift, Databricks, and BigQuery.
  * If you are referring a public package in the project and get `ssh: handshake failed error`, then you’ll have to manually remove the entire folder from `WhtGitCache` to make it work.
  * The code for `validity_time` is redundant and should be removed.
  * Timegrains is an experimental feature. There might be some undiscovered issues.


## Version 0.16.1

 _6 August 2024_

**Bug Fixes**

  * Fixed the concurrency issue where project run was failing because the same ID stitcher model was served as an input source to two models.
  * Resolved the ambiguous column issue by using an alias for selecting `main_id` in the `entity_var`.


## Version 0.16

 _1 August 2024_  
 _Schema version: 71_

**What’s New**

  * You can now choose between the username-password and key-pair authentication modes while running the `pb init connection` command for Snowflake.
  * Added support to remove materials based on time in hours and milliseconds. For example, to remove materials older than 3 hours, use `pb cleanup materials --retention_time_in_hours 3`. To remove materials older than 100 milliseconds, use `pb cleanup materials --retention_time_in_ms 100`.
  * Schema has been updated from 69 to 71.
  * Edge type `preferred` has been renamed to `coercive`. Here’s a sample code:


    
    
     - name: example
       model_type: sql_template
       model_spec:
         single_sql: |
           select * from {{this.DeRef(test, dependency = "coercive")}}       
    

**Improvements**

  * Changed the casting for timestamp columns for Snowflake, Redshift, and Databricks warehouses to avoid a timestamp with string comparison. `CAST(timestamp_column AS TIMESTAMP) < ‘2024-07-28T23:00:00Z’` has been changed to `CAST(timestamp_column AS TIMESTAMP) < CAST(‘2024-07-28T23:00:00Z’ AS TIMESTAMP)`


**Bug Fixes**

  * Fixed the **Sequence number conflict found** error on BigQuery.
  * Fixed the bug in RudderStack dashboard where entities weren’t showing up, in case no features were defined in the project.
  * Resolved the intermittent **timeout waiting for python client to initialize** error for projects using pynative models.
  * Fixed the **directory not empty** error when Profiles tries to clone a git repository.
  * Fixed the issue where the registry entry for materials was not using the same casing due to which the relations were getting created in the warehouse. Now the cleanup is able to delete materials that were skipped earlier due to case mismatch.
  * Fixed the issue where the same hash was calculated for different cohorts, as the filter pipeline wasn’t being considered.
  * Fixed the issue where some procedures on Snowflake and BigQuery were not getting removed after the run.


**Known Issues**

  * RudderStack does not support accessing input sources in a different project for the BigQuery warehouse.
  * Linux users might see this warning for all command runs - you can ignore it: `WARN[0000]log.go:228 gosnowflake.(*defaultLogger).Warn DBUS_SESSION_BUS_ADDRESS envvar looks to be not set, this can lead to runaway dbus-daemon processes. To avoid this, set envvar DBUS_SESSION_BUS_ADDRESS=$XDG_RUNTIME_DIR/bus (if it exists) or DBUS_SESSION_BUS_ADDRESS=/dev/null`.
  * Redshift: If two different users create material objects on the same schema, RudderStack gives an error during cleanup when trying to drop views created by the other user, like `user_var_table`.
  * `pb validate access` command does not work for BigQuery.
  * `pb insert` does not work for Redshift, Databricks, and BigQuery.
  * Cross database references can fail on Redshift for a few clusters.
  * If you are referring a public package in the project and get `ssh: handshake failed error`, then you’ll have to manually remove the entire folder from _WhtGitCache_ to make it work.
  * The code for `validity_time` is redundant and should be removed.
  * Timegrains is an experimental feature. There might be some undiscovered issues.
  * While creating Activations, validation for Redshift does not work correctly in the RudderStack dashboard.


## Version 0.15

 _10 July 2024_  
 _Schema version: 69_

**What’s New**

  * Support for key-pair authentication in Snowflake for enhanced security.
  * Schema has been updated from 67 to 69.


**Improvements**

  * Replaced `ROW_NUMBER() OVER(ORDER BY 1)` with `ROW_NUMBER() OVER()` for Redshift and BigQuery. This eliminates an unnecessary `ORDER BY` first column.


**Known Issues**

  * When using the CLI: You will have to manually make changes in the [`siteconfig.yaml` file](<>) to add a Snowflake connection with key-pair authentication.
  * RudderStack does not support accessing input sources in a different project for the BigQuery warehouse.
  * Linux users might see this warning for all command runs - you can ignore it: `WARN[0000]log.go:228 gosnowflake.(*defaultLogger).Warn DBUS_SESSION_BUS_ADDRESS envvar looks to be not set, this can lead to runaway dbus-daemon processes. To avoid this, set envvar DBUS_SESSION_BUS_ADDRESS=$XDG_RUNTIME_DIR/bus (if it exists) or DBUS_SESSION_BUS_ADDRESS=/dev/null`.
  * Redshift: If two different users create material objects on the same schema, RudderStack gives an error during cleanup when trying to drop views created by the other user, like `user_var_table`.
  * `pb validate access` command does not work for BigQuery.
  * `pb insert` does not work for Redshift, Databricks, and BigQuery.
  * Cross database references can fail on Redshift for a few clusters.
  * If you are referring a public package in the project and get `ssh: handshake failed error`, then you’ll have to manually remove the entire folder from _WhtGitCache_ to make it work.
  * The code for `validity_time` is redundant and should be removed.
  * Timegrains is an experimental feature. There might be some undiscovered issues.
  * While creating Activations, validation for Redshift does not work correctly in the RudderStack dashboard.


## Version 0.14.2

 _28 June 2024_

**Bug Fixes**

  * Resolved “authentication token has expired” issue on Snowflake.


## Version 0.14.1

 _26 June 2024_

**Bug Fixes**

  * Resolved few migration issues.
  * Fixed BigQuery issues where the project name had special characters.


## Version 0.14

 _19 June 2024_  
 _Schema version: 67_

**What’s New**

  * You can now refer to `entity_vars` defined on cohorts using the `<cohort_name>.Var("<var_name>")` syntax along with the original `entity.Var("v1")` syntax.
  * Vars from ancestor vars are now inherited in derived cohorts. If a derived cohort has vars with the same name as ancestors, they are overridden.
  * You can also specify `timegrains` on a specific `entity_var` and not only on the entire `var_group`.
  * If a column is specified as mandatory in a model contract, it must be present in the warehouse. Otherwise, the project will fail. Also, contract validation is now enabled for SQL models and Python models.
  * `pb show models` command now displays additional information such as the `enable_status` of models, warehouse name, namespace, and timegrains.
  * In materialization status, the flag `not_needed` has been renamed to `only_if_necessary`.
  * Some experimental features are added to optimize performance by partitioning var tables.
  * A new key `row_identifier` _(experimental)_ has been added under `app_defaults` in the `inputs.yaml` file.
  * Schema has been updated from 63 -> 67 in the `pb_project.yaml` file.


**Improvements**

  * Few optimizations in the RudderStack dashboard to make it leaner and faster.


**Bug Fixes**

  * Fixed the issue where features list wasn’t getting added to input models build specification.
  * Resolved a bug where <`entity`>`/feature_views` model wasn’t getting created, in case the `feature_views` key didn’t have any value.
  * Resolved the error where some BigQuery projects were failing with the message `Dataset <> not found in location`.
  * Fixed the symlink issue where the `pb run`/`pb compile` commands were failing when the relative path of the project is passed.
  * Resolved the bug where input models were getting enabled if they did not exist earlier, even if their status wasn’t set.
  * Error is now being thrown in case all the inputs of a model are disabled but they are mandatory.
  * Fixed the error `nil pointer dereference` when `other_id` is not defined in the feature views.
  * Resolved the issue where different cohorts with same feature names were throwing an error.
  * Fixed the bug where a derived cohort was not able to refer other cohort’s vars.
  * Fixed `column name is ambiguous` error in feature views when there are vars with the same name in different timegrains.
  * Resolved the issue where some projects with concurrency were failing with error `concurrent map read and map write`.
  * Fixed the issue with force runs on models with begin time.


**Known Issues**

  * RudderStack does not support accessing input sources in a different project for the BigQuery warehouse.
  * Linux users might see this warning for all command runs - you can ignore it: `WARN[0000]log.go:228 gosnowflake.(*defaultLogger).Warn DBUS_SESSION_BUS_ADDRESS envvar looks to be not set, this can lead to runaway dbus-daemon processes. To avoid this, set envvar DBUS_SESSION_BUS_ADDRESS=$XDG_RUNTIME_DIR/bus (if it exists) or DBUS_SESSION_BUS_ADDRESS=/dev/null`.
  * Redshift: If two different users create material objects on the same schema, RudderStack gives an error during cleanup when trying to drop views created by the other user, like `user_var_table`.
  * `pb validate access` command does not work for BigQuery.
  * `pb insert` does not work for Redshift, Databricks, and BigQuery.
  * Cross database references can fail on Redshift for a few clusters.
  * If you are referring a public package in the project and get `ssh: handshake failed error`, then you’ll have to manually remove the entire folder from _WhtGitCache_ to make it work.
  * The code for `validity_time` is redundant and should be removed.
  * In some cases, you may need to install the `profiles-rudderstack` and `profiles-rudderstack-bin` pip packages separately.
  * You may have to execute the compile command once before executing validate access. Otherwise, you will get a `seq_no` error.
  * Timegrains is an experimental feature. There might be some undiscovered issues.
  * Activations does not work with Redshift warehouse.


## Version 0.13.2

 _11 June 2024_

**Bug Fixes**

  * Fixed issues with auto-migrate on Windows.
  * Resolved insufficient memory error encountered while adding `main_id` to `input_var` tables in Redshift.


## Version 0.13.1

 _23 May 2024_

**Bug Fixes**

  * Resolved the issue with remapped models in entity projects in the RudderStack dashboard.
  * Fixed timestamp casting issues on BigQuery.


**Known Issues**

  * RudderStack does not support accessing input sources in a different project for the BigQuery warehouse.
  * Linux users might see this warning for all command runs - you can ignore it: `WARN[0000]log.go:228 gosnowflake.(*defaultLogger).Warn DBUS_SESSION_BUS_ADDRESS envvar looks to be not set, this can lead to runaway dbus-daemon processes. To avoid this, set envvar DBUS_SESSION_BUS_ADDRESS=$XDG_RUNTIME_DIR/bus (if it exists) or DBUS_SESSION_BUS_ADDRESS=/dev/null`.
  * Redshift: If two different users create material objects on the same schema, RudderStack gives an error during cleanup when trying to drop views created by the other user, like `user_var_table`.
  * `pb validate access` command does not work for BigQuery.
  * `pb insert` does not work for Redshift, Databricks, and BigQuery.
  * Cross database references can fail on Redshift for a few clusters.
  * If you are referring a public package in the project and get `ssh: handshake failed error`, then you’ll have to manually remove the entire folder from _WhtGitCache_ to make it work.
  * The code for `validity_time` is redundant and should be removed.
  * In some cases, you may need to install the `profiles-rudderstack` and `profiles-rudderstack-bin` pip packages separately.
  * You may have to execute the compile command once before executing validate access. Otherwise, you will get a `seq_no` error.
  * Cohort features do not inherit the parent’s features.
  * RudderStack dashboard lists a cohort only if it has features.
  * Timegrains is an experimental feature. There might be some undiscovered issues.
  * Activations does not work with Redshift warehouse.


## Version 0.13

 _16 May 2024_  
 _Schema version: 63_

**What’s New**

  * Timegrains feature _(experimental)_ lets you reuse the output material of a model within the specified time period, preventing unnecessary recalculations⁠. You can define its value as a day, week, month etc. to compute features at the end of that particular period.
  * Cohorts feature _(experimental)_ lets you define core customer segments within an entity based on some characteristics.
  * Removed support for `rebase_incremental` in project_spec. However, you can specify it using the command-line tool.
  * The `output` folder now generates artifacts for `run` and `compile` commands in separate subfolders with the same name.
  * `pb init pb-project` now comes with a sample SQL model.
  * `ReadFile` support introduced in YAML which lets you highlight syntax. In a SQL model, you can use `{{this.ReadFile("models/sql_file.sql")}}` to refer SQL content from a file.
  * Material registry is now at v5. It includes two new columns - `model_ref` and `registry_version`. The registry will be automatically migrated once you execute `pb run` command.


**Improvements**

  * Improved performance in compilation and ID stitching processes, resulting in faster operations.
  * Improved error handling at some places.
  * Few internal refactorings for enhanced working.


**Bug Fixes**

  * Removed `include_untimed` key from the `pb_project.yaml` file as it was redundant.
  * Fixed sporadic lengthening of project runs in RudderStack dashboard.


**Known Issues**

  * Linux users might see this warning for all command runs - you can ignore it: `WARN[0000]log.go:228 gosnowflake.(*defaultLogger).Warn DBUS_SESSION_BUS_ADDRESS envvar looks to be not set, this can lead to runaway dbus-daemon processes. To avoid this, set envvar DBUS_SESSION_BUS_ADDRESS=$XDG_RUNTIME_DIR/bus (if it exists) or DBUS_SESSION_BUS_ADDRESS=/dev/null`.
  * Redshift: If two different users create material objects on the same schema, RudderStack will throw error during cleanup when trying to drop views created by the other user, such as `user_var_table`.
  * `pb validate access` command does not work for BigQuery.
  * Some commands such as `pb insert` does not work for Redshift, Databricks, and BigQuery.
  * For a few clusters, cross database references can fail on Redshift.
  * If you are referring a public package in the project and get `ssh: handshake failed error`, then you’ll have to manually clear  _WhtGitCache_ folder to make it work.
  * The code for `validity_time` is redundant and should be removed.
  * In some cases, you may need to install the `profiles-rudderstack` and `profiles-rudderstack-bin` pip packages separately.
  * You may have to execute the compile command once before executing validate access. Otherwise, you will get a `seq_no` error.
  * Cohort features do not inherit parent’s features.
  * RudderStack dashboard lists a cohort only if it has features.
  * Timegrains is an experimental feature. There might be some undiscovered issues.
  * Activations does not work with Redshift warehouse.


## Version 0.12.1

 _2 May 2024_

**Improvements**

  * If all the inputs of a model are disabled, the model is disabled by default.


**Bug Fixes**

  * Resolved bug where some projects were failing in case nested columns were missing.
  * Updated the migration logic to preserve old view names. The reason being that some existing Activation API projects were failing due to the renaming of `serve_traits` to `feature_views`.


**Known Issues**

  * Linux users might see this warning for all command runs - you can ignore it: `WARN[0000]log.go:228 gosnowflake.(*defaultLogger).Warn DBUS_SESSION_BUS_ADDRESS envvar looks to be not set, this can lead to runaway dbus-daemon processes. To avoid this, set envvar DBUS_SESSION_BUS_ADDRESS=$XDG_RUNTIME_DIR/bus (if it exists) or DBUS_SESSION_BUS_ADDRESS=/dev/null`.
  * Redshift: If two different users create material objects on the same schema, RudderStack will throw error during cleanup when trying to drop views created by the other user, such as `user_var_table`.
  * `pb validate access` command does not work for BigQuery.
  * Some commands such as `pb insert` does not work for Redshift, Databricks, and BigQuery.
  * For a few clusters, cross database references can fail on Redshift.
  * If you are referring a public package in the project and get `ssh: handshake failed error`, then you’ll have to manually clear  _WhtGitCache_ folder to make it work.
  * The code for `validity_time` is redundant and should be removed.
  * In some cases, you may need to install the `profiles-rudderstack` and `profiles-rudderstack-bin` pip packages separately.
  * You may have to execute the compile command once before executing validate access. Otherwise, you will get a `seq_no` error.


## Version 0.12

 _25 April 2024_  
 _Schema version: 61_

**What’s New**

  * Support for external tables on Redshift Serverless.

  * Redshift users can now also connect via SSH Tunnel.

  * Support to specify the version on which you want to run your Profiles project. It is also backported to v0.10.8 and v0.11.5 onwards.

  * Feature views path refs look like below:

    * user/all/feature_view _# By default, the id served is user`main_id`._
    * user/all/feature_view/using_email _# For non default IDs, the path ref has using_ <idname>_
    * user/all/feature_view/salesforce_id_stitched_features _# The names can still be overridden._
  * Ability to add description (optional) to feature tags in the project file.
        
        available_tags:
            - name: demographics
              description: all tags related to user demographics
            - name: billing
        

  * Reorganized the overall flow when defining a Redshift connection. You can specify the region while using Redshift.

  * Creating a new project using `pb init pb-project` now comes with sample data in CSV format, in a folder named `csvs`. These are referenced in the input file.

  * Renamed `Entity Traits 360` model to `Feature Views`. Also, in the `pb_project.yaml` file, a Feature Views model is included by default under the entities definition.

  * Schema has been migrated from 54 -> 61 in the project file.


**Improvements**

  * `pb init connection` now fetches connection name from the site configuration file, and asks you to specify one as well. If you don’t enter any value and there’s only one entry in the file, then it picks that value.
  * Default ID stitcher now uses all package models for ID sources as well, in addition to local ones.
  * Relevant error is now thrown, if ID types for an entity has not been specified in the `pb_project.yaml` file.
  * An entity project in the RudderStack dashboard no longer fails in case a few columns are missing in the source tables.
  * Debugging is improved and the correct line number is displayed.
  * `pb show models` command now includes model dependencies along with some more statistics.
  * Few retoolings from the ground up.


**Bug Fixes**

  * Resolved bug related to failure when a git repo couldn’t be found in the RudderStack dashboard.
  * Resolved bug where default ID stitcher was getting created even if there were no ID edges.
  * Resolved bug where Redshift Profiles projects were failing if names of `entity_var`/`input_var` were longer than 47 characters.
  * Resolved bug where `pb run --rebase_incremental` command was taking edges from previous runs.
  * Resolved the issue where a project wasn’t compiling in case it referenced a package having inputs that weren’t defined in the application with the same name.


## Version 0.11.5

 _16 April 2024_

**Bug Fixes**

  * Fixed issue for Redshift where the driver version wasn’t getting populated correctly.
  * Improved cleanup functionality for Redshift by dropping procedures that were used for creating `entity_vars`.
  * Resolved the issue where migrated project folder’s files weren’t getting deleted.
  * Fixed the bug where `pb run --rebase_incremental` command was taking edges from previous runs.
  * Few internal refactorings while returning data types of columns.


## Version 0.11.3

 _1 April 2024_

**What’s New**

  * An optional parameter `column_data_type` to specify the data type for an `entity_var`/`input_var`.
  * Support for programmatic credentials for Redshift.
  * Schema update in the project yaml file from 53 to 54.


**Improvements**

  * Better error propagation in case of concurrency.
  * Few internal refactorings for improved overall working.


**Bug Fixes**

  * Resolved `relation still open` error when accessing external tables in Redshift.
  * Fixed some bugs when getting the `latest seq_no` for a material in BigQuery.
  * Resolved the issue of conflict in row-ID in case of very large datasets in BigQuery.
  * Begin and end time of all models are now in UTC timezone. This fixes a few inconsistency issues in models.
  * Resolved a concurrency issue which occurred on two different root models with the same name.


## Version 0.11.2

 _15 March 2024_

**What’s New**

  * You can now do parallel processing while running a project using the `--concurrency` flag. Currently, this is supported only for Snowflake warehouse. It is recommended to use this option judiciously as applying a very large value can impact your system resources.
  * RedShift users can now access external tables in their data catalog(s).


**Improvements**

  * Project created using `pb init pb-project` now works for all warehouses.


**Bug Fixes**

  * Fixed issues encountered while running BigQuery projects on Windows.
  * Resolved errors for entity var names in case they match with input column name.
  * Resolved bugs related to inserting `seq_no`.


## Version 0.11.1

 _7 March 2024_

  * Includes bug fixes related to creating vars on ID models and nil model remapping.


## Version 0.11

 _1 March 2024_

**What’s New**

  * RudderStack now supports BigQuery (beta), offering the same seamless experience as on other data warehouses.
  * CSV models _(Experimental)_ : In the inputs specs, RudderStack has added the ability to read data from a CSV file, instead of a Database table/view. You can use files from local storage, or kept on S3. Under `app_defaults`, instead of `table`/`view`, use `csv` (local storage) or `s3` (kept on S3) followed by the path where the CSV file is kept. Note that this feature is experimental, and RudderStack currently supports S3 on Snowflake and Redshift. A sample code is as follows:


    
    
        app_defaults:
          csv: "../common.xtra/Temp_tbl_a.csv"
    …
        app_defaults:
          s3: "s3://s3-wht-input-test-bucket/test/Temp_tbl_d.csv"
    

  * Filter IDs: You can now filter out a vast number of ID’s using SQL. For example, if you wish to exclude all blacklisted ID’s that are listed in an input model named `csv_email_blacklist` and user ID’s from an SQL model named `sql_exclusion_model`, then, you may edit your project file as:


    
    
    id_types:
      - name: email
        filters:
          - type: exclude
            sql:
              select: email
              from: inputs/csv_email_blacklist
      - name: user_id
        filters:
          - type: exclude
            sql:
              select: user_id
              from: models/sql_exclusion_model
    

  * Pre and Post Hooks: A pre hook enables you to execute an SQL, before running a model, for example, if you want to change DB access, create a DB object, etc. Likewise, a post hook enables you to execute an SQL after running a model. The SQL can also be templatized. Here’s an example code snippet:


    
    
    models:
      - name: test_id_stitcher
        model_type: id_stitcher
        hooks:
          pre_run: "CREATE OR REPLACE VIEW {{warehouse.ObjRef('V1')}} AS (SELECT * from {{warehouse.ObjRef('Temp_tbl_a')}});"
          post_run: 'CREATE OR REPLACE VIEW {{warehouse.ObjRef("V2")}} AS (SELECT * from {{warehouse.ObjRef("Temp_tbl_a")}});'
        model_spec:
    

  * `pb show models` \- You can now view in JSON format by passing the flag –json.
  * For Databricks, RudderStack now supports the `pb validate access` command.
  * RudderStack has reverted to having a custom ID stitcher in a new project created using `pb init pb-project`.
  * When creating a new connection in Redshift, you’ll now be asked to input sslmode. You can enter either `disable` (default) or `require`. This will help RudderStack’s tool to work with Redshift DB’s that require SSL mode to be enabled.
  * RudderStack supports triggering tasks by using URL and also read the status back.
  * RudderStack dashboard now supports Git Projects hosted on BitBucket and GitLab.
  * In model specs, a materialization’s `enable_status` is changed to `snake_case`. That is, `enable_status`: `mustHave` -> `enable_status`: `must_have`.
  * Schema version in the project file has been updated from 49 to 53.


**Improvements**

  * Better error messages are shown in case of incorrect/missing/duplicate entity-vars.
  * Error handling has been improved at a few places in Python models.
  * Model path refs are now case insensitive.
  * The command `pb migrate auto` can now handle the case where model folders aren’t present.
  * Specific messages are now shown, in case of errors in the material registry.
  * Due to limitations of Databricks SQL, RudderStack has added restrictions on using catalog `hive_metastore`. So, in case a user on that catalog tries to use RudderStack’s tool, an error is thrown.


**Bug Fixes**

  * Resolved the intermittent issue in Redshift where it throws an error `ptr_to_latest_seqno_cache does not exist`.
  * Bugs in `pb show idstitcher-report`, `pb show user-lookup`, and `pb cleanup materials` commands have been rectified. `pb show idstitcher-report` is still flaky, however, RudderStack team is working on improving it.
  * Fixed bug in packages wherein `entityvars`/`inputvars` weren’t able to refer SQL models.
  * Resolved erroneous queries for validate access command in case of missing privileges.
  * Recsolved the issue where git repo wasn’t getting cloned in case `cache_dir` in siteconfig was written using tilde notation.
  * Fixed some bugs related to `begin_time` of models.
  * Resolved a few issues when cloning Git projects in the web app.
  * Several fixes in gRPC, making it more stable.
  * The remapping: key is removed (if exists) in `models/inputs.yaml` as it was redundant.
  * Resolved some bugs in incremental ID stitcher.


**Known Issues**

  * `pb validate access` command does not work for BigQuery.


## Version 0.10.6

 _19 January 2024_

An internal fix to address issues that arose from a recent update by Snowflake.

## Version 0.10.5

 _9 January 2024_

Some internal fixes to make py-native models more robust.

## Version 0.10.4

 _15 December 2023_

Our latest version has a plethora of features that makes our product more feature-rich and impactful.

**What’s New**

  * **Vars as models** : Earlier, Vars could only be defined inside the feature table under `vars:` section. Now, Vars are defined independent of feature tables. In the model specs file, we have created a new top level key called `var_groups`. We can create multiple groups of vars that can then be used in various models (eg. in feature table). All vars in a var-group need to have the same entity. So if you have 2 entities, you need at least 2 var groups. However, you can create multiple var_groups for every entity. For example, you can create churn_vars, revenue_vars, engagement_vars etc. So that it is easier to navigate and maintain the vars that you need. Each such model shall have name, entity_key and vars (list of objects). This is in line with Profiles design philosophy to see everything as a model.
  * **User defined model types via Python [Experimental feature]** : Ever wondered what it would take to implement a new model type yourself? Custom model types can now be implemented in Python. Check out [this library](<https://github.com/rudderlabs/profiles-pycorelib>) for some officially supported model types with their Python source. Note that this is an experimental feature, so the implementation and interfaces can change significantly in the upcoming versions. To use a python package model in your project, simply specify it as a `python_requirement` in `pb_project.yaml`, similar to requirements.txt. The BuildSpec structure is defined using JSON schema within the Python package. Below code snippet shows how the requirements such as for training and config can be specified in the project:


    
    
        entities:
          - name: user
          python_requirements:
          - profiles_rudderstack_pysql==0.2.0 #registers py_sql_model model type
    
    
    
        models:
          - name: test_py_native_model
            model_type: py_sql_model
            model_spec:
              occurred_at_col: insert_ts
              train_config:
                prop1: "prop1"
                prop2: "prop2"
    

  * **Default ID stitcher** : Until now, when a new project was created using `pb init pb-project`, the file `profiles.yaml` had specifications for creating a custom ID stitcher. That has a few limitations, when edge sources are spanning across packages. Also, we observed that several of our users weren’t doing much changes to the ID stitcher, except for making it `incremental`. As a solution, we have a “default ID stitcher”, that is created by default for all projects. It runs on all the input sources and ID types defined. For quickstart purposes, users needn’t make any changes to the project, to get the ID stitcher working. In case any changes are to be made, then a user can create a custom ID stitcher, as was done in earlier versions.

  * **Default ID types** : Now, common concepts like ID types can be loaded from packages. So we needn’t define them in all new projects. Hence, we have moved the common ID type definitions into a library project called [`profiles-corelib`](<https://github.com/rudderlabs/rudderstack-profiles-corelib>). So when you create a new project, the key `id_types` is not created by default. In case you wish to create a custom list of ID types that is different from the default one, then you may do it as was the case in earlier versions.

  * **Override packages** : Continuing from previous point: packages now have `overrides` materialization spec. In case you wish to add custom ID types to the default list or modify an existing one, then you may extend the package to include your specifications. For the corresponding id_type, add the key `extends:` followed by name of the same/different id_type that you wish to extend, and corresponding `filters` with include/exclude values. Below is an example of the same:


    
    
        packages:
            - name: foo-bar
            url: "https://github.com/rudderlabs/package-555"
        id_types:
            - name: user_id
            extends: user_id
            filters:
                - type: exclude
                  value: 123456
        id_types:
            - name: customer_id
            extends: user_id
            filters:
                - type: include
                  regex: sample
    

  * **entity_var tags** : You can now define a list of tags in the project file under `tags:` key. Then, you can add a tag to each entity_var.
  * **Redshift** : We have added support for the RA3 node type. So now our users on that cluster can cross-reference objects in another database/schema.
  * Schema version in the project file has been updated from 44 -> 49.


**Improvements**

  * Generated ID’s are now more stable. This means that they are unlikely to adapt to merging of ID Clusters, thereby creating a more accurate profile of your users.
  * By default, every entity_var is a feature, unless specified otherwise using `is_feature: false`. So now, you need not explicitly add them to the `features:` list.
  * You can now add escape characters to an entity_var’s description.
  * Several internal refactorings to improve overall working of the application.


**Bug Fixes**

  * An entity_var having a description with special characters was failing during project re-runs. This has now been resolved.
  * We have fixed the bug where two entity_vars across different entities in the same project couldn’t have the same name.
  * Fixed some bugs related to vars as models, auto migration of projects, and ID lookup.


**Known Issues**

  * Redshift: If two different users create material objects on the same schema, then our tool will throw error when trying to drop views created by the other user, such as `user_var_table`.
  * Some commands such as `insert` do not work on Redshift and Databricks.
  * For a few clusters, cross DB references can fail on Redshift.
  * If you are referring a public package in the project and get `ssh: handshake failed` error, then you’ll have to manually clear `WhtGitCache` folder to make it work.
  * The code for `validity_time` is redundant and should be removed.
  * Sometimes you may have sometimes install both the pip packages separately (`profiles-rudderstack` and `profiles-rudderstack-bin`).
  * You may have to execute the `compile` command once, before executing `validate access`. Otherwise, you can get a `seq_no` error.


## Version 0.9.4

 _8 November 2023_

This release includes the following bug fixes and improvements:

  * `pb run --grep_var_dependencies` \- we are now setting default values using the rule “if a project is migrated on load from a version older than 43, then grep_var_dependencies will default to true otherwise false”. Also, handled a null pointer case for non existent vars listed in dependencies.
  * `pb migrate_on_load` / `migrate auto` \- we have made the message clearer on curly braches in dot syntax message.
  * `pb migrate manual` \- we have removed compatibility-mode as it was no longer required.
  * A few internal refactorings.


## Version 0.9.3

 _2 November 2023_

This release addresses a few vulnerability fixes.

## Version 0.9.2

 _26 October 2023_

> ![info](/docs/images/info.svg)
> 
> In case you are unable to install then we recommend having Python3 versions from 3.8 to 3.10.

This release includes a bug fix on self dependency of vars, in case column has same name as entity-var.

## Version 0.9.1

 _19 October 2023_

Our latest release contains some useful features and improvements, as asked by our users.

> ![warning](/docs/images/warning.svg)
> 
> After the auto-migration to v44, you might be shown some warnings to do changes in the YAML. Please check the Tutorials section. Or, you may contact our team and we will assist you with the same.

**What’s New**

  * We have added support for Databricks (beta). Now Databricks users can seamlessly create ID stitcher and feature table models, without writing complex SQL queries! If you’re using Databricks and want to try out Profiles, kindly get in touch with our team.
  * **Vars as models** : Now, entity_vars and input_vars can be treated as independent models. Presently, they are tied to a feature table model. In SQL template text, for example in SQL model templates, please use `{{entity-name.Var(var-name)}}` going forward to refer to an entity-var or an input-var. For example, for entity_var `user_lifespan` in HelloPbProject, change `select: last_seen - first_seen` to `select: '{{user.Var("last_seen")}} - {{user.Var("first_seen")}}'`.
  * `pb show dataflow` and `pb show dependencies` commands - A new flag `--include_disabled` flag is added to let disabled models be part of the generated image. Also, we now show the relative path from local root, instead of the full path.
  * `pb run` command - Added flag `--ignore-model-errors` to let the project continue running in case of an erroneous model. So, the execution wouldn’t stop due to 1 bad model.
  * `pb run` \- Added flag `--grep_var_dependencies` (default: true) which searches for vars dependencies by using `grep` over fields from vars definition.
  * `pb show idstitcher-report` \- Added flag `--seq_no`, using which a specific run for an ID stitcher model can be specified.
  * **Best schema version** \- For a library project, in the `url` key of `packages`, we have introduced the concept of “best version tag”. That is, instead of specifying the specific Git URL of the library project, we give a URL with GIT tag `url: https://github.com/rudderlabs/librs360-shopify-features/tag/schema_{{best_schema_version}}`. Using this will make our tool use the best compatible version of the library project, in case of any schema updates.
  * Schema has been migrated from version 42 -> 44.


**Improvements**

  * The command `pb show user-lookup` now includes more details including the count of rows created and total number of features.
  * Commenting out features will ensure that the corresponding entity-var and any related entity-var/input-var being used only for computation of this commented feature wont run
  * Several improvements done beneath the surface.


**Bug Fixes**

  * The flag `-- force` was having issues in dropping priorly created materialization models. This has now been resolved.
  * Fixed bug where project was unable to run due to giving a custom name to the ID stitcher.
  * Resolved an issue in the command `pb show idstitcher-report`, in the case if the hash of the ID Stitcher model has changed from that of the last run, rerunning the ID Stitcher model.
  * Removed flag `-l` from the command `pb show idstitcher-report` as it was redundant.


**Known Issues**

  * Redshift: If two different users create material objects on the same schema, then our tool will throw error when trying to drop views created by the other user, such as `user_var_table`.
  * Some commands such as `insert` do not work on Redshift and Databricks.
  * For a few clusters, cross DB references can fail on Redshift.


## Version 0.8

 _25 August 2023_

**What’s New**

  * Model Contracts - We have added support for model contracts and their validation. For every input or SQL model, there’s a new key `contract:` which contains the following keys: `is_optional` (boolean, to indicate if the model is optional), `is_event_stream` (boolean, in case the data is event stream and has timestamp), `with_entity_ids` (list of all entities model contains), `with_columns` (list of all column names model have). A contract can be passed along with the model path in `this.DeRef`. For more information, check out [Model Contracts](<>).
  * Inputs model - The keys `occurred_at_col` and `ids` are now a part of `app_defaults`, to reinforce that they can also be overridden.
  * Schema has been migrated from 40 -> 42 in the project file.


**Improvements**

  * The command `pb cleanup materials` now removes tables generated by Python models also.
  * `pb show user-lookup` now includes user traits from Python models as well.
  * A few changes under the hood, for more efficient processing and execution.


**Bug Fixes**

  * Fixed issue in Python models where validity of the train file wasn’t working and it so was retraining the model(s) on every run.
  * Resolved the bug where wrong credentials in siteconfig file was not printing the exact error.
  * Queries for checking warehouse access (grant) were duplicated and therefore recursively checking grants on the same models again and again. This resulted in taking more time than what was required. It has now been fixed.
  * `pb migrate auto` \- There was an issue in migration of multi-line strings of SQL models, that has now been resolved.


## Version 0.7.3

 _14 August 2023_

**What’s New**

  * `pb show idstitcher-report`:`pb show idstitcher-report`: By passing flag `--id_stitcher_model`, you can now create an HTML report with relevant results and graphics including largest cluster, ID graph, etc.
  * Material Registry has been updated to version 4, as additional information is now stored for target (as defined in siteconfig), system username, and invocation metadata (hostname and the project’s invocation folder). So now, if anyone logs into the system and creates material objects using PB, then these details will be stored. This is based on a feature request from one of our customers. Note: make sure to execute `pb validate access` for migrating the registry.
  * `pb discover materials`:`pb discover materials` \- This command now shows a few additional columns - target, username, hostname, invocation folder.
  * Default ID stitcher: In the inputs file, the key `to_default_stitcher` needs to be set to `true` explicitly for an ID to get picked in the default ID stitcher. This field is optional and by default set to false, without impacting if the project is using a custom ID stitcher. In your project file, if you remove the key `id_stitcher: models/<name of ID stitcher model>`, then it’ll use the default ID stitcher and create a material view of the name `<entity_name>_default_id_stitcher`.
  * In the inputs.yaml file, table or view names now appear under a key named `app_defaults:`. This signifies that these are values that input defaults to, when the project is run directly. For library projects, inputs can be remapped and appdefaults overridden. when library projects are imported.
  * Schema has been migrated from 38 -> 40 in the project file.


**Improvements**

  * `pb init pb-project`:`pb init pb-project`: Added keys on default ID stitcher.
  * A few improvements behind the scenes, for enhancing the overall functionality.


**Bug Fixes**

  * Resolved the issue where projects migrated using `migrate_on_load` were referring to the location of the migrated project in the material registry. This was affecting the count of ID’s before and after stitching.
  * Fixed bug where ID stitcher wouldn’t check whether a material was actually existing in the database, before running in incremental mode.
  * When the material registry was on an unsupported common tables version, then the project environment loading would fail, thereby crashing the application. This has now been resolved.
  * Features defined in Python models, now do appear in the list of features.
  * Vars can still be specified in specs of a feature table model. However, the app ignores them. This is a bug and would be fixed in subsequent releases.


## Version 0.7.2

 _24 July 2023_

Our newest release brings enhanced functionality and a more efficient experience.

**What’s New**

  * **Model Enable/Disable** : You can now enable or disable specific models using the `materialization` key in model specifications. Use the `status` key to set values. For more information, refer to [Models enabling themselves](<https://rudderlabs.github.io/pywht/source/120_tutorials.html#models-enabling-themselves>).
  * **Migrate Auto** : When migrating a project, the ordering of elements now remains the same as in the original files, preserving comments.
  * **Graceful Application Exit** : You can now exit the application gracefully while it’s running. For example, if you’re generating material tables using the run command, you can exit using Ctrl+C.
  * **Schema Migration** : The schema version in the project file has been updated from 37 to 38.


**Improvements**

  * Projects created using `init pb-project` now include dependencies.
  * Instead of generating one big SQL file, we now create multiple files in a folder during SQL generation of a feature table model. This reduces the disk space requirements.
  * Internal optimizations have been implemented to improve overall performance and efficiency.


**Bug Fixes**

  * An issue has been fixed where insufficient grants for accessing the warehouse would lead to duplicate suggested queries. Also, in some cases, incorrect queries were displayed, such as when a Redshift user was asked to grant a role.
  * The project URL is now being stored in the material registry, instead of GitHub passkey.
  * Fixed a bug where macros defined in a separate file as global macros were unable to access a common context.
  * Resolved a bug where Python models were not appearing in the dependency graph.


## Version 0.7.1

 _23 June 2023_

Our latest release addresses some critical issues in the previous release. Therefore, if you’re on v0.7, then it’s highly recommended to update to the latest version.

## Version 0.7

 _22 June 2023_

Our newest release is quite significant in terms of new features and improvements offered. Be sure to try it out and share your feedback with us.

**What’s New**

  * `query` \- A new command which displays output of tables/views from the warehouse. So you can view generated material tables from the CLI itself. For example, `pb query "select * from {{this.DeRef("models/user_id_stitcher")}}"`.
  * `show idstitcher-report` \- A new sub command that creates report on an ID stitcher run. Such as, whether it converged, count of Pre-stitched ID’s before run, Post-stitched ID’s after run, etc. Usage: `pb show idstitcher-report` .
  * `show user-lookup` \- A new sub command that allows you to search a user by using any of the traits as ID types. E.g., `pb show user-lookup -v <trait value>`.
  * If non-mandatory inputs required by the model are not present in the warehouse, you can still run the model. Applicable to packages and feature tables.
  * Schema updated from 33 -> 37 in the project file. Please note that the material registry has been migrated to version 3, so you’ll have to execute `pb validate access` once in order to execute the `run` command.


**Improvements**

  * Added an optional field `source_metadata` in the model file inputs.yaml.
  * Added EnableStatus field in materialization so that models can be enabled and disabled automatically based on whether it is required or not.
  * Default ID stitcher now supports incremental mode as well.
  * In macros, you can now specify timestamps in any format.


**Bug Fixes**

  * In case a project is migrated using flag `migrate_on_load`, then src_url in the material registry was pointing to the new folder. Now, that is fixed.
  * Resolved bugs in generating edges for dependency graphs.
  * Tons of several other improvements and bug fixes under the hood.


## Version 0.6

 _26 May 2023_

We are excited to announce the release of PB Version 0.6: packed with new features, improvements, and enhanced user experience.

**What’s New**

  * **Support for begin time and end time** : Our latest release introduces the ability to specify time range for your operations, using two new flags `--begin_time` and `--end_time`. By default, the `--end_time` flag is set to `now`. For example, you can use the command `pb run --begin_time 2023-05-01T12:00:00Z` to fetch all data loaded after 1st May 2023. Note that the flag `--timestamp` is now deprecated.
  * A new flag, `model_refs`, has been introduced which restricts the operation to a specified model. You can specify model references, such as `pb run --model_refs models/user_id_stitcher`.
  * `seq_no` \- Another new flag, using which you can Continue a previous run by specifying its sequence number. Models that already exist would not be rebuilt, unless `--force` is also specified.
  * **Show command** \- `pb show dependencies` has been added to generate a graph showcasing model dependencies. This visual representation will help you understand the relationships between various models in your project.
  * **Show command** \- `pb show dataflow`: Another new command which generates a graph with reversed edges, illustrating the dataflow within your project.
  * **migrate_on_load** \- A new flag, `migrate_on_load`, has been introduced. When executing the command `pb run --migrate_on_load`, by default this flag creates a `migrations` folder inside the project folder that has migrated version of your project to the latest schema version and runs it on the warehouse. This simplifies the process of upgrading your project to the latest schema version, without changing source files.
  * **migrated_folder_path** \- Continuing from previous command, you can use this flag to change folder location of the migrated project.
  * Schema in the project file has been updated to version 33.


**Improvements**

  * SQL Models now provide more relevant and informative error messages instead of generic “not found” errors. This simplifies troubleshooting and debugging processes.
  * Numerous improvements and optimizations have been made behind the scenes, enhancing the overall performance and stability of PB.


## Version 0.5.2

 _5 May 2023_

Our latest release offers significant performance improvements, enhancements, and bug fixes to provide a better experience.

**What’s New:**

  * A new command, `pb show models`, which displays various models and their specifications in the project.
  * Ability to exit the application while the run command is being executed.
  * Project schema version has been migrated to 30.


**Improvements:**

  * Major performance improvements for Redshift. In large data sets, it will reduce the time taken to create ID stitcher table to less than 1/4th of the time taken earlier.
  * `insert` command now picks the connection specified in the current project folder. If not available, it picks “test” in the connection file.
  * Siteconfig is now validated when project is loaded.
  * The `cleanup materials` command now removes SQL models as well.


**Bug Fixes:**

  * Resolved the problem where values with null timestamps were excluded from incremental ID stitcher.
  * The `insert` command was showing a success message even if no tables were inserted in the warehouse. This has been fixed.


## Version 0.5.1

 _11 April 2023_

**What’s New**

  * Updated schema to version 28 in the project file.


**Improvements**

  * Changed project path parameter from `-w` to `-p` for improved usability.


**Bug Fixes**

  * Addressed a few reported bugs for an improved user experience.
  * Implemented performance enhancements to optimize overall system performance.


## Version 0.5

 _28 March 2023_

This release offers significant new additions and improvements, as well as bug fixes.

**What’s New**

  * **Cleanup materials** \- You can now use the command `pb cleanup materials` to delete materials in the warehouse automatically, without the need for manual deletion. Just specify the retention time period in the number of days (default 180) and all tables/views created prior to that date will be deleted.

  * Schema has been migrated to 27. This includes the following changes:

    * **pb_project.yaml** \- The schema version has been updated from 25 → 27. Also, `main_id` is removed from `id_types` as main_id_type is now optional, rudder_id is the main_id_type by default.
    * **models/profiles.yaml** \- To explicitly declare edge source ids, each value in `edge_sources` now requires a `from:` key to be appended. Also, if you didn’t define `main_id` in the project file, then no need to specify here.


**Improvements**

  * In the backend code we’ve enabled registry migration which flattens the registry, enabling incremental ID stitcher to operate on incomplete materials. It also introduces a mechanism for migrating common tables.
  * We have implemented better error handling for cases where an incorrect model name is passed. Any errors related to incorrect model names are now properly identified and handled by the system.
  * Based on feedback from our users, we have renamed default models from `domain_profile<>` to `user_profile<>`.


> ![info](/docs/images/info.svg)
> 
> Due to changes in registry, we will be depricating older versions of PB.

**Bug Fixes**

  * Fixed the bug where some experimental features, such as Discover, were not working for Redshift.
  * Addressed the problem where validation errors were incorrectly being triggered when a connection had multiple targets, one of which was invalid. The system now only generates an error if the warehouse target that is being passed has errors.
  * In addition to previous one, a few more bugs were fixed that were related to validation.
  * Errors were coming for users who had initialized the GIT repository but had not added the remote origin. This issue has now been fixed.


**Known Issues**

  * Warning: While the run command is being executed, canceling it by pressing Ctrl+C doesn’t work as expected. Though it will stop the program’s execution on the CLI, the query will keep running on the data warehouse. This is a documented Snowflake behavior.
  * In a model, an input can’t use columns named “MAIN_ID”, “OTHER_ID”, “OTHER_ID_TYPE”, or “VALID_AT” in its ID SQL.
  * When creating a connection via `init` command, pressing the Ctrl+C command doesn’t exit the application.
  * `migrate auto` jumbles up the order and removes comments.
  * On Redshift, validate access passes all tests, but `run` command sometimes fail giving error “permission denied for language plpythonu”.
  * Some commands such as `insert` do not work on Redshift.
  * For a few clusters, cross DB references can fail on Redshift.
  * The command `migrate auto` migrates siteconfig in your home directory but not any local one.
  * While working with same type of data in Snowflake and Redshift you might encounter errors where it works on Snowflake but not on Redshift. This is due to the fact that implicit casting of different data types for different function or operator might not be supported on one data warehouse while supported on other.


## Version 0.4

 _2 March 2023_

We are proud to announce the latest version of PB 0.4, which includes several new features and improvements.

**What’s New**

  * **Redshift** \- We are excited to share that we now offer Redshift integration. With YAML, you can now effortlessly create ID stitched and feature table models on your Redshift warehouse, without any difficulty.

  * **Incremental ID stitching** : You can now stitch together data from multiple sources in incremental mode. When new data is added to your source tables, only that data will be fetched, without needing to reload the whole table each time! This shall result in significant performance improvements from earlier versions, especially if the delta of new data is much smaller compared to what’s already been stitched.

  * **Insert** : A new command, allowing users to add sample data to their warehouse, without having to manually add them.

  * Schema has been migrated to 25. This includes the following changes:

    * **models/profiles.yaml** \- Renamed entityvar to `entity_var` and inputvar to `input_var`
    * **pb_project.yaml** \- Renamed profile to `connection`.
    * **siteconfig.yaml** \- Renamed profiles to `connections`.


Be sure to use the `migrate auto` command to upgrade your project and the connections file.

**Improvements**

  * The command `init profile` has been renamed to `init connection`.
  * Lots of modifications under the hood.


**Bug Fixes**

Resolved issue on default values in an entity var, ensuring that the values are properly set.

**Known Issues**

  * Warning: While the run command is being executed, canceling it by pressing Ctrl+C doesn’t work as expected. Though it will stop the program’s execution on the CLI, the query will keep running on the data warehouse. This is a documented Snowflake behavior.
  * In a model, an input can’t use columns named “MAIN_ID”, “OTHER_ID”, “OTHER_ID_TYPE”, or “VALID_AT” in its ID SQL.
  * When creating a connection via `init` command, pressing the Ctrl+C command doesn’t exit the application.
  * `migrate auto` jumbles up the order and removes comments.
  * On Redshift, some experimental commands such as discover do not work.
  * The command `migrate auto` migrates siteconfig in your home directory but not any local one.
  * While working with same type of data in Snowflake and Redshift you might encounter errors where it works on Snowflake but not on Redshift. This is due to the fact that implicit casting of different data types for different function or operator might not be supported on one data warehouse while supported on other.


## Version 0.3.1

 _3 February 2023_

This version addresses a crucial defect, so please make sure to update your version. Note that you won’t have to update your schema for this release.

## Version 0.3

 _25 January 2023_

We have got a new name! WHT is now called Profile Builder (PB), RS360 is now Profiles. Be sure to check out our newest release that comes with several new features for an enhanced user experience.

**What’s New**

  * **Migrate** \- A new command that will enable you to migrate your project to a newer schema. It has two subcommands:

    * **Manual** \- You will get to know steps you need to follow to manually migrate the project yourself. It will include both breaking and non-breaking changes.
    * **Auto** \- Automatically migrate from one version to another.
  * We have made a few significant changes to YAML. The changes consist of:

    * Bumping schema version from 9 → 18.
    * Entityvar (Feature Table) - We have renamed tablevar, tablefeature and feature to entityvar; as they all were adding columns to an entity with nearly identical YAML. A new `vars:` section of feature table YAML contains list of inputvars and entityvars. Whereas `features:` field same YAML is a list of entityvar names which should be part of the final output table.
    * ID Stitcher is now linked to an entity. As a result, all tables using that entity will use the linked ID Stitcher. Earlier, an ID stitcher was linked to a feature model.
    * Some of the terms in yaml spec are changed to make it closer to SQL terminologies. For entityvar and inputvar spec: value → select, filter → where , ref → from. In inputs spec: sql → select.
    * Project file has a new key named `include_untimed`. If set to `true`, data without timestamps are included when running models. This reduces data errors for timestamp materials. Also, we have deprecated the flag `require-time-clean` in the `run` command.
    * Id types can now be re-used between entities. In the project file, entities now have a list of id types names, instead of a list of definitions. In the inputs file, a required entity field is added to the ID list that specifies which entity this ID type is being extracted for.
    * Now an inputvar can also read from a macro, just like tablevar.
    * Global Macros - You can now define macros in a separate YAML file inside your models folder. They can then be used across different models in your project. Thus a macro becomes independent that can be reused across multiple models.
    * wht_project.yaml is renamed to pb_project.yaml and ml-features.yaml to profiles.yaml.
  * **Cleanup Materials** \- A new command that allows you to review all the created materials and then delete them (NOTE: experimental feature).

  * **Discover** \- A new subcommand `discover materials` has been added. Using it, you can now discover all the materials associated with a project.

  * **Compile/Run** \- GIT URL now supports tags. To use, execute the command `pb compile -w git@github.com:<orgname>/<repo>/tag/<tag_version>/<folderpath>`.


**Improvements**

  * **Web app** \- The UI is now more intuitive and user-friendly.
  * Log tracing is now enabled by default for most commands. Log files are stored in logs/logfile.log of your current working directory. They store upto 10 MB data. Also, the logger file now stores more granular information for easier debugging in case of unexpected errors.
  * Significant performance improvements in creating ID stitched tables, in case a lot of duplicates are present.
  * Add extra columns (Hash, SeqNos) to differentiate between entries for commands to discover sources and entities.
  * When you execute a profile via run command, then the generated SQL gets saved in the output folder.
  * Added .gitignore file to init project command, to prevent unnecessary files being added to GIT Repo. Such as, .DS_Store, output and logs folders.
  * Tonnes of changes under the hood.


**Bug Fixes**

  * Fixed the bug where window functions were creating multiple rows (duplicates) per main id.
  * Resolved the bug in inputvars which was doing joins on main_id instead of row id.
  * Executing the command init profile now inputs values in the same order as on the web app.
  * Resolved the bug where extra gitcreds[] and warehouse lines were added on overwriting a profile that already existed.
  * A few redundant parameters were being shown in the validate access command which have been removed.
  * Removed a couple of redundant subcommands in the init project.


**Known Issues:**

  * Warning: While the run command is being executed, canceling it by pressing Ctrl+C doesn’t work as expected. Though it will stop the program’s execution on the CLI, the query will keep running on the data warehouse. This is a documented Snowflake behavior.
  * In a model, an input can’t use columns named “MAIN_ID”, “OTHER_ID”, “OTHER_ID_TYPE”, or “VALID_AT” in its ID SQL.
  * When creating a profile via `init` command, pressing the Ctrl+C command doesn’t exit the application.
  * Web app doesn’t allow you to select a date older than 30 days.
  * Migrate auto jumbles up the order and removes comments.


## Version 0.2.2

 _12 November 2022_

Our November release is significant as it has several fixes and improvements for an enhanced experience. Check it out and be sure to let us know your feedback.

**What’s New**

  * **ID Stitcher / Feature Table** \- You can now define a view as source, in addition to table, in the inputs file. This is particularly of use when you need to support an sql query that’s complex or out of scope for PB. To use it, in your inputs file define the edge_source as `view: <view_name>` instead of `table: <table_name>`.
  * **Inputvars** \- A new identifier which adds temporary helper columns to an input table, for use in calculating a featuretable.
  * **Window Functions** \- In your model file, you can now add window function support to features, tablevars, tablefeatures and inputvars. Also, you can add filters to features.


**Improvements**

  * Schema version 9 makes it more streamlined to define the model. We welcome your feedback for further improvements on this.
  * Compile command now show errors if the input SQL is buggy.
  * Discover - subcommands `entities` and `features` now show a few more fields.
  * Discover - Export to CSV works for subcommands and also generates files in the output folder.
  * Init pb-project - Based on feedback, it now generates a README file and also has simpler YAML files with comments. It should now be easier for our users to create a model and get it running.
  * Several internal refactorings on how the application works.
  * Web app - Massive improvements under the hood related to UI elements, preserving state when entering data, showing correct data and validations, and displaying run time in user’s local time zone.


**Bug Fixes**

  * Fixed the issue where every time `pb run` was executed for a feature table, it was adding a new row to the output of `pb discover features`.
  * Resolved the bug where error wasn’t shown if an unknown flag was used.
  * There was an issue generating material tables on a new schema, which has now been resolved.
  * Bug fix on generating empty SQL files from input models.
  * Fixed bug where model names with _ in the name would sometimes fail to update the latest view pointer correctly.
  * Web app - Artifacts list now shows different folders for different runs to isolate them.
  * Web app - When the PB project is running, the screen now shows correct start timestamp.
  * Web app - Date filters to find PB runs are now working.
  * Web app - Scheduling UI is now fully responsive about when the run will take place.
  * Web app - Resolved the issue where a project would run only once and was then showing error.


**Known Issues:**

  * Warning: While the run command is being executed, canceling it by pressing Ctrl+C doesn’t work as expected. Though it will stop the program’s execution on the CLI, the query will keep running on the data warehouse. This is a documented Snowflake behavior.
  * In a model, an input can’t use columns named “MAIN_ID”, “OTHER_ID”, “OTHER_ID_TYPE”, or “VALID_AT” in its ID SQL.
  * When creating a profile via `init` command, pressing the Ctrl+C command doesn’t exit the application.
  * Logger file generation is disabled at the moment.
  * Some no-op parameters are shown upon passing the help flag(-h) to `validate access` command.


## Version 0.2

 _5 October 2022_

The September release is our largest update yet. We have added a lot of quality of life improvements and net new features to the PB product line. We plan on releasing even more features in our mid-October release to further improve the usability of the product as well as add additional features that will further help form the core of the product. A substantial amount of the features in this release were based directly off feedback from the first beta testing with external users and internal stakeholders. Please feel free to walk through our newest release. We welcome and encourage all constructive feedback on the product.

**What’s New**

  * **Feature Table** \- After encouraging feedback from beta testing of the ID Stitcher, we are feeling more confident about sharing our C360 feature table functionality with beta customers. During testing of this release, we benchmarked ourselves against the feature set that our E-Commerce ML models expect. Many features were implemented successfully. Some needed functionality which could not be pushed through QA gates in this September release. Nevertheless, the feature table YAML is now ready for internal customers to explore.
  * **Web App** \- We are now ready to share the scheduling functionality within the web app. This will allow the user to schedule, and automatically run PB models from the Rudder backplane. Any artifacts and log files created during the execution of PB projects are also available for the user to explore. This critical functionality will enable users to debug their cloud PB runs.
  * **Validate** \- A new command, `pb validate` allows users to run various tests on the project related configurations and validate the privileges associated with the role used for running the project. For example, the subcommand `pb validate access` does an exhaustive test of required privileges before accessing the warehouse.
  * **Version** \- This is another new command that provides information on the current version of the app.
  * **Logger** \- When you execute the compile and run commands, all errors and success messages that were previously only displayed on screen, are now also logged in a file inside the project output folder.
  * **Discover** \- You can now export the output of the discover command in a CSV file. The ability to discover across all schemas in one’s warehouse is also added.


**Improvements**

  * We have made many changes to the way ID Stitcher config is written. We are forming a more complete opinion on the semantic model representation for customer’s data. Entities, IDs, and ID types are now defined in the PB project file. The model file syntax is also more organized and easier to write. To see examples of the new syntax check out the section on [Identity Stitching](<https://www.rudderstack.com/docs/archive/profiles/0.19/dev-docs/profiles-yaml/id-stitcher/>) or sample files by executing command `pb init pb-project`. The sample project file also contains include and exclude filters, to illustrate their usage.
  * In PB command invocation, whenever a file is written, its location is now shown on the console and in log files.
  * Many enhancements on how errors are handled inside the application.
  * Massive improvements under the hood.


**Bug Fixes**

  * Fixed the issue in ID stitching where it was not picking up singleton components (i.e. the ones with only 1 edge), due to which they were getting skipped in the final output table.
  * In the `init` command, not entering any value for target wasn’t setting it to default value as “dev”.
  * Pressing Ctrl+C wasn’t exiting the application.
  * The command `init profile` now appends to an existing profile, instead of overwriting it.
  * Fixed the issue in `discover` command where the material table name was being displayed instead of the model name.


**Known Issues:**

  * Warning: While the run command is being executed, canceling it by pressing Ctrl+C doesn’t work as expected. Though it will stop the program’s execution on the CLI, the query will keep running on the data warehouse. This is a documented Snowflake behavior.
  * In a model, an input can’t use columns named “MAIN_ID”, “OTHER_ID”, “OTHER_ID_TYPE”, or “VALID_AT” in its ID SQL.
  * The web app is not showing a description and last run on the landing page.
  * In the web app, date filters to find PB runs aren’t working.
  * In the web app, when the PB project is running, the screen shows an incorrect start timestamp.
  * Artifacts list changes when a project is running versus when it completes execution. Since all runs on the same Kubernetes pod share the same project folder, we are creating artifacts of different runs under the same parent folder. So, the same folder is currently shown for different runs of the project. In the next release, we will configure different folders for different runs to isolate them.
  * In case of feature table models, the compile command doesn’t always show error if the input SQL is buggy. Thise error may still be found when the model is run.
  * When creating a profile via `init` command, pressing the Ctrl+C command doesn’t exit the application.
  * Creating a PB Project doesn’t currently include a sample independent ID stitcher. Instead, it is a child model to the generated feature table model.
  * We are working toward better readability of the logger file. We welcome any feedback here.
  * The command `pb discover features` needs to show a few more fields.
  * Every time `pb run` is executed for a feature table, it adds a new row to the output of pb discover features. Only one row should appear for each feature.
  * Export to CSV for the discover command should work for subcommands and also generate files in an output folder.
  * Some no-op parameters are shown upon passing the help flag(-h) to `validate access` command.
  * In some cases, error isn’t shown if an unknown flag is used.
  * Scheduling UI isn’t sometimes fully responsive about when the run will take place.


> ![info](/docs/images/info.svg)
> 
> The documentation for September release does not completely match with the current release. We are currently working on updating the documentation and will have new versions out soon. Please contact the Data Apps team if you are confused by some deviation.

## Version 0.1

 _18 August 2022_

We are now in beta! Please do try out PB and share your feedback with us, so that we can make it better.

**What’s New**

  * **ID Stitcher** \- ID Stitching solves the problem of tying different identities together, for the same user across different sessions/devices. With v0.1, we launch PB ID Stitching. It provides an easy to use and powerful interface to specify Id Stitching inputs.
  * **Command Line Interface** \- Our CLI tool works on Linux, Windows and Mac machines. Using it you can setup a profile having connection to your Database, make a PB project, create SQL from models, run ID stitcher models directly on the Warehouse, and discover all the created models/entities/sources on DW.


**Improvements**

  * We have enhanced the speed of Discover and Compile commands, from minutes to a few seconds.
  * The description of a few commands in Help has been improved.


**Bug Fixes**

  * The command for discovering entities wasn’t working, which has now been resolved.
  * Fixed the bug on init profile command where siteconfig wasn’t getting created on first-time installations.
  * A few bugs resolved related to output of discover command.


**Known Issues:**

  * Warning: While the run command is being executed, please do not cancel it by pressing Ctrl+C. Though it will stop the program’s execution on CLI, the query will keep running on the data warehouse. This is a documented Snowflake behaviour.
  * Null ID’s in ID stitcher. If first listed Id is null, the entire row may be ignored. That means, results are silently incorrect.
  * If first listed ID is null, the entire row may be ignored. The first listed ID is assumed to be the key ID. If it is ever null the results may be incorrect.


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.19/additional-resources/faq/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.19/changelog/profiles-0.19-changelog/>)