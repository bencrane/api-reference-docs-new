# Call Ended Reasons Documentation

## Overview

Every call in Vapi terminates with an `endedReason` code explaining its conclusion. Users can access this information through the call logs dashboard or via the Call object in the API reference.

## Quick Diagnosis Table

The documentation provides a rapid troubleshooting matrix organized by caller experience:

- **Phone never rang**: Look for `call.start.error-*` codes, typically stemming from account issues or configuration problems
- **Phone rang but no answer**: Expected behavior indicated by `customer-did-not-answer` or `customer-busy`
- **Mid-conversation drops**: Usually signal transient network issues, marked by `*-worker-died` or similar infrastructure errors
- **Assistant silence**: Suggests provider outages or credential problems; the docs recommend configuring fallback providers
- **Normal termination**: Expected reasons like `assistant-ended-call` or `silence-timed-out`
- **Transfer failures**: Typically caused by bad destination configurations or SIP issues

## Error Prefix Classifications

The documentation categorizes errors by responsible party:

**Vapi Faults** (`call.in-progress.error-vapifault-*`): Platform infrastructure failures—users typically aren't charged

**Provider Faults** (`call.in-progress.error-providerfault-*`): Third-party service failures outside Vapi's control

**Pipeline Errors** (`pipeline-error-*`): Often indicate credential or quota issues when using custom provider keys

## Major Error Categories

### Call Start Errors

These occur before connection during resource setup, including:
- Subscription issues (frozen accounts, insufficient credits)
- Resource resolution failures (missing assistants, phone numbers)
- Phone number limits (international calling restrictions, daily limits)

### Assistant & Customer Actions

The documentation distinguishes intentional call endings from failures:
- Assistants can end calls via tools, functions, or configured phrases
- Customers can end calls, deny permissions, or disconnect during transfers

### Provider-Specific Failures

Detailed error patterns exist for:
- **LLM providers**: Status codes indicate validation, authorization, quota, or server issues
- **Voice/TTS providers**: Voice not found, quota exceeded, credential problems
- **Transcriber/STT providers**: Bad requests, invalid credentials, or provider outages

### Transport & Connectivity

Errors specific to call providers:
- **Twilio**: Connection failures, invalid numbers
- **Vonage**: Disconnection, rejection
- **SIP**: Protocol-specific errors including 403, 407, 408, 480, and 503 responses

## Additional Resources

The page directs users to supplementary documentation for troubleshooting workflows, debugging tools, and issue reporting procedures with required information like call IDs.
