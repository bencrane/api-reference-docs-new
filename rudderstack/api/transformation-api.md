# Transformations API

API Specification to manage your RudderStack Transformations and Libraries.

* * *

  * __15 minute read

  * 


RudderStack’s Transformations API allows you to create, read, update and delete transformations and libraries programmatically by making HTTP calls.

This guide describes the various API operations, related request and response structures, and error codes associated with this API.

## Prerequisites

  * Generate a [workspace-level Service Access Token](<https://www.rudderstack.com/docs/access-management/service-access-tokens/#workspace-sat>) with the following permissions to authenticate the API:

Resource| Permissions  
---|---  
Transformations| **Create & Delete**, **Connect** , **Edit**  
Transformation Libraries| **Edit**  
Destinations| **Connect**  
  
#### Token permissions for legacy RBAC system

If you are on the [legacy Permissions Management (RBAC) system](<https://www.rudderstack.com/docs/archive/dashboard-guides/user-management/>), your workspace-level Service Access Token should have minimum **Admin** permissions with **Grant edit access** toggled on under **Transformations**.

See [this documentation](<https://www.rudderstack.com/docs/archive/dashboard-guides/service-access-tokens/#generate-service-access-token>) for more information on generating the token.

[![workspace-level Service Access Token with Transformations Admin permission](/docs/images/access-management/permissions/legacy/admin-transformations.webp)](</docs/images/access-management/permissions/legacy/admin-transformations.webp>)

## Authentication

The Transformations API is authenticated via HTTP Basic Authentication.

If you’re using Postman, authenticate the API by including an empty string (`""`) as the username and your workspace-level Service Access Token as the password in the **Authorization** tab.

> ![info](/docs/images/info.svg)
> 
> RudderStack recommends using:
> 
>   * Service Access Tokens (SATs) for production use cases that require shared access to the services and resources across the workspace.
>   * [Personal Access Tokens (PATs)](<https://www.rudderstack.com/docs/access-management/personal-access-tokens/>) for testing a service/feature or personal use cases.
> 


You can also pass your Service Access Token in the authorization header directly:
    
    
    Authorization: Basic {Base64Encoded(:<SERVICE_ACCESS_TOKEN>)}
    

An example is shown below:

  * Username: `""` (empty string)
  * Service Access Token: `<SERVICE_ACCESS_TOKEN>`
  * Header: `Basic {Base64Encoded(:<SERVICE_ACCESS_TOKEN>)}`


## Base URL

Use the base URL for your API requests depending on your region:
    
    
    https://api.rudderstack.com
    
    
    
    https://api.eu.rudderstack.com
    

## Transformations

RudderStack transformations are responsible for converting received event data into a suitable destination-specific format. All the transformation code is written in JavaScript.

> ![success](/docs/images/tick.svg)
> 
> We also support [user-specific transformations](<https://www.rudderstack.com/docs/transformations/overview/>) for real-time operations, such as aggregation and sampling.

Transformations help you to create a user-defined code that allow you to route your events in a manner that is suitable for your destinations.

#### Transformer payload

**Field**| **Type**| **Presence**| **Description**  
---|---|---|---  
`name`| String| Required| Sets the transformation name.  
`language`| String| Required| Language of the transformation code. Acceptable values are `javascript` and `pythonfaas`.  
`description`| String| Optional| Sets the transformation description.  
`code`| String| Optional| User-defined code that maps event data to destinations as defined by the user  
`codeVersion`| String| Optional| This is a number value always set to version “1” for API calls.  
`createdAt`| Date| Optional| The timestamp of the transformer when it is created  
`updatedAt`| Date| Optional| The timestamp of the transformer when it is updated  
`versionId`| String| Optional| Maintains a version of transformer every time it is updated  
`workspaceId`| Object| Optional| Workspace ID on which this transformation is created  
`destinations`| Array| Optional| List of all Destination IDs to which your transformation is connected  
  
### Create a transformation

Create an unpublished transformation.

When you create a transformation but do not publish it, that is, when `publish = false`, RudderStack creates revisions for the transformation, but it is not available to incoming event traffic and cannot connect to destinations.

When you wish to make the transformation live, see Publish a transformation.

POST

/transformations

**Query parameters** :

publish

optional, default is `false`

boolean

If `true`, publishes your transformer to the latest version; code is made live for incoming traffic.

* * *

**Example request** :

In this example, `publish` is `false`, which is the default setting for the parameter. When unpublished, RudderStack only creates revisions for the transformation, meaning that you cannot connect destinations to the transformation and it cannot be used for incoming event traffic.
    
    
    POST /transformations HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=
    Content-Type: application/json
    
    {
      "name": "Get metdata",
      "description": "Gets the metadata for an event",
      "code" : "export function transformEvent(message, metadata) { const met = metadata(message); return met; }",
      "language": "javascript"
    }
    
    
    
    curl --location 'https://api.rudderstack.com/transformations' \
    --header 'Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=' \
    --header 'Content-Type: application/json' \
    --data '{
    "name": "Get metdata",
    "description": "Gets the metadata for an event",
    "code" : "export function transformEvent(event, metadata) { const meta = metadata(event);\n event.meta = meta;\n return event; }",
    "language": "javascript"
    }
    

**Request body** :

events

optional

object

Pass a set of JSON events to be tested for your code. This should be an array of JSON data.

destinationIds

optional

array

Pass an array of `destinationIds` that you wish to connect with this transformation. You can connect only if `publish` is set to `true`.

name

optional

string

The transformation name.

description

optional

string

Description of the transformation you are creating.

code

optional

string

The transformation code.

language

required

string

Language of the transformation code. Acceptable values are `javascript` and `pythonfaas`.

**Example response** :
    
    
    HTTP/1.1 200 OK
    content-type: application/json; charset=utf-8
    
    {
        "id": "2LnbcGgKON5BbHHuyYVesZ24uqu",
        "versionId": "2LnbcImcBqOTkm4FFVCpIakptZJ",
        "name": "Get metdata",
        "description": "Gets the metadata for an event",
        "code": "export function transformEvent(message, metadata) { const met = metadata(message); return met; }",
        "codeVersion": "1",
        "language": "javascript",
        "createdAt": "2023-02-16T01:11:11.586Z",
        "updatedAt": "2023-02-16T01:11:11.586Z"
    }
    

**Events JSON** : When passing events in the request body, format the events in JSON
    
    
    {
      "events": [
        {
          "anonymousId": "8d872292709c6fbe",
          "channel": "mobile",
          "context": {
            "traits": {
              "address": {
                "city": "Kolkata",
                "country": "India",
                "postalcode": "700096",
                "state": "West bengal",
                "street": "Park Street"
              }
            }
          },
          "properties": {
            "revenue": "30",
            "currency": "USD",
            "quantity": "5",
            "price": "58.0"
          }
        }
      ]
    }
    

### Publish a transformation

Publish your transformation. This request is the same as Create transformation except that you need to include `?publish=true` in the query, which will allow you to connect destinations to the transformation and make it available to incoming traffic.

When you publish a transformation, we maintain two copies of the transformer: one is published and the other is used for revisions. The published version can be connected to destinations and its code is made live for incoming traffic.

POST

/transformations?publish=true

**Query parameters** :

publish

optional, default is `false`

boolean

If `true`, publishes your transformer to the latest version; code is made live for incoming traffic.

* * *

**Request body** :

events

optional

object

Pass a set of JSON events to be tested for your code. This should be an array of JSON data.

destinationIds

optional

array

Pass an array of `destinationIds` that you wish to connect with this transformation. You can connect only if `publish` is set to `true`.

name

optional

string

Name of the transformer that you wish to create.

description

optional

string

Description of the transformer you are creating.

code

optional

string

The transformer code.

language

required

string

Language of the transformation code. Acceptable values are `javascript` and `pythonfaas`.
    
    
    POST /transformations?publish=true HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=
    Content-Type: application/json
    
    {
      "name": "Cool transformation",
      "description": "A test description",
      "code": "export function transformEvent(event) { return event; }",
      "destinations": ["2C8YtptB4KF2eL3KRi9mCFkY3BF"],
      "language": "javascript"
    }
    
    
    
    curl --location 'https://api.rudderstack.com/transformations?publish=true' \
    --header 'Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=' \
    --header 'Content-Type: application/json' \
    --data '{
      "name": "Cool transformation",
      "description": "A test description",
      "code": "export function transformEvent(event) { return event; }",
      "destinations": ["2C8YtptB4KF2eL3KRi9mCFkY3BF"],
      "language": "javascript"
    }'
    

**Example response** :
    
    
    HTTP/1.1 200 OK
    content-type: application/json; charset=utf-8
    
    {
      "id": "2LpkmqnLEuUziYZcfRCdNLDQxDk",
      "versionId": "2LpkmrHiyW4gXovOzhvtzbhdZ23",
      "name": "Cool transformation",
      "description": "A test description",
      "code": "export function transformEvent(event) { return event; }",
      "codeVersion": "1",
      "language": "javascript",
      "createdAt": "2023-02-16T19:26:13.263Z",
      "updatedAt": "2023-02-16T19:26:13.263Z",
      "destinations": []
    }
    

### List all transformations

List all published transformations for a workspace.

GET

/transformations

**Example request** :
    
    
    GET /transformations HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=
    
    
    
    curl --location 'https://api.rudderstack.com/transformations' \
    --header 'Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=' \
    

**Example response** :
    
    
    HTTP/1.1 200 OK
    content-type: application/json; charset=utf-8
    
    {
      "transformations": [
        {
          "id": "sedrftg",
          "versionId": "edrtv",
          "name": "new Transformations-2",
          "description": "",
          "code": "export function transformEvent(event) { return event; }",
          "codeVersion": "1",
          "language": "javascript",
          "createdAt": "2021-03-04T04:48:27.288Z",
          "updatedAt": "2021-03-04T04:48:27.288Z",
          "destinations": []
        },
        {
          "id": "xcgvhcfdx",
          "versionId": "dtvbyutbvc",
          "name": "Update Transformations and Publish",
          "description": "",
          "code": "function transformEvent(event) { return event; } ",
          "codeVersion": "1",
          "language": "javascript",
          "createdAt": "2021-03-04T10:07:25.513Z",
          "updatedAt": "2021-03-04T10:07:25.513Z",
          "destinations": []
        }
      ]
    }
    

### Retrieve a single transformation

Retrieve a published transformations from an ID.

GET

/transformations/{id}

**Example request** :
    
    
    GET /transformations/2C8Vk2wj8qkofy00YzJbvJOGeqa HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=
    
    
    
    curl --location 'https://api.rudderstack.com/transformations/2C8Vk2wj8qkofy00YzJbvJOGeqa' \
    --header 'Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=' \
    

**Example response** :
    
    
    HTTP/1.1 200 OK
    content-type: application/json; charset=utf-8
    
    {
      "id": "swderftgy",
      "versionId": "edftgyhu",
      "name": "new Transformations-2",
      "description": "",
      "code": "export function transformEvent(event) { return event; } ",
      "codeVersion": "1",
      "language": "javascript",
      "createdAt": "2021-03-04T04:48:27.288Z",
      "updatedAt": "2021-03-04T04:48:27.288Z",
      "destinations": []
    }
    

### Update and publish a transformation

Updating a transformation creates a new **revision** and sets it as **published** if the `publish` flag is set is `true`, and its code becomes live for upcoming traffic. If the `publish` flag is `false` , it only creates a new **revision** for that transformation.

> ![warning](/docs/images/warning.svg)
> 
> You cannot update the language used to write the transformation code, that is, a JavaScript transformation cannot be converted to Python and vice versa.

POST

/transformations/{id}

**Example request** :
    
    
    POST /transformations/2C8Vk2wj8qkofy00YzJbvJOGeqa HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=
    Content-Type: application/json
    Content-Length: 158
    
    {
        "name":"Updated transformation JS 2",
        "description": "Updated description",
        "code":"export function transformEvent(event) { return event; }\n"
    }
    
    
    
    curl --location 'https://api.rudderstack.com/transformations/2C8Vk2wj8qkofy00YzJbvJOGeqa' \
    --header 'Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=' \
    --header 'Content-Type: application/json' \
    --data '{
        "name":"Updated transformation JS 2",
        "description": "Updated description",
        "code":"export function transformEvent(event) { return event; }\n"
    }'
    

**Example response** :
    
    
    {
        "id": "2C8Vk2wj8qkofy00YzJbvJOGeqa",
        "versionId": "2MTBAAFdGs29S080tsvyg8gbsUj",
        "name": "Updated transformation JS 2",
        "description": "Updated description",
        "code": "export function transformEvent(event) { return event; }\n",
        "codeVersion": "1",
        "language": "javascript",
        "createdAt": "2023-03-02T18:23:30.580Z",
        "updatedAt": "2023-03-02T18:23:30.580Z"
    }
    

### Delete a transformation

Delete a published transformation by ID. Note that RudderStack never deletes a transformation revision.

DELETE

/transformations/{id}

**Example request** :
    
    
    DELETE /transformations/2LyH0PQOBAJo7UgFXfDoMacGDPZ HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=
    
    
    
    curl --location --request DELETE 'https://api.rudderstack.com/transformations/2LyH0PQOBAJo7UgFXfDoMacGDPZ' \
    --header 'Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=' \
    

**Example response** :
    
    
    HTTP/1.1 200 OK
    

### List transformation versions

List all transformation versions for a given transformation ID.

GET

/transformations{id}/versions

**Example request** :
    
    
    GET /transformations/2C8Vk2wj8qkofy00YzJbvJOGeqa/versions HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=
    
    
    
    curl --location 'https://api.rudderstack.com/transformations/2C8Vk2wj8qkofy00YzJbvJOGeqa/versions' \
    --header 'Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=' \
    

**Query parameters** :

count

optional

number

Gets the number of objects in your array. By default always returns the first 5 objects.

orderBy

optional, default is `asc`

Pass either `asc` for ascending or `desc` for descending. By default, it sets the order as ascending on createdAt.

Possible Values: asc, desc

* * *

**Example response** :
    
    
    {
      "TransformationVersions": [
        {
          "id": "1pIYoILGZTNYZP4YYkeyNIKlitl",
          "versionId": "1pIYoLfEzcMK3D3M1ihjqI02wnx",
          "name": "Update Transformations and Publish",
          "description": "",
          "code": "export function transformEvent(event) { return event; }\n",
          "codeVersion": "1",
          "language": "javascript",
          "createdAt": "2021-03-04T10:07:24.562Z",
          "updatedAt": "2021-03-04T10:07:24.562Z"
        },
        {
          "id": "1pIYoILGZTNYZP4YYkeyNIKlitl",
          "versionId": "1pIhxFXd7NR7XDA914rLAn5f7wq",
          "name": "Update Transformations and Publish",
          "description": "Hey I am updated again",
          "code": "export default function cube(x) { return x * x * x ; }",
          "codeVersion": "1",
          "language": "javascript",
          "createdAt": "2021-03-04T11:22:36.102Z",
          "updatedAt": "2021-03-08T04:22:42.646Z"
        }
      ]
    }
    

### Retrieve a single transformation version

Get a single transformation revision.

GET

/transformations{id}/versions/{versionId}

**Example request** :
    
    
    GET /transformations/2C8Vk2wj8qkofy00YzJbvJOGeqa/versions/2C8ifOCgRIpxgyF9voHIgUHFP4c HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=
    
    
    
    curl --location 'https://api.rudderstack.com/transformations/2C8Vk2wj8qkofy00YzJbvJOGeqa/versions/2C8ifOCgRIpxgyF9voHIgUHFP4c' \
    --header 'Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=' \
    

**Example response** :
    
    
    HTTP/1.1 200 OK
    content-type: application/json; charset=utf-8
    
    {
      "id": "1pIYoILGZTNYZP4YYkeyNIKlitl",
      "versionId": "1pIYoLfEzcMK3D3M1ihjqI02wnx",
      "name": "Update Transformations and Publish",
      "description": "Updated sample transformation ready to be published",
      "code": "export function transformEvent(event) { return event; }\n",
      "codeVersion": "1",
      "language": "javascript",
      "createdAt": "2021-03-04T10:07:24.562Z",
      "updatedAt": "2021-03-04T10:07:24.562Z"
    }
    

## Libraries

Libraries are JavaScript code that you can write and export to be used in your transformations. They give you the flexibility for reusing and maintaining different versions of the transformation code.

Suppose you write an aggregation function. You can easily export them and use it within different transformations just by importing that module by the library name.

#### Libraries payload

**Field**| **Type**| **Presence**| **Description**  
---|---|---|---  
`name`| String| Required| Sets the library name. This name is used as modules when it is imported in the transformation code.  
`language`| String| Required| Language of the library code. Acceptable values are `javascript` and `pythonfaas`.  
`description`| String| Optional| Sets the library description  
`code`| String| Optional| The library code.  
`importName`| String| Optional| This is library name that users can use in their transformation code while importing that library.  
`createdAt`| Date| Optional| The timestamp when the transformer is created.  
`updatedAt`| Date| Optional| The timestamp when the transformer is updated.  
`versionId`| String| Optional| Maintains a version of library every time it is updated.  
`workspace`| Object| Optional| Dictionary of information that provides workspace data where any transformation is used.  
  
### Create a library

Create a library and get its object as a response.

POST

/libraries

**Example request** :
    
    
    POST /libraries HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Basic TVlfRU1BSUxfQUREUkVTUzpNAAAAQ0NFU1NfVE9LRU4=
    Content-Type: application/json
    Content-Length: 164
    
    {
        "name": "cool library",
        "description": "cool description",
        "code": "export function add(a,b) {return a+b; } export function sub(a,b) {return a-b; }",
        "language": "javascript"
    }
    
    
    
    curl --location 'https://api.rudderstack.com/libraries' \
    --header 'Authorization: Basic TVlfRU1BSUxfQUREUkVTUzpNAAAAQ0NFU1NfVE9LRU4=' \
    --header 'Content-Type: application/json' \
    --data '{
        "name": "cool library",
        "description": "cool description",
        "code": "export function add(a,b) {return a+b; } export function sub(a,b) {return a-b; }",
        "language": "javascript"
    }'
    

**Example response** :
    
    
    HTTP/1.1 200 OK
    content-type: application/json; charset=utf-8
    
    {
      "id": "2M1HnI40CGbHb4FxjjRBj1aFRZK",
      "versionId": "2M1HnJoHwL4zXE91pEwZaAHQp8F",
      "name": "cool library",
      "description": "cool description",
      "code": "export function add(a,b) {return a+b; } export function sub(a,b) {return a-b; }",
      "language": "javascript",
      "createdAt": "2023-02-20T21:25:33.380Z",
      "updatedAt": "2023-02-20T21:25:33.380Z",
      "importName": "coolLibrary"
    }
    

**Query parameters** :

publish

optional, default is `false`

boolean

If `true`, publishes your transformer to the latest version; code is made live for incoming traffic.

* * *

**Request body** :

name

required

string

Name of the library that you wish to create.

description

optional

string

Description of the library you.

code

required

string

The library code.

language

required

string

Language of the library code. Acceptable values are `javascript` and `pythonfaas`.

### List all libraries

Get all published libraries.

GET

/libraries

**Example request** :
    
    
    GET /libraries HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Basic TVlfRU1BSUxfQUREUkVTUzpNAAAAQ0NFU1NfVE9LRU4=
    
    
    
    curl --location 'https://api.rudderstack.com/libraries' \
    --header 'Authorization: Basic TVlfRU1BSUxfQUREUkVTUzpNAAAAQ0NFU1NfVE9LRU4=' \
    

**Example response** :
    
    
    HTTP/1.1 200 OK
    content-type: application/json; charset=utf-8
    
    {
      "libraries": [
        {
          "id": "1pHx15j5rXvmmQUIMBaQdIyrpr2",
          "versionId": "1pHxdlGL8IyoP7WfvRil4Qs88cp",
          "name": "Get Cube",
          "description": "First Library using apiCall",
          "code": "export default function cube(x) { return x * x ; }",
          "language": "javascript",
          "createdAt": "2021-03-04T05:01:46.985Z",
          "updatedAt": "2021-03-04T05:01:47.141Z",
          "importName": "getCube"
        },
        {
          "id": "1pT7933tHRBPlEMIZt5Zi3VIht1",
          "versionId": "1pT793mcqQkcyHdqwXkxHmtgMMg",
          "name": "User Defined Library",
          "description": "Get User context",
          "code": "    export default function cube(x) { return x * x * x; }",
          "language": "javascript",
          "createdAt": "2021-03-08T03:47:51.512Z",
          "updatedAt": "2021-03-08T03:47:51.512Z",
          "importName": "userDefinedLibrary"
        }
      ]
    }
    

### Retrieve a library by ID

Get a single published library by ID.

GET

/libraries/{id}

**Example request** :
    
    
    GET /libraries/2DmDQHMNpAk1HvvWBK2SlWhmPS2 HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Basic TVlfRU1BSUxfQUREUkVTUzpNAAAAQ0NFU1NfVE9LRU4=
    
    
    
    curl --location 'https://api.rudderstack.com/libraries/2DmDQHMNpAk1HvvWBK2SlWhmPS2' \
    --header 'Authorization: Basic TVlfRU1BSUxfQUREUkVTUzpNAAAAQ0NFU1NfVE9LRU4=' \
    

**Example response** :
    
    
    HTTP/1.1 200 OK
    content-type: application/json; charset=utf-8
    
    {
      "id": "1pT7933tHRBPlEMIZt5Zi3VIht1",
      "versionId": "1pT793mcqQkcyHdqwXkxHmtgMMg",
      "name": "User Defined Library",
      "description": "Get User context",
      "code": "    export default function cube(x) { return x * x * x; }",
      "language": "javascript",
      "createdAt": "2021-03-08T03:47:51.512Z",
      "updatedAt": "2021-03-08T03:47:51.512Z",
      "importName": "userDefinedLibrary"
    }
    

### List all library versions

Get all library revisions for a library ID.

GET

/libraries/{id}/versions

**Example request** :
    
    
    GET /libraries/2DmDQHMNpAk1HvvWBK2SlWhmPS2 HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Basic TVlfRU1BSUxfQUREUkVTUzpNAAAAQ0NFU1NfVE9LRU4=
    
    
    
    curl --location 'https://api.rudderstack.com/libraries/2DmDQHMNpAk1HvvWBK2SlWhmPS2' \
    --header 'Authorization: Basic TVlfRU1BSUxfQUREUkVTUzpNAAAAQ0NFU1NfVE9LRU4=' \
    

**Example response** :
    
    
    HTTP/1.1 200 OK
    content-type: application/json; charset=utf-8
    
    {
      "libraryVersions": [
        {
          "id": "1pT7933tHRBPlEMIZt5Zi3VIht1",
          "versionId": "1pT793mcqQkcyHdqwXkxHmtgMMg",
          "name": "userDefinedLibrary",
          "description": "Get User context",
          "code": "export default function cube(x) { return x * x * x; }",
          "language": "javascript",
          "createdAt": "2021-03-08T03:47:51.686Z",
          "updatedAt": "2021-03-08T03:47:51.686Z",
          "isPublished": false
        },
        {
          "id": "1pT7933tHRBPlEMIZt5Zi3VIht1",
          "versionId": "1pT8KDAD66mQxnaUQxJpNs9qLFn",
          "name": "userDefinedLibrary",
          "description": "Get Divisible by 2",
          "code": "export default function cube(x) { return 2 * x; }",
          "language": "javascript",
          "createdAt": "2021-03-08T03:57:33.738Z",
          "updatedAt": "2021-03-08T03:57:33.738Z",
          "isPublished": true
        }
      ]
    }
    

**Query parameters** :

count

optional

number

Gets the number of objects in your array. By default always returns the first 5 objects.

orderBy

optional, default is `asc`

Pass either `asc` for ascending or `desc` for descending. By default, it sets the order as ascending on createdAt.

Possible Values: asc, desc

* * *

### Retrieve a single library version

Get a single library revision.

GET

/libraries/{id}/versions/{versionId}

**Example request** :
    
    
    GET /libraries/1pT7933tHRBPlEMIZt5Zi3VIht1/versions/1pT8KDAD66mQxnaUQxJpNs9qLFn HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Basic TVlfRU1BSUxfQUREUkVTUzpNAAAAQ0NFU1NfVE9LRU4=
    
    
    
    curl --location 'https://api.rudderstack.com/libraries/1pT7933tHRBPlEMIZt5Zi3VIht1/versions/1pT8KDAD66mQxnaUQxJpNs9qLFn' \
    --header 'Authorization: Basic TVlfRU1BSUxfQUREUkVTUzpNAAAAQ0NFU1NfVE9LRU4=' \
    

**Example response** :
    
    
    HTTP/1.1 200 OK
    content-type: application/json; charset=utf-8
    
    {
      "id": "1pT7933tHRBPlEMIZt5Zi3VIht1",
      "versionId": "1pT8KDAD66mQxnaUQxJpNs9qLFn",
      "name": "userDefinedLibrary",
      "description": "Get Divisible by 2",
      "code": "export default function cube(x) { return 2 * x; }",
      "language": "javascript",
      "createdAt": "2021-03-08T03:57:33.738Z",
      "updatedAt": "2021-03-08T03:57:33.738Z",
      "isPublished": false
    }
    

### Update and publish a library

This request lets you update the code and description of the transformation library by specifying its ID. To publish the library, set the `publish` flag to `true`. If the `publish` flag is `false` , it only creates a new version of that library.

> ![warning](/docs/images/warning.svg)
> 
> Note that:
> 
>   * You cannot change the name of the library using this request.
>   * You cannot update the language used to write the library code, that is, a JavaScript library cannot be converted to Python and vice versa.
> 


POST

/libraries/{id}

**Request body** :

description

optional

string

The updated library description.

code

required

string

The updated library code.

language

required

string

Language of the library code.

**Example request** :
    
    
    POST /libraries/2MTEP4IhlKLXYtnbOqAOx1kKcBd HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=
    Content-Type: application/json
    Content-Length: 158
    {
        "description": "Updated library description",
        "code": "export function sum(a, b) { return a + b; }",
        "language": "javascript"
    }
    
    
    
    curl --location 'https://api.rudderstack.com/libraries/2MTEP4IhlKLXYtnbOqAOx1kKcBd' \
    --header 'Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=' \
    --header 'Content-Type: application/json' \
    --data '{
        "description": "Updated library description",
        "code": "export function sum(a, b) { return a + b; }",
        "language": "javascript"
    }'
    

