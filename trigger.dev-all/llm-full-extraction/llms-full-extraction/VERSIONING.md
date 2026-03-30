> Sources:
> - https://trigger.dev/docs/versioning
> - https://trigger.dev/docs/deployment/atomic-deployment

# Versioning

## Versioning

We use atomic versioning to ensure that started tasks are not affected by changes to the task code.

A version is a bundle of tasks at a certain point in time.

## Version identifiers

Version identifiers look like this:

* `20240313.1` - March 13th, 2024, version 1
* `20240313.2` - March 13th, 2024, version 2
* `20240314.1` - March 14th, 2024, version 1

You can see there are two parts to the version identifier:

* The date (in reverse format)
* The version number

Versions numbers are incremented each time a new version is created for that date and environment. So it's possible to have `20240313.1` in both the `dev` and `prod` environments.

## Version locking

When a task run starts it is locked to the latest version of the code (for that environment). Once locked it won't change versions, even if you deploy new versions. This is to ensure that a task run is not affected by changes to the code.

Delayed runs are locked to the version that's active when they begin executing, not when they're enqueued.

### Child tasks and version locking

Trigger and wait functions version lock child task runs to the parent task run version. This ensures the results from child runs match what the parent task is expecting. If you don't wait then version locking doesn't apply.

| Trigger function        | Parent task version | Child task version | isLocked |
| ----------------------- | ------------------- | ------------------ | -------- |
| `trigger()`             | `20240313.2`        | Latest             | No       |
| `batchTrigger()`        | `20240313.2`        | Latest             | No       |
| `triggerAndWait()`      | `20240313.2`        | `20240313.2`       | Yes      |
| `batchTriggerAndWait()` | `20240313.2`        | `20240313.2`       | Yes      |

## Local development

When running the local server (using `npx trigger.dev dev`), every relevant code change automatically creates a new version of all tasks.

So a task run will continue running on the version it was locked to. We do this by spawning a new process for each task run. This ensures that the task run is not affected by changes to the code.

## Deployment

Every deployment creates a new version of all tasks for that environment.

## Retries and reattempts

When a task has an uncaught error it will [retry](/errors-retrying), assuming you have not set `maxAttempts` to 0. Retries are locked to the original version of the run.

## Replays

A "replay" is a new run of a task that uses the same inputs but will use the latest version of the code. This is useful when you fix a bug and want to re-run a task with the same inputs. See [replaying](/replaying) for more information.

---

## Atomic deploys

Use atomic deploys to coordinate changes to your tasks and your application.

Atomic deploys in Trigger.dev allow you to synchronize the deployment of your application with a specific version of your tasks. This ensures that your application always uses the correct version of its associated tasks, preventing inconsistencies or errors due to version mismatches.

## How it works

Atomic deploys achieve synchronization by deploying your tasks to Trigger.dev without promoting them to the default version. Instead, you explicitly specify the deployed task version in your application’s environment. Here’s the process at a glance:

1. **Deploy Tasks to Trigger.dev**: Use the Trigger.dev CLI to deploy your tasks with the `--skip-promotion` flag. This creates a new task version without making it the default.
2. **Capture the Deployment Version**: The CLI outputs the version of the deployed tasks, which you’ll use in the next step.
3. **Deploy Your Application**: Deploy your application (e.g., to Vercel), setting an environment variable like `TRIGGER_VERSION` to the captured task version.

## Vercel CLI & GitHub Actions

If you deploy to Vercel via their CLI, you can use this sample workflow that demonstrates performing atomic deploys with GitHub Actions, Trigger.dev, and Vercel:

```yml theme={"theme":"css-variables"}
name: Deploy to Trigger.dev (prod)
on:
  push:
    branches:
      - main
concurrency:
  group: ${{ github.workflow }}
  cancel-in-progress: true
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Use Node.js 20.x
        uses: actions/setup-node@v4
        with:
          node-version: "20.x"

      - name: Install dependencies
        run: npm install

      - name: Deploy Trigger.dev
        id: deploy-trigger
        env:
          TRIGGER_ACCESS_TOKEN: ${{ secrets.TRIGGER_ACCESS_TOKEN }}
        run: |
          npx trigger.dev@latest deploy --skip-promotion

      - name: Deploy to Vercel
        run: npx vercel --yes --prod -e TRIGGER_VERSION=$TRIGGER_VERSION --token $VERCEL_TOKEN
        env:
          VERCEL_TOKEN: ${{ secrets.VERCEL_TOKEN }}
          TRIGGER_VERSION: ${{ steps.deploy-trigger.outputs.deploymentVersion }}

      - name: Promote Trigger.dev Version
        run: npx trigger.dev@latest promote $TRIGGER_VERSION
        env:
          TRIGGER_ACCESS_TOKEN: ${{ secrets.TRIGGER_ACCESS_TOKEN }}
          TRIGGER_VERSION: ${{ steps.deploy-trigger.outputs.deploymentVersion }}
```

