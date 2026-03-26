# Run Profiles Project

> Version: Latest (0.25 — Beta)0.240.230.220.210.200.190.180.170.160.150.140.130.120.110.100.9.40.9.30.9.10.9.00.8.0

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

  


  * [![](/docs/images/previous.svg)Previous](</docs/profiles/dev-docs/advanced-id-stitcher-features/advanced-operations/>)
  * [Next ![](/docs/images/next.svg)](</docs/profiles/dev-docs/warehouse-output/>)