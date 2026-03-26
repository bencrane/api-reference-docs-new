# Import Profiles Project from Git

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Import Profiles Project from Git

Import an existing Profiles project from the Git repository in RudderStack dashboard.

* * *

  * __2 minute read

  * 


If you have created a Profiles project using the **Profile Builder** (command-line tool), you can make it [available in a Git repository](<https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories>), and further import it in the RudderStack dashboard to:

  * View the project, its details, and the output tables in the UI.
  * Schedule its invocation periodically (for example, every 12 hours, 6 hours, etc.).
  * Seamlessly collaborate with your teammates, with modular control over your model files.


## Prerequisites

  * Profiles project in a Git repository


> ![info](/docs/images/info.svg)
> 
> RudderStack recommends using a different target schema and user for Profiles for RudderStack dashboard than the one used for CLI project. This will maintain differentiation in case of manual runs (using CLI) and scheduled runs (using RudderStack dashboard):

[![](/docs/images/profiles/DifferentSchemasWebCLI.webp)](</docs/images/profiles/DifferentSchemasWebCLI.webp>)

## Steps

To import the Profiles project from a Git repository in the RudderStack dashboard:

  1. Log in to the [RudderStack dashboard](<https://app.rudderstack.com>) and go to **Unify** > **Profiles** option in the left sidebar.
  2. Click **Create project**.

[![Choose predefined template](/docs/images/profiles/create-project.webp)](</docs/images/profiles/create-project.webp>)

  3. Select **Import project from Git Repo** on the next screen.
  4. Enter a unique name and description for your Profiles project.
  5. Enter the SSH URL of your Git repository to be used for your Profiles project:


[![](/docs/images/profiles/ssh-key.webp)](</docs/images/profiles/ssh-key.webp>)  


> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * The SSH URL you provide must contain the Profiles project, otherwise it can result in an error.
> 
>   * The git SSH URL must follow any of the below patterns:
> 
>     * `git@<provider-host>:<org-name>/<repo-name>/tree/<branch-name>`
>     * `git@<provider-host>:<org-name>/<repo-name>`
>     * `git@<provider-host>:<org-name>/<repo-name>/tree/main/path/to/project`
>   * RudderStack supports any subfolder in the git project without the `.git` extension.
> 
>   * See [GitHub documentation](<https://docs.github.com/en/authentication/connecting-to-github-with-ssh>), [GitLab documentation](<https://docs.gitlab.com/ee/user/project/deploy_keys/#create-a-project-deploy-key>), and [BitBucket documentation](<https://confluence.atlassian.com/bitbucketserver/ssh-access-keys-for-system-use-776639781.html>) for more information.
> 
> 


  6. Copy the SSH public key. Then, click **Add deploy key** which will take you to your git repository’s **Deploy keys** section. See [Set up deploy keys](<https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys#set-up-deploy-keys>) for more information.

[![](/docs/images/profiles/deploy-key.webp)](</docs/images/profiles/deploy-key.webp>)

  7. Click **Add deploy key**. Then, add a **Title** , paste your SSH public key, and click **Add key**.
  8. Go back to the RudderStack dashboard, then click **Continue** to let RudderStack verify read access.
  9. Select the warehouse and enter its credentials to store this Profiles project.

[![](/docs/images/profiles/warehouse-details.webp)](</docs/images/profiles/warehouse-details.webp>)

  10. Finally, click **Create Profiles project**.


Next, choose any of the following options:

  * **View Profiles project** which takes you to the **Overview** tab of the project to view project details.
  * **Run Profiles project** which takes you to the **History** tab of the project from where you can click **Run** to run the project.


You can explore other project settings in the different tabs. For more information, see [Project details](<https://www.rudderstack.com/docs/archive/profiles/0.17/get-started/quickstart-ui/#project-details>).

> ![warning](/docs/images/warning.svg)
> 
> Once you import a project successfully in the dashboard, you cannot edit its Git repository URL.

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.17/get-started/quickstart-ui/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.17/get-started/sample-data/>)