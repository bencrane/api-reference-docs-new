# RudderStack Docker Setup

Set up RudderStack on Docker.

* * *

  * __2 minute read

  * 


This guide will help you set up the RudderStack data plane in your Docker environment.

> ![success](/docs/images/tick.svg)
> 
> The Docker setup is the easiest and the fastest way to get up and running with RudderStack.

## Data plane setup in Docker

  1. Download the `rudder-docker.yml` [docker-compose](<https://raw.githubusercontent.com/rudderlabs/rudder-server/master/rudder-docker.yml>) file.
  2. Replace `<your_workspace_token>` in this file with your workspace token.
  3. In your terminal, navigate to the directory where you want to install RudderStack and run the following command:


    
    
    docker compose -f rudder-docker.yml up -d
    

> ![info](/docs/images/info.svg)
> 
> If you’re using an older version of Docker, run the following command:
>     
>     
>     docker-compose -f rudder-docker.yml up
>     

## Update setup

> ![warning](/docs/images/warning.svg)
> 
> RudderStack **recommends** using the latest `rudder-server` and `rudder-transformer` versions to avoid any breaking changes to your pipelines.
> 
> See the [Server-Transformer Compatibility](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/server-transformer-compatibility/>) guide for more information.

  1. Stop the running container.
  2. Pull the images with the **latest minor release** for both [`rudder-server`](<https://hub.docker.com/r/rudderlabs/rudder-server/tags>) and [`rudder-transformer`](<https://hub.docker.com/r/rudderlabs/rudder-transformer/tags>).


    
    
    docker pull rudderlabs/rudder-server:<version>
    
    docker pull rudderlabs/rudder-transformer:<version>
    

> ![info](/docs/images/info.svg)
> 
> See the below `rudder-docker.yml` references to update specific image versions:
> 
>   * [rudder-server](<https://github.com/rudderlabs/rudder-server/blob/master/rudder-docker.yml#L17>)
>   * [rudder-transformer](<https://github.com/rudderlabs/rudder-server/blob/master/rudder-docker.yml#L41>)
> 


  3. Start the container.
  4. Test the [container health](<https://medium.com/@thkhoobsmart/adding-health-check-to-docker-container-b4eb1d554f36>) with the `/health` endpoint.


#### Workspace token

The workspace token is a unique identifier of your RudderStack workspace. RudderStack uses this token to automatically read your source-destination configurations when you set up and run the data plane.

  1. Log in to your RudderStack Open Source dashboard.
  2. Copy your workspace token from **Settings** > **Workspace** :

[![Workspace Token](/docs/images/rs-cloud/workspace-token.webp)](</docs/images/rs-cloud/workspace-token.webp>)

## Self-hosted control plane

If you are self-hosting your control plane using [Control Plane Lite](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/>), see [Docker instructions](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/#docker>) to set up your data plane.

> ![danger](/docs/images/danger.svg)
> 
> [Control Plane Lite](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/>) is now deprecated and does not work with the latest [`rudder-server`](<https://github.com/rudderlabs/rudder-server>) versions.
> 
> To set up and manage your connections, using the [RudderStack-hosted control plane](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-setup/#rudderstack-open-source>) is strongly recommended.

## Verify installation

To verify if the setup is successful, follow the steps listed in [Verify installation](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/sending-test-events/>).