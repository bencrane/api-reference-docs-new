# Retries

The Sendoso webhook system implements automatic delivery attempts using an exponential backoff strategy to handle failed messages.

## Retry Schedule

Each message is attempted based on the following schedule, where each period is started following the failure of the preceding attempt:

1. Immediately
2. 5 seconds
3. 5 minutes
4. 30 minutes
5. 2 hours
6. 5 hours
7. 10 hours
8. 10 hours (additional)

The system will continue retrying until successful delivery. For instance, a message failing three times before succeeding takes approximately 35 minutes and 5 seconds from initial attempt.

## Endpoint Management

If an endpoint gets removed or disabled, delivery attempts to the endpoint will be disabled as well.

## Manual Retry Options

Users can leverage the webhooks portal to:

- Manually retry individual messages at any time
- Automatically recover and retry all failed messages from a specified date forward
