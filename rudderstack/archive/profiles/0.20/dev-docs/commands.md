# Commands

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Commands

Learn about the Profiles commands and how to use them.

* * *

  * __13 minute read

  * 


The Profile Builder tool supports specific commands, making executing the usual operations easier. The basic syntax of executing a command is:
    
    
    $ pb <command> <subcommand> [parameters]
    

## Supported commands

You can use the following Profile Builder commands:

### audit

Analyze your ID graphs, for example, count of IDs before and after stitching, distribution of ID counts, etc.

This command also lets you analyze a single cluster by understanding how different IDs get connected to one, by visualizing all IDs and their connections and highlighting the most important IDs that form connections in that group.

See the [Profiles ID Stitcher Audit tool](<https://www.rudderstack.com/docs/archive/profiles/0.20/dev-docs/profiles-audit/>) guide for more information.
    
    
    pb audit id_stitcher
    

> ![info](/docs/images/info.svg)
> 
> To use this command, make sure to:
> 
>   * Run the project successfully at least once so that it produces an ID graph.
>   * Install the package `profiles-mlcorelib` (v0.6.0 or above) in your Python environment (v3.9.0 to v3.11.10) using `pip install profiles-mlcorelib`. Note that it should be the same Python environment as the `profiles-rudderstack` library.
> 


### cleanup

Displays and removes materials, older than the retention time period specified by the user (default value is 180 days).
    
    
    pb cleanup materials -r <number of days>
    

**Optional Parameter**

Parameter| Description  
---|---  
`-r`| Retention time in number of days.  
  
**Example** : If you pass 1, then all the materials created prior to one day (24 hours) are listed. This is followed by prompts asking you for confirmation, after which you can view the material names and delete them.  
`--retention_time_in_hours`| Retention time in hours.  
  
**Example** : To remove materials older than 3 hours, use `pb cleanup materials --retention_time_in_hours 3`. This is followed by prompts asking you for confirmation, after which you can view the material names and delete them.  
`--retention_time_in_ms`| Retention time in milliseconds.  
  
**Example** : To remove materials older than 100 milliseconds, use `pb cleanup materials --retention_time_in_ms 100`. This is followed by prompts asking you for confirmation, after which you can view the material names and delete them.  
`--concurrency`| Enables concurrency by defining the number of concurrent workers for clean up. The default value is 1.  
  
**Note** : This flag is currently supported for Snowflake only.  
  
### compile

Generates SQL queries from models.
    
    
    pb compile
    

It creates SQL queries from the `models/profiles.yaml` file, storing the generated results in the **Output** subfolder in the project’s folder. With each run, a new folder is created inside it. You can manually execute these SQL files on the warehouse.

**Optional parameters**

Parameter| Description  
---|---  
`clean_output`| Empties the output folder(s) before executing the command.  
`-c`| Uses a site configuration file other than the one in `.pb` directory.  
  
**Example** : `$ pb compile -c MyOtherConnection/siteconfig.yaml`  
`-t`| Defines target name (mentioned in `siteconfig.yaml`) or timestamp in building the model.  
  
**Example** : If your `siteconfig.yaml` has two targets, `dev` and `test`, and you want to use the `test` instance: `$ pb compile -t test`  
`--begin_time`| Timestamp to be used as a start time in building model.  
`--end_time`| Timestamp to be used as an end time in building model.  
`--migrate_on_load`| Whether to automatically migrate the project and packages to the latest version. Defaults to false.  
`--migrated_folder_path`| Folder location of the migrated project. Defaults to sub-directory of the project folder.  
`-p`| 

  * Uses a project file (`pb_project.yaml`) other than the one in current directory.  
**Example** : `$ pb compile -p MyOtherProject`.
  

  * Fetches project from a URL such as GitHub.  
**Example 1** :`$ pb compile -p git@github.com:<orgname>/<repo>`. You can also fetch a specific tag, like `$ pb compile -p git@github.com:<orgname>/<repo>/tag/<tag_version>/<folderpath>`
  

  * Compiles project hosted on S3.  
**Example** : `pb compile -p s3://<url>`

  
`--rebase_incremental`| Rebases any incremental models (build afresh from their inputs) instead of starting from a previous run. You can do this every once in a while to address the stale data or migration/cleanup of an input table.  
`--assume_all_inputs_exist`| Does not throw error if the specified table/column is absent in the warehouse. It is helpful in debugging issues when you want to compile the materials even if any table or column is absent.  
`--end_time_offset`| Adds an offset to the end timestamp in a human readable format. It means that RudderStack **does not use** any data you load in the warehouse after the offset time has elapsed for that run. For example, `pb run --end_time_offset=45m` ensures that RudderStack does not use any data older than 45 minutes from the run’s start time.  
  
Note that you can’t use this new flag with the `seq_no` or `end_time` flags.  
  
### discover

Discovers elements in the warehouse, such as models, entities, features and sources.
    
    
    pb discover
    

It allows you to discover all the registered elements in the warehouse.

#### Subcommands

Discover all the `models`, `entities`, `features`, `sources`, and `materials` in the warehouse.
    
    
    $ pb discover models
    $ pb discover entities
    $ pb discover features
    $ pb discover sources
    $ pb discover materials
    

**Optional parameters**

Parameter| Description  
---|---  
`-e`| Discovers specific entities with their name.  
  
**Example** : `$ pb discover -e 'Name'`  
`-m`| Discovers a specific model.  
  
**Example** : `$ pb discover -m 'MY_DATABASE.PROD_SCHEMA.CREATED_MODEL'`  
`-c`| Uses a site config other than the default one.  
  
**Example** : `$ pb discover -c siteconfig.yaml`  
`-s`| Discovers entities in a specified schema.  
`-s "*"`| Discovers entities across all schemas (case-sensitive).  
`-u`| Discovers entities having the specified source URL’s.  
  
**Example** : To discover all the entities coming from GitHub: `$ pb discover -u %github%`  
`-t`| Selects target (mentioned in `siteconfig.yaml`).  
`-p`| Uses project folder other than the one in current directory.  
  
**Example** : `$ pb discover -p ThisFolder/ThatSubFolder/SomeOtherProject/`  
`-f`| Specifies a file path to dump the discovery output into a csv file.  
  
**Example** : `$ pb discover -f path/to/csv_file.csv`  
`-k`| Restricts discovery of the specified model keys.  
  
**Example** : `$ pb discover -k entity_key:mode_type:model_name`  
`--csv_file`| Specify this flag with a file path to dump the discovery output into a csv file.  
  
**Examples**
    
    
     # Discover all the models
    $ pb discover models
    
    # Discover a model with specific name
    $ pb discover -m 'RUDDER_WEB_EVENTS.PROD_SCHEMA.feature_profile'
    
    # Discover all features having 'max' in their name
    $ pb discover features -u %max%
    
    # Discover all the entities for a specific profile
    $ pb discover entities -c siteconfig.yaml
    
    # Discover all materials for target dev
    $ pb discover materials -t dev
    
    # Export output of discover command to a CSV file in output folder
    $ pb discover -f my-custom-name.csv
    
    # Export all sources to a CSV file in output folder
    $ pb discover sources -f my-custom-name.csv
    

### help

Provides list information for any command.
    
    
    $ pb help
    

#### Subcommand
    
    
    $ pb help <command_name>
    

Get usage information for a specific command, with subcommands, and optional parameters.

### init

Creates connection and initializes projects.
    
    
    pb init
    

#### Subcommands
    
    
    pb init connection
    

Inputs values for a warehouse connection and then stores it in the `siteconfig.yaml` file.
    
    
    pb init pb-project
    

Generates files in a folder named **HelloPbProject** with sample data. You can change it as per project information, models, etc.

**Optional parameters**

Parameter| Description  
---|---  
`pb-project -o`| Creates a Profile Builder project with a different name by specifying it as an additional parameter.  
  
**Example** : To create a Profile Builder project with the name **SomeOtherProject** : `$ pb init pb-project -o SomeOtherProject`  
`connection -c`| Creates `siteconfig.yaml` at a location other than `.pb` inside home directory.  
  
**Example** : To create `myconfig.yaml` in the current folder: `$ pb init connection -c myconfig.yaml`.  
  
### insert

Allows you to store the test dataset in your (Snowflake) warehouse . It creates the tables `sample_rs_demo_identifies` and `sample_rs_demo_tracks` in your warehouse schema specified in the `test` connection.
    
    
    # Select the first connection named test having target and output as dev, of type Snowflake.
    $ pb insert
    # By default it'll pick up connection named test. To use connection named red:
    $ pb insert -n red
    # To pick up connection named red, with target test .
    $ pb insert -n red -t test
    

> ![warning](/docs/images/warning.svg)
> 
> This command is supported only for Snowflake currently.

### migrate

Migrate your project to the latest schema.

#### Subcommands
    
    
    pb migrate manual
    

Based on the current schema version of your project, enlists all the steps needed to migrate it to the latest one.
    
    
    pb migrate auto 
    

Automatically migrate from one version to another. To migrate your models, navigate to the folder where your project files are stored and execute one of the following:

  * `pb migrate auto --inplace`: Replaces contents of existing folder with the migrated folder.
  * `pb migrate auto -d <MigratedFolder>`: Keeps the original project intact and stores the migrated project in another folder.


**Optional parameters**

Parameter| Description  
---|---  
`-c`| Uses a `siteconfig.yaml` file other than the one in your home directory.  
`-t`| Target name (defaults to the one specified in `siteconfig.yaml` file).  
`-v`| Version to which the project needs to be migrated (defaults to the latest version).  
`-d`| Destination folder to store the migrated project files.  
  
**Example** : `pb migrate auto -d FolderName`  
`--force`| Ignores warnings (if any) and migrates the project.  
`--inplace`| Overwrites the source folder and stores migrated project files in place of original.  
  
**Example** : `pb migrate auto --inplace`  
`-p`| Uses a project folder other than the one in current directory.  
  
**Example** : `$ pb migrate auto -p ThisFolder/ThatSubFolder/SomeOtherProject/`  
  
### run

Creates identity stitcher or feature view model in the warehouse.
    
    
    pb run
    

It generates the SQL files from models and executes them in the warehouse. Once executed, you can see the output table names, which are accessible from the warehouse.

**Optional parameters**

The `run` command supports:

  * All the parameters of `compile` command except `--assume_all_inputs_exist`,
  * And the following ones:

Parameter| Description  
---|---  
`--force`| Does a force run even if the material already exists.  
`--write_output_csv`| Writes all the generated tables to CSV files in the specified directory.  
  
**Example** : `$ pb run --write_output_csv WriteOutputHere.csv`  
`--model_args`| Customizes behavior of an individual model by passing configuration params to it.  
  
The only argument type supported currently is `breakpoint` for feature table models.  
  
The `breakpoint` parameter lets you generate and run SQL only till a specific feature/tablevar. You can specify it in the format `modelName:argType:argName` where argName is the name of feature/tablevar.  
  
**Example** : `$ pb run --model_args domain_profile:breakpoint:salesforceEvents`  
`--model_refs`| Restricts the operation to a specified model. You can specify model references like `pb run --model_refs models/<model-name> --seq_no latest`  
`--seq_no`| Sequence number for the run, for example, 0, 1, 2,…, latest/new. The default value is `new`. You can check run logs or use discover commands to know about existing sequence numbers.  
`--ignore_model_errors`| Allows the project to continue to run in case of an erroneous model. The execution will not stop due to one bad model.  
`--grep_var_dependencies`| Uses regex pattern matching over fields from vars to find references to other vars and set dependencies. By default, it is set to `true`.  
`--concurrency`| (_Experimental_) Lets you run the models concurrently in a warehouse (wherever possible) based on the dependency graph. In CLI, you can specify the concurrency level for running models in a project via `pb run --concurrency <int>` (default int value is 1).  
  
**Note** : This flag is currently supported for Snowflake only and the concurrency limit is `20`. To increase the limit, see the [Snowflake documentation](<https://community.snowflake.com/s/question/0D50Z00008VjQDkSAN/how-to-handle-thenumberofwaitersexceedsthe20statementslimit-error>).  
`--begin_time`| Timestamp to be used as a start time in building model.  
`--end_time`| Timestamp to be used as an end time in building model.  
`--migrate_on_load`| Whether to automatically migrate the project and packages to the latest version. Defaults to false.  
`--migrated_folder_path`| Folder location of the migrated project. Defaults to sub-directory of the project folder.  
`--disable_registry_cache`| Disables the feature where the registry is cached by default while running the project material, to reduce the number of warehouse calls. Default value is `false`.  
  
### show

Obtains a comprehensive overview of models, id_clusters, packages, and more in a project. Its capacity to provide detailed information makes it particularly useful when searching for specific details, like all the models in your project.
    
    
    $ pb show
    

#### Subcommands

##### **models**
    
    
     pb show models
    

This command lets you view information about the models in your project. The output includes the following information about each model:

  * **Warehouse name** : Name of the table/view to be created in the warehouse.
  * **Model type** : Whether its an identity stitching, feature view, SQL model etc.
  * **Output type** : Whether the output type is `ephemeral`, `table`, or `view`.
  * **Run type** : Whether the model’s run type is `discrete` or `incremental`.
  * **SQL type** : Whether the SQL type of the model is `single_sql` or `multi_sql`.


    
    
    pb show models --json
    

This subcommand saves all model details in a JSON file.

##### **dependencies**
    
    
     pb show dependencies
    

This subcommand generates a DAG in a graph file (`dependencies.png`) highlighting the dependencies of all models in your project.

##### **dataflow**
    
    
     pb show dataflow
    

This subcommand generates a DAG in a graph file (`dataflow.png`) highlighting the data flow of all models in your project.

##### **idstitcher-report**
    
    
     pb show idstitcher-report --id_stitcher_model models/<ModelName> --migrate_on_load
    

This subcommand creates a detailed report about the identity stitching model runs. To know the exact model reference to be used, execute the `pb show models` command.

Note that:

  * By default, this command picks up the last run - you can change this behavior using the flag `-l`.
  * Use the `--seed_clusters_csv` flag to pass a CSV file with two columns - `id` and `id_type`. The cluster ID can be either `rudder_id` or `other_id`. A sample file is shown below:

id| id_type  
---|---  
`'8f81237f90'`| `'user_id'`  
`'alex@example.com'`| `'email'`  
  
> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * Each row specifies an ID to be mapped to a cluster main ID, which is then included in the report.
>   * The ID need not be specific - for example, specifying `alex` returns all the pattern matches containing that name.
> 


The output of the `pb show idstitcher-report` command consists of:

  * **ModelRef** : The model reference name.
  * **Seq No** : Sequence number of the run for which you are creating the report.
  * **Material Name** : Output name as created in warehouse.
  * **Creation Time** : Time when the material object was created.
  * **Model Converged** : Indicates a successful run if `true`.
  * **Pre Stitched IDs before run** : Count of all the IDs before stitching.
  * **Post Stitched IDs after run** : Count of unique IDs after stitching.


Profile Builder also generates a HTML report with relevant results and graphics including largest cluster, ID graph, etc. It is saved in `output` folder and the exact path is shown on screen when you execute the command.

##### **entity-lookup**
    
    
     pb show entity-lookup -v '<trait value>'
    

This subcommand lists all the features associated with an entity using any of the traits (flag `-v`) as ID types (email, user id, etc. that you are trying to discover).

**Optional parameters**

Parameter| Description  
---|---  
`--entity string`| (Optional) Passes the entity value. (default `user`).  
`-h`| Displays help information for the command.  
`-p`| Specifies the project path to list the models. If not specified, it uses the project in the current directory.  
`-c`| File location of the `siteconfig.yaml` (defaults to the one in your home directory).  
`-t`| Target name (defaults to the target specified in `siteconfig.yaml` file).  
`--include_disabled`| Lets the disabled models be a part of the generated graph image (applicable to `dataflow` and `dependencies`).  
`--seq_no`| Specifies a particular run for an ID stitcher model (applicable for `idstitcher-report`).  
  
##### **plan**
    
    
     pb show plan
    

This subcommand shows the detailed information about materials created by a specific run and their corresponding timegrains.

**Optional parameters**

Parameter| Description  
---|---  
`--show_dependents`| Shows the list of dependent objects along with dependencies for each material. For example, to view information about a material with `seq_no 2` and get information about its dependent objects, use `pb show plan --seq_no 2 --show_dependents`.  
`--json`| Shows the information in JSON format.  
  
### query

Executes SQL query on the warehouse and prints the output on screen (10 rows by default).
    
    
    pb query <query>
    

For example, if you want to print the output of a specific table/view named `user_id_stitcher`, run the following query:
    
    
    pb query "select * from user_id_stitcher"
    

To reference a model with the name `user_default_id_stitcher` for a previous run with seq_no 26, you can execute:
    
    
    pb query "select * from {{this.DeRef('path/to/user_default_id_stitcher')}} limit 10" --seq_no=26
    

**Optional parameters** :

Parameter| Description  
---|---  
`-f`| Exports output to a CSV file.  
`-max_rows`| Maximum number of rows to be printed (default is 10).  
`-seq_no`| Sequence number for the run.  
  
### validate

Validates aspects of the project and configuration.
    
    
    $ pb validate
    

It allows you to run various tests on the project-related configurations and validate those. This includes but is not limited to validating the project configuration, privileges associated with the role specified in the site configuration of the project’s connection, etc.

#### Subcommands
    
    
    $ pb validate access
    

Runs tests on the role specified in the site configuration file and validates if the role has privileges to access all the related objects in the warehouse. It throws an error if the role does not have required privileges to access the input tables or does not have the permissions to write the material output in the output schema.

### version

Shows the Profile Builder’s current version along with its GitHash and native schema version.
    
    
    pb version
    

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.20/dev-docs/profiles-audit/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.20/dev-docs/yaml-refresher/>)