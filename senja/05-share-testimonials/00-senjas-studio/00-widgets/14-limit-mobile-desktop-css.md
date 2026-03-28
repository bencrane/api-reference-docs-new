---
title: "How to limit testimonials shown on mobile vs desktop using CSS"
url: "https://support.senja.io/how-to-limit-testimonials-shown-on-mobile-vs-desktop-using-css-a8xe8"
path: "/how-to-limit-testimonials-shown-on-mobile-vs-desktop-using-css-a8xe8"
---

# How to limit testimonials shown on mobile vs desktop using CSS

Limit testimonials shown on mobile vs desktop using CSSLearn how to control the number of testimonials displayed on different devices by using custom CSS media queries with your Senja widget.Why limit testimonials on mobile?Mobile screens have limited space, and showing too many testimonials can overwhelm users or cause performance issues. By limiting testimonials on mobile while keeping more visible on desktop, you create a better user experience across all devices.PrerequisitesBefore you start, you'll need:A Senja widget already embedded on your websiteAccess to add custom CSS to your widget or websiteBasic understanding of CSS (helpful but not required)How to limit testimonials using CSSThe technique uses CSS media queries combined with the nth-child selector to hide specific testimonials on smaller screens.Step 1: Identify your widget typeFirst, you need to know which Senja widget type you're using, as the CSS selector will vary:Hero Quote widgets: Use .sj-hero-quotesGrid widgets: Use .sj-gridCarousel widgets: Use .sj-carouselList widgets: Use .sj-listStep 2: Add the CSS codeHere are examples for common scenarios:Show 3 testimonials on mobile, 6 on desktop (Hero Quote widget)  @media only screen and (max-width: 600px) {
.sj-hero-quotes > *:nth-child(n+4) {
display: none;
}
}   Show 2 testimonials on mobile, 4 on desktop (Grid widget)  @media only screen and (max-width: 768px) {
.sj-grid > *:nth-child(n+3) {
display: none;
}
}   Show 1 testimonial on mobile, 3 on desktop (any widget type)  @media only screen and (max-width: 480px) {
.senja-embed > *:nth-child(n+2) {
display: none;
}
}   Step 3: Apply the CSSYou can add this CSS in several ways:Option 1: Senja widget custom CSSOpen your widget in Senja StudioClick on DesignClick on AdvancedClick on Custom CSSPaste your CSS codeClick Save changesOption 2: Your website's CSS fileAdd the CSS to your website's stylesheet or in a <style> tag in your page's <head> section.Common breakpoints and examplesHere are responsive breakpoints commonly used for different devices:Mobile-first approach  /* Mobile (default): Show 2 testimonials */
/* No media query needed for mobile-first */
/* Tablet: Show 4 testimonials */
@media only screen and (min-width: 768px) {
.sj-hero-quotes > *:nth-child(n+3) {
display: block;
}
}
/* Desktop: Show 6 testimonials */
@media only screen and (min-width: 1024px) {
.sj-hero-quotes > *:nth-child(n+5) {
display: block;
}
}   Desktop-first approach  /* Desktop (default): Show 6 testimonials */
/* No media query needed for desktop-first */
/* Tablet: Hide testimonials 5 and above */
@media only screen and (max-width: 1023px) {
.sj-hero-quotes > *:nth-child(n+5) {
display: none;
}
}
/* Mobile: Hide testimonials 3 and above */
@media only screen and (max-width: 767px) {
.sj-hero-quotes > *:nth-child(n+3) {
display: none;
}
}   Understanding the CSSMedia queries@media only screen and (max-width: 600px) targets screens smaller than 600px (typically mobile devices).nth-child selector:nth-child(n+4) selects the 4th child element and all subsequent elements. Combined with display: none, it hides these elements.Widget selectorsDifferent widget types use different CSS classes. If you're unsure, use .senja-embed > * as a general selector.TroubleshootingCSS not working?Make sure you're using the correct widget selector classTry adding !important to force the style: display: none !important;Check that your CSS is properly formatted and savedClear your browser cache and refresh the pageWrong number of testimonials showing?Adjust the nth-child number. For example:To show 2 testimonials: :nth-child(n+3)To show 3 testimonials: :nth-child(n+4)To show 5 testimonials: :nth-child(n+6)Need help identifying CSS classes?Right-click on your widget, select "Inspect Element," and look for classes starting with sj- in the HTML structure.Advanced examplesDifferent limits for multiple breakpoints  /* Show 1 testimonial on small mobile */
@media only screen and (max-width: 480px) {
.sj-hero-quotes > *:nth-child(n+2) {
display: none;
}
}
/* Show 2 testimonials on large mobile */
@media only screen and (min-width: 481px) and (max-width: 767px) {
.sj-hero-quotes > *:nth-child(n+3) {
display: none;
}
}
/* Show 4 testimonials on tablet */
@media only screen and (min-width: 768px) and (max-width: 1023px) {
.sj-hero-quotes > *:nth-child(n+5) {
display: none;
}
}
/* Show all testimonials on desktop (1024px+) */   Fade effect instead of hiding  @media only screen and (max-width: 600px) {
.sj-hero-quotes > *:nth-child(n+4) {
opacity: 0.3;
pointer-events: none;
}
}   Related guidesLearn more about customizing your Senja widgets:How to customize widget CSSHow to limit the number of testimonials displayed in a widgetHow to add testimonials to WixFor platform-specific embedding guides, check out our comprehensive list of website integration tutorials.
