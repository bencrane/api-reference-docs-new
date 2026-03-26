# Event Retry Mechanism in Mobile SDKs

Learn about the event retry mechanism feature available in the Android (Kotlin) and iOS (Swift) SDKs.

* * *

  * __2 minute read

  * 


This guide explains the event retry mechanism supported by the Android (Kotlin) and iOS (Swift) SDKs. It explains how the retry system works, when it retries failed uploads, and how it handles different types of errors.

## Overview

The RudderStack [Android (Kotlin)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/kotlin-sdk/>) and [iOS (Swift)](<https://www.rudderstack.com/docs/sources/event-streams/sdks/swift-sdk/>) SDKs implement a robust retry mechanism to ensure reliable event delivery to the data plane.

The retry mechanism is built around two main components:

  * **Event upload system** : Handles the actual upload of event batches to the RudderStack data plane
  * **Backoff policy** : Manages retry timing and delays to avoid overwhelming the server


## How retry works

The SDKs group events into batches and store them as files. Each batch is a JSON string containing a collection of events, and is processed and sent to the server.

The server response is categorized as **Success** , **Retryable error** , and **Non-retryable error**.

Based on the above responses, the SDKs respond as follows:

### Success

Represents a success response from the server for a batch upload. The batch file is then deleted and the retry counter is reset in this case.

### Retryable errors

Represents a temporary failure like network issues, server unavailable, etc. In this case, the SDK retries requests using an **exponential backoff strategy with jitter**.

Each request is retried for up to five times. After exhausting these attempts, the SDK enters a **30-minute cool-off period** , after which it retries the requests with the same retry strategy. This cycle repeats until the request succeeds or results in a non-retryable error.

### Non-retryable errors

Represents a permanent failure which cannot be retried. In this case, the retry counter is reset and errors are handled immediately, as mentioned in the below table:

Error| Description| Action  
---|---|---  
Bad request/payload too large| The JSON batch payload is malformed or the payload size is too large.| The current batch file is deleted and the upload continues with the next batch.  
Invalid write key| The write key used to initialize the SDK is invalid.| The SDK is [shut down](<https://www.rudderstack.com/docs/sources/event-streams/sdks/mobile-sdk-apis/shutdown/>), upload is canceled, and all the persistent SDK storage is cleared (including stored batches)  
Source disabled| Source is disabled in the RudderStack dashboard.| Upload is cancelled in this case and no new events are accepted.