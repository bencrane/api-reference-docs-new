# OpenAPI Specification v3.0.3 -- Overview, Definitions, and Format

Source: https://spec.openapis.org/oas/v3.0.3.html
Version: 3.0.3 (20 February 2020)
License: The Apache License, Version 2.0

---

## 1. OpenAPI Specification

### 1.1 Version 3.0.3

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.

This document is licensed under The Apache License, Version 2.0.

---

## 2. Introduction

The OpenAPI Specification (OAS) defines a standard, language-agnostic interface to RESTful APIs which allows both humans and computers to discover and understand the capabilities of the service without access to source code, documentation, or through network traffic inspection. When properly defined, a consumer can understand and interact with the remote service with a minimal amount of implementation logic.

An OpenAPI definition can then be used by documentation generation tools to display the API, code generation tools to generate servers and clients in various programming languages, testing tools, and many other use cases.

---

## 3. Definitions

### 3.1 OpenAPI Document

A document (or set of documents) that defines or describes an API. An OpenAPI definition uses and conforms to the OpenAPI Specification.

### 3.2 Path Templating

Path templating refers to the usage of template expressions, delimited by curly braces (`{}`), to mark a section of a URL path as replaceable using path parameters.

Each template expression in the path MUST correspond to a path parameter that is included in the Path Item itself and/or in each of the Path Item's Operations.

### 3.3 Media Types

Media type definitions are spread across several resources. The media type definitions SHOULD be in compliance with [RFC6838].

Some examples of possible media type definitions:

```
text/plain; charset=utf-8
application/json
application/vnd.github+json
application/vnd.github.v3+json
application/vnd.github.v3.raw+json
application/vnd.github.v3.text+json
application/vnd.github.v3.html+json
application/vnd.github.v3.full+json
application/vnd.github.v3.diff
application/vnd.github.v3.patch
```

### 3.4 HTTP Status Codes

The HTTP Status Codes are used to indicate the status of the executed operation. The available status codes are defined by [RFC7231] Section 6 and registered status codes are listed in the IANA Status Code Registry.

---

## 4. Specification

### 4.1 Versions

The OpenAPI Specification is versioned using Semantic Versioning 2.0.0 (semver) and follows the semver specification.

The `major.minor` portion of the semver (for example `3.0`) SHALL designate the OAS feature set. Typically, `.patch` versions address errors in this document, not the feature set. Tooling which supports OAS 3.0 SHOULD be compatible with all OAS 3.0.* versions. The patch version SHOULD NOT be considered by tooling, making no distinction between `3.0.0` and `3.0.1` for example.

Each new minor version of the OpenAPI Specification SHALL allow any OpenAPI document that is valid against any previous minor version of the Specification, within the same major version, to be updated to the new Specification version with equivalent semantics. Such an update MUST only require changing the `openapi` property to the new minor version.

For example, a valid OpenAPI 3.0.2 document, upon changing its `openapi` property to `3.1.0`, SHALL be a valid OpenAPI 3.1.0 document, semantically equivalent to the original OpenAPI 3.0.2 document. New minor versions of the OpenAPI Specification MUST be written to ensure this form of backward compatibility.

An OpenAPI document compatible with OAS 3.*.* contains a required `openapi` field which designates the semantic version of the OAS that it uses. (OAS 2.0 documents contain a top-level version field named `swagger` and value `"2.0"`.)

### 4.2 Format

An OpenAPI document that conforms to the OpenAPI Specification is itself a JSON object, which may be represented either in JSON or YAML format.

For example, if a field has an array value, the JSON array representation will be used:

```json
{
   "field": [ 1, 2, 3 ]
}
```

All field names in the specification are **case sensitive**. This includes all fields that are used as keys in a map, except where explicitly noted that keys are case insensitive.

The schema exposes two types of fields: **Fixed fields**, which have a declared name, and **Patterned fields**, which declare a regex pattern for the field name.

Patterned fields MUST have unique names within the containing object.

In order to preserve the ability to round-trip between YAML and JSON formats, YAML version 1.2 is RECOMMENDED along with some additional constraints:

- Tags MUST be limited to those allowed by the JSON Schema ruleset.
- Keys used in YAML maps MUST be limited to a scalar string, as defined by the YAML Failsafe schema ruleset.

> **Note:** While APIs may be defined by OpenAPI documents in either YAML or JSON format, the API request and response bodies and other content are not required to be JSON or YAML.

### 4.3 Document Structure

An OpenAPI document MAY be made up of a single document or be divided into multiple, connected parts at the discretion of the user. In the latter case, `$ref` fields MUST be used in the specification to reference those parts as follows from the JSON Schema definitions.

It is RECOMMENDED that the root OpenAPI document be named: `openapi.json` or `openapi.yaml`.

### 4.4 Data Types

Primitive data types in the OAS are based on the types supported by the JSON Schema Specification Wright Draft 00.

Note that `integer` as a type is also supported and is defined as a JSON number without a fraction or exponent part.

`null` is not supported as a type (see `nullable` for an alternative solution).

Models are defined using the Schema Object, which is an extended subset of JSON Schema Specification Wright Draft 00.

Primitives have an optional modifier property: `format`. OAS uses several known formats to define in fine detail the data type being used. However, to support documentation needs, the `format` property is an open `string`-valued property, and can have any value. Formats such as `"email"`, `"uuid"`, and so on, MAY be used even though undefined by this specification.

Types that are not accompanied by a `format` property follow the type definition in the JSON Schema. Tools that do not recognize a specific `format` MAY default back to the `type` alone, as if the `format` is not specified.

The formats defined by the OAS are:

| `type` | `format` | Comments |
|---|---|---|
| `integer` | `int32` | signed 32 bits |
| `integer` | `int64` | signed 64 bits (a.k.a long) |
| `number` | `float` | |
| `number` | `double` | |
| `string` | | |
| `string` | `byte` | base64 encoded characters |
| `string` | `binary` | any sequence of octets |
| `boolean` | | |
| `string` | `date` | As defined by `full-date` - [RFC3339] Section 5.6 |
| `string` | `date-time` | As defined by `date-time` - [RFC3339] Section 5.6 |
| `string` | `password` | A hint to UIs to obscure input. |

### 4.5 Rich Text Formatting

Throughout the specification `description` fields are noted as supporting [CommonMark] markdown formatting.

Where OpenAPI tooling renders rich text it MUST support, at a minimum, markdown syntax as described by [CommonMark-0.27]. Tooling MAY choose to ignore some CommonMark features to address security concerns.

### 4.6 Relative References in URLs

Unless specified otherwise, all properties that are URLs MAY be relative references as defined by [RFC3986] Section 4.2.

Relative references are resolved using the URLs defined in the Server Object as a Base URI.

Relative references used in `$ref` are processed as per JSON Reference, using the URL of the current document as the base URI. See also the Reference Object.
