---
title: "Why isn’t my custom domain working?"
url: "https://support.senja.io/why-isnt-my-custom-domain-working-kmbo3"
path: "/why-isnt-my-custom-domain-working-kmbo3"
---

# Why isn’t my custom domain working?

If your custom domain isn’t working, there are a few things you can check to troubleshoot the issue.

First, make sure that your domain is properly set up with your domain registrar and that you have a CNAME record pointing to cname.senja.cloudIt may take a few hours or days for your custom domain to work, so please be patient 🙏I’m getting an ERR_SSL_VERSION_OR_CIPHER_MISMATCH errorIf you’re getting this error, then Senja wasn’t able to set up an SSL certificate pointing to your domain.

This usually happens because you might have CAA records set up that restrict SSL certificates from being issued to your domain.

To fix this, you'll need to eitherremove any CAA records that are blocking the SSL certificate oradd Senja’s CAA records that allows the SSL certificate to be issued.

You can contact your domain registrar for assistance with this process.I’m getting a Cname cross user banned errorYou might get this error if you have zone holds enabled on your Cloudflare account.

If that’s the case, Cloudflare won’t allow you to cname to other Cloudflare zones.

You can temporarily toggle it off by following this guide. https://developers.cloudflare.com/fundamentals/setup/account/account-security/zone-holds/Once your domain has been connected, you can turn this back on.I need more helpPlease send us an email to support@senja.io and we will help you get your custom domain set up.
