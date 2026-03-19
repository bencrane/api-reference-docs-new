# Autocompletion Test Env

Your test API key does not autocomplete US addresses and is used to simulate behavior. With your test API key, requests with specific values for `address_prefix` return predetermined values. When `address_prefix` is set to:

- `0 suggestions` — Returns no suggestions.
- `[PRIMARY NUMBER] s[uggestion]` — Returns a maximum of ten predefined suggested addresses. `[PRIMARY NUMBER]` does not have to be a valid primary number when sending a test request. Each additional letter in `suggestion` reduces the number of suggestions by one (e.g. `1 su` returns 9 suggested addresses). `[PRIMARY NUMBER]` does not affect the number of suggestions returned.

City and state filters work as expected and filter the list of predetermined suggested addresses. See the `test` request & response examples under Autocomplete Examples within the "Autocomplete a partial address" section in US Autocompletions.