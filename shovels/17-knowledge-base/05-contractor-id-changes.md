# Contractor ID Changes

> **Source:** https://docs.shovels.ai/docs/knowledge-base/data/contractors/id-changes
> **Fetched:** 2026-04-16

Understand why contractor IDs may occasionally change, how branch-level assignment works, and how to stay current with the contractor-ID changelog.

## Why IDs change

Contractor IDs occasionally shift as Shovels discovers new permit data and additional contractor details. Changes occur when a subsequent permit scrape reveals new information — for example, a newly identified business address enabling matching to existing branch records.

## Branch-level assignment

IDs are assigned at the branch level:

- A contractor operating in City X receives a different ID than the same business name in another city.
- Contractors without identifiable business addresses receive separate IDs.

## Changelog and tracking

Shovels maintains a **contractor ID changelog** that tracks these changes. Organizations affected by ID modifications can request access to this changelog from support.

## Remediation

When you encounter a not-found response for a cached ID, relookup using alternative attributes:

- Business name
- Address
- License number

## Key v2.1.7 context

The 2026-04-02 release regenerated **all** contractor IDs as part of the data-pipeline transition. 81.8% of pre-2026-04-02 IDs map to new IDs via the changelog; 18.2% have no mapping. See `../13-release-notes/01-release-notes.md` v2.1.7.

## Support

- `support@shovels.ai` for changelog access or ID remediation help.
