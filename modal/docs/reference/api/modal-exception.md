# modal.exception

Source: https://modal.com/docs/reference/modal.exception

---

```python
modal.exception

```

Modal-specific exception types.

Notes on grpclib.GRPCError migration

Historically, the Modal SDK could propagate grpclib.GRPCError exceptions out to user code. As of v1.3, we are in the process of gracefully migrating to always raising a Modal exception type in these cases. To avoid breaking user code that relies on catching grpclib.GRPCError, a subset of Modal exception types temporarily inherit from grpclib.GRPCError.

We encourage users to migrate any code that currently catches grpclib.GRPCError to instead catch the appropriate Modal exception type. The following mapping between GRPCError status codes and Modal exception types is currently in use:

CANCELLED -> ServiceError
UNKNOWN -> ServiceError
INVALID_ARGUMENT -> InvalidError
DEADLINE_EXCEEDED -> ServiceError
NOT_FOUND -> NotFoundError
ALREADY_EXISTS -> AlreadyExistsError
PERMISSION_DENIED -> PermissionDeniedError
RESOURCE_EXHAUSTED -> ResourceExhaustedError
FAILED_PRECONDITION -> ConflictError
ABORTED -> ConflictError
OUT_OF_RANGE -> InvalidError
UNIMPLEMENTED -> UnimplementedError
INTERNAL -> InternalError
UNAVAILABLE -> ServiceError
DATA_LOSS -> DataLossError
UNAUTHENTICATED -> AuthError
```python
modal.exception.AlreadyExistsError 
class AlreadyExistsError(modal.exception.Error, modal.exception._GRPCErrorWrapper)
```

Raised when a resource creation conflicts with an existing resource.

```python
def __init__(self, message: Optional[str] = None):
    # Override GRPCError's init and repr to behave more like a regular Exception
    # (We don't customize these anywhere in our custom error types currently).
```

message
@property
```python
def message(self) -> str:
```

status
@property
```python
def status(self) -> grpclib.Status:
```

details
@property
```python
def details(self) -> Any:
```

```python
modal.exception.AsyncUsageWarning 
class AsyncUsageWarning(UserWarning)
```

Warning emitted when a blocking Modal interface is used in an async context.

```python
modal.exception.AuthError 
class AuthError(modal.exception.Error, modal.exception._GRPCErrorWrapper)
```

Raised when a client has missing or invalid authentication.

```python
def __init__(self, message: Optional[str] = None):
    # Override GRPCError's init and repr to behave more like a regular Exception
    # (We don't customize these anywhere in our custom error types currently).
```

message
@property
```python
def message(self) -> str:
```

status
@property
```python
def status(self) -> grpclib.Status:
```

details
@property
```python
def details(self) -> Any:
```

```python
modal.exception.ClientClosed 
class ClientClosed(modal.exception.Error)
```

```python
modal.exception.ConflictError 
class ConflictError(modal.exception.InvalidError, modal.exception._GRPCErrorWrapper)
```

Raised when a resource conflict occurs between the request and current system state.

```python
def __init__(self, message: Optional[str] = None):
    # Override GRPCError's init and repr to behave more like a regular Exception
    # (We don't customize these anywhere in our custom error types currently).
```

message
@property
```python
def message(self) -> str:
```

status
@property
```python
def status(self) -> grpclib.Status:
```

details
@property
```python
def details(self) -> Any:
```

```python
modal.exception.ConnectionError 
class ConnectionError(modal.exception.Error)
```

Raised when an issue occurs while connecting to the Modal servers.

```python
modal.exception.DataLossError 
class DataLossError(modal.exception.Error, modal.exception._GRPCErrorWrapper)
```

Raised when data is lost or corrupted.

```python
def __init__(self, message: Optional[str] = None):
    # Override GRPCError's init and repr to behave more like a regular Exception
    # (We don't customize these anywhere in our custom error types currently).
```

message
@property
```python
def message(self) -> str:
```

status
@property
```python
def status(self) -> grpclib.Status:
```

details
@property
```python
def details(self) -> Any:
```

```python
modal.exception.DeprecationError 
class DeprecationError(UserWarning)
```

UserWarning category emitted when a deprecated Modal feature or API is used.

```python
modal.exception.DeserializationError 
class DeserializationError(modal.exception.Error)
```

Raised to provide more context when an error is encountered during deserialization.

```python
modal.exception.ExecTimeoutError 
class ExecTimeoutError(modal.exception.TimeoutError)
```

Raised when a container process exceeds its execution duration limit and times out.

