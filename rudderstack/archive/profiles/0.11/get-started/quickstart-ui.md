# Profiles UI

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Profiles UI

Create your Profiles project from the RudderStack dashboard.

* * *

  * __3 minute read

  * 


This guide lists the detailed steps to create a Profiles project in the RudderStack dashboard.

## Create Profiles project

RudderStack provides you with the following options to create a Profiles project:

### Basic entity setup

To create a Profiles project from scratch:

  1. Log in to the [RudderStack dashboard](<https://app.rudderstack.com>) and go to **Unify** > **Profiles** option in the left sidebar.
  2. Click **Create project**.

[![Choose predefined template](/docs/images/profiles/create-project.webp)](</docs/images/profiles/create-project.webp>)

  3. Select **Basic Entity Setup** on the next screen.
  4. Enter a unique name and description for your Profiles project.
  5. Select the data warehouse from the dropdown and the source(s) connected to the warehouse.


> ![info](/docs/images/info.svg)
> 
> RudderStack currently supports the [Snowflake](<https://www.rudderstack.com/docs/sources/reverse-etl/snowflake/#configuring-the-connection-credentials>), [Redshift](<https://www.rudderstack.com/docs/sources/reverse-etl/amazon-redshift/#configuring-the-connection-credentials>), [Databricks](<https://www.rudderstack.com/docs/sources/reverse-etl/databricks/#configuring-the-connection-credentials>), and [BigQuery](<https://www.rudderstack.com/docs/sources/reverse-etl/google-bigquery/#configuring-the-connection-credentials>) warehouses for creating a Profiles project. You need to set up the warehouse source in the first place to populate it here in the dropdown.

[![Choose predefined template](/docs/images/profiles/source.webp)](</docs/images/profiles/source.webp>)

  6. Map the identifiers from above-selected source by selecting the source, event, property, and ID type by clicking **Add mapping** :

[![Choose predefined template](/docs/images/profiles/map-id.webp)](</docs/images/profiles/map-id.webp>)

  7. Define features either by adding a custom feature or selecting a pre-defined feature as shown:

[![Choose predefined template](/docs/images/profiles/define-features.webp)](</docs/images/profiles/define-features.webp>)

  * To add a custom feature, click **Add a custom feature** and enter the relevant feature details:

[![Choose predefined template](/docs/images/profiles/custom-feature.webp)](</docs/images/profiles/custom-feature.webp>)

  * To use a pre-defined feature, select the required feature from the **Template features library**.


  8. Select the [schedule type](<https://www.rudderstack.com/docs/data-pipelines/reverse-etl/developer-guides/sync-schedule-settings/>).
  9. Enter the warehouse details where you want to store this Profiles project.
  10. Finally, review all the provided details and click **Create Profiles project**.


### Import project from Git Repo

To create a Profiles project by importing it from a Git repository:

  1. Log in to the [RudderStack dashboard](<https://app.rudderstack.com>) and go to **Unify** > **Profiles** option in the left sidebar.
  2. Click **Create project**.

[![Choose predefined template](/docs/images/profiles/create-project.webp)](</docs/images/profiles/create-project.webp>)

  3. Select **Import project from Git Repo** on the next screen.
  4. Enter a unique name and description for your Profiles project.
  5. Enter the [SSH URL of your Git repository](<https://docs.github.com/en/authentication/connecting-to-github-with-ssh>) to be used for your Profiles project.


> ![warning](/docs/images/warning.svg)
> 
> Make sure the SSH URL you provide contains the Profiles project, otherwise it can result in an error.

  6. Copy the SSH public key and click **Add deploy key** which will take you to your git repository’s **Deploy keys** section. See [Set up deploy keys](<https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys#set-up-deploy-keys>) for more information.
  7. Select the warehouse and enter its credentials to store this Profiles project.
  8. Finally, click **Create Profiles project**.


## Download project

To download the Profiles project, click **View** corresponding to your Profiles project and click **Download this project** :

[![Download Profiles project](/docs/images/profiles/download-profiles-project.webp)](</docs/images/profiles/download-profiles-project.webp>)

## Profile details

To view the profile details, click **View** corresponding to your Profiles project:

Option| Description  
---|---  
**Overview**|  Lists the features of your Profiles project.  
**History**|  Displays the history of Profile runs.  
**Explorer**|  Displays the preview of first 50 rows of the output tables (features and ID stitching) only after the successful run of the project. You can also search for all the records, by typing in a unique identifier such as user_id, email, etc.  
**Settings**|  Displays your profile settings and lets you delete your Profiles project. You can edit the project by clicking the edit icon next to each section.  
  
> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * It can take up to thirty minutes for the data preview to show up in your profile’s **History** tab.
>   * If you keep getting a blank screen, it may be because you do not have sufficient access. Make sure you have a [Connections Admin](<https://www.rudderstack.com/docs/dashboard-guides/user-management/#resource-roles>) resource role with [access to PII](<https://www.rudderstack.com/docs/dashboard-guides/data-management/#limiting-access-to-pii-related-features>). In case the problem persists, contact [RudderStack support](<mailto:support@rudderstack.com>).
> 


## FAQ

**When trying to fetch data for a lib project, then data/columns are shown as blank. What should I do?**

You’ll need to sync data from a source to a destination. If data is synced from the source you are using and not from some pre-existing tables in the destination, the missing column/data issues should not occur.

**I am not able to see Unify tab on the web app though I have admin privileges. What should I do?**

Disable any adblockers on your web browser.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.11/get-started/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.11/get-started/profile-builder/>)