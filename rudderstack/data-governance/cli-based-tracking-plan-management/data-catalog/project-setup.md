# Data Catalog Project Setup Alpha

Set up your project containing the definitions of your Data Catalog resources.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __less than a minute

  * 


This guide shows you how to set up your project containing the definitions of your Data Catalog resources.

## Overview

In the context of the [Rudder CLI](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/>) tool, a Data Catalog project typically consists of a root directory that contains all the project files. Within this root directory, each YAML file can contain definitions for resources of a particular type, for example, events, properties, custom data types, and Tracking Plans.

The location and naming of these YAML files is flexible, as you can store the YAML files anywhere within the project’s root directory or subdirectories.

## Set up your project

The Rudder CLI tool expects the Data Catalog resources to be described in [YAML files](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/project-yaml-reference/>) present in your system.

If you’re working with a Unix-compatible shell, run the following command to create a `tutorial-catalog` folder in your home directory, which you can use to populate the Data Catalog resources as YAML files:
    
    
    mkdir ~/tutorial-catalog
    

> ![success](/docs/images/tick.svg)
> 
> The Rudder CLI tool automatically processes all valid YAML files within the project structure to recognize the defined resources.

## Next steps

  * [Create events](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/events/>)
  * [Create event categories](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/events/categories/>)
  * [Create properties](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/properties/>)
  * [Create custom types](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/data-catalog/custom-types/>)


See [Data Catalog YAML Reference](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/project-yaml-reference/>) for the detailed YAML spec containing the definitions of these Data Catalog resources.