---
title: "How to make your widget's text fit on mobile"
url: "https://support.senja.io/how-to-make-your-widgets-text-fit-on-mobile-ahnl4"
path: "/how-to-make-your-widgets-text-fit-on-mobile-ahnl4"
---

# How to make your widget's text fit on mobile

This article explains how to ensure your widget's text fits correctly on mobile devices.Why your widget text shrinks on mobilePadding applied to your widget can cause its content to shrink on smaller screens. This often happens when the padding is too large for the mobile viewport.How to fix widget text on mobileYou can use a CSS media query to remove or reduce padding specifically for mobile devices. Add the following CSS code to your website's stylesheet or within a <style> tag in your HTML.  @media (max-width: 768px) { /* Adjust max-width as needed for your mobile breakpoint */
.your-widget-class { /* Replace with your actual widget's CSS class or ID */
padding: 0 !important; /* Removes padding */
}
}   This code targets screens up to 768 pixels wide. It sets the padding of your widget to zero, ensuring the text has more space. Remember to replace .your-widget-class with the actual CSS class or ID of your widget.
