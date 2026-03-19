# HTML Examples

Use a pre-designed template from our gallery or follow these basic guidelines as starting points for creating custom Postcards, Self Mailers, Letters, and Checks.

Please follow the standards used in these templates, such as:

- For any linked assets, you must use a performant file hosting provider with no rate limits such as Amazon S3.
- Use inline styles or an internal stylesheet, do not link to external stylesheets.
- Link to images that are 300DPI and sized at the final desired size on the physical mailing. For example, for a photo that is desired to be 1in x 1in on the final postcard, the image asset should be sized at 1in x 1in at 300DPI (which equates to 300px by 300px).
- The sum of all linked assets should not exceed 5MB in file size.
- Use `-webkit` prefixes for CSS properties when recommended here.

Because different browsers have varying user-agent styles, the HTML you see in your browser will not always look identical to what is produced through the API. It is strongly recommended that you test all HTML requests by reviewing the final PDF files in your Test Environment, as these are the files that will be printed.