```python
modal.exception.ExecutionError 
class ExecutionError(modal.exception.Error)
```

Raised when something unexpected happened during runtime.

```python
modal.exception.FilesystemExecutionError 
class FilesystemExecutionError(modal.exception.Error)
```

Raised when an unknown error is thrown during a container filesystem operation.

```python
modal.exception.FunctionTimeoutError 
class FunctionTimeoutError(modal.exception.TimeoutError)
```

Raised when a Function exceeds its execution duration limit and times out.

```python
modal.exception.InputCancellation 
class InputCancellation(BaseException)
```

Raised when the current input is cancelled by the task

Intentionally a BaseException instead of an Exception, so it won’t get caught by unspecified user exception clauses that might be used for retries and other control flow.

```python
modal.exception.InteractiveTimeoutError 
class InteractiveTimeoutError(modal.exception.TimeoutError)
```

Raised when interactive frontends time out while trying to connect to a container.

```python
modal.exception.InternalError 
class InternalError(modal.exception.Error, modal.exception._GRPCErrorWrapper)
```

Raised when an internal error occurs in the Modal system.

```python
def __init__(self, message: Optional[str] = None):
    # Override GRPCError's init and repr to behave more like a regular Exception
    # (We don't customize these anywhere in our custom error types currently).
```

message
@property
```python
def message(self) -> str:
```

status
@property
```python
def status(self) -> grpclib.Status:
```

details
@property
```python
def details(self) -> Any:
```

```python
modal.exception.InternalFailure 
class InternalFailure(modal.exception.Error)
```

Retriable internal error.

```python
modal.exception.InvalidError 
class InvalidError(modal.exception.Error, modal.exception._GRPCErrorWrapper)
```

Raised when user does something invalid.

```python
def __init__(self, message: Optional[str] = None):
    # Override GRPCError's init and repr to behave more like a regular Exception
    # (We don't customize these anywhere in our custom error types currently).
```

message
@property
```python
def message(self) -> str:
```

status
@property
```python
def status(self) -> grpclib.Status:
```

details
@property
```python
def details(self) -> Any:
```

```python
modal.exception.LogsFetchError 
class LogsFetchError(modal.exception.Error)
```

Raised when trying to fetch too many logs.

```python
modal.exception.ModuleNotMountable 
class ModuleNotMountable(Exception)
```

```python
modal.exception.MountUploadTimeoutError 
class MountUploadTimeoutError(modal.exception.TimeoutError)
```

Raised when a Mount upload times out.

```python
modal.exception.NotFoundError 
class NotFoundError(modal.exception.Error, modal.exception._GRPCErrorWrapper)
```

Raised when a requested resource was not found.

```python
def __init__(self, message: Optional[str] = None):
    # Override GRPCError's init and repr to behave more like a regular Exception
    # (We don't customize these anywhere in our custom error types currently).
```

message
@property
```python
def message(self) -> str:
```

status
@property
```python
def status(self) -> grpclib.Status:
```

details
@property
```python
def details(self) -> Any:
```

```python
modal.exception.OutputExpiredError 
class OutputExpiredError(modal.exception.TimeoutError)
```

Raised when the Output exceeds expiration and times out.

```python
modal.exception.PendingDeprecationError 
class PendingDeprecationError(UserWarning)
```

Soon to be deprecated feature. Only used intermittently because of multi-repo concerns.

```python
modal.exception.PermissionDeniedError 
class PermissionDeniedError(modal.exception.Error, modal.exception._GRPCErrorWrapper)
```

Raised when a user does not have permission to perform the requested operation.

```python
def __init__(self, message: Optional[str] = None):
    # Override GRPCError's init and repr to behave more like a regular Exception
    # (We don't customize these anywhere in our custom error types currently).
```

message
@property
```python
def message(self) -> str:
```

status
@property
```python
def status(self) -> grpclib.Status:
```

details
@property
```python
def details(self) -> Any:
```

```python
modal.exception.RemoteError 
class RemoteError(modal.exception.Error)
```

Raised when an error occurs on the Modal server.

```python
modal.exception.RequestSizeError 
class RequestSizeError(modal.exception.Error)
```

Raised when an operation produces a gRPC request that is rejected by the server for being too large.

```python
modal.exception.ResourceExhaustedError 
class ResourceExhaustedError(modal.exception.Error, modal.exception._GRPCErrorWrapper)
```

Raised when a server-side resource has been exhausted, e.g. a quota or rate limit.

