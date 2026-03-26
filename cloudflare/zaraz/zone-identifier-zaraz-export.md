# Export Zaraz configuration

`GET /zones/{zone_id}/settings/zaraz/export`

Exports full current published Zaraz configuration for a zone, secret variables included.

## Parameters

- **zone_id** (string, required) [path]: 

## Response

### 200

Get Zaraz configuration response.

- **analytics** (object, optional): Cloudflare Monitoring settings.
- **consent** (object, optional): Consent management configuration.
- **dataLayer** (boolean, optional): Data layer compatibility mode enabled.
- **debugKey** (string, optional): The key for Zaraz debug mode.
- **historyChange** (boolean, optional): Single Page Application support enabled.
- **settings** (object, optional): General Zaraz settings.
- **triggers** (object, optional): Triggers set up under Zaraz configuration, where key is the trigger alpha-numeric ID and value is the trigger configuration.
- **variables** (object, optional): Variables set up under Zaraz configuration, where key is the variable alpha-numeric ID and value is the variable configuration. Values of variables of type secret are not included.
- **zarazVersion** (integer, optional): Zaraz internal version of the config.
- **tools** (object, optional): Tools set up under Zaraz configuration, where key is the alpha-numeric tool ID and value is the tool configuration object.

### 4XX

Get Zaraz configuration response failure.

- **errors** (object): 
- **messages** (object): 
- **result** (object): 
- **success** (boolean): Whether the API call was successful.
