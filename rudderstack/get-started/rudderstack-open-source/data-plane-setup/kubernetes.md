# RudderStack Kubernetes Setup

Set up RudderStack on your Kubernetes cluster.

* * *

  * __4 minute read

  * 


Use the [Helm](<https://helm.sh>) package manager to deploy the RudderStack data plane on your Kubernetes cluster. You can find the Helm chart in the [RudderStack GitHub repository](<https://github.com/rudderlabs/rudderstack-helm>).

> ![warning](/docs/images/warning.svg)
> 
> If you plan to use RudderStack in production, using the Kubernetes Helm charts is strongly recommended.

## Prerequisites

  * Install [Kubectl](<https://kubernetes.io/docs/tasks/tools/>) and connect to your Kubernetes cluster.
  * Install [Helm](<https://helm.sh/>).


## Data plane setup in Kubernetes

  1. Run the following command to clone the [RudderStack Helm repository](<https://github.com/rudderlabs/rudderstack-helm>) containing the RudderStack Helm chart:


    
    
    git clone git@github.com:rudderlabs/rudderstack-helm.git
    

  2. Navigate to the folder containing the Helm chart:


    
    
    cd rudderstack-helm
    

  3. To install the chart with the release name `my-release`, run the following command after replacing `<your_workspace_token>` with your workspace token.


    
    
    helm install my-release ./ --set rudderWorkspaceToken="<your_workspace_token>"
    

> ![info](/docs/images/info.svg)
> 
> The above command deploys RudderStack on your default Kubernetes cluster configured with `kubectl`.
> 
> See Configuration for more information on the configurable parameters during the deployment.

  4. To update the setup, change the configuration or version of the images used, and run the below command:


    
    
    helm upgrade my-release ./ --set rudderWorkspaceToken="<your_workspace_token>"
    

See the below `values.yaml` references to update the image versions:

  * [`rudder-server`](<https://github.com/rudderlabs/rudderstack-helm/blob/master/values.yaml#L38>)
  * [`rudder-transformer`](<https://github.com/rudderlabs/rudderstack-helm/blob/master/values.yaml#L130>)


> ![warning](/docs/images/warning.svg)
> 
> RudderStack **recommends** using the latest `rudder-server` and `rudder-transformer` versions to avoid any breaking changes to your pipelines.
> 
> See the [Server-Transformer Compatibility](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/server-transformer-compatibility/>) guide for more information.

#### Workspace token

The workspace token is a unique identifier of your RudderStack workspace. RudderStack uses this token to automatically read your source-destination configurations when you set up and run the data plane.

  1. Log in to your RudderStack Open Source dashboard.
  2. Copy your workspace token from **Settings** > **Workspace** :

[![Workspace Token](/docs/images/rs-cloud/workspace-token.webp)](</docs/images/rs-cloud/workspace-token.webp>)

For more details on RudderStack Open Source, see [Control plane setup](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-setup/#rudderstack-open-source>).

## Self-hosted control plane

If you are self-hosting your control plane using [Control Plane Lite](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/>), see [Kubernetes instructions](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/#kubernetes>) to set up the data plane.

> ![danger](/docs/images/danger.svg)
> 
> [Control Plane Lite](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/>) is now deprecated and does not work with the latest [`rudder-server`](<https://github.com/rudderlabs/rudder-server>) versions.
> 
> To set up and manage your connections, using the [RudderStack-hosted control plane](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-setup/#rudderstack-open-source>) is strongly recommended.

## Verify installation

To verify if the setup is successful, follow the steps listed in [Verify installation](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/sending-test-events/>).

## Upgrade Helm chart

The following sections will help you upgrade your Helm chart depending on your RudderStack control plane setup.

#### RudderStack Open Source

Update the configuration or version of the images and run the following command:
    
    
    helm upgrade my-release ./ --set rudderWorkspaceToken="<your_workspace_token>"
    

Replace `<your_workspace_token>` with the workspace token copied in Step 2.

#### Self-hosted control plane

Update the configuration or version of the images and run the following command:
    
    
    helm upgrade my-release ./ --set backend.controlPlaneJSON=true
    

## Uninstall deployment

To uninstall or delete the deployment named `my-release`, run the following command:
    
    
    helm uninstall my-release
    

> ![info](/docs/images/info.svg)
> 
> This command also removes all components created by the chart.

## Configuration

The following table lists the configurable parameters of the RudderStack Helm chart and their default values:

Parameter| Description| Default value  
---|---|---  
`rudderWorkspaceToken`| Your workspace token obtained from the RudderStack Open Source dashboard.| -  
`backend.image.repository`| Container image repository for the backend.| `rudderlabs/rudder-server`  
`backend.image.version`| Container image tag for the backend. Check the [available versions](<https://hub.docker.com/r/rudderlabs/rudder-server/tags>)| -  
`backend.image.pullPolicy`| Container image pull policy for the backend image.| `Always`  
`transformer.image.repository`| Container image repository for the transformer.| `rudderlabs/transformer`  
`transformer.image.version`| Container image tag for the transformer. Check the [available versions](<https://hub.docker.com/r/rudderlabs/rudder-transformer/tags>)| -  
`transformer.image.imagePullPolicy`| Container image pull policy for the transformer image.| `Always`  
`backend.extraEnvVars`| Extra environments variables to be used by the backend in the deployments| See the `values.yaml` file.  
`backend.controlPlaneJSON`| If you have self-hosted the control plane using Control Plane Lite, set this to `true`.  
  
The data plane then reads the configuration from the exported `workspaceConfig.json` file.| `false`  
  
You can change each of these parameters in `values.yaml` and specify each parameter using the `--set key=value[,key=value]` argument while running the `helm install` command:
    
    
    helm install --name my-release \
      --set backend.image.version=v0.1.6 \
      ./
    

> ![info](/docs/images/info.svg)
> 
> Note that:
> 
>   * You can edit the data plane-specific configuration in the [`config.yaml`](<https://github.com/rudderlabs/rudder-server/blob/master/config/config.yaml>) file.
>   * You can configure the PostgreSQL-specific configuration in the `pg_hba.conf` and `postgresql.conf` files.
> 


## Components

Installing this Helm chart deploy the following pods and containers in the configured cluster:

**POD - {Release name}-rudderstack-0 :**

  * `rudderstack-backend`
  * `rudderstack-telegraf-sidecar`


**POD - {Release name}-rudderstack-postgresql-0 :**

  * `{Release name}-rudderstack-postgresql`


**POD - {Release name}-rudderstack-transformer-xxxxxxxxxx-xxxxx:**

  * `transformer`


## Setup instructions for GCP

If you plan to use the following destinations:

  * [Google Cloud Storage](<https://www.rudderstack.com/docs/destinations/streaming-destinations/google-cloud-storage/>)
  * [Google BigQuery](<https://www.rudderstack.com/docs/destinations/warehouse-destinations/bigquery/>)


Make sure to replace the contents of the file [rudder-google-application-credentials.json](<https://github.com/rudderlabs/rudderstack-helm/blob/master/rudder-google-application-credentials.json>) in the repository with the details of your Google service account.