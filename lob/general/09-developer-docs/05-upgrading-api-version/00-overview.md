# Upgrading API version

When backward-incompatible changes are made to the API, a new dated version is released. You can view your current version in your [dashboard settings](https://dashboard.lob.com/settings/api-keys).&#x20;

{% hint style="info" %}
Any API version prior to **2020-02-11** has been sunsetted.
{% endhint %}

It is recommended that when you are ready to upgrade your API version to the current version, you should add the version to your requests in the HTTP header as shown in the [API documentation](https://docs.lob.com/#tag/Versioning-and-Changelog) and then attempt test requests to ensure your integration will not break upon fully upgrading.&#x20;

Once testing is complete, you can go into your dashboard [settings](https://dashboard.lob.com/settings/api-keys) and make the full upgrade. After that is complete, you should remove the Lob version header from your requests to ensure all your requests use your global version.

You will only need to specify a version if you would like to test a newer version of the API without doing a full upgrade. The API will return an error if a version older than your current one is passed in.&#x20;

For more information about versioning see [our API documentation](https://docs.lob.com/#tag/Versioning-and-Changelog). &#x20;