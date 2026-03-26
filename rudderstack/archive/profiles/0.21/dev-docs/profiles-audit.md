# Profiles ID Stitcher Audit Tool

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Profiles ID Stitcher Audit Tool

Get aggregate analysis of your ID graph across entities and in-depth analysis of single IDs.

* * *

  * __26 minute read

  * 


Profiles ID Stitcher Audit tool is embedded within the Profiles Builder (PB) core CLI tool and helps you analyze the health of your ID graph.

> ![info](/docs/images/info.svg)
> 
> Profiles ID Stitcher Audit tool is only available in Profile Builder (PB) version 0.19.0 and above. Also, note that this tool is only available for the PB CLI.
> 
> If you are developing your Profiles projects within the web-based editor (IDE), then see IDE project migration for the steps to develop locally.

This feature provides the following insights:

  * A high level aggregate analysis of your overall ID graph across all IDs for a given entity.
  * The option to select a single ID (typically, a customer) and provide a drilled-down analysis and visualization about their individual graph.
  * An optional interactive LLM session where you can ask questions about your ID graph and get answers to them.


## Prerequisites

  * Python environment (v3.9.0 to v3.11.10).
  * Profiles v0.19.0 or later installed locally within the above Python environment.


    
    
    pip3 install profiles-rudderstack
    

  * `profiles-mlcorelib` library (v0.6.0 or above) installed within the above Python environment (and same as the environment for the `profiles-rudderstack` library).


    
    
    pip install profiles-mlcorelib>=0.6.0
    

  * The audit tool helps understand an ID graph that is already materialized. So, it expects a successful Profiles project run on the same pb version **at least once** that has generated an ID graph, and the ID graph definition **does not change** after the run.
  * Generate a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) in your RudderStack workspace. Then, add it to your [site configuration file](<https://www.rudderstack.com/docs/archive/profiles/0.21/dev-docs/site-configuration-file/>).


> ![info](/docs/images/info.svg)
> 
> The workspace-level Service Access Token has **Read** permissions by default. You do not need to assign any [resource permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) while generating the token.

#### Permissions for legacy RBAC system

If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), your workspace-level Service Access Token should have **Viewer** permission.

