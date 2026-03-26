# Activations

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# Activations

Activate your cohorts data in downstream systems to run targeted campaigns.

* * *

  * __2 minute read

  * 


Once you create [cohorts](<https://www.rudderstack.com/docs/archive/profiles/0.14/cohorts/>) and run the project successfully, you can use the Profiles **Activations** feature to sync your target customer data to the downstream marketing tools like Braze, Mailchimp, etc.

This will help you make informed decisions, run personalized marketing campaigns, and enhance the overall customer experience across multiple platforms.

> ![warning](/docs/images/warning.svg)
> 
> RudderStack does not support the Activations feature with Redshift warehouse.

## Prerequisites

You must have a Profiles project available as a Git repository. Import the project in your RudderStack dashboard and run it. Refer [Profiles UI](<https://www.rudderstack.com/docs/archive/profiles/0.14/cohorts/#profiles-ui>) for more information.

## Add activations

Once you have your Profiles project available in the RudderStack dashboard, you can view the cohorts data after the first successful run.

Follow these steps to add an activation for a cohort:

  1. Click **Add activation** next to the cohort for which you want to send data to the downstream destination.

[![Activation API](/docs/images/profiles/activation-view-ui.webp)](</docs/images/profiles/activation-view-ui.webp>)

  2. Configure the following settings in the **Create Activation** window:

Setting| Description  
---|---  
Activation name| Assign a name to uniquely identify the activation.  
Select identifier| Select the type of ID you want to use for the activation from the dropdown menu.  
Select your activation type| Choose a table or audience as your source.  
  
  3. Click **Continue** to verify your credentials.
  4. Review the details and click **Create activation**.
  5. Choose from **Use existing destination** or **Set up a new destination** to connect your activation to the destination.
  6. Configure the destination-specific settings.
  7. Click **Turn on the connection** to enable the connection.

[![Activation API](/docs/images/profiles/activation-connection.webp)](</docs/images/profiles/activation-connection.webp>)

You can view your **Activations** in the list of **Sources** in the RudderStack dashboard.

## View/modify activations

  1. Click **[n] Activations** next to your cohort:

[![Activation API](/docs/images/profiles/view-activation.webp)](</docs/images/profiles/view-activation.webp>)

  2. Click the **Activations** tab to view the detailed list of all the connected activations:

[![Activation API](/docs/images/profiles/activation-list.webp)](</docs/images/profiles/activation-list.webp>)

  3. Click on the activation name. It will take you to the source overview page:

[![Activation API](/docs/images/profiles/connected-destinations.webp)](</docs/images/profiles/connected-destinations.webp>)

  4. Click the **Connection details** next to the destination.

[![Activation API](/docs/images/profiles/connection-details.webp)](</docs/images/profiles/connection-details.webp>)

  5. Edit the **Schema** or **Settings** in the relevant tabs:

[![Activation API](/docs/images/profiles/connection-edit.webp)](</docs/images/profiles/connection-edit.webp>)

  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.14/cohorts/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.14/activation-api/>)