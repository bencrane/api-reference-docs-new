# Profiles Tutorial

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Profiles Tutorial

Get a walkthrough of the key Profiles concepts within a guided terminal session.

* * *

  * __4 minute read

  * 


> ![info](/docs/images/info.svg)
> 
> Profiles Tutorial (`pb tutorial`) is currently available only for Snowflake and Google BigQuery warehouses. Also, note that you can use it only with the Profiles Builder (PB) CLI tool.

Profiles Tutorial (`pb tutorial` command) is a guided interactive tutorial within the Profiles CLI.

This tutorial walks you through the key Profiles concepts and how they work. You will also build a basic Profiles project with an ID Stitcher model and a handful of features, ultimately producing an ID Graph in your warehouse and a view of the customers along with some customer features/attributes.

## Overview

The Profiles Tutorial has multiple interactive components and most of the interaction takes place within a terminal session. The goal of this tutorial is to familiarize you with the Profiles product - this includes details on the YAML configuration, how data unification works, what the outputs look like after a run, and how to troubleshoot and build a solid ID graph around a defined entity.

As a part of the tutorial, you will build a demo Profiles project configuration YAML which you will edit directly following the directions provided in the terminal. You will also seed your warehouse with some sample data that is sent to a target schema within your warehouse. You can query this data directly as well as the materialized tables produced by Profiles within the tutorial session.

With the help of this tutorial, you can build your own Profiles project and extend it further to unify your data around a defined entity, building a C360 degree view of this entity, and much more.

## Sample data

The sample data used for this tutorial is based on a fictional business called **Secure Solutions, LLC**.

This fictional business sells security IOT devices and a security management subscription service. They have a number of Shopify stores and a subscription management service, and one physical store where customers can buy security equipment and checkout at a kiosk.

This fictional business decided to use Profiles to more quickly and easily unify different data sources related to their customers as well as help produce a customer 360 table that they can activate in downstream tools.

## Prerequisites

  * Python environment (v3.9.0 to v3.11.10).
  * Profiles v0.20.0 or above installed locally within the above Python environment.


    
    
    pip3 install profiles-rudderstack
    

  * `profiles-mlcorelib` library (v0.7.0 or above) installed within the above Python environment (and same as the environment for the `profiles-rudderstack` library).


    
    
    pip install profiles-mlcorelib>=0.7.0
    

  * [Create a warehouse connection](<https://www.rudderstack.com/docs/archive/profiles/0.23/overview/quickstart/#2-create-warehouse-connection>) file that Profiles uses to access your warehouse. This creates a local site configuration file inside your home directory: `~/.pb/siteconfig.yaml`.


## Workflow

Retrieve the name of the connection you would like to use from the `siteconfig.yaml`. Then, run the below command in your terminal to start a new tutorial session:
    
    
    pb tutorial --connection <connection_name>
    

For example, if your `siteconfig.yaml` looks as follows:
    
    
    connections:
        snowflake-conn:
            target: snowflake
            outputs:
                snowflake:
                    type: snowflake
                    account: xxxxx
    

In that case, your connection name is `snowflake-conn`.

> ![info](/docs/images/info.svg)
> 
> The session takes between 30 minutes to one hour to complete. Once the tutorial is complete, the session automatically ends within your terminal.

### Tutorial components

  * Introduction to the tutorial and how to interact with it.
  * Introduction the the fictional business to provide context to the sample data.
  * Profiles project creation.
  * Profiles runs: Create an ID Graph.
  * ID graph QA - Phase 1
  * Fix the over stitching issues that happen in the first run.
  * ID graph QA - Phase 2: This includes more detailed analysis and sample queries to run to debug some users who got merged.
  * Run again to produce a healthy ID graph.
  * Feature creation: You will build a handful of features on the user entity defined in the tutorial.
  * Final run to produce a feature view, which is a view within the warehouse where each record is a unique user and each column is a defined feature or attribute on that user.


### Get started with your own project

Once you exit the tutorial session and want to begin a a new Profiles project with your own data, follow this [Quickstart guide](<https://www.rudderstack.com/docs/archive/profiles/0.23/overview/quickstart/>) to get started.

## FAQ

In addition to the below FAQs, see the FAQs on [Python-related errors](<https://www.rudderstack.com/docs/archive/profiles/0.23/additional-resources/faq/#python-related-errors>) for more information on debugging issues related to running the tutorial.

#### Is this tutorial powered by an LLM?

No, this tutorial is based on a simple static script meant as a step-by-step guide with some simple built-in validations.

#### Does the tutorial session seed my warehouse with data?

Yes, a part of the tutorial will seed your target schema (specified in the connection setup) with sample data for **Secure Solutions LLC**. It will add the below three tables: 1\. `PAGES` 2\. `TRACKS` 3\. `IDENTIFIES`

These tables will serve as source data for the Profiles configuration built during the tutorial session, for runs.

#### Does the tutorial output any tables in my warehouse?

Yes, the source data (see above) is used as an input into Profiles’ semantic models configured in the tutorial session.

The materialized tables and views will output to the same target schema configured in the site configuration/connection setup step.

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.23/dev-docs/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.23/dev-docs/create-new-project/>)