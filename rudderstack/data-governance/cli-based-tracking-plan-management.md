# CLI-based Data Catalog and Tracking Plan Management Alpha

Track, version control, and manage your events, properties, and Tracking Plans as code.

Available Plans

  * free
  * starter
  * growth
  * enterprise


* * *

  *  __3 minute read

  * 


> ![announcement](/docs/images/announcement.svg)
> 
> This feature is in **Alpha** as part of RudderStack’s [Early Access Program](<https://www.rudderstack.com/docs/get-started/alpha-and-beta-features/alpha-features/>), where we work with early users and customers to test new features and get feedback before making them generally available. Note that these features are functional but can change as we improve them.
> 
> Before you get started, note the following:
> 
>   * See the limitations section to learn more about current differences between the CLI and UI.
>   * RudderStack recommends testing this feature in a clean **Dev** workspace.
>   * [Contact the Product team](<mailto:product@rudderstack.com>) if you have any questions.
> 


RudderStack’s CLI-based Tracking Plans management feature helps you manage [Tracking Plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>) and [Data Catalog](<https://www.rudderstack.com/docs/data-governance/data-catalog/>) as code by leveraging the new CLI-based workflow. It helps you bring data governance into your existing development workflows through code-first management.

With this feature, you can bring the same rigor and process to your Tracking Plans that you apply to your application code, ensuring consistency and quality in your data collection strategy.

## Key features

With RudderStack’s CLI-based Tracking Plan management, you get the following features:

### Declarative YAML configuration

  * Define and manage events, properties, and Tracking Plans directly in your codebase using simple [YAML files](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/project-yaml-reference/>).
  * Create reusable property definitions with [advanced validation rules](<https://www.rudderstack.com/docs/data-governance/data-catalog/properties/#advanced-rules>) like minimum/maximum length, patterns, enums, etc. across multiple events.
  * Define dynamic validation rules using [Conditional Validation](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/conditional-validation/>) that adapt based on context.
  * Leverage a structured referencing system to associate events and properties to a Tracking Plan.


### Powerful Rudder CLI tool

This feature comes with a powerful [Rudder CLI](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/>) utility that lets you:

  * Create, update, and delete Tracking Plan resources via command line.
  * Verify your YAML configurations locally before pushing changes to production.
  * Sync the local configuration files with your RudderStack workspace.


> ![success](/docs/images/tick.svg)
> 
> In contrast to how Infrastructure-as-Code (IaC) tools typically depend on external object storage like S3 to maintain their state, you can store the relevant state directly in RudderStack, thereby significantly reducing configuration overhead.
> 
> You only need the YAML configuration files and a [RudderStack token](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/quickstart/#prerequisites>) to use Rudder CLI.

### Git integration and CI/CD support

  * Leverage [GitHub Actions](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/github-actions/>) to automatically validate and deploy Tracking Plans from your repository.
  * Use the standard Git workflows to track changes, implement version control, manage branches, and make any other modifications.


## Who can use this feature?

The CLI-based Data Catalog and Tracking Plan management feature is helpful for data teams who need to:

  * Manage their Tracking Plans and Data Catalog programmatically with consistent tracking standards.
  * Integrate their Tracking Plan changes into their existing development workflows.
  * Validate their Tracking Plan changes before deployment.


## Get started

  1. [Install the Rudder CLI tool](<https://www.rudderstack.com/docs/dev-tools/rudder-cli/installation/>) in your preferred environment.
  2. Generate a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) in the RudderStack dashboard with the following [permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) to manage Data Catalog and Tracking Plans:

Resource| Permissions  
---|---  
Tracking Plans| **Create & Delete**, **Edit**  
Data Catalog| **Edit**  
  
> ![info](/docs/images/info.svg)
> 
> **Token permissions for legacy RBAC system**
> 
> If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), your workspace-level Service Access Token should have **Admin** permissions.
> 
> See [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for more information on generating the token.

  * **For testing or development purposes only** : Generate a [Personal Access Token](<https://www.rudderstack.com/docs/access-management/personal-access-tokens/>) with **Read-Write** role


> ![warning](/docs/images/warning.svg)
> 
> **RudderStack recommends using a workspace-level Service Access Token for authentication.**
> 
> Any action authenticated by a Personal Access Token will break if the user is removed from the organization or a breaking change is made to their permissions.

  3. [Initialize a new Tracking Plan project](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/tracking-plans/>) with [YAML definitions](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/project-yaml-reference/>). Then, sync the changes to your workspace.
  4. Automate Tracking Plan management using [GitHub Actions](<https://www.rudderstack.com/docs/data-governance/cli-based-tracking-plan-management/github-actions/>).


## Limitations

Rudder CLI only supports **pushing** updates to RudderStack, not **pulling**. This means you will need to test with a clean **Dev** workspace where the Data Catalog is empty and there are no Tracking Plans.

[Contact the Product team](<mailto:product@rudderstack.com>) or your Technical Account Manager if you need a new workspace.