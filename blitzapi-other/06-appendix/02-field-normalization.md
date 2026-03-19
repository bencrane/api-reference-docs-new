> ## Documentation Index
> Fetch the complete documentation index at: https://docs.blitz-api.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Field Normalization

> Accepted values for industry, employee range, job level, job function, company type, sales region, and country codes. All values are case-sensitive.

BlitzAPI Search endpoints (Company Search, Employee Finder, Waterfall ICP) use **normalized values** for categorical filters. Passing an incorrect value (e.g., `"SaaS"` instead of `"Software Development"`) will silently return 0 results.

<Warning>
  All enum values are **case-sensitive** and must match exactly. Copy-paste from this page to avoid typos.
</Warning>

***

## Employee Range

Used in: **Company Search** (`employee_range` filter)

| Value          | Headcount                  |
| :------------- | :------------------------- |
| `"1-10"`       | 1–10 employees             |
| `"11-50"`      | 11–50 employees            |
| `"51-200"`     | 51–200 employees           |
| `"201-500"`    | 201–500 employees          |
| `"501-1000"`   | 501–1,000 employees        |
| `"1001-5000"`  | 1,001–5,000 employees      |
| `"5001-10000"` | 5,001–10,000 employees     |
| `"10001+"`     | More than 10,000 employees |

***

## Job Levels

Used in: **Employee Finder** (`job_level` filter)

| Value        | Description                                    |
| :----------- | :--------------------------------------------- |
| `"C-Team"`   | C-Level executives (CEO, CTO, CFO, CMO, CRO…)  |
| `"VP"`       | Vice Presidents                                |
| `"Director"` | Directors                                      |
| `"Manager"`  | Managers                                       |
| `"Staff"`    | Individual contributors, specialists, analysts |
| `"Other"`    | Roles that don't fit the above categories      |

***

## Job Functions

Used in: **Employee Finder** (`job_function` filter)

<Accordion title="View all accepted job function values (22)">
  | Job Function                                |
  | :------------------------------------------ |
  | `"Advertising & Marketing"`                 |
  | `"Art, Culture and Creative Professionals"` |
  | `"Construction"`                            |
  | `"Customer/Client Service"`                 |
  | `"Education"`                               |
  | `"Engineering"`                             |
  | `"Finance & Accounting"`                    |
  | `"General Business & Management"`           |
  | `"Healthcare & Human Services"`             |
  | `"Human Resources"`                         |
  | `"Information Technology"`                  |
  | `"Legal"`                                   |
  | `"Manufacturing & Production"`              |
  | `"Operations"`                              |
  | `"Other"`                                   |
  | `"Public Administration & Safety"`          |
  | `"Purchasing"`                              |
  | `"Research & Development"`                  |
  | `"Sales & Business Development"`            |
  | `"Science"`                                 |
  | `"Supply Chain & Logistics"`                |
  | `"Writing/Editing"`                         |
</Accordion>

***

## Sales Regions

Used in: **Employee Finder** (`sales_region` filter)

| Value     | Coverage                        |
| :-------- | :------------------------------ |
| `"NORAM"` | North America (US, Canada)      |
| `"LATAM"` | Latin America                   |
| `"EMEA"`  | Europe, Middle East, and Africa |
| `"APAC"`  | Asia-Pacific                    |

***

## Continents

Used in: **Employee Finder** (`continent` filter)

| Value             |
| :---------------- |
| `"Africa"`        |
| `"Antarctica"`    |
| `"Asia"`          |
| `"Europe"`        |
| `"North America"` |
| `"Oceania"`       |
| `"South America"` |

***

## Company Type

Used in: **Company Search** (`company.type.include` and `company.type.exclude` filters).

| Value                       | Description                     |
| :-------------------------- | :------------------------------ |
| `"Educational"`             | Educational organizations       |
| `"Educational Institution"` | Schools, colleges, universities |
| `"Government Agency"`       | Government bodies and agencies  |
| `"Nonprofit"`               | Non-profit organizations        |
| `"Partnership"`             | Partnerships                    |
| `"Privately Held"`          | Private companies               |
| `"Public Company"`          | Publicly traded companies       |
| `"Self-Employed"`           | Self-employed individuals       |
| `"Self-Owned"`              | Self-owned entities             |
| `"Sole Proprietorship"`     | Sole proprietorships            |

***

## Industry

Used in: **Company Search** (`industry.include` and `industry.exclude` filters)

<Accordion title="View all accepted industry values">
  | Industry                                 |
  | :--------------------------------------- |
  | `"Accounting"`                           |
  | `"Airlines and Aviation"`                |
  | `"Alternative Medicine"`                 |
  | `"Animation"`                            |
  | `"Apparel and Fashion"`                  |
  | `"Architecture and Planning"`            |
  | `"Arts and Crafts"`                      |
  | `"Automotive"`                           |
  | `"Aviation and Aerospace"`               |
  | `"Banking"`                              |
  | `"Biotechnology"`                        |
  | `"Broadcast Media"`                      |
  | `"Building Materials"`                   |
  | `"Business Supplies and Equipment"`      |
  | `"Capital Markets"`                      |
  | `"Chemicals"`                            |
  | `"Civic and Social Organization"`        |
  | `"Civil Engineering"`                    |
  | `"Commercial Real Estate"`               |
  | `"Computer and Network Security"`        |
  | `"Computer Games"`                       |
  | `"Computer Hardware"`                    |
  | `"Computer Networking"`                  |
  | `"Computer Software"`                    |
  | `"Construction"`                         |
  | `"Consumer Electronics"`                 |
  | `"Consumer Goods"`                       |
  | `"Consumer Services"`                    |
  | `"Cosmetics"`                            |
  | `"Dairy"`                                |
  | `"Defense and Space"`                    |
  | `"Design"`                               |
  | `"E-Learning"`                           |
  | `"Education Management"`                 |
  | `"Electrical/Electronic Manufacturing"`  |
  | `"Entertainment"`                        |
  | `"Environmental Services"`               |
  | `"Events Services"`                      |
  | `"Executive Office"`                     |
  | `"Facilities Services"`                  |
  | `"Farming"`                              |
  | `"Financial Services"`                   |
  | `"Fine Art"`                             |
  | `"Fishery"`                              |
  | `"Food Production"`                      |
  | `"Food and Beverages"`                   |
  | `"Fundraising"`                          |
  | `"Furniture"`                            |
  | `"Gambling and Casinos"`                 |
  | `"Glass, Ceramics and Concrete"`         |
  | `"Government Administration"`            |
  | `"Government Relations"`                 |
  | `"Graphic Design"`                       |
  | `"Health, Wellness and Fitness"`         |
  | `"Higher Education"`                     |
  | `"Hospital and Health Care"`             |
  | `"Hospitality"`                          |
  | `"Human Resources"`                      |
  | `"Import and Export"`                    |
  | `"Individual and Family Services"`       |
  | `"Industrial Automation"`                |
  | `"Information Services"`                 |
  | `"Information Technology and Services"`  |
  | `"Insurance"`                            |
  | `"International Affairs"`                |
  | `"International Trade and Development"`  |
  | `"Internet"`                             |
  | `"Investment Banking"`                   |
  | `"Investment Management"`                |
  | `"Judiciary"`                            |
  | `"Law Enforcement"`                      |
  | `"Law Practice"`                         |
  | `"Legal Services"`                       |
  | `"Legislative Office"`                   |
  | `"Leisure, Travel and Tourism"`          |
  | `"Libraries"`                            |
  | `"Logistics and Supply Chain"`           |
  | `"Luxury Goods and Jewelry"`             |
  | `"Machinery"`                            |
  | `"Management Consulting"`                |
  | `"Maritime"`                             |
  | `"Market Research"`                      |
  | `"Marketing and Advertising"`            |
  | `"Mechanical or Industrial Engineering"` |
  | `"Media Production"`                     |
  | `"Medical Devices"`                      |
  | `"Medical Practice"`                     |
  | `"Mental Health Care"`                   |
  | `"Military"`                             |
  | `"Mining and Metals"`                    |
  | `"Motion Pictures and Film"`             |
  | `"Museums and Institutions"`             |
  | `"Music"`                                |
  | `"Nanotechnology"`                       |
  | `"Newspapers"`                           |
  | `"Non-Profit Organization Management"`   |
  | `"Oil and Energy"`                       |
  | `"Online Media"`                         |
  | `"Outsourcing/Offshoring"`               |
  | `"Package/Freight Delivery"`             |
  | `"Packaging and Containers"`             |
  | `"Paper and Forest Products"`            |
  | `"Performing Arts"`                      |
  | `"Pharmaceuticals"`                      |
  | `"Philanthropy"`                         |
  | `"Photography"`                          |
  | `"Plastics"`                             |
  | `"Political Organization"`               |
  | `"Primary/Secondary Education"`          |
  | `"Printing"`                             |
  | `"Professional Training and Coaching"`   |
  | `"Program Development"`                  |
  | `"Public Policy"`                        |
  | `"Public Relations and Communications"`  |
  | `"Public Safety"`                        |
  | `"Publishing"`                           |
  | `"Railroad Manufacture"`                 |
  | `"Ranching"`                             |
  | `"Real Estate"`                          |
  | `"Recreational Facilities and Services"` |
  | `"Religious Institutions"`               |
  | `"Renewables and Environment"`           |
  | `"Research"`                             |
  | `"Restaurants"`                          |
  | `"Retail"`                               |
  | `"Security and Investigations"`          |
  | `"Semiconductors"`                       |
  | `"Shipbuilding"`                         |
  | `"Sporting Goods"`                       |
  | `"Sports"`                               |
  | `"Staffing and Recruiting"`              |
  | `"Supermarkets"`                         |
  | `"Telecommunications"`                   |
  | `"Textiles"`                             |
  | `"Think Tanks"`                          |
  | `"Tobacco"`                              |
  | `"Translation and Localization"`         |
  | `"Transportation/Trucking/Railroad"`     |
  | `"Utilities"`                            |
  | `"Venture Capital and Private Equity"`   |
  | `"Veterinary"`                           |
  | `"Warehousing"`                          |
  | `"Wholesale"`                            |
  | `"Wine and Spirits"`                     |
  | `"Wireless"`                             |
  | `"Writing and Editing"`                  |