**Example response** :
    
    
    HTTP/1.1 200 OK
    content-type: application/json; charset=utf-8
    
    {
      "id": "2MTDFOdoL9qQxFFnhl6oB23oAQ2",
        "versionId": "2MTDbAFBqzB7Wg8mWyWNBIk5DOU",
        "name": "Sample Transformation Library JS 2",
        "description": "Updated library description",
        "code": "export function sum(a, b) { return a + b; }",
        "language": "javascript",
        "createdAt": "2023-03-02T18:42:53.821Z",
        "updatedAt": "2023-03-02T18:42:53.821Z",
        "importName": "sampleTransformationLibraryJs2"
    }
    

### Delete a library

Delete a library by ID.

DELETE

/libraries/{id}

**Example request** :
    
    
    DELETE /libraries/2LyH0PQOBAJo7UgFXfDoMacGDPZ HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=
    
    
    
    curl --location --request DELETE 'https://api.rudderstack.com/libraries/2LyH0PQOBAJo7UgFXfDoMacGDPZ' \
    --header 'Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=' \
    

**Example response** :
    
    
    HTTP/1.1 200 OK
    

## Publish API

As an end user you can create a transformer/library and perform several edits on it. Note that **publishing is optional at`create`**.

If you perform some edits on this version of transformer, RudderStack takes your latest update as the published version, creates a copy of the older version, and saves it as revisions. Let’s assume that after creating some 7 to 8 such revisions of your transformer, you finally decide to use the second or third version of the transformer.

