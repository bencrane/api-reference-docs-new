# RudderTyper

Use RudderTyper to generate native clients for your Tracking Plans.

Available Plans

  * starter
  * growth
  * enterprise


* * *

  *  __10 minute read

  * 


[RudderTyper](<https://github.com/rudderlabs/rudder-typer>) is a tool that lets you generate strongly-typed RudderStack analytics library wrappers based on your [Tracking Plan](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>). It uses an event from your specified Tracking Plan and generates an analytics call in the supported languages.

> ![info](/docs/images/info.svg)
> 
> Use a stable version of RudderTyper (v1.x) for the latest [Tracking Plans](<https://www.rudderstack.com/docs/data-governance/tracking-plans/>) support.

[![Github Badge](https://img.shields.io/npm/v/rudder-typer?style=flat)](<https://www.npmjs.com/package/rudder-typer/>)

[![](https://img.shields.io/badge/Node.js-v20.x-7447fc.svg?logo=data:image/png;base64,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&logoColor=&logoWidth=&style=)](<>)

  
  


[![RudderTyper in action](/docs/images/readme-example.gif)](</docs/images/readme-example.gif>)

## Overview

The following steps give a high-level overview of how RudderTyper works:

  1. RudderTyper generates type-safe SDK code from a Tracking Plan by parsing it to understand the events and data types.
  2. It then creates platform-specific classes and methods that match the Tracking Plan, ensuring that only valid events and properties are used.
  3. Finally, it integrates this code into the SDKs and provides compile-time checks to catch any errors and ensure consistency in the tracking implementation.


> ![info](/docs/images/info.svg)
> 
> RudderTyper currently generates native clients for the following SDKs:
> 
>   * [JavaScript](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/>)
>   * [Android (Java)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-android-sdk/>)
>   * [iOS (Obj-C)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-ios-sdk/>)
>   * [Node.js](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-node-sdk/>)
> 


## Key features

  * Displays compile-time errors and warns you about any missing required properties, data mismatch, and any issues in the JSON schema configured in your Tracking Plan.
  * Lets you contextualize your analytics instrumentation and validate it with your event spec before deploying it to production.
  * Lets you access and validate your event names, properties, types, etc.


## Get started

The following sections will help you set up and use RudderTyper to generate your first client.

### Prerequisites

  * Make sure your [Node version](<https://nodejs.org/en/about/previous-releases>) is v20.x or above
  * Clone the [RudderTyper repository](<https://github.com/rudderlabs/rudder-typer>) in your preferred location
  * Generate a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) in your RudderStack workspace


> ![info](/docs/images/info.svg)
> 
> The workspace-level Service Access Token has **Read** permissions by default. You do not need to assign any [resource permissions](<https://www.rudderstack.com/docs/access-management/policies-overview/#resource-permissions>) while generating the token.

#### Token permissions for legacy RBAC system

If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), your workspace-level Service Access Token should have **Viewer** permission.

See [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for more information on generating the token.

[![workspace-level Service Access Token with Viewer permission](/docs/images/access-management/permissions/legacy/viewer.webp)](</docs/images/access-management/permissions/legacy/viewer.webp>)

### Quickstart

The following steps highlight the process of creating a `ruddertyper.yml` file and generate your first RudderTyper client with the specified configuration details:

  1. Run the following command to initialize RudderTyper:


    
    
    $ npx rudder-typer init  # Or initialize or quickstart
    

  2. Choose the SDK type for your RudderTyper client - you can use the up/down arrow key to navigate through the options.

[![Choose SDK for RudderTyper client](/docs/images/dev-tools/ruddertyper/choose-sdk.webp)](</docs/images/dev-tools/ruddertyper/choose-sdk.webp>)

  3. Choose the appropriate language and continue. The following image shows the language options for the Web SDK:

[![Choose language option](/docs/images/dev-tools/ruddertyper/choose-language.webp)](</docs/images/dev-tools/ruddertyper/choose-language.webp>)

  4. Enter the workspace-level Service Access Token generated above. RudderTyper uses this token to fetch all the Tracking Plans present in your workspace.

  5. Choose the Tracking Plan for which RudderTyper generates the client - this plan is automatically saved locally in a `plan.json` file.


[![Choose Tracking Plan](/docs/images/dev-tools/ruddertyper/tracking-plan.webp)](</docs/images/dev-tools/ruddertyper/tracking-plan.webp>)

  6. Choose the RudderTyper mode. You will see two options - `Production` or `Development`. See RudderTyper modes for more information on each mode.

  7. Specify the directory to store the generated RudderTyper client. You can choose an existing directory or create a new one, depending on your requirement.


[![Choose directory to store the client](/docs/images/dev-tools/ruddertyper/specify-directory.webp)](</docs/images/dev-tools/ruddertyper/specify-directory.webp>)

  8. Review the settings and select **Looks good!** to complete the process. You can select **Edit** to make any changes to the above steps.

[![Review settings](/docs/images/dev-tools/ruddertyper/review.webp)](</docs/images/dev-tools/ruddertyper/review.webp>)

RudderTyper then generates the client based on your configuration settings and stores it in the specified directory. See Configuration reference for more information on the `ruddertyper.yml` file structure.

[![Generated RudderTyper client](/docs/images/dev-tools/ruddertyper/client-generate.webp)](</docs/images/dev-tools/ruddertyper/client-generate.webp>)

#### Troubleshooting

  * If you get an error during the setup process, run the following commands to clear your cache and local storage:


    
    
    npm cache clean --force
    rm -r ~/.ruddertyper
    

  * If you get a “Your workspace does not have any Tracking Plans” error during the setup, verify that your RudderTyper client is on a stable version (v1.x).


## Commands

Command| Description  
---|---  
Initialize  
  

    
    
    $ npx rudder-typer init

| Initializes RudderTyper with a quickstart guide to generate your RudderTyper client .  
Help  
  

    
    
    $ npx rudder-typer help

| Prints the help message describing different commands available with RudderTyper.  
Update plan  
  

    
    
    $ npx rudder-typer update | u | *   (default)

| Syncs `plan.json` with RudderStack to pull the latest changes from your Tracking Plan and generates an updated development client.  
Build development client  
  

    
    
    $ npx rudder-typer build | b | d | dev | development

| Generates a development client from `plan.json` with runtime validation.  
Build production client  
  

    
    
    $ npx rudder-typer prod | p | production

| Generates a production client from `plan.json` without runtime validation .  
Print token configuration  
  

    
    
    $ npx rudder-typer token | tokens | t

| Prints the local RudderStack API token configuration.  
Print RudderTyper version  
  

    
    
    $ npx rudder-typer version

| Prints the RudderTyper CLI version.  
  
## CLI arguments

Run the help command (`npx rudder-typer help`) to get the below list of CLI arguments that you can use with RudderTyper:

Argument| Description  
---|---  
`config`| Optional path to a `ruddertyper.yml` (or a directory with `ruddertyper.yml`).  
`debug`| Optional (hidden) flag to turn on/off debug mode.  
`version` / `v`| Prints the RudderTyper CLI version.  
`help` / `h`| Prints help on a command.  
  
## RudderTyper modes

RudderTyper operates in two distinct modes: **Development** and **Production** mode. Each mode serves a specific purpose in the analytics implementation workflow. By utilizing the required mode, you can streamline the process of implementing and managing analytics with RudderTyper.

#### Development mode

This mode is designed to facilitate testing and validating your changes before the events go live.

This mode is suitable for local development and debugging and helps you:

  * Validate the JSON schema to ensure correctness.
  * Verify the tracking events against the defined Tracking Plan.
  * Include additional validation logic to catch potential errors early.


#### Production mode

This mode is optimized for deployment and ensures seamless event tracking in live environments.

This mode is suitable for staging and production environments and helps you:

  * Generate production-ready, optimized code.
  * Adhere strictly to the validated schema to maintain consistency.
  * Remove unnecessary validation and debugging logic for efficiency.


## Configuration reference

RudderTyper stores its configuration in a `ruddertyper.yml` file in the root of your repository.

A sample configuration looks like the following:
    
    
    # RudderStack RudderTyper configuration reference (https://github.com/rudderlabs/rudder-typer)
    # Run `npx rudder-typer` to regenerate a client with the latest versions of these events.
    
    scripts:
      # You can supply a RudderStack service access token using a `scripts.token` command. The output of `script.token` command should be a valid RudderStack API token.
      token: source .env; echo $RUDDERTYPER_TOKEN
    
      # You can supply the email address linked to your workspace using a `scripts.email` command.The output of `script.email` command should be an email address registered with your workspace.
      email: source .env; echo $EMAIL
    
      # You can format any of RudderTyper's auto-generated files using a `scripts.after` command.
      # See `Formatting Generated Files` below.
      after: ./node_modules/.bin/prettier --write analytics/plan.json
    
    client:
      # The RudderStack SDK you are generating the client for
      # Valid values: analytics.js, analytics-node, analytics-ios, analytics-android.
      sdk: analytics.js
    
      # The target language for your RudderTyper client.
      # Valid values: javascript, typescript, objective-c, swift, java.
      language: typescript
    
      # JavaScript Transpilation Settings
      # Valid values: 'ES3','ES5','ES2015','ES2016','ES2017','ES2018','ES2019','ESNext','Latest'
      scriptTarget: "ES5"
    
      # Valid values: 'CommonJS','AMD','UMD','System','ES2015','ESNext'
      moduleTarget: "ESNext"
    
    trackingPlans:
      # The RudderStack Tracking Plan that you are generating a client for.
      # Provide your workspace slug and Tracking Plan id
      # You also need to supply a path to a directory to save your RudderTyper client.
      - id: <TRACKING_PLAN_ID>
        workspaceSlug: rudderstack-demo
        path: ./analytics
    
        # Valid values: v1 (old Tracking Plan), v2 (new Tracking Plan format)
        APIVersion: v2
    

Note the following:

  * Store `token` and `email` in a `.env` file created in the same directory as `ruddertyper.yml` to ensure the scripts automatically use these values. A sample `.env` file is shown below:


    
    
    RUDDERTYPER_TOKEN=<SERVICE_ACCESS_TOKEN>
    EMAIL=<EMAIL_ADDRESS>
    

  * You can get the `id` field by going to the Tracking Plan in the RudderStack dashboard. For example, `https://app.rudderstack.com/trackingPlans/<TRACKING_PLAN_ID>`.


## Integrate RudderTyper client with SDK

This section includes the steps to integrate your RudderTyper-generated client with your app across different RudderStack SDKs.

  1. Import all files in the client generated by RudderTyper as a package in your project.
  2. Make the calls using the RudderTyper client, as shown:


    
    
    // Import your auto-generated RudderTyper client:
    import com.rudderstack.generated.*
    
      // Issue your first RudderTyper track call
      RudderTyperAnalytics.with(this).orderCompleted(
        OrderCompleted.Builder()
        .orderID("ck-f306fe0e-cc21-445a-9caa-08245a9aa52c")
        .total(39.99)
        .build()
      );
    

  1. Import your RudderTyper client into your project using XCode.


> ![warning](/docs/images/warning.svg)
> 
> If you place the generated files into a folder within your project, import the project as a group, **not** as a folder reference.

  2. Make the calls using the RudderTyper client, as shown:


    
    
    // Import your auto-generated RudderTyper client:
    #import "RSRudderTyperAnalytics.h"
    
    // Issue your first RudderTyper track call
    [RSRudderTyperAnalytics orderCompletedWithOrderID: "ck-f306fe0e-cc21-445a-9caa-08245a9aa52c" total: @39.99];
    

There are two ways to get started with RudderTyper in your browser:

### Using JavaScript SDK snippet

  1. Paste the [JavaScript SDK snippet](<https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/quickstart/#using-cdn>) from the RudderStack dashboard in your HTML file.
  2. If you use TypeScript, add `@rudderstack/analytics-js` as a dev dependency:


    
    
    npm install --save-dev  @rudderstack/analytics-js
    

  3. Run the below command to generate a bundle from the RudderTyper client:


    
    
    npx browserify analytics/index.js --standalone rudderTyper >  rudderTyperBundle.js
    

  4. For the TypeScript analytics client, add the npm package `tsify` as a dependency and run the below command to generate the bundle:


    
    
    npx browserify analytics/index.ts -p [ tsify ] --standalone rudderTyper >  rudderTyperBundle.js
    

  5. Import your RudderTyper client and send events.


    
    
    <script>
      // Add the JavaScript SDK snippet from https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/quickstart/#using-cdn
    </script>
    <script src="./rudderTyperBundle.js"></script>
    <script>
      rudderTyper.setRudderTyperOptions({
        analytics: rudderanalytics,
      });
      rudderTyper.orderCompleted({
        orderID: 'ck-f306fe0e-cc21-445a-9caa-08245a9aa52c',
        total: 39.99,
      });
    </script>
    

See the [sample application](<https://github.com/rudderlabs/rudder-typer/tree/develop/examples/js-cdn-typescript>) for more information.

### Using NPM

Import the RudderTyper-generated client and make the calls if your framework supports them.
    
    
    // Import RudderStack JS SDK and initialize it
    import { RudderAnalytics } from '@rudderstack/analytics-js';
    // Import your auto-generated RudderTyper client:
    import { RudderTyperAnalytics } from './analytics/index';
    
    const rudderAnalytics = new RudderAnalytics();
    rudderAnalytics.load(WRITE_KEY, DATA_PLANE_URL, {});
    
    // Pass in your @rudderstack/analytics-js instance to RudderTyper client
    RudderTyperAnalytics.setRudderTyperOptions({
      analytics: rudderAnalytics,
    });
    
    // Issue your first RudderTyper track call
    RudderTyperAnalytics.orderCompleted({
      orderID: 'ck-f306fe0e-cc21-445a-9caa-08245a9aa52c',
      total: 39.99,
    });
    

Note that:

  * Replace `WRITE_KEY` and `DATA_PLANE_URL` in the above snippet with your source write key and [data plane URL](<https://www.rudderstack.com/docs/dashboard-guides/overview/#connections>) respectively.
  * Make sure to run `npx rudder-typer` to regenerate your RudderTyper client every time you update the Tracking Plan.


See the [sample application](<https://github.com/rudderlabs/rudder-typer/tree/develop/examples/js-npm-typescript>) for more information.

Import the RudderTyper-generated client and start making calls, as shown:
    
    
    // Import RudderStack Node.js SDK and initialize it
    const RudderAnalytics = require('@rudderstack/rudder-sdk-node');
    
    const client = new RudderAnalytics(WRITE_KEY, {
      dataPlaneUrl: DATA_PLANE_URL,
      // Other initialization options
    });
    
    const RudderTyperAnalytics = require('./analytics/index');
    // Pass in your @rudderstack/rudder-sdk-node instance to RudderTyper.
    RudderTyperAnalytics.setRudderTyperOptions({
      analytics: client,
    });
    
    // Issue your first RudderTyper track call
    RudderTyperAnalytics.orderCompleted({
      orderID: 'ck-f306fe0e-cc21-445a-9caa-08245a9aa52c',
      total: 39.99,
    });
    

## How RudderTyper validates events based on Tracking Plan

**Case 1: Source is connected to a Tracking Plan**

Scenario| Behavior  
---|---  
RudderTyper configured with the same Tracking Plan ID and version| RudderStack validates the events with the specified Tracking Plan and shows the violations accordingly.  
RudderTyper configured with the same Tracking Plan ID but different version| RudderTyper validates the events and shows the violations based on the Tracking Plan version used to generate it, **even if** the Tracking Plan has undergone revisions since then.  
  
For example, if you generate RudderTyper with Tracking Plan version v5 and then revise the Tracking Plan version to v6, then RudderTyper validates events and shows violations based on Tracking Plan v5, not v6.  
RudderTyper configured with a different Tracking Plan ID| RudderStack validates the events with the Tracking Plan connected to the source in the dashboard and shows the violations accordingly.  
  
**Case 2: Source is not connected to a Tracking Plan**

In this case, RudderStack does not proceed to the Tracking Plan validation stage. As a result, no violations are shown.

## Contribute

  * To submit a bug report or feature request, file an issue [here](<https://github.com/rudderlabs/rudder-typer/issues>).
  * To build on a RudderTyper feature or propose support for a new language, see the [contributor’s documentation](<https://github.com/rudderlabs/rudder-typer/blob/master/.github/CONTRIBUTING.md>).


## References

  * [Download Node](<https://nodejs.org/en/download/package-manager>). You will also get the necessary commands to set up Node.js and verify your installation.
  * [Commands to build and run the RudderTyper client](<https://github.com/rudderlabs/rudder-typer/blob/master/.github/CONTRIBUTING.md#developing-on-ruddertyper>)
  * [Yarn reference](<https://classic.yarnpkg.com/lang/en/docs/install/#mac-stable>)


## FAQ

#### Can I use a different Service Access Token for authenticating RudderTyper?

Yes, you can.

  1. Follow steps 1 to 3 from the Quickstart section.
  2. In the **Enter Rudder API token** window, choose **No, provide a different token**.

[![Choose different SAT option](/docs/images/dev-tools/ruddertyper/sat.webp)](</docs/images/dev-tools/ruddertyper/sat.webp>)

#### Why am I seeing events validated against different Tracking Plan versions in the live events viewer?

Different events may be validated against different Tracking Plan versions because RudderStack validates each event against the **specific version** that was used to instrument it.

This behavior ensures that each event is validated against the exact rules it was designed to follow, and prevents false validation errors when Tracking Plans evolve over time.

See [Tracking Plan observability](<https://www.rudderstack.com/docs/data-governance/tracking-plans/observability/#how-validation-works>) for more details.