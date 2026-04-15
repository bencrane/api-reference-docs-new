# modal serve

Run a web endpoint(s) associated with a Modal app and hot-reload code.

Modal-generated URLs will have a `-dev` suffix appended to them when running with `modal serve`. To customize this suffix (i.e., to avoid collisions with other users in your workspace who are concurrently serving the App), you can set the `dev_suffix` in your `.modal.toml` file or the `MODAL_DEV_SUFFIX` environment variable.

## Usage

```
modal serve [OPTIONS] APP_REF
```

## Arguments

- `APP_REF`: Path to a Python file with an app. [required]

## Options

- `--timeout FLOAT`
- `-e, --env TEXT`: Environment to interact with. If not specified, Modal will use the default environment of your current profile, or the `MODAL_ENVIRONMENT` variable. Otherwise, raises an error if the workspace has multiple environments.
- `-m`: Interpret argument as a Python module path instead of a file/script path.
- `--timestamps`: Show timestamps for each log line.
- `--help`: Show this message and exit.
