# Delete Insight API Reference

## Endpoint

**Method:** DELETE
**URL:** `https://api.vapi.ai/reporting/insight/{id}`

## Description

This endpoint removes an insight from the reporting system. The deletion operation returns the deleted insight object with all its configuration details.

## Parameters

### Path Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `id` | string | Yes | The unique identifier of the insight to delete |

### Header Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `Authorization` | string | Yes | "Retrieve your API Key from Dashboard" |

## Response

### Success Response (200 OK)

The response returns the deleted insight object. The insight can be one of four types: **bar**, **pie**, **line**, or **text**. Each variant includes:

**Common fields for all insight types:**
- `id` (string): Unique identifier for the insight
- `type` (string): The insight visualization type (bar, pie, line, or text)
- `name` (string): Display name of the insight
- `queries` (array): Query definitions used to generate the insight
- `orgId` (string): Organization identifier
- `createdAt` (datetime): ISO 8601 creation timestamp
- `updatedAt` (datetime): ISO 8601 last update timestamp

**Type-specific fields:**

**Bar Insight:**
- `formulas` (array): Mathematical expressions for data transformation
- `metadata` (object): Chart labels and axis bounds
- `timeRange` (object): Time range with step, start, and end
- `groupBy` (string): Column to group results by

**Pie Insight:**
- `formulas` (array): Mathematical expressions
- `timeRange` (object): Time range configuration
- `groupBy` (string): Grouping column

**Line Insight:**
- `formulas` (array): Mathematical expressions
- `metadata` (object): Chart metadata
- `timeRange` (object): Time range with aggregation step
- `groupBy` (string): Grouping column

**Text Insight:**
- `formula` (object): Single mathematical expression
- `timeRange` (object): Time range configuration
- `queries` (array): Single query or multiple with formula requirement

## SDK Example

```python
from vapi import Vapi

client = Vapi(
    token="YOUR_TOKEN_HERE",
)

client.insight.insight_controller_remove(
    id="id",
)
```
