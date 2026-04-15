# modal.Secret

Source: https://modal.com/docs/reference/modal.Secret

---

```python
modal.Secret
class Secret(modal.object.Object)
```

Secrets provide a dictionary of environment variables for images.

Secrets are a secure way to add credentials and other sensitive information to the containers your functions run in. You can create and edit secrets on the dashboard, or programmatically from Python code.

See the secrets guide page for more information.

hydrate
```python
def hydrate(self, client: Optional[_Client] = None) -> Self:
```

Synchronize the local object with its identity on the Modal server.

It is rarely necessary to call this method explicitly, as most operations will lazily hydrate when needed. The main use case is when you need to access object metadata, such as its ID.

Added in v0.72.39: This method replaces the deprecated .resolve() method.

objects
```python
class objects(object)
```

Namespace with methods for managing named Secret objects.

create
@staticmethod
```python
def create(
    name: str,  # Name to use for the new Secret
    env_dict: dict[str, str],  # Key-value pairs to set in the Secret
    *,
    allow_existing: bool = False,  # If True, no-op when the Secret already exists
    environment_name: Optional[str] = None,  # Uses active environment if not specified
    client: Optional[_Client] = None,  # Optional client with Modal credentials
) -> None:
```

Create a new Secret object.

Examples:

```python
contents = {"MY_KEY": "my-value", "MY_OTHER_KEY": "my-other-value"}
modal.Secret.objects.create("my-secret", contents)
```

Secrets will be created in the active environment, or another one can be specified:

```python
modal.Secret.objects.create("my-secret", contents, environment_name="dev")
```

By default, an error will be raised if the Secret already exists, but passing allow_existing=True will make the creation attempt a no-op in this case. If the env_dict data differs from the existing Secret, it will be ignored.

```python
modal.Secret.objects.create("my-secret", contents, allow_existing=True)
```

Note that this method does not return a local instance of the Secret. You can use modal.Secret.from_name to perform a lookup after creation.

Added in v1.1.2.

list
@staticmethod
```python
def list(
    *,
    max_objects: Optional[int] = None,  # Limit requests to this size
    created_before: Optional[Union[datetime, str]] = None,  # Limit based on creation date
    environment_name: str = "",  # Uses active environment if not specified
    client: Optional[_Client] = None,  # Optional client with Modal credentials
) -> builtins.list["_Secret"]:
```

Return a list of hydrated Secret objects.

Examples:

```python
secrets = modal.Secret.objects.list()
print([s.name for s in secrets])
```

Secrets will be retreived from the active environment, or another one can be specified:

```python
dev_secrets = modal.Secret.objects.list(environment_name="dev")
```

By default, all named Secrets are returned, newest to oldest. It’s also possible to limit the number of results and to filter by creation date:

```python
secrets = modal.Secret.objects.list(max_objects=10, created_before="2025-01-01")
```

Added in v1.1.2.

delete
@staticmethod
```python
def delete(
    name: str,  # Name of the Secret to delete
    *,
    allow_missing: bool = False,  # If True, don't raise an error if the Secret doesn't exist
    environment_name: Optional[str] = None,  # Uses active environment if not specified
    client: Optional[_Client] = None,  # Optional client with Modal credentials
):
```

Delete a named Secret.

Warning: Deletion is irreversible and will affect any Apps currently using the Secret.

Examples:

await modal.Secret.objects.delete("my-secret")

Secrets will be deleted from the active environment, or another one can be specified:

await modal.Secret.objects.delete("my-secret", environment_name="dev")

Added in v1.1.2.

name
@property
```python
def name(self) -> Optional[str]:
```

from_dict
@staticmethod
```python
def from_dict(
    env_dict: dict[
        str, Optional[str]
    ] = {},  # dict of entries to be inserted as environment variables in functions using the secret
) -> "_Secret":
```

Create a secret from a str-str dictionary. Values can also be None, which is ignored.

Usage:

```python
@app.function(secrets=[modal.Secret.from_dict({"FOO": "bar"})])
def run():
    print(os.environ["FOO"])
```

from_local_environ
@staticmethod
```python
def from_local_environ(
    env_keys: list[str],  # list of local env vars to be included for remote execution
) -> "_Secret":
```

Create secrets from local environment variables automatically.

from_dotenv
@staticmethod
```python
def from_dotenv(path=None, *, filename=".env", client: Optional[_Client] = None) -> "_Secret":
```

Create secrets from a .env file automatically.

If no argument is provided, it will use the current working directory as the starting point for finding a .env file. Note that it does not use the location of the module calling Secret.from_dotenv.

If called with an argument, it will use that as a starting point for finding .env files. In particular, you can call it like this:

```python
@app.function(secrets=[modal.Secret.from_dotenv(__file__)])
def run():
    print(os.environ["USERNAME"])  # Assumes USERNAME is defined in your .env file
```

This will use the location of the script calling modal.Secret.from_dotenv as a starting point for finding the .env file.

A file named .env is expected by default, but this can be overridden with the filename keyword argument:

```python
@app.function(secrets=[modal.Secret.from_dotenv(filename=".env-dev")])
def run():
    ...
```

from_name
@staticmethod
```python
def from_name(
    name: str,
    *,
    environment_name: Optional[str] = None,
    required_keys: list[str] = [],  # Optional list of required environment variables (asserted server-side)
    client: Optional[_Client] = None,
) -> "_Secret":
```

Reference a Secret by its name.

```python
secret = modal.Secret.from_name("my-secret")

@app.function(secrets=[secret])
def run():
   ...
```

info
@live_method
```python
def info(self) -> SecretInfo:
```

Return information about the Secret object.

update
@live_method
```python
def update(self, env_dict: dict[str, str]) -> None:
```

Update this Secret, adding or overwriting key-value pairs.

Like dict.update(), this merges env_dict into the existing Secret. Keys not mentioned in env_dict are left unchanged.
