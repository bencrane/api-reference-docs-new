# Manage Transformations

Manage your transformations in the RudderStack dashboard.

* * *

  * __3 minute read

  * 


RudderStack provides an intuitive UI to help you manage your transformations. This guide will walk you through the steps to:

  * Connect a transformation to a destination
  * Disconnect a transformation
  * Switch transformation between destinations
  * Delete a transformation
  * Manage your transformation-destination connections
  * Manage notifications


## Connect transformation to destination

You can connect a transformation to many destinations. However, each destination can have only one connected transformation at any given time.

#### **Connect cloud mode destinations**

RudderStack supports connecting a transformation to a cloud mode destination, that is, destination that supports sending events via [cloud mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#cloud-mode>).

See [Connect transformations to cloud mode destinations](<https://www.rudderstack.com/docs/transformations/usage/#connect-cloud-mode-destination>) for more information.

#### **Connect device mode destinations**

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * Device mode transformations are currently in beta.
>   * You can enable device mode transformations only from the **Transformations** tab.
> 


You can also connect a transformation to a device mode destination, that is, destination that supports sending events via [device mode](<https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode>).

See [Connect transformations to device mode destinations](<https://www.rudderstack.com/docs/transformations/usage/#connect-device-mode-destination>) for more information.

## Disconnect transformation

There are two ways to disconnect a transformation from a destination:

#### **From transformation**

  1. Go to the **Connections** tab of your transformation and click **Manage Destinations**.
  2. Click the **Edit Connection** button.
  3. Disable the **Connect to transformation** toggle and click **Save**.

[![Disable transformation](/docs/images/features/transformations/connect-disconnect-transformation.webp)](</docs/images/features/transformations/connect-disconnect-transformation.webp>)

  4. Click **Proceed** to confirm.


#### **From destination**

  1. Go to the destination and click the **Transformation** tab. The connected transformation is shown here.
  2. Click **Remove**.
  3. Click **Yes, remove** to confirm and disconnect the transformation.


## Switch transformation

> ![warning](/docs/images/warning.svg)
> 
> Switching between transformations affects the data sent to the destination.

  1. Click the **Connections** tab of your transformation and click **Manage Destinations**. You will see a list of **all** the destinations and the transformations connected to them.

[![Current transformation](/docs/images/features/transformations/current-transformation.webp)](</docs/images/features/transformations/current-transformation.webp>)

  2. Suppose you want to switch the transformation from `T2` to `Test Transformation` for the destination `databricks destn-1`. Click the **Edit Connection** option.

[![Switch transformation](/docs/images/features/transformations/switch-transformation-1.webp)](</docs/images/features/transformations/switch-transformation-1.webp>)

  3. Click **Yes** to disconnect the existing transformation and proceed.

[![Save transformation](/docs/images/features/transformations/connect-disconnect-transformation.webp)](</docs/images/features/transformations/connect-disconnect-transformation.webp>)

  4. Click **Save** > **Switch** to confirm switching the transformation.

[![Switch transformation confirmation](/docs/images/features/transformations/confirm-switch.webp)](</docs/images/features/transformations/confirm-switch.webp>)

> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * You must click the **Save** button for any connection-related changes to take effect.
>   * The previous transformation will be reconnected to the destination automatically, if you switch a transformation but do not save the changes.
> 


## Delete transformation

To delete a transformation, go to **Collect** > **Transformations** and click the **Delete** button next to the transformation you want to delete.

> ![warning](/docs/images/warning.svg)
> 
> You cannot delete a transformation connected to a destination.

[![Delete transformation](/docs/images/features/transformations/delete-transformation.webp)](</docs/images/features/transformations/delete-transformation.webp>)

## Manage connections

RudderStack gives you clear visibility into which transformation is connected to a destination at a given point. This is helpful in cases where you have many transformations connected to various destinations.

To manage your transformation-destination connections, go to the **Connections** tab of your transformation and click **Manage Destinations**.

[![Manage destinations button](/docs/images/features/transformations/manage-transformations-1.webp)](</docs/images/features/transformations/manage-transformations-1.webp>)

You will see a list of **all** the destinations and the transformations connected to them. The transformation you’re currently viewing will be highlighted in bold.

[![Current transformation](/docs/images/features/transformations/current-transformation.webp)](</docs/images/features/transformations/current-transformation.webp>)