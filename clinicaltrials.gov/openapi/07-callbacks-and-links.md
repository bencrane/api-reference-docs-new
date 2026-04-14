# OpenAPI Specification v3.0.3 -- Callbacks, Examples, and Links

Source: https://spec.openapis.org/oas/v3.0.3.html (Sections 4.7.18--4.7.20)

---

## 4.7.18 Callback Object

A map of possible out-of band callbacks related to the parent operation. Each value in the map is a Path Item Object that describes a set of requests that may be initiated by the API provider and the expected responses. The key value used to identify the path item object is an expression, evaluated at runtime, that identifies a URL to use for the callback operation.

### 4.7.18.1 Patterned Fields

| Field Pattern | Type | Required? | Description |
|---|---|---|---|
| `{expression}` | [Path Item Object] | No | A Path Item Object used to define a callback request and expected responses. A [complete example](../examples/v3.0/callback-example.yaml) is available. |

This object MAY be extended with Specification Extensions.

### 4.7.18.2 Key Expression

The key that identifies the Path Item Object is a runtime expression that can be evaluated in the context of a runtime HTTP request/response to identify the URL to be used for the callback request. A simple example might be `$request.body#/url`. However, using a runtime expression the complete HTTP message can be accessed. This includes accessing any part of a body that a JSON Pointer [RFC6901](https://tools.ietf.org/html/rfc6901) can reference.

For example, given the following HTTP request:

```http
POST /subscribe/myevent?queryUrl=http://clientdomain.com/stillrunning HTTP/1.1
Host: example.org
Content-Type: application/json
Content-Length: 187

{
  "failedUrl" : "http://clientdomain.com/failed",
  "successUrls" : [
    "http://clientdomain.com/fast",
    "http://clientdomain.com/medium",
    "http://clientdomain.com/slow"
  ]
}

201 Created
Location: http://example.org/subscription/1
```

The following examples show how the various expressions evaluate, assuming the callback URL is being used as the key expression:

| Expression | Value |
|---|---|
| `$url` | `http://example.org/subscribe/myevent?queryUrl=http://clientdomain.com/stillrunning` |
| `$method` | `POST` |
| `$request.path.eventType` | `myevent` |
| `$request.query.queryUrl` | `http://clientdomain.com/stillrunning` |
| `$request.header.content-Type` | `application/json` |
| `$request.body#/failedUrl` | `http://clientdomain.com/failed` |
| `$request.body#/successUrls/2` | `http://clientdomain.com/medium` |
| `$response.header.Location` | `http://example.org/subscription/1` |

### 4.7.18.3 Callback Object Examples

The following example shows a callback to the URL specified by the `$request.query.queryUrl` runtime expression in the query string with a request body containing the event payload:

**YAML:**

```yaml
myCallback:
  '{$request.query.queryUrl}':
    post:
      requestBody:
        description: Callback payload
        content:
          'application/json':
            schema:
              $ref: '#/components/schemas/SomePayload'
      responses:
        '200':
          description: callback successfully processed
```

The following example uses the `$request.body#/id` and `$request.body#/email` runtime expression to build a callback URL from values in the request body, and shows a complete callback operation specification:

**YAML:**

```yaml
transactionCallback:
  'http://notificationServer.com?transactionId={$request.body#/id}&email={$request.body#/email}':
    post:
      requestBody:
        description: Callback payload
        content:
          'application/json':
            schema:
              $ref: '#/components/schemas/SomePayload'
      responses:
        '200':
          description: callback successfully processed
```

---

## 4.7.19 Example Object

### 4.7.19.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `summary` | `string` | No | Short description for the example. |
| `description` | `string` | No | Long description for the example. [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text representation. |
| `value` | Any | No | Embedded literal example. The `value` field and `externalValue` field are mutually exclusive. To represent examples of media types that cannot naturally be represented in JSON or YAML, use a string value to contain the example, escaping where necessary. |
| `externalValue` | `string` | No | A URL that points to the literal example. This provides the capability to reference examples that cannot easily be included in JSON or YAML documents. The `value` field and `externalValue` field are mutually exclusive. |

This object MAY be extended with Specification Extensions.

In all cases, the example value is expected to be compatible with the type schema of its associated value. Tooling implementations MAY choose to validate compatibility automatically, and reject the example value(s) if incompatible.

### 4.7.19.2 Example Object Examples

In a request body:

**YAML:**

```yaml
requestBody:
  content:
    'application/json':
      schema:
        $ref: '#/components/schemas/Address'
      examples:
        foo:
          summary: A foo example
          value: {"foo": "bar"}
        bar:
          summary: A bar example
          value: {"bar": "baz"}
    'application/xml':
      examples:
        xmlExample:
          summary: This is an example in XML
          externalValue: 'http://example.org/examples/address-example.xml'
    'text/plain':
      examples:
        textExample:
          summary: This is a text example
          externalValue: 'http://foo.bar/examples/address-example.txt'
```

In a parameter:

**YAML:**

```yaml
parameters:
  - name: 'zipCode'
    in: 'query'
    schema:
      type: 'string'
      format: 'zip-code'
    examples:
      zip-example:
        $ref: '#/components/examples/zip-example'
```

In a response:

**YAML:**

```yaml
responses:
  '200':
    description: your car appointment has been booked
    content:
      application/json:
        schema:
          $ref: '#/components/schemas/SuccessResponse'
        examples:
          confirmation-success:
            $ref: '#/components/examples/confirmation-success'
```

---

## 4.7.20 Link Object

The `Link object` represents a possible design-time link for a response. The presence of a link does not guarantee the caller's ability to successfully invoke it, rather it provides a known relationship and traversal mechanism between responses and other operations.

Unlike _dynamic_ links (i.e. links provided **in** the response payload), the OAS linking mechanism does not require link information in the runtime response.

For computing links, and providing instructions to execute them, a runtime expression is used for accessing values in an operation and using them as parameters while invoking the linked operation.

A linked operation MUST be identified using either an `operationRef` or `operationId`. In the case of an `operationId`, it MUST be unique and resolved in the scope of the OAS document. Because of the potential for name clashes, the `operationRef` syntax is preferred for specifications with external references.

### 4.7.20.1 Fixed Fields

| Field Name | Type | Required? | Description |
|---|---|---|---|
| `operationRef` | `string` | No | A relative or absolute URI reference to an OAS operation. This field is mutually exclusive of the `operationId` field, and MUST point to an Operation Object. Relative `operationRef` values MAY be used to locate an existing Operation Object in the OpenAPI definition. |
| `operationId` | `string` | No | The name of an _existing_, resolvable OAS operation, as defined with a unique `operationId`. This field is mutually exclusive of the `operationRef` field. |
| `parameters` | Map[`string`, Any \| {expression}] | No | A map representing parameters to pass to an operation as specified with `operationId` or identified via `operationRef`. The key is the parameter name to be used, whereas the value can be a constant or an expression to be evaluated and passed to the linked operation. The parameter name can be qualified using the parameter location `[{in}.]{name}` for operations that use the same parameter name in different locations (e.g. `path.id`). |
| `requestBody` | Any \| {expression} | No | A literal value or expression to use as a request body when calling the target operation. |
| `description` | `string` | No | A description of the link. [CommonMark syntax](https://spec.commonmark.org/) MAY be used for rich text representation. |
| `server` | [Server Object] | No | A server object to be used by the target operation. |

This object MAY be extended with Specification Extensions.

### 4.7.20.2 Examples

Computing a link from a request operation where the `$request.path.id` is used to pass a request parameter to the linked operation:

**YAML:**

```yaml
paths:
  /users/{id}:
    parameters:
    - name: id
      in: path
      required: true
      description: the user identifier, as userId
      schema:
        type: string
    get:
      responses:
        '200':
          description: the user being returned
          content:
            application/json:
              schema:
                type: object
                properties:
                  uuid: # the unique user id
                    type: string
                    format: uuid
          links:
            address:
              # the target link operationId
              operationId: getUserAddress
              parameters:
                # get the `id` field from the request path parameter named `id`
                userId: $request.path.id
  # the path item of the linked operation
  /users/{userid}/address:
    parameters:
    - name: userid
      in: path
      required: true
      description: the user identifier, as userId
      schema:
        type: string
    # linked operation
    get:
      operationId: getUserAddress
      responses:
        '200':
          description: the user's address
```

When a runtime expression fails to evaluate, no parameter value is passed to the target operation.

Values from the response body can be used to drive a linked operation:

**YAML:**

```yaml
links:
  address:
    operationId: getUserAddressByUUID
    parameters:
      # get the `uuid` field from the `uuid` field in the response body
      userUuid: $response.body#/uuid
```

### 4.7.20.3 OperationRef Examples

As references to `operationId` MAY NOT be possible (the `operationId` is an optional field in an Operation Object), references MAY also be made through a relative `operationRef`:

**YAML:**

```yaml
links:
  UserRepositories:
    # returns array of '#/components/schemas/repository'
    operationRef: '#/paths/~12.0~1repositories~1{username}/get'
    parameters:
      username: $response.body#/username
```

Or an absolute `operationRef`:

**YAML:**

```yaml
links:
  UserRepositories:
    # returns array of '#/components/schemas/repository'
    operationRef: 'https://na2.gigantic-server.com/#/paths/~12.0~1repositories~1{username}/get'
    parameters:
      username: $response.body#/username
```

Note that in the use of `operationRef`, the _escaped forward-slash_ is necessary when using JSON references.

### 4.7.20.4 Runtime Expressions

Runtime expressions allow defining values based on information that will only be available within the HTTP message in an actual API call. This mechanism is used by Link Objects and Callback Objects.

The runtime expression is defined by the following ABNF syntax:

```abnf
expression = ( "$url" / "$method" / "$statusCode" / "$request." source / "$response." source )
source = ( header-reference / query-reference / path-reference / body-reference )
header-reference = "header." token
query-reference = "query." name
path-reference = "path." name
body-reference = "body" ["#" json-pointer ]
json-pointer    = *( "/" reference-token )
reference-token = *( unescaped / escaped )
unescaped       = %x00-2E / %x30-7D / %x7F-10FFFF
escaped         = "~" ( "0" / "1" )
name = *( CHAR )
token = 1*tchar
tchar = "!" / "#" / "$" / "%" / "&" / "'" / "*" / "+" / "-" / "." /
  "^" / "_" / "`" / "|" / "~" / DIGIT / ALPHA
```

The `json-pointer` is taken from [RFC6901](https://tools.ietf.org/html/rfc6901), `char` from [RFC7159](https://tools.ietf.org/html/rfc7159), and `token` from [RFC7230](https://tools.ietf.org/html/rfc7230).

The `name` identifier is case-sensitive, whereas `token` is not.

### 4.7.20.5 Examples

| Source Location | example expression | notes |
|---|---|---|
| HTTP Method | `$method` | The allowable values for the `$method` will be those for the HTTP operation. |
| Requested media type | `$request.header.accept` | |
| Request parameter | `$request.path.id` | Request parameters MUST be declared in the `parameters` section of the parent operation or they cannot be evaluated. This includes request headers. |
| Request body property | `$request.body#/user/uuid` | In operations which accept payloads, references may be made to portions of the `requestBody` or the entire body. |
| Request URL | `$url` | |
| Response value | `$response.body#/status` | In operations which return payloads, references may be made to portions of the response body or the entire body. |
| Response header | `$response.header.Server` | Single header values only are available. |

Runtime expressions preserve the type of the referenced value. Expressions can be embedded into string values by surrounding the expression with `{}` curly braces.
