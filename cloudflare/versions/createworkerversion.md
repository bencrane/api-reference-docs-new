# Create Version

`POST /accounts/{account_id}/workers/workers/{worker_id}/versions`

Create a new version.

## Parameters

- **account_id** (string, required) [path]: 
- **worker_id** (string, required) [path]: 
- **deploy** (boolean, optional) [query]: 

## Request Body

- **annotations** (object, optional): Metadata about the version.
- **assets** (object, optional): Configuration for assets within a Worker.

[`_headers`](https://developers.cloudflare.com/workers/static-assets/headers/#custom-headers) and
[`_redirects`](https://developers.cloudflare.com/workers/static-assets/redirects/) files should be
included as modules named `_headers` and `_redirects` with content type `text/plain`.

- **bindings** (array, optional): List of bindings attached to a Worker. You can find more about bindings on our docs: https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings.
- **compatibility_date** (string, optional): Date indicating targeted support in the Workers runtime. Backwards incompatible fixes to the runtime following this date will not affect this Worker.
- **compatibility_flags** (array, optional): Flags that enable or disable certain features in the Workers runtime. Used to enable upcoming features or opt in or out of specific changes not included in a `compatibility_date`.
- **created_on** (string, required): When the version was created.
- **id** (string, required): Version identifier.
- **limits** (object, optional): Resource limits enforced at runtime.
- **main_module** (string, optional): The name of the main module in the `modules` array (e.g. the name of the module that exports a `fetch` handler).
- **migrations** (object, optional): Migrations for Durable Objects associated with the version. Migrations are applied when the version is deployed.
- **modules** (array, optional): Code, sourcemaps, and other content used at runtime.

This includes [`_headers`](https://developers.cloudflare.com/workers/static-assets/headers/#custom-headers) and
[`_redirects`](https://developers.cloudflare.com/workers/static-assets/redirects/) files used to configure 
[Static Assets](https://developers.cloudflare.com/workers/static-assets/). `_headers` and `_redirects` files should be 
included as modules named `_headers` and `_redirects` with content type `text/plain`.

- **number** (integer, required): The integer version number, starting from one.
- **placement** (object, optional): Configuration for [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement). Specify mode='smart' for Smart Placement, or one of region/hostname/host.
- **source** (string, optional): The client used to create the version.
- **startup_time_ms** (integer, optional): Time in milliseconds spent on [Worker startup](https://developers.cloudflare.com/workers/platform/limits/#worker-startup-time).
- **urls** (array, required): All routable URLs that always point to this version. Does not include alias URLs, since aliases can be updated to point to a different version.
- **usage_model** (string, optional): Usage model for the version. Values: `standard`, `bundled`, `unbound`

## Response

### 200

Create version success.

- **errors** (array, optional): 
- **messages** (array, optional): 
- **success** (boolean, optional): Whether the API call was successful. Values: `true`
- **result** (object, optional): 

### 4XX

Create version failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
