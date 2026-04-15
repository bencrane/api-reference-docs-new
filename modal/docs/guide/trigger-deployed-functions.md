# Invoking deployed functions
Modal lets you take a function created by a [deployment](https://modal.com/docs/guide/managing-deployments) and call it from other contexts. There are two ways of invoking deployed functions. If the invoking client is
running Python, then the same [Modal client library](https://pypi.org/project/modal/) used to write Modal code
can be used. HTTPS is used if the invoking client is not running Python and
therefore cannot import the Modal client library. 
## Invoking with Python
Some use cases for Python invocation include: An existing Python web server (eg. Django, Flask) wants to invoke Modal
functions.
- You have split your product or system into multiple Modal applications that
deploy independently and call each other.

### Function lookup and invocation basics

Let’s say you have a script `my_shared_app.py` and this script defines a Modal
app with a function that computes the square of a number:

You can deploy this app to create a persistent deployment:

Let’s try to run this function from a different context. For instance, let’s
fire up the Python interactive interpreter:

This works exactly the same as a regular modal `Function` object. For example,
you can `.map()` over functions invoked this way too:

#### Authentication

The Modal Python SDK will read the token from `~/.modal.toml` which typically is
created using `modal token new`.

Another method of providing the credentials is to set the environment variables `MODAL_TOKEN_ID` and `MODAL_TOKEN_SECRET`. If you want to call a Modal function
from a context such as a web server, you can expose these environment variables
to the process.

#### Lookup of lifecycle functions

[Lifecycle functions](https://modal.com/docs/guide/lifecycle-functions) are defined on classes,
which you can look up in a different way. Consider this code:

Let’s say you deploy this app. You can then call the function by doing this:

### Asynchronous invocation

In certain contexts, a Modal client will need to trigger Modal functions without
waiting on the result. This is done by spawning functions and receiving a [FunctionCall](https://modal.com/docs/reference/modal.FunctionCall) as a
handle to the triggered execution.

The following is an example of a Flask web server (running outside Modal) which
accepts model training jobs to be executed within Modal. Instead of the HTTP
POST request waiting on a training job to complete, which would be infeasible,
the relevant Modal function is spawned and the [FunctionCall](https://modal.com/docs/reference/modal.FunctionCall) object is stored for later polling of execution status.

### Importing a Modal function between Modal apps

You can also import one function defined in an app from another app:

### Comparison with HTTPS

Compared with HTTPS invocation, Python invocation has the following benefits:
- Avoids the need to create web endpoint functions.
- Avoids handling serialization of request and response data between Modal and
your client.
- Uses the Modal client library’s built-in authentication. Web endpoints are public to the entire internet, whereas function `lookup` only exposes your code to you (and your org).
- You can work with shared Modal functions as if they are normal Python
functions, which might be more convenient.

## Invoking with HTTPS

Any application that can make HTTPS requests can interact with deployed Modal
applications via [web endpoint functions](https://modal.com/docs/guide/webhooks). Note that
all deployed web endpoint functions have [a stable HTTPS
URL](https://modal.com/docs/guide/webhook-urls).

Some use cases for HTTPS invocation include:
- Calling Modal functions from a web browser client running JavaScript
- Calling Modal functions from backend services in languages we don’t yet have
official SDKs for (Java, Ruby, etc.)
- Calling Modal functions using UNIX tools (`curl`, `wget`)

However, if the client of your Modal deployment is running Python, JavaScript,
or Go, it’s better to use the [Modal Python
SDK](https://pypi.org/project/modal/) or [libmodal SDKs for JavaScript and
Go](https://modal.com/docs/guide/sdk-javascript-go) to invoke your Modal code.

For more detail on setting up functions for invocation over HTTP see the [web endpoints guide](https://modal.com/docs/guide/webhooks).
