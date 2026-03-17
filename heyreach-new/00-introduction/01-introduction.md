HeyReach API
Introduction
Welcome to the HeyReach API. Let' get started with a quick setup on how to use the API!
Finding your API key
The first step when using the HeyReach API is authenticating your requests with an API key.
The API key is used to authenticate the incoming requests and map them to your organization.
API keys never expire, however they can be deleted/deactivated.
Authentication
After you have your API key, you will need to provide it in every request that you make to the HeyReach API.
You will need to use add the X-API-KEY request header to every request and set you API key as the value.
Test your API key
Once you have your API key, you can check if it's working by sending the following request.
If everything is working properly, you should get a 200 HTTP status code.
 View More
Plain Text
curl --location &#x27;https://api.heyreach.io/api/public/auth/CheckApiKey&#x27; --header &#x27;X-API-KEY: <YOUR_API_KEY>&#x27;
Rate Limits
HeyReach allows a maximum of 300 requests per minute. All requests are attributed to the same limit.
Going above the limit will return a 429 HTTP status code and an error.
Enjoy building 🛠️