```python
def __init__(self, message: Optional[str] = None):
    # Override GRPCError's init and repr to behave more like a regular Exception
    # (We don't customize these anywhere in our custom error types currently).
```

message
@property
```python
def message(self) -> str:
```

status
@property
```python
def status(self) -> grpclib.Status:
```

details
@property
```python
def details(self) -> Any:
```

```python
modal.exception.SandboxFilesystemError 
class SandboxFilesystemError(modal.exception.Error)
```

Base class for sandbox filesystem errors.

```python
modal.exception.SandboxFilesystemFileTooLargeError 
class SandboxFilesystemFileTooLargeError(modal.exception.SandboxFilesystemError)
```

Raised when a file exceeds the maximum allowed size for a read operation in the sandbox.

```python
modal.exception.SandboxFilesystemIsADirectoryError 
class SandboxFilesystemIsADirectoryError(modal.exception.SandboxFilesystemError)
```

Raised when a file operation in the sandbox targets a directory when it should target a non-directory file.

```python
modal.exception.SandboxFilesystemNotADirectoryError 
class SandboxFilesystemNotADirectoryError(modal.exception.SandboxFilesystemError)
```

Raised when a path component in the sandbox is not a directory.

```python
modal.exception.SandboxFilesystemNotFoundError 
class SandboxFilesystemNotFoundError(modal.exception.SandboxFilesystemError)
```

Raised when a file or directory is not found in the sandbox.

```python
modal.exception.SandboxFilesystemPermissionError 
class SandboxFilesystemPermissionError(modal.exception.SandboxFilesystemError)
```

Raised when permission is denied for a file operation in the sandbox.

```python
modal.exception.SandboxTerminatedError 
class SandboxTerminatedError(modal.exception.Error)
```

Raised when a Sandbox is terminated for an internal reason.

```python
modal.exception.SandboxTimeoutError 
class SandboxTimeoutError(modal.exception.TimeoutError)
```

Raised when a Sandbox exceeds its execution duration limit and times out.

```python
modal.exception.SerializationError 
class SerializationError(modal.exception.Error)
```

Raised to provide more context when an error is encountered during serialization.

```python
modal.exception.ServerWarning 
class ServerWarning(UserWarning)
```

Warning originating from the Modal server and re-issued in client code.

```python
modal.exception.ServiceError 
class ServiceError(modal.exception.Error, modal.exception._GRPCErrorWrapper)
```

Raised when an error occurs in basic client/server communication.

```python
def __init__(self, message: Optional[str] = None):
    # Override GRPCError's init and repr to behave more like a regular Exception
    # (We don't customize these anywhere in our custom error types currently).
```

message
@property
```python
def message(self) -> str:
```

status
@property
```python
def status(self) -> grpclib.Status:
```

details
@property
```python
def details(self) -> Any:
```

```python
modal.exception.TimeoutError 
class TimeoutError(modal.exception.Error)
```

Base class for Modal timeouts.

```python
modal.exception.UnimplementedError 
class UnimplementedError(modal.exception.Error, modal.exception._GRPCErrorWrapper)
```

Raised when a requested operation is not implemented or not supported.

```python
def __init__(self, message: Optional[str] = None):
    # Override GRPCError's init and repr to behave more like a regular Exception
    # (We don't customize these anywhere in our custom error types currently).
```

message
@property
```python
def message(self) -> str:
```

status
@property
```python
def status(self) -> grpclib.Status:
```

details
@property
```python
def details(self) -> Any:
```

```python
modal.exception.VersionError 
class VersionError(modal.exception.Error)
```

Raised when the current client version of Modal is unsupported.

```python
modal.exception.VolumeUploadTimeoutError 
class VolumeUploadTimeoutError(modal.exception.TimeoutError)
```

Raised when a Volume upload times out.

```python
modal.exception.simulate_preemption 
def simulate_preemption(wait_seconds: int, jitter_seconds: int = 0):
```

Utility for simulating a preemption interrupt after wait_seconds seconds. The first interrupt is the SIGINT signal. After 30 seconds, a second interrupt will trigger.

This second interrupt simulates SIGKILL, and should not be caught. Optionally add between zero and jitter_seconds seconds of additional waiting before first interrupt.

Usage:

```python
import time
from modal.exception import simulate_preemption

```

simulate_preemption(3)

try:
```python
    time.sleep(4)
```

except KeyboardInterrupt:
```python
    print("got preempted") # Handle interrupt
    raise
```

See https://modal.com/docs/guide/preemption for more details on preemption handling.
