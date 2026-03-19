# Request Body

When manually sending a POST HTTP request directly to the Lob API, without the use of a library, you may represent the body as either a Form URL Encoded request, a JSON document, or a Multipart Form Data request.

However, if you're using one of our SDKs, the generation of the request bodies is done for you automatically and you don't need to worry about the format.

For fields that are intended to accept only string values, submitting JSON objects in string format (stringified JSON objects) is not supported. Our system automatically parses and validates incoming data according to their expected types. As a result, providing a stringified JSON object in a field designated for string input can cause parsing errors or lead to unexpected validation results.

## Form URL Encoded

This request body encoding is accompanied with the `Content-Type: application/x-www-form-urlencoded` header. The content is an example of what the Verify a US address endpoint accepts. An example of a request body encoded in this format follows.

```
primary_line=210 King Street&city=San Francisco&state=CA&zip_code=94107
```

## JSON

This request body encoding is accompanied with the `Content-Type: application/json` header. The content is an example of what the Verify a US address endpoint accepts. An example of a request body encoded in this format follows.

```json
{
  "primary_line": "210 King Street",
  "city": "San Francisco",
  "state": "CA",
  "zip_code": "94107"
}
```

## Multipart Form Data

This request body encoding is accompanied with the `Content-Type: multipart/form-data` header. This is the only format that can be used for uploading a file to the API. The content is an example of what the Create a check endpoint accepts. An example of a request body encoded in this format follows.

```
--------------------------7015ebe79c0a5f8c
Content-Disposition: form-data; name="description"

Demo Letter
--------------------------7015ebe79c0a5f8c
Content-Disposition: form-data; name="to"

adr_bae820679f3f536b
--------------------------7015ebe79c0a5f8c
Content-Disposition: form-data; name="from"

adr_210a8d4b0b76d77b
--------------------------7015ebe79c0a5f8c
Content-Disposition: form-data; name="file"; filename="file.pdf"
Content-Type: application/pdf

<FILE CONTENT>
--------------------------7015ebe79c0a5f8c
Content-Disposition: form-data; name="color"

true
--------------------------7015ebe79c0a5f8c--
```