See [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for more information on generating the token.

[![workspace-level Service Access Token with Viewer permission](/docs/images/access-management/permissions/legacy/viewer.webp)](</docs/images/access-management/permissions/legacy/viewer.webp>)

### IDE project migration

If you are developing a Profiles project in the RudderStack dashboard using the web-based editor (IDE), then follow these steps:

  1. Navigate to your Profiles project in the RudderStack dashboard.
  2. Make sure that your latest IDE session is saved to ensure that you have the latest changes. If your project is connected to a remote repo, you can commit those changes as well.
  3. Download the project: \- If in a remote repo, navigate there and download locally. \- If the project is not connected to a remote repo, then navigate to the project’s settings and click **Download this project** , as shown:

[![Download Profiles project](/docs/images/profiles/download-profiles-project-1.webp)](</docs/images/profiles/download-profiles-project-1.webp>)

  4. Move the project configuration to the desired local directory.
  5. Navigate to the root of that directory within your terminal.
  6. Before performing the runs locally, verify that you have set up a warehouse connection. See [Step 2: Create warehouse connection](<https://www.rudderstack.com/docs/profiles/overview/quickstart/#2-create-warehouse-connection>) to create a local file containing your warehouse credentials.


You can successfully run PB and utilize the Profiles ID Stitcher Audit tool after completing the above steps.

## Workflow overview

To use this feature, go to your Profiles project configuration and run the below command within your terminal:
    
    
    pb audit id_stitcher
    

The audit tool then:

  1. Scans the project to look for ID stitcher models.

  2. Asks the customers to select one model in case there are multiple ID stitcher models.

  3. For the selected model, presents the below three audit stages:

     * Static ID graph summary report
     * Cluster analysis
     * Interactive LLM session


Note that the tool works only on top of a batch ID graph run. By default, an ID stitcher model runs incrementally and a batch run typically happens in the below cases:

  * First run of a Profiles project.
  * When you change the ID stitcher model’s definition, for example, adding/removing input sources or id_types, filters, etc.
  * When you upgrade your Profiles project to a new version.
  * If the underlying Profiles tables in the output schema are not found.


Usually, an audit is done after modifying the ID stitcher model - this should not cause an issue because the run happens in batch mode. However, in case an audit is being performed after an incremental run, you can force a one-time batch run by adding a flag `rebase_incremental` in the `pb run` command, as shown:
    
    
    pb run --rebase_incremental
    

The above command forces a full batch run for one time, allowing for a full audit of the ID graph.

## Static ID graph summary

The `pb audit id_stitcher` command gives you a detailed report on the ID stitcher as an output. It contains the ID graph summary that helps you understand:

  * ID graph’s definition, like ID types, main ID, etc.

  * Count of values, like:

    * Counts of each ID types before and after ID stitching.
    * Most widely connected IDs.
    * Resolved main ID stats on the number of IDs connected together, like average, 99th percentile, etc.
    * IDs that are never connected to any other ID.


Note that for all the counts, the tool shows some samples but they are at an aggregate level, not on an individual `main_id` level.

**Click here to view a sample report**. Note that the exact text and format may differ.  

    
    
    main id for entity user: USER_MAIN_ID
    
    
    Analyzing ID Stitcher for entity: user
            Node types: ['id', 'anonymous_id', 'contact_id', 'email', 'lead_id', 'user_id']
            Unique IDs of each type and their counts:
                    id: 10958
                    anonymous_id: 4294899
                    contact_id: 79854
                    email: 122661
                    lead_id: 75482
                    user_id: 296346
    Total Distinct IDs
            Before stitching: 4880200
            After stitching: 4290186
    
    
    Top 10 nodes by edge count:
                    ID: alex@example.com, Type: email, Edges: 2503
                    ID: alex@example.com, Type: user_id, Edges: 2140
                    ID: alice@example.com, Type: email, Edges: 1725
                    ID: abc@example.com, Type: email, Edges: 946
    
    Top 5 nodes of different types, before id stitching, by edge counts:
    
            type id by edge count:
                    ID: a2ab0609d6c10187ff11, Edges: 2
                    ID: a2ab060a860ee7b512, Edges: 2
                    ID: a2ab0605e232d3c609, Edges: 2
                    ID: a2ab060bb95dcaef14, Edges: 2
                    ID: a2ab0600d159d259, Edges: 2
    
            type anonymous_id by edge count:
                    ID: 49a8bebe-4d9d-47e5-8ea3-29153fc33dcb, Edges: 71
                    ID: d81d2d84-71a8-46db-9d30-81502051c214, Edges: 61
                    ID: 3421a313-189e-45d2-9270-e0ae3181e07d, Edges: 47
    
            type contact_id by edge count:
                    ID: 003QP000001SRUjYAO, Edges: 7
                    ID: 003QP000001LpBGYA0, Edges: 6
    
            type email by edge count:
                    ID: alex@example.com, Edges: 2503
                    ID: alice@example.com, Edges: 1725
    
            type lead_id by edge count:
                    ID: 00Q5x00001zW1Y9EAK, Edges: 3
                    ID: 00QQP00000800rR2AQ, Edges: 3
    
            type user_id by edge count:
                    ID: alex@example.com, Edges: 2140
                    ID: 28HhwSx1WEU56QM5sY7r74MEf9n, Edges: 1526
    
    Average edge count per node (before stitching): 1.331919
    
    Average edge count by node type (before stitching):
                    id: 2.518149
                    anonymous_id: 3.122989
                    contact_id: 3.068089
                    email: 3.406679
                    lead_id: 2.453102
                    user_id: 4.522037
    
                    POST ID STITCHING ANALYSIS
    
    
    Cluster size after stitching:
                    No:of main ids with a single other id (Singleton nodes): 3998772
                    Average other id counts: 1.137526
                    Min other id counts for a single main id: 1
                    Max other id counts for a single main id: 13711
                    25th percentile: 1
                    50th percentile: 1
                    75th percentile: 1
                    90th percentile: 1
                    99th percentile: 4
    
    Average number of ids of different id types, per main id, after stitching:
                    id: 1.059563
                    anonymous_id: 1.026212
                    contact_id: 1.031319
                    email: 1.049362
                    lead_id: 1.104071
                    user_id: 1.149782
    
    Top 5 biggest clusters after id stitching (and the distinct id types in each cluster):
            Main ID: rid0e06a33cfdbccc7679e635e78f0f391f, Size: 13711
                    anonymous_id: 11503
                    user_id: 1205
                    email: 457
                    lead_id: 375
                    contact_id: 117
                    id: 54
            Main ID: rid039ea1d83a8484fa66f153143f013ac7, Size: 1526
                    anonymous_id: 1525
                    user_id: 1
            Main ID: rid25ddb86517babaa3f45dceef3c400330, Size: 964
                    anonymous_id: 949
                    user_id: 9
                    email: 2
                    contact_id: 2
                    lead_id: 2
            Main ID: ridf0fef860592708f92f211df285bef625, Size: 833
                    anonymous_id: 618
                    user_id: 88
                    email: 47
                    lead_id: 47
                    contact_id: 32
                    id: 1
            Main ID: rid2e9139338ef8ccfec085e259da0ef3fb, Size: 719
                    anonymous_id: 718
                    user_id: 1
    
    Singleton Node Analysis (after stitching):
    anonymous_id: 3963171 nodes (92.28%) not connected to any other ID type
    user_id: 28686 nodes (9.68%) not connected to any other ID type
    contact_id: 5376 nodes (6.73%) not connected to any other ID type
    lead_id: 1374 nodes (1.82%) not connected to any other ID type
    id: 165 nodes (1.51%) not connected to any other ID type
    
    Checking for potential issues:
    WARNING:__main__:Potential overstitching detected: Node alex@example.com of type email has 2503 edges
    
    Checking for missing direct edges between node types (but indirect edges can exist):
    WARNING:__main__:Warning: No direct edges found between id and anonymous_id
    WARNING:__main__:Warning: No direct edges found between id and contact_id
    WARNING:__main__:Warning: No direct edges found between id and lead_id
    WARNING:__main__:Warning: No direct edges found between id and user_id
    WARNING:__main__:Warning: No direct edges found between anonymous_id and id
    WARNING:__main__:Warning: No direct edges found between anonymous_id and contact_id
    WARNING:__main__:Warning: No direct edges found between anonymous_id and lead_id
    WARNING:__main__:Warning: No direct edges found between contact_id and id
    WARNING:__main__:Warning: No direct edges found between contact_id and anonymous_id
    WARNING:__main__:Warning: No direct edges found between contact_id and user_id
    WARNING:__main__:Warning: No direct edges found between lead_id and id
    WARNING:__main__:Warning: No direct edges found between lead_id and anonymous_id
    WARNING:__main__:Warning: No direct edges found between lead_id and user_id
    WARNING:__main__:Warning: No direct edges found between user_id and id
    WARNING:__main__:Warning: No direct edges found between user_id and contact_id
    WARNING:__main__:Warning: No direct edges found between user_id and lead_id
    
     Check for missing edges between node types (direct or indirect) after id stitching:
    No missing edges found between node types. GREAT!!
    
    
    ANALYSIS COMPLETE FOR ENTITY: user
    

## Cluster analysis

The `pb audit id_stitcher` command also lets you understand specific clusters (`main_id`s), for example, how an email ID `E1` is linked to a Salesforce ID `S1`.

The audit tools gives a snapshot of the complete cluster and also points to the IDs that **may be** problematic.

**Click here to view a sample**  

    
    
     You can explore specific clusters by entering an ID to see how the other ids are all connected and the cluster is formed.
    The ID can be either the main ID or any other ID type.
    Enter an ID to visualize (or 'skip' to skip this step): 
    Acme
    
    Your network visualization is ready! We've saved an interactive map of your data connections here:
    /Users/user_name/git_repos/profiles-prod/graph_outputs/Acme_graph.html
    You can open this file in your web browser to explore the network visually.
    Cluster Summary:
    
            Network overview:
            -----------------
            1. Size: 7 ids connected by 9 links
            2. Connectivity: On average, each id is connected to 2.6 other ids
            3. Spread: The farthest connected ids are 2 steps apart
    
            Key Players:
            ------------       
    
            Most connected ids:
            - ID: acme.com, No:of edges: 6
            - ID: Acme, No:of edges: 2
            - ID: 000123XYZ, No:of edges: 2
            - ID: Acme America, No:of edges: 2
            - ID: 000456ABC, No:of edges: 2
            - ID: 000789DEF, No:of edges: 2
            - ID: Acme Inc, No:of edges: 2
    
            Critical Linking Nodes, and percent of id pairs they are connecting (these are the nodes that act as bridges across all nodes):
            - ID: acme.com, % of shortest paths: 80.00%
    

  


The audit tool also outputs an HTML file that helps you understand the cluster visually. It is stored locally and is loaded proactively by highlighting the path so you can revisit it later. A sample file is shown:

[![Cluster analysis](/docs/images/profiles/cluster-analysis.webp)](</docs/images/profiles/cluster-analysis.webp>)

In the above example, you can see how `acme.com` joins `Acme Inc` and `Acme America` entities which are probably different. You can address this by removing the `acme.com` domain.

**Click here to view a sample project** that helps you identify a common ID that has multiple users stitched together.  

    
    
    <html>
        <head>
            <meta charset="utf-8">
                <script src="lib/bindings/utils.js"></script>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.2/dist/dist/vis-network.min.css" integrity="sha512-WgxfT5LWjfszlPHXRmBWHkV2eceiWTOBvrKCNbdgDYTHrT2AeLCGbF4sZlZw3UMN3WtL0tGUoIAKsu8mllg/XA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
                <script src="https://cdnjs.cloudflare.com/ajax/libs/vis-network/9.1.2/dist/vis-network.min.js" integrity="sha512-LnvoEWDFrqGHlHmDD2101OrLcbsfkrzoSpvtSQtxK3RMnRV0eOkhhBN2dXHKRrUU8p2DGRTk35n4O8nWSVe1mQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <center>
    <h1></h1>
    </center>
    
    <!-- <link rel="stylesheet" href="../node_modules/vis/dist/vis.min.css" type="text/css" />
    <script type="text/javascript" src="../node_modules/vis/dist/vis.js"> </script>-->
            <link
              href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"
              rel="stylesheet"
              integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6"
              crossorigin="anonymous"
            />
            <script
              src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js"
              integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf"
              crossorigin="anonymous"
            ></script>
            <center>
              <h1></h1>
            </center>
            <style type="text/css">
                 #mynetwork {
                     width: 100%;
                     height: 1000px;
                     background-color: #ffffff;
                     border: 1px solid lightgray;
                     position: relative;
                     float: left;
                 }
            </style>
        </head>
        <body>
            <div style="position: fixed; top: 20px; right: 20px; background-color: rgba(255, 255, 255, 0.9); 
                        padding: 15px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.2); z-index: 1000;">
                <div style="font-weight: bold; margin-bottom: 10px;">ID Types</div>
                    <div style="display: flex; align-items: center; margin-bottom: 5px;">
                        <div style="width: 20px; height: 20px; background-color: #b23535; margin-right: 10px; border-radius: 3px;"></div>
                        <div>user_id</div>
                    </div>
                    <div style="display: flex; align-items: center; margin-bottom: 5px;">
                        <div style="width: 20px; height: 20px; background-color: #99b235; margin-right: 10px; border-radius: 3px;"></div>
                        <div>anonymous_id</div>
                    </div>
                    <div style="display: flex; align-items: center; margin-bottom: 5px;">
                        <div style="width: 20px; height: 20px; background-color: #35b267; margin-right: 10px; border-radius: 3px;"></div>
                        <div>sample_customer_id</div>
                    </div>
                    <div style="display: flex; align-items: center; margin-bottom: 5px;">
                        <div style="width: 20px; height: 20px; background-color: #3567b2; margin-right: 10px; border-radius: 3px;"></div>
                        <div>device_id</div>
                    </div>
                    <div style="display: flex; align-items: center; margin-bottom: 5px;">
                        <div style="width: 20px; height: 20px; background-color: #9935b2; margin-right: 10px; border-radius: 3px;"></div>
                        <div>email</div>
                    </div>
            </div>
            
            <div class="card" style="width: 100%">
                <div id="mynetwork" class="card-body"></div>
            </div>
    
            <script type="text/javascript">
    
                  // initialize global variables.
                  var edges;
                  var nodes;
                  var allNodes;
                  var allEdges;
                  var nodeColors;
                  var originalNodes;
                  var network;
                  var container;
                  var options, data;
                  var filter = {
                      item : '',
                      property : '',
                      value : []
                  };
    
                  // This method is responsible for drawing the graph, returns the drawn network
                  function drawGraph() {
                      var container = document.getElementById('mynetwork');
    
                      // parsing and collecting nodes and edges from the python
                      nodes = new vis.DataSet([{"color": "rgba(153, 53, 178, 1.0)", "font": {"color": "black"}, "id": "alexkeener@example.com", "label": "alexkeener@example.com", "shape": "dot", "title": "ID: alexkeener@example.com\nID-Type: email\nDegree: 36"}, {"color": "rgba(53, 103, 178, 0.37777777777777777)", "font": {"color": "black"}, "id": "887d473fa43c", "label": "887d473fa43c", "shape": "dot", "title": "ID: 887d473fa43c\nID-Type: device_id\nDegree: 4"}, {"color": "rgba(53, 103, 178, 0.37777777777777777)", "font": {"color": "black"}, "id": "bc854f11fca5", "label": "bc854f11fca5", "shape": "dot", "title": "ID: bc854f11fca5\nID-Type: device_id\nDegree: 4"}, {"color": "rgba(53, 103, 178, 0.37777777777777777)", "font": {"color": "black"}, "id": "65dacdcce759", "label": "65dacdcce759", "shape": "dot", "title": "ID: 65dacdcce759\nID-Type: device_id\nDegree: 4"}, {"color": "rgba(53, 103, 178, 0.37777777777777777)", "font": {"color": "black"}, "id": "29fc92b6df57", "label": "29fc92b6df57", "shape": "dot", "title": "ID: 29fc92b6df57\nID-Type: device_id\nDegree: 4"}, {"color": "rgba(178, 53, 53, 0.33888888888888885)", "font": {"color": "black"}, "id": "akeener", "label": "akeener", "shape": "dot", "title": "ID: akeener\nID-Type: user_id\nDegree: 2"}, {"color": "rgba(153, 53, 178, 0.8833333333333333)", "font": {"color": "black"}, "id": "alicekeener@example.com", "label": "alicekeener@example.com", "shape": "dot", "title": "ID: alicekeener@example.com\nID-Type: email\nDegree: 30"}, {"color": "rgba(53, 103, 178, 0.37777777777777777)", "font": {"color": "black"}, "id": "64e041ba1b8c", "label": "64e041ba1b8c", "shape": "dot", "title": "ID: 64e041ba1b8c\nID-Type: device_id\nDegree: 4"}, {"color": "rgba(153, 178, 53, 0.33888888888888885)", "font": {"color": "black"}, "id": "56ed43ca-22c3-40cd-858d-3e3711a10395", "label": "56ed43ca-22c3-40cd-858d-3e3711a10395", "shape": "dot", "title": "ID: 56ed43ca-22c3-40cd-858d-3e3711a10395\nID-Type: anonymous_id\nDegree: 2"}, {"color": "rgba(53, 178, 103, 0.4361111111111111)", "font": {"color": "black"}, "id": "1001724", "label": "1001724", "shape": "dot", "title": "ID: 1001724\nID-Type: sample_customer_id\nDegree: 7"}, {"color": "rgba(153, 178, 53, 0.33888888888888885)", "font": {"color": "black"}, "id": "37dd4c20-6bef-4de6-bedd-c4cc204ff1e1", "label": "37dd4c20-6bef-4de6-bedd-c4cc204ff1e1", "shape": "dot", "title": "ID: 37dd4c20-6bef-4de6-bedd-c4cc204ff1e1\nID-Type: anonymous_id\nDegree: 2"}, {"color": "rgba(53, 178, 103, 0.611111111111111)", "font": {"color": "black"}, "id": "1001601", "label": "1001601", "shape": "dot", "title": "ID: 1001601\nID-Type: sample_customer_id\nDegree: 16"}, {"color": "rgba(153, 178, 53, 0.33888888888888885)", "font": {"color": "black"}, "id": "61e3bcdc-d995-41d9-a6aa-1172af68f104", "label": "61e3bcdc-d995-41d9-a6aa-1172af68f104", "shape": "dot", "title": "ID: 61e3bcdc-d995-41d9-a6aa-1172af68f104\nID-Type: anonymous_id\nDegree: 2"}, {"color": "rgba(53, 178, 103, 0.7472222222222221)", "font": {"color": "black"}, "id": "8096804", "label": "8096804", "shape": "dot", "title": "ID: 8096804\nID-Type: sample_customer_id\nDegree: 23"}, {"color": "rgba(53, 103, 178, 0.37777777777777777)", "font": {"color": "black"}, "id": "da21019fe59d", "label": "da21019fe59d", "shape": "dot", "title": "ID: da21019fe59d\nID-Type: device_id\nDegree: 4"}, {"color": "rgba(153, 178, 53, 0.33888888888888885)", "font": {"color": "black"}, "id": "77f689d8-1d07-4ea2-a34c-a73aa9b76516", "label": "77f689d8-1d07-4ea2-a34c-a73aa9b76516", "shape": "dot", "title": "ID: 77f689d8-1d07-4ea2-a34c-a73aa9b76516\nID-Type: anonymous_id\nDegree: 2"}, {"color": "rgba(53, 103, 178, 0.37777777777777777)", "font": {"color": "black"}, "id": "2001cbbf1ffd", "label": "2001cbbf1ffd", "shape": "dot", "title": "ID: 2001cbbf1ffd\nID-Type: device_id\nDegree: 4"}, {"color": "rgba(153, 178, 53, 0.33888888888888885)", "font": {"color": "black"}, "id": "2f41b084-7c53-4ef4-a746-a36c591aabdc", "label": "2f41b084-7c53-4ef4-a746-a36c591aabdc", "shape": "dot", "title": "ID: 2f41b084-7c53-4ef4-a746-a36c591aabdc\nID-Type: anonymous_id\nDegree: 2"}, {"color": "rgba(153, 178, 53, 0.33888888888888885)", "font": {"color": "black"}, "id": "a207523c-d826-45c5-b104-d2f0a80dda12", "label": "a207523c-d826-45c5-b104-d2f0a80dda12", "shape": "dot", "title": "ID: a207523c-d826-45c5-b104-d2f0a80dda12\nID-Type: anonymous_id\nDegree: 2"}, {"color": "rgba(153, 178, 53, 0.33888888888888885)", "font": {"color": "black"}, "id": "3407e0e3-4900-497c-bff8-8d370754e3ee", "label": "3407e0e3-4900-497c-bff8-8d370754e3ee", "shape": "dot", "title": "ID: 3407e0e3-4900-497c-bff8-8d370754e3ee\nID-Type: anonymous_id\nDegree: 2"}, {"color": "rgba(53, 178, 103, 0.7277777777777779)", "font": {"color": "black"}, "id": "8097816", "label": "8097816", "shape": "dot", "title": "ID: 8097816\nID-Type: sample_customer_id\nDegree: 22"}, {"color": "rgba(153, 178, 53, 0.33888888888888885)", "font": {"color": "black"}, "id": "dcf6d0f9-3710-4f97-98cb-75288033c56d", "label": "dcf6d0f9-3710-4f97-98cb-75288033c56d", "shape": "dot", "title": "ID: dcf6d0f9-3710-4f97-98cb-75288033c56d\nID-Type: anonymous_id\nDegree: 2"}, {"color": "rgba(153, 178, 53, 0.33888888888888885)", "font": {"color": "black"}, "id": "efc1aeba-0a0d-40be-a24a-ee393299a480", "label": "efc1aeba-0a0d-40be-a24a-ee393299a480", "shape": "dot", "title": "ID: efc1aeba-0a0d-40be-a24a-ee393299a480\nID-Type: anonymous_id\nDegree: 2"}, {"color": "rgba(53, 103, 178, 0.37777777777777777)", "font": {"color": "black"}, "id": "1bf9329f6a6e", "label": "1bf9329f6a6e", "shape": "dot", "title": "ID: 1bf9329f6a6e\nID-Type: device_id\nDegree: 4"}, {"color": "rgba(53, 103, 178, 0.37777777777777777)", "font": {"color": "black"}, "id": "c0ba22140cec", "label": "c0ba22140cec", "shape": "dot", "title": "ID: c0ba22140cec\nID-Type: device_id\nDegree: 4"}, {"color": "rgba(153, 178, 53, 0.33888888888888885)", "font": {"color": "black"}, "id": "39974b70-b667-4540-8eaa-a91d0e5180a1", "label": "39974b70-b667-4540-8eaa-a91d0e5180a1", "shape": "dot", "title": "ID: 39974b70-b667-4540-8eaa-a91d0e5180a1\nID-Type: anonymous_id\nDegree: 2"}, {"color": "rgba(53, 103, 178, 0.35833333333333334)", "font": {"color": "black"}, "id": "f7d3790baeea", "label": "f7d3790baeea", "shape": "dot", "title": "ID: f7d3790baeea\nID-Type: device_id\nDegree: 3"}, {"color": "rgba(53, 103, 178, 0.35833333333333334)", "font": {"color": "black"}, "id": "2cf176c253e7", "label": "2cf176c253e7", "shape": "dot", "title": "ID: 2cf176c253e7\nID-Type: device_id\nDegree: 3"}, {"color": "rgba(53, 103, 178, 0.37777777777777777)", "font": {"color": "black"}, "id": "84f9eb766ea0", "label": "84f9eb766ea0", "shape": "dot", "title": "ID: 84f9eb766ea0\nID-Type: device_id\nDegree: 4"}, {"color": "rgba(53, 103, 178, 0.35833333333333334)", "font": {"color": "black"}, "id": "54cb22e5f0a7", "label": "54cb22e5f0a7", "shape": "dot", "title": "ID: 54cb22e5f0a7\nID-Type: device_id\nDegree: 3"}, {"color": "rgba(53, 103, 178, 0.35833333333333334)", "font": {"color": "black"}, "id": "6848d77e2c51", "label": "6848d77e2c51", "shape": "dot", "title": "ID: 6848d77e2c51\nID-Type: device_id\nDegree: 3"}, {"color": "rgba(53, 103, 178, 0.35833333333333334)", "font": {"color": "black"}, "id": "e54e6b399efc", "label": "e54e6b399efc", "shape": "dot", "title": "ID: e54e6b399efc\nID-Type: device_id\nDegree: 3"}, {"color": "rgba(53, 103, 178, 0.35833333333333334)", "font": {"color": "black"}, "id": "77e1b9368bd0", "label": "77e1b9368bd0", "shape": "dot", "title": "ID: 77e1b9368bd0\nID-Type: device_id\nDegree: 3"}, {"color": "rgba(53, 103, 178, 0.35833333333333334)", "font": {"color": "black"}, "id": "e14211ff4114", "label": "e14211ff4114", "shape": "dot", "title": "ID: e14211ff4114\nID-Type: device_id\nDegree: 3"}, {"color": "rgba(53, 103, 178, 0.35833333333333334)", "font": {"color": "black"}, "id": "278e2d59feeb", "label": "278e2d59feeb", "shape": "dot", "title": "ID: 278e2d59feeb\nID-Type: device_id\nDegree: 3"}, {"color": "rgba(53, 103, 178, 0.35833333333333334)", "font": {"color": "black"}, "id": "639d42ba6306", "label": "639d42ba6306", "shape": "dot", "title": "ID: 639d42ba6306\nID-Type: device_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "34ffd366-5581-404c-9de7-8e20958bd62f", "label": "34ffd366-5581-404c-9de7-8e20958bd62f", "shape": "dot", "title": "ID: 34ffd366-5581-404c-9de7-8e20958bd62f\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "1adf0fa5-91a7-4dd3-895e-75799df6bbc6", "label": "1adf0fa5-91a7-4dd3-895e-75799df6bbc6", "shape": "dot", "title": "ID: 1adf0fa5-91a7-4dd3-895e-75799df6bbc6\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "6758a04b-f52e-432b-9f42-54fb615baa63", "label": "6758a04b-f52e-432b-9f42-54fb615baa63", "shape": "dot", "title": "ID: 6758a04b-f52e-432b-9f42-54fb615baa63\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "ec58c825-69b5-4406-bb89-189aed588793", "label": "ec58c825-69b5-4406-bb89-189aed588793", "shape": "dot", "title": "ID: ec58c825-69b5-4406-bb89-189aed588793\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "e9779e82-9943-4039-a8c7-fc1609d99295", "label": "e9779e82-9943-4039-a8c7-fc1609d99295", "shape": "dot", "title": "ID: e9779e82-9943-4039-a8c7-fc1609d99295\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "c09ceb12-0242-4eed-b1f9-07416475978f", "label": "c09ceb12-0242-4eed-b1f9-07416475978f", "shape": "dot", "title": "ID: c09ceb12-0242-4eed-b1f9-07416475978f\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(53, 103, 178, 0.35833333333333334)", "font": {"color": "black"}, "id": "cc66231a1a9b", "label": "cc66231a1a9b", "shape": "dot", "title": "ID: cc66231a1a9b\nID-Type: device_id\nDegree: 3"}, {"color": "rgba(53, 103, 178, 0.35833333333333334)", "font": {"color": "black"}, "id": "d8d63dac8d42", "label": "d8d63dac8d42", "shape": "dot", "title": "ID: d8d63dac8d42\nID-Type: device_id\nDegree: 3"}, {"color": "rgba(53, 103, 178, 0.35833333333333334)", "font": {"color": "black"}, "id": "d61186783374", "label": "d61186783374", "shape": "dot", "title": "ID: d61186783374\nID-Type: device_id\nDegree: 3"}, {"color": "rgba(53, 103, 178, 0.35833333333333334)", "font": {"color": "black"}, "id": "3aa23c92e2a2", "label": "3aa23c92e2a2", "shape": "dot", "title": "ID: 3aa23c92e2a2\nID-Type: device_id\nDegree: 3"}, {"color": "rgba(53, 103, 178, 0.35833333333333334)", "font": {"color": "black"}, "id": "dfd7297746b0", "label": "dfd7297746b0", "shape": "dot", "title": "ID: dfd7297746b0\nID-Type: device_id\nDegree: 3"}, {"color": "rgba(53, 103, 178, 0.35833333333333334)", "font": {"color": "black"}, "id": "450ba6e99bc6", "label": "450ba6e99bc6", "shape": "dot", "title": "ID: 450ba6e99bc6\nID-Type: device_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.3194444444444444)", "font": {"color": "black"}, "id": "324190ef-a1dc-4153-8a7a-1f61dc3a06e9", "label": "324190ef-a1dc-4153-8a7a-1f61dc3a06e9", "shape": "dot", "title": "ID: 324190ef-a1dc-4153-8a7a-1f61dc3a06e9\nID-Type: anonymous_id\nDegree: 1"}, {"color": "rgba(153, 178, 53, 0.3194444444444444)", "font": {"color": "black"}, "id": "610575ef-102f-4ad6-ad11-ce1ba8eaa7b1", "label": "610575ef-102f-4ad6-ad11-ce1ba8eaa7b1", "shape": "dot", "title": "ID: 610575ef-102f-4ad6-ad11-ce1ba8eaa7b1\nID-Type: anonymous_id\nDegree: 1"}, {"color": "rgba(153, 178, 53, 0.3194444444444444)", "font": {"color": "black"}, "id": "24b39873-2ba1-4e34-b172-eb9b6a086d4e", "label": "24b39873-2ba1-4e34-b172-eb9b6a086d4e", "shape": "dot", "title": "ID: 24b39873-2ba1-4e34-b172-eb9b6a086d4e\nID-Type: anonymous_id\nDegree: 1"}, {"color": "rgba(153, 178, 53, 0.3194444444444444)", "font": {"color": "black"}, "id": "877ee12f-180b-4051-8a25-3bec111f3076", "label": "877ee12f-180b-4051-8a25-3bec111f3076", "shape": "dot", "title": "ID: 877ee12f-180b-4051-8a25-3bec111f3076\nID-Type: anonymous_id\nDegree: 1"}, {"color": "rgba(153, 178, 53, 0.3194444444444444)", "font": {"color": "black"}, "id": "dc4a08da-d493-48b7-beb7-2bc045e6dd2c", "label": "dc4a08da-d493-48b7-beb7-2bc045e6dd2c", "shape": "dot", "title": "ID: dc4a08da-d493-48b7-beb7-2bc045e6dd2c\nID-Type: anonymous_id\nDegree: 1"}, {"color": "rgba(53, 103, 178, 0.35833333333333334)", "font": {"color": "black"}, "id": "71446f27d2a1", "label": "71446f27d2a1", "shape": "dot", "title": "ID: 71446f27d2a1\nID-Type: device_id\nDegree: 3"}, {"color": "rgba(53, 103, 178, 0.35833333333333334)", "font": {"color": "black"}, "id": "f7d072960756", "label": "f7d072960756", "shape": "dot", "title": "ID: f7d072960756\nID-Type: device_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "677571db-4cac-4501-9a14-3dde045673f2", "label": "677571db-4cac-4501-9a14-3dde045673f2", "shape": "dot", "title": "ID: 677571db-4cac-4501-9a14-3dde045673f2\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "b1f5cac8-6cc2-4e4d-81c0-478210da138a", "label": "b1f5cac8-6cc2-4e4d-81c0-478210da138a", "shape": "dot", "title": "ID: b1f5cac8-6cc2-4e4d-81c0-478210da138a\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "823305a7-5740-42b4-b007-29e490e17b08", "label": "823305a7-5740-42b4-b007-29e490e17b08", "shape": "dot", "title": "ID: 823305a7-5740-42b4-b007-29e490e17b08\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "6e6e960d-4166-4a5e-a865-aaec299166b7", "label": "6e6e960d-4166-4a5e-a865-aaec299166b7", "shape": "dot", "title": "ID: 6e6e960d-4166-4a5e-a865-aaec299166b7\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "922d079e-4a67-47a5-b84e-e286242d5c9e", "label": "922d079e-4a67-47a5-b84e-e286242d5c9e", "shape": "dot", "title": "ID: 922d079e-4a67-47a5-b84e-e286242d5c9e\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "8ee77e07-5c95-4540-ba17-5ca052a36720", "label": "8ee77e07-5c95-4540-ba17-5ca052a36720", "shape": "dot", "title": "ID: 8ee77e07-5c95-4540-ba17-5ca052a36720\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "03499e02-dce1-43dd-bf1a-0c73ff75a36e", "label": "03499e02-dce1-43dd-bf1a-0c73ff75a36e", "shape": "dot", "title": "ID: 03499e02-dce1-43dd-bf1a-0c73ff75a36e\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "2fb65df5-633e-47e6-abcd-4496fe47e470", "label": "2fb65df5-633e-47e6-abcd-4496fe47e470", "shape": "dot", "title": "ID: 2fb65df5-633e-47e6-abcd-4496fe47e470\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "66c13c66-5df1-4af1-a38f-ffc0f65ac0cc", "label": "66c13c66-5df1-4af1-a38f-ffc0f65ac0cc", "shape": "dot", "title": "ID: 66c13c66-5df1-4af1-a38f-ffc0f65ac0cc\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "7e3cf9a0-4d7a-4a2b-a905-8385f9523baf", "label": "7e3cf9a0-4d7a-4a2b-a905-8385f9523baf", "shape": "dot", "title": "ID: 7e3cf9a0-4d7a-4a2b-a905-8385f9523baf\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "8ccd8f72-69ca-4e64-a195-adde694b14d3", "label": "8ccd8f72-69ca-4e64-a195-adde694b14d3", "shape": "dot", "title": "ID: 8ccd8f72-69ca-4e64-a195-adde694b14d3\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "97777211-6db6-4532-806d-8e44a7c1f83f", "label": "97777211-6db6-4532-806d-8e44a7c1f83f", "shape": "dot", "title": "ID: 97777211-6db6-4532-806d-8e44a7c1f83f\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "73a88af0-e480-4d7e-9ad4-647d221f273b", "label": "73a88af0-e480-4d7e-9ad4-647d221f273b", "shape": "dot", "title": "ID: 73a88af0-e480-4d7e-9ad4-647d221f273b\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "e843ead3-744f-4d53-bbd0-84c19fca6e87", "label": "e843ead3-744f-4d53-bbd0-84c19fca6e87", "shape": "dot", "title": "ID: e843ead3-744f-4d53-bbd0-84c19fca6e87\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "d39934c4-a029-4fd9-a04e-344ea251e89e", "label": "d39934c4-a029-4fd9-a04e-344ea251e89e", "shape": "dot", "title": "ID: d39934c4-a029-4fd9-a04e-344ea251e89e\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "0415f350-ed54-4037-9fed-40712a77fc43", "label": "0415f350-ed54-4037-9fed-40712a77fc43", "shape": "dot", "title": "ID: 0415f350-ed54-4037-9fed-40712a77fc43\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "22765460-7b19-4f2a-9138-ac601e1a824c", "label": "22765460-7b19-4f2a-9138-ac601e1a824c", "shape": "dot", "title": "ID: 22765460-7b19-4f2a-9138-ac601e1a824c\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "aaf7c363-922b-4443-a7d0-4073750b6f0c", "label": "aaf7c363-922b-4443-a7d0-4073750b6f0c", "shape": "dot", "title": "ID: aaf7c363-922b-4443-a7d0-4073750b6f0c\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "25727c7d-380f-4845-993e-b34406f9330f", "label": "25727c7d-380f-4845-993e-b34406f9330f", "shape": "dot", "title": "ID: 25727c7d-380f-4845-993e-b34406f9330f\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "4e26df5b-b1ac-4964-9f23-979d8237a2b4", "label": "4e26df5b-b1ac-4964-9f23-979d8237a2b4", "shape": "dot", "title": "ID: 4e26df5b-b1ac-4964-9f23-979d8237a2b4\nID-Type: anonymous_id\nDegree: 3"}, {"color": "rgba(153, 178, 53, 0.3194444444444444)", "font": {"color": "black"}, "id": "ddbbbca3-34d7-4e90-b9e5-de9407a9e0c7", "label": "ddbbbca3-34d7-4e90-b9e5-de9407a9e0c7", "shape": "dot", "title": "ID: ddbbbca3-34d7-4e90-b9e5-de9407a9e0c7\nID-Type: anonymous_id\nDegree: 1"}, {"color": "rgba(153, 178, 53, 0.35833333333333334)", "font": {"color": "black"}, "id": "38d72063-56fc-493c-9f27-dd17e58dcedd", "label": "38d72063-56fc-493c-9f27-dd17e58dcedd", "shape": "dot", "title": "ID: 38d72063-56fc-493c-9f27-dd17e58dcedd\nID-Type: anonymous_id\nDegree: 3"}]);
                      edges = new vis.DataSet([{"color": "#888888", "from": "alexkeener@example.com", "to": "887d473fa43c"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "bc854f11fca5"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "65dacdcce759"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "29fc92b6df57"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "akeener"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "64e041ba1b8c"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "f7d3790baeea"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "2cf176c253e7"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "54cb22e5f0a7"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "6848d77e2c51"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "c0ba22140cec"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "77e1b9368bd0"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "34ffd366-5581-404c-9de7-8e20958bd62f"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "1adf0fa5-91a7-4dd3-895e-75799df6bbc6"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "ec58c825-69b5-4406-bb89-189aed588793"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "e9779e82-9943-4039-a8c7-fc1609d99295"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "d8d63dac8d42"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "d61186783374"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "610575ef-102f-4ad6-ad11-ce1ba8eaa7b1"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "877ee12f-180b-4051-8a25-3bec111f3076"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "dc4a08da-d493-48b7-beb7-2bc045e6dd2c"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "71446f27d2a1"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "f7d072960756"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "8097816"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "677571db-4cac-4501-9a14-3dde045673f2"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "823305a7-5740-42b4-b007-29e490e17b08"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "6e6e960d-4166-4a5e-a865-aaec299166b7"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "922d079e-4a67-47a5-b84e-e286242d5c9e"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "66c13c66-5df1-4af1-a38f-ffc0f65ac0cc"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "7e3cf9a0-4d7a-4a2b-a905-8385f9523baf"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "97777211-6db6-4532-806d-8e44a7c1f83f"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "73a88af0-e480-4d7e-9ad4-647d221f273b"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "e843ead3-744f-4d53-bbd0-84c19fca6e87"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "0415f350-ed54-4037-9fed-40712a77fc43"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "1001601"}, {"color": "#888888", "from": "alexkeener@example.com", "to": "4e26df5b-b1ac-4964-9f23-979d8237a2b4"}, {"color": "#888888", "from": "887d473fa43c", "to": "2f41b084-7c53-4ef4-a746-a36c591aabdc"}, {"color": "#888888", "from": "887d473fa43c", "to": "823305a7-5740-42b4-b007-29e490e17b08"}, {"color": "#888888", "from": "887d473fa43c", "to": "1001601"}, {"color": "#888888", "from": "bc854f11fca5", "to": "37dd4c20-6bef-4de6-bedd-c4cc204ff1e1"}, {"color": "#888888", "from": "bc854f11fca5", "to": "1001601"}, {"color": "#888888", "from": "bc854f11fca5", "to": "34ffd366-5581-404c-9de7-8e20958bd62f"}, {"color": "#888888", "from": "65dacdcce759", "to": "1001601"}, {"color": "#888888", "from": "65dacdcce759", "to": "39974b70-b667-4540-8eaa-a91d0e5180a1"}, {"color": "#888888", "from": "65dacdcce759", "to": "677571db-4cac-4501-9a14-3dde045673f2"}, {"color": "#888888", "from": "29fc92b6df57", "to": "1001601"}, {"color": "#888888", "from": "29fc92b6df57", "to": "a207523c-d826-45c5-b104-d2f0a80dda12"}, {"color": "#888888", "from": "29fc92b6df57", "to": "922d079e-4a67-47a5-b84e-e286242d5c9e"}, {"color": "#888888", "from": "akeener", "to": "alicekeener@example.com"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "da21019fe59d"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "2001cbbf1ffd"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "84f9eb766ea0"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "e54e6b399efc"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "1bf9329f6a6e"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "e14211ff4114"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "278e2d59feeb"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "639d42ba6306"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "1001724"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "6758a04b-f52e-432b-9f42-54fb615baa63"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "cc66231a1a9b"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "3aa23c92e2a2"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "dfd7297746b0"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "450ba6e99bc6"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "324190ef-a1dc-4153-8a7a-1f61dc3a06e9"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "24b39873-2ba1-4e34-b172-eb9b6a086d4e"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "8096804"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "b1f5cac8-6cc2-4e4d-81c0-478210da138a"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "8ee77e07-5c95-4540-ba17-5ca052a36720"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "03499e02-dce1-43dd-bf1a-0c73ff75a36e"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "2fb65df5-633e-47e6-abcd-4496fe47e470"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "8ccd8f72-69ca-4e64-a195-adde694b14d3"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "d39934c4-a029-4fd9-a04e-344ea251e89e"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "c09ceb12-0242-4eed-b1f9-07416475978f"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "22765460-7b19-4f2a-9138-ac601e1a824c"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "ddbbbca3-34d7-4e90-b9e5-de9407a9e0c7"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "aaf7c363-922b-4443-a7d0-4073750b6f0c"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "38d72063-56fc-493c-9f27-dd17e58dcedd"}, {"color": "#888888", "from": "alicekeener@example.com", "to": "25727c7d-380f-4845-993e-b34406f9330f"}, {"color": "#888888", "from": "64e041ba1b8c", "to": "efc1aeba-0a0d-40be-a24a-ee393299a480"}, {"color": "#888888", "from": "64e041ba1b8c", "to": "1001601"}, {"color": "#888888", "from": "64e041ba1b8c", "to": "1adf0fa5-91a7-4dd3-895e-75799df6bbc6"}, {"color": "#888888", "from": "56ed43ca-22c3-40cd-858d-3e3711a10395", "to": "1001724"}, {"color": "#888888", "from": "56ed43ca-22c3-40cd-858d-3e3711a10395", "to": "da21019fe59d"}, {"color": "#888888", "from": "1001724", "to": "77f689d8-1d07-4ea2-a34c-a73aa9b76516"}, {"color": "#888888", "from": "1001724", "to": "da21019fe59d"}, {"color": "#888888", "from": "1001724", "to": "2001cbbf1ffd"}, {"color": "#888888", "from": "1001724", "to": "b1f5cac8-6cc2-4e4d-81c0-478210da138a"}, {"color": "#888888", "from": "1001724", "to": "aaf7c363-922b-4443-a7d0-4073750b6f0c"}, {"color": "#888888", "from": "37dd4c20-6bef-4de6-bedd-c4cc204ff1e1", "to": "1001601"}, {"color": "#888888", "from": "1001601", "to": "2f41b084-7c53-4ef4-a746-a36c591aabdc"}, {"color": "#888888", "from": "1001601", "to": "a207523c-d826-45c5-b104-d2f0a80dda12"}, {"color": "#888888", "from": "1001601", "to": "39974b70-b667-4540-8eaa-a91d0e5180a1"}, {"color": "#888888", "from": "1001601", "to": "efc1aeba-0a0d-40be-a24a-ee393299a480"}, {"color": "#888888", "from": "1001601", "to": "677571db-4cac-4501-9a14-3dde045673f2"}, {"color": "#888888", "from": "1001601", "to": "34ffd366-5581-404c-9de7-8e20958bd62f"}, {"color": "#888888", "from": "1001601", "to": "1adf0fa5-91a7-4dd3-895e-75799df6bbc6"}, {"color": "#888888", "from": "1001601", "to": "823305a7-5740-42b4-b007-29e490e17b08"}, {"color": "#888888", "from": "1001601", "to": "922d079e-4a67-47a5-b84e-e286242d5c9e"}, {"color": "#888888", "from": "61e3bcdc-d995-41d9-a6aa-1172af68f104", "to": "8096804"}, {"color": "#888888", "from": "61e3bcdc-d995-41d9-a6aa-1172af68f104", "to": "84f9eb766ea0"}, {"color": "#888888", "from": "8096804", "to": "dcf6d0f9-3710-4f97-98cb-75288033c56d"}, {"color": "#888888", "from": "8096804", "to": "1bf9329f6a6e"}, {"color": "#888888", "from": "8096804", "to": "84f9eb766ea0"}, {"color": "#888888", "from": "8096804", "to": "c09ceb12-0242-4eed-b1f9-07416475978f"}, {"color": "#888888", "from": "8096804", "to": "639d42ba6306"}, {"color": "#888888", "from": "8096804", "to": "dfd7297746b0"}, {"color": "#888888", "from": "8096804", "to": "8ccd8f72-69ca-4e64-a195-adde694b14d3"}, {"color": "#888888", "from": "8096804", "to": "6758a04b-f52e-432b-9f42-54fb615baa63"}, {"color": "#888888", "from": "8096804", "to": "25727c7d-380f-4845-993e-b34406f9330f"}, {"color": "#888888", "from": "8096804", "to": "d39934c4-a029-4fd9-a04e-344ea251e89e"}, {"color": "#888888", "from": "8096804", "to": "cc66231a1a9b"}, {"color": "#888888", "from": "8096804", "to": "e54e6b399efc"}, {"color": "#888888", "from": "8096804", "to": "278e2d59feeb"}, {"color": "#888888", "from": "8096804", "to": "e14211ff4114"}, {"color": "#888888", "from": "8096804", "to": "8ee77e07-5c95-4540-ba17-5ca052a36720"}, {"color": "#888888", "from": "8096804", "to": "2fb65df5-633e-47e6-abcd-4496fe47e470"}, {"color": "#888888", "from": "8096804", "to": "03499e02-dce1-43dd-bf1a-0c73ff75a36e"}, {"color": "#888888", "from": "8096804", "to": "22765460-7b19-4f2a-9138-ac601e1a824c"}, {"color": "#888888", "from": "8096804", "to": "3aa23c92e2a2"}, {"color": "#888888", "from": "8096804", "to": "450ba6e99bc6"}, {"color": "#888888", "from": "8096804", "to": "38d72063-56fc-493c-9f27-dd17e58dcedd"}, {"color": "#888888", "from": "da21019fe59d", "to": "aaf7c363-922b-4443-a7d0-4073750b6f0c"}, {"color": "#888888", "from": "77f689d8-1d07-4ea2-a34c-a73aa9b76516", "to": "2001cbbf1ffd"}, {"color": "#888888", "from": "2001cbbf1ffd", "to": "b1f5cac8-6cc2-4e4d-81c0-478210da138a"}, {"color": "#888888", "from": "3407e0e3-4900-497c-bff8-8d370754e3ee", "to": "8097816"}, {"color": "#888888", "from": "3407e0e3-4900-497c-bff8-8d370754e3ee", "to": "c0ba22140cec"}, {"color": "#888888", "from": "8097816", "to": "c0ba22140cec"}, {"color": "#888888", "from": "8097816", "to": "6848d77e2c51"}, {"color": "#888888", "from": "8097816", "to": "77e1b9368bd0"}, {"color": "#888888", "from": "8097816", "to": "d8d63dac8d42"}, {"color": "#888888", "from": "8097816", "to": "4e26df5b-b1ac-4964-9f23-979d8237a2b4"}, {"color": "#888888", "from": "8097816", "to": "e9779e82-9943-4039-a8c7-fc1609d99295"}, {"color": "#888888", "from": "8097816", "to": "ec58c825-69b5-4406-bb89-189aed588793"}, {"color": "#888888", "from": "8097816", "to": "f7d3790baeea"}, {"color": "#888888", "from": "8097816", "to": "d61186783374"}, {"color": "#888888", "from": "8097816", "to": "54cb22e5f0a7"}, {"color": "#888888", "from": "8097816", "to": "2cf176c253e7"}, {"color": "#888888", "from": "8097816", "to": "f7d072960756"}, {"color": "#888888", "from": "8097816", "to": "71446f27d2a1"}, {"color": "#888888", "from": "8097816", "to": "6e6e960d-4166-4a5e-a865-aaec299166b7"}, {"color": "#888888", "from": "8097816", "to": "e843ead3-744f-4d53-bbd0-84c19fca6e87"}, {"color": "#888888", "from": "8097816", "to": "73a88af0-e480-4d7e-9ad4-647d221f273b"}, {"color": "#888888", "from": "8097816", "to": "7e3cf9a0-4d7a-4a2b-a905-8385f9523baf"}, {"color": "#888888", "from": "8097816", "to": "97777211-6db6-4532-806d-8e44a7c1f83f"}, {"color": "#888888", "from": "8097816", "to": "0415f350-ed54-4037-9fed-40712a77fc43"}, {"color": "#888888", "from": "8097816", "to": "66c13c66-5df1-4af1-a38f-ffc0f65ac0cc"}, {"color": "#888888", "from": "dcf6d0f9-3710-4f97-98cb-75288033c56d", "to": "1bf9329f6a6e"}, {"color": "#888888", "from": "1bf9329f6a6e", "to": "d39934c4-a029-4fd9-a04e-344ea251e89e"}, {"color": "#888888", "from": "c0ba22140cec", "to": "e9779e82-9943-4039-a8c7-fc1609d99295"}, {"color": "#888888", "from": "f7d3790baeea", "to": "73a88af0-e480-4d7e-9ad4-647d221f273b"}, {"color": "#888888", "from": "2cf176c253e7", "to": "4e26df5b-b1ac-4964-9f23-979d8237a2b4"}, {"color": "#888888", "from": "84f9eb766ea0", "to": "8ee77e07-5c95-4540-ba17-5ca052a36720"}, {"color": "#888888", "from": "54cb22e5f0a7", "to": "97777211-6db6-4532-806d-8e44a7c1f83f"}, {"color": "#888888", "from": "6848d77e2c51", "to": "6e6e960d-4166-4a5e-a865-aaec299166b7"}, {"color": "#888888", "from": "e54e6b399efc", "to": "22765460-7b19-4f2a-9138-ac601e1a824c"}, {"color": "#888888", "from": "77e1b9368bd0", "to": "ec58c825-69b5-4406-bb89-189aed588793"}, {"color": "#888888", "from": "e14211ff4114", "to": "38d72063-56fc-493c-9f27-dd17e58dcedd"}, {"color": "#888888", "from": "278e2d59feeb", "to": "03499e02-dce1-43dd-bf1a-0c73ff75a36e"}, {"color": "#888888", "from": "639d42ba6306", "to": "c09ceb12-0242-4eed-b1f9-07416475978f"}, {"color": "#888888", "from": "6758a04b-f52e-432b-9f42-54fb615baa63", "to": "3aa23c92e2a2"}, {"color": "#888888", "from": "cc66231a1a9b", "to": "8ccd8f72-69ca-4e64-a195-adde694b14d3"}, {"color": "#888888", "from": "d8d63dac8d42", "to": "e843ead3-744f-4d53-bbd0-84c19fca6e87"}, {"color": "#888888", "from": "d61186783374", "to": "66c13c66-5df1-4af1-a38f-ffc0f65ac0cc"}, {"color": "#888888", "from": "dfd7297746b0", "to": "25727c7d-380f-4845-993e-b34406f9330f"}, {"color": "#888888", "from": "450ba6e99bc6", "to": "2fb65df5-633e-47e6-abcd-4496fe47e470"}, {"color": "#888888", "from": "71446f27d2a1", "to": "7e3cf9a0-4d7a-4a2b-a905-8385f9523baf"}, {"color": "#888888", "from": "f7d072960756", "to": "0415f350-ed54-4037-9fed-40712a77fc43"}]);
    
                      nodeColors = {};
                      allNodes = nodes.get({ returnType: "Object" });
                      for (nodeId in allNodes) {
                        nodeColors[nodeId] = allNodes[nodeId].color;
                      }
                      allEdges = edges.get({ returnType: "Object" });
                      // adding nodes and edges to the graph
                      data = {nodes: nodes, edges: edges};
    
                      var options = {"physics": {"forceAtlas2Based": {"gravitationalConstant": -50, "centralGravity": 0.01, "springLength": 100, "springConstant": 0.08}, "minVelocity": 0.75, "solver": "forceAtlas2Based"}, "nodes": {"font": {"color": "black"}, "borderWidth": 2, "borderWidthSelected": 4}, "edges": {"color": {"inherit": false}, "smooth": {"enabled": true, "type": "dynamic"}}};
    
                      network = new vis.Network(container, data, options);
    
                      return network;
                  }
                  drawGraph();
            </script>
        </body>
    </html>
    

  


In the above project, there is a resolved ID that appears to have two users merged together. Note that `user_main_id` had 2 emails (`alexkeener@example.com` and `alicekeener@example.com`) within. Upon running the visualizer on this `main_id` \- you can see that both the users associated with the emails share the same `user_id` (`akeener`). With this knowledge, you can quickly make changes to the Profiles configuration to unstitch these users or fix the source data.

[![Cluster analysis sample graph](/docs/images/profiles/cluster-analysis-sample-graph.webp)](</docs/images/profiles/cluster-analysis-sample-graph.webp>)

## Interactive LLM session

> ![info](/docs/images/info.svg)
> 
> RudderStack supports this feature only for the Snowflake warehouse currently. Support for the other warehouses is coming soon.

The audit tool also provides an open-ended text2sql session where you can ask arbitrary questions related to the ID graph. The question goes to an LLM which prepares a SQL query.

The SQL query then runs on your data warehouse and generates an answer.

**Click here to view a sample**  

    
    
     Question:
            how many accounts do we have with more than one domain?
    
    Thought:
            Ran following queries to get the answer:
    
            SELECT COUNT(*) AS accounts_with_multiple_domains
    FROM (
        SELECT ACCOUNT_MAIN_ID
        FROM account_id_graph
        WHERE other_id_type = 'domain'
        GROUP BY ACCOUNT_MAIN_ID
        HAVING COUNT(DISTINCT other_id) > 1
    ) subquery;;
    
            SELECT COUNT(DISTINCT ACCOUNT_MAIN_ID) AS total_accounts_with_domains
    FROM account_id_graph
    WHERE other_id_type = 'domain';;
    
    Response:
    
    Now we have more context to provide a comprehensive answer:
    
    There are 100 accounts that have more than one domain associated with them. This is out of a total of 25,000 accounts that have at least one domain.
    
    To put this into perspective:
    - Approximately 0.50% of accounts with domains (100 out of 25,000) have multiple domains associated with them.
    - The vast majority (about 99.75%) of accounts with domains are associated with just a single domain.
    
    This distribution suggests that while most accounts in the system are linked to a single domain, there is a small but significant number of accounts that operate across multiple domains. These could represent larger organizations, companies with multiple brands, or entities that have expanded their online presence across different domain names.
    
    You can ask next question, type exit to quit, or back to select a different entity
    
    Q: what are these accounts? why do they have multiple domains?
    INFO:api_server.sessions.chat_session@2024-09-30 11:02:28,987: Getting response for prompt: what are these accounts? why do they have multiple domains?
    INFO:api_server.sessions.chat_session@2024-09-30 11:02:28,988: Converted history to prompt
    INFO:api_server.sessions.chat_session@2024-09-30 11:02:28,988: Making llm calls with the extended prompt
    
    Response: 
    
    Based on the query results, we can answer the user's question:
    
    These are the top 10 accounts with multiple domains, ordered by the number of domains they have:
    
    1. An account (ACCOUNT_MAIN_ID: rid0a615df48d4ae923f518ab3d052ded1f) with 8 domains, including <domain1>, <domain2>, <domain3>, and others.
    2. Apex (ACCOUNT_MAIN_ID: rid7492d64d982d1e6b8531e12a39513d6e) with 4 domains across different countries.
    3. Aurora (ACCOUNT_MAIN_ID: rid149ba1fd2a2c59b30663fb22d4aabfaa) with 4 domains in different countries.
    4. Acme (ACCOUNT_MAIN_ID: rid49a8de71ef3cbe73d0359965e000a20b) with 3 domains in different Nordic countries.
    5. A company (ACCOUNT_MAIN_ID: rid0a256a02fc2aaf3bf812db4df78b95fa) with 3 domains.
    6. Clement (ACCOUNT_MAIN_ID: rid44cb9148b8c8b5b608d5a8ecebc11e4b) with 3 related domains.
    7. Hero (ACCOUNT_MAIN_ID: rid301a9453dddc0bca3a7315af38370c3e) with 3 domains in different countries.
    8. Buffalo (ACCOUNT_MAIN_ID: rid0c22fb973e9b75dd2356072f29c4f91e) with 3 related domains.
    9. Majority (ACCOUNT_MAIN_ID: rid5d63f8165e5fa418cef359f0dcde888a) with 2 domains.
    10. Super (ACCOUNT_MAIN_ID: rid21bb08ad7fd688b23e43d00b0b54d3c0) with 2 domains.
    
    As for why these accounts have multiple domains, we can infer several reasons based on the patterns observed:
    
    1. International presence: Companies like Apex, Aurora, Acme, and Buffalo have domains for different countries or regions.
    
    2. Brand diversification: The first account with 8 domains seems to represent multiple brands or services under one parent company.
    
    ...response continued...
    
    These multiple domains allow companies to tailor their online presence to different markets, products, or strategies while maintaining a unified backend infrastructure for user identification and data management.
    

  


