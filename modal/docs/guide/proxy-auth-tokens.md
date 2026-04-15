# Proxy Auth Tokens

Use Proxy Auth Tokens to prevent unauthorized clients from triggering your web endpoints.

import modal

image = modal.Image.debian_slim().pip_install("fastapi")
app = modal.App("proxy-auth-public", image=image)

@app.function()
@modal.fastapi_endpoint()
def public():
    return "hello world"

@app.function()
@modal.fastapi_endpoint(requires_proxy_auth=True)
def private():
    return "hello friend"

The public endpoint can be hit by any client over the Internet.

curl https://public-url--goes-here.modal.run

The private endpoint cannot.

curl --fail-with-body https://private-url--goes-here.modal.run
# modal-http: missing credentials for proxy authorization
# curl: (22) The requested URL returned error: 401
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401

Authorization is demonstrated via a Proxy Auth Token. You can create a Proxy Auth Token for your workspace here. In requests to the web endpoint, clients supply the Token ID and Token Secret in the Modal-Key and Modal-Secret HTTP headers.

export TOKEN_ID=wk-1234abcd
export TOKEN_SECRET=ws-1234abcd
curl -H "Modal-Key: $TOKEN_ID" \
     -H "Modal-Secret: $TOKEN_SECRET" \
     https://private-url--goes-here.modal.run

Proxy authorization can be added to web endpoints created by the fastapi_endpoint, asgi_app, wsgi_app, or web_server decorators, which are otherwise publicly available.

Everyone within the workspace of the web endpoint can manage its Proxy Auth Tokens.

Restricting tokens to specific Environments 

On workspaces with RBAC enabled, tokens can be scoped to specific Environments, restricting which web endpoints they are valid for. See Proxy auth tokens for web endpoints in the RBAC guide for more.
