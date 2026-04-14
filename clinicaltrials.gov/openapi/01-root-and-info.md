# OpenAPI Specification v3.0.3 -- Root and Info Objects

Source: https://spec.openapis.org/oas/v3.0.3.html (Sections 4.7.1--4.7.4)

---

## 4.7 Schema

In the following description, if a field is not explicitly REQUIRED or described with a MUST or SHALL, it can be considered OPTIONAL.

---

## 4.7.1 OpenAPI Object

This is the root document object of the OpenAPI document.

### 4.7.1.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `openapi` | `string` | **REQUIRED** | This string MUST be the semantic version number of the OpenAPI Specification version that the OpenAPI document uses. The `openapi` field SHOULD be used by tooling specifications and clients to interpret the OpenAPI document. This is not related to the API `info.version` string. |
| `info` | [Info Object](#472-info-object) | **REQUIRED** | Provides metadata about the API. The metadata MAY be used by tooling as required. |
| `servers` | [[Server Object]] | No | An array of Server Objects, which provide connectivity information to a target server. If the `servers` property is not provided, or is an empty array, the default value would be a Server Object with a `url` value of `/`. |
| `paths` | [Paths Object] | **REQUIRED** | The available paths and operations for the API. |
| `components` | [Components Object] | No | An element to hold various schemas for the specification. |
| `security` | [[Security Requirement Object]] | No | A declaration of which security mechanisms can be used across the API. The list of values includes alternative security requirement objects that can be used. Only one of the security requirement objects need to be satisfied to authorize a request. Individual operations can override this definition. To make security optional, an empty security requirement (`{}`) can be included in the array. |
| `tags` | [[Tag Object]] | No | A list of tags used by the specification with additional metadata. The order of the tags can be used to reflect on their order by the parsing tools. Not all tags that are used by the Operation Object must be declared. The tags that are not declared MAY be organized randomly or based on the tools' logic. Each tag name in the list MUST be unique. |
| `externalDocs` | [External Documentation Object] | No | Additional external documentation. |

This object MAY be extended with Specification Extensions.

---

## 4.7.2 Info Object

The object provides metadata about the API. The metadata MAY be used by the clients if needed, and MAY be presented in editing or documentation generation tools for convenience.

### 4.7.2.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `title` | `string` | **REQUIRED** | The title of the API. |
| `description` | `string` | No | A short description of the API. [CommonMark] syntax MAY be used for rich text representation. |
| `termsOfService` | `string` | No | A URL to the Terms of Service for the API. MUST be in the format of a URL. |
| `contact` | [Contact Object](#473-contact-object) | No | The contact information for the exposed API. |
| `license` | [License Object](#474-license-object) | No | The license information for the exposed API. |
| `version` | `string` | **REQUIRED** | The version of the OpenAPI document (which is distinct from the OpenAPI Specification version or the API implementation version). |

This object MAY be extended with Specification Extensions.

### 4.7.2.2 Info Object Example

**JSON:**

```json
{
  "title": "Sample Pet Store App",
  "description": "This is a sample server for a pet store.",
  "termsOfService": "http://example.com/terms/",
  "contact": {
    "name": "API Support",
    "url": "http://www.example.com/support",
    "email": "support@example.com"
  },
  "license": {
    "name": "Apache 2.0",
    "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
  },
  "version": "1.0.1"
}
```

**YAML:**

```yaml
title: Sample Pet Store App
description: This is a sample server for a pet store.
termsOfService: http://example.com/terms/
contact:
  name: API Support
  url: http://www.example.com/support
  email: support@example.com
license:
  name: Apache 2.0
  url: https://www.apache.org/licenses/LICENSE-2.0.html
version: 1.0.1
```

---

## 4.7.3 Contact Object

Contact information for the exposed API.

### 4.7.3.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `name` | `string` | No | The identifying name of the contact person/organization. |
| `url` | `string` | No | The URL pointing to the contact information. MUST be in the format of a URL. |
| `email` | `string` | No | The email address of the contact person/organization. MUST be in the format of an email address. |

This object MAY be extended with Specification Extensions.

### 4.7.3.2 Contact Object Example

**JSON:**

```json
{
  "name": "API Support",
  "url": "http://www.example.com/support",
  "email": "support@example.com"
}
```

**YAML:**

```yaml
name: API Support
url: http://www.example.com/support
email: support@example.com
```

---

## 4.7.4 License Object

License information for the exposed API.

### 4.7.4.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `name` | `string` | **REQUIRED** | The license name used for the API. |
| `url` | `string` | No | A URL to the license used for the API. MUST be in the format of a URL. |

This object MAY be extended with Specification Extensions.

### 4.7.4.2 License Object Example

**JSON:**

```json
{
  "name": "Apache 2.0",
  "url": "https://www.apache.org/licenses/LICENSE-2.0.html"
}
```

**YAML:**

```yaml
name: Apache 2.0
url: https://www.apache.org/licenses/LICENSE-2.0.html
```
