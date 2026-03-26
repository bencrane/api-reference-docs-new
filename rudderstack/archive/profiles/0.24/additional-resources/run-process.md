# Profiles Run Process

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Profiles Run Process

Learn about the steps RudderStack performs when you run a Profiles project.

* * *

  * __2 minute read

  * 


This guide explains the run process of your Profiles project in detail along with the order of execution of all of its components.

## Project assumptions

This guide assumes you have a Profiles project with the following specifications:

  * A `user` entity
  * ID stitcher model
  * `entity_vars`
  * A feature table model
  * Two Feature views models (default, and using `email` as the primary key)
  * Custom SQL model to create `entity_vars`
  * Cohort representing high value users


## Run process

When you exceute the `pb run` command to run your Profiles project, RudderStack performs these steps:

  1. Constructs a DAG to analyze the order in which each component should run based on the model dependencies.

  2. Compiles the configuration specified in your project files and outputs the SQL files (that will run in your database) in the output directory of your project.

  3. Creates an input var table for each input table/source and adds an input row ID to it. This is used to create the `entity_vars`.

  4. Performs the ID stitching process.

  5. Creates the `ALL` cohort which is a table of distinct list of all the `main_ids` created from the most recent ID stitcher run. It serves as the base for the entity var table as well as custom cohorts.

  6. Uses `main_ids` created in the previous step and appends them to the input var tables (created in step 3).

  7. Creates entity var tables which serve as the base for any feature table/views models built around this entity. The default output is a single column containing `main_ids` from the ID graph.

  8. Creates features for actionable views by calculating `entity_vars` and `input_vars`.

  9. Joins calculated features (via `entity_vars`) to the entity var table.

  10. Creates and materializes the custom cohort list (if defined in the YAML).

  11. Creates the custom cohort var table (similar to the entity var table) which serves as the target table for feature creation and the base table for any feature table/views created on top of custom cohorts.

  12. Generates the final tables and views:

     * Feature table model and default feature view using the entity var table
     * Custom feature views using the default feature views
     * Custom cohort views using the cohort var table


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.24/additional-resources/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.24/additional-resources/multi-version/>)