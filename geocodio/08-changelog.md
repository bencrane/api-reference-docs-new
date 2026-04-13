# Changelog | Geocodio API

The Geocodio API is continuously improved. Most updates require no changes for API users, but in some cases breaking changes are introduced.

Breaking changes are introduced with new API versions, allowing you to upgrade at your own pace. Older API versions are guaranteed to be available for at least 12 months after they have been replaced by a newer version, but may be supported for longer.

Breaking changes are defined as changes that remove or rename properties in the JSON output of any API endpoint. Your API client should be able to gracefully support addition of new JSON properties, as this is not considered a breaking change.

---

## v1.12

**Released on March 24, 2026**

- **Breaking:** Mexican addresses are now formatted as `<street> <house number>`, matching the correct local convention. Previous API versions returned the house number before the street name.

## v1.11

**Released on March 11, 2026**

- Secondary address line geocoding is now supported at the unit level. When a secondary address component is provided (e.g. apartment, suite, or unit number), Geocodio will attempt to return unit-specific coordinates. Different units at the same street address may now return different coordinates.
- All geocoding results now include a `match_type` field that indicates the coordinate match granularity. Possible values are `building_centroid`, `parcel_centroid`, `unit`, and `null`.
- **Breaking:** Stable address keys now include a unit suffix for addresses with secondary address components (e.g. `gcod_usnbfvbm5l57cc8b8bnfnyrua9ym3-a1b2c3`). The full key with unit suffix can be used as input for geocoding and distance calculations.

## v1.10

**Released on March 11, 2026**

- Added forward geocoding support for Mexico.
- Updated `ffiec` field append to 2025 FFIEC data release (using 2024 Census geographies).

**Released on March 2, 2026**

- Added `skipGeocoding` parameter for reverse geocoding endpoints. This allows applying field appends directly to coordinates without performing a geocoding lookup, so only field append lookups are billed.

**Released on February 24, 2026**

- **Breaking:** ACS 2024 data is now returned for all Census ACS appends. ACS 2024 uses 2023 Census boundaries (the `census2023` data append). Changes include:
  - The `acs-social` field append has renamed row labels in Table #B21002 (Period of military service for veterans): "Vietnam Era" has been changed to "Vietnam War".
  - No other ACS field appends have breaking table changes.
- `cd120`: Updated with redistricted boundaries for California, Missouri, North Carolina, Ohio, and Utah.
- All geocoding results now include a stable address key (`stable_address_key`) that uniquely identifies an address. Stable address keys can be used as input in any API endpoint and enable free field appends on already-geocoded addresses.

## v1.9

**Released on January 6, 2026**

- Added new Distance endpoints for calculating distances and travel times between locations:
  - New `/distance` endpoint for single origin to multiple destinations.
  - New `/distance-matrix` endpoint for multiple origins to multiple destinations (up to 10,000 calculations).
  - New `/distance-jobs` endpoints for asynchronous large-scale distance calculations (up to 50,000 calculations).
  - Distance calculations can also be added to geocoding results via the `destinations[]` parameter on `/geocode` and `/reverse` endpoints.

**Released on December 16, 2025**

- The `census2025` field append is now available (the `census` data append will now default to `census2025`).

**Released on November 19, 2025**

- Added Google Maps API compatibility endpoint at `/maps/api/geocode/json`. This allows developers to migrate from Google Maps by using existing Google Maps SDKs with Geocodio by simply changing the endpoint and API key.

**Released on November 18, 2025**

- The `cd120` field has been added for the 120th Congress. It remains in preview until finalized. `cd119` continues to be the default.

**Released on June 17, 2025**

- **Breaking:** State legislative district names and numbers have been standardized. The changes do not apply to API versions below v1.9 and OCD ids are not affected.
- The lists API endpoint now includes the updated header names recently introduced to the spreadsheet geocoding tool as well as state legislator data.

## v1.8

**Released on June 6, 2025**

- The state legislative districts field append now returns the current legislators for the district.
- The congressional districts field append now returns a `photo_url` along with each legislator.

**Released on June 2, 2025**

- Updated state legislative districts for North Dakota.

**Released on May 16, 2025**

- **Breaking:** 2023 data is now returned for all Census ACS appends. Changes include:
  - 2023 Census boundaries and ACS data are returned instead of 2021.
  - The `acs-families` field append has certain table titles renamed ("wife" or "husband" replaced with "spouse"). No other ACS field appends have renamed tables.
  - Support for additional Census Geographies (prior to v1.8 all ACS data was returned at the Census Block Group level). The geography is now automatically selected based on the `accuracy_type` of the result and can be explicitly specified.
  - ACS Table #B19301 was added for the `acs-economics` field append.
  - ACS Tables #B11003, #B25010, and #B09002 were added for the `acs-families` field append.
- No other breaking changes for v1.8.

## v1.7

**Released on May 6, 2025**

- Added `address_lines` along with each geocoding result.

**Released on March 25, 2025**

- Added new `ffiec` field append.

**Released on March 24, 2025**

- The Canadian elections have been called. `riding` now returns the new, redistricted ridings. `riding-next` continues to return the redistricted ridings as well, but is otherwise no longer in use.

**Released on March 10, 2025**

- Added the ability to use the `Authorization` header for API authentication.
- List geocoding is now available for Geocodio Enterprise.

**Released on February 27, 2025**

- The `current_legislators` data for the `cd` field append now returns sorted legislators. The representative is always returned first, senators are then returned sorted by seniority. A new `seniority` key can be used to determine if a senator is senior or junior (the value is `null` for representatives).

**Released on January 17, 2025**

- Added support for `street2` and `county` as input address components. Available for both single geocoding and batch geocoding.

**Released on January 9, 2025**

- The `census2024` field append is now available (the `census` data append will now default to `census2024`).
- The senate districts for California have been updated with new post-election boundaries.

**Released on December 16, 2024**

- The `cd119` field append has been added for the 119th Congress. This becomes the default congressional district append starting on January 3rd, 2025.

**Released on November 4, 2024**

- The `zip4` field append now returns a residential delivery indicator (RDI) with the new `residential` property.

**Released on September 27, 2024**

- The `provriding-next` data append is now available. Upcoming provincial ridings for Saskatchewan can be previewed. The `provriding` will return these new ridings as of 10/28/2024.

**Released on September 20, 2024**

- `provriding`: New district boundaries are now used for British Columbia.

**Released on April 29, 2024**

- `stateleg-next`: Upcoming district boundaries were added for Minnesota House and Senate districts, to be promoted to `stateleg` on 1/14/2025.

**Released on April 24, 2024**

- Added Census County Subdivisions to the `census` field append.

**Released on April 16, 2024**

- `cd118`: District boundaries were updated for North Carolina, Louisiana, and New York.
- `stateleg`: Wisconsin and Michigan House district boundaries were updated. New Mexico Senate district boundaries were updated.
- `stateleg-next`: Upcoming district boundaries were added for New York Assembly (promoted to `stateleg` on 1/1/2025), Ohio House and Senate (promoted 1/1/2025), and Washington House and Senate (promoted 8/6/2024).

**Released on April 8, 2024**

- Introduced `riding-next` for federal electoral district lookups in Canada based on redistricting ridings.

**Released on January 18, 2024**

- Introduced `census2023` data append (the `census` data append will now default to `census2023`).
- Corrected an issue where census field appends always returned county FIPS codes for the most recent census year. This primarily affects census county lookups in Connecticut.

**Released on November 8, 2023**

- Updated state legislative districts for North Carolina.

**Released on August 14, 2023**

- Corrected an issue that caused batch geocoding requests to only return results from the first country when addresses from mixed countries were present in a single batch.

**Released on April 26, 2023**

- Added upcoming redistricted boundaries for Montana with the `stateleg-next` data append.
- Corrected boundaries for current senate state legislative districts for California.
- Updated Statistics Canada data to latest 2021 census release with additional values: Designated place, Population centre, Dissemination area, Dissemination block.

**Released on March 14, 2023**

- Updated Alaska state legislative district boundaries.

**Released on February 7, 2023**

- Corrected version of state legislative districts returned for NM State Senate, KS State Senate, and SC State Senate.
- Redistricted state boundaries can still be requested early by using the `stateleg-next` data append.

**Released on February 1, 2023**

- Corrected version of state legislative districts returned for New Mexico Senate.
- Corrected Massachusetts state legislative district OCD ids.

**Released on January 23, 2023**

- Updated congressional district and state legislative district boundaries for Wisconsin.
- Corrected an issue where 4th Middlesex and 5th Middlesex in Massachusetts returned an incorrect OCD id.

**Released on January 17, 2023**

- Census ACS data updated to the latest release (2021 ACS data).
- The `ocd_id` value is now set for all `stateleg` district results (previously, it was `null` for pre-redistricting districts).

**Released on January 11, 2023**

- Introduced `census2022` data append (the `census` data append will now default to `census2022`).
- `stateleg` data append now returns redistricted boundaries for all states except MS, NJ, LA, MT, and VA. For these states, use `stateleg-next` to get redistricted data instead.

**Released on May 19, 2022**

- The `stateleg-next` and `cd118` field appends now return OCD identifiers.

**Released on March 7, 2022**

- When using the `stateleg-next` data append, the `is_upcoming_state_legislative_district` property now returns `false` when the state's data has not been updated yet.

**Released on February 11, 2022**

- Added the new `provriding` field append for provincial/territorial legislative districts in Canada.

**Released on February 10, 2022**

- The `cd118` and `stateleg-next` data appends updated with districts for California, Massachusetts, and Virginia.

**Released on January 17, 2022**

- Introduced `census2021` data append (the `census` data append will now default to `census2021`).

**Released on January 13, 2022**

- Introduced `census2000` data append for 2000 vintage census boundaries.
- Updated `cd118` and `stateleg-next` data appends with data for additional redistricted states.

**Released on November 12, 2021**

- **Breaking:** The `state_legislative_districts` key from the `stateleg` field append now returns an array of house and senate districts instead of a single object.
- The `stateleg-next` field append returns a preview of upcoming state legislative district changes.
- `stateleg` and `stateleg-next` can now return all districts that intersect with a zip code boundary along with the proportion of overlap.
- `cd118` has been added as a field append, returning districts for the upcoming 118th Congress.

## v1.6

**Released on September 15, 2021**

- Introduced the `format` parameter for single forward and reverse geocoding requests.

**Released on June 16, 2021**

- Counties can now be geocoded in the U.S., either standalone or as part of an address.

**Released on March 1, 2021**

- `stateleg` now returns the same data as `stateleg-next`. `stateleg-next` may be used again for future legislative district changes.

**Released on February 25, 2021**

- Introduced `census2020` data append (the `census` data append will now default to `census2020`).
- Updated all Census ACS data to most recent 5-year release (2015-2019).

**Released on May 28, 2020**

- **Breaking:** Fixes a bug with backwards-incompatible consequences for `acs-families` and `acs-demographics` field appends.
- Non-breaking: The `acs-social` table, Population with veteran status (Table B21001) now includes age breakdowns.
- The following ACS data tables have titles changed and/or values corrected:
  - `acs-families`: Household type by household (Table B11001), Household type by population (Table B11002), Marital status (Table B12001).
  - `acs-demographics`: Race and ethnicity (Table B03002).

## v1.5

**Released on May 13, 2020**

- **Breaking:** PO Box and second address lines (e.g. apartment/unit/suite numbers) are now returned as results and appear within the `formatted_address` keys.
- The `zip4` data append is now generally available.

## v1.4

**Released on September 18, 2019**

- `census` appends:
  - **Breaking:** The census append now supports vintage years. Data is keyed by year instead of returning a single year.

## v1.3

**Released on March 12, 2018**

- `timezone` appends:
  - **Breaking:** `name` property has been renamed to `abbreviation`.
  - `name` is now the full timezone name in a tzdb-compatible format.

## v1.2

**Released on January 20, 2018**

- `cd` (Congressional district) appends:
  - **Breaking:** `current_legislator` property has been renamed to `current_legislators` and is now an array instead of an object.
  - Both house and senate legislators are now returned.

## v1.1

**Released on January 8, 2018**

- `cd` (Congressional district) appends:
  - **Breaking:** `congressional_district` property has been renamed to `congressional_districts`.
  - **Breaking:** Postal code lookups now return multiple Congressional districts if the zip code area spans more than one district.
  - Current legislator information is now returned with Congressional districts.
