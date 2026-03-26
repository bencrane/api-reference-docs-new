# Transformations Management Using Rudder CLI Quickstart Alpha

Learn how to manage transformations and transformation libraries using Rudder CLI.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __4 minute read

  * 


In this quickstart, you will use the [Rudder CLI tool](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/>) to define, validate, test, and apply transformations from your local project.

## Prerequisites

  * Rudder CLI tool (`rudder-cli`) [installed locally](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/installation/>)
  * In your RudderStack workspace, create a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) with the following permissions:

Resource| Permissions  
---|---  
Transformations| **Edit** , **Connect** , **Create & Delete**  
Transformation Libraries| **Edit**  
  
  * **For testing purposes only** : [Personal Access Token](<https://www.rudderstack.com/docs/access-management/personal-access-tokens/>) with minimum **Read-Write** role
  * A project directory with your transformation YAML files


#### Token permissions for legacy RBAC system

If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), your workspace-level Service Access Token should have the **Admin** role and **Grant edit access** toggled on under **Transformations**.

See [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for more information on generating the token.

[![workspace-level Service Access Token with Transformations Admin permission](/docs/images/access-management/permissions/legacy/admin-transformations.webp)](</docs/images/access-management/permissions/legacy/admin-transformations.webp>)

## 1\. Authenticate the CLI tool

Run the following command and enter your access token when prompted:
    
    
    rudder-cli auth login
    

## 2\. Create a project directory

Create a project directory to store your transformation specs, code, and tests:
    
    
    mkdir -p ~/tutorial-transformations/transformations
    

Example structure:
    
    
    tutorial-transformations/
    └── transformations/
        ├── my-transformation.yaml
        ├── my-library.yaml
        ├── my-python-transformation.yaml
        ├── my-python-library.yaml
        ├── javascript/
        │   ├── my-transformation.js
        │   └── my-library.js
        ├── python/
        │   ├── my-python-transformation.py
        │   └── my-python-library.py
        └── tests/
            ├── input/
            │   └── product_clicked.json
            └── output/
                └── product_clicked.json
    

> ![announcement](/docs/images/announcement.svg)
> 
> RudderStack supports Python transformation libraries only in the [Growth](<https://rudderstack.com/pricing/>) and [Enterprise](<https://www.rudderstack.com/enterprise-quote/>) plans.

## 3\. Add a transformation spec

This section lists the steps to create a transformation YAML spec via the following methods:

  * Referencing an external file
  * Using inline code


#### Referencing an external file

  1. Create the YAML spec for your transformation:


`~/tutorial-transformations/transformations/my-transformation.yaml`:
    
    
    version: rudder/v1
    kind: transformation
    metadata:
      name: my-transformation
    spec:
      id: my-transformation
      name: My Transformation
      description: Add static metadata to each incoming event
      language: javascript
      file: javascript/my-transformation.js
      tests:
        - name: Basic payload test
          input: tests/input
          output: tests/output
    

`~/tutorial-transformations/transformations/my-python-transformation.yaml`:
    
    
    version: rudder/v1
    kind: transformation
    metadata:
      name: my-python-transformation
    spec:
      id: my-python-transformation
      name: My Python Transformation
      description: Tag each incoming event with a processing timestamp
      language: python
      file: python/my-python-transformation.py
      tests:
        - name: Basic payload test
          input: ./tests/input
          output: ./tests/output
    

  2. Create the transformation code file:


`~/tutorial-transformations/transformations/javascript/my-transformation.js`:
    
    
    export function transformEvent(event, metadata) {
      event.context = event.context || {};
      event.context.cliManaged = true;
      return event;
    }
    

`~/tutorial-transformations/transformations/python/my-python-transformation.py`:
    
    
    from datetime import datetime, timezone
    
    def transformEvent(event, metadata):
        event.setdefault("context", {})
        event["context"]["processedAt"] = datetime.now(timezone.utc).isoformat()
        return event
    

#### Using inline code

You can also write transformation code directly in the YAML spec using `code` instead of referencing an external file with `file`:
    
    
    version: rudder/v1
    kind: transformation
    metadata:
      name: inline-transformation
    spec:
      id: inline-transformation
      name: Inline Transformation
      description: Add processing metadata to each event
      language: javascript
      code: |
        export function transformEvent(event, metadata) {
          event.context = event.context || {};
          event.context.processedBy = "inline-transformation";
          return event;
        }    
    
    
    
    version: rudder/v1
    kind: transformation
    metadata:
      name: inline-python-transformation
    spec:
      id: inline-python-transformation
      name: Inline Python Transformation
      description: Add processing metadata to each event
      language: python
      code: |
        def transformEvent(event, metadata):
            event.setdefault("context", {})
            event["context"]["processedBy"] = "inline-python-transformation"
            return event    
    

> ![info](/docs/images/info.svg)
> 
> `code` and `file` are mutually exclusive — use one or the other in a given spec. See the [Transformation YAML Reference](<https://www.rudderstack.com/docs/transformations/manage-transformations-with-rudder-cli/transformation-yaml-reference/>) for the complete schema.

## 4\. Add a transformation library spec

Create the YAML spec for your transformation library:

`~/tutorial-transformations/transformations/my-library.yaml`:
    
    
    version: rudder/v1
    kind: transformation-library
    metadata:
      name: my-library
    spec:
      id: my-library
      name: my library
      description: Shared helper utilities
      language: javascript
      file: javascript/my-library.js
      import_name: myLibrary
    

`~/tutorial-transformations/transformations/my-python-library.yaml`:
    
    
    version: rudder/v1
    kind: transformation-library
    metadata:
      name: my-python-library
    spec:
      id: my-python-library
      name: my python library
      description: Shared Python helper utilities
      language: python
      file: python/my-python-library.py
      import_name: myPythonLibrary
    

Then, create the library code file:

`~/tutorial-transformations/transformations/javascript/my-library.js`:
    
    
    export function addTag(event, key, value) {
      event.context = event.context || {};
      event.context[key] = value;
      return event;
    }
    

`~/tutorial-transformations/transformations/python/my-python-library.py`:
    
    
    def add_tag(event, key, value):
        event.setdefault("context", {})
        event["context"][key] = value
        return event
    

> ![info](/docs/images/info.svg)
> 
> For library resources, `import_name` must be the camelCase form of `name`. For example, `name: my library` maps to `import_name: myLibrary` and `name: my python library` maps to `import_name: myPythonLibrary`.

## 5\. Validate YAML and code references

Run validation from the project root:
    
    
    rudder-cli validate -l ~/tutorial-transformations
    

This command validates required fields, `code`/`file` rules, supported languages, code syntax, and test definitions.

## 6\. Test transformations locally

Rudder CLI supports 3 test modes:

> ![warning](/docs/images/warning.svg)
> 
> You cannot include multiple test modes in a single command.

  1. Test a specific transformation by ID:


    
    
    rudder-cli transformations test my-transformation -l ~/tutorial-transformations
    

  2. Test all transformations:


    
    
    rudder-cli transformations test --all -l ~/tutorial-transformations
    

  3. Test only new or modified transformations:


    
    
    rudder-cli transformations test --modified -l ~/tutorial-transformations
    

**Optional**

  * Show detailed failures and diffs:


    
    
    rudder-cli transformations test --all --verbose -l ~/tutorial-transformations
    

  * Show the built-in default events:


    
    
    rudder-cli transformations show-default-events
    

#### How it works

When running tests, Rudder CLI loads input files from each test suite’s `input` path. If a matching output file (same filename) exists in the `output` path, it compares the actual output against the expected output. If no matching output file exists, the test still runs but skips the output comparison.

> ![info](/docs/images/info.svg)
> 
> Rudder CLI tests the transformation using default RudderStack events if:
> 
>   * `spec.tests` isn’t configured, or
>   * No input JSON files are found in the configured input paths
> 


See the [Rudder CLI transformations testing framework](<https://www.rudderstack.com/docs/transformations/manage-transformations-with-rudder-cli/transformation-yaml-reference/#testing-framework>) section for more details.

## 7\. Apply changes

  1. Optional dry-run:


    
    
    rudder-cli apply -l ~/tutorial-transformations --dry-run
    

  2. Apply to workspace:


    
    
    rudder-cli apply -l ~/tutorial-transformations
    

## Next steps

  * See the [Transformation YAML Reference](<https://www.rudderstack.com/docs/transformations/manage-transformations-with-rudder-cli/transformation-yaml-reference/>) for detailed resource schemas and constraints
  * See [Manage Transformations Using Rudder CLI](<https://www.rudderstack.com/docs/transformations/manage-transformations-with-rudder-cli/>) for the overall CLI workflow