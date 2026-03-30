> Sources:
> - https://trigger.dev/docs/cli-introduction
> - https://trigger.dev/docs/cli-dev
> - https://trigger.dev/docs/cli-dev-commands
> - https://trigger.dev/docs/cli-deploy-commands
> - https://trigger.dev/docs/cli-init-commands
> - https://trigger.dev/docs/cli-login-commands
> - https://trigger.dev/docs/cli-logout-commands
> - https://trigger.dev/docs/cli-whoami-commands
> - https://trigger.dev/docs/cli-update-commands
> - https://trigger.dev/docs/cli-promote-commands
> - https://trigger.dev/docs/cli-preview-archive
> - https://trigger.dev/docs/cli-switch
> - https://trigger.dev/docs/cli-list-profiles-commands

# CLI Reference

## Introduction

The Trigger.dev CLI has a number of options and commands to help you develop locally, self host, and deploy your tasks.

## Options

<ParamField type="--help | -h">
  Shows the help information for the command.
</ParamField>

<ParamField type="--version | -v">
  Displays the version number of the CLI.
</ParamField>

## Commands

| Command                                      | Description                                                        |
| :------------------------------------------- | :----------------------------------------------------------------- |
| [login](/cli-login-commands)                 | Login with Trigger.dev so you can perform authenticated actions.   |
| [init](/cli-init-commands)                   | Initialize your existing project for development with Trigger.dev. |
| [dev](/cli-dev-commands)                     | Run your Trigger.dev tasks locally.                                |
| [deploy](/cli-deploy-commands)               | Deploy your Trigger.dev v3 project to the cloud.                   |
| [whoami](/cli-whoami-commands)               | Display the current logged in user and project details.            |
| [logout](/cli-logout-commands)               | Logout of Trigger.dev.                                             |
| [list-profiles](/cli-list-profiles-commands) | List all of your CLI profiles.                                     |
| [update](/cli-update-commands)               | Updates all `@trigger.dev/*` packages to match the CLI version.    |

---

## CLI dev command

The `trigger.dev dev` command is used to run your tasks locally.

This runs a server on your machine that can execute Trigger.dev tasks:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest dev
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest dev
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest dev
  ```
</CodeGroup>

It will first perform an update check to prevent version mismatches, failed deploys, and other errors. You will always be prompted first.

You will see in the terminal that the server is running and listening for tasks. When you run a task, you will see it in the terminal along with a link to view it in the dashboard.

It is worth noting that each task runs in a separate Node process. This means that if you have a long-running task, it will not block other tasks from running.

## Options

<ParamField type="--config | -c">
  The name of the config file found at the project path. Defaults to `trigger.config.ts`
</ParamField>

<ParamField type="--project-ref | -p">
  The project ref. Required if there is no config file.
</ParamField>

<ParamField type="--env-file">
  Load environment variables from a file. This will only hydrate the `process.env` of the CLI
  process, not the tasks.
</ParamField>

<ParamField type="--skip-update-check">
  Skip checking for `@trigger.dev` package updates.
</ParamField>

<ParamField type="--analyze">
  Analyzes the build output and displays detailed import timings. This is useful for debugging the
  start times for your runs which can be caused by importing lots of code or heavy packages.
</ParamField>

### Common options

These options are available on most commands.

<ParamField type="--profile">
  The login profile to use. Defaults to "default".
</ParamField>

<ParamField type="--api-url | -a">
  Override the default API URL. If not specified, it uses `https://api.trigger.dev`. This can also be set via the `TRIGGER_API_URL` environment variable.
</ParamField>

<ParamField type="--log-level | -l">
  The CLI log level to use. Options are `debug`, `info`, `log`, `warn`, `error`, and `none`. This does not affect the log level of your trigger.dev tasks. Defaults to `log`.
</ParamField>

<ParamField type="--skip-telemetry">
  Opt-out of sending telemetry data. This can also be done via the `TRIGGER_TELEMETRY_DISABLED` environment variable. Just set it to anything other than an empty string.
</ParamField>

<ParamField type="--help | -h">
  Shows the help information for the command.
</ParamField>

<ParamField type="--version | -v">
  Displays the version number of the CLI.
</ParamField>

## Concurrently running the terminal

Install the concurrently package as a dev dependency:

```ts theme={"theme":"css-variables"}
concurrently --raw --kill-others npm:dev:remix npm:dev:trigger
```

Then add something like this in your package.json scripts:

```json theme={"theme":"css-variables"}
"scripts": {
  "dev": "concurrently --raw --kill-others npm:dev:*",
  "dev:trigger": "npx trigger.dev@latest dev",
  // Add your framework-specific dev script here, for example:
  // "dev:next": "next dev",
  // "dev:remix": "remix dev",
  //...
}
```

---

## CLI dev command

The `trigger.dev dev` command is used to run your tasks locally.

This runs a server on your machine that can execute Trigger.dev tasks:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest dev
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest dev
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest dev
  ```
</CodeGroup>

It will first perform an update check to prevent version mismatches, failed deploys, and other errors. You will always be prompted first.

You will see in the terminal that the server is running and listening for tasks. When you run a task, you will see it in the terminal along with a link to view it in the dashboard.

It is worth noting that each task runs in a separate Node process. This means that if you have a long-running task, it will not block other tasks from running.

## Options

<ParamField type="--config | -c">
  The name of the config file found at the project path. Defaults to `trigger.config.ts`
</ParamField>

<ParamField type="--project-ref | -p">
  The project ref. Required if there is no config file.
</ParamField>

<ParamField type="--env-file">
  Load environment variables from a file. This will only hydrate the `process.env` of the CLI
  process, not the tasks.
</ParamField>

<ParamField type="--skip-update-check">
  Skip checking for `@trigger.dev` package updates.
</ParamField>

<ParamField type="--analyze">
  Analyzes the build output and displays detailed import timings. This is useful for debugging the
  start times for your runs which can be caused by importing lots of code or heavy packages.
</ParamField>

### Common options

These options are available on most commands.

<ParamField type="--profile">
  The login profile to use. Defaults to "default".
</ParamField>

<ParamField type="--api-url | -a">
  Override the default API URL. If not specified, it uses `https://api.trigger.dev`. This can also be set via the `TRIGGER_API_URL` environment variable.
</ParamField>

<ParamField type="--log-level | -l">
  The CLI log level to use. Options are `debug`, `info`, `log`, `warn`, `error`, and `none`. This does not affect the log level of your trigger.dev tasks. Defaults to `log`.
</ParamField>

<ParamField type="--skip-telemetry">
  Opt-out of sending telemetry data. This can also be done via the `TRIGGER_TELEMETRY_DISABLED` environment variable. Just set it to anything other than an empty string.
</ParamField>

<ParamField type="--help | -h">
  Shows the help information for the command.
</ParamField>

<ParamField type="--version | -v">
  Displays the version number of the CLI.
</ParamField>

## Concurrently running the terminal

Install the concurrently package as a dev dependency:

```ts theme={"theme":"css-variables"}
concurrently --raw --kill-others npm:dev:remix npm:dev:trigger
```

Then add something like this in your package.json scripts:

```json theme={"theme":"css-variables"}
"scripts": {
  "dev": "concurrently --raw --kill-others npm:dev:*",
  "dev:trigger": "npx trigger.dev@latest dev",
  // Add your framework-specific dev script here, for example:
  // "dev:next": "next dev",
  // "dev:remix": "remix dev",
  //...
}
```

---

## CLI deploy command

Use the deploy command to deploy your tasks to Trigger.dev.

Run the command like this:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest deploy
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest deploy
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest deploy
  ```
</CodeGroup>

<Warning>
  This will fail in CI if any version mismatches are detected. Ensure everything runs locally first
  using the [dev](/cli-dev-commands) command and don't bypass the version checks!
</Warning>

It performs a few steps to deploy:

1. Optionally updates packages when running locally.
2. Compiles and bundles the code.
3. Deploys the code to the Trigger.dev instance.
4. Registers the tasks as a new version in the environment (prod by default).

## Deploying from CI

When deploying from CI/CD environments such as GitHub Actions, GitLab CI, or Jenkins, you need to authenticate non-interactively by setting the `TRIGGER_ACCESS_TOKEN` environment variable. Please see the [CI / GitHub Actions guide](/github-actions) for more information.

## Arguments

```
npx trigger.dev@latest deploy [path]
```

<ParamField type="[path]">
  The path to the project. Defaults to the current directory.
</ParamField>

## Options

<ParamField type="--config | -c">
  The name of the config file found at the project path. Defaults to `trigger.config.ts`
</ParamField>

<ParamField type="--project-ref | -p">
  The project ref. Required if there is no config file.
</ParamField>

<ParamField type="--env-file">
  Load environment variables from a file. This will only hydrate the `process.env` of the CLI
  process, not the tasks.
</ParamField>

<ParamField type="--skip-update-check">
  Skip checking for `@trigger.dev` package updates.
</ParamField>

<ParamField type="--env | -e">
  Defaults to `prod` but you can specify `staging` or `preview`. If you specify `preview` we will
  try and automatically detect the branch name from git.
</ParamField>

<ParamField type="--branch | -b">
  When using `--env preview` the branch is automatically detected from git. But you can manually
  specify it by using this option, e.g. `--branch my-branch` or `-b my-branch`.
</ParamField>

<ParamField type="--dry-run">
  Create a deployable build but don't deploy it. Prints out the build path so you can inspect it.
</ParamField>

<ParamField type="--skip-promotion">
  Skips automatically promoting the newly deployed version to the "current" deploy.
</ParamField>

<ParamField type="--skip-sync-env-vars">
  Turn off syncing environment variables with the Trigger.dev instance.
</ParamField>

<ParamField type="--local-build">
  Force building the deployment image locally using your local Docker. This is automatic when self-hosting.
</ParamField>

### Common options

These options are available on most commands.

<ParamField type="--profile">
  The login profile to use. Defaults to "default".
</ParamField>

<ParamField type="--api-url | -a">
  Override the default API URL. If not specified, it uses `https://api.trigger.dev`. This can also be set via the `TRIGGER_API_URL` environment variable.
</ParamField>

<ParamField type="--log-level | -l">
  The CLI log level to use. Options are `debug`, `info`, `log`, `warn`, `error`, and `none`. This does not affect the log level of your trigger.dev tasks. Defaults to `log`.
</ParamField>

<ParamField type="--skip-telemetry">
  Opt-out of sending telemetry data. This can also be done via the `TRIGGER_TELEMETRY_DISABLED` environment variable. Just set it to anything other than an empty string.
</ParamField>

<ParamField type="--help | -h">
  Shows the help information for the command.
</ParamField>

<ParamField type="--version | -v">
  Displays the version number of the CLI.
</ParamField>

### Self-hosting

When [self-hosting](/self-hosting/overview), builds are performed locally by default. Once you've logged in to your self-hosted instance using the CLI, you can deploy with:

```bash theme={"theme":"css-variables"}
npx trigger.dev@latest deploy
```

For CI/CD environments, set `TRIGGER_ACCESS_TOKEN` and `TRIGGER_API_URL` environment variables. See the [GitHub Actions guide](/github-actions#self-hosting) for more details.

---

## CLI init command

Use these options when running the CLI `init` command.

Run the command like this:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest init
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest init
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest init
  ```
</CodeGroup>

## Options

<ParamField type="--javascript">
  By default, the init command assumes you are using TypeScript. Use this flag to initialize a
  project that uses JavaScript.
</ParamField>

<ParamField type="--project-ref | -p">
  The project ref to use when initializing the project.
</ParamField>

<ParamField type="--tag | -t">
  The version of the `@trigger.dev/sdk` package to install. Defaults to `latest`.
</ParamField>

<ParamField type="--skip-package-install">
  Skip installing the `@trigger.dev/sdk` package.
</ParamField>

<ParamField type="--override-config">
  Override the existing config file if it exists.
</ParamField>

<ParamField type="--pkg-args">
  Additional arguments to pass to the package manager. Accepts CSV for multiple args.
</ParamField>

### Common options

These options are available on most commands.

<ParamField type="--profile">
  The login profile to use. Defaults to "default".
</ParamField>

<ParamField type="--api-url | -a">
  Override the default API URL. If not specified, it uses `https://api.trigger.dev`. This can also be set via the `TRIGGER_API_URL` environment variable.
</ParamField>

<ParamField type="--log-level | -l">
  The CLI log level to use. Options are `debug`, `info`, `log`, `warn`, `error`, and `none`. This does not affect the log level of your trigger.dev tasks. Defaults to `log`.
</ParamField>

<ParamField type="--skip-telemetry">
  Opt-out of sending telemetry data. This can also be done via the `TRIGGER_TELEMETRY_DISABLED` environment variable. Just set it to anything other than an empty string.
</ParamField>

<ParamField type="--help | -h">
  Shows the help information for the command.
</ParamField>

<ParamField type="--version | -v">
  Displays the version number of the CLI.
</ParamField>

---

## CLI login command

Use these options when logging in to Trigger.dev using the CLI.

Run the command like this:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest login
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest login
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest login
  ```
</CodeGroup>

## Options

### Common options

These options are available on most commands.

<ParamField type="--profile">
  The login profile to use. Defaults to "default".
</ParamField>

<ParamField type="--api-url | -a">
  Override the default API URL. If not specified, it uses `https://api.trigger.dev`. This can also be set via the `TRIGGER_API_URL` environment variable.
</ParamField>

<ParamField type="--log-level | -l">
  The CLI log level to use. Options are `debug`, `info`, `log`, `warn`, `error`, and `none`. This does not affect the log level of your trigger.dev tasks. Defaults to `log`.
</ParamField>

<ParamField type="--skip-telemetry">
  Opt-out of sending telemetry data. This can also be done via the `TRIGGER_TELEMETRY_DISABLED` environment variable. Just set it to anything other than an empty string.
</ParamField>

<ParamField type="--help | -h">
  Shows the help information for the command.
</ParamField>

<ParamField type="--version | -v">
  Displays the version number of the CLI.
</ParamField>

---

## CLI logout command

Use these options when using the `logout` CLI command.

Run the command like this:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest logout
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest logout
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest logout
  ```
</CodeGroup>

## Options

### Common options

These options are available on most commands.

<ParamField type="--profile">
  The login profile to use. Defaults to "default".
</ParamField>

<ParamField type="--api-url | -a">
  Override the default API URL. If not specified, it uses `https://api.trigger.dev`. This can also be set via the `TRIGGER_API_URL` environment variable.
</ParamField>

<ParamField type="--log-level | -l">
  The CLI log level to use. Options are `debug`, `info`, `log`, `warn`, `error`, and `none`. This does not affect the log level of your trigger.dev tasks. Defaults to `log`.
</ParamField>

<ParamField type="--skip-telemetry">
  Opt-out of sending telemetry data. This can also be done via the `TRIGGER_TELEMETRY_DISABLED` environment variable. Just set it to anything other than an empty string.
</ParamField>

<ParamField type="--help | -h">
  Shows the help information for the command.
</ParamField>

<ParamField type="--version | -v">
  Displays the version number of the CLI.
</ParamField>

---

## CLI whoami command

Use these options to display the current logged in user and project details.

Run the command like this:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest whoami
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest whoami
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest whoami
  ```
</CodeGroup>

## Options

### Common options

These options are available on most commands.

<ParamField type="--profile">
  The login profile to use. Defaults to "default".
</ParamField>

<ParamField type="--api-url | -a">
  Override the default API URL. If not specified, it uses `https://api.trigger.dev`. This can also be set via the `TRIGGER_API_URL` environment variable.
</ParamField>

<ParamField type="--log-level | -l">
  The CLI log level to use. Options are `debug`, `info`, `log`, `warn`, `error`, and `none`. This does not affect the log level of your trigger.dev tasks. Defaults to `log`.
</ParamField>

<ParamField type="--skip-telemetry">
  Opt-out of sending telemetry data. This can also be done via the `TRIGGER_TELEMETRY_DISABLED` environment variable. Just set it to anything other than an empty string.
</ParamField>

<ParamField type="--help | -h">
  Shows the help information for the command.
</ParamField>

<ParamField type="--version | -v">
  Displays the version number of the CLI.
</ParamField>

---

## CLI update command

Use these options when using the `update` CLI command.

Run the command like this:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest update
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest update
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest update
  ```
</CodeGroup>

## Options

### Common options

These options are available on most commands.

<ParamField type="--log-level | -l">
  The CLI log level to use. Options are `debug`, `info`, `log`, `warn`, `error`, and `none`. This does not affect the log level of your trigger.dev tasks. Defaults to `log`.
</ParamField>

<ParamField type="--skip-telemetry">
  Opt-out of sending telemetry data. This can also be done via the `TRIGGER_TELEMETRY_DISABLED` environment variable. Just set it to anything other than an empty string.
</ParamField>

<ParamField type="--help | -h">
  Shows the help information for the command.
</ParamField>

<ParamField type="--version | -v">
  Displays the version number of the CLI.
</ParamField>

---

## CLI promote command

Use the promote command to promote a previously deployed version to the current version.

Run the command like this:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest promote [version]
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest promote [version]
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest promote [version]
  ```
</CodeGroup>

## Arguments

```
npx trigger.dev@latest promote [version]
```

<ParamField type="[version]">
  The version to promote. This is the version that was previously deployed.
</ParamField>

### Common options

These options are available on most commands.

<ParamField type="--profile">
  The login profile to use. Defaults to "default".
</ParamField>

<ParamField type="--api-url | -a">
  Override the default API URL. If not specified, it uses `https://api.trigger.dev`. This can also be set via the `TRIGGER_API_URL` environment variable.
</ParamField>

<ParamField type="--log-level | -l">
  The CLI log level to use. Options are `debug`, `info`, `log`, `warn`, `error`, and `none`. This does not affect the log level of your trigger.dev tasks. Defaults to `log`.
</ParamField>

<ParamField type="--skip-telemetry">
  Opt-out of sending telemetry data. This can also be done via the `TRIGGER_TELEMETRY_DISABLED` environment variable. Just set it to anything other than an empty string.
</ParamField>

<ParamField type="--help | -h">
  Shows the help information for the command.
</ParamField>

<ParamField type="--version | -v">
  Displays the version number of the CLI.
</ParamField>

---

## CLI preview archive command

The `trigger.dev preview archive` command can be used to archive a preview branch.

Run the command like this:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest preview archive
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest preview archive
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest preview archive
  ```
</CodeGroup>

It will archive the preview branch, automatically detecting the branch name from git. You can manually specify the branch using the `--branch` option.

## Arguments

```
npx trigger.dev@latest preview archive [path]
```

<ParamField type="[path]">
  The path to the project. Defaults to the current directory.
</ParamField>

## Options

<ParamField type="--branch | -b">
  When using `--env preview` the branch is automatically detected from git. But you can manually
  specify it by using this option, e.g. `--branch my-branch` or `-b my-branch`.
</ParamField>

<ParamField type="--config | -c">
  The name of the config file found at the project path. Defaults to `trigger.config.ts`
</ParamField>

<ParamField type="--project-ref | -p">
  The project ref. Required if there is no config file.
</ParamField>

<ParamField type="--env-file">
  Load environment variables from a file. This will only hydrate the `process.env` of the CLI
  process, not the tasks.
</ParamField>

<ParamField type="--skip-update-check">
  Skip checking for `@trigger.dev` package updates.
</ParamField>

### Common options

These options are available on most commands.

<ParamField type="--profile">
  The login profile to use. Defaults to "default".
</ParamField>

<ParamField type="--api-url | -a">
  Override the default API URL. If not specified, it uses `https://api.trigger.dev`. This can also be set via the `TRIGGER_API_URL` environment variable.
</ParamField>

<ParamField type="--log-level | -l">
  The CLI log level to use. Options are `debug`, `info`, `log`, `warn`, `error`, and `none`. This does not affect the log level of your trigger.dev tasks. Defaults to `log`.
</ParamField>

<ParamField type="--skip-telemetry">
  Opt-out of sending telemetry data. This can also be done via the `TRIGGER_TELEMETRY_DISABLED` environment variable. Just set it to anything other than an empty string.
</ParamField>

<ParamField type="--help | -h">
  Shows the help information for the command.
</ParamField>

<ParamField type="--version | -v">
  Displays the version number of the CLI.
</ParamField>

---

## CLI switch command

The `trigger.dev switch` command can be used to switch between profiles.

Run the command like this:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest switch [profile]
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest switch [profile]
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest switch [profile]
  ```
</CodeGroup>

It will switch to the specified profile. If no profile is specified, it will list all available profiles and run interactively.

## Arguments

```
npx trigger.dev@latest switch [profile]
```

<ParamField type="[profile]">
  The profile to switch to. If not specified, it will list all available profiles and run interactively.
</ParamField>

---

## CLI list-profiles command

Use these options when using the `list-profiles` CLI command.

Run the command like this:

<CodeGroup>
  ```bash npm theme={"theme":"css-variables"}
  npx trigger.dev@latest list-profiles
  ```

  ```bash pnpm theme={"theme":"css-variables"}
  pnpm dlx trigger.dev@latest list-profiles
  ```

  ```bash yarn theme={"theme":"css-variables"}
  yarn dlx trigger.dev@latest list-profiles
  ```
</CodeGroup>

## Options

### Common options

These options are available on most commands.

<ParamField type="--log-level | -l">
  The CLI log level to use. Options are `debug`, `info`, `log`, `warn`, `error`, and `none`. This does not affect the log level of your trigger.dev tasks. Defaults to `log`.
</ParamField>

<ParamField type="--skip-telemetry">
  Opt-out of sending telemetry data. This can also be done via the `TRIGGER_TELEMETRY_DISABLED` environment variable. Just set it to anything other than an empty string.
</ParamField>

<ParamField type="--help | -h">
  Shows the help information for the command.
</ParamField>

<ParamField type="--version | -v">
  Displays the version number of the CLI.
</ParamField>

---