This is where the RudderStack **Publish API** comes into play.

### Publish a transformation or library

Publish any transformation revisions or library revisions.

POST

/libraries/publish

**Example request** :
    
    
    POST /libraries/publish HTTP/1.1
    Host: api.rudderstack.com
    Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=
    Content-Type: application/json
    Content-Length: 591
    {
      "transformations": [{
          "versionId": "2MTC30bbSUANEeLb7TeknDbBeFy",
          "testInput": [{
              "anonymousId": "8d872292709c6fbe",
              "channel": "mobile",
              "messageId": "m1"
            },
            {
              "anonymousId": "8d872292709c6fbe",
              "channel": "mobile",
              "messageId": "m2"
            }
          ]
        },
        {
          "versionId": "2MTAtB7m8oR7zLyBJS0QWkuUY93",
          "testInput": [{
              "anonymousId": "8d872292709c6fbe",
              "messageId": "m1"
            },
            {
              "anonymousId": "8d872292709c6fbe",
              "messageId": "m2"
            }
          ]
        }
      ],
      "libraries": [{
          "versionId": "2MTDbAFBqzB7Wg8mWyWNBIk5DOU"
        },
        {
          "versionId": "2MTEP94GdpHFzfwxzqENf5L0WjI"
        }
      ]
    }
    
    
    
    curl --location 'https://api.rudderstack.com/libraries/publish' \
    --header 'Authorization: Basic XYZleEBleGFtcGxlLmNvbToyTWxxbW9rRGxTeFE2bWJYQ1ZqcVFmbUpoRXk=' \
    --header 'Content-Type: application/json' \
    --data '{
        "transformations": [
            {
                "versionId": "2MTC30bbSUANEeLb7TeknDbBeFy",
                "testInput": [
                    {
                        "anonymousId": "8d872292709c6fbe",
                        "channel": "mobile",
                        "messageId": "m1"
                    },
                    {
                        "anonymousId": "8d872292709c6fbe",
                        "channel": "mobile",
                        "messageId": "m2"
                    }
                ]
            },
            {
                "versionId": "2MTAtB7m8oR7zLyBJS0QWkuUY93",
                "testInput": [
                    {
                        "anonymousId": "8d872292709c6fbe",
                        "messageId": "m1"
                    },
                    {
                        "anonymousId": "8d872292709c6fbe",
                        "messageId": "m2"
                    }
                ]
            }
        ],
        "libraries": [
            {
                "versionId": "2MTDbAFBqzB7Wg8mWyWNBIk5DOU"
            },
            {
                "versionId": "2MTEP94GdpHFzfwxzqENf5L0WjI"
            }
        ]
    }'
    

**Request body** :

transformations

optional

array

Pass an array of transformer `versionIds` that you wish to publish.

libraries

optional

array

Pass an array of library `versionIds` that you wish to publish.

One of above `transformations` or `libraries` must be present to make a successful `publish` call.

> ![info](/docs/images/info.svg)
> 
> A few things to note:
> 
>   * You can choose to publish some revisions transformer without the libraries.
>   * You can choose to publish some revisions libraries without the transformers.
>   * You can publish both library and transformation revisions.
> 


> ![warning](/docs/images/warning.svg)
> 
> Whenever you call the `publish` API, we run tests in our server to make sure you won’t save any transformation/libraries code that can lead to any exceptions. In case if your publish is failing, make sure to check your transformation code and the libraries that it is referring to.

**Example response** :
    
    
    {
        "published": true
    }