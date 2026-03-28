---
title: "Troubleshoot your Webflow widget"
url: "https://support.senja.io/troubleshoot-your-webflow-widget-ks7yb"
path: "/troubleshoot-your-webflow-widget-ks7yb"
---

# Troubleshoot your Webflow widget

If your widget isn't displaying correctly on your Webflow site, there are a few things you can check to troubleshoot the issue.

This guide will walk you through the most common problems and how to solve them.

Before you begin Important: Custom code can sometimes conflict with Webflow's underlying functionality.

Webflow's support team is unable to provide direct help with custom code setup or troubleshooting.

If you continue to experience issues after following these steps, we recommend posting on the Webflow Forum for community assistance.

Troubleshooting StepsCheck your embed codeThe most common cause of issues is an error in the embed code.

Double-check the following:Make sure you've copied the entire code snippet from your widget settings.

Ensure there are no extra <html>, <head>, or <body> tags in the code.

Verify that all HTML tags are properly opened and closed.

Confirm your Webflow setupEnsure the widget is embedded correctly in your Webflow project:The Embed element should be placed inside a Container, which is itself inside a Section.

Preview your site to see if the widget appears.

Remember that some scripts only run on the published site, so you may need to publish your changes to see the widget.

Review Webflow's custom code limitations Webflow has a 50,000-character limit for custom code embeds.

If your widget code exceeds this limit, it may not work correctly.

You can try minifying the code or splitting it into multiple Embed elements.

Also, be aware of potential conflicts with other scripts on your site, such as different versions of jQuery.

Common IssuesMy widget isn't displaying at allIf your widget isn't showing up, try the following:Re-copy the embed code from your widget settings and paste it into a new Embed element in Webflow.

Check for any custom code errors in your browser's developer console.

Temporarily remove any other custom scripts from your page to see if there's a conflict.

My widget isn’t updatingIf you've made changes to your widget but they aren't reflected on your Webflow site, it may be a caching issue.

Try republishing your site to clear the cache.

If you're using dynamic embeds, ensure that your Collection fields are correctly mapped to the embed code.

Once you've followed these steps, your widget should display correctly on your Webflow site.

If you're still having trouble, don't hesitate to reach out to our support team for further assistance.

What's next?

How to add testimonials to WebflowWebflow Custom Code Forum
