# Online Presence

## Description
Indicates whether a website is an e-commerce website that sells products directly online.

## Tier
Core

## Applies To
- Brand
- Operating Location

## Data Source
Publicly accessible business websites that Enigma analyzes directly.

## Key Details
Data represents the latest available information rather than tracking changes over time. Uses multiple analytical approaches to detect shopping functionality indicators.

## Data Fields

| Field | Type | Description |
|-------|------|-------------|
| hasOnlineSales | String | "Yes" or null (insufficient data) |
| id | UUID | Unique identifier |
| firstObservedDate | String | Date first observed |
| lastObservedDate | String | Date last observed |

## Source
https://documentation.enigma.com/reference/attributes/website-online-presence
