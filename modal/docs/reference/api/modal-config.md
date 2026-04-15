# modal.config

Source: https://modal.com/docs/reference/modal.config

---

```python
modal.config

```

Modal intentionally keeps configurability to a minimum.

The main configuration options are the API tokens: the token id and the token secret. These can be configured in two ways:

By running the modal token set command. This writes the tokens to .modal.toml file in your home directory.
By setting the environment variables MODAL_TOKEN_ID and MODAL_TOKEN_SECRET. This takes precedence over the previous method.
.modal.toml

The .modal.toml file is generally stored in your home directory. It should look like this::

[default]
```python
token_id = "ak-12345..."
token_secret = "as-12345..."
```

You can create this file manually, or you can run the modal token set ... command (see below).

Setting tokens using the CLI

You can set a token by running the command::

modal token set \
--token-id <token id> \
--token-secret <token secret>

This will write the token id and secret to .modal.toml.

If the token id or secret is provided as the string - (a single dash), then it will be read in a secret way from stdin instead.

Other configuration options

Other possible configuration options are:

loglevel (in the .toml file) / MODAL_LOGLEVEL (as an env var). Defaults to WARNING. Set this to DEBUG to see internal messages.
logs_timeout (in the .toml file) / MODAL_LOGS_TIMEOUT (as an env var). Defaults to 10. Number of seconds to wait for logs to drain when closing the session, before giving up.
max_throttle_wait (in the .toml file) / MODAL_MAX_THROTTLE_WAIT (as an env var). Defaults to None (no limit). Maximum number of seconds to wait when requests are being throttled (i.e., due to rate limiting or other cases that can normally be resolved through backoff).
force_build (in the .toml file) / MODAL_FORCE_BUILD (as an env var). Defaults to False. When set, ignores the Image cache and builds all Image layers. Note that this will break the cache for all images based on the rebuilt layers, so other images may rebuild on subsequent runs / deploys even if the config is reverted.
ignore_cache (in the .toml file) / MODAL_IGNORE_CACHE (as an env var). Defaults to False. When set, ignores the Image cache and builds all Image layers. Unlike force_build, this will not overwrite the cache for other images that have the same recipe. Subsequent runs that do not use this option will pull the previous Image from the cache, if one exists. It can be useful for testing an App’s robustness to Image rebuilds without clobbering Images used by other Apps.
traceback (in the .toml file) / MODAL_TRACEBACK (as an env var). Defaults to False. Enables printing full tracebacks on unexpected CLI errors, which can be useful for debugging client issues.
log_pattern (in the .toml file) / MODAL_LOG_PATTERN (as an env var). Defaults to "[modal-client] %(asctime)s %(message)s" The log formatting pattern that will be used by the modal client itself. See https://docs.python.org/3/library/logging.html#logrecord-attributes for available log attributes.
dev_suffix (in the .toml file) / MODAL_DEV_SUFFIX (as an env var). Overrides the default -dev suffix added to URLs generated for web endpoints when the App is ephemeral (i.e., created via modal serve). Must be a short alphanumeric string.
Meta-configuration

Some “meta-options” are set using environment variables only:

MODAL_CONFIG_PATH lets you override the location of the .toml file, by default ~/.modal.toml.
MODAL_PROFILE lets you use multiple sections in the .toml file and switch between them. It defaults to “default”.
```python
modal.config.Config 
class Config(object)
```

Singleton that holds configuration used by Modal internally.

```python
def __init__(self):
```

get
```python
def get(self, key, profile=None, use_env=True):
```

Looks up a configuration value.

Will check (in decreasing order of priority):

Any environment variable of the form MODAL_FOO_BAR (when use_env is True)
Settings in the user’s .toml configuration file
The default value of the setting
override_locally
```python
def override_locally(self, key: str, value: str):
    # Override setting in this process by overriding environment variable for the setting
    #
    # Does NOT write back to settings file etc.
```

to_dict
```python
def to_dict(self):
```

```python
modal.config.config_profiles 
def config_profiles():
```

List the available modal profiles in the .modal.toml file.

```python
modal.config.config_set_active_profile 
def config_set_active_profile(profile: str) -> None:
```

Set the user’s active modal profile by writing it to the .modal.toml file.
