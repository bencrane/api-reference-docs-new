> Sources:
> - https://trigger.dev/docs/wait
> - https://trigger.dev/docs/wait-for
> - https://trigger.dev/docs/wait-until
> - https://trigger.dev/docs/wait-for-token

# Waits & Waitpoint Tokens

## Wait: Overview

During your run you can wait for a period of time or for something to happen.

Waiting allows you to write complex tasks as a set of async code, without having to schedule another task or poll for changes.

In the Trigger.dev Cloud we automatically pause execution of tasks when they are waiting for
longer than a few seconds.

When triggering and waiting for subtasks, the parent is checkpointed and while waiting does not count towards compute usage. When waiting for a time period (`wait.for` or `wait.until`), if the wait is longer than 5 seconds we checkpoint and it does not count towards compute usage.

| Function                                                              | What it does                                       |
| :-------------------------------------------------------------------- | :------------------------------------------------- |
| [wait.for()](/wait-for)                                               | Waits for a specific period of time, e.g. 1 day.   |
| [wait.until()](/wait-until)                                           | Waits until the provided `Date`.                   |
| [wait.forToken()](/wait-for-token)                                    | Pauses runs until a token is completed.            |
| [inputStream.wait()](/tasks/streams#wait--suspend-until-data-arrives) | Pauses runs until data arrives on an input stream. |

---

## Wait for

Wait for a period of time, then continue execution.

Inside your tasks you can wait for a period of time before you want execution to continue.

```ts /trigger/long-task.ts theme={"theme":"css-variables"}
export const veryLongTask = task({
  id: "very-long-task",
  run: async (payload) => {
    await wait.for({ seconds: 5 });

    await wait.for({ minutes: 10 });

    await wait.for({ hours: 1 });

    await wait.for({ days: 1 });

    await wait.for({ weeks: 1 });

    await wait.for({ months: 1 });

    await wait.for({ years: 1 });
  },
});
```

This allows you to write linear code without having to worry about the complexity of scheduling or managing cron jobs.

In the Trigger.dev Cloud we automatically pause execution of tasks when they are waiting for
longer than a few seconds.

When triggering and waiting for subtasks, the parent is checkpointed and while waiting does not count towards compute usage. When waiting for a time period (`wait.for` or `wait.until`), if the wait is longer than 5 seconds we checkpoint and it does not count towards compute usage.

## Wait idempotency

You can pass an idempotency key to any wait function, allowing you to skip waits if the same idempotency key is used again. This can be useful if you want to skip waits when retrying a task, for example:

```ts theme={"theme":"css-variables"}
// Specify the idempotency key and TTL when waiting for a duration:
await wait.for({ seconds: 10 }, { idempotencyKey: "my-idempotency-key", idempotencyKeyTTL: "1h" });
```

---

## Wait until

Wait until a date, then continue execution.

This example sends a reminder email to a user at the specified datetime.

```ts /trigger/reminder-email.ts theme={"theme":"css-variables"}
export const sendReminderEmail = task({
  id: "send-reminder-email",
  run: async (payload: { to: string; name: string; date: string }) => {
    //wait until the date
    await wait.until({ date: new Date(payload.date) });

    //todo send email
    const { data, error } = await resend.emails.send({
      from: "hello@trigger.dev",
      to: payload.to,
      subject: "Don't forget…",
      html: `<p>Hello ${payload.name},</p><p>...</p>`,
    });
  },
});
```

This allows you to write linear code without having to worry about the complexity of scheduling or managing cron jobs.

In the Trigger.dev Cloud we automatically pause execution of tasks when they are waiting for
longer than a few seconds.

When triggering and waiting for subtasks, the parent is checkpointed and while waiting does not count towards compute usage. When waiting for a time period (`wait.for` or `wait.until`), if the wait is longer than 5 seconds we checkpoint and it does not count towards compute usage.

## `throwIfInThePast`

You can optionally throw an error if the date is already in the past when the function is called:

```ts theme={"theme":"css-variables"}
await wait.until({ date: new Date(date), throwIfInThePast: true });
```

You can of course use try/catch if you want to do something special in this case.

## Wait idempotency

You can pass an idempotency key to any wait function, allowing you to skip waits if the same idempotency key is used again. This can be useful if you want to skip waits when retrying a task, for example:

```ts theme={"theme":"css-variables"}
// Specify the idempotency key and TTL when waiting until a date:
await wait.until({
  date: futureDate,
  idempotencyKey: "my-idempotency-key",
  idempotencyKeyTTL: "1h",
});
```

---

## Wait for token

Wait until a token is completed using waitpoint tokens.

Waitpoint tokens pause task runs until you complete the token. They're commonly used for approval workflows and other scenarios where you need to wait for external confirmation, such as human-in-the-loop processes.

You can complete a token using the SDK or by making a POST request to the token's URL.

<Note>
  If you're waiting for data from an [input stream](/tasks/streams#input-streams), use [`inputStream.wait()`](/tasks/streams#wait--suspend-until-data-arrives) instead — it uses waitpoint tokens internally but provides a simpler API with full type safety from your stream definition.
</Note>

## Usage

To get started using wait tokens, you need to first create a token using the `wait.createToken` function:

```ts theme={"theme":"css-variables"}
import { wait } from "@trigger.dev/sdk";

// This can be called anywhere in your codebase, either in a task or in your backend code
const token = await wait.createToken({
  timeout: "10m", // you can optionally specify a timeout for the token
});
```

Once you have a token, you can wait for it to be completed using the `wait.forToken` function:

```ts theme={"theme":"css-variables"}
import { wait } from "@trigger.dev/sdk";

type ApprovalToken = {
  status: "approved" | "rejected";
};

// This must be called inside a task run function
const result = await wait.forToken<ApprovalToken>(tokenId);

if (result.ok) {
  console.log("Token completed", result.output.status); // "approved" or "rejected"
} else {
  console.log("Token timed out", result.error);
}
```

To complete a token, you can use the `wait.completeToken` function:

```ts theme={"theme":"css-variables"}
import { wait } from "@trigger.dev/sdk";
// This can be called anywhere in your codebase, or from an external service,
// passing in the token ID and the output of the token
await wait.completeToken<ApprovalToken>(tokenId, {
  status: "approved",
});
```

Or you can make an HTTP POST request to the `url` it returns. This is an HTTP callback:

```ts theme={"theme":"css-variables"}
import { wait } from "@trigger.dev/sdk";

const token = await wait.createToken({
  timeout: "10m",
});

const call = await replicate.predictions.create({
  version: "27b93a2413e7f36cd83da926f3656280b2931564ff050bf9575f1fdf9bcd7478",
  input: {
    prompt: "A painting of a cat by Andy Warhol",
  },
  // pass the provided URL to Replicate's webhook, so they can "callback"
  webhook: token.url,
  webhook_events_filter: ["completed"],
});

const prediction = await wait.forToken<Prediction>(token).unwrap();
// unwrap() throws a timeout error or returns the result   👆
```

## wait.createToken

Create a waitpoint token.

### options

The `createToken` function accepts an object with the following properties:

<ParamField type="string">
  The maximum amount of time to wait for the token to be completed. Defaults to "10m".
</ParamField>

<ParamField type="string">
  An idempotency key for the token. If provided, the token will be completed with the same payload
  if the same idempotency key is used again.
</ParamField>

<ParamField type="string">
  The time to live for the idempotency key. Defaults to "1h".
</ParamField>

<ParamField type="string[]">
  Tags to attach to the token. Tags can be used to filter waitpoints in the dashboard.
</ParamField>

### returns

The `createToken` function returns a token object with the following properties:

<ParamField type="string">
  The ID of the token. Starts with `waitpoint_`.
</ParamField>

<ParamField type="string">
  The URL of the token. This is the URL you can make a POST request to in order to complete the token.

  The JSON body of the POST request will be used as the output of the token. If there's no body the output will be an empty object `{}`.
</ParamField>

<ParamField type="boolean">
  Whether the token is cached. Will return true if the token was created with an idempotency key and
  the same idempotency key was used again.
</ParamField>

<ParamField type="string">
  A Public Access Token that can be used to complete the token from a client-side application (or
  another backend). See our [Realtime docs](/realtime/auth) for more details.
</ParamField>

### Example

```ts theme={"theme":"css-variables"}
import { wait } from "@trigger.dev/sdk";

const token = await wait.createToken({
  timeout: "10m",
  idempotencyKey: "my-idempotency-key",
  tags: ["my-tag"],
});
```

## wait.completeToken

Complete a waitpoint token.

### parameters

<ParamField type="string">
  The ID of the token to complete.
</ParamField>

<ParamField type="any">
  The data to complete the token with.
</ParamField>

### returns

The `completeToken` function returns an object with the following properties:

<ParamField type="boolean">
  Whether the token was completed successfully.
</ParamField>

### Example

```ts theme={"theme":"css-variables"}
import { wait } from "@trigger.dev/sdk";

await wait.completeToken<ApprovalToken>(tokenId, {
  status: "approved",
});
```

### From another language

You can complete a token using a raw HTTP request or from another language.

<CodeGroup>
  ```bash curl theme={"theme":"css-variables"}
  curl -X POST "https://api.trigger.dev/api/v1/waitpoints/tokens/{tokenId}/complete" \
    -H "Authorization: Bearer {token}" \
    -H "Content-Type: application/json" \
    -d '{"data": { "status": "approved"}}'
  ```

  ```python python theme={"theme":"css-variables"}
  import requests

  response = requests.post(
    "https://api.trigger.dev/api/v1/waitpoints/tokens/{tokenId}/complete",
    headers={"Authorization": f"Bearer {token}"},
    json={"data": { "status": "approved"}}
  )
  ```

  ```ruby ruby theme={"theme":"css-variables"}
  require "net/http"

  uri = URI("https://api.trigger.dev/api/v1/waitpoints/tokens/{tokenId}/complete")

  http = Net::HTTP.new(uri.host, uri.port)
  request = Net::HTTP::Post.new(uri)
  request["Authorization"] = "Bearer {token}"
  request["Content-Type"] = "application/json"
  request.body = JSON.generate({ data: { status: "approved" } })

  response = http.request(request)
  ```

  ```go go theme={"theme":"css-variables"}
  package main

  import (
  	"bytes"
  	"encoding/json"
  	"fmt"
  	"net/http"
  )

  func main() {
  	url := "https://api.trigger.dev/api/v1/waitpoints/tokens/{tokenId}/complete"

  	payload := map[string]interface{}{
  		"data": map[string]interface{}{
  			"status": "approved",
  		},
  	}

  	jsonData, err := json.Marshal(payload)
  	if err != nil {
  		fmt.Println("Error marshalling payload:", err)
  		return
  	}

  	req, err := http.NewRequest("POST", url, bytes.NewBuffer(jsonData))
  	if err != nil {
  		fmt.Println("Error creating request:", err)
  		return
  	}

  	req.Header.Set("Authorization", "Bearer {token}")
  	req.Header.Set("Content-Type", "application/json")

  	client := &http.Client{}
  	resp, err := client.Do(req)
  	if err != nil {
  		fmt.Println("Error sending request:", err)
  		return
  	}

  	defer resp.Body.Close()

  	fmt.Println("Response status:", resp.Status)
  }
  ```
</CodeGroup>

## wait.forToken

Wait for a token to be completed.

### parameters

<ParamField type="string | { id: string }">
  The token to wait for.
</ParamField>

### returns

The `forToken` function returns a result object with the following properties:

<ParamField type="boolean">
  Whether the token was completed successfully.
</ParamField>

<ParamField type="any">
  If `ok` is `true`, this will be the output of the token.
</ParamField>

<ParamField type="Error">
  If `ok` is `false`, this will be the error that occurred. The only error that can occur is a
  timeout error.
</ParamField>

### unwrap()

We provide a handy `.unwrap()` method that will throw an error if the result is not ok. This means your happy path is a lot cleaner.

```ts theme={"theme":"css-variables"}
const approval = await wait.forToken<ApprovalToken>(tokenId).unwrap();
// unwrap means an error will throw if the waitpoint times out 👆

// This is the actual data you sent to the token now, not a result object
console.log("Approval", approval);
```

### Example

```ts theme={"theme":"css-variables"}
import { wait } from "@trigger.dev/sdk";

const result = await wait.forToken<ApprovalToken>(tokenId);

if (result.ok) {
  console.log("Token completed", result.output.status); // "approved" or "rejected"
} else {
  console.log("Token timed out", result.error);
}
```

## wait.listTokens

List all tokens for an environment.

### parameters

The `listTokens` function accepts an object with the following properties:

<ParamField type="string | string[]">
  Statuses to filter by. Can be one or more of: `WAITING`, `COMPLETED`, `TIMED_OUT`.
</ParamField>

<ParamField type="string">
  The idempotency key to filter by.
</ParamField>

<ParamField type="string | string[]">
  Tags to filter by.
</ParamField>

<ParamField type="string">
  The period to filter by. Can be one of: `1h`, `1d`, `7d`, `30d`.
</ParamField>

<ParamField type="Date | number">
  The start date to filter by.
</ParamField>

<ParamField type="Date | number">
  The end date to filter by.
</ParamField>

### returns

The `listTokens` function returns a list of tokens that can be iterated over using a for-await-of loop.

Each token is an object with the following properties:

<ParamField type="string">
  The ID of the token.
</ParamField>

<ParamField type="string">
  The URL of the token. This is the URL you can make a POST request to in order to complete the token.

  The JSON body of the POST request will be used as the output of the token. If there's no body the output will be an empty object `{}`.
</ParamField>

<ParamField type="string">
  The status of the token.
</ParamField>

<ParamField type="Date">
  The date and time the token was completed.
</ParamField>

<ParamField type="Date">
  The date and time the token will timeout.
</ParamField>

<ParamField type="string">
  The idempotency key of the token.
</ParamField>

<ParamField type="Date">
  The date and time the idempotency key will expire.
</ParamField>

<ParamField type="string[]">
  The tags of the token.
</ParamField>

<ParamField type="Date">
  The date and time the token was created.
</ParamField>

<Note>
  The output of the token is not included in the list. To get the output, you need to retrieve the
  token using the `wait.retrieveToken` function.
</Note>

### Example

```ts theme={"theme":"css-variables"}
import { wait } from "@trigger.dev/sdk";

const tokens = await wait.listTokens({
  status: "COMPLETED",
  tags: ["user:123"],
});

for await (const token of tokens) {
  console.log(token);
}
```

## wait.retrieveToken

Retrieve a token by ID.

### parameters

<ParamField type="string">
  The ID of the token to retrieve.
</ParamField>

### returns

The `retrieveToken` function returns a token object with the following properties:

<ParamField type="string">
  The ID of the token.
</ParamField>

<ParamField type="string">
  The URL of the token. This is the URL you can make a POST request to in order to complete the token.

  The JSON body of the POST request will be used as the output of the token. If there's no body the output will be an empty object `{}`.
</ParamField>

<ParamField type="string">
  The status of the token.
</ParamField>

<ParamField type="Date">
  The date and time the token was completed.
</ParamField>

<ParamField type="Date">
  The date and time the token will timeout.
</ParamField>

<ParamField type="string">
  The idempotency key of the token.
</ParamField>

<ParamField type="Date">
  The date and time the idempotency key will expire.
</ParamField>

<ParamField type="string[]">
  The tags of the token.
</ParamField>

<ParamField type="Date">
  The date and time the token was created.
</ParamField>

<ParamField type="any">
  The output of the token.
</ParamField>

<ParamField type="Error">
  The error that occurred.
</ParamField>

### Example

```ts theme={"theme":"css-variables"}
import { wait } from "@trigger.dev/sdk";

const token = await wait.retrieveToken(tokenId);

console.log(token);
```

## Wait idempotency

You can pass an idempotency key to any wait function, allowing you to skip waits if the same idempotency key is used again. This can be useful if you want to skip waits when retrying a task, for example:

```ts theme={"theme":"css-variables"}
// Specify the idempotency key and TTL when creating a wait token
const token = await wait.createToken({
  idempotencyKey: "my-idempotency-key",
  idempotencyKeyTTL: "1h",
});
```

---
