# TinType Enum

## Overview

`TinType` is an enumeration used within the Enigma GraphQL API to specify different categories of taxpayer identification numbers.

## Definition

```graphql
enum TinType {
  EIN
  SSN
  ITIN
  TIN
}
```

## Values

| Value | Description |
|-------|-------------|
| **EIN** | Employer Identification Number |
| **SSN** | Social Security Number |
| **ITIN** | Individual Taxpayer Identification Number |
| **TIN** | General Taxpayer Identification Number |

## Usage

This enumeration is utilized as a member of the [`TinInput`](/reference/graphql_api/inputs/tin-input) input type, allowing developers to specify which type of tax identification number they are working with when querying or filtering business entity data.

## Related Documentation

- **Referenced by:** [`TinInput`](/reference/graphql_api/inputs/tin-input)
- **API Section:** GraphQL API Reference > Enums
