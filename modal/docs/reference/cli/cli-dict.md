# modal dict

Manage `modal.Dict` objects and inspect their contents.

## Usage

```
modal dict [OPTIONS] COMMAND [ARGS]...
```

## Options

- `--help`: Show this message and exit.

## Commands

- `create`: Create a named Dict object.
- `list`: List all named Dicts.
- `clear`: Clear the contents of a named Dict by deleting all of its data.
- `delete`: Delete a named Dict and all of its data.
- `get`: Print the value for a specific key.
- `items`: Print the contents of a Dict.

---

## modal dict create

Create a named Dict object.

Note: This is a no-op when the Dict already exists.

### Usage

```
modal dict create [OPTIONS] NAME
```

### Arguments

- `NAME`: [required]

### Options

- `-e, --env TEXT`: Environment to interact with. If not specified, Modal will use the default environment of your current profile, or the `MODAL_ENVIRONMENT` variable. Otherwise, raises an error if the workspace has multiple environments.
- `--help`: Show this message and exit.

---

## modal dict list

List all named Dicts.

### Usage

```
modal dict list [OPTIONS]
```

### Options

- `--json / --no-json`: [default: no-json]
- `-e, --env TEXT`: Environment to interact with. If not specified, Modal will use the default environment of your current profile, or the `MODAL_ENVIRONMENT` variable. Otherwise, raises an error if the workspace has multiple environments.
- `--help`: Show this message and exit.

---

## modal dict clear

Clear the contents of a named Dict by deleting all of its data.

### Usage

```
modal dict clear [OPTIONS] NAME
```

### Arguments

- `NAME`: [required]

### Options

- `-y, --yes`: Run without pausing for confirmation.
- `-e, --env TEXT`: Environment to interact with. If not specified, Modal will use the default environment of your current profile, or the `MODAL_ENVIRONMENT` variable. Otherwise, raises an error if the workspace has multiple environments.
- `--help`: Show this message and exit.

---

## modal dict delete

Delete a named Dict and all of its data.

### Usage

```
modal dict delete [OPTIONS] NAME
```

### Arguments

- `NAME`: [required]

### Options

- `--allow-missing`: Don't error if the Dict doesn't exist.
- `-y, --yes`: Run without pausing for confirmation.
- `-e, --env TEXT`: Environment to interact with. If not specified, Modal will use the default environment of your current profile, or the `MODAL_ENVIRONMENT` variable. Otherwise, raises an error if the workspace has multiple environments.
- `--help`: Show this message and exit.

---

## modal dict get

Print the value for a specific key.

Note: When using the CLI, keys are always interpreted as having a string type.

### Usage

```
modal dict get [OPTIONS] NAME KEY
```

### Arguments

- `NAME`: [required]
- `KEY`: [required]

### Options

- `-e, --env TEXT`: Environment to interact with. If not specified, Modal will use the default environment of your current profile, or the `MODAL_ENVIRONMENT` variable. Otherwise, raises an error if the workspace has multiple environments.
- `--help`: Show this message and exit.

---

## modal dict items

Print the contents of a Dict.

Note: By default, this command truncates the contents. Use the N argument to control the amount of data shown or the `--all` option to retrieve the entire Dict, which may be slow.

### Usage

```
modal dict items [OPTIONS] NAME [N]
```

### Arguments

- `NAME`: [required]
- `[N]`: Limit the number of entries shown [default: 20]

### Options

- `-a, --all`: Ignore N and print all entries in the Dict (may be slow)
- `-r, --repr`: Display items using repr() to see more details
- `--json / --no-json`: [default: no-json]
- `-e, --env TEXT`: Environment to interact with. If not specified, Modal will use the default environment of your current profile, or the `MODAL_ENVIRONMENT` variable. Otherwise, raises an error if the workspace has multiple environments.
- `--help`: Show this message and exit.