</Accordion>

***

## Country Codes

Used in: **Waterfall ICP** (`location` field), **Employee Finder** (`country_code` field), **Company Search** (`hq.country_code` field).

Country codes follow the **ISO 3166-1 alpha-2** standard (consistent with LinkedIn).

<Tip>
  For **Waterfall ICP Search**, use `"WORLD"` to search globally without geographic restriction. For **Employee Finder**, use `["WORLD"]` as `country_code` default or simply omit the field. For **Company Search** omit the location/hq fields entirely or pass empty arrays.
</Tip>

### Common Codes

| Country        | Code |
| :------------- | :--- |
| United States  | `US` |
| United Kingdom | `GB` |
| France         | `FR` |
| Canada         | `CA` |
| Germany        | `DE` |
| Australia      | `AU` |
| Netherlands    | `NL` |
| Spain          | `ES` |
| Italy          | `IT` |
| India          | `IN` |
| Brazil         | `BR` |
| Singapore      | `SG` |
| Sweden         | `SE` |
| Switzerland    | `CH` |
| Belgium        | `BE` |
| Denmark        | `DK` |
| Norway         | `NO` |
| Finland        | `FI` |
| Poland         | `PL` |
| Israel         | `IL` |
| Japan          | `JP` |
| South Korea    | `KR` |
| China          | `CN` |
| Mexico         | `MX` |
| Argentina      | `AR` |
| Chile          | `CL` |
| Colombia       | `CO` |
| South Africa   | `ZA` |
| UAE            | `AE` |
| Saudi Arabia   | `SA` |

For the complete list of all country codes, refer to the [official ISO 3166-1 standard](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) or the [Microsoft LinkedIn Documentation](https://learn.microsoft.com/en-us/linkedin/shared/references/reference-tables/country-codes).

***

## Troubleshooting: 0 Results

<AccordionGroup>
  <Accordion title="I get 0 results but my filters look correct">
    The most common cause is a non-normalized value. Check these:

    * **Industry**: `"Tech"` is not valid — use `"Information Technology and Services"` or `"Computer Software"` or `"Internet"`.
    * **Country code**: `"USA"` is not valid — use `"US"`. `"United Kingdom"` is not valid — use `"GB"`.
    * **Employee range**: `"50-200"` is not valid — use `"51-200"`.
    * **Job level**: `"vp"` is not valid — use `"VP"`. `"C-Level"` is not valid — use `"C-Team"`.
    * **Job function**: `"Sales"` is not valid — use `"Sales & Business Development"`.
    * **Sales region**: `"NA"` is not valid — use `"NORAM"`.

    All values are case-sensitive. Copy-paste from this page.
  </Accordion>

  <Accordion title="My industry filter returns fewer results than expected">
    LinkedIn's industry taxonomy is granular. Try using multiple values in your `industry.include` array to broaden the search. For example, instead of just `"Computer Software"`, also include `"Information Technology and Services"` and `"Internet"`.
  </Accordion>

  <Accordion title="Employee Finder returns results but not the roles I expected">
    Check that you're using the right combination of `job_level` and `job_function`. For example, to find senior sales leaders, use `"job_level": ["C-Team", "VP", "Director"]` combined with `"job_function": ["Sales & Business Development"]`.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).