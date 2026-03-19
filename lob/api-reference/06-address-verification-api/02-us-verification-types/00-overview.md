# US Verification Types

These are detailed definitions for various fields in the US verification object.

## ZIP Code Types — `components[zip_code_type]`

| Value | Description |
|---|---|
| `standard` | The default ZIP code type. Used when none of the other types apply. |
| `po_box` | The ZIP code contains only PO Boxes. |
| `unique` | The ZIP code is uniquely assigned to a single organization (such as a government agency) that receives a large volume of mail. |
| `military` | The ZIP code contains military addresses. |
| *(empty string)* | A match could not be made with the provided inputs. |

## Record Types — `components[record_type]`

| Value | Description |
|---|---|
| `street` | The default address type. |
| `highrise` | The address is a commercial building, apartment complex, highrise, etc. |
| `firm` | The address is of an organizational entity which receives a minimum number of mailpieces per day. |
| `po_box` | The address is a PO Box. |
| `rural_route` | The address exists on a Rural Route. This is an older system of mail delivery which is still used in some parts of the country. |
| `general_delivery` | The address is part of the USPS General Delivery service, which allows individuals without permanent addresses to receive mail. |
| *(empty string)* | A match could not be made with the provided inputs. |

## Carrier Route Types — `components[carrier_route_type]`

| Value | Description |
|---|---|
| `city_delivery` | The default carrier route type. Used when none of the other types apply. |
| `rural_route` | The carrier route is a Rural Route. This is an older system of mail delivery which is still used in some parts of the country. |
| `highway_contract` | The carrier route is a Highway Contract Route. This is an older system of mail delivery which is still used in some parts of the country. |
| `po_box` | The carrier route consists of PO Boxes. |
| `general_delivery` | The carrier route is part of the USPS General Delivery service, which allows individuals without permanent addresses to receive mail. |
| *(empty string)* | A match could not be made with the provided inputs. |

## DPV Footnotes — `deliverability_analysis[dpv_footnotes]`

| Value | Description |
|---|---|
| `AA` | Some parts of the address (such as the street and ZIP code) are valid. |
| `A1` | The address is invalid based on given inputs. |
| `BB` | The address is deliverable. |
| `CC` | The address is deliverable by removing the provided secondary unit designator. |
| `TA` | The address is deliverable by dropping a trailing alphabet from the primary number. |
| `IA` | The address is an Informed Address. The recipient and the street address is replaced with a special code provided by the USPS. |
| `N1` | The address is deliverable but is missing a secondary information (apartment, unit, etc). |
| `F1` | The address is a deliverable military address. |
| `G1` | The address is a deliverable General Delivery address. General Delivery is a USPS service which allows individuals without permanent addresses to receive mail. |
| `U1` | The address is a deliverable unique address. A unique ZIP code is assigned to a single organization (such as a government agency) that receives a large volume of mail. |
| `C1` | The primary number was confirmed whereas the secondary number is unconfirmed and required to be deliverable. |
| `M1` | The primary number is missing. |
| `M3` | The primary number is invalid. |
| `P1` | PO Box, Rural Route, or Highway Contract box number is missing. |
| `P3` | PO Box, Rural Route, or Highway Contract box number is invalid. |
| `PB` | The address is identified as PO Box street address. |
| `R1` | The address matched to a CMRA and private mailbox information is not present. |
| `R7` | The address matched to a Phantom Carrier Route (`carrier_route` of `R777`), which corresponds to physical addresses that are not eligible for delivery. |
| `RR` | The address matched to a CMRA and private mailbox information is present. |