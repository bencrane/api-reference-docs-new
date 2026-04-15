# modal.fastapi_endpoint

Source: https://modal.com/docs/reference/modal.fastapi_endpoint

---

```python
modal.fastapi_endpoint
def fastapi_endpoint(
    *,
    method: str = "GET",  # REST method for the created endpoint.
    label: Optional[str] = None,  # Label for created endpoint. Final subdomain will be <workspace>--<label>.modal.run.
    custom_domains: Optional[Iterable[str]] = None,  # Custom fully-qualified domain name (FQDN) for the endpoint.
    docs: bool = False,  # Whether to enable interactive documentation for this endpoint at /docs.
    requires_proxy_auth: bool = False,  # Require Modal-Key and Modal-Secret HTTP Headers on requests.
) -> Callable[
    [Union[_PartialFunction[P, ReturnType, ReturnType], Callable[P, ReturnType]]],
    _PartialFunction[P, ReturnType, ReturnType],
]:
```

Convert a function into a basic web endpoint by wrapping it with a FastAPI App.

Modal will internally use FastAPI to expose a simple, single request handler. If you are defining your own FastAPI application (e.g. if you want to define multiple routes), use @modal.asgi_app instead.

The endpoint created with this decorator will automatically have CORS enabled and can leverage many of FastAPI’s features.

For more information on using Modal with popular web frameworks, see our guide on web endpoints.

Added in v0.73.82: This function replaces the deprecated @web_endpoint decorator.
