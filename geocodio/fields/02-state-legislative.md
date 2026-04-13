# State Legislative Districts | Geocodio API

**Field name:** `stateleg` or `stateleg-next`

**Coverage:** US only

Returns state legislative districts (house and senate) along with current legislator information for an address or coordinate pair.

- `stateleg` returns districts based on current boundaries.
- `stateleg-next` returns districts based on upcoming redistricted boundaries (preview of off-year election changes).

## Request

```bash
curl "https://api.geocod.io/v1.12/geocode?q=1109+N+Highland+St%2C+Arlington+VA&fields=stateleg&api_key=YOUR_API_KEY"
```

```bash
curl "https://api.geocod.io/v1.12/reverse?q=38.886672,-77.094735&fields=stateleg&api_key=YOUR_API_KEY"
```

## Response

```json
{
  "fields": {
    "state_legislative_districts": {
      "house": [
        {
          "name": "2nd District",
          "district_number": "2",
          "ocd_id": "ocd-division/country:us/state:va/sldl:2",
          "is_upcoming_state_legislative_district": false,
          "proportion": 1,
          "current_legislators": [
            {
              "type": "representative",
              "bio": {
                "last_name": "McClure",
                "first_name": "Adele",
                "birthday": null,
                "gender": "F",
                "party": "Democrat",
                "photo_url": "https://memdata.virginiageneralassembly.gov/images/display_image/H0375"
              },
              "contact": {
                "url": "https://house.vga.virginia.gov/members/H0375",
                "address": "Room 1102, General Assembly Building 201 N. 9th St., Richmond, VA 23219",
                "phone": "804-698-1002",
                "email": "delamcclure@house.virginia.gov",
                "contact_form": null
              },
              "social": {
                "rss_url": null,
                "twitter": null,
                "facebook": null,
                "youtube": null,
                "youtube_id": null
              },
              "references": {
                "votesmart_id": "212037",
                "ballotpedia_id": "Adele_McClure",
                "wikipedia_id": "Adele_McClure",
                "openstates_id": "ocd-person/d0de7acb-ce8d-4bb2-b6e5-99cefe5e76a6"
              },
              "source": "Legislator data collected by Open States (https://github.com/openstates/)"
            }
          ]
        }
      ],
      "senate": [
        {
          "name": "District 40",
          "district_number": "40",
          "ocd_id": "ocd-division/country:us/state:va/sldu:40",
          "is_upcoming_state_legislative_district": false,
          "proportion": 1,
          "current_legislators": [
            {
              "type": "senator",
              "bio": {
                "last_name": "Favola",
                "first_name": "Barbara",
                "birthday": "1955-06-21",
                "gender": "F",
                "party": "Democrat",
                "photo_url": "https://apps.senate.virginia.gov/Senator/images/member_photos/Favola40"
              },
              "contact": {
                "url": "https://apps.senate.virginia.gov/Senator/memberpage.php?id=S86",
                "address": "Room 509, General Assembly Building P.O. Box 396, Richmond, VA 23218",
                "phone": "804-698-7540",
                "email": "senatorfavola@senate.virginia.gov",
                "contact_form": null
              },
              "social": {
                "rss_url": null,
                "twitter": "BarbaraFavola",
                "facebook": "BarbaraFavola",
                "youtube": null,
                "youtube_id": null
              },
              "references": {
                "votesmart_id": "94043",
                "ballotpedia_id": "Barbara_Favola",
                "wikipedia_id": "Barbara_Favola",
                "openstates_id": "ocd-person/72ecc30c-7175-4aef-9762-fda3ba5b451e"
              },
              "source": "Legislator data collected by Open States (https://github.com/openstates/)"
            }
          ]
        }
      ]
    }
  }
}
```

## Response Fields

| Field | Description |
|---|---|
| `house` | Array of state house (lower chamber) districts |
| `senate` | Array of state senate (upper chamber) districts |
| `name` | Full name of the legislative district |
| `district_number` | District number |
| `ocd_id` | Open Civic Data Division Identifier for the district |
| `is_upcoming_state_legislative_district` | Whether this is a future redistricted district |
| `proportion` | Decimal percentage of district overlap (relevant for ZIP code lookups) |
| `current_legislators` | Array of current legislators for the district |

## Notes

- For unicameral legislatures (Washington DC, Nebraska), the `house` and `senate` keys return the same district.
- For at-large districts (Washington DC, Puerto Rico), at-large legislators are returned for all districts but listed last.
- OCD-IDs are returned for all legislative districts and can be used as unique identifiers.
- Legislator data is sourced from Open States.

## Using stateleg-next

`stateleg-next` previews upcoming redistricting changes for states with off-year elections. Where available, the returned districts are based on newly redistricted boundaries.

```bash
curl "https://api.geocod.io/v1.12/geocode?q=1109+N+Highland+St%2C+Arlington+VA&fields=stateleg-next&api_key=YOUR_API_KEY"
```

## ZIP Code Lookups

When looking up by ZIP code, multiple districts may be returned per chamber, ranked by `proportion` (descending). Use full addresses for best accuracy.

```json
{
  "state_legislative_districts": {
    "house": [
      { "name": "State House District 49", "district_number": "49", "proportion": 0.532 },
      { "name": "State House District 45", "district_number": "45", "proportion": 0.453 },
      { "name": "State House District 46", "district_number": "46", "proportion": 0.015 }
    ],
    "senate": [
      { "name": "State Senate District 30", "district_number": "30", "proportion": 1 }
    ]
  }
}
```