* Deploy to Trigger.dev

  * The `npx trigger.dev deploy` command uses `--skip-promotion` to deploy the tasks without setting the version as the default.
  * The step’s id: `deploy-trigger` allows us to capture the deployment version in the output (deploymentVersion).

* Deploy to Vercel:
  * The `npx vercel` command deploys the application, setting the `TRIGGER_VERSION` environment variable to the task version from the previous step.
  * The --prod flag ensures a production deployment, and -e passes the environment variable.
  * The `@trigger.dev/sdk` automatically uses the `TRIGGER_VERSION` environment variable to trigger the correct version of the tasks.

For this workflow to work, you need to set up the following secrets in your GitHub repository:

* `TRIGGER_ACCESS_TOKEN`: Your Trigger.dev personal access token. View the instructions [here](/github-actions) to learn more.
* `VERCEL_TOKEN`: Your Vercel personal access token. You can find this in your Vercel account settings.

## Vercel GitHub integration

If you're are using Vercel, chances are you are using their GitHub integration and deploying your application directly from pushes to GitHub. This section covers how to achieve atomic deploys with Trigger.dev in this setup.

### Turn off automatic promotion

By default, Vercel automatically promotes new deployments to production. To prevent this, you need to disable the auto-promotion feature in your Vercel project settings:

1. Go to your Production environment settings in Vercel at `https://vercel.com/<team-slug>/<project-slug>/settings/environments/production`
2. Disable the "Auto-assign Custom Production Domains" setting:

<img alt="Vercel project settings showing the auto-promotion setting" />

3. Hit the "Save" button to apply the changes.

Now whenever you push to your main branch, Vercel will deploy your application to the production environment without promoting it, and you can control the promotion manually.

### Deploy with Trigger.dev

Now we want to deploy that same commit to Trigger.dev, and then promote the Vercel deployment when that completes. Here's a sample GitHub Actions workflow that does this:

```yml theme={"theme":"css-variables"}
name: Deploy to Trigger.dev (prod)

on:
  push:
    branches:
      - main

concurrency:
  group: ${{ github.workflow }}
  cancel-in-progress: true

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Use Node.js 20.x
        uses: actions/setup-node@v4
        with:
          node-version: "20.x"

      - name: Install dependencies
        run: npm install

      - name: Wait for vercel deployment (push)
        id: wait-for-vercel
        uses: ludalex/vercel-wait@v1
        with:
          project-id: ${{ secrets.VERCEL_PROJECT_ID }}
          team-id: ${{ secrets.VERCEL_SCOPE_NAME }}
          token: ${{ secrets.VERCEL_TOKEN }}
          sha: ${{ github.sha }}

      - name: 🚀 Deploy Trigger.dev
        id: deploy-trigger
        env:
          TRIGGER_ACCESS_TOKEN: ${{ secrets.TRIGGER_ACCESS_TOKEN }}
        run: |
          npx trigger.dev@latest deploy

      - name: Promote Vercel deploy
        run: npx vercel promote $VERCEL_DEPLOYMENT_ID --yes --token $VERCEL_TOKEN --scope $VERCEL_SCOPE_NAME
        env:
          VERCEL_DEPLOYMENT_ID: ${{ steps.wait-for-vercel.outputs.deployment-id }}
          VERCEL_TOKEN: ${{ secrets.VERCEL_TOKEN }}
          VERCEL_SCOPE_NAME: ${{ secrets.VERCEL_SCOPE_NAME }}
```

This workflow does the following:

1. Waits for the Vercel deployment to complete using the `ludalex/vercel-wait` action.
2. Deploys the tasks to Trigger.dev using the `npx trigger.dev deploy` command. There's no need to use the `--skip-promotion` flag because we want to promote the deployment.
3. Promotes the Vercel deployment using the `npx vercel promote` command.

For this workflow to work, you need to set up the following secrets in your GitHub repository:

* `TRIGGER_ACCESS_TOKEN`: Your Trigger.dev personal access token. View the instructions [here](/github-actions) to learn more.
* `VERCEL_TOKEN`: Your Vercel personal access token. You can find this in your Vercel account settings.
* `VERCEL_PROJECT_ID`: Your Vercel project ID. You can find this in your Vercel project settings.
* `VERCEL_SCOPE_NAME`: Your Vercel team slug.

Checkout our [example repo](https://github.com/ericallam/vercel-atomic-deploys) to see this workflow in action.

<Note>
  We are using the `ludalex/vercel-wait` action above as a fork of the [official
  tj-actions/vercel-wait](https://github.com/tj-actions/vercel-wait) action because there is a bug
  in the official action that exits early if the deployment isn't found in the first check and due
  to the fact that it supports treating skipped (cancelled) Vercel deployments as valid (on by default).
  I've opened a PR for this issue [here](https://github.com/tj-actions/vercel-wait/pull/106).
</Note>

---
