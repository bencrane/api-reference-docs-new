# account Query

## Overview

The `account` query is part of the Enigma GraphQL API reference documentation. It provides access to account-related data through the GraphQL interface.

## Query Signature

```graphql
account: Account
```

## Return Type

This query returns an [`Account`](/reference/graphql_api/objects/account) object, which contains account-related information accessible through the Enigma GraphQL API.

## Usage

To use this query, include it in your GraphQL request to retrieve account data:

```graphql
query {
  account {
    # Account fields
  }
}
```

## Related Resources

- **Previous:** [Website](/reference/graphql_api/objects/website) object reference
- **Next:** [aggregate](/reference/graphql_api/queries/aggregate) query
- **Related:** [Account Object](/reference/graphql_api/objects/account) documentation

## Additional Information

- **Last Updated:** March 11, 2026
- **API Version:** Current GraphQL API
- **Documentation Location:** `/reference/graphql_api/queries/account`

For comprehensive details about the Account object structure and available fields, consult the [Account object documentation](/reference/graphql_api/objects/account).
