# RudderStack Open Source FAQ

Troubleshoot problems encountered while setting up and using RudderStack Open Source.

* * *

  * __4 minute read

  * 


For questions and issues not listed in this guide, start a conversation in the [RudderStack Slack Community](<https://rudderstack.com/join-rudderstack-slack-community>).

## General

#### Why do I need to sign up to use RudderStack Open Source?

Signing up for [RudderStack Open Source](<https://app.rudderstack.com/signup?type=opensource>) is the easiest way to set up and manage your data pipelines.

RudderStack Open Source offers an intuitive dashboard that is only used for source-destination configuration. It also provides features like [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>) for observability and debugging purposes and [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) to enhance your in-transit event data.

If you do not wish to sign up for RudderStack Open Source and want to self-host your configurations, you can use the [Control Plane Lite](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/>) utility.

Note that:

  * Control Plane Lite is now deprecated and does not work with the latest `rudder-server` versions (after v1.2).
  * Control Plane Lite does not support features like [Transformations](<https://www.rudderstack.com/docs/transformations/overview/>) and [Live Events](<https://www.rudderstack.com/docs/dashboard-guides/live-events/>).


#### What is a workspace token? Where do I get it?

The workspace token is a unique identifier for your RudderStack workspace.

> ![info](/docs/images/info.svg)
> 
> The workspace token is available only in RudderStack [Free](<https://www.rudderstack.com/pricing/>) and [Open Source](<https://app.rudderstack.com/signup?type=opensource>) plans to help you set up a self-hosted deployment.

To get your workspace token, go to **Settings** > **Workspace**. The workspace token is present in the **General** tab.

[![Workspace Token](/docs/images/rs-cloud/workspace-token.webp)](</docs/images/rs-cloud/workspace-token.webp>)

To view the workspace token, click the show icon and enter the password associated with your RudderStack account.

> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * By default, the workspace token is hidden for security purposes.
>   * Only **Admins** can access the workspace token.
> 


## Data plane setup

#### What is a data plane URL? Where do I get it?

For processing and routing your events, RudderStack requires a [data plane URL](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>).

For RudderStack Open Source, you are required to [set up your own data plane](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/data-plane-setup/>). A data plane URL typically looks like `http:localhost:8080`, where `8080` is the port where your RudderStack data plane is hosted.

#### How do I check the status of the data plane?

The format of the command to check your data plane status is:
    
    
    curl <DATA_PLANE_URL>/health
    

A sample command that checks the status of the data plane hosted at port `8080`:
    
    
    curl http://localhost:8080/health
    

You will get the following output:
    
    
    {"server":"UP", "db":"UP","acceptingEvents":"TRUE","routingEvents":"TRUE","mode":"NORMAL","goroutines":"15364", "backendConfigMode": "API", "lastSync":"2020-12-01T04:20:33Z", "lastRegulationSync":"2020-11-30T21:40:27Z"}
    

#### What are the Normal and Degraded modes when running the RudderStack server?

The RudderStack server (backend) supports two running modes:

  * **Normal** (`"mode": "NORMAL"`): In this mode, the RudderStack server runs as expected and there are no issues.
  * **Degraded** (`"mode": "DEGRADED"`): RudderStack enters the degraded mode if it keeps crashing while processing the events after a threshold restart number is reached. RudderStack still receives and stores the events in degraded mode but does not process them and route them to your specified destinations.


#### Can I set up multiple instances of RudderStack data plane?

Setting up multiple instances of RudderStack is not recommended. It can cause concurrent requests to your warehouse, leading to event failures and retries. It can also increase your costs in the case of data warehouses like Snowflake, BigQuery, etc.

> ![info](/docs/images/info.svg)
> 
> When sending events to your warehouse destinations using RudderStack Open Source, every node (data plane instance) runs the warehouse sync operations individually.

#### While running `git submodule update`, I get this error:
    
    
    Please make sure you have the correct access rights and the repository exists.
    fatal: clone of 'git@github.com:rudderlabs/rudder-transformer.git' into submodule path '/home/ubuntu/rudder-server/rudder-transformer' failed
    Failed to clone 'rudder-transformer'. Retry scheduled.
    Cloning into '/home/ubuntu/rudder-server/rudder-transformer'...
    git@github.com: Permission denied (publickey).
    fatal: Could not read from remote repository.
    

Verify if you have correctly set the SSH keys in your GitHub account as they are used when cloning using the git protocol.

For more information, see this [Stack Overflow thread](<https://stackoverflow.com/questions/25957125/git-submodule-permission-denied>).

#### How do I verify my RudderStack installation?

You can verify your RudderStack installation by sending test events and checking if they are delivered correctly.

For more information, see [Verify RudderStack Installation](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/sending-test-events/>).

#### My RudderStack setup keeps creating a new database automatically. What could be the reason?

This can happen if you have changed your workspace token. Also, ensure that the RudderStack server is running on the latest version.

#### For Docker setup, is there a recommended size for the EC2 instance?

A **c4.xlarge** or **c4.2xlarge** machine should work just fine for your Docker setup.

#### I’m running RudderStack on Docker in a GCP VM instance. I upgraded the instance to have more CPU and now the RudderStack container is stuck on this message:
    
    
    sh -c '/wait-for db:5432 -- /rudder-server'
    

This message indicates that the RudderStack server is waiting on the PostgreSQL database dependency to be up and running. Verify if your PostgreSQL container is up.

## Control plane setup

#### I am using the Control Plane Lite to generate the `workspaceConfig.json` file. But when I import this file, I get the error:
    
    
    TypeError: Cannot read property 'name' of undefined"
    

This issue can occur when you have some old data left in your browser’s local storage. Clear your browser cache and local storage and retry.

## Event volume

#### Is there any event volume limit for RudderStack Open Source?

There is no event volume limit for RudderStack Open Source.