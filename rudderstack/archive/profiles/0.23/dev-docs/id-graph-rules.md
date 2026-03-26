# ID Graph Inclusion/Exclusion Rules

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# ID Graph Inclusion/Exclusion Rules

Define rules to control which nodes and edges are included in your ID graph.

* * *

  * __4 minute read

  * 


The ID graph exclusions/inclusions feature lets you determine which nodes and edges are included in your ID graph by defining rules in a warehouse table—giving you fine-grained control over the graph structure beyond what’s possible with regex-based filters.

> ![info](/docs/images/info.svg)
> 
> These rules take the highest precedence over any other filtering mechanisms, including regex filters and rule-based filters.

## Key Features

  * **Node control** : Exclude or include specific nodes (identifiers) in the ID graph.
  * **Edge control** : Define specific connections between the identifiers to exclude or include.
  * **Rule management** : Get CLI tools for creating and populating rules tables.
  * **Precedence control** : Specify how conflicting rules should be handled.


## Set up the rules table

This section describes how to create and populate the rules table that controls ID Graph inclusions and exclusions.

### 1\. Create the rules table

Use the following CLI command to create a dedicated table in your warehouse:
    
    
    pb idstitch rules create
    

This creates a table named `id_stitch_rules` by default. You can specify a custom name as follows:
    
    
    pb idstitch rules create --name my_custom_rules
    

### 2\. Add rules to this table

You can add rules in two ways:

#### Interactive mode

Run the following command:
    
    
    pb idstitch rules update --interactive
    

You will then be prompted to enter the following details:

  * Entity name (for example, `user`, `account`)
  * ID1 value and type
  * Optional ID2 value and type
  * Action (EXCLUDE or INCLUDE)
  * Optional reason for the action


#### Batch mode

Run the following command:
    
    
    pb idstitch rules update -f rules.csv
    

This `rules.csv` file will contain the required columns: `entity`, `id1`, `id1_type`, `action`, and optional columns: `id2`, `id2_type`, `reason`.

## Configure your project YAML

To enable the rules for your project, add the following configuration to your YAML file:
    
    
    # Existing configuration...
    
    entities:
      - name: user
        id_stitcher: models/rudder_user_id_stitcher
        # Other entity configuration
    
    # Add the id_stitcher_rules section
    id_stitcher_rules:
      enabled: true                             # Optional, defaults to false
      table_name: id_stitch_rules    # Optional, defaults to id_stitch_rules
      priority: exclude                        # Optional, defaults to exclude
    

### Configuration parameters

Parameter| Description  
---|---  
`enabled`| Set it to `true` to activate the rules feature.  
`table_name`| The name of your rules table. It defaults to `id_stitch_rules`.  
`priority`| Defines how to handle conflicting rules. Acceptable values are `exclude` and `include`. The default value is `exclude`.  
  
## Rule behavior and examples

Note that the rules fall into two categories:

### 1\. Single ID rules (Node rules)

These rules apply to a single identifier and affect the entire node.

#### Example: Exclude a test email
    
    
    Entity: user  
    ID1: test@company.com  
    ID1_Type: email  
    Action: EXCLUDE
    

**Effect** : The node for `test@company.com` will be completely removed from the ID graph.

#### Example: Include a specific user ID
    
    
    Entity: user  
    ID1: 12345  
    ID1_Type: user_id  
    Action: INCLUDE
    

**Effect** : The node for user_id `12345` will be added to the graph even if it doesn’t appear in the input data.

### 2\. Paired ID rules (Edge rules)

These rules apply to the connections between two identifiers.

#### Example: Exclude a specific connection
    
    
    Entity: user  
    ID1: john@example.com  
    ID1_Type: email  
    ID2: user_67890  
    ID2_Type: user_id  
    Action: EXCLUDE
    

**Effect** : The direct connection between `john@example.com` and `user_67890` will be removed but both nodes remain in the ID graph. You can still connect them through other paths.

#### Example: Include a specific connection
    
    
    Entity: user  
    ID1: jane@example.com  
    ID1_Type: email  
    ID2: user_54321  
    ID2_Type: user_id  
    Action: INCLUDE
    

**Effect** : A direct connection between `jane@example.com` and `user_54321` will be added to the ID graph **even if** this connection doesn’t exist in the input data.

## Conflict resolution

When rules conflict, the resolution depends on your `priority` setting:

  * **With`priority: exclude` (default)**: If a node is excluded but appears in an edge inclusion rule, the node exclusion takes precedence and the edge inclusion is discarded.
  * **With`priority: include`**: If a node is excluded but appears in an edge inclusion rule, the edge inclusion takes precedence and the node will remain in the graph.


> ![info](/docs/images/info.svg)
> 
> If multiple rules exist for the same entity and identifiers, the most recent rule takes precedence.

## How this feature works

  1. During `pb run` or `pb compile`, the system checks for any enabled rules.
  2. Rules are applied while preparing the `raw_edges` table. Note that excluded nodes are not added to this `raw_edges` table.

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.23/dev-docs/optimizations/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.23/dev-docs/run-project/>)