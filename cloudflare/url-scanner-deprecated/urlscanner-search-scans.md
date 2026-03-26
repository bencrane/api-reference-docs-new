# Search URL scans

`GET /accounts/{account_id}/urlscanner/scan`

> **Deprecated**

Search scans by date and webpages' requests, including full URL (after redirects), hostname, and path. <br/> A successful scan will appear in search results a few minutes after finishing but may take much longer if the system in under load. By default, only successfully completed scans will appear in search results, unless searching by `scanId`. Please take into account that older scans may be removed from the search index at an unspecified time.

## Parameters

- **account_id** (string, required) [path]: Account ID.
- **scan_id** (string, optional) [query]: Scan UUID.
- **limit** (integer, optional) [query]: Limit the number of objects in the response.
- **next_cursor** (string, optional) [query]: Pagination cursor to get the next set of results.
- **date_start** (string, optional) [query]: Filter scans requested after date (inclusive).
- **date_end** (string, optional) [query]: Filter scans requested before date (inclusive).
- **url** (string, optional) [query]: Filter scans by URL of _any_ request made by the webpage
- **hostname** (string, optional) [query]: Filter scans by hostname of _any_ request made by the webpage.
- **path** (string, optional) [query]: Filter scans by url path of _any_ request made by the webpage.
- **ip** (string, optional) [query]: Filter scans by IP address (IPv4 or IPv6) of _any_ request made by the webpage.
- **hash** (string, optional) [query]: Filter scans by hash of any html/js/css request made by the webpage.
- **page_url** (string, optional) [query]: Filter scans by submitted or scanned URL
- **page_hostname** (string, optional) [query]: Filter scans by main page hostname (domain of effective URL).
- **page_path** (string, optional) [query]: Filter scans by exact match of effective URL path (also supports suffix search).
- **page_asn** (string, optional) [query]: Filter scans by main page Autonomous System Number (ASN).
- **page_ip** (string, optional) [query]: Filter scans by  main page IP address (IPv4 or IPv6).
- **account_scans** (boolean, optional) [query]: Return only scans created by account.
- **is_malicious** (boolean, optional) [query]: Filter scans by malicious verdict.

## Response

### 200

Search results

- **errors** (array): 
- **messages** (array): 
- **result** (object): 
- **success** (boolean): Whether search request was successful or not

### 400

Invalid params.

- **errors** (array): 
- **messages** (array): 
- **success** (boolean): Whether request was successful or not
