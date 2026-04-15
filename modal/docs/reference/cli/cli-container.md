# modal container

Manage and connect to running containers.

## Usage

```
modal container [OPTIONS] COMMAND [ARGS]...
```

## Options

- `--help`: Show this message and exit.

## Commands

- `list`: List all containers that are currently running.
- `logs`: Fetch or stream logs for a specific container.
- `exec`: Execute a command in a container.
- `stop`: Stop a currently-running container and reassign its in-progress inputs.

---

## modal container list

List all containers that are currently running.

### Usage

```
modal container list [OPTIONS]
```

### Options

- `--app-id TEXT`: List containers running for a specific App.
- `-e, --env TEXT`: Environment to interact with. If not specified, Modal will use the default environment of your current profile, or the `MODAL_ENVIRONMENT` variable. Otherwise, raises an error if the workspace has multiple environments.
- `--json / --no-json`: [default: no-json]
- `--help`: Show this message and exit.

---

## modal container logs

Fetch or stream logs for a specific container.

By default, this command fetches the last 100 log entries and exits. Use `-f` to live-stream logs from a running container instead. Fetch and follow are mutually exclusive.

### Examples

Get recent logs for a container:

```
modal container logs ta-123456
```

Follow (stream) logs from a running container:

```
modal container logs ta-123456 -f
```

Fetch logs from the last 2 hours:

```
modal container logs ta-123456 --since 2h
```

Fetch logs in a specific time range:

```
modal container logs ta-123456 --since 2026-03-01T05:00:00 --until 2026-03-01T08:00:00
```

Fetch the last 1000 entries:

```
modal container logs ta-123456 --tail 1000
```

Fetch all container logs:

```
modal container logs ta-123456 --all
```

### Usage

```
modal container logs [OPTIONS] CONTAINER_ID
```

### Arguments

- `CONTAINER_ID`: Container ID [required]

### Options

- `-f, --follow`: Stream log output until Container stops
- `--all`: Show all logs for the container
- `--since TEXT`: Start of time range. Accepts ISO 8601 datetime or relative time, e.g. '1d' (1 day ago), '2h', '30m', etc.
- `--until TEXT`: End of time range; accepts same argument types as --since
- `-n, --tail INTEGER`: Show only the last N log entries
- `--search TEXT`: Filter by search text
- `-s, --source TEXT`: Filter by source: 'stdout', 'stderr', or 'system'
- `--timestamps`: Prefix each line with its timestamp
- `--help`: Show this message and exit.

---

## modal container exec

Execute a command in a container.

### Usage

```
modal container exec [OPTIONS] CONTAINER_ID COMMAND...
```

### Arguments

- `CONTAINER_ID`: Container ID [required]
- `COMMAND...`: A command to run inside the container. To pass command-line flags or options, add `--` before the start of your commands. For example: `modal container exec <id> -- /bin/bash -c 'echo hi'` [required]

### Options

- `--pty / --no-pty`: Run the command using a PTY.
- `--help`: Show this message and exit.

---

## modal container stop

Stop a currently-running container and reassign its in-progress inputs.

This will send the container a SIGINT signal that Modal will handle.

### Usage

```
modal container stop [OPTIONS] CONTAINER_ID
```

### Arguments

- `CONTAINER_ID`: Container ID [required]

### Options

- `--help`: Show this message and exit.
