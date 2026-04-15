# Managing deployments
Once you’ve finished using `modal run` or `modal serve` to iterate on your Modal
code, it’s time to deploy. A Modal deployment creates and then persists an
application and its objects, providing the following benefits: Repeated application function executions will be grouped under the deployment,
aiding observability and usage tracking. Programmatically triggering lots of
ephemeral App runs can clutter your web and CLI interfaces.
- Function calls are much faster because deployed functions are persistent and
reused, not created on-demand by calls. Learn how to trigger deployed
functions in [Invoking deployed functions](https://modal.com/docs/guide/trigger-deployed-functions).
- [Scheduled functions](https://modal.com/docs/guide/cron) will continue scheduling separate from
any local iteration you do, and will notify you on failure.
- [Web endpoints](https://modal.com/docs/guide/webhooks) keep running when you close your laptop,
and their URL address matches the deployment name.

## Creating deployments

Deployments are created using the [modal deploy command](https://modal.com/docs/reference/cli/app#modal-app-list).

Running this command on an existing deployment will redeploy the App,
incrementing its version. For detail on how live deployed apps transition
between versions, see the [Updating deployments](#updating-deployments) section.

Deployments can also be created programmatically using Modal’s [Python API](https://modal.com/docs/reference/modal.App#deploy).

## Viewing deployments

Deployments can be viewed in the [web UI](https://modal.com/apps) on an App’s “Deployment History”
page, or from the command line using the [modal app list command](https://modal.com/docs/reference/cli/app#modal-app-list).

### Deployment history on metric charts

You can overlay deployment history information on your Function’s metric charts by enabling
the Show Deployments** toggle. Each marker represents one or more deployments
that occurred within a time bucket.

Hovering over a marker shows the version number and timestamp of each deployment, plus a link to the full “Deployment History” page.

*

## Updating deployments

A deployment can deploy a new App or redeploy a new version of an existing
deployed App. It’s useful to understand how Modal handles the transition between
versions when an App is redeployed. In general, Modal aims to support
zero-downtime deployments by gradually transitioning traffic to the new version.

If the deployment involves building new versions of the Images used by the App,
the build process will need to complete successfully. The existing version of
the App will continue to handle requests during this time. Errors during the
build will abort the deployment with no change to the status of the App.

After the build completes, Modal will start to bring up new containers running
the latest version of the App. The existing containers will continue handling
requests (using the previous version of the App) until the new containers have
completed their cold start.

Once the new containers are ready, old containers will stop accepting new
requests. However, the old containers will continue running any requests they
had previously accepted. The old containers will not terminate until they have
finished processing all ongoing requests.

Any warm pool containers will also be cycled during a deployment, as the
previous version’s warm pool are now outdated.

## Deployment rollbacks
Deployment rollbacks are available on the [Team and Enterprise plans](https://modal.com/pricing). Visit [workspace settings](https://modal.com/settings/plans) to upgrade. 
To quickly reset an App back to a previous version, you can perform a deployment rollback*. Rollbacks can be triggered from either the App dashboard or the CLI.
Rollback deployments look like new deployments: they increment the version number
and are attributed to the user who triggered the rollback. But the App’s functions
and metadata will be reset to their previous state independently of your current
App codebase.

## Stopping deployments

Deployed apps can be stopped in the web UI by clicking the red “Stop app” button on
the App’s “Overview” page, or alternatively from the command line using the [modal app stop command](https://modal.com/docs/reference/cli/app#modal-app-stop).

Stopping an App is a destructive action. Apps cannot be restarted from this state;
a new App will need to be deployed from the same source files. Objects associated
with stopped deployments will eventually be garbage collected.
