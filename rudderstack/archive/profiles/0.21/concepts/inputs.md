# Inputs

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Inputs

Learn about inputs in Profiles.

* * *

  * __2 minute read

  * 


This guide introduces you to the concept of inputs in Profiles and shows how to use them in your Profiles project.

## Overview

The foundation of every companies data is the source files and data tables - these are the inputs that go into every data product a company produces.

In Profiles, `inputs` contain the IDs for identity graphs and the fields that build into a Customer360 (C360). They can be database tables or views, S3 buckets, and/or CSV files.

**SQL Keyword** : `FROM`

## Usage

You can define `inputs` in the [`inputs.yaml`](<https://www.rudderstack.com/docs/archive/profiles/0.21/dev-docs/inputs-yaml/>) file, as shown:
    
    
    inputs:
      - name: rsIdentifies
        app_defaults:
          table: autotrack_data.autotrack.identifies
          occurred_at_col: timestamp
          ids:
            - select: "user_id"
              type: user_id
              entity: user
            - select: "anonymous_id"
              type: anonymous_id
              entity: user
            - select: "lower(email)"
              type: email
              entity: user
      - name: rsPages
        app_defaults:
          table: autotrack_data.autotrack.pages
          occurred_at_col: timestamp
          ids:
            - select: "user_id"
              type: user_id
              entity: user
            - select: "anonymous_id"
              type: anonymous_id
              entity: user
    

## Best practices

  * Though it is possible to bring in data sources that only have one identifier column for your entity, it is best to have two or more columns, especially for `inputs` that you want to use as a source for the `id_stitcher` model.
  * If any of your ID columns are not of the string data type, then you must case them explicitly, as shown below:


    
    
          ids:
            - select: "CAST(user_id AS VARCHAR)"
              type: user_id
              entity: user
    

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.21/concepts/identity-graph/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.21/concepts/features/>)