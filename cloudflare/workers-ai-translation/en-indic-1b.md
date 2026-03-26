# Execute @cf/ai4bharat/indictrans2-en-indic-1B model.

`POST /accounts/{account_id}/ai/run/@cf/ai4bharat/indictrans2-en-indic-1B`

Runs inference on the @cf/ai4bharat/indictrans2-en-indic-1B model.

## Parameters

- **account_id** (string, required) [path]: 
- **queueRequest** (string, optional) [query]: 
- **tags** (string, optional) [query]: 

## Request Body

- **target_language** (string, required): Target langauge to translate to Values: `asm_Beng`, `awa_Deva`, `ben_Beng`, `bho_Deva`, `brx_Deva`, `doi_Deva`, `eng_Latn`, `gom_Deva`, `gon_Deva`, `guj_Gujr`, `hin_Deva`, `hne_Deva`, `kan_Knda`, `kas_Arab`, `kas_Deva`, `kha_Latn`, `lus_Latn`, `mag_Deva`, `mai_Deva`, `mal_Mlym`, `mar_Deva`, `mni_Beng`, `mni_Mtei`, `npi_Deva`, `ory_Orya`, `pan_Guru`, `san_Deva`, `sat_Olck`, `snd_Arab`, `snd_Deva`, `tam_Taml`, `tel_Telu`, `urd_Arab`, `unr_Deva`
- **text** (object, required): Input text to translate. Can be a single string or a list of strings.

## Response

### 200

Object with user data.

Type: object

### 400

Bad request

- **errors** (array): 
- **result** (object): 
- **success** (boolean):
