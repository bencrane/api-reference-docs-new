# Project Structure

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

# Project Structure

Details on the file structure generated upon initializing a new Profiles project.

* * *

  * __2 minute read

  * 


This guide walks you through the Profiles project structure generated once you initialize a new project using the `pb init` command.

## Initial project structure

After initializing a new Profiles project, you will see the following project folder structure:
    
    
    .
    ├── logs/logfile.log
    ├── models/
    │   ├── inputs.yaml
    │   └── profiles.yaml
    ├── output/
    ├── .gitignore
    ├── pb_project.yaml
    └── README.md
    

Folder| Description  
---|---  
`logs/`| Stores the `logfile.log` file containing the logs from all `pb` runs.  
`models/`| Stores the [`inputs`](<https://www.rudderstack.com/docs/profiles/dev-docs/inputs-yaml/>), [`profiles`](<https://www.rudderstack.com/docs/profiles/dev-docs/profiles-yaml/>), [`sql_models`](<https://www.rudderstack.com/docs/profiles/dev-docs/sql-model-yaml/>), and [`macros`](<https://www.rudderstack.com/docs/profiles/dev-docs/macros-yaml/>) YAML files.  
`output/`| Stores the compiled SQL files from each project run.  
  
These files are then executed in your warehouse.  
File| Description  
---|---  
`.gitignore`| Specifies the files that Git ignores.  
[`pb_project.yaml`](<https://www.rudderstack.com/docs/profiles/dev-docs/pb-project-yaml/>)| Profiles project configuration.  
`README.md`| Overview on using `pb` and the SQL queries for analysis.  
  
## Full project structure

After adding [`sql_models.yaml`](<https://www.rudderstack.com/docs/profiles/dev-docs/sql-model-yaml/>) and [`macros.yaml`](<https://www.rudderstack.com/docs/profiles/dev-docs/macros-yaml/>) files (if used), the project structure looks as follows:
    
    
    .
    ├── logs/logfile.log
    ├── models/
    │   ├── inputs.yaml
    |   ├── macros.yaml
    |   ├── profiles.yaml
    │   └── sql_models.yaml
    ├── output/
    ├── .gitignore
    ├── pb_project.yaml
    └── README.md
    

## SQL output structure

Profiles projects are compiled into SQL files which are executed in your data warehouse.

These compiled SQL queries are stored in a hierarchy of folders in the `output` folder.
    
    
    output/
    └── <target>/
        └── seq_no/
            ├── 1/
            ├── 2/
            ├── ...
            └── latest/
                ├── compile/
                └── run/
    

The `output` folder contains folders for each warehouse connection target (for example, `dev`, `prod`, etc.).

Within each target folder is a `seq_no` folder containing separate folders for each sequence number (`1`, `2`, `3`, etc.), along with a `latest` symbolic link for the latest sequence number. The sequence number folders contain `compile` (compiled SQL files, staged for execution) and `run` (post execution SQL files) folders storing the SQL files and folders containing the SQL files.

### Naming convention

The SQL files and folders containing SQL files are named in the following format: `Material_<name>_<hash>_<seq_no>`.

For example: `Material_product_tier_32cf8f89_1`

  


  * [![](/docs/images/previous.svg)Previous](</docs/profiles/dev-docs/create-new-project/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/dev-docs/site-configuration-file/>)