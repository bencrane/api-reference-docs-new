# Profiles UI

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Profiles UI

Create your Profiles project from the RudderStack dashboard.

* * *

  * __5 minute read

  * 


> ![info](/docs/images/info.svg)
> 
> While creating a Profiles project, you can choose either of the below:
> 
>   * **Profile Builder (PB) CLI** which gives you the flexibility to create, develop, and debug your Profiles project using various commands in fine detail. You can explore and implement the exhaustive list of features and functionalities offered by Profiles.
>   * **Profiles UI** which provides a step-by-step intuitive workflow in the RudderStack dashboard. You can configure your project, schedule its run, explore the outputs and the user profiles.
> 


This guide lists the detailed steps to create a Profiles project in the RudderStack dashboard.

## Create Profiles project

  1. Log in to the [RudderStack dashboard](<https://app.rudderstack.com>) and go to **Unify** > **Profiles** option in the left sidebar.
  2. Click **Create project**.

[![Choose predefined template](/docs/images/profiles/create-project.webp)](</docs/images/profiles/create-project.webp>)

  3. Select **Basic Entity Setup** on the next screen.

[![Choose predefined template](/docs/images/profiles/basic-setup-profiles.webp)](</docs/images/profiles/basic-setup-profiles.webp>)

> ![info](/docs/images/info.svg)
> 
> You can also import an existing project from your Git repository. See [Import Profiles from Git](<https://www.rudderstack.com/docs/archive/profiles/0.13/get-started/import-from-git/>) for more information.

  4. Enter a unique name and description for your Profiles project.
  5. Select a data warehouse from the dropdown and the source(s) connected to the warehouse.


> ![warning](/docs/images/warning.svg)
> 
> RudderStack currently supports the [Snowflake](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/>), [Redshift](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/redshift/>), [Databricks](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/delta-lake/>), and [BigQuery](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/bigquery/>) warehouses for creating a Profiles project.
> 
> You must connect an [event stream source](<https://www.rudderstack.com/docs/sources/event-streams/>) to one of the above warehouses and sync data at least once so that they populate in the dropdown.  
>   
> For example, in the below image, the Node event stream source (_es src_) is connected to the Snowflake warehouse destination (_cohort sample_ ) containing the schema _SAMPLE_SHOPIFY_DATA_.

[![Choose predefined template](/docs/images/profiles/source.webp)](</docs/images/profiles/source.webp>)

  6. Click **Add mapping** and provide values to map the existing ID types from the above-selected event stream source:


> ![info](/docs/images/info.svg)
> 
> You can see some predefined mappings for the identifiers which comes from the [Profiles library project](<https://github.com/rudderlabs/profiles-multieventstream-features/tree/main>).  
>   
> Here, **Event** column represents the tables present in the warehouse, **Property** column represents the column name in that table, and **ID type** represents the type of identifier.

[![Choose predefined template](/docs/images/profiles/map-id.webp)](</docs/images/profiles/map-id.webp>)

  7. Define features either by adding a custom feature or selecting a pre-defined feature as shown:

[![Choose predefined template](/docs/images/profiles/define-features.webp)](</docs/images/profiles/define-features.webp>)

  * To add a custom feature, click **Add a custom feature** and enter the relevant feature details:

[![Choose predefined template](/docs/images/profiles/custom-feature.webp)](</docs/images/profiles/custom-feature.webp>)

  * To use a pre-defined feature, select the required feature from the **Template features library**.


  8. Select the [schedule type](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-schedule-settings/>).
  9. Enter the warehouse details where you want to store this Profiles project.
  10. Finally, review all the provided details and click **Create Profiles project**.


### Convert to a Git project

Once you set up a Profiles project in the dashboard, you can convert it to a configuration-based Git repository by [uploading it either to GitHub, GitLab, or Bitbucket](<https://www.rudderstack.com/docs/archive/profiles/0.13/example/packages/#supported-git-urls>):

> ![warning](/docs/images/warning.svg)
> 
> You cannot revert to your UI-based project after Git conversion. Once converted, all the project edits and updates can only be done via Git repository.

  1. Navigate to the **Unify** > **Profiles** option in the left sidebar to view all your Profiles projects.
  2. Click **Convert to Git** button next to the project you want to convert.
  3. [Create a new Git repository](<https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository>).
  4. Enter the [SSH URL of your Git repository](<https://git-scm.com/book/en/v2/Git-on-the-Server-The-Protocols>) to be used for your Profiles project and click **Continue**.
  5. Copy the SSH public key and click **Add deploy key** which will take you to your git repository’s **Deploy keys** section. See deploy keys section in the [GitHub](<https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys#set-up-deploy-keys>), [GitLab](<https://docs.gitlab.com/ee/user/project/deploy_keys/>), or [Bitbucket](<https://bitbucket.org/blog/deployment-keys>) documentation for more information.


> ![warning](/docs/images/warning.svg)
> 
> Make sure your Git repository has at least one commit for successful validation.

  7. Click **Add deploy key** , add a **Title** , paste your SSH public key, and click **Add key**.
  8. Click **Continue** to let RudderStack verify read access.
  9. Click **Download project** to download the Profiles project you set up in the dashboard.
  10. Commit the downloaded project to your Git repository.
  11. Once the project is committed successfully, return to the dashboard and click **Convert Profiles project**.


## Run project

Once created, you can run your Profiles project using either of the following ways:

  * Clicking **Run** in the **History** tab of the project.
  * Programmatically using the [Profiles API](<https://www.rudderstack.com/docs/api/profiles-api/>).


## Download project

To download the Profiles project, click the arrow icon corresponding to your Profiles project and click **Download this project** :

[![Activation API](/docs/images/profiles/cohorts-view-ui.webp)](</docs/images/profiles/cohorts-view-ui.webp>)

Once downloaded, you can view the [project folder structure](<https://www.rudderstack.com/docs/archive/profiles/0.13/cli-user-guide/structure/>), modify the files, or run various [commands](<https://www.rudderstack.com/docs/archive/profiles/0.13/cli-user-guide/commands/>) to execute the desired use-cases.

## Project details

To view the Profile project details, click the arrow icon corresponding to your Profiles project:

Option| Description  
---|---  
**Entities**|  Lists the entities, cohorts, features, activations, etc. for your Profiles project.  
**History**|  Displays the history of Profile runs.  
**Settings**|  Displays your profile settings and lets you delete your Profiles project. You can edit the project by clicking the edit icon next to each section.  
  
### Profile details

You can also view the details of a specific profile in your Profiles project:

  1. In your Profiles project’s **Entities** tab, click **View** button across the entity for which you want to see the profile:[![Activation API](/docs/images/profiles/entity_view.webp)](</docs/images/profiles/entity_view.webp>)

  2. Click **Profile Lookup** tab to search a profile record.

  3. Type an available unique identifier like `email`, `phone number`, `user id`, `anonymous id` etc. and click **Search user profile**.[![Activation API](/docs/images/profiles/profiles-lookup.webp)](</docs/images/profiles/profiles-lookup.webp>)


> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * It can take a few minutes for the data preview to show up in your profile’s **History** tab.
>   * If you keep getting a blank screen, it may be because you do not have sufficient access. Make sure you have a [Connections Admin](<https://www.rudderstack.com/docs/dashboard-guides/user-management/#resource-roles>) resource role with [access to PII](<https://www.rudderstack.com/docs/dashboard-guides/data-management/#limiting-access-to-pii-related-features>). In case the problem persists, contact [RudderStack support](<mailto:support@rudderstack.com>).
> 


## FAQ

**When trying to fetch data for a lib project, then data/columns are shown as blank. What should I do?**

You’ll need to sync data from a source to a destination. If data is synced from the source you are using and not from some pre-existing tables in the destination, the missing column/data issues should not occur.

**I am not able to see Unify tab on the web app though I have admin privileges. What should I do?**

Disable any adblockers on your web browser.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.13/get-started/profile-builder/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.13/get-started/import-from-git/>)