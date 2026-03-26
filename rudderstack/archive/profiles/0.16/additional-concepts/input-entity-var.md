# Input Var Vs. Entity Var

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Input Var Vs. Entity Var

Know the basics of an `entity_var` and `input_var` and their difference.

* * *

  * __3 minute read

  * 


In Profiles, both `entity_var` and `input_var` are used to define and store data, but they serve different purposes and have different characteristics.

**`entity_var`** : It represents the individual attributes or variables which describe your entities. For example, they can be `name`, `city`, `LastVisitTimestamp`, etc. for the `user` entity. By default, every `entity_var` gets stored as a feature. The final output of an `entity_var` is an additional column on the entity var table, which serves as a base for other models, like feature view⁠.

**`input_var`** : It is very similar to an `entity_var` in syntax and is used to calculate a column for a source/input table. However, it represents a single value per row of an input model instead of a single value per entity ID. Essentially, an `input_var` modifies the input table by adding a new column, which can then be used to calculate features in entity vars.

## Choosing between `input_var` and `entity_var`

In most of the common scenarios, you can build features defining an `entity_var` with a `name`, `select`, `from`, etc.

However, at times, you might need finer control and influence on how to create a particular feature. You might need to use the output of:

  * An `entity_var` as an input to another `entity_var`.
  * An `input_var` as an input to another `entity_var`.


For example, you need to use an `input_var` when you need to perform a specific partition in a window clause. Here, you need to access the original input table as well as the `main_id`. This cannot be done with an `entity_var` referenced from another `entity_var` as `entity_vars` do not support partitioning values other than the `main_id`.

An `input_var` can be considered as an additional subquery that calculates a certain value directly from the input/source table and adds that value back in via a `JOIN` clause. The new helper column can then be accessed within an `entity_var` definition for further calculation or filtering.

Features are calculated off of their inputs whether the input is a direct input table or a custom SQL model. The `input_var` modifies the input table so that you have an additional column that you can use for feature calculation.

## Comparison

`entity_var`| `input_var`  
---|---  
It is an entity feature itself.| It can be used to define entity features but is not an entity feature itself.  
Adds a helper column to the feature table.| Adds a helper column to the input table.  
Each value is associated with a row of the feature table.| Each value is associated with a row of the specified input table.  
Final output is an additional column on the entity var table.| Final output is an additional column on the input var table.  
Does not support partitioning values other than the `main_id`.| Supports partitioning values other than the `main_id`.  
  
## Example

Let’s assume that you want to build a feature for getting metadata of the users who visited the web and the number of pages on a particular date. You would need to partition the users by their `main_id` and dates to get the count per user per date. `Entity_vars` partition by `main_id` by default. So, you have to create an `input_var` that calculates the count of pages visited partitioned by the `main_id` and date. Then use the output of that `input_var` within the `entity_var` feature you want to populate in the customer 360 table:
    
    
    - input_var:
       name: page_count
       description: Input var to add column to rsPages SQL model to get a page count per date
       select: count(distinct url)
       from: models/pages_orderby_table
       window:
         partition_by:
           - profile_id
           - date
       tags:
         - engagement
    - entity_var:
       name: web_dates_visited_365_days
       select: array_agg(distinct object_construct('date', date, 'page_count',{{pages_orderby_table.Var("page_count")}}))
       from: models/pages_orderby_table
       description: rolling 365 days array of json objects with the UTC timestamps the user visited the website along with the number of pages visited per date stamp
       tags:
         - Attribution
    

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.16/additional-concepts/input-sources/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.16/additional-concepts/run-process/>)