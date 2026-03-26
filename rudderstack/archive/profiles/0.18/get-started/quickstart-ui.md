# Profiles UI

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Profiles UI

Create your Profiles project from the RudderStack dashboard.

* * *

  * __4 minute read

  * 


A Profiles project is a collection of interdependent YAML based configuration files. Once you create and run the project, you can access the outputs from your data warehouse or from the RudderStack dashboard.

This guide lists the detailed steps to create a Profiles project in the RudderStack dashboard using the web-based editor.

## Create Profiles project

  1. Log in to the [RudderStack dashboard](<https://app.rudderstack.com>) and go to **Unify** > **Profiles** option in the left sidebar.
  2. Click **Create project**.

[![Choose predefined template](/docs/images/profiles/create-project.webp)](</docs/images/profiles/create-project.webp>)

  3. Select **Web-based editor (IDE)** on the next screen.

[![Choose predefined template](/docs/images/profiles/basic-setup-profiles.webp)](</docs/images/profiles/basic-setup-profiles.webp>)

> ![info](/docs/images/info.svg)
> 
> You can also import an existing project from your Git repository. See [Import Profiles from Git](<https://www.rudderstack.com/docs/archive/profiles/0.18/get-started/import-from-git/>) for more information.

  4. Enter a unique name and description for your Profiles project.
  5. Select a data warehouse from the dropdown.


> ![warning](/docs/images/warning.svg)
> 
> RudderStack currently supports the following warehouses for creating a Profiles project:
> 
>   * [Snowflake](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/snowflake/>)
>   * [Redshift](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/redshift/>)
>   * [Databricks](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/delta-lake/>)
>   * [BigQuery](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/bigquery/>)
> 


  6. Enter the schema name for the corresponding warehouse in the **Schema** field where you want your Profiles project to store the outputs.

  7. Click **Create Profiles Project** and select **Open in editor mode**.

  8. Enter the schema name you want to use for development purposes for your editing session and click **Continue**.


> ![info](/docs/images/info.svg)
> 
> RudderStack recommends using a development schema while editing your project so that you can modify your YAML configuration files, run your changes within the editor, and validate the outputs in a separate development schema.
> 
> This makes it convenient to test your changes in the development schema without affecting the outputs in your production schema.

You will be able to see the following screen displaying a sample Profiles project with different YAML files:

[![](/docs/images/profiles/profiles-ide.webp)](</docs/images/profiles/profiles-ide.webp>)

You can edit the YAML files and [save and commit the changes](<https://www.rudderstack.com/docs/archive/profiles/0.18/ide/#what-is-the-difference-in-save-and-commit>) to your project. Then, you can run the project by clicking the **Run** button. Upon successful run completion, you can view the outputs in your data warehouse.

### Convert to a Git project

Once you set up a Profiles project in the dashboard, you can convert it to a configuration-based Git repository by [uploading it either to GitHub, GitLab, or Bitbucket](<https://www.rudderstack.com/docs/archive/profiles/0.18/additional-concepts/packages/#supported-git-urls>):

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


## Start/Stop project run

Once created, you can:

  * Run your Profiles project using either of the following ways:
    * Clicking **Run** in the **History** tab of the project.
    * Programmatically using the [Profiles API](<https://www.rudderstack.com/docs/api/profiles-api/>).  
  

  * Stop a running project by clicking the red button in the **Status** column:

[![Stop profiles project](/docs/images/profiles/stop-profiles-project.webp)](</docs/images/profiles/stop-profiles-project.webp>)

> ![warning](/docs/images/warning.svg)
> 
> It might take up to a few seconds to stop a running project.

## Download project

To download the Profiles project, click the arrow icon corresponding to your Profiles project and click **Download this project** :

[![Activation API](/docs/images/profiles/cohorts-view-ui.webp)](</docs/images/profiles/cohorts-view-ui.webp>)

Once downloaded, you can view the [project folder structure](<https://www.rudderstack.com/docs/archive/profiles/0.18/cli-user-guide/structure/>), modify the files, or run various [commands](<https://www.rudderstack.com/docs/archive/profiles/0.18/cli-user-guide/commands/>) to execute the desired use-cases.

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

#### I am not able to see Unify tab on the web app though I have admin privileges. What should I do?

Disable any adblockers on your web browser.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.18/get-started/profile-builder/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.18/get-started/import-from-git/>)