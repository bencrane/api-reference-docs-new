# Statistics Canada Boundaries | Geocodio API

**Field name:** `statcan`

**Coverage:** Canada only

Returns Statistics Canada geographic boundaries for a Canadian address or coordinate pair, including census divisions, subdivisions, dissemination areas/blocks, economic regions, and more.

## Request

```bash
curl "https://api.geocod.io/v1.12/geocode?q=300+King+St%2C+Sturgeon+Falls%2C+ON+P2B+3A1%2C+Canada&fields=statcan&api_key=YOUR_API_KEY"
```

```bash
curl "https://api.geocod.io/v1.12/reverse?q=46.225866,-79.36316&fields=statcan&api_key=YOUR_API_KEY"
```

## Response

```json
{
  "fields": {
    "statcan": {
      "division": {
        "id": "3548",
        "name": "Nipissing",
        "type": "DIS",
        "type_description": "District"
      },
      "consolidated_subdivision": {
        "id": "3548055",
        "name": "West Nipissing / Nipissing Ouest"
      },
      "subdivision": {
        "id": "3548055",
        "name": "West Nipissing / Nipissing Ouest",
        "type": "M",
        "type_description": "Municipality / Municipalite\u0301"
      },
      "economic_region": "Northeast / Nord-est",
      "statistical_area": {
        "code": "997",
        "code_description": "Moderate",
        "type": "5",
        "type_description": "Census subdivision outside of census metropolitan area/census agglomeration area having moderate metropolitan influence"
      },
      "cma_ca": {
        "id": "997",
        "name": "Moderate metropolitan influenced zone (Ont.) / Zone d'influence m\u00e9tropolitaine mod\u00e9r\u00e9e (Ont.)",
        "type": "H",
        "type_description": "Not applicable (outside of CMA or CA)"
      },
      "tract": null,
      "designated_place": null,
      "population_centre": {
        "id": "350901",
        "name": "Sturgeon Falls",
        "type": "4",
        "type_description": "Population centre outside of a census metropolitan area or census agglomeration",
        "class": "2",
        "class_description": "Small population centre (1,000 to 29,999)"
      },
      "dissemination_area": {
        "id": "35480186"
      },
      "dissemination_block": {
        "id": "35480186023",
        "population": "458"
      },
      "census_year": 2021
    }
  }
}
```

## Response Fields

### Division (Census Division)

One of the largest Census-designated geographies.

| Field | Description |
|---|---|
| `id` | Census division ID |
| `name` | Division name |
| `type` | Type code |
| `type_description` | Description (e.g., "District", "County", "Region") |

### Consolidated Subdivision

A geographic unit between divisions and subdivisions in size, combining adjacent census subdivisions.

| Field | Description |
|---|---|
| `id` | Consolidated subdivision ID |
| `name` | Name |

### Subdivision (Census Subdivision)

Generally corresponds to a municipality.

| Field | Description |
|---|---|
| `id` | Subdivision ID |
| `name` | Name |
| `type` | Type code |
| `type_description` | Description (e.g., "Town", "Village", "Municipality", "City") |

### Economic Region

Name of the economic region. Economic regions are mostly groupings of complete census divisions, created for analysis of regional economic activity.

### Statistical Area

Groups census subdivisions based on their CMA/CA type.

| Field | Description |
|---|---|
| `code` | Statistical area code |
| `code_description` | Description of the code |
| `type` | Type number |
| `type_description` | Description of the type |

### CMA/CA (Census Metropolitan Area or Census Agglomeration)

| Field | Description |
|---|---|
| `id` | CMA/CA ID |
| `name` | Full name |
| `type` | Type code |
| `type_description` | "Census metropolitan area (CMA)", "Census agglomeration (CA) that is not tracted", or "Census agglomeration (CA) that is tracted" |

### Tract

The full Canadian census tract code. Returns `null` if not applicable.

### Designated Place

A small community or settlement that does not meet Statistics Canada's requirements for a census subdivision or population centre. Returns `null` if not applicable.

| Field | Description |
|---|---|
| `id` | Designated place ID |
| `name` | Name |

### Population Centre

Population centres have a population of at least 1,000 and a density of 400+ persons per square kilometre.

| Field | Description |
|---|---|
| `id` | Population centre ID |
| `name` | Name |
| `type` | Type code |
| `type_description` | Description of the type |
| `class` | Class code |
| `class_description` | "Small population centre (1,000 to 29,999)", "Medium population centre (30,000 to 99,999)", "Large urban population centre (100,000+)", or "Rural area" |

### Dissemination Area and Dissemination Block

The dissemination area is geographically one step below census tracts. Dissemination blocks are one step below dissemination areas.

| Field | Description |
|---|---|
| `dissemination_area.id` | Dissemination area ID |
| `dissemination_block.id` | Dissemination block ID |
| `dissemination_block.population` | Population of the dissemination block |

### Census Year

The year of the Census data used (e.g., `2021`).

## Notes

- If a given geography does not apply to the query, `null` is returned instead of the geography object.
- For US Census data, see the `census` field append.
- These boundaries can be matched with data from Statistics Canada to retrieve further census information such as demographics.
