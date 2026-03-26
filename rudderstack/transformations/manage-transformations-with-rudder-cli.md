# Manage Transformations Using Rudder CLI Alpha

Define, validate, test, and apply transformations and transformation libraries as YAML configurations using Rudder CLI.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __2 minute read

  * 


> ![announcement](/docs/images/announcement.svg)
> 
> This feature is in **Alpha** as part of RudderStack’s [Early Access Program](<https://www.rudderstack.com/docs/get-started/alpha-and-beta-features/alpha-features/>), where we work with early users and customers to test new features and get feedback before making them generally available. Note that these features are functional but can change as we improve them.
> 
> [Contact the Product team](<mailto:product@rudderstack.com>) if you have any questions.

You can leverage [Rudder CLI](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/>) to manage [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) and [Transformation Libraries](<https://www.rudderstack.com/docs/transformations/libraries/>) as code using a YAML-driven workflow. You can keep transformation code and test definitions in your repository, validate changes locally, and apply updates to your workspace in a controlled way.

## Key features

With Rudder CLI’s transformations management feature, you get the following capabilities:

### Declarative YAML configuration

  * Define both `transformation` and `transformation-library` resources in YAML files
  * Write transformation code inline or reference external code files
  * Include local test suites alongside your transformation definitions
  * Validate configurations locally before deployment


### Local testing and safer deployment workflow

  * Test individual, all, or only modified transformations
  * Compare actual output against expected results
  * Preview changes with a dry run before applying them to your workspace


### Git integration and CI/CD support

  * Keep transformation specs, code, and test fixtures version-controlled in Git
  * Reuse the same commands locally and in CI pipelines
  * Use a review-first **Validate** > **Test** > **Apply** workflow


## Who can use this feature?

The CLI-based transformations workflow is useful to:

  * Manage transformations and libraries programmatically with consistent standards
  * Test transformation behavior before publishing updates
  * Keep transformation code and tests in the same repository and review process
  * Automate validation and deployment in CI/CD


## Get started

  * See the [Quickstart](<https://www.rudderstack.com/docs/transformations/manage-transformations-with-rudder-cli/quickstart/>) to create, validate, test, and apply transformations using Rudder CLI
  * See the [Transformation YAML Reference](<https://www.rudderstack.com/docs/transformations/manage-transformations-with-rudder-cli/transformation-yaml-reference/>) for complete YAML schemas, constraints, and examples