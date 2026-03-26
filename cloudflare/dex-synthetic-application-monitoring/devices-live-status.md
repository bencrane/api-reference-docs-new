# Get the live status of a latest device

`GET /accounts/{account_id}/dex/devices/{device_id}/fleet-status/live`

Get the live status of a latest device given device_id from the device_state table

## Parameters

- **account_id** (string, required) [path]: Unique identifier for account
- **device_id** (string, required) [path]: Unique identifier for device
- **since_minutes** (string, required) [query]: Number of minutes before current time
- **time_now** (string, optional) [query]: Number of minutes before current time
- **colo** (string, optional) [query]: List of data centers to filter results

## Response

### 200

Get the live status of a latest device

- **alwaysOn** (boolean): 
- **batteryCharging** (boolean): 
- **batteryCycles** (integer): 
- **batteryPct** (number): 
- **colo** (string): Cloudflare colo
- **connectionType** (string): 
- **cpuPct** (number): 
- **cpuPctByApp** (array): 
- **deviceId** (string): Device identifier (UUID v4)
- **deviceIpv4** (object): 
- **deviceIpv6** (object): 
- **deviceName** (string): Device identifier (human readable)
- **diskReadBps** (integer): 
- **diskUsagePct** (number): 
- **diskWriteBps** (integer): 
- **dohSubdomain** (string): 
- **estimatedLossPct** (number): 
- **firewallEnabled** (boolean): 
- **gatewayIpv4** (object): 
- **gatewayIpv6** (object): 
- **handshakeLatencyMs** (number): 
- **ispIpv4** (object): 
- **ispIpv6** (object): 
- **metal** (string): 
- **mode** (string): The mode under which the WARP client is run
- **networkRcvdBps** (integer): 
- **networkSentBps** (integer): 
- **networkSsid** (string): 
- **personEmail** (string): User contact email address
- **platform** (string): Operating system
- **ramAvailableKb** (integer): 
- **ramUsedPct** (number): 
- **ramUsedPctByApp** (array): 
- **status** (string): Network status
- **switchLocked** (boolean): 
- **timestamp** (string): Timestamp in ISO format
- **version** (string): WARP client version
- **wifiStrengthDbm** (integer): 

### 4XX

Get the live status of a latest device failure

- **errors** (object, optional): 
- **messages** (object, optional): 
- **result** (object, optional):  Values: ``
- **success** (boolean, optional): Whether the API call was successful. Values: `false`
