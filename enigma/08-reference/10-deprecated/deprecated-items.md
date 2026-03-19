# Deprecated GraphQL Items

## Overview

This section documents deprecated items in the Enigma GraphQL API. As of the latest documentation update, no specific deprecated items are actively listed in the API reference.

## Checking for Deprecations

When working with the Enigma GraphQL API:

1. **Review Field Descriptions**: Individual fields may be marked as deprecated in their type documentation
2. **Check Schema Introspection**: Use GraphQL introspection to query for deprecated fields:
   ```graphql
   {
     __schema {
       types {
         name
         fields {
           name
           isDeprecated
           deprecationReason
         }
       }
     }
   }
   ```
3. **Consult Release Notes**: Check Enigma's release notes for deprecation announcements

## Best Practices

- Monitor API version updates for deprecation notices
- Use schema introspection to identify deprecated fields before they're removed
- Plan migrations well in advance when deprecations are announced
- Refer to the [GraphQL API Reference](https://documentation.enigma.com/reference/graphql_api) for the most current schema information

## Related Resources

- [GraphQL API Overview](https://documentation.enigma.com/reference/graphql_api)
- [Query Guide](https://documentation.enigma.com/guides/graphql)

---

*Last updated: March 18, 2026*
