# Databricks Partner Connect

Connect your Databricks cluster to RudderStack and set up your Databricks Delta Lake destination.

* * *

  * __2 minute read

  * 


You can now use [Databricks Partner Connect](<https://www.databricks.com/partnerconnect>) to set up your Databricks Delta Lake destination in RudderStack without following the [setup guide instructions](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/delta-lake/#configuring-delta-lake-destination-in-rudderstack>).

Using Partner Connect, RudderStack automatically creates the destination for you with a configuration received from Databricks. Once the destination is set up, you can then add or modify the configuration depending on your requirement.

> ![warning](/docs/images/warning.svg)
> 
> Before using Partner Connect to set up your Databricks destination, make sure you meet [Databricks’ requirements](<https://docs.databricks.com/en/partner-connect/index.html#requirements>).

## Prerequisites

To connect your Databricks cluster to RudderStack, you need the following:

  * A Databricks account.
  * A RudderStack account with the required [resource permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/>) to add destinations.
  * If you have enabled the Unity Catalog feature on your workspace for Databricks on Azure, make sure to follow the [Azure Databricks documentation](<https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/#how-do-i-set-up-unity-catalog-for-my-organization>) to set up Unity Catalog for your organization.


> ![info](/docs/images/info.svg)
> 
> You can also connect Databricks to RudderStack using a [Databricks cluster](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/delta-lake/#creating-a-new-databricks-cluster>).

## Set up Delta Lake destination

This section lists the steps to set up a Databricks Delta Lake destination in RudderStack using Partner Connect.

Note that [Azure Databricks](<https://accounts.azuredatabricks.net/login>) is used as an example in this section. However, these steps are similar for other cloud providers.

  1. Sign in to your Databricks portal.
  2. Click **Partner Connect** in the left sidebar:

[![Partner Connect option in Azure Databricks](/docs/images/dw-integrations/partner-connect/partner-connect.webp)](</docs/images/dw-integrations/partner-connect/partner-connect.webp>)

  3. Search **RudderStack** and select the tile.

[![RudderStack option in Azure Databricks](/docs/images/dw-integrations/partner-connect/partner-connect-rudderstack.webp)](</docs/images/dw-integrations/partner-connect/partner-connect-rudderstack.webp>)

  4. You will see some preconfigured settings under **Connect to partner**. Click **Next** to proceed.
  5. Enter your email and click **Connect to RudderStack**.

[![Connect to RudderStack option in Azure Databricks](/docs/images/dw-integrations/partner-connect/connect-to-rudderstack.webp)](</docs/images/dw-integrations/partner-connect/connect-to-rudderstack.webp>)

  6. Enter your credentials to sign up/log in to RudderStack.

[![Log in to RudderStack](/docs/images/dw-integrations/partner-connect/login-signup.webp)](</docs/images/dw-integrations/partner-connect/login-signup.webp>)

> ![success](/docs/images/tick.svg)
> 
> RudderStack will automatically provision and set up your Databricks destination.

  7. Connect the Delta Lake destination to a data source. Go to the **Sources** tab and click **Add source**. See [Add a source](<https://www.rudderstack.com/docs/dashboard-guides/sources/#add-a-source>) for more information.


> ![warning](/docs/images/warning.svg)
> 
> Before connecting, make sure that the Databricks provisioned cluster is up.

[![Connect a source](/docs/images/dw-integrations/partner-connect/add-source.webp)](</docs/images/dw-integrations/partner-connect/add-source.webp>)

  8. To edit or modify the preconfigured credentials, go to the **Configuration** tab and click **Edit configuration**. See [Databricks documentation](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/delta-lake/#connection-settings>) for more information on the connection credentials.

[![Edit destination configuration](/docs/images/dw-integrations/partner-connect/edit-configuration.webp)](</docs/images/dw-integrations/partner-connect/edit-configuration.webp>)