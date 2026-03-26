# Verify RudderStack Installation

Verify your RudderStack installation by sending test events.

* * *

  * __3 minute read

  * 


Before using RudderStack, it is highly recommended to verify that your installation works as expected by sending some test events. You can use any of the following approaches:

  * Use the bundled shell script
  * Use RudderStack’s HTTP API


> ![info](/docs/images/info.svg)
> 
> This guide assumes that you have already installed and set up RudderStack in your preferred environment.

## Bundled shell script

The [`rudder-server` GitHub repository](<https://github.com/rudderlabs/rudder-server>) contains a bundled shell script that generates test events. Clone the repository by running the following command:
    
    
    git clone https://github.com/rudderlabs/rudder-server.git
    

Then, follow the steps below to send test events.

### Step 1: Get source write key

#### RudderStack Open Source dashboard

If you have signed up for [RudderStack open source](<https://app.rudderstack.com/signup?type=opensource>), follow these steps:

  1. Log in to your RudderStack Open Source dashboard.
  2. Set up a source and connect it to a destination.
  3. You can find the write key in the **Setup** tab of your source.

[![RudderStack source write key](/docs/images/rudderstack-open-source/write-key.webp)](</docs/images/rudderstack-open-source/write-key.webp>)

#### Self-hosted control plane

If you are self-hosting the control plane using [Control Plane Lite](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/>), follow these steps:

  1. Set up a source and connect it to a destination.
  2. Note the write key for the source:

[![Control plane lite source write Key](/docs/images/rudderstack-open-source/control-plane-lite-source-writekey.webp)](</docs/images/rudderstack-open-source/control-plane-lite-source-writekey.webp>)

### Step 2: Send test events

To send test events, follow the steps in the sections below depending on your preferred setup:

#### Local setup

  1. Navigate to the folder where RudderStack is installed.
  2. Run the following command:


    
    
    ./scripts/generate-event <WRITE_KEY> <DATA_PLANE_URL>/v1/batch
    

> ![info](/docs/images/info.svg)
> 
> Replace `<WRITE_KEY>` and `<DATA_PLANE_URL>` with your source write key and [data plane URL](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>).

  3. Go to your source in the RudderStack Open Source dashboard and check the **Live Events** tab to verify if the events are delivered.

[![Source live events](/docs/images/rudderstack-open-source/source-live-events.webp)](</docs/images/rudderstack-open-source/source-live-events.webp>)

An example is shown below:

[![Test Event](/docs/images/rudderstack-open-source/test-event.webp)](</docs/images/rudderstack-open-source/test-event.webp>)

#### Docker setup

  1. Run the following command:


    
    
    docker exec -ti \
        <rudder-server-running-container-id> \
        ./scripts/generate-event <WRITE_KEY> <DATA_PLANE_URL>/v1/batch
    

> ![info](/docs/images/info.svg)
> 
> Replace `<WRITE_KEY>` and `<DATA_PLANE_URL>` with your source write key and [data plane URL](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>).

  2. Go to your source in the RudderStack Open Source dashboard and check the **Live Events** tab to verify if the events are delivered.


> ![warning](/docs/images/warning.svg)
> 
> Unlike RudderStack Open Source, the control plane set up using [Control Plane Lite](<https://www.rudderstack.com/docs/get-started/rudderstack-open-source/control-plane-lite/>) does not support the **Live Events** feature.

If you supply an invalid source write key or data plane URL, you will get the following error:

[![Test Event error](/docs/images/rudderstack-open-source/test-event-error.webp)](</docs/images/rudderstack-open-source/test-event-error.webp>)

## RudderStack HTTP API

To send test events using the [RudderStack HTTP API](<https://www.rudderstack.com/docs/api/http-api/>), follow these steps:

  1. Import this [Postman collection](<https://www.getpostman.com/collections/480307c55ad2b9dd4e27>).
  2. Edit the variables `source_write_key` and `data_plane_url` in this collection with your source write key and [data plane URL](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>).


RudderStack uses **Basic Authentication** for authenticating all HTTP requests. The HTTP Basic Authentication requires a user name and password, where:

  * Username is the `source_write_key`.
  * Password is an empty string (`""`).


  3. Send the test API requests.
  4. Go to your source in the RudderStack Open Source dashboard and check the **Live Events** tab to verify if the events are delivered.