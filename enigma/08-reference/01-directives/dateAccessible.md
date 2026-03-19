# dateAccessible Directive

## Overview

The `@dateAccessible` directive computes an accessible date by calculating 15th day of the third month following a provided period end date.

## Syntax

```graphql
directive @dateAccessible(
  ref: String
  refs: [String!]
) on FIELD
```

## Description

This directive transforms a period end date into a forward-looking accessible date. According to the documentation, "it returns the 15th day of +3 months from the input date."

### Example Calculation

When applied to a date of August 30, 2025, the directive produces November 15, 2025—effectively adding three months and standardizing to the 15th day of that month.

## Parameters

| Parameter | Type | Description |
|-----------|------|-------------|
| `ref` | String | Single field reference for date transformation |
| `refs` | [String!] | Multiple field references for batch transformation |

## Usage Pattern

Apply this directive to fields containing period end dates when you need to derive compliance or accessibility deadlines based on a three-month forward offset.
