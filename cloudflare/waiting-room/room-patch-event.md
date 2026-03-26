# Patch event

`PATCH /zones/{zone_id}/waiting_rooms/{waiting_room_id}/events/{event_id}`

Patches a configured event for a waiting room.

## Parameters

- **event_id** (string, required) [path]: 
- **waiting_room_id** (string, required) [path]: 
- **zone_id** (string, required) [path]: 

## Request Body

- **custom_page_html** (string, optional): If set, the event will override the waiting room's `custom_page_html` property while it is active. If null, the event will inherit it.
- **description** (string, optional): A note that you can use to add more details about the event.
- **disable_session_renewal** (boolean, optional): If set, the event will override the waiting room's `disable_session_renewal` property while it is active. If null, the event will inherit it.
- **event_end_time** (string, required): An ISO 8601 timestamp that marks the end of the event.
- **event_start_time** (string, required): An ISO 8601 timestamp that marks the start of the event. At this time, queued users will be processed with the event's configuration. The start time must be at least one minute before `event_end_time`.
- **name** (string, required): A unique name to identify the event. Only alphanumeric characters, hyphens and underscores are allowed.
- **new_users_per_minute** (integer, optional): If set, the event will override the waiting room's `new_users_per_minute` property while it is active. If null, the event will inherit it. This can only be set if the event's `total_active_users` property is also set.
- **prequeue_start_time** (string, optional): An ISO 8601 timestamp that marks when to begin queueing all users before the event starts. The prequeue must start at least five minutes before `event_start_time`.
- **queueing_method** (string, optional): If set, the event will override the waiting room's `queueing_method` property while it is active. If null, the event will inherit it.
- **session_duration** (integer, optional): If set, the event will override the waiting room's `session_duration` property while it is active. If null, the event will inherit it.
- **shuffle_at_event_start** (boolean, optional): If enabled, users in the prequeue will be shuffled randomly at the `event_start_time`. Requires that `prequeue_start_time` is not null. This is useful for situations when many users will join the event prequeue at the same time and you want to shuffle them to ensure fairness. Naturally, it makes the most sense to enable this feature when the `queueing_method` during the event respects ordering such as **fifo**, or else the shuffling may be unnecessary.
- **suspended** (boolean, optional): Suspends or allows an event. If set to `true`, the event is ignored and traffic will be handled based on the waiting room configuration.
- **total_active_users** (integer, optional): If set, the event will override the waiting room's `total_active_users` property while it is active. If null, the event will inherit it. This can only be set if the event's `new_users_per_minute` property is also set.
- **turnstile_action** (string, optional): If set, the event will override the waiting room's `turnstile_action` property while it is active. If null, the event will inherit it. Values: `log`, `infinite_queue`
- **turnstile_mode** (string, optional): If set, the event will override the waiting room's `turnstile_mode` property while it is active. If null, the event will inherit it. Values: `off`, `invisible`, `visible_non_interactive`, `visible_managed`

## Response

### 200

Patch event response

_Empty object_

### 4XX

Patch event response failure

_Empty object_
