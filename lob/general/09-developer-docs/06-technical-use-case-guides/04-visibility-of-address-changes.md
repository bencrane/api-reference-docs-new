# Visibility of address changes

When sending mail or using Address Verification through Lob, addresses can be altered to match USPS requirements. This includes performing actions such as standardization, fixing typos like wrong zip codes, etc. These changes are surfaced back up to you, and if needed you can see the changes made.

## Why is this important? <a href="#why-is-this-important-0" id="why-is-this-important-0"></a>

Some companies may want to update their addresses to what we return when standardizing and correcting—however, some may also want to log what we changed. This could be important for compliance reasons as well as customer experience; showing your end users what was changed could be a very nice touch in your workflow.

## How do we solve this problem programmatically? <a href="#how-do-we-programmatically-solve-this-problem-1" id="how-do-we-programmatically-solve-this-problem-1"></a>

The way to do this today is to do a string comparison and see what we altered. For example, you will need to compare the address you passed to Lob with the address we returned back. With our AV product, you can retrieve more granular information without having to split out the address data on your own. For example, if you passed in "street" and in the API response you received "ST" in the "Street Suffix" field, you would know that was the specific change. If the "Street Name" was corrected you would see that split out as well. Otherwise, you can compare the full address and pull out the changes from there.

This leaves a lot of room for customization on business logic to determine what is important to your team when classifying something as a change. Oftentimes a change like “Street” to “St '' is not something the business team wants to be surfaced. It’s these types of business rules that are important when handling these alterations.

<br>

<figure><img src="https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1654105548084-Communication%20With%20Lob%20(20).jpg" alt=""><figcaption></figcaption></figure>

Below is an example of creating a postcard and comparing the to address input with the to address response to identify changes.

{% tabs %}
{% tab title="TypeScript" %}
{% embed url="<https://gist.github.com/lobot/e82cabf1b1dd498fcebeb24d2b25af7d#file-tracking-event-changes-typescript>" %}
{% endtab %}

{% tab title="Python" %}
{% embed url="<https://gist.github.com/lobot/58ab412fbe14bac5aeab88123f92f274#file-tracking-event-changes-python>" %}
{% endtab %}

{% tab title="Ruby" %}
{% embed url="<https://gist.github.com/lobot/e3d14a402722d3f961d14ec135d9e6e1#file-tracking-event-changes-ruby>" %}
{% endtab %}

{% tab title="PHP" %}
{% embed url="<https://gist.github.com/lobot/a510e7c6a77b3dc840614530e75f68c2#file-tracking-event-changes-php>" %}
{% endtab %}

{% tab title="Java" %}
{% embed url="<https://gist.github.com/lobot/ab49befc52b8e42104665c6d82dec983#file-tracking-event-changes-java>" %}
{% endtab %}
{% endtabs %}

## Further resources <a href="#further-resources-2" id="further-resources-2"></a>

* [Lob’s Print & Mail and Address Verification APIs & National Change of Address (NCOA) ](https://help.lob.com/print-and-mail/reaching-your-audience/all-about-addresses#national-change-of-address-ncoa-7)
* [NationalChangeofAddress.com](http://www.nationalchangeofaddress.com/) (NCOALink)