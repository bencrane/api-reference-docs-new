# TRIGGER_DEV_WAITS_TOKENS

Wait primitives, token workflows, and input stream interaction model.

---

## Duration-based Waits: `wait.for()`

```ts
import { task, wait } from "@trigger.dev/sdk";

export const retryLater = task({
  id: "retry-later",
  run: async () => {
    await wait.for({ minutes: 30 });
    return { resumed: true };
  },
});
```

| Property | Type | Required | Default | Description |
|---|---|---:|---|---|
| `seconds` | `number` | One of | `0` | Delay duration |
| `minutes` | `number` | One of | `0` | Delay duration |
| `hours` | `number` | One of | `0` | Delay duration |
| `days` | `number` | One of | `0` | Delay duration |

---

## Date-based Waits: `wait.until()`

```ts
await wait.until({ date: new Date("2026-04-01T00:00:00Z") });
```

| Property | Type | Required | Default | Description |
|---|---|---:|---|---|
| `date` | `Date` | Yes | - | Resume time |

---

## Wait Tokens

### Create token

```ts
import { wait } from "@trigger.dev/sdk";

const token = await wait.createToken({
  idempotencyKey: "approval:order_123",
  idempotencyKeyTTL: "24h",
  timeout: "7d",
  tags: ["workflow:order-approval", "tenant:acme"],
});
```

| Property | Type | Required | Default | Description |
|---|---|---:|---|---|
| `idempotencyKey` | `string` | No | none | Reuse existing token before expiry |
| `idempotencyKeyTTL` | duration string | No | platform default | Idempotency window |
| `timeout` | ISO datetime or duration | No | docs vary | Auto-timeout for waiting run |
| `tags` | `string \| string[]` | No | none | Token classification |

Response highlights: `id`, `url`, `isCached`.

### Wait for token inside task

```ts
const result = await wait.forToken<{ approved: boolean }>(token.id);
if (!result.ok) return { approved: false, reason: "timeout" };
return { approved: result.output.approved };
```

### Complete token (SDK/API)

```ts
await wait.completeToken(token.id, { approved: true, reviewer: "alice@example.com" });
```

| Property | Type | Required | Default | Description |
|---|---|---:|---|---|
| `data` | JSON object | No | `{}` | Payload returned to waiting run |

### Complete via callback URL (no API key)

```bash
curl -X POST "$TOKEN_URL" \
  -H "Content-Type: application/json" \
  -d '{"approved":true,"reviewer":"alice@example.com"}'
```

`TOKEN_URL` is the presigned callback URL returned by `wait.createToken`.

> ⚠️ WARNING
> Callback completion requires valid `callbackHash` in URL path. Invalid hash returns 401.

> ⚠️ WARNING
> Callback endpoint can return 411 if `Content-Length` is missing, and 413 for oversized payloads.

---

## `wait.listTokens()` and `wait.retrieveToken()`

```ts
for await (const t of wait.listTokens({ status: ["WAITING"], tags: ["tenant:acme"] })) {
  console.log(t.id, t.status);
}

const token = await wait.retrieveToken("waitpoint_abc123");
```

| Property | Type | Required | Default | Description |
|---|---|---:|---|---|
| `status` | `WAITING \| COMPLETED \| TIMED_OUT` (array/string by layer) | No | all statuses | Filter by token state |
| `tags` | string/list | No | none | Filter by token tags |
| `idempotencyKey` | string | No | none | Filter by idempotency key |
| `createdAt.period` | duration string | No | none | Relative window |
| `createdAt.from/to` | datetime | No | none | Absolute range |
| `page[size]`, `page[after/before]` | numbers/cursors | No | API defaults | Cursor pagination |

---

## Checkpointing and Compute Cost

- Waitpoints over short durations may still run inline briefly.
- Long waits (documented threshold: > 5 seconds in Trigger docs) checkpoint and release compute slot.
- Waiting runs resume with preserved state.

> ⚠️ WARNING
> Treat waits as durable suspension points, not in-memory sleep calls; external side effects before wait should be idempotent.

---

## Idempotency + Waits

Use idempotency keys on token creation and trigger boundaries so retries do not create duplicate approval gates.

```ts
const token = await wait.createToken({ idempotencyKey: `approval:${payload.orderId}` });
const result = await wait.forToken(token.id);
```

If a token already completed is returned via idempotency replay, `wait.forToken` can continue immediately.

---

## Input Streams (Higher-level interactive waiting)

Input streams provide typed inbound event channels to running tasks.

```ts
import { streams, task } from "@trigger.dev/sdk";

export const approval = streams.input<{ approved: boolean; reviewer: string }>({ id: "approval" });

export const publishDraft = task({
  id: "publish-draft",
  run: async () => {
    const result = await approval.wait({ timeout: "7d" });
    if (!result.ok || !result.output.approved) return { published: false };
    return { published: true, reviewer: result.output.reviewer };
  },
});
```

Frontend send:

```ts
import { useInputStreamSend } from "@trigger.dev/react-hooks";

const { send } = useInputStreamSend("approval", runId, { accessToken: publicAccessToken });
await send({ approved: true, reviewer: "alice@example.com" });
```

| Method | Purpose |
|---|---|
| `.wait()` | suspend until message/timeout |
| `.once()` | receive once without full suspension pattern |
| `.on()` | register persistent listener |
| `.send(runId, data)` | push data into running task |

---

## Public Access Tokens for Completion

`POST /waitpoints/tokens/{id}/complete` can accept secret key or scoped public access token.

Pattern:

1. backend triggers task and returns `handle.id` + `handle.publicAccessToken`,
2. frontend sends realtime subscriptions and/or token completion,
3. no backend secret exposure.

Related:

- Realtime auth/hook usage: [`TRIGGER_DEV_REALTIME.md`](./TRIGGER_DEV_REALTIME.md)
- Task orchestration patterns: [`TRIGGER_DEV_PATTERNS.md`](./TRIGGER_DEV_PATTERNS.md)