### Privacy policy

For an interactive LLM session, RudderStack sends the user prompt and some data (for example, table and column names, SQL query response, etc.) to an external LLM service.

RudderStack currently uses two LLM service providers:

  * OpenAI (Privacy policy: [here](<https://platform.openai.com/docs/models/default-usage-policies-by-endpoint#how-we-use-your-data>))
  * Anthropic (Privacy policy: [here](<https://privacy.anthropic.com/en/articles/10023548-how-long-do-you-store-personal-data>))


> ![warning](/docs/images/warning.svg)
> 
> Both the OpenAI and Anthropic privacy policies state that the data in APIs is retained for 30 days to monitor for any policy violations.
> 
> It **will not be used** for training purposes and **will be deleted** after 30 days.

The tool asks for your consent to use these LLMs **before** making the first LLM call. You can opt out of the LLM services if there are concerns about sending your data to the external providers.

> ![info](/docs/images/info.svg)
> 
> If you opt out of the LLM services, the audit tool never makes any calls to the LLM provider.

Any consent you provide (opt-in or opt-out) is stored locally in the `~/.pb/preferences.yaml` file on the same device and gets reused in all the future profiles audit runs.

To reset your consent, manually delete the consent from the `~/.pb/preferences.yaml` file.

## Tracking

Note that for every command run, the tool tracks the `audit_start` and `audit_end` events.

It creates an `anonymous_id` in the `~/.pb/preferences.yaml` file and uses this ID for future runs. All the runs get associated with this ID. On the very first run when `anonymous_id` is created, you will see the following disclaimer:
    
    
      Privacy Policy regarding Telemetry:
      - This tool collects usage statistics to help us improve the product.
      - We do not collect or store any sensitive information from your models.
      - You can opt out by adding 'telemetry_opted_out: true' to ~/.pb/preferences.yaml
    

> ![info](/docs/images/info.svg)
> 
> The audit tool also collects the IP address of the device as a part of the standard RudderStack call. However, it **does not** collect any other user identifier.

You can add a line `telemetry_opted_out: true` in this preference file to **opt out** of tracking.

## FAQ

See the FAQs on [Python-related errors](<https://www.rudderstack.com/docs/archive/profiles/0.21/additional-resources/faq/#python-related-errors>) for more information.

  


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.21/dev-docs/activation-api/v1/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.21/dev-docs/commands/>)