# RudderStack Developer Machine Setup

Set up RudderStack in your development environment.

* * *

  * __2 minute read

  * 


This guide lists the steps to set up the RudderStack data plane in your development environment.

## Prerequisites

  * [Go 1.17](<https://golang.org/dl/>) or above.
  * [Node.js 14.17](<https://nodejs.org/en/download/>) or above.
  * [PostgreSQL 11](<https://www.postgresql.org/download/>) or above.


## Data plane setup

> ![warning](/docs/images/warning.svg)
> 
> RudderStack **recommends** using the latest `rudder-server` and `rudder-transformer` versions to avoid any breaking changes to your pipelines.
> 
> See the [Server-Transformer Compatibility](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/server-transformer-compatibility/>) guide for more information.

  1. Log in to your RudderStack Open Source dashboard.
  2. Copy your [workspace token](<https://www.rudderstack.com/docs/dashboard-guides/overview/#workspace-token>) from **Settings** > **Workspace** :

[![Workspace Token](/docs/images/rs-cloud/workspace-token.webp)](</docs/images/rs-cloud/workspace-token.webp>)

  3. Set up the database in your preferred directory using the following commands:


    
    
    createdb jobsdb
    createuser --superuser rudder
    psql "jobsdb" -c "alter user rudder with encrypted password 'rudder'";
    psql "jobsdb" -c "grant all privileges on database jobsdb to rudder";
    

  4. Clone the [`rudder-server`](<https://github.com/rudderlabs/rudder-server>) repository:


    
    
    git clone https://github.com/rudderlabs/rudder-server.git
    

  5. Run the following commands to fetch the `rudder-transformer` repository.


    
    
    git submodule init
    git submodule update
    

  6. Navigate to the `rudder-transformer` directory using the `cd rudder-transformer` command.
  7. Install the dependencies using the `npm i` command.
  8. Start the destination transformer:


    
    
    node destTransformer.js
    

  9. Navigate back to the main directory using the `cd rudder-server` command.
  10. Copy `sample.env` to the main directory:


    
    
    cp config/sample.env .env
    

  11. Update `WORKSPACE_TOKEN` in this file with the workspace token you copied in Step 2.
  12. Start the RudderStack server:


    
    
    go run main.go
    

## Self-hosted control plane

If you are self-hosting your control plane using [Control Plane Lite](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/>), see [Developer Machine Setup instructions](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/#developer-machine-setup>) to set up the data plane.

## Verify installation

To verify if the setup is successful, follow the steps listed in [Verify installation](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/sending-test-events/>).