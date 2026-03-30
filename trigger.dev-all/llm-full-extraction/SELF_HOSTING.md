> Sources:
> - https://trigger.dev/docs/self-hosting/overview
> - https://trigger.dev/docs/self-hosting/docker
> - https://trigger.dev/docs/self-hosting/kubernetes
> - https://trigger.dev/docs/self-hosting/env/supervisor
> - https://trigger.dev/docs/self-hosting/env/webapp

# Self-Hosting

## Overview

You can self-host Trigger.dev on your own infrastructure.

Self-hosting Trigger.dev means you run and manage the platform on your own infrastructure, giving you full control over your environment, deployment process, and the URLs you expose the service on.

You are responsible for provisioning resources, handling updates, and managing any security, scaling or reliability challenges that arise.

We provide version-tagged releases for self-hosted deployments. It's highly advised to use these tags exclusively and keep them locked with your CLI version.

## Should you self-host?

Trigger.dev Cloud is fully managed, scalable, and comes with dedicated support. For most users, it offers the best experience. However, if you have specific requirements around data residency, compliance, or infrastructure control, self-hosting may be the right choice for you.

The self-hosted version is functionally the same as Trigger.dev Cloud with [some exceptions](#feature-comparison), but our managed Cloud infrastructure is designed for high availability, security, and scale.

Because we don't manage self-hosted instances, we cannot guarantee how Trigger.dev will perform on your infrastructure. You assume all responsibility and risk for your deployment, including security, uptime, and data integrity.

For more details, carry on reading and follow our guides for instructions on setting up a self-hosted Trigger.dev instance. If you prefer a managed experience, you can [sign up](https://cloud.trigger.dev/login) for our Cloud offering instead - we have a generous [free tier](https://trigger.dev/pricing) for you to try it out.

## Architecture

The self-hosted version is a set of containers running on your own infrastructure. It's split into two parts that can be scaled independently:

* **Webapp**: includes the dashboard and other services like Redis and Postgres.
* **Worker**: includes the supervisor and the runners that execute your tasks.

<img alt="Self-hosting architecture" />

## Feature comparison

While [limits](#limits) are generally configurable when self-hosting, some features are only available on Trigger.dev Cloud:

| Feature           | Cloud | Self-hosted | Description                             |
| :---------------- | :---- | :---------- | :-------------------------------------- |
| Warm starts       | ✅     | ❌           | Faster startups for consecutive runs    |
| Auto-scaling      | ✅     | ❌           | No need for manual worker node scaling  |
| Checkpoints       | ✅     | ❌           | Non-blocking waits, less resource usage |
| Dedicated support | ✅     | ❌           | Direct access to our support team       |
| Community support | ✅     | ✅           | Access to our Discord community         |
| ARM support       | ✅     | ✅           | ARM-based deployments                   |

## Limits

Most of the [limits](/limits) are configurable when self-hosting, with some hardcoded exceptions. You can configure them via environment variables on the [webapp](/self-hosting/env/webapp) container.

| Limit             | Configurable | Hardcoded value |
| :---------------- | :----------- | :-------------- |
| Concurrency       | ✅            | —               |
| Rate limits       | ✅            | —               |
| Queued tasks      | ✅            | —               |
| Task payloads     | ✅            | —               |
| Batch payloads    | ✅            | —               |
| Task outputs      | ✅            | —               |
| Batch size        | ✅            | —               |
| Log size          | ✅            | —               |
| Machines          | ✅            | —               |
| OTel limits       | ✅            | —               |
| Log retention     | —            | Never deleted   |
| I/O packet length | ❌            | 128KB           |
| Alerts            | ❌            | 100M            |
| Schedules         | ❌            | 100M            |
| Team members      | ❌            | 100M            |
| Preview branches  | ❌            | 100M            |

### Machine overrides

You can override the machine type for a task by setting the `MACHINE_PRESETS_OVERRIDE_PATH` environment variable to a JSON file with the following structure.

```json theme={"theme":"css-variables"}
{
  "defaultMachine": "small-1x",
  "machines": {
    "micro": { "cpu": 0.25, "memory": 0.25 },
    "small-1x": { "cpu": 0.5, "memory": 0.5 },
    "small-2x": { "cpu": 1, "memory": 1 }
    // ...etc
  }
}
```

All fields are optional. Partial overrides are supported:

```json theme={"theme":"css-variables"}
{
  "defaultMachine": "small-2x",
  "machines": {
    "small-1x": { "memory": 2 }
  }
}
```

## Community support

It's dangerous to go alone! Join the self-hosting channel on our [Discord server](https://discord.gg/NQTxt5NA7s).

## Next steps

<CardGroup>
  <Card title="Docker compose" icon="docker" href="/self-hosting/docker">
    Learn how to self-host Trigger.dev with Docker compose.
  </Card>

  <Card title="Kubernetes" icon="dharmachakra" href="/self-hosting/kubernetes">
    Learn how to self-host Trigger.dev with Kubernetes.
  </Card>
</CardGroup>

---

## Docker compose

You can self-host Trigger.dev on your own infrastructure using Docker.

The following instructions will use docker compose to spin up a Trigger.dev instance. Make sure to read the self-hosting [overview](/self-hosting/overview) first.

As self-hosted deployments tend to have unique requirements and configurations, we don't provide specific advice for securing your deployment, scaling up, or improving reliability.

Should the burden ever get too much, we'd be happy to see you on [Trigger.dev cloud](https://trigger.dev/pricing) where we deal with these concerns for you.

**Warning:** This guide alone is unlikely to result in a production-ready deployment. Security, scaling, and reliability concerns are not fully addressed here.

## What's new?

Goodbye v3, hello v4! We made quite a few changes:

* **Much simpler setup.** The provider and coordinator are now combined into a single supervisor. No more startup scripts, just `docker compose up`.
* **Automatic container cleanup.** The supervisor will automatically clean up containers that are no longer needed.
* **Support for multiple worker machines.** This is a big one, and we're very excited about it! You can now scale your workers horizontally as needed.
* **Resource limits enforced by default.** This means that tasks will be limited to the total CPU and RAM of the machine preset, preventing noisy neighbours.
* **No direct Docker socket access.** The compose file now comes with [Docker Socket Proxy](https://github.com/Tecnativa/docker-socket-proxy) by default. Yes, you want this.
* **No host networking.** All containers are now running with network isolation, using only the network access they need.
* **No checkpoint support.** This was only ever experimental when self-hosting and not recommended. It caused a bunch of issues. We decided to focus on the core features instead.
* **Built-in container registry and object storage.** You can now deploy and execute tasks without needing third party services for this.
* **Improved CLI commands.** You don't need any additional flags to deploy anymore, and there's a new command to easily `switch` between profiles.
* **Whitelisting for GitHub OAuth.** Any whitelisted email addresses will now also apply to sign ins via GitHub, unlike v3 where they only applied to magic links.

## Requirements

These are the minimum requirements for running the webapp and worker components. They can run on the same, or on separate machines.

It's fine to run everything on the same machine for testing. To be able to scale your workers, you will want to run them separately.

### Prerequisites

To run the webapp and worker components, you will need:

* [Docker](https://docs.docker.com/get-docker/) 20.10.0+
* [Docker Compose](https://docs.docker.com/compose/install/) 2.20.0+

### Webapp

This machine will host the webapp, postgres, redis, and related services.

* 3+ vCPU
* 6+ GB RAM

### Worker

This machine will host the supervisor and all of the runs.

* 4+ vCPU
* 8+ GB RAM

How many workers and resources you need will depend on your workloads and concurrency requirements.

For example:

* 10 concurrency x `small-1x` (0.5 vCPU, 0.5 GB RAM) = 5 vCPU and 5 GB RAM
* 20 concurrency x `small-1x` (0.5 vCPU, 0.5 GB RAM) = 10 vCPU and 10 GB RAM
* 100 concurrency x `small-1x` (0.5 vCPU, 0.5 GB RAM) = 50 vCPU and 50 GB RAM
* 100 concurrency x `small-2x` (1 vCPU, 1 GB RAM) = 100 vCPU and 100 GB RAM

You may need to spin up multiple workers to handle peak concurrency. The good news is you don't have to know the exact numbers upfront. You can start with a single worker and add more as needed.

## Setup

### Webapp

1. Clone the repository

```bash theme={"theme":"css-variables"}
git clone --depth=1 https://github.com/triggerdotdev/trigger.dev
cd trigger.dev/hosting/docker
```

2. Create a `.env` file

```bash theme={"theme":"css-variables"}
cp .env.example .env
```

3. Start the webapp

```bash theme={"theme":"css-variables"}
cd webapp
docker compose up -d
```

4. Configure the webapp using the [environment variables](/self-hosting/env/webapp) in your `.env` file, then apply the changes:

```bash theme={"theme":"css-variables"}
docker compose up -d
```

5. You should now be able to access the webapp at `http://localhost:8030`. When logging in, check the container logs for the magic link:

```bash theme={"theme":"css-variables"}
docker compose logs -f webapp
```

6. (optional) To initialize a new project, run the following command:

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest init -p <project-ref> -a http://localhost:8030
```

### Worker

1. Clone the repository

```bash theme={"theme":"css-variables"}
git clone --depth=1 https://github.com/triggerdotdev/trigger.dev
cd trigger.dev/hosting/docker
```

2. Create a `.env` file

```bash theme={"theme":"css-variables"}
cp .env.example .env
```

3. Start the worker

```bash theme={"theme":"css-variables"}
cd worker
docker compose up -d
```

4. Configure the supervisor using the [environment variables](/self-hosting/env/supervisor) in your `.env` file, including the [worker token](#worker-token).

5. Apply the changes:

```bash theme={"theme":"css-variables"}
docker compose up -d
```

6. Repeat as needed for additional workers.

### Combined

If you want to run the webapp and worker on the same machine, just replace the `up` command with the following:

```bash theme={"theme":"css-variables"}
# Run this from the /hosting/docker directory
docker compose -f webapp/docker-compose.yml -f worker/docker-compose.yml up -d
```

## Worker token

When running the combined stack, worker bootstrap is handled automatically. When running the webapp and worker separately, you will need to manually set the worker token.

On the first run, the webapp will generate a worker token and store it in a shared volume. It will also print the token to the console. It should look something like this:

```bash theme={"theme":"css-variables"}
==========================
Trigger.dev Bootstrap - Worker Token

WARNING: This will only be shown once. Save it now!

Worker group:
bootstrap

Token:
tr_wgt_fgfAEjsTmvl4lowBLTbP7Xo563UlnVa206mr9uW6

If using docker compose, set:
TRIGGER_WORKER_TOKEN=tr_wgt_fgfAEjsTmvl4lowBLTbP7Xo563UlnVa206mr9uW6

Or, if using a file:
TRIGGER_WORKER_TOKEN=file:///home/node/shared/worker_token

==========================
```

You can then uncomment and set the `TRIGGER_WORKER_TOKEN` environment variable in your `.env` file.

Don't forget to restart the worker container for the changes to take effect:

```bash theme={"theme":"css-variables"}
# Run this from the /hosting/docker/worker directory
docker compose down
docker compose up -d
```

### Creating additional worker groups

To create additional worker groups beyond the bootstrap group, use the admin API endpoint. This requires admin privileges.

**Making a user admin:**

* **New users**: Set `ADMIN_EMAILS` environment variable (regex pattern) before user creation.
* **Existing users**: Set `admin = true` in the `user` table in your database.

**Creating a worker group:**

```bash theme={"theme":"css-variables"}
api_url=http://localhost:8030
wg_name=my-worker
admin_pat=tr_pat_...

curl -X POST \
  "$api_url/admin/api/v1/workers" \
  -H "Authorization: Bearer $admin_pat" \
  -H "Content-Type: application/json" \
  -d "{\"name\": \"$wg_name\"}"
```

The response includes a `token` field if the worker group is newly created.

## Registry setup

The registry is used to store and pull deployment images. When testing the stack locally, the defaults should work out of the box.

When deploying to production, you will need to set the correct URL and generate secure credentials for the registry.

### Default settings

The default settings for the registry are:

* Registry: `localhost:5000`
* Username: `registry-user`
* Password: `very-secure-indeed`

You should change these before deploying to production, especially the password. You can find more information about how to do this in the official [registry docs](https://github.com/distribution/distribution/blob/735c161b53e7faf81a21ba94c55ac9edee081cd9/docs/deploying.md#native-basic-auth).

**Note:** This will require modifying the default `.htpasswd` file located at `./hosting/docker/registry/auth.htpasswd` of the repo root.

### Logging in

When self-hosting, builds run locally. You will have to login to the registry on every machine that runs the `deploy` command. You should only have to do this once:

```bash theme={"theme":"css-variables"}
docker login -u <username> <registry>
```

This will prompt for the password. Afterwards, the deploy command should work as expected.

## Object storage

This is mainly used for large payloads and outputs. There are a few simple steps to follow to get started.

### Default settings

The default settings for the object storage are:

* Endpoint: `http://localhost:9000`
* Username: `admin`
* Password: `very-safe-password`

You should change these before deploying to production, especially the password.

### Setup

<Note>
  The `packets` bucket is created by default. In case this doesn't work, you can create it manually.
</Note>

1. Login to the dashboard: `http://localhost:9001`

2. Create a bucket named `packets`.

3. For production, you will want to set up a dedicated user and not use the root credentials above.

## Authentication

The specific set of variables required will depend on your choice of email transport or alternative login methods like GitHub OAuth.

### Magic link

By default, magic link auth is the only login option. If the `EMAIL_TRANSPORT` env var is not set, the magic links will be logged by the webapp container and not sent via email.

#### Resend

```bash theme={"theme":"css-variables"}
EMAIL_TRANSPORT=resend
FROM_EMAIL=
REPLY_TO_EMAIL=
RESEND_API_KEY=<your_resend_api_key>
```

#### SMTP

Note that setting `SMTP_SECURE=false` does *not* mean the email is sent insecurely.
This simply means that the connection is secured using the modern STARTTLS protocol command instead of implicit TLS.
You should only set this to true when the SMTP server host directs you to do so (generally when using port 465)

```bash theme={"theme":"css-variables"}
EMAIL_TRANSPORT=smtp
FROM_EMAIL=
REPLY_TO_EMAIL=
SMTP_HOST=<your_smtp_server>
SMTP_PORT=587
SMTP_SECURE=false
SMTP_USER=<your_smtp_username>
SMTP_PASSWORD=<your_smtp_password>
```

#### AWS SES

Credentials are to be supplied as with any other program using the AWS SDK.

In this scenario, you would likely either supply the additional environment variables `AWS_REGION`, `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` or, when running on AWS, use credentials supplied by the EC2 IMDS.

```bash theme={"theme":"css-variables"}
EMAIL_TRANSPORT=aws-ses
FROM_EMAIL=
REPLY_TO_EMAIL=
```

### GitHub OAuth

To authenticate with GitHub, you will need to set up a GitHub OAuth app. It needs a callback URL `https://<your_webapp_domain>/auth/github/callback` and you will have to set the following env vars:

```bash theme={"theme":"css-variables"}
AUTH_GITHUB_CLIENT_ID=<your_client_id>
AUTH_GITHUB_CLIENT_SECRET=<your_client_secret>
```

### Restricting access

All email addresses can sign up and log in this way. If you would like to restrict this, you can use the `WHITELISTED_EMAILS` env var. For example:

```bash theme={"theme":"css-variables"}
# every email that does not match this regex will be rejected
WHITELISTED_EMAILS="^(authorized@yahoo\.com|authorized@gmail\.com)$"
```

This will apply to all auth methods including magic link and GitHub OAuth.

## Version locking

There are several reasons to lock the version of your Docker images:

* **Backwards compatibility.** We try our best to maintain compatibility with older CLI versions, but it's not always possible. If you don't want to update your CLI, you can lock your Docker images to that specific version.
* **Ensuring full feature support.** Sometimes, new CLI releases will also require new or updated platform features. Running unlocked images can make any issues difficult to debug. Using a specific tag can help here as well.

By default, the images will point at the latest versioned release via the `latest` tag. You can override this by specifying a different tag in your `.env` file. For example:

```bash theme={"theme":"css-variables"}
TRIGGER_IMAGE_TAG=v4.0.0
```

## Troubleshooting

* **Deployment fails at the push step.** The machine running `deploy` needs registry access. See the [registry setup](#registry-setup) section for more details.

* **Magic links don't arrive.** The webapp container needs to be able to send emails. You probably need to set up an email transport. See the [authentication](#authentication) section for more details.

  You should check the logs of the webapp container to see the magic link:

  ```bash theme={"theme":"css-variables"}
  # Run this from the /hosting/docker/webapp directory
  docker compose logs -f webapp
  ```

* **Deploy fails with `ERROR: schema "graphile_worker" does not exist`.** This error occurs when Graphile Worker migrations fail to run during webapp startup. Check the webapp logs for certificate-related errors like `self-signed certificate in certificate chain`. This is often caused by PostgreSQL SSL certificate issues when using an external PostgreSQL instance with SSL enabled. Ensure that both the webapp and supervisor containers have access to the same CA certificate used by your PostgreSQL instance. You can configure this by mounting the certificate file and setting the `NODE_EXTRA_CA_CERTS` environment variable to point to the certificate path. Once the certificate issue is resolved, the migrations will complete and create the required `graphile_worker` schema.

* **ClickHouse migrations say "no migrations to run" but schema is missing.** The goose migration tracker is out of sync. Exec into the webapp container, set the GOOSE env vars (from webapp startup logs), and run `goose reset && goose up`.

  <Warning>
    **Data Loss Warning:** The `goose reset` command is destructive and will drop the entire schema. Make sure to backup your data and confirm you are running this in a non-production environment before executing this command.
  </Warning>

## CLI usage

This section highlights some of the CLI commands and options that are useful when self-hosting. Please check the [CLI reference](/cli-introduction) for more in-depth documentation.

### Login

To avoid being redirected to [Trigger.dev Cloud](https://cloud.trigger.dev) when using the CLI, you need to specify the URL of your self-hosted instance with the `--api-url` or `-a` flag. For example:

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest login -a http://trigger.example.com
```

Once you've logged in, you shouldn't have to specify the URL again with other commands.

### Profiles

You can specify a profile when logging in. This allows you to easily use the CLI with multiple instances of Trigger.dev. For example:

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest login -a http://trigger.example.com \
    --profile self-hosted
```

Logging in with a new profile will also make it the new default profile.

To use a specific profile, you can use the `--profile` flag with other commands:

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest dev --profile self-hosted
```

To list all your profiles, use the `list-profiles` command:

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest list-profiles
```

To remove a profile, use the `logout` command:

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest logout --profile self-hosted
```

To switch to a different profile, use the `switch` command:

```bash theme={"theme":"css-variables"}
# To run interactively
npx trigger.dev@latest switch

# To switch to a specific profile
npx trigger.dev@latest switch self-hosted
```

### Whoami

It can be useful to check you are logged into the correct instance. Running this will also show the API URL:

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest whoami
```

## CI / GitHub Actions

When running the CLI in a CI environment, your login profiles won't be available. Instead, you can use the `TRIGGER_API_URL` and `TRIGGER_ACCESS_TOKEN` environment
variables to point at your self-hosted instance and authenticate.

For more detailed instructions, see the [GitHub Actions guide](/github-actions).

## Telemetry

By default, the Trigger.dev webapp sends telemetry data to our servers. This data is used to improve the product and is not shared with third parties. If you would like to opt-out of this, you can set the `TRIGGER_TELEMETRY_DISABLED` environment variable on the webapp container. The value doesn't matter, it just can't be empty. For example:

```yaml theme={"theme":"css-variables"}
services:
  webapp:
    ...
    environment:
      TRIGGER_TELEMETRY_DISABLED: 1
```

---

## Kubernetes

You can self-host Trigger.dev in Kubernetes using our official Helm chart.

The following instructions will help you deploy Trigger.dev to Kubernetes using our official Helm chart. Make sure to read the self-hosting [overview](/self-hosting/overview) first.

As self-hosted deployments tend to have unique requirements and configurations, we don't provide specific advice for securing your deployment, scaling up, or improving reliability.

Should the burden ever get too much, we'd be happy to see you on [Trigger.dev cloud](https://trigger.dev/pricing) where we deal with these concerns for you.

**Warning:** This guide alone is unlikely to result in a production-ready deployment. Security, scaling, and reliability concerns are not fully addressed here.

## Requirements

### Prerequisites

* Kubernetes cluster 1.19+
* Helm 3.8+
* Kubectl with cluster access

### Resources

The following are minimum requirements for running the entire stack on Kubernetes:

**Cluster resources:**

* 6+ vCPU total
* 12+ GB RAM total
* Persistent volume support

**Individual components:**

* **Webapp**: 1 vCPU, 2 GB RAM
* **Supervisor**: 1 vCPU, 1 GB RAM
* **PostgreSQL**: 1 vCPU, 2 GB RAM
* **Redis**: 0.5 vCPU, 1 GB RAM
* **ClickHouse**: 1 vCPU, 2 GB RAM
* **Object Storage**: 0.5 vCPU, 1 GB RAM
* **Workers**: Depending on concurrency and machine preset

These requirements scale based on your task concurrency and can be adjusted via the `resources` section in your `values.yaml`. For example:

```yaml theme={"theme":"css-variables"}
webapp:
  resources:
    requests:
      cpu: 500m
      memory: 1Gi
    limits:
      cpu: 2000m
      memory: 4Gi
```

## Installation

### Quick start

1. Install with default values (for testing only):

```bash theme={"theme":"css-variables"}
helm upgrade -n trigger --install trigger \
  oci://ghcr.io/triggerdotdev/charts/trigger \
  --version "~4.0.0" \
  --create-namespace
```

2. Access the webapp:

```bash theme={"theme":"css-variables"}
kubectl port-forward svc/trigger-webapp 3040:3030 -n trigger
```

3. Open the dashboard: `http://localhost:3040`

4. Login with the magic link:

```bash theme={"theme":"css-variables"}
# Check the webapp logs
kubectl logs -n trigger deployment/trigger-webapp | grep -A1 "magic link"
```

## Configuration

Most values map directly to the environment variables documented in the [webapp](/self-hosting/env/webapp) and [supervisor](/self-hosting/env/supervisor) environment variable overview.

**Naming convention:**

* Environment variables use `UPPER_SNAKE_CASE`
* Helm values use `camelCase`

**Example mapping:**

```bash theme={"theme":"css-variables"}
# Environment variable
APP_ORIGIN=https://trigger.example.com

# Becomes Helm value
config:
  appOrigin: "https://trigger.example.com"
```

### Default values

The following commands will display the default values:

```bash theme={"theme":"css-variables"}
# Specific version
helm show values oci://ghcr.io/triggerdotdev/charts/trigger \
  --version "4.0.5"

# Latest v4
helm show values oci://ghcr.io/triggerdotdev/charts/trigger \
  --version "~4.0.0"
```

### Custom values

The default values are insecure and are only suitable for testing. You will need to configure your own secrets as a bare minimum.

Create a `values-custom.yaml` file to override the defaults. For example:

```yaml theme={"theme":"css-variables"}
# Generate new secrets with `openssl rand -hex 16`
# WARNING: You should probably use an existingSecret instead
secrets:
  enabled: true
  sessionSecret: "your-32-char-hex-secret-1"
  magicLinkSecret: "your-32-char-hex-secret-2"
  # ...

# Recommended: existingSecret, must contain at least the following keys:
# - SESSION_SECRET
# - MAGIC_LINK_SECRET
# - ENCRYPTION_KEY
# - MANAGED_WORKER_SECRET
# - OBJECT_STORE_ACCESS_KEY_ID
# - OBJECT_STORE_SECRET_ACCESS_KEY
secrets:
  enabled: false
  existingSecret: "your-existing-secret"

# Application URLs
config:
  appOrigin: "https://trigger.example.com"
  loginOrigin: "https://trigger.example.com"
  apiOrigin: "https://trigger.example.com"

# Resource limits
webapp:
  resources:
    requests:
      cpu: 1000m
      memory: 2Gi
    limits:
      cpu: 2000m
      memory: 4Gi

supervisor:
  resources:
    requests:
      cpu: 200m
      memory: 512Mi
    limits:
      cpu: 1000m
      memory: 2Gi
```

Deploy with your custom values:

```bash theme={"theme":"css-variables"}
helm upgrade -n trigger --install trigger \
  oci://ghcr.io/triggerdotdev/charts/trigger \
  --version "~4.0.0" \
  --create-namespace \
  -f values-custom.yaml
```

### Extra env

You can set extra environment variables on all services. For example:

```yaml theme={"theme":"css-variables"}
webapp:
  extraEnvVars:
    - name: EXTRA_ENV_VAR
      value: "extra-value"
```

### Extra annotations

You can set extra annotations on all services. For example:

```yaml theme={"theme":"css-variables"}
webapp:
  podAnnotations:
    "my-annotation": "my-value"
```

### External services

You can disable the built-in services and use external services instead. The chart supports both direct configuration and existing Kubernetes secrets for secure credential management.

#### PostgreSQL

**Direct configuration:**

```yaml theme={"theme":"css-variables"}
postgres:
  deploy: false
  external:
    databaseUrl: "postgresql://user:password@host:5432/database?schema=public"
    directUrl: "" # Optional, defaults to databaseUrl
```

**Using existing secrets (recommended):**

```yaml theme={"theme":"css-variables"}
postgres:
  deploy: false
  external:
    existingSecret: "postgres-credentials"
    # Optional: Use secretKeys to specify the key names in the secret
    # secretKeys:
    #   databaseUrlKey: "postgres-database-url" # default
    #   directUrlKey: "postgres-direct-url"     # default
```

#### Redis

**Direct configuration:**

```yaml theme={"theme":"css-variables"}
redis:
  deploy: false
  external:
    host: "my-redis.example.com"
    port: 6379
    password: "my-password"
    tls:
      enabled: true
```

**Using existing secrets (recommended):**

```yaml theme={"theme":"css-variables"}
redis:
  deploy: false
  external:
    host: "my-redis.example.com"
    port: 6379
    existingSecret: "redis-credentials"
    # existingSecretPasswordKey: "redis-password" # default (optional)
    tls:
      enabled: true
```

#### ClickHouse

**Direct configuration:**

```yaml theme={"theme":"css-variables"}
clickhouse:
  deploy: false
  external:
    host: "my-clickhouse.example.com"
    port: 8123
    username: "my-username"
    password: "my-password"
```

**Using existing secrets (recommended):**

```yaml theme={"theme":"css-variables"}
clickhouse:
  deploy: false
  external:
    host: "my-clickhouse.example.com"
    port: 8123
    username: "my-username"
    existingSecret: "clickhouse-credentials"
    # existingSecretKey: "clickhouse-password" # default (optional)
```

#### S3 Object Storage

**Direct configuration:**

```yaml theme={"theme":"css-variables"}
minio:
  deploy: false
s3:
  external:
    endpoint: "https://s3.amazonaws.com"
    accessKeyId: "my-access-key"
    secretAccessKey: "my-secret-key"
```

**Using existing secrets (recommended):**

```yaml theme={"theme":"css-variables"}
minio:
  deploy: false
s3:
  external:
    endpoint: "https://s3.amazonaws.com"
    existingSecret: "s3-credentials"
    # Optional: Use secretKeys to specify the key names in the secret
    # secretKeys:
    #   accessKeyIdKey: "access-key-id"     # default
    #   secretAccessKeyKey: "secret-access-key" # default
```

### PostgreSQL SSL with custom CA certificates

When connecting to PostgreSQL instances that require custom CA certificates (such as AWS RDS with SSL verification), you can mount the CA certificate as a volume and configure the webapp to use it:

```yaml theme={"theme":"css-variables"}
postgres:
  deploy: false
  external:
    databaseUrl: "postgresql://user:password@mydb.example.com:5432/triggerdb?schema=public&sslmode=require"
    # Alternatively, use an existing secret
    existingSecret: "postgres-credentials"
    # secretKeys:
    #   databaseUrlKey: "postgres-database-url" # default
  connection:
    sslMode: "require"

# Webapp configuration with SSL CA certificate
webapp:
  extraEnvVars:
    - name: NODE_EXTRA_CA_CERTS
      value: "/etc/ssl/certs/postgres-ca.crt"

  extraVolumes:
    - name: postgres-ca-cert
      secret:
        secretName: postgres-ca-secret
        items:
          - key: ca.crt
            path: postgres-ca.crt

  extraVolumeMounts:
    - name: postgres-ca-cert
      mountPath: /etc/ssl/certs
      readOnly: true
```

**Benefits:**

* No plaintext credentials in `values.yaml` or Helm releases
* Complete `DATABASE_URL` stored securely in Kubernetes secrets
* Compatible with secret management tools (External Secrets Operator, etc.)
* Follows Kubernetes security best practices

## Worker token

When using the default bootstrap configuration, worker creation and authentication is handled automatically. The webapp generates a worker token and makes it available to the supervisor via a shared volume.

### Bootstrap (default)

```yaml theme={"theme":"css-variables"}
webapp:
  bootstrap:
    enabled: true
    workerGroupName: "bootstrap"
```

### Manual

If you need to set up workers separately or use a custom token:

1. Get the worker token from the webapp logs:

```bash theme={"theme":"css-variables"}
kubectl logs deployment/trigger-webapp -n trigger | grep -A15 "Worker Token"
```

2. Create a secret with the token:

```bash theme={"theme":"css-variables"}
kubectl create secret generic worker-token \
  --from-literal=token=tr_wgt_your_token_here \
  -n trigger
```

3. Configure the supervisor to use the secret:

```yaml theme={"theme":"css-variables"}
supervisor:
  bootstrap:
    enabled: false
    workerToken:
      secret:
        name: "worker-token"
        key: "token"
```

## Registry setup

See the [Docker registry setup](/self-hosting/docker#registry-setup) for conceptual information. The configuration is specified in your `values.yaml`:

```yaml theme={"theme":"css-variables"}
# Use external registry (recommended)
registry:
  deploy: false
  # Part of deployment image ref, for example: your-registry.example.com/your-company/proj_123:20250625.1.prod
  repositoryNamespace: "your-company"
  external:
    host: "your-registry.example.com"
    port: 5000
    auth:
      enabled: true
      username: "your-username"
      password: "your-password"
```

<Note>
  The internal registry (`registry.external: false`) is experimental and requires proper TLS setup
  and additional cluster configuration. Use an external registry for production.
</Note>

## Object storage

See the [Docker object storage setup](/self-hosting/docker#object-storage) for conceptual information. The defaults will use built-in MinIO, but you can use an external S3-compatible storage. The configuration is specified in your `values.yaml`:

```yaml theme={"theme":"css-variables"}
# Use external S3-compatible storage
minio:
  deploy: false
  external:
    url: "https://s3.amazonaws.com"
    # or: "https://your-minio.com:9000"

# Configure credentials
secrets:
  objectStore:
    accessKeyId: "admin"
    secretAccessKey: "very-safe-password"
```

## Authentication

Authentication options are identical to the [Docker-based installation](/self-hosting/docker#authentication). The configuration is specified in your `values.yaml`:

**GitHub OAuth:**

```yaml theme={"theme":"css-variables"}
webapp:
  extraEnvVars:
    - name: AUTH_GITHUB_CLIENT_ID
      value: "your-github-client-id"
    - name: AUTH_GITHUB_CLIENT_SECRET
      value: "your-github-client-secret"
```

**Email authentication (Resend):**

```yaml theme={"theme":"css-variables"}
webapp:
  extraEnvVars:
    - name: EMAIL_TRANSPORT
      value: "resend"
    - name: FROM_EMAIL
      value: "noreply@yourdomain.com"
    - name: REPLY_TO_EMAIL
      value: "support@yourdomain.com"
    - name: RESEND_API_KEY
      value: "your-resend-api-key"
```

**Restricting access:**

```yaml theme={"theme":"css-variables"}
webapp:
  extraEnvVars:
    - name: WHITELISTED_EMAILS
      value: "^(user1@company\\.com|user2@company\\.com)$"
```

## Version locking

You can lock versions in two ways:

**Helm chart version (recommended):**

```bash theme={"theme":"css-variables"}
# Pin to a specific version for production
helm upgrade -n trigger --install trigger \
  oci://ghcr.io/triggerdotdev/charts/trigger \
  --version "4.0.5"

# The app version will be different from the chart version
# This is the version of the Trigger.dev webapp and supervisor
# ..and should always match your Trigger.dev CLI version
helm show chart \
  oci://ghcr.io/triggerdotdev/charts/trigger \
  --version "4.0.5" | grep appVersion
```

**Specific image tags:**

```yaml theme={"theme":"css-variables"}
webapp:
  image:
    tag: "v4.0.0"

supervisor:
  image:
    tag: "v4.0.0"
```

The chart version's `appVersion` field determines the default image tags. Newer image tags may be incompatible with older chart versions and vice versa.

## Troubleshooting

**Check logs:**

```bash theme={"theme":"css-variables"}
# Webapp logs
kubectl logs deployment/trigger-webapp -n trigger -f

# Supervisor logs
kubectl logs deployment/trigger-supervisor -n trigger -f

# All pods
kubectl logs -l app.kubernetes.io/instance=trigger -n trigger -f
```

**Check pod status:**

```bash theme={"theme":"css-variables"}
kubectl get pods -n trigger
kubectl describe pod <pod-name> -n trigger
```

**Start from scratch:**

```bash theme={"theme":"css-variables"}
# Delete the release
helm uninstall trigger -n trigger

# Delete persistent volumes (optional)
# WARNING: This will delete all your data!
kubectl delete pvc -l app.kubernetes.io/instance=trigger -n trigger

# Delete the namespace (optional)
kubectl delete namespace trigger
```

**Common issues:**

* **Magic links not working**: Check webapp logs for email delivery errors
* **Deploy fails**: Verify registry access and authentication
* **Pods stuck pending**: Describe the pod and check the events
* **Worker token issues**: Check webapp and supervisor logs for errors
* **Deploy fails with `ERROR: schema "graphile_worker" does not exist`**: See the [Docker troubleshooting](/self-hosting/docker#troubleshooting) section for details on resolving PostgreSQL SSL certificate issues that prevent Graphile Worker migrations.

See the [Docker troubleshooting](/self-hosting/docker#troubleshooting) section for more information.

## CLI usage

See the [Docker CLI usage](/self-hosting/docker#cli-usage) section, the commands are identical regardless of deployment method.

## CI / GitHub Actions

When running the CLI in a CI environment, your login profiles won't be available. Instead, you can use the `TRIGGER_API_URL` and `TRIGGER_ACCESS_TOKEN` environment
variables to point at your self-hosted instance and authenticate.

For more detailed instructions, see the [GitHub Actions guide](/github-actions).

## Telemetry

By default, the Trigger.dev webapp sends telemetry data to our servers. This data is used to improve the product and is not shared with third parties. To disable telemetry, set in your `values.yaml`:

```yaml theme={"theme":"css-variables"}
telemetry:
  enabled: false
```

---

## Supervisor

Environment variables for the supervisor container.

| Name                                        | Required | Default     | Description                                                 |
| :------------------------------------------ | :------- | :---------- | :---------------------------------------------------------- |
| **Required settings**                       |          |             |                                                             |
| `TRIGGER_API_URL`                           | Yes      | —           | Trigger.dev API URL. Should point at the webapp.            |
| `TRIGGER_WORKER_TOKEN`                      | Yes      | —           | Worker token (can be a file path with file://).             |
| `MANAGED_WORKER_SECRET`                     | Yes      | —           | Managed worker secret. Needs to match webapp value.         |
| `OTEL_EXPORTER_OTLP_ENDPOINT`               | Yes      | —           | OTel exporter endpoint. Point at: `<webapp-url>/otel`       |
| **Worker instance**                         |          |             |                                                             |
| `TRIGGER_WORKER_INSTANCE_NAME`              | No       | random UUID | Worker instance name. Set to `spec.nodeName` on k8s.        |
| `TRIGGER_WORKER_HEARTBEAT_INTERVAL_SECONDS` | No       | 30          | Worker heartbeat interval (seconds).                        |
| **Workload API settings**                   |          |             |                                                             |
| `TRIGGER_WORKLOAD_API_ENABLED`              | No       | true        | Enable workload API. Runs use this to perform actions.      |
| `TRIGGER_WORKLOAD_API_PROTOCOL`             | No       | http        | Workload API protocol (http/https).                         |
| `TRIGGER_WORKLOAD_API_DOMAIN`               | No       | —           | Workload API domain. Keep empty for auto-detection.         |
| `TRIGGER_WORKLOAD_API_HOST_INTERNAL`        | No       | 0.0.0.0     | Workload API internal host.                                 |
| `TRIGGER_WORKLOAD_API_PORT_INTERNAL`        | No       | 8020        | Workload API internal port.                                 |
| `TRIGGER_WORKLOAD_API_PORT_EXTERNAL`        | No       | 8020        | Workload API external port.                                 |
| **Runner settings**                         |          |             |                                                             |
| `RUNNER_HEARTBEAT_INTERVAL_SECONDS`         | No       | —           | Runner heartbeat interval (seconds).                        |
| `RUNNER_SNAPSHOT_POLL_INTERVAL_SECONDS`     | No       | —           | Runner snapshot poll interval (seconds).                    |
| `RUNNER_ADDITIONAL_ENV_VARS`                | No       | —           | Additional runner env vars (CSV).                           |
| `RUNNER_PRETTY_LOGS`                        | No       | false       | Pretty logs for runner.                                     |
| **Dequeue settings**                        |          |             |                                                             |
| `TRIGGER_DEQUEUE_ENABLED`                   | No       | true        | Enable dequeue to pull runs from the queue.                 |
| `TRIGGER_DEQUEUE_INTERVAL_MS`               | No       | 250         | Dequeue interval (ms).                                      |
| `TRIGGER_DEQUEUE_IDLE_INTERVAL_MS`          | No       | 1000 (1s)   | Dequeue idle interval (ms).                                 |
| `TRIGGER_DEQUEUE_MAX_RUN_COUNT`             | No       | 10          | Max dequeue run count.                                      |
| `TRIGGER_DEQUEUE_MAX_CONSUMER_COUNT`        | No       | 1           | Max dequeue consumer count.                                 |
| **Docker settings**                         |          |             |                                                             |
| `DOCKER_API_VERSION`                        | No       | v1.41       | Docker API version. You should probably not touch this.     |
| `DOCKER_STRIP_IMAGE_DIGEST`                 | No       | true        | Strip image digest in Docker. Turning off can cause issues. |
| `DOCKER_ENFORCE_MACHINE_PRESETS`            | No       | true        | Enforce Docker machine cpu and memory limits.               |
| `DOCKER_AUTOREMOVE_EXITED_CONTAINERS`       | No       | true        | Auto-remove exited containers.                              |
| `DOCKER_RUNNER_NETWORKS`                    | No       | host        | Docker runner networks (CSV).                               |
| **Registry auth**                           |          |             |                                                             |
| `DOCKER_REGISTRY_URL`                       | No       | —           | Docker registry URL, e.g. `docker.io`.                      |
| `DOCKER_REGISTRY_USERNAME`                  | No       | —           | Docker registry username.                                   |
| `DOCKER_REGISTRY_PASSWORD`                  | No       | —           | Docker registry password.                                   |
| **Kubernetes settings**                     |          |             |                                                             |
| `KUBERNETES_FORCE_ENABLED`                  | No       | false       | Force Kubernetes mode.                                      |
| `KUBERNETES_NAMESPACE`                      | No       | default     | The namespace that runs should be in.                       |
| `KUBERNETES_WORKER_NODETYPE_LABEL`          | No       | v4-worker   | Nodes for runs need this label, e.g. `nodetype=v4-worker`.  |
| `KUBERNETES_IMAGE_PULL_SECRETS`             | No       | —           | Image pull secrets (CSV).                                   |
| `KUBERNETES_EPHEMERAL_STORAGE_SIZE_LIMIT`   | No       | 10Gi        | Ephemeral storage size limit. Applies to all runs.          |
| `KUBERNETES_EPHEMERAL_STORAGE_SIZE_REQUEST` | No       | 2Gi         | Ephemeral storage size request. Applies to all runs.        |
| **Metrics**                                 |          |             |                                                             |
| `METRICS_ENABLED`                           | No       | true        | Enable metrics.                                             |
| `METRICS_COLLECT_DEFAULTS`                  | No       | true        | Collect default metrics.                                    |
| `METRICS_HOST`                              | No       | 127.0.0.1   | Metrics host.                                               |
| `METRICS_PORT`                              | No       | 9090        | Metrics port.                                               |
| **Pod cleaner**                             |          |             |                                                             |
| `POD_CLEANER_ENABLED`                       | No       | true        | Enable pod cleaner.                                         |
| `POD_CLEANER_INTERVAL_MS`                   | No       | 10000 (10s) | Pod cleaner interval (ms). Best not to touch this.          |
| `POD_CLEANER_BATCH_SIZE`                    | No       | 500         | Pod cleaner batch size.                                     |
| **Failed pod handler**                      |          |             |                                                             |
| `FAILED_POD_HANDLER_ENABLED`                | No       | true        | Enable failed pod handler.                                  |
| `FAILED_POD_HANDLER_RECONNECT_INTERVAL_MS`  | No       | 1000 (1s)   | Failed pod handler reconnect interval (ms).                 |
| **Debug**                                   |          |             |                                                             |
| `DEBUG`                                     | No       | false       | Enable debug logs.                                          |
| `SEND_RUN_DEBUG_LOGS`                       | No       | false       | Send run debug logs to the platform.                        |
| **Not used for self-hosting**               |          |             |                                                             |
| `TRIGGER_WARM_START_URL`                    | No       | —           | Warm start URL.                                             |
| `TRIGGER_CHECKPOINT_URL`                    | No       | —           | Checkpoint URL.                                             |
| `TRIGGER_METADATA_URL`                      | No       | —           | Metadata URL.                                               |
| `RESOURCE_MONITOR_ENABLED`                  | No       | false       | Enable resource monitor.                                    |
| `RESOURCE_MONITOR_OVERRIDE_CPU_TOTAL`       | No       | —           | Override CPU total for resource monitor.                    |
| `RESOURCE_MONITOR_OVERRIDE_MEMORY_TOTAL_GB` | No       | —           | Override memory total (GB) for resource monitor.            |

---

## Webapp

Environment variables for the webapp container.

| Name                                             | Required | Default                                        | Description                                                                                                        |
| :----------------------------------------------- | :------- | :--------------------------------------------- | :----------------------------------------------------------------------------------------------------------------- |
| **Secrets**                                      |          |                                                |                                                                                                                    |
| `SESSION_SECRET`                                 | Yes      | —                                              | Session encryption secret. Run: `openssl rand -hex 16`                                                             |
| `MAGIC_LINK_SECRET`                              | Yes      | —                                              | Magic link encryption secret. Run: `openssl rand -hex 16`                                                          |
| `ENCRYPTION_KEY`                                 | Yes      | —                                              | Secret store encryption key. Run: `openssl rand -hex 16`                                                           |
| `MANAGED_WORKER_SECRET`                          | No       | managed-secret                                 | Managed worker secret. Should be changed and match supervisor.                                                     |
| **Domains & ports**                              |          |                                                |                                                                                                                    |
| `REMIX_APP_PORT`                                 | No       | 3030                                           | Remix app port.                                                                                                    |
| `APP_ORIGIN`                                     | Yes      | [http://localhost:3030](http://localhost:3030) | App origin URL.                                                                                                    |
| `LOGIN_ORIGIN`                                   | Yes      | [http://localhost:3030](http://localhost:3030) | Login origin URL. Most likely the same as `APP_ORIGIN`.                                                            |
| `API_ORIGIN`                                     | No       | `APP_ORIGIN`                                   | API origin URL.                                                                                                    |
| `STREAM_ORIGIN`                                  | No       | `APP_ORIGIN`                                   | Realtime stream origin URL.                                                                                        |
| `ELECTRIC_ORIGIN`                                | No       | [http://localhost:3060](http://localhost:3060) | Electric origin URL.                                                                                               |
| **Postgres**                                     |          |                                                |                                                                                                                    |
| `DATABASE_URL`                                   | Yes      | —                                              | PostgreSQL connection string.                                                                                      |
| `DIRECT_URL`                                     | Yes      | —                                              | Direct DB connection string used for migrations etc.                                                               |
| `DATABASE_CONNECTION_LIMIT`                      | No       | 10                                             | Max DB connections.                                                                                                |
| `DATABASE_POOL_TIMEOUT`                          | No       | 60                                             | DB pool timeout (s).                                                                                               |
| `DATABASE_CONNECTION_TIMEOUT`                    | No       | 20                                             | DB connect timeout (s).                                                                                            |
| `DATABASE_READ_REPLICA_URL`                      | No       | `DATABASE_URL`                                 | Read-replica DB string.                                                                                            |
| **Redis**                                        |          |                                                |                                                                                                                    |
| `REDIS_HOST`                                     | Yes      | —                                              | Redis host.                                                                                                        |
| `REDIS_PORT`                                     | Yes      | —                                              | Redis port.                                                                                                        |
| `REDIS_READER_HOST`                              | No       | `REDIS_HOST`                                   | Redis reader host.                                                                                                 |
| `REDIS_READER_PORT`                              | No       | `REDIS_PORT`                                   | Redis reader port.                                                                                                 |
| `REDIS_USERNAME`                                 | No       | —                                              | Redis username.                                                                                                    |
| `REDIS_PASSWORD`                                 | No       | —                                              | Redis password.                                                                                                    |
| `REDIS_TLS_DISABLED`                             | No       | —                                              | Disable Redis TLS.                                                                                                 |
| **Auth**                                         |          |                                                |                                                                                                                    |
| `WHITELISTED_EMAILS`                             | No       | —                                              | Whitelisted emails regex.                                                                                          |
| `AUTH_GITHUB_CLIENT_ID`                          | No       | —                                              | GitHub client ID.                                                                                                  |
| `AUTH_GITHUB_CLIENT_SECRET`                      | No       | —                                              | GitHub client secret.                                                                                              |
| **Email**                                        |          |                                                |                                                                                                                    |
| `EMAIL_TRANSPORT`                                | No       | —                                              | Email transport type. One of `resend`, `smtp`, `aws-ses`.                                                          |
| `FROM_EMAIL`                                     | No       | —                                              | From email address.                                                                                                |
| `REPLY_TO_EMAIL`                                 | No       | —                                              | Reply-to email address.                                                                                            |
| `RESEND_API_KEY`                                 | No       | —                                              | Resend API key.                                                                                                    |
| `SMTP_HOST`                                      | No       | —                                              | SMTP host.                                                                                                         |
| `SMTP_PORT`                                      | No       | —                                              | SMTP port.                                                                                                         |
| `SMTP_SECURE`                                    | No       | —                                              | SMTP secure flag.                                                                                                  |
| `SMTP_USER`                                      | No       | —                                              | SMTP user.                                                                                                         |
| `SMTP_PASSWORD`                                  | No       | —                                              | SMTP password.                                                                                                     |
| `AWS_REGION`                                     | No       | —                                              | AWS region for SES.                                                                                                |
| `AWS_ACCESS_KEY_ID`                              | No       | —                                              | AWS access key ID for SES.                                                                                         |
| `AWS_SECRET_ACCESS_KEY`                          | No       | —                                              | AWS secret access key for SES.                                                                                     |
| **Graphile & Redis worker**                      |          |                                                |                                                                                                                    |
| `WORKER_CONCURRENCY`                             | No       | 10                                             | Redis worker concurrency.                                                                                          |
| `WORKER_POLL_INTERVAL`                           | No       | 1000                                           | Redis worker poll interval (ms).                                                                                   |
| `WORKER_SCHEMA`                                  | No       | graphile\_worker                               | Graphile worker schema.                                                                                            |
| `GRACEFUL_SHUTDOWN_TIMEOUT`                      | No       | 60000 (1m)                                     | Graphile graceful shutdown timeout (ms). Affects shutdown time.                                                    |
| **Concurrency limits**                           |          |                                                |                                                                                                                    |
| `DEFAULT_ENV_EXECUTION_CONCURRENCY_LIMIT`        | No       | 100                                            | Default env execution concurrency.                                                                                 |
| `DEFAULT_ORG_EXECUTION_CONCURRENCY_LIMIT`        | No       | 300                                            | Default org execution concurrency, needs to be 3x env concurrency.                                                 |
| **Dev**                                          |          |                                                |                                                                                                                    |
| `DEV_MAX_CONCURRENT_RUNS`                        | No       | 25                                             | Sets the max concurrency for dev runs via the CLI.                                                                 |
| `DEV_OTEL_EXPORTER_OTLP_ENDPOINT`                | No       | `APP_ORIGIN/otel`                              | OTel endpoint for dev runs.                                                                                        |
| **Rate limiting**                                |          |                                                |                                                                                                                    |
| `API_RATE_LIMIT_REFILL_INTERVAL`                 | No       | 10s                                            | API rate limit refill interval.                                                                                    |
| `API_RATE_LIMIT_MAX`                             | No       | 750                                            | API rate limit max.                                                                                                |
| `API_RATE_LIMIT_REFILL_RATE`                     | No       | 250                                            | API rate limit refill rate.                                                                                        |
| `API_RATE_LIMIT_REQUEST_LOGS_ENABLED`            | No       | 0                                              | API rate limit request logs.                                                                                       |
| `API_RATE_LIMIT_REJECTION_LOGS_ENABLED`          | No       | 1                                              | API rate limit rejection logs.                                                                                     |
| `API_RATE_LIMIT_LIMITER_LOGS_ENABLED`            | No       | 0                                              | API rate limit limiter logs.                                                                                       |
| `API_RATE_LIMIT_JWT_WINDOW`                      | No       | 1m                                             | API rate limit JWT window.                                                                                         |
| `API_RATE_LIMIT_JWT_TOKENS`                      | No       | 60                                             | API rate limit JWT tokens.                                                                                         |
| **Deploy & Registry**                            |          |                                                |                                                                                                                    |
| `DEPLOY_REGISTRY_HOST`                           | Yes      | —                                              | Deploy registry host.                                                                                              |
| `DEPLOY_REGISTRY_USERNAME`                       | No       | —                                              | Deploy registry username.                                                                                          |
| `DEPLOY_REGISTRY_PASSWORD`                       | No       | —                                              | Deploy registry password.                                                                                          |
| `DEPLOY_REGISTRY_NAMESPACE`                      | No       | trigger                                        | Deploy registry namespace.                                                                                         |
| `DEPLOY_IMAGE_PLATFORM`                          | No       | linux/amd64                                    | Deploy image platform, same values as docker `--platform` flag.                                                    |
| `DEPLOY_TIMEOUT_MS`                              | No       | 480000 (8m)                                    | Deploy timeout (ms).                                                                                               |
| **Object store (S3)**                            |          |                                                |                                                                                                                    |
| `OBJECT_STORE_BASE_URL`                          | No       | —                                              | Object store base URL.                                                                                             |
| `OBJECT_STORE_ACCESS_KEY_ID`                     | No       | —                                              | Object store access key.                                                                                           |
| `OBJECT_STORE_SECRET_ACCESS_KEY`                 | No       | —                                              | Object store secret key.                                                                                           |
| `OBJECT_STORE_REGION`                            | No       | —                                              | Object store region.                                                                                               |
| `OBJECT_STORE_SERVICE`                           | No       | s3                                             | Object store service.                                                                                              |
| **Alerts**                                       |          |                                                |                                                                                                                    |
| `ORG_SLACK_INTEGRATION_CLIENT_ID`                | No       | —                                              | Slack client ID. Required for Slack alerts.                                                                        |
| `ORG_SLACK_INTEGRATION_CLIENT_SECRET`            | No       | —                                              | Slack client secret. Required for Slack alerts.                                                                    |
| `ALERT_EMAIL_TRANSPORT`                          | No       | —                                              | Alert email transport.                                                                                             |
| `ALERT_FROM_EMAIL`                               | No       | —                                              | Alert from email.                                                                                                  |
| `ALERT_REPLY_TO_EMAIL`                           | No       | —                                              | Alert reply-to email.                                                                                              |
| `ALERT_RESEND_API_KEY`                           | No       | —                                              | Alert Resend API key.                                                                                              |
| `ALERT_SMTP_HOST`                                | No       | —                                              | Alert SMTP host.                                                                                                   |
| `ALERT_SMTP_PORT`                                | No       | —                                              | Alert SMTP port.                                                                                                   |
| `ALERT_SMTP_SECURE`                              | No       | —                                              | Alert SMTP secure.                                                                                                 |
| `ALERT_SMTP_USER`                                | No       | —                                              | Alert SMTP user.                                                                                                   |
| `ALERT_SMTP_PASSWORD`                            | No       | —                                              | Alert SMTP password.                                                                                               |
| **Limits**                                       |          |                                                |                                                                                                                    |
| `TASK_PAYLOAD_OFFLOAD_THRESHOLD`                 | No       | 524288 (512KB)                                 | Max task payload size before offloading to S3.                                                                     |
| `TASK_PAYLOAD_MAXIMUM_SIZE`                      | No       | 3145728 (3MB)                                  | Max task payload size.                                                                                             |
| `BATCH_TASK_PAYLOAD_MAXIMUM_SIZE`                | No       | 1000000 (1MB)                                  | Max batch payload size.                                                                                            |
| `TASK_RUN_METADATA_MAXIMUM_SIZE`                 | No       | 262144 (256KB)                                 | Max metadata size.                                                                                                 |
| `MAX_BATCH_V2_TRIGGER_ITEMS`                     | No       | 500                                            | Max batch size (legacy v2 API).                                                                                    |
| `STREAMING_BATCH_MAX_ITEMS`                      | No       | 1000                                           | Max items in streaming batch (v3 API, requires SDK 4.3.1+).                                                        |
| `STREAMING_BATCH_ITEM_MAXIMUM_SIZE`              | No       | 3145728 (3MB)                                  | Max size per item in streaming batch.                                                                              |
| `MAXIMUM_DEV_QUEUE_SIZE`                         | No       | —                                              | Max dev queue size.                                                                                                |
| `MAXIMUM_DEPLOYED_QUEUE_SIZE`                    | No       | —                                              | Max deployed queue size.                                                                                           |
| **OTel limits**                                  |          |                                                |                                                                                                                    |
| `TRIGGER_OTEL_SPAN_ATTRIBUTE_COUNT_LIMIT`        | No       | 1024                                           | OTel span attribute count limit.                                                                                   |
| `TRIGGER_OTEL_LOG_ATTRIBUTE_COUNT_LIMIT`         | No       | 1024                                           | OTel log attribute count limit.                                                                                    |
| `TRIGGER_OTEL_SPAN_ATTRIBUTE_VALUE_LENGTH_LIMIT` | No       | 131072                                         | OTel span attribute value length limit.                                                                            |
| `TRIGGER_OTEL_LOG_ATTRIBUTE_VALUE_LENGTH_LIMIT`  | No       | 131072                                         | OTel log attribute value length limit.                                                                             |
| `TRIGGER_OTEL_SPAN_EVENT_COUNT_LIMIT`            | No       | 10                                             | OTel span event count limit.                                                                                       |
| `TRIGGER_OTEL_LINK_COUNT_LIMIT`                  | No       | 2                                              | OTel link count limit.                                                                                             |
| `TRIGGER_OTEL_ATTRIBUTE_PER_LINK_COUNT_LIMIT`    | No       | 10                                             | OTel attribute per link count limit.                                                                               |
| `TRIGGER_OTEL_ATTRIBUTE_PER_EVENT_COUNT_LIMIT`   | No       | 10                                             | OTel attribute per event count limit.                                                                              |
| `SERVER_OTEL_SPAN_ATTRIBUTE_VALUE_LENGTH_LIMIT`  | No       | 8192                                           | OTel span attribute value length limit.                                                                            |
| **Realtime**                                     |          |                                                |                                                                                                                    |
| `REALTIME_STREAM_MAX_LENGTH`                     | No       | 1000                                           | Realtime stream max length.                                                                                        |
| `REALTIME_STREAM_TTL`                            | No       | 86400 (1d)                                     | Realtime stream TTL (s).                                                                                           |
| **Bootstrap**                                    |          |                                                |                                                                                                                    |
| `TRIGGER_BOOTSTRAP_ENABLED`                      | No       | 0                                              | Trigger bootstrap enabled.                                                                                         |
| `TRIGGER_BOOTSTRAP_WORKER_GROUP_NAME`            | No       | —                                              | Trigger bootstrap worker group name.                                                                               |
| `TRIGGER_BOOTSTRAP_WORKER_TOKEN_PATH`            | No       | —                                              | Trigger bootstrap worker token path.                                                                               |
| **Run engine**                                   |          |                                                |                                                                                                                    |
| `RUN_ENGINE_WORKER_COUNT`                        | No       | 4                                              | Run engine worker count.                                                                                           |
| `RUN_ENGINE_TASKS_PER_WORKER`                    | No       | 10                                             | Run engine tasks per worker.                                                                                       |
| `RUN_ENGINE_WORKER_CONCURRENCY_LIMIT`            | No       | 10                                             | Run engine worker concurrency limit.                                                                               |
| `RUN_ENGINE_WORKER_POLL_INTERVAL`                | No       | 100                                            | Run engine worker poll interval (ms).                                                                              |
| `RUN_ENGINE_WORKER_IMMEDIATE_POLL_INTERVAL`      | No       | 100                                            | Run engine worker immediate poll interval (ms).                                                                    |
| `RUN_ENGINE_WORKER_SHUTDOWN_TIMEOUT_MS`          | No       | 60000 (1m)                                     | Run engine worker shutdown timeout (ms).                                                                           |
| `RUN_ENGINE_RATE_LIMIT_REFILL_INTERVAL`          | No       | 10s                                            | Run engine rate limit refill interval.                                                                             |
| `RUN_ENGINE_RATE_LIMIT_MAX`                      | No       | 1200                                           | Run engine rate limit max.                                                                                         |
| `RUN_ENGINE_RATE_LIMIT_REFILL_RATE`              | No       | 400                                            | Run engine rate limit refill rate.                                                                                 |
| `RUN_ENGINE_RATE_LIMIT_REQUEST_LOGS_ENABLED`     | No       | 0                                              | Run engine rate limit request logs.                                                                                |
| `RUN_ENGINE_RATE_LIMIT_REJECTION_LOGS_ENABLED`   | No       | 1                                              | Run engine rate limit rejection logs.                                                                              |
| `RUN_ENGINE_RATE_LIMIT_LIMITER_LOGS_ENABLED`     | No       | 0                                              | Run engine rate limit limiter logs.                                                                                |
| `RUN_ENGINE_DEFAULT_MAX_TTL`                     | No       | —                                              | Maximum TTL for all runs (e.g. "14d"). Runs without a TTL use this as default; runs with a larger TTL are clamped. |
| `MAXIMUM_DEV_QUEUE_SIZE`                         | No       | —                                              | Maximum queued runs per queue in development environments.                                                         |
| `MAXIMUM_DEPLOYED_QUEUE_SIZE`                    | No       | —                                              | Maximum queued runs per queue in deployed (staging/prod) environments.                                             |
| **Misc**                                         |          |                                                |                                                                                                                    |
| `TRIGGER_TELEMETRY_DISABLED`                     | No       | —                                              | Disable telemetry.                                                                                                 |
| `NODE_MAX_OLD_SPACE_SIZE`                        | No       | 8192                                           | Maximum memory allocation for Node.js heap in MiB (e.g. "4096" for 4GB).                                           |
| `OPENAI_API_KEY`                                 | No       | —                                              | OpenAI API key.                                                                                                    |
| `MACHINE_PRESETS_OVERRIDE_PATH`                  | No       | —                                              | Path to machine presets override file. See [machine overrides](/self-hosting/overview#machine-overrides).          |
| `APP_ENV`                                        | No       | `NODE_ENV`                                     | App environment. Used for things like the title tag.                                                               |
| `ADMIN_EMAILS`                                   | No       | —                                              | Regex of user emails to automatically promote to admin on signup. Does not apply to existing users.                |
| `EVENT_LOOP_MONITOR_ENABLED`                     | No       | 1                                              | Node.js event loop lag monitor.                                                                                    |

---
