# Create URL Scan

`POST /accounts/{account_id}/urlscanner/scan`

> **Deprecated**

Submit a URL to scan. You can also set some options, like the visibility level and custom headers. Check limits at https://developers.cloudflare.com/security-center/investigate/scan-limits/.

## Parameters

- **account_id** (string, required) [path]: Account ID.

## Request Body

- **country** (string, optional): Country to geo egress from Values: `AF`, `AL`, `DZ`, `AD`, `AO`, `AG`, `AR`, `AM`, `AU`, `AT`, `AZ`, `BH`, `BD`, `BB`, `BY`, `BE`, `BZ`, `BJ`, `BM`, `BT`, `BO`, `BA`, `BW`, `BR`, `BN`, `BG`, `BF`, `BI`, `KH`, `CM`, `CA`, `CV`, `KY`, `CF`, `TD`, `CL`, `CN`, `CO`, `KM`, `CG`, `CR`, `CI`, `HR`, `CU`, `CY`, `CZ`, `CD`, `DK`, `DJ`, `DM`, `DO`, `EC`, `EG`, `SV`, `GQ`, `ER`, `EE`, `SZ`, `ET`, `FJ`, `FI`, `FR`, `GA`, `GE`, `DE`, `GH`, `GR`, `GL`, `GD`, `GT`, `GN`, `GW`, `GY`, `HT`, `HN`, `HU`, `IS`, `IN`, `ID`, `IR`, `IQ`, `IE`, `IL`, `IT`, `JM`, `JP`, `JO`, `KZ`, `KE`, `KI`, `KW`, `KG`, `LA`, `LV`, `LB`, `LS`, `LR`, `LY`, `LI`, `LT`, `LU`, `MO`, `MG`, `MW`, `MY`, `MV`, `ML`, `MR`, `MU`, `MX`, `FM`, `MD`, `MC`, `MN`, `MS`, `MA`, `MZ`, `MM`, `NA`, `NR`, `NP`, `NL`, `NZ`, `NI`, `NE`, `NG`, `KP`, `MK`, `NO`, `OM`, `PK`, `PS`, `PA`, `PG`, `PY`, `PE`, `PH`, `PL`, `PT`, `QA`, `RO`, `RU`, `RW`, `SH`, `KN`, `LC`, `VC`, `WS`, `SM`, `ST`, `SA`, `SN`, `RS`, `SC`, `SL`, `SK`, `SI`, `SB`, `SO`, `ZA`, `KR`, `SS`, `ES`, `LK`, `SD`, `SR`, `SE`, `CH`, `SY`, `TW`, `TJ`, `TZ`, `TH`, `BS`, `GM`, `TL`, `TG`, `TO`, `TT`, `TN`, `TR`, `TM`, `UG`, `UA`, `AE`, `GB`, `US`, `UY`, `UZ`, `VU`, `VE`, `VN`, `YE`, `ZM`, `ZW`
- **customHeaders** (object, optional): Set custom headers.
- **screenshotsResolutions** (array, optional): Take multiple screenshots targeting different device types.
- **url** (string, required): 
- **visibility** (string, optional): The option `Public` means it will be included in listings like recent scans and search results. `Unlisted` means it will not be included in the aforementioned listings, users will need to have the scan's ID to access it. A a scan will be automatically marked as unlisted if it fails, if it contains potential PII or other sensitive material. Values: `Public`, `Unlisted`

## Response

### 200

Scan request accepted successfully.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): 

### 400

Invalid params.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether request was successful or not

### 409

Scan request denied: hostname was recently scanned.

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): 

### 429

Scan request denied: rate limited.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean):
