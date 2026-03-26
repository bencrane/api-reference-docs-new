# Manage Event Stream Sources using Rudder CLI Alpha

Define and manage event stream sources as YAML configurations using the Rudder CLI tool.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __2 minute read

  * 


> ![info](/docs/images/info.svg)
> 
> This feature is in **Alpha** as part of RudderStack’s [Early Access Program](<https://www.rudderstack.com/docs/get-started/alpha-and-beta-features/alpha-features/>), where we work with early users and customers to test new features and get feedback before making them generally available. Note that these features are functional but can change as we improve them.
> 
> [Contact the Product team](<mailto:product@rudderstack.com>) if you have any questions.

RudderStack’s CLI-based Event Stream source management feature helps you manage [Event Stream sources](<https://www.rudderstack.com/docs/sources/event-streams/>) as code by leveraging the new CLI-based workflow. It helps you bring source configuration into your existing development workflows through code-first management.

With this feature, you can apply the same rigor and process to your source configuration that you apply to your application code, ensuring consistency and quality in your event collection strategy.

## Key features

With RudderStack’s CLI-based Event Stream source management, you get the following features:

### Declarative YAML configuration

  * Define and manage Event Stream sources directly in your codebase using simple [YAML files](<https://www.rudderstack.com/docs/sources/event-streams/sdks/manage-sources-with-rudder-cli/source-yaml-reference/>).
  * Configure source-level data governance settings by associating [Tracking Plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>) with sources.
  * Control violation handling behavior for different event types (`track`, `identify`, `group`, `page`, `screen`) through granular configuration options.


### Git integration and CI/CD support

  * Leverage [GitHub Actions](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/github-actions/>) to automatically validate and deploy source configurations from your repository.
  * Use the standard Git workflows to track changes, implement version control, manage branches, and make any other modifications.


## Who can use this feature?

The CLI-based Event Stream source management feature is helpful for data teams who need to:

  * Manage their Event Stream sources programmatically with consistent configuration standards.
  * Integrate their source configuration changes into their existing development workflows.
  * Validate their source configuration changes before deployment.
  * Apply data governance policies consistently across multiple sources.


## Get started

  * See the [Quickstart](<https://www.rudderstack.com/docs/sources/event-streams/sdks/manage-sources-with-rudder-cli/quickstart/>) guide to start managing your Event Stream sources using Rudder CLI
  * See the [Source YAML Reference](<https://www.rudderstack.com/docs/sources/event-streams/sdks/manage-sources-with-rudder-cli/source-yaml-reference/>) to understand the complete YAML structure for Event Stream source files