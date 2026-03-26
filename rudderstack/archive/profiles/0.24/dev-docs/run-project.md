# Run Profiles Project

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Run Profiles Project

Compile and run your Profiles project.

* * *

  * __less than a minute

  * 


This guide lists the commands required to run your Profiles project successfully.

## Compile

Once you have created the Profiles project, make sure to compile it to verify that there are no compilation errors.

Run the following command:
    
    
    pb compile
    

This generates SQL files in the `output/` folder that you can run directly on the warehouse. In case of any compilation errors, you will see them on your screen and also in the `logs/logfile.log` file.

## Run

Once the compilation is successful and there are no errors, run your Profiles project:
    
    
    pb run
    

This command generates and runs the SQL files in the warehouse, creating the material tables.

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.24/dev-docs/advanced-id-stitcher-features/id-graph-cardinality-rules/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.24/dev-docs/warehouse-output/>)