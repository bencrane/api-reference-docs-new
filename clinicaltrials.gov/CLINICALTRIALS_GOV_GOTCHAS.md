# ClinicalTrials.gov API — Gotchas, Edge Cases & Integration Pitfalls

> **Produced:** 2026-04-15
> **Source material:** `docs/api-reference-docs/clinicaltrials.gov/docs/` and `docs/api-reference-docs/clinicaltrials.gov/openapi/`

Everything non-obvious that will bite you when building against this API.

---

## 1. Modernization Breaking Changes (August 26, 2025)

The ClinicalTrials.gov data pipeline was modernized on August 26, 2025. Two categories of data are affected:

### 1.1 Markup Field Format Changes

- Markup fields that previously contained rich text in the legacy "chintzy" format (an HTML subset) **do not have the exact same format** from the new pipeline.
- Even with `markupFormat=legacy`, the output may differ from the classic pipeline.
- Default format is now **CommonMark markdown**.
- If you were parsing legacy markup HTML, your parsers will break.

### 1.2 Location & GeoPoint Data Source Change

- Locations and geopoint data now pull from **a different geographic database**.
- Existing geocoordinates may shift. If you cache or compare geopoints, expect differences post-modernization.
- `LocationGeoPoint` (with `lat`/`lon`) was **added** in the v2 data model — it did not exist in classic.

---

## 2. Type Conversion Landmines

The v2 API changed the types of many fields. If you're migrating from classic or from cached data, these will silently break parsers expecting the old types.

### 2.1 Text → Boolean (18 fields)

These fields were plain text strings in the classic API and are now JSON booleans (`true`/`false`):

| Field |
|---|
| `AgreementPISponsorEmployee` |
| `AgreementRestrictiveAgreement` |
| `BaselineMeasureCalculatePct` |
| `OutcomeMeasureCalculatePct` |
| `DelayedPosting` |
| `ExpAccTypeIndividual` |
| `ExpAccTypeIntermediate` |
| `ExpAccTypeTreatment` |
| `FDAAA801Violation` |
| `GenderBased` |
| `HealthyVolunteers` |
| `IsPPSD` |
| `IsUnapprovedDevice` |
| `IsUSExport` |
| `LargeDocNoSAP` |
| `OversightHasDMC` |
| `OutcomeAnalysisTestedNonInferiority` |
| `PatientRegistry` |

### 2.2 Text → Enum (40+ fields)

These fields were free-text in classic and are now constrained enum values in `UPPER_SNAKE_CASE`. The full list with value mappings:

| Field | Enum Type | Example: Old → New |
|---|---|---|
| `ArmGroupType` | `ArmGroupType` | `Experimental` → `EXPERIMENTAL` |
| `OverallStatus` | `Status` | `Active, not recruiting` → `ACTIVE_NOT_RECRUITING` |
| `Phase` | `Phase` | `Phase 1` → `PHASE1`, `Not Applicable` → `NA` |
| `StudyType` | `StudyType` | `Interventional` → `INTERVENTIONAL` |
| `Sex` | `Sex` | `All` → `ALL` |
| `StdAge` | `StandardAge` | `Older Adult` → `OLDER_ADULT` |
| `DesignAllocation` | `DesignAllocation` | `N/A` → `NA` |
| `DesignInterventionModel` | `InterventionalAssignment` | `Single Group Assignment` → `SINGLE_GROUP` |
| `DesignMasking` | `DesignMasking` | `None (Open Label)` → `NONE` |
| `DesignPrimaryPurpose` | `PrimaryPurpose` | `Educational/Counseling/Training` → `ECT` |
| `DesignObservationalModel` | `ObservationalModel` | `Case-Control` → `CASE_CONTROL` |
| `DesignTimePerspective` | `DesignTimePerspective` | `Cross-Sectional` → `CROSS_SECTIONAL` |
| `DesignWhoMasked` | `WhoMasked` | `Outcomes Assessor` → `OUTCOMES_ASSESSOR` |
| `InterventionType` | `InterventionType` | `Drug` → `DRUG` |
| `LeadSponsorClass` | `AgencyClass` | `INDUSTRY` → `INDUSTRY` |
| `CollaboratorClass` | `AgencyClass` | (same enum) |
| `OrgClass` | `AgencyClass` | (same enum) |
| `LocationStatus` | `RecruitmentStatus` | `Recruiting` → `RECRUITING` |
| `LastKnownStatus` | `Status` | `Unknown status` → `UNKNOWN` |
| `IPDSharing` | `IpdSharing` | `Yes` → `YES` |
| `IPDSharingInfoType` | `IpdSharingInfoType` | `Study Protocol` → `STUDY_PROTOCOL` |
| `ReferenceType` | `ReferenceType` | `background` → `BACKGROUND` |
| `BioSpecRetention` | `BioSpecRetention` | `Samples With DNA` → `SAMPLES_WITH_DNA` |
| `ResponsiblePartyType` | `ResponsiblePartyType` | `Sponsor-Investigator` → `SPONSOR_INVESTIGATOR` |
| `SamplingMethod` | `SamplingMethod` | `Probability Sample` → `PROBABILITY_SAMPLE` |
| `CentralContactRole` | `ContactRole` | `Principal Investigator` → `PRINCIPAL_INVESTIGATOR` |
| `LocationContactRole` | `ContactRole` | (same enum) |
| `OverallOfficialRole` | `OfficialRole` | `Study Chair` → `STUDY_CHAIR` |
| `OrgStudyIdType` | `OrgStudyIdType` | `U.S. NIH Grant/Contract` → `NIH` |
| `SecondaryIdType` | `SecondaryIdType` | `EudraCT Number` → `EUDRACT_NUMBER` |
| `ExpandedAccessStatusForNCTId` | `ExpandedAccessStatus` | `Available` → `AVAILABLE` |
| `SeriousEventAssessmentType` | `EventAssessment` | `Systematic Assessment` → `SYSTEMATIC_ASSESSMENT` |
| `OtherEventAssessmentType` | `EventAssessment` | (same enum) |
| `ConditionBrowseLeafRelevance` | `BrowseLeafRelevance` | `high` → `HIGH` |
| `InterventionBrowseLeafRelevance` | `BrowseLeafRelevance` | (same enum) |
| `OutcomeAnalysisNonInferiorityType` | `NonInferiorityType` | `Non-Inferiority` → `NON_INFERIORITY` |
| `OutcomeAnalysisDispersionType` | `AnalysisDispersionType` | `Standard Deviation` → `STANDARD_DEVIATION` |
| `OutcomeAnalysisCINumSides` | `ConfidenceIntervalNumSides` | `2-Sided` → `TWO_SIDED` |
| `OutcomeMeasureType` | `OutcomeMeasureType` | `Primary` → `PRIMARY` |
| `OutcomeMeasureReportingStatus` | `ReportingStatus` | `Posted` → `POSTED` |
| `BaselineMeasureParamType` | `MeasureParam` | `Median` → `MEDIAN` |
| `OutcomeMeasureParamType` | `MeasureParam` | (same enum) |
| `BaselineMeasureDispersionType` | `MeasureDispersionType` | `Standard Deviation` → `STANDARD_DEVIATION` |
| `AgreementRestrictionType` | `AgreementRestrictionType` | `LTE 60` → `LTE60` |
| `UnpostedEventType` | `UnpostedEventType` | `Release` → `RELEASE` |
| `ViolationEventType` | `ViolationEventType` | `Penalty Imposed by FDA` → `PENALTY_IMPOSED` |
| All `*DateType` fields | `DateType` | `Actual` → `ACTUAL`, `Anticipated` → `ESTIMATED` |
| `EnrollmentType` | `EnrollmentType` | `Anticipated` → `ESTIMATED` |

**Watch out:** `Anticipated` maps to `ESTIMATED` (not `ANTICIPATED`) for all date type and enrollment type fields.

### 2.3 Markup → Text (2 fields)

These fields were markup (HTML-capable) and are now plain text because the PRS never allowed formatted text in them:
- `BriefTitle`
- `OfficialTitle`

### 2.4 List → Single Value (2 fields)

These fields were arrays in classic and are now single values:
- `DesignObservationalModel`
- `DesignTimePerspective`

If your code expects arrays for these fields, it will break.

### 2.5 Date Field Format Change

All date fields now use **ISO 8601** format. Possible formats:
- `yyyy`
- `yyyy-MM`
- `yyyy-MM-dd`
- `yyyy-MM-dd'T'HH:mm`

Previously, some date fields could contain the string `"Unknown"`. This is no longer possible. Two new boolean fields were added to handle these cases:
- `SubmissionUnreleaseDateUnknown` — `true` when the date was previously `"Unknown"`
- `UnpostedEventDateUnknown` — `true` when the date was previously `"Unknown"`

---

## 3. Array Serialization (No Wrappers)

In the classic API, lists used wrapper elements:
```xml
<ConditionList>
  <Condition>Cancer</Condition>
  <Condition>Tumor</Condition>
</ConditionList>
```

In v2 JSON, there are **no wrapper elements**. Arrays use **plural names** directly:
```json
{
  "conditions": ["Cancer", "Tumor"]
}
```

If you're generating field paths from classic XPaths, strip the wrapper level.

---

## 4. Field Availability Asymmetry

Some fields are **searchable but not retrievable** (marked with ✗ in the data structure). These are computed/aggregation fields:

| Field | Description |
|---|---|
| `NumConditionMeshes` | Count of condition MeSH terms |
| `NumConditionAncestors` | Count of condition ancestor terms |
| `NumConditionBrowseLeafs` | Count of condition browse leaves |
| `NumConditionBrowseBranches` | Count of condition browse branches |
| `NumInterventionMeshes` | Count of intervention MeSH terms |
| `NumInterventionAncestors` | Count of intervention ancestor terms |
| `NumInterventionBrowseLeafs` | Count of intervention browse leaves |
| `NumInterventionBrowseBranches` | Count of intervention browse branches |

You can filter/search by these fields, but they will not appear in the response JSON even if explicitly requested in `fields`.

> :warning: **INFERRED:** The inverse case — fields that are retrievable but not searchable — is not explicitly documented. The search areas documentation lists which fields participate in search; any field not in any search area may only be accessible via direct retrieval.

---

## 5. Nested Search Complexity

### The Problem

If a study has locations in both Florence, Italy and Florence, South Carolina, a naive query like:
```
query.locn=Florence AND query.locn=South Carolina
```
...may match the study even though no single location is "Florence, South Carolina" — it matches Florence from one location and South Carolina from another.

### The Fix

Use the `SEARCH` operator to scope the match to a single nested object:
```
SEARCH[Location](AREA[LocationCity]Florence AND AREA[LocationState]South Carolina AND AREA[LocationCountry]United States)
```

### When You Need It

Any time you're querying multiple fields within a repeated nested structure:
- Locations (city + state + country + facility)
- Interventions (name + type + description)
- Arm groups
- Outcome measures

---

## 6. CSV vs JSON Coverage Gap

| | CSV | JSON |
|---|---|---|
| **Max columns/fields** | 30 fixed column groups | Unlimited (full data model) |
| **Nested data** | Flattened into combined columns | Full nested structure |
| **Results section** | Limited (outcome measures only) | Full results data |
| **Browse/MeSH data** | Not available | Available |
| **Markup encoding** | Markdown | Markdown or legacy (configurable) |

**Bottom line:** CSV is useful for quick exports of core study metadata. For any serious data work — especially results data, adverse events, browse modules, or complex nested structures — use JSON.

---

## 7. Data Freshness

- Refreshes happen **Monday through Friday only**.
- Target completion: **9:00 AM ET (14:00 UTC)**.
- **Weekend data is stale** — anything submitted Friday afternoon through Sunday won't appear until Monday's refresh.
- Always check `/api/v2/version` → `dataTimestamp` before relying on data freshness.
- If you run a sync job at 8:00 AM ET Monday, you may get Friday's data — the refresh might not be complete yet.

---

## 8. Legacy vs Modern Endpoint Differences

| Dimension | Modern (`/api/v2/`) | Legacy (`/api/legacy/`) |
|---|---|---|
| **Format** | JSON, CSV | XML only |
| **Result limit (with search expr)** | No documented limit | 10,000 studies |
| **Field names** | camelCase JSON paths | Classic XPath-style names |
| **Array format** | Plural names, no wrappers | Wrapper elements (e.g., `ConditionList`) |
| **Enums** | `UPPER_SNAKE_CASE` | Human-readable text |
| **Booleans** | JSON `true`/`false` | Text strings |
| **Dates** | ISO 8601 | Mixed formats including `"Unknown"` |
| **Markup** | Markdown (default) or legacy | Legacy HTML subset |
| **Search areas** | Default differs from classic | Matches classic behavior |
| **Pagination** | Token-based (`pageToken`) | Offset-based (`min_rnk`, `max_rnk`) |
| **Unavailable fields** | — | `FlowReasonNumUnits`, `OrgStudyIdDomain` (no data in any study) |

---

## 9. FHIR Format Limitations

- **Pilot status** — not production-stable.
- **Single study only** — FHIR download is available for individual study records, not for search results or bulk downloads.
- **FHIR R6** — this is a very recent FHIR version. Many FHIR libraries may not yet support R6.
- Uses specialized resources (`Citation`, `Evidence`, `EvidenceVariable`) that require R6.
- External rendering via [FEvIR Platform](https://fevir.net/) — ClinicalTrials.gov does not render FHIR directly.

---

## 10. COVERAGE and EXPANSION Operators

The `COVERAGE` and `EXPANSION` search operators are **not fully implemented** on the modernized ClinicalTrials.gov. If your queries use these operators, they may silently return incorrect or incomplete results. There is no timeline for full implementation.

---

## 11. Search Area Default Mismatch

The source material notes:

> "The default search areas for the classic and new API full studies endpoints are different."

This means the same query text passed to `/api/query/full_studies` (classic) and `/api/v2/studies` (modern) may return **different results** because they search different default field sets. If you're migrating, explicitly specify the search area using `query.*` parameters or `AREA[]` operators rather than relying on defaults.

---

## 12. `stats/field/values` Limitations

The `/api/v2/stats/field/values` endpoint:
- Does **not** accept search expressions — it always returns values across the entire database.
- Returns a **maximum of 250 values** per field.
- For high-cardinality fields (e.g., `LeadSponsorName`, `LocationCity`), you will not get a complete list.
- Not a replacement for the classic `/api/query/field_values` endpoint which accepted search expressions.

---

## 13. Undocumented Behaviors (Inferred)

> :warning: The following are inferred from the source material and API structure. They are not explicitly documented and should be verified by testing.

1. **Rate limiting exists but is undocumented.** The API is public with no auth — some form of rate limiting almost certainly exists. No HTTP headers or error codes for rate limiting are documented.

2. **`filter.geo` syntax is undocumented.** The parameter exists on `/api/v2/studies` but the exact syntax for distance-based queries is not specified in the source material. GeoPoint data (`lat`/`lon`) is available on locations, suggesting distance queries are supported.

3. **`filter.advanced` accepts AREA expressions.** Based on the query system documentation, advanced filters likely support the same `AREA[]` and `SEARCH[]` operators as `query.term`.

4. **`countTotal` may have performance implications.** Total count computation on large result sets is typically expensive. The fact that it's an opt-in parameter suggests it adds latency.

5. **Pagination tokens are opaque and likely time-limited.** The source material does not document token expiration, but token-based pagination systems typically expire tokens after minutes to hours.

6. **The "most popular" JSON preset may change.** The 8 pre-selected fields for the "most popular" download option are a UI concern and may be updated without API versioning.

---

## 14. Field Name Gotchas

- **camelCase in JSON, PascalCase in piece names:** The JSON field path uses camelCase (`briefTitle`), but the "Piece Name" used in search areas and the `fields` parameter uses PascalCase (`BriefTitle`). These are different namespaces.
- **Date struct fields:** Date fields that have associated type information use a `Struct` suffix in the JSON path (e.g., `startDateStruct` containing `date` and `type` sub-fields), but the flat piece name is just `StartDate` and `StartDateType`.
- **Enrollment ambiguity:** `EnrollmentCount` is the piece name for the enrollment number, but in JSON it's nested as `enrollmentInfo.count` with a sibling `enrollmentInfo.type`.

---

## 15. Known Data Quality Issues

- **`LocationGeoPoint` sourced from new database:** Post-modernization, geographic coordinates may differ from any cached values from the classic pipeline.
- **Withheld studies:** Several fields are `[Missing]` for studies with `OverallStatus = WITHHELD`, including `OversightHasDMC`, `IsFDARegulatedDrug`, `IsFDARegulatedDevice`.
- **`HasResults` is computed:** It's defined as `Present(ResultsFirstSubmitDate)` — if a study submitted results but they haven't been posted, `HasResults` may still be `true` even though the results section may be sparse or have `ReportingStatus = NOT_POSTED`.
