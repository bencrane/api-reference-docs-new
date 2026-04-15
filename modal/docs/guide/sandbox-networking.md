# Networking and security
Sandboxes are built to be secure-by-default, meaning that a default Sandbox has
no ability to accept incoming network connections or access your Modal resources. 
## Networking
Since Sandboxes may run untrusted code, they have options to restrict their network access.
To block all network access, set `block_network=True` on [Sandbox.create](https://modal.com/docs/reference/modal.Sandbox#create). For more fine-grained networking control, a Sandbox’s outbound network access
can be restricted using the `cidr_allowlist` parameter. This parameter takes a
list of CIDR ranges that the Sandbox is allowed to access, blocking all other
outbound traffic. 
### Connecting to Sandboxes with HTTP and WebSockets
You can make authenticated HTTP and WebSocket requests to a Sandbox by generating
Sandbox Connect Tokens. They work like this: The server running on port 8080 in the container will receive an authenticated
request with an unspoofable `X-Verified-User-Data` header whose value is the
JSON-serialized Python dict that was passed as `user_metadata` to the `create_connect_token()` function. This can be used by the application to
determine access control, for example. There are a few things to remember with Sandbox Connect Tokens: The server inside the container must be listening on port 8080.
- The token may be sent in an `Authorization` header, in a `_modal_connect_token` query param, or in a `_modal_connect_token` cookie.
- If `_modal_connect_token` is set as a query param, the resulting response will
include a `Set-Cookie` header that sets it as a cookie.
- The `user_metadata` must be JSON-serializable and must be less than 512
characters after serialization.

### Forwarding ports

While it is recommended to use [Sandbox Connect Tokens](#connecting-to-sandboxes-with-http-and-websockets) for HTTP requests and WebSocket connections to the container, you can also expose
raw TCP ports to the internet. This is useful if, for example, you want to run a
server inside the Sandbox that expects a raw TCP connection and handles
authentication itself.

Use the `encrypted_ports` and `unencrypted_ports` parameters of `Sandbox.create` to specify which ports to forward. You can then access the public URL of a tunnel
using the [Sandbox.tunnels](https://modal.com/docs/reference/modal.Sandbox#tunnels) method:

It is also possible to create an encrypted port that uses `HTTP/2` rather than `HTTP/1.1` with the `h2_ports` option. This will return
a URL that you can make H2 (HTTP/2 + TLS) requests to. If you want to run an `HTTP/2` server inside a sandbox, this feature may be useful.
Here is an example:

For more details on how tunnels work, see the [tunnels guide](https://modal.com/docs/guide/tunnels).

### Custom domains (Beta)
Custom domains for Sandbox tunnels are available on the [Team and Enterprise plans](https://modal.com/pricing). Visit [workspace settings](https://modal.com/settings/plans) to upgrade. 
Beta This feature is in beta. We’d love to hear your feedback — please reach out via [Slack](https://modal.com/slack) or email us at [support@modal.com](mailto:support@modal.com). Note: the infrastructure is production-grade, but onboarding requires a manual setup step.

By default, Sandbox tunnels are served from subdomains of `w.modal.host`.
In some cases, it’s necessary to have a tunnel served through a custom domain
for security reasons. This is possible with manual setup.

Note that tunnel custom domains are distinct from other custom domains in Modal.
Other custom domains use `CNAME` forwarding. For tunnels, we need to use an `NS` record to delegate the domain to Modal’s nameservers.

1. Delegate a (sub)domain to Modal’s nameservers.**

Add `NS` records to your DNS zone pointing to Modal’s nameservers. For example,
to use `sandbox.example.com`, add the following records in your DNS provider’s
control panel:
NameTypeValue `sandbox.example.com`NS`w-ns-a.modal.host.``sandbox.example.com`NS`w-ns-b.modal.host.``sandbox.example.com`NS`w-ns-c.modal.host.``sandbox.example.com`NS`w-ns-d.modal.host.` 
You can delegate any subdomain depth you like (e.g. `tunnels.a.b.c.example.com`).

**2. Ask Modal to set up the domain.**

Reach out to us on Slack and provide the domain name. We’ll enable it for your
workspace.

**3. Pass `custom_domain` to `Sandbox.create`.**

Modal will provision a TLS certificate automatically. Sandbox Connect Tokens generated
for this sandbox will also use the custom domain.

## Security model

Sandboxes are built on top of [gVisor](https://gvisor.dev/), a container runtime
by Google that provides strong isolation properties. gVisor has custom logic to
prevent Sandboxes from making malicious system calls, giving you stronger isolation
than most other container runtimes.

Additionally, Sandboxes are not authorized to access other resources in your Modal
workspace the way that Modal Functions are [by default](https://modal.com/docs/guide/restricted-access).
As a result, the blast radius of any malicious code will be limited to the Sandbox
container itself.
