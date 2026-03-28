---
title: "How to make avatar circles bigger in your widget"
url: "https://support.senja.io/how-to-make-avatar-circles-bigger-in-your-widget-hb5y3"
path: "/how-to-make-avatar-circles-bigger-in-your-widget-hb5y3"
---

# How to make avatar circles bigger in your widget

How to make avatar circles bigger in your widgetYou can customize the size of avatar images in your widget using custom CSS to better fit your design needs.

Add custom CSS to increase avatar sizeTo make the avatar circles larger, add this CSS code to your widget's custom CSS section:  .sj-avatar-container,
.sj-avatar-container img {
width: 100px !important;
height: 100px !important;
}   You can adjust the 100px values to any size you prefer.

Both width and height should use the same value to maintain circular avatars.

Important considerationsWhen you increase avatar sizes, the image quality might decrease.

This happens because Senja optimizes images for faster loading by default.

If you notice quality issues with larger avatars, you can disable image optimization in your settings.

This will preserve image quality but may slightly increase loading times.
