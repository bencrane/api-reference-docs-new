# Transformation Action

Create, test, and publish JavaScript/Python transformations and libraries directly from your development repository.

* * *

  * __4 minute read

  * 


RudderStack’s [Transformation Action](<https://github.com/rudderlabs/rudder-transformation-action-code/>) lets you create, update, test, and publish transformations and libraries written in JavaScript or Python - directly from your development repository. Internally, this action leverages the [Transformations API](<https://www.rudderstack.com/docs/api/transformation-api/>).

> ![info](/docs/images/info.svg)
> 
> This action is currently available for GitHub only.

## Prerequisites

  * You will need the email address associated with your RudderStack workspace.
  * In your RudderStack workspace, create a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#generate-service-access-token>) with the following [permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>):

Resource| Permission| Description  
---|---|---  
Transformations| **Edit**|  Make changes to the configuration of transformations  
Transformations| **Connect**|  Connect a transformation to a destination  
Transformations| **Create & Delete**| Create or delete transformations  
Transformation Libraries| **Edit**|  Make changes to the configuration of transformation libraries  
  
**Click here to see how these permissions appear in the workspace policy**.  
![RudderStack permissions for SAT](/docs/images/data-governance/transformation-action-sat-permissions.webp)  


> ![warning](/docs/images/warning.svg)
> 
> For security purposes, RudderStack recommends using [GitHub secrets](<https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository>) to store your Service Access Token.

#### Token permissions for legacy RBAC system

If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), your workspace-level Service Access Token should have **Admin** role with **Grant edit access** setting toggled on under **Transformations**.

See [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for more information on generating the token.

[![workspace-level Service Access Token with Transformations Admin permission](/docs/images/access-management/permissions/legacy/admin-transformations.webp)](</docs/images/access-management/permissions/legacy/admin-transformations.webp>)

## Usage

> ![info](/docs/images/info.svg)
> 
> See the [sample workflow](<https://github.com/rudderlabs/rudder-transformation-action-code/blob/main/.github/workflows/rudderTransformation.yml>) for more information on using the action.
    
    
    name: RudderStack Transformer Test and Publish
    uses: rudderlabs/rudder-transformation-action@<current_action_version>
    with:
        metaPath: './code/meta.json'
        email: 'test@rudderlabs.com'
        accessToken: ${{ secrets.ACCESS_TOKEN }}
        uploadTestArtifact: true
    

Specify the email address and Service Access Token obtained in the Prerequisites section in the `email` and `accessToken` fields respectively.

See FAQ for more information on the `uploadTestArtifact` parameter.

## Action fields

Field| Description  
---|---  
`metapath`Required| Path to the meta file that:  
  


  * Lets the action know about what transformations/libraries to test based on the input events and the expected output.
  * Publishes the transformations/libraries if the test passes.

See Meta file structure for more information.  
`email`Required| Email address associated with the RudderStack workspace.  
`accessToken`Required| Your Service Access Token obtained from the RudderStack dashboard.  
`uploadTestArtifact`| Boolean flag that determines:  
  


  * Whether to upload the individual transformation outputs after running the transformation on the test events.
  * The difference from the expected output.

See `uploadTestArtifact` parameter for more information.  
  
**Default value** : False  
  
## Meta file structure

As mentioned above, a meta file lets the transformation action know what transformations or libraries to test depending on the input events and the expected output.

A generic meta file schema is shown below:
    
    
    // Meta file schema
    {
      "transformations": <array of transformation schema>,
      "libraries": <array of library schema>
    }
    

A sample meta file is shown below:
    
    
     // example meta.json
     {
       "transformations": [
        {
           "file": "./code/t1.js",
           "name": "action-T1",
           "language": "javascript",
           "description": "action-T1",
           "test-input-file": "./code/testevents.json",
           "expected-output": "./code/expectedoutput.json"
         },
         {
           "file": "./code/t2.py",
           "name": "action-T2",
           "language": "pythonfaas",
           "description": "action-T2",
           "test-input-file": "./code/events.json",
           "expected-output": "./code/expected.json"
         }
       ],
       "libraries": [{
           "file": "./code/lib1.js",
           "name": "lib1",
           "language": "javascript",
           "description": "action-lib1"
         },
         {
           "file": "./code/lib2.py",
           "name": "getFinanceDataPy",
           "language": "pythonfaas",
           "description": "Python library to get finance data"
         }
       ]
     }
    

> ![warning](/docs/images/warning.svg)
> 
> The path mentioned in the `file` field should be relative to the base repository path.

### Transformation schema

The `transformations` parameter in the meta file contains an array of transformation schemas. A single transformation schema contains the following parameters:

Parameter| Description  
---|---  
`file`Required| Path to the transformation code.  
`name`Required| Transformation name.  
`language`Required| Transformation language. Permissible values are `javascript` and `pythonfaas`.  
`description`| Transformation description.  
`test-input-file`| Path to the JSON file containing an array of events to test the transformation.  
`expected-output`| Path to the JSON file containing the expected output for the above input, after running the transformation code.  
  
### Library schema

The `libraries` parameter in the meta file contains an array of library schemas. A single library schema contains the following parameters:

Parameter| Description  
---|---  
`file`Required| Path to the library code.  
`name`Required| Library name that you must specify to import it in any transformation.  
`language`Required| Library language. Permissible values are `javascript` and `pythonfaas`.  
`description`| Library description.  
  
## FAQ

#### **How do I use the`uploadTestArtifact` parameter?**

When you set `uploadTestArtifact` to `true` in the transformation action, RudderStack:

  1. Runs the transformation on the test events present in `test-input-file`.
  2. Generates and stores the output in a **test-outputs** folder contained within a zipped artifact.
  3. Validates the output against the contents of the file specified in `expected-output`.


> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * RudderStack stores the output from Step 1 in a `[transformation name in camel case]_output.json` file.
>   * It stores the validation differences from Step 3 in the respective `[transformation name in camel case]_diff.json` file.
>   * If you do not set `uploadTestArtifact` to `true` in the transformation action, RudderStack **does not** create the output zip containing the above files.
> 

> 
> For more context, see the use case below.

Consider the following transformation schema:
    
    
    // single transformationSchema
    {
      "file": "./code/t1.js",
      "name": "action-T1",
      "language": "javascript",
      "description": "action-T1",
      "test-input-file": "./code/testevents.json",
      "expected-output": "./code/expectedoutput.json"
    }
    

The workflow when you set `uploadTestArtifact` to `true` is as follows:

  1. RudderStack runs the transformation `action-T1`(with its code present in `t1.js`) on the `testevents.json` file.

  2. RudderStack then:

     1. Generates and stores the output from Step 1 in a file named `actionT1_output.json`. This file is stored in a **test-outputs** folder contained within a zipped artifact.
     2. Validates the output with the contents present in the `expectedoutput.json` file. It stores any differences in a file named `actionT1_diff.json`.


> ![info](/docs/images/info.svg)
> 
> The **test-outputs** folder contains the two files - `actionT1_output.json` and `actionT1_diff.json`.

##### [How to Deploy RudderStack Transformations with GitHub Actions](</docs/transformations/transformation-action/github-actions/>)

Automate transformation testing and deployment with GitHub Actions.