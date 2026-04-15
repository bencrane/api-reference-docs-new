# ClinicalTrials.gov API v2 — Canonical Reference

> **Produced:** 2026-04-15
> **Source material:** `docs/api-reference-docs/clinicaltrials.gov/docs/` (ClinicalTrials.gov API docs) and `docs/api-reference-docs/clinicaltrials.gov/openapi/` (OpenAPI 3.0.3 spec reference)
> **Spec:** [ctg-oas-v2.yaml](https://clinicaltrials.gov/api/oas/v2/ctg-oas-v2.yaml) (OpenAPI 3.0.3)

---

## Table of Contents

1. [API Fundamentals](#1-api-fundamentals)
2. [Core Endpoints](#2-core-endpoints)
3. [Data Model](#3-data-model)
4. [Query & Search System](#4-query--search-system)
5. [Pagination & Bulk Retrieval](#5-pagination--bulk-retrieval)
6. [Practical Patterns](#6-practical-patterns)
7. [Legacy & Migration Endpoints](#7-legacy--migration-endpoints)
8. [Response Formats](#8-response-formats)

---

## 1. API Fundamentals

### Base URL & Versioning

| Path prefix | Purpose |
|---|---|
| `/api/v2/` | Modern API (primary — use this) |
| `/api/legacy/` | Legacy compatibility shim (replicates classic behavior; XML only) |
| `/api/info/` | Classic info endpoints (deprecated; mapped to v2 equivalents) |
| `/api/query/` | Classic query endpoints (deprecated; mapped to v2 equivalents) |

Base URL: `https://clinicaltrials.gov`

### Authentication

The API is **public and unauthenticated**. No API keys, tokens, or auth headers are required.

> :warning: **NOT DOCUMENTED:** There is no documented rate limiting policy. The source material does not specify request-per-second limits, throttling behavior, or HTTP 429 handling. Plan defensively: implement backoff, respect HTTP status codes, and avoid aggressive parallelism.

### Data Refresh Schedule

- Data is refreshed **daily, Monday through Friday**, generally by **9:00 AM ET (14:00 UTC)**.
- **No weekend refreshes** — data visible Saturday/Sunday is the Friday snapshot.
- Always check `dataTimestamp` from `/api/v2/version` to confirm the refresh has completed before relying on freshness.

### Response Formats

| Format | Availability | Notes |
|---|---|---|
| **JSON** | All endpoints | Primary format. Full field coverage. |
| **CSV** | `/api/v2/studies` (search results download) | Limited to 30 column groups. Markup fields encoded as markdown. |
| **RIS** | Search results download | Research Information Systems format for citation managers. Fixed tag set. |
| **FHIR** | Single study download only | Pilot project. FHIR R6. Converts to ResearchStudy Resource. |
| **XML** | Legacy endpoints only (`/api/legacy/*`) | Not available on v2 endpoints. |

---

## 2. Core Endpoints

### 2.1 `GET /api/v2/studies` — List / Search Studies

The primary endpoint for searching and retrieving study data.

**Parameters:**

| Parameter | Type | Description |
|---|---|---|
| `query.term` | string | Free-text search against the BasicSearch area (57 weighted fields) |
| `query.cond` | string | Condition/disease search (ConditionSearch area, 7 fields) |
| `query.intr` | string | Intervention/treatment search (InterventionSearch area, 12 fields) |
| `query.titles` | string | Title/acronym search (TitleSearch area, 3 fields) |
| `query.outc` | string | Outcome measure search (OutcomeSearch area, 9 fields) |
| `query.spons` | string | Sponsor/collaborator search (SponsorSearch area, 3 fields) |
| `query.locn` | string | Location search (LocationSearch area, 5 fields) |
| `query.id` | string | Study ID search (IdSearch area, 5 fields) |
| `query.patient` | string | Patient-oriented search (PatientSearch area, 47 fields) |
| `fields` | string | Comma-separated field names to include in response. Omit for full records. |
| `sort` | string | Sort order for results |
| `format` | string | Response format: `json` (default), `csv` |
| `markupFormat` | string | Markup field format: `markdown` (default) or `legacy` |
| `pageSize` | integer | Results per page. Default: 10. Maximum: 1000. |
| `pageToken` | string | Pagination token from previous response's `nextPageToken` |
| `countTotal` | boolean | Whether to include total count in response |
| `filter.overallStatus` | string | Filter by study status enum values |
| `filter.geo` | string | Geographic filter (distance-based location search) |
| `filter.ids` | string | Filter by NCT IDs |
| `filter.advanced` | string | Advanced filter expression |
| `postFilter.overallStatus` | string | Post-search filter by status |
| `postFilter.geo` | string | Post-search geographic filter |
| `aggFilters` | string | Aggregation-based filters |

**Response shape** (JSON):
```json
{
  "studies": [
    {
      "protocolSection": { ... },
      "resultsSection": { ... },
      "annotationSection": { ... },
      "documentSection": { ... },
      "derivedSection": { ... },
      "hasResults": true
    }
  ],
  "nextPageToken": "...",
  "totalCount": 12345
}
```

**Notes:**
- When `fields` is specified, the response retains the full nested structure but only populates the requested fields.
- Responses are paginated. Default page size is 10; max is 1000.
- Multiple `query.*` parameters are combined with AND logic.

### 2.2 `GET /api/v2/studies/{nctId}` — Single Study Lookup

Retrieves the complete record for a single study by NCT ID.

**Path parameter:** `nctId` — e.g., `NCT04280705`

**Query parameters:** Same as `/api/v2/studies` for `fields` and `markupFormat`.

**Response:** A single study object (same shape as one element of the `studies` array above).

### 2.3 `GET /api/v2/studies/metadata` — Field Metadata

Returns the study data model definition — all available fields, their types, nesting structure, and attributes.

**Replaces:** `/api/info/study_structure`, `/api/info/study_statistics`

### 2.4 `GET /api/v2/studies/search-areas` — Search Areas

Returns the list of search areas with their constituent fields and weights.

**Replaces:** `/api/info/search_areas`

### 2.5 `GET /api/v2/version` — Data Version / Timestamp

Returns the current data version and timestamp.

**Response:**
```json
{
  "apiVersion": "...",
  "dataTimestamp": "2026-04-14T14:00:00Z"
}
```

Use `dataTimestamp` to verify whether the daily refresh has completed.

### 2.6 `GET /api/v2/stats/field/values` — Field Value Statistics

Returns distinct values for specified fields across all studies.

**Parameters:**

| Parameter | Description |
|---|---|
| `fields` | Comma-separated field names |
| `types` | Filter by data type (e.g., `DATE`, `ENUM`) |

**Limitations:**
- Does not accept a search expression — always returns values across all studies.
- Maximum 250 returned values per field.

### 2.7 `GET /api/v2/stats/field/sizes` — Field Size Statistics

Returns size/count statistics for specified fields.

### 2.8 `GET /api/v2/studies/download` — Bulk Download

Downloads study data in bulk.

**Parameters:**

| Parameter | Description |
|---|---|
| `format` | `json.zip` for a ZIP archive of all studies in JSON format |

Each file in the ZIP has the same JSON schema as `GET /api/v2/studies/{nctId}`.

> :warning: **NOT DOCUMENTED:** Exact file size, compression behavior, and whether incremental/delta downloads are supported are not documented. These ZIP files are very large (hundreds of thousands of studies) and will take several minutes to download.

---

## 3. Data Model

### 3.1 Top-Level Structure

Every study record consists of five sections plus a top-level flag:

| Section | JSON path | Description |
|---|---|---|
| **Protocol Section** | `protocolSection` | Core study protocol: identification, status, sponsor, design, eligibility, contacts, locations |
| **Results Section** | `resultsSection` | Posted results: participant flow, baseline, outcomes, adverse events |
| **Annotation Section** | `annotationSection` | NLM annotations: unposted events, violation events |
| **Document Section** | `documentSection` | Large documents (protocol PDFs, SAPs, ICFs) |
| **Derived Section** | `derivedSection` | Computed fields: MeSH term mappings, browse modules |
| **Has Results** | `hasResults` | Boolean flag: `true` if `ResultsFirstSubmitDate` exists |

### 3.2 Protocol Section Modules

| Module | Path | Key Fields |
|---|---|---|
| **Identification** | `protocolSection.identificationModule` | `nctId`, `orgStudyIdInfo`, `secondaryIdInfos`, `briefTitle`, `officialTitle`, `acronym` |
| **Status** | `protocolSection.statusModule` | `overallStatus`, `lastKnownStatus`, `startDateStruct`, `primaryCompletionDateStruct`, `completionDateStruct`, `studyFirstSubmitDate`, `studyFirstPostDateStruct`, `lastUpdatePostDateStruct` |
| **Sponsor/Collaborators** | `protocolSection.sponsorCollaboratorsModule` | `leadSponsor.name`, `leadSponsor.class`, `collaborators[].name`, `collaborators[].class` |
| **Oversight** | `protocolSection.oversightModule` | `oversightHasDmc`, `isFdaRegulatedDrug`, `isFdaRegulatedDevice`, `isUnapprovedDevice`, `isUSExport` |
| **Description** | `protocolSection.descriptionModule` | `briefSummary`, `detailedDescription` |
| **Conditions** | `protocolSection.conditionsModule` | `conditions[]`, `keywords[]` |
| **Design** | `protocolSection.designModule` | `studyType`, `phases[]`, `designInfo` (allocation, interventionModel, masking, primaryPurpose, observationalModel, timePerspective), `enrollmentInfo` |
| **Arms/Interventions** | `protocolSection.armsInterventionsModule` | `armGroups[]` (label, type, description), `interventions[]` (type, name, description, otherNames) |
| **Outcomes** | `protocolSection.outcomesModule` | `primaryOutcomes[]`, `secondaryOutcomes[]`, `otherOutcomes[]` — each with `measure`, `description`, `timeFrame` |
| **Eligibility** | `protocolSection.eligibilityModule` | `eligibilityCriteria`, `healthyVolunteers`, `sex`, `genderBased`, `minimumAge`, `maximumAge`, `stdAges[]` |
| **Contacts/Locations** | `protocolSection.contactsLocationsModule` | `centralContacts[]`, `overallOfficials[]`, `locations[]` (facility, city, state, zip, country, geoPoint, status, contacts) |
| **References** | `protocolSection.referencesModule` | `references[]` (pmid, type, citation), `seeAlsoLinks[]` |
| **IPD Sharing** | `protocolSection.ipdSharingStatementModule` | `ipdSharing`, `ipdSharingDescription`, `ipdSharingInfoTypes[]`, `ipdSharingTimeFrame`, `ipdSharingAccessCriteria`, `ipdSharingUrl` |

### 3.3 Results Section Modules

| Module | Path | Key Fields |
|---|---|---|
| **Participant Flow** | `resultsSection.participantFlowModule` | `groups[]`, `periods[]` (with milestones and dropWithdraws) |
| **Baseline** | `resultsSection.baselineCharacteristicsModule` | `groups[]`, `measures[]` (with classes and categories) |
| **Outcome Measures** | `resultsSection.outcomeMeasuresModule` | `outcomeMeasures[]` (type, title, groups, denoms, classes with categories, analyses) |
| **Adverse Events** | `resultsSection.adverseEventsModule` | `frequencyThreshold`, `timeFrame`, `description`, `eventGroups[]`, `seriousEvents[]`, `otherEvents[]` |
| **More Info** | `resultsSection.moreInfoModule` | `certainAgreement`, `pointOfContact`, `limitationsAndCaveats` |

### 3.4 Derived Section Modules

| Module | Path | Description |
|---|---|---|
| **MiscInfo** | `derivedSection.miscInfoModule` | Version holder |
| **Condition Browse** | `derivedSection.conditionBrowseModule` | MeSH terms, ancestors, browse leaves, browse branches for conditions |
| **Intervention Browse** | `derivedSection.interventionBrowseModule` | MeSH terms, ancestors, browse leaves, browse branches for interventions |

### 3.5 Field Type System

| Type | Format | Notes |
|---|---|---|
| `text` | Plain string | |
| `nct` | String (`NCT` + 8 digits) | NCT ID format |
| `markup` | Markdown string (default) or legacy HTML subset | Controlled by `markupFormat` parameter |
| `boolean` | JSON boolean | 18 fields were converted from text to boolean in v2 |
| `enum` | UPPER_SNAKE_CASE string | 40+ fields were converted from text to enum. See Enumeration Types below. |
| `date` | ISO 8601: `yyyy`, `yyyy-MM`, or `yyyy-MM-dd` | Partial dates are valid |
| `datetime` | ISO 8601: `yyyy-MM-dd'T'HH:mm` | |
| `short` | Integer | Computed count fields |
| `GeoName` | String | Geographic name (city, state) — supports geo queries |
| `GeoPoint` | `{ lat: number, lon: number }` | Added in v2; sourced from new geographic database |

### 3.6 Array Serialization

Arrays use **plural JSON names** with **no wrapper elements**:
- `conditions` (not `conditionList.condition`)
- `interventions`, `locations`, `phases`, `collaborators`, etc.

This is a breaking change from the classic API which used wrapper elements like `ConditionList`.

### 3.7 Key Enumeration Types

| Enum | Values |
|---|---|
| `Status` | `ACTIVE_NOT_RECRUITING`, `COMPLETED`, `ENROLLING_BY_INVITATION`, `NOT_YET_RECRUITING`, `RECRUITING`, `SUSPENDED`, `TERMINATED`, `WITHDRAWN`, `AVAILABLE`, `NO_LONGER_AVAILABLE`, `TEMPORARILY_NOT_AVAILABLE`, `APPROVED_FOR_MARKETING`, `WITHHELD`, `UNKNOWN` |
| `StudyType` | `EXPANDED_ACCESS`, `INTERVENTIONAL`, `OBSERVATIONAL` |
| `Phase` | `NA`, `EARLY_PHASE1`, `PHASE1`, `PHASE2`, `PHASE3`, `PHASE4` |
| `Sex` | `FEMALE`, `MALE`, `ALL` |
| `StandardAge` | `CHILD`, `ADULT`, `OLDER_ADULT` |
| `AgencyClass` | `NIH`, `FED`, `OTHER_GOV`, `INDIV`, `INDUSTRY`, `NETWORK`, `AMBIG`, `OTHER`, `UNKNOWN` |
| `InterventionType` | `BEHAVIORAL`, `BIOLOGICAL`, `COMBINATION_PRODUCT`, `DEVICE`, `DIAGNOSTIC_TEST`, `DIETARY_SUPPLEMENT`, `DRUG`, `GENETIC`, `PROCEDURE`, `RADIATION`, `OTHER` |
| `DesignAllocation` | `RANDOMIZED`, `NON_RANDOMIZED`, `NA` |
| `InterventionalAssignment` | `SINGLE_GROUP`, `PARALLEL`, `CROSSOVER`, `FACTORIAL`, `SEQUENTIAL` |
| `PrimaryPurpose` | `TREATMENT`, `PREVENTION`, `DIAGNOSTIC`, `ECT`, `SUPPORTIVE_CARE`, `SCREENING`, `HEALTH_SERVICES_RESEARCH`, `BASIC_SCIENCE`, `DEVICE_FEASIBILITY`, `OTHER` |
| `ObservationalModel` | `COHORT`, `CASE_CONTROL`, `CASE_ONLY`, `CASE_CROSSOVER`, `ECOLOGIC_OR_COMMUNITY`, `FAMILY_BASED`, `DEFINED_POPULATION`, `NATURAL_HISTORY`, `OTHER` |
| `DesignMasking` | `NONE`, `SINGLE`, `DOUBLE`, `TRIPLE`, `QUADRUPLE` |
| `DateType` | `ACTUAL`, `ESTIMATED` |
| `ReferenceType` | `BACKGROUND`, `RESULT`, `DERIVED` |
| `RecruitmentStatus` | `ACTIVE_NOT_RECRUITING`, `COMPLETED`, `ENROLLING_BY_INVITATION`, `NOT_YET_RECRUITING`, `RECRUITING`, `SUSPENDED`, `TERMINATED`, `WITHDRAWN`, `AVAILABLE` |
| `ContactRole` | `STUDY_CHAIR`, `STUDY_DIRECTOR`, `PRINCIPAL_INVESTIGATOR`, `SUB_INVESTIGATOR`, `CONTACT` |
| `ArmGroupType` | `EXPERIMENTAL`, `ACTIVE_COMPARATOR`, `PLACEBO_COMPARATOR`, `SHAM_COMPARATOR`, `NO_INTERVENTION`, `OTHER` |
| `EnrollmentType` | `ACTUAL`, `ESTIMATED` |

See the full enumeration table in the Study Data Structure source for all 40+ enum types including `MeasureParam`, `MeasureDispersionType`, `OutcomeMeasureType`, `ReportingStatus`, `EventAssessment`, `NonInferiorityType`, `BrowseLeafRelevance`, `WhoMasked`, `ViolationEventType`, and others.

### 3.8 Built-in Types

```typescript
/** Date in format: yyyy-MM-dd */
type NormalizedDate = string;

/** Date in one of the formats: yyyy, yyyy-MM, or yyyy-MM-dd */
type PartialDate = string;

/** DateTime in format: yyyy-MM-dd'T'HH:mm */
type DateTimeMinutes = string;

type NormalizedTime = string;

interface GeoPoint {
  lat: number;
  lon: number;
}
```

---

## 4. Query & Search System

### 4.1 Overview

ClinicalTrials.gov supports one search document type: **Study**. It contains **19 search areas**, each mapping to a `query.*` parameter or usable via the `AREA[]` operator.

### 4.2 The 19 Search Areas

| # | Search Area | Parameter | Fields | Purpose |
|---|---|---|---|---|
| 1 | **BasicSearch** | `query.term` | 57 | Default free-text search. Broad weighted search across most study fields. |
| 2 | **ConditionSearch** | `query.cond` | 7 | Condition/disease name search with MeSH term expansion. |
| 3 | **InterventionSearch** | `query.intr` | 12 | Drug/intervention name, type, and description search. |
| 4 | **InterventionNameSearch** | — | 2 | Narrow search: `InterventionName` (1.0) + `InterventionOtherName` (0.9) only. |
| 5 | **ObsoleteConditionSearch** | — | 4 | Older condition search area (condition + MeSH terms + keywords). |
| 6 | **ExternalIdsSearch** | — | 2 | Search by `OrgStudyId` and `SecondaryId`. |
| 7 | **ExternalIdTypesSearch** | — | 2 | Search by ID type enums (`OrgStudyIdType`, `SecondaryIdType`). |
| 8 | **EligibilitySearch** | — | 2 | Search `EligibilityCriteria` and `StudyPopulation` (markup fields). |
| 9 | **OutcomeSearch** | `query.outc` | 9 | Primary/secondary/other outcome measures and descriptions. |
| 10 | **OutcomeNameSearch** | — | 4 | Narrow outcome name search only. |
| 11 | **TitleSearch** | `query.titles` | 3 | `Acronym`, `BriefTitle`, `OfficialTitle`. |
| 12 | **LocationSearch** | `query.locn` | 5 | City, state, country, facility, zip. |
| 13 | **ContactSearch** | — | 4 | Official names, affiliations, contact names. |
| 14 | **NCTIdSearch** | — | 2 | `NCTId` (1.0) + `NCTIdAlias` (0.9). |
| 15 | **IdSearch** | `query.id` | 5 | All ID fields: NCT, alias, acronym, org study ID, secondary ID. |
| 16 | **SponsorSearch** | `query.spons` | 3 | `LeadSponsorName` (1.0), `CollaboratorName` (0.9), `OrgFullName` (0.6). |
| 17 | **FunderTypeSearch** | — | 2 | `LeadSponsorClass`, `CollaboratorClass` (AgencyClass enums). |
| 18 | **ResponsiblePartySearch** | — | 5 | Responsible party investigator names, affiliations, titles. |
| 19 | **PatientSearch** | `query.patient` | 47 | Patient-oriented broad search (similar to BasicSearch but with patient-facing weighting). |

Search areas without a dedicated `query.*` parameter can be targeted using the `AREA[]` operator in `query.term`:
```
AREA[EligibilitySearch]diabetes AND AREA[LocationSearch]California
```

### 4.3 Field Weighting

Each field within a search area has a numeric weight (0.0–1.0) that affects relevance scoring. Higher-weighted fields contribute more to result ranking.

**BasicSearch top weights:**

| Field | Weight |
|---|---|
| `NCTId` | 1.0 |
| `Acronym` | 1.0 |
| `BriefTitle` | 0.89 |
| `OfficialTitle` | 0.85 |
| `Condition` | 0.81 |
| `InterventionName` | 0.80 |
| `InterventionOtherName` | 0.75 |
| `Phase` | 0.65 |
| `StdAge` | 0.65 |
| `BriefSummary` | 0.60 |

Fields without a listed weight in the source material still participate in search but have unspecified/default weight.

### 4.4 Synonym Support

Fields marked with **✓** in the search area tables produce synonyms — the search engine automatically expands the query to include known synonyms (e.g., MeSH term synonyms for conditions and interventions).

Synonym-producing fields include: `BriefTitle`, `OfficialTitle`, `Condition`, `InterventionName`, `InterventionOtherName`, `BriefSummary`, `ArmGroupLabel`, `ArmGroupDescription`, `Keyword`, `EligibilityCriteria`, `StudyPopulation`, and all MeSH/ancestor term fields.

### 4.5 The SEARCH Operator

For nested structures where multiple fields must match **within the same nested object**, use the `SEARCH` operator:

```
SEARCH[Location](AREA[LocationCity]Florence AND AREA[LocationState]South Carolina AND AREA[LocationCountry]United States)
```

This ensures all three conditions match within a single location entry, not across different locations on the same study.

Fields marked with **⤷** in the data structure start nested documents that support the `SEARCH` operator. Key nested structures:
- `Location` (city + state + country + facility within one location)
- `Intervention` (name + type + description within one intervention)
- `ArmGroup`
- `OutcomeMeasure` (for results data)

### 4.6 Known Operator Limitations

> :warning: The **COVERAGE** and **EXPANSION** operators are **not fully implemented** on the modernized ClinicalTrials.gov. Do not rely on them.

---

## 5. Pagination & Bulk Retrieval

### 5.1 Pagination Mechanism

The API uses **token-based pagination** (not offset-based).

| Parameter | Description |
|---|---|
| `pageSize` | Number of studies per page. Default: 10. Max: 1000. |
| `pageToken` | Opaque token from the previous response's `nextPageToken` field. |
| `countTotal` | Set to `true` to include `totalCount` in the response. |

**Pattern:**
1. Make initial request without `pageToken`
2. Read `nextPageToken` from response
3. Pass it as `pageToken` in the next request
4. Repeat until `nextPageToken` is absent (no more pages)

### 5.2 Legacy `expr` Parameter Limit

On legacy endpoints (`/api/legacy/full-studies`, `/api/legacy/study-fields`), when the `expr` parameter is set, **only the first 10,000 studies can be retrieved**. This limit does not apply to the modern `/api/v2/studies` endpoint.

### 5.3 Bulk Download Options

| Method | Endpoint | Format | Coverage |
|---|---|---|---|
| **Full JSON archive** | `GET /api/v2/studies/download?format=json.zip` | ZIP of JSON files | All studies, all fields |
| **Paginated JSON** | `GET /api/v2/studies` with `pageSize=1000` | JSON | All studies via iteration, selectable fields |
| **Paginated CSV** | `GET /api/v2/studies` with `format=csv` | CSV | All studies via iteration, max 30 column groups |
| **Legacy full XML** | `GET /api/legacy/public-xml?format=zip` | ZIP of XML | All studies (legacy schema) |
| **Legacy API XML** | `GET /api/legacy/api-xml?format=zip` | ZIP of XML | All studies (FullStudies schema) |

### 5.4 CSV Download Columns

CSV format supports exactly **30 column groups** (some columns combine multiple fields):

| Column Name | Fields |
|---|---|
| NCT Number | `NCTId` |
| Study Title | `BriefTitle` |
| Study URL | derived from `NCTId` |
| Acronym | `Acronym` |
| Study Status | `OverallStatus` |
| Brief Summary | `BriefSummary` |
| Study Results | `HasResults` |
| Conditions | `Condition` |
| Interventions | `InterventionType`, `InterventionName` |
| Primary Outcome Measures | `PrimaryOutcomeMeasure`, `PrimaryOutcomeDescription`, `PrimaryOutcomeTimeFrame` |
| Secondary Outcome Measures | `SecondaryOutcomeMeasure`, `SecondaryOutcomeDescription`, `SecondaryOutcomeTimeFrame` |
| Other Outcome Measures | `OtherOutcomeMeasure`, `OtherOutcomeDescription`, `OtherOutcomeTimeFrame` |
| Sponsor | `LeadSponsorName` |
| Collaborators | `CollaboratorName` |
| Sex | `Sex` |
| Age | `MinimumAge`, `MaximumAge`, `StdAge` |
| Phases | `Phase` |
| Enrollment | `EnrollmentCount` |
| Funder Type | `LeadSponsorClass` |
| Study Type | `StudyType` |
| Study Design | `DesignAllocation`, `DesignInterventionModel`, `DesignMasking`, `DesignWhoMasked`, `DesignPrimaryPurpose` |
| Other IDs | `OrgStudyId`, `SecondaryId` |
| Start Date | `StartDate` |
| Primary Completion Date | `PrimaryCompletionDate` |
| Completion Date | `CompletionDate` |
| First Posted | `StudyFirstPostDate` |
| Results First Posted | `ResultsFirstPostDate` |
| Last Update Posted | `LastUpdatePostDate` |
| Locations | `LocationFacility`, `LocationCity`, `LocationState`, `LocationZip`, `LocationCountry` |
| Study Documents | `NCTId`, `LargeDocLabel`, `LargeDocFilename` |

9 columns are pre-selected by default: NCT Number, Study Title, Study URL, Study Status, Conditions, Interventions, Sponsor, Collaborators, Study Type.

### 5.5 JSON Download Presets

When downloading JSON via the UI:
- **All available** — every field in the study record
- **Most popular** — 8 pre-selected fields: NCT Number, Study Title, Study Status, Conditions, Interventions, Sponsor, Collaborators, Study Type
- **Custom set** — pick individual fields from the full nested structure

### 5.6 Strategies for Exhaustive Data Pulls

For pulling the entire database:
1. **Preferred:** Use `GET /api/v2/studies/download?format=json.zip` for a single bulk download.
2. **Incremental:** Paginate through `/api/v2/studies` with `pageSize=1000`, using date filters to partition (e.g., `filter.advanced` with date ranges on `LastUpdatePostDate`).
3. **By status:** Query each `OverallStatus` enum value separately to partition the dataset.

For monitoring updates:
- Compare `dataTimestamp` from `/api/v2/version` against your last sync time.
- Query studies by `LastUpdatePostDate` range to find changed records since your last pull.

---

## 6. Practical Patterns

### 6.1 Find All Studies for a Company/Sponsor

Use `query.spons` to search by sponsor name:
```
GET /api/v2/studies?query.spons=Pfizer&pageSize=1000
```

This searches `LeadSponsorName` (weight 1.0), `CollaboratorName` (0.9), and `OrgFullName` (0.6).

To distinguish lead sponsor from collaborator, request the `fields` parameter:
```
GET /api/v2/studies?query.spons=Pfizer&fields=NCTId,BriefTitle,LeadSponsorName,CollaboratorName
```

For funder type filtering (NIH, Industry, etc.), use the `FunderTypeSearch` area:
```
GET /api/v2/studies?query.term=AREA[FunderTypeSearch]INDUSTRY&query.spons=Pfizer
```

### 6.2 Find Studies by Condition/Disease Area

```
GET /api/v2/studies?query.cond=breast cancer&pageSize=100
```

The `ConditionSearch` area includes MeSH terms and ancestor terms with synonym expansion, so `breast cancer` will match studies using related terminology.

### 6.3 Find Studies by Intervention Type

```
GET /api/v2/studies?query.intr=pembrolizumab
```

For intervention type filtering:
```
GET /api/v2/studies?query.term=AREA[InterventionType]DRUG&query.cond=melanoma
```

### 6.4 Find Studies with Posted Results

Use the `HasResults` field:
```
GET /api/v2/studies?query.cond=diabetes&filter.advanced=AREA[HasResults]true&pageSize=100
```

### 6.5 Find Studies by Geographic Location

Simple location search:
```
GET /api/v2/studies?query.locn=United States
```

Multi-field location match using SEARCH operator (ensure city+state+country match within one location):
```
GET /api/v2/studies?query.term=SEARCH[Location](AREA[LocationCity]Boston AND AREA[LocationState]Massachusetts)
```

Geographic distance filter (if supported by `filter.geo`):
```
GET /api/v2/studies?filter.geo=distance(39.0035,-77.1013,50mi)
```

> :warning: **INFERRED:** The `filter.geo` parameter syntax is not fully documented in the source material. The distance-based syntax above is inferred from the parameter name and GeoPoint data type. Test before relying on specific syntax.

### 6.6 Monitor for New or Updated Studies

Check the data version first:
```
GET /api/v2/version
```

Then query for recently updated studies:
```
GET /api/v2/studies?filter.advanced=AREA[LastUpdatePostDate]RANGE[2026-04-14,MAX]&pageSize=1000
```

### 6.7 Retrieve a Full Study Record with All Nested Data

```
GET /api/v2/studies/NCT04280705
```

Omitting the `fields` parameter returns the complete record with all sections.

To get markup in legacy format:
```
GET /api/v2/studies/NCT04280705?markupFormat=legacy
```

---

## 7. Legacy & Migration Endpoints

### 7.1 Endpoint Mapping

| Classic Endpoint | v2 Replacement | Legacy Shim |
|---|---|---|
| `GET /api/info/data_vrs` | `/api/v2/version` (`dataTimestamp`) | Response from `/api/legacy/full-studies` (DataVrs tag) |
| `GET /api/info/api_vrs` | `/api/v2/version` (`apiVersion`) | Response from `/api/legacy/full-studies` (ApiVrs tag) |
| `GET /api/info/api_defs` | `/api/v2/studies/metadata`, `/api/v2/studies/search-areas`, `/api/v2/stats/field/values`, `/api/v2/stats/field/sizes` | — |
| `GET /api/info/study_structure` | `/api/v2/studies/metadata` | — |
| `GET /api/info/study_fields_list` | `/api/v2/studies/metadata` | `/api/legacy/study-fields-list` (XML only) |
| `GET /api/info/study_statistics` | `/api/v2/studies/metadata` + `/api/v2/stats/field/values` + `/api/v2/stats/field/sizes` | — |
| `GET /api/info/search_areas` | `/api/v2/studies/search-areas` | — |
| `GET /api/query/full_studies` | `/api/v2/studies` | `/api/legacy/full-studies` (XML, 10k limit w/ expr) |
| `GET /api/query/study_fields` | `/api/v2/studies` + `fields` param | `/api/legacy/study-fields` (XML, 10k limit w/ expr) |
| `GET /api/query/field_values` | `/api/v2/stats/field/values` + `/api/v2/studies` | — |
| `GET /ct2/show/{nctId}?displayxml=true` | `/api/v2/studies/{nctId}` | `/api/legacy/public-xml/{nctId}` |
| `GET /ct2/show/{nctId}?resultsxml=true` | `/api/v2/studies/{nctId}` | `/api/legacy/public-xml/{nctId}?full=true` |
| `GET /AllPublicXML.zip` | `/api/v2/studies/download?format=json.zip` | `/api/legacy/public-xml?format=zip` |
| `GET /AllAPIXML.zip` | `/api/v2/studies/download?format=json.zip` | `/api/legacy/api-xml?format=zip` |
| `GET /ct2/download_studies` | `/api/v2/studies` | `/api/legacy/public-xml?format=zip&term=...` |

### 7.2 Legacy Limitations

- Legacy endpoints support **XML only** (no JSON).
- `expr` parameter queries are limited to the **first 10,000 results**.
- Legacy `study-fields` does not include `FlowReasonNumUnits` or `OrgStudyIdDomain` (these contain no data in any study).
- Search expression syntax: use `AREA[SearchAreaName]term` and combine with `AND`/`OR` boolean operators.

---

## 8. Response Formats

### 8.1 RIS Format Tags

| Tag | Description | Source Fields |
|---|---|---|
| `TY` | Type of reference | Always `DBASE` |
| `DP` | Database provider | Always `National Library of Medicine (US)` |
| `PP` | Publishing place | Always `Bethesda (MD)` |
| `ID` | Unique identifier | `NCTId` |
| `U1` | Secondary ID | `SecondaryId`, `SecondaryIdType` |
| `AB` | Abstract/summary | `BriefSummary` |
| `AN` | NCT number | `NCTId` |
| `SF` | Subfile | Always `ClinicalTrials.gov` |
| `ST` | Short title | `BriefTitle`, `Acronym` |
| `TI` | Official title | `OfficialTitle` |
| `Y1` | First submitted date | `StudyFirstSubmitDate` |
| `Y2` | Study start date | `StartDate` |
| `A2` | Investigators | `CollaboratorName` |
| `C1` | Sponsor | `LeadSponsorName` |
| `C2` | Overall status | `OverallStatus` |
| `C3` | Last update posted | `LastUpdatePostDate` |
| `C4` | Last update submitted | `LastUpdateSubmitDate` |
| `C5` | Study type | `StudyType` + expanded access fields + `PatientRegistry` |
| `C6` | Has results | `HasResults`, `SubmissionInfo` |
| `C7` | Study documents | `LargeDocHasProtocol`, `LargeDocHasSAP`, `LargeDocHasICF` |
| `C8` | Central contact | `CentralContactName`, `CentralContactRole`, `CentralContactPhone`, `CentralContactPhoneExt`, `CentralContactEMail` |
| `RD` | Retrieved date | (auto-generated) |
| `UR` | Study URL | derived from `NCTId` |

### 8.2 FHIR Format

- **Status:** Pilot project.
- **Version:** FHIR R6.
- **Scope:** Single study download only (not available for bulk/search results).
- **Resource type:** `ResearchStudy` with referenced `Citation`, `Evidence`, `EvidenceVariable`, `Composition`, `Practitioner`, `PractitionerRole`, `Organization`, `Location`, and `Group` resources.
- **Access:** Download button on individual study record pages, or direct API call.
- **External viewer:** [FEvIR Platform](https://fevir.net/) for human-readable rendering.

### 8.3 Markup Format Control

The `markupFormat` parameter on `/api/v2/studies` and `/api/v2/studies/{nctId}` controls how markup fields are rendered:

| Value | Description |
|---|---|
| `markdown` (default) | CommonMark markdown format |
| `legacy` | Legacy HTML-subset format ("chintzy" format) |

> :warning: As of the August 26, 2025 modernization, markup fields from the new data pipeline may not have identical formatting to the classic pipeline even when `markupFormat=legacy` is used. See GOTCHAS doc for details.
