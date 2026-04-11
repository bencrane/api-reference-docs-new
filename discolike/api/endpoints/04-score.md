# Score API [Starter]

## Overview

The Score API delivers a composite score (0-800, higher is better) for any domain, reflecting company size, time in business, and technology adoption. Based on ten years of SSL certificate history. Subdomains are automatically normalized.

Use alongside [BizData](../bizdata/) for full firmographic profiles and [Growth](../growth/) for quarter-over-quarter changes.

## Methodology

### Score Components

The scoring mechanism combines four distinct elements:

| Component | Description |
|-----------|-------------|
| **Base Score (β)** | Accumulated points from 10 years of certificate history, weighted by market and time |
| **Recency Multiplier (ε)** | Ranges 0-1; penalizes domains where all certificates are very recent |
| **Growth Boost (φ)** | Positive if certificate activity increased year-over-year, negative if declined |
| **Expiration Penalty (λ)** | Reduces score when certificates are within 14 days of expiring |

### How It Works

**1. Base Score** — For each of the past 10 years, we calculate how many certificates were issued compared to the expected baseline for the market. More certificates = more points, with a cap at 100% of baseline.

**2. Recency Check** — If all certificates were issued within the current year, the score is reduced proportionally. A domain with 3+ years of history gets the full score.

**3. Growth Adjustment** — We compare certificate activity from the past 360 days against the prior 360 days (720-360 days ago). Growing companies get a boost; declining activity results in a penalty.

**4. Expiration Penalty** — If certificates are about to expire (within 14 days), the final score is reduced to reflect potential domain inactivity.

### Final Calculation

```
Final Score = (Base Score × Recency Multiplier + Growth Boost) × Expiration Penalty
```

## Endpoint

```
GET https://api.discolike.com/v1/score
```

## Parameters

| Parameter | Description |
|-----------|-------------|
| domain | Domain to investigate. |

## Response Fields

| Field | Format | Description |
|-------|--------|-------------|
| domain | String | Normalized domain name (excluding any subdomain). |
| score | Unsigned Int32 | Final calculated score. |
| first_event | Date (YYYY-MM-DD) | Date of first registration event. |
| confidence | Decimal (1,2) | Confidence score for classification label. |
| parameters | Array[ParameterObjects] | Set of calculation parameters as described in the parameters section. |
| base_score | Decimal (3,2) | The baseline score for the domain provided over 10 years (β). |
| recency_multiplier | Decimal(1,2) | Decreases score in case of all company certificates were created in the current year (ε). |
| growth_boost | Decimal(3,2) | Increases score if the number of certificates opened in the last 360 days is greater than those opened 2 years before or decreases one if vice versa (φ). |
| expiration_penalty | Decimal(1,2) | Decreases score in case of the average expiration period of currently active certificates is less than λd (λ). |
| lookback_360 | Unsigned Int32 | Number of certificates generated in the past 360 days (Ω360). |
| lookback_720 | Unsigned Int32 | Number of certificates generated between 720 and 360 days (Ω720). |

## Example Request

```bash
curl "https://api.discolike.com/v1/score?domain=acmecorp.com" \
  -H "x-discolike-key: API_KEY"
```

## Example Response

```json
{
  "domain": "acmecorp.com",
  "score": 657,
  "parameters": {
    "base_score": 700,
    "recency_multiplier": 1,
    "growth_boost": -42.78,
    "lookback_360": 14796,
    "lookback_720": 190199,
    "expiration_penalty": 1
  },
  "first_event": "2010-03-01"
}
```
