# OpenAPI Specification v3.0.3 -- Server Objects

Source: https://spec.openapis.org/oas/v3.0.3.html (Sections 4.7.5--4.7.6)

---

## 4.7.5 Server Object

An object representing a Server.

### 4.7.5.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `url` | `string` | **REQUIRED** | A URL to the target host. This URL supports Server Variables and MAY be relative, to indicate that the host location is relative to the location where the OpenAPI document is being served. Variable substitutions will be made when a variable is named in `{`brackets`}`. |
| `description` | `string` | No | An optional string describing the host designated by the URL. [CommonMark] syntax MAY be used for rich text representation. |
| `variables` | Map[`string`, [Server Variable Object](#476-server-variable-object)] | No | A map between a variable name and its value. The value is used for substitution in the server's URL template. |

This object MAY be extended with Specification Extensions.

### 4.7.5.2 Server Object Example

A single server would be described as:

**JSON:**

```json
{
  "url": "https://development.gigantic-server.com/v1",
  "description": "Development server"
}
```

**YAML:**

```yaml
url: https://development.gigantic-server.com/v1
description: Development server
```

The following shows how multiple servers can be described, for example, at the OpenAPI Object's `servers`:

**JSON:**

```json
{
  "servers": [
    {
      "url": "https://development.gigantic-server.com/v1",
      "description": "Development server"
    },
    {
      "url": "https://staging.gigantic-server.com/v1",
      "description": "Staging server"
    },
    {
      "url": "https://api.gigantic-server.com/v1",
      "description": "Production server"
    }
  ]
}
```

**YAML:**

```yaml
servers:
- url: https://development.gigantic-server.com/v1
  description: Development server
- url: https://staging.gigantic-server.com/v1
  description: Staging server
- url: https://api.gigantic-server.com/v1
  description: Production server
```

The following shows how variables can be used for a server configuration:

**JSON:**

```json
{
  "servers": [
    {
      "url": "https://{username}.gigantic-server.com:{port}/{basePath}",
      "description": "The production API server",
      "variables": {
        "username": {
          "default": "demo",
          "description": "this value is assigned by the service provider, in this example `gigantic-server.com`"
        },
        "port": {
          "enum": [
            "8443",
            "443"
          ],
          "default": "8443"
        },
        "basePath": {
          "default": "v2"
        }
      }
    }
  ]
}
```

**YAML:**

```yaml
servers:
- url: https://{username}.gigantic-server.com:{port}/{basePath}
  description: The production API server
  variables:
    username:
      # note! no enum here means it is an open value
      default: demo
      description: this value is assigned by the service provider, in this example `gigantic-server.com`
    port:
      enum:
        - '8443'
        - '443'
      default: '8443'
    basePath:
      # open meaning there is the opportunity to use special base paths as assigned by the provider, default is `v2`
      default: v2
```

---

## 4.7.6 Server Variable Object

An object representing a Server Variable for server URL template substitution.

### 4.7.6.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `enum` | [`string`] | No | An enumeration of string values to be used if the substitution options are from a limited set. The array SHOULD NOT be empty. |
| `default` | `string` | **REQUIRED** | The default value to use for substitution, which SHALL be sent if an alternate value is not supplied. Note this behavior is different than the Schema Object's treatment of default values, because in those cases parameter values are optional. If the `enum` is defined, the value SHOULD exist in the enum's values. |
| `description` | `string` | No | An optional description for the server variable. [CommonMark] syntax MAY be used for rich text representation. |

This object MAY be extended with Specification Extensions.
