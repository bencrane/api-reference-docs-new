---
title: "Handling Review Dates and the API"
url: "https://support.senja.io/handling-review-dates-and-the-api-e4vdo"
path: "/handling-review-dates-and-the-api-e4vdo"
---

# Handling Review Dates and the API

When you retrieve reviews using our API, you might notice that the dates associated with them aren't always exact. This is a known limitation that stems from how we receive date information from our third-party data providers.

**What's the issue?** Some data providers, like Google, don't provide precise dates for reviews. Instead, they might provide a relative time (e.g., "2 months ago") or a date that's close to, but not exactly, the original review date. To handle this, our system defaults to the 22nd of the month when an exact date isn't available. This is why you might see a disproportionate number of reviews dated on the 22nd.

## Displaying relative dates

To avoid confusion and provide a better experience for your users, we recommend displaying relative dates (e.g., "3 months ago," "last year") instead of exact dates. This approach is more in line with how many platforms, including Google, display review dates.

If you prefer not to show dates at all, you can disable them in your widget settings. Many of our users choose this option to simplify their display.

## Looking ahead

We understand that this is a frustration for our users, and we're actively exploring ways to improve the accuracy of review dates. If you have any feedback or suggestions, we'd love to hear from you. Please share your ideas on our feedback page.
