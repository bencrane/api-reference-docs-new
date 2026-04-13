# Congressional Districts | Geocodio API

**Field name:** `cd`, `cd113`, `cd114`, `cd115`, `cd116`, `cd117`, `cd118`, `cd119`, `cd120`

**Coverage:** US only

Returns the Congressional district and current legislator information for an address or coordinate pair.

- `cd` always returns the district for the **current** Congress.
- Versioned fields (e.g., `cd113`, `cd119`) return the district for that specific Congress number.
- Detailed legislator information is only included when requesting the current Congress (`cd` or the current numbered version).

## Request

```bash
curl "https://api.geocod.io/v1.12/geocode?q=1109+N+Highland+St%2C+Arlington+VA&fields=cd&api_key=YOUR_API_KEY"
```

```bash
curl "https://api.geocod.io/v1.12/reverse?q=38.886672,-77.094735&fields=cd&api_key=YOUR_API_KEY"
```

## Response

```json
{
  "fields": {
    "congressional_districts": [
      {
        "name": "Congressional District 8",
        "district_number": 8,
        "ocd_id": "ocd-division/country:us/state:va/cd:8",
        "congress_number": "119th",
        "congress_years": "2025-2027",
        "proportion": 1,
        "current_legislators": [
          {
            "type": "representative",
            "seniority": null,
            "bio": {
              "last_name": "Beyer",
              "first_name": "Donald",
              "birthday": "1950-06-20",
              "gender": "M",
              "party": "Democrat",
              "photo_url": "https://www.congress.gov/img/member/b001292_200.jpg",
              "photo_attribution": "Image courtesy of the Member"
            },
            "contact": {
              "url": "https://beyer.house.gov",
              "address": "1226 Longworth House Office Building Washington DC 20515-4608",
              "phone": "202-225-4376",
              "contact_form": null
            },
            "social": {
              "rss_url": null,
              "twitter": "RepDonBeyer",
              "facebook": "RepDonBeyer",
              "youtube": null,
              "youtube_id": "UCPJGVbOVcAVGiBwq8qr_T9w"
            },
            "references": {
              "bioguide_id": "B001292",
              "thomas_id": "02272",
              "opensecrets_id": "N00036018",
              "lis_id": null,
              "cspan_id": "21141",
              "govtrack_id": "412657",
              "votesmart_id": "1707",
              "ballotpedia_id": "Don Beyer",
              "washington_post_id": null,
              "icpsr_id": "21554",
              "wikipedia_id": "Don Beyer"
            },
            "source": "Legislator data collected by the @unitedstates project (https://github.com/unitedstates/)"
          },
          {
            "type": "senator",
            "seniority": "senior",
            "bio": { ... },
            "contact": { ... },
            "social": { ... },
            "references": { ... },
            "source": "..."
          },
          {
            "type": "senator",
            "seniority": "junior",
            "bio": { ... },
            "contact": { ... },
            "social": { ... },
            "references": { ... },
            "source": "..."
          }
        ]
      }
    ]
  }
}
```

## Response Fields

| Field | Description |
|---|---|
| `name` | Full name of the Congressional district |
| `district_number` | District number. `0` for at-large states (e.g., Vermont). `98` for non-voting delegates (e.g., Washington DC). |
| `ocd_id` | Open Civic Data Division Identifier. Returned for `cd119` and `cd120`; `null` for earlier periods. |
| `congress_number` | Congress number (e.g., "119th") |
| `congress_years` | Year range for the Congress (e.g., "2025-2027") |
| `proportion` | Decimal percentage of district overlap (relevant for ZIP code lookups) |
| `current_legislators` | Array of legislators. Representative listed first, then senators. Only included for current Congress. |

## Legislator Object

Each legislator includes:

| Field | Description |
|---|---|
| `type` | `"representative"` or `"senator"` |
| `seniority` | `"senior"`, `"junior"`, or `null` (for representatives) |
| `bio` | Name, birthday, gender, party, photo URL |
| `contact` | Website URL, office address, phone, contact form |
| `social` | Twitter, Facebook, YouTube, RSS |
| `references` | IDs for Bioguide, GovTrack, VoteSmart, Ballotpedia, Wikipedia, etc. |

## ZIP Code Lookups

When looking up by ZIP code, multiple Congressional districts may be returned, ranked by `proportion` (descending). The proportion represents how much of the district boundary intersects with the ZIP code boundary.

For best accuracy, use full addresses rather than ZIP codes, since ZIP codes are postal routes rather than geographic areas.
