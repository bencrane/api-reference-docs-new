# Transformation YAML Reference Alpha

Complete YAML reference for transformation and transformation-library resources managed with Rudder CLI.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __3 minute read

  * 


This guide provides a complete YAML reference for managing transformation resources using Rudder CLI.

## Overview

You can define transformation resources in YAML files anywhere inside your CLI project directory. Rudder CLI scans the project recursively and processes valid resource files.

Supported resource kinds for this workflow:

  * `transformation`
  * `transformation-library`


## Transformation resource

Use `kind: transformation` to define a transformation.

### `spec` properties

Property| Type| Description  
---|---|---  
`id`  
Required| String| Unique project ID for the transformation.  
`name`  
Required| String| Human-readable name. Must be non-empty.  
`language`  
Required| String| Transformation language. Allowed values: `javascript`, `python`.  
`description`| String| Optional description.  
`code`| String| Inline transformation code containing valid syntax for the selected language. Mutually exclusive with `file`.  
`file`| String| Path to transformation code file. Note that:  
  


  * The referenced file must exist and be readable.
  * Relative paths are resolved from the YAML spec’s parent directory.


> ![warning](/docs/images/warning.svg)One of `code` or `file` is required.  
  
`tests`| Array| Optional list of local test suites. These tests are used only by [`rudder-cli transformations test`](<https://www.rudderstack.com/docs/transformations/manage-transformations-with-rudder-cli/#test-transformations-locally>) and are not synced to workspace state during [`rudder-cli apply`](<https://www.rudderstack.com/docs/transformations/manage-transformations-with-rudder-cli/#apply-changes>).  
  
### `tests` properties

Property| Type| Description  
---|---|---  
`name`  
Required| String| Test suite name. Must be non-empty and can contain only letters, numbers, spaces, `_`, `-`, and `/`.  
`input`| String| Directory with JSON input payload files. Relative paths resolve from the spec directory. If omitted, default is `./input`.  
`output`| String| Directory with expected output JSON files. Relative paths resolve from the spec directory. If omitted, default is `./output`.  
  
> ![info](/docs/images/info.svg)
> 
> Rudder CLI tests the transformation using default RudderStack events if:
> 
>   * `spec.tests` is not configured, or
>   * No input JSON files are found in the specified `input` path
> 


## Transformation library resource

Use `kind: transformation-library` to define a reusable transformation library.

### `spec` properties

Property| Type| Description  
---|---|---  
`id`  
Required| String| Unique project ID for the library.  
`name`  
Required| String| Human-readable name — must be non-empty.  
`description`| String| Optional description.  
`language`  
Required| String| Library language. Allowed values are `javascript` and `python`.  
`code`| String| Inline library code containing valid syntax for the selected language. Mutually exclusive with `file`.  
`file`| String| Path to library code file. Note that:  
  


  * The referenced file must exist and be readable.
  * Relative paths are resolved from the YAML spec’s parent directory.


> ![warning](/docs/images/warning.svg)One of `code` or `file` is required.  
  
`import_name`  
Required| String| Handle used when importing the library in transformation code — must be camelCase of `name`.  
  


> ![warning](/docs/images/warning.svg)Validation fails if `import_name` does not match the camelCase form of `name`.  
  
## Testing framework

Rudder CLI includes a rich built-in testing framework for validating transformations and transformation libraries locally.

### Structure

The testing framework uses input and output directories to run test cases:

  * All files in the `input` directory are treated as test inputs
  * Corresponding files in the `output` directory are used as expected outputs for comparison against the actual transformation results


> ![warning](/docs/images/warning.svg)
> 
> Input and output file names must match for accurate testing and comparison.

For each test case, the framework sends the input event through the transformation and compares the actual output against the expected output.

### Test modes

The testing framework supports two modes:

Mode| Description  
---|---  
Default| Displays minimal details about test results.  
`--verbose`| Displays more context around differences, including three lines above and below each code diff.  
  
### Test result classification

Each input file represents a separate test case. Rudder CLI classifies transformation test results into the following categories:

Result| Description  
---|---  
Passed| The actual output matches the expected output. If the expected output is missing, then a successful execution is considered as passed.  
Execution error| The transformation code encountered an error during execution.  
Output mismatch error| The actual output doesn’t match the expected output.  
  
> ![info](/docs/images/info.svg)
> 
> Transformation library tests focus specifically on syntax validation.

## See more

  * See [Transformations Management Using Rudder CLI Quickstart](<https://www.rudderstack.com/docs/transformations/manage-transformations-with-rudder-cli/quickstart/>) for a complete end-to-end example
  * See [Manage Transformations Using Rudder CLI](<https://www.rudderstack.com/docs/transformations/manage-transformations-with-rudder-cli/>) for the overall feature overview