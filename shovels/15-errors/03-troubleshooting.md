# API Troubleshooting

> **Source:** https://docs.shovels.ai/docs/shovels-api-troubleshooting
> **Fetched:** 2026-04-16

Common issues and how to fix them when using the Shovels API.

## General 5-step diagnostic

1. **Verify API key.** Ensure that your API key is accurate and matches what you see in your Shovels Account Settings.
2. **Validate required fields.** Different endpoints have different required-field sets; consult the API Reference.
3. **Confirm server URL.** Make sure you're using the full `api.shovels.ai/v2` URL, not just `/v2`.
4. **Review request syntax.** Errors in query configuration cause issues; consult API Reference examples.
5. **Identify parameter conflicts.** For scenarios where you receive a `404` unexpectedly, conflicting parameters can produce queries with no possible results.

## 404 error causes

- Conflicting parameters creating queries with no possible results.
- Example: combining `property_type = "residential"` with `permit_min_fees = "X,XXX"` — residential permit fees are under-reported, so the combination can yield zero matches.

## Null values in responses

- There's significant variability in the required fields for permits across different permit jurisdictions.
- Data gaps are filled using available information or extracted from `description` fields.
- Unifying fields across diverse jurisdictions necessarily produces incomplete datasets for some fields.

## Common issues

1. Encountering undocumented HTTP error codes.
2. High frequency of null values in responses.

## Error-code references

- Shovels recommends the Mozilla HTTP Status Codes documentation for generic codes.
- For Shovels-specific codes see `01-error-handling.md` in this directory.

## Support contact

- Email `support@shovels.ai` with request details, troubleshooting steps attempted, and relevant context.
- Include the user email tied to the API key, the full request, any error payload, and steps already tried.

## Related

- `01-error-handling.md`
- `02-error-422.md`
- `../14-api-basics/` — basics directory for rate/credit limit context when errors are limit-related.
