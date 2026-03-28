---
title: "How to customize the width of your widget embed"
url: "https://support.senja.io/how-to-customize-the-width-of-your-widget-embed-n49ja"
path: "/how-to-customize-the-width-of-your-widget-embed-n49ja"
---

# How to customize the width of your widget embed

By default, Senja widgets span the full width of their container (100%). You can customize the width by adding inline styles to your embed code.

## Customize width with inline styles

Add a style attribute to the div element in your embed code:

```html
<div class="senja-embed" data-id="YOUR_ID" style="width: 600px; margin-left: auto; margin-right: auto;" data-lazyload="true"></div>
<script async type="text/javascript" src="https://static.senja.io/dist/platform.js"></script>
```

- Replace 600px with your desired width (e.g., 400px, 800px, 50%)
- Replace YOUR_ID with your widget's ID
- The `margin-left: auto; margin-right: auto;` centers the widget

> Use a percentage value (e.g., width: 80%) to keep your widget responsive on different screen sizes.

## Advanced customization with CSS

For more control over responsive behavior or multiple widgets, use custom CSS instead. You can set different widths for mobile and desktop using media queries.
