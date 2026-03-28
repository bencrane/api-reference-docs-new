---
title: "Add Senja Video Testimonials to Your App"
url: "https://support.senja.io/collect-video-testimonials-from-senja-customers-24tum"
path: "/collect-video-testimonials-from-senja-customers-24tum"
---

# Add Senja Video Testimonials to Your App

Let your users add their Senja video testimonials directly in your product.

Our platform integration allows your users to load a modal, pick one of their Senja video testimonials and play or upload them directly in your app.

This functionality is ideal for:

- Social media scheduling tools (ex. Postbridge, Buffer)
- Publishing tools (Substack, Beehiiv)
- Video sharing and hosting tools (Vimeo, Wistia)

## Getting started

To collect a video testimonial from a Senja customer, follow these steps:

### Step 1: Install the platform script

To get started, add the Senja platform script to the `<head>` of your website:

```html
<script src="https://static.senja.io/dist/integration.js" type="text/javascript" async="true"></script>
```

### Step 2: Open the Senja popup

Call `window.SenjaIntegrationPlatform.getVideoClip` to get a video clip from a customer:

```javascript
async function getVideoClip() {
  const clip = await window.SenjaIntegrationPlatform.getVideoClip({
    // optional: if you don't want Senja to open a popup and would
    // prefer the widget picker to be embedded, use this argument.
    target: "#the-id-of-your-container"
  });

  if(!clip) return;

  const url = clip.videoUrl;
  // upload the video URL to your own servers.
}
```

This is an asynchronous function that will prompt the user to:

1. Log into or create their Senja account
2. Search for and select a Senja video clip

The mp4 file will be available via the `clip.videoUrl` property. You can upload this file to your servers + CDN, or serve it directly.

## Other ways to integrate

Senja's platform script also allows you to add Senja widgets from customers to your app. See: Add Senja widget testimonials to your app.
