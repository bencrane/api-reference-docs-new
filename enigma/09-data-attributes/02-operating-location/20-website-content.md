# Website Content

## Description
The state of the website at a particular time.

## Tier
Plus

## Applies To
- Brand
- Operating Location

## Key Details
Enigma requests each website at minimum every 90 days. Each object represents findings from a single request.

## Historical Tracking
- **Rank 0** = Most recent website request
- **Higher ranks** = Earlier requests

Enables tracking of changes like when sites became unavailable or underwent rebranding.

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| faviconImage | String | Binary favicon representation from HTTP response |
| faviconUrl | String | URL where favicon was served |
| httpStatusCode | Integer | HTTP response code (e.g., 200, 404) |
| websiteAvailability | String | Availability status |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Source
https://documentation.enigma.com/reference/attributes/website-content
