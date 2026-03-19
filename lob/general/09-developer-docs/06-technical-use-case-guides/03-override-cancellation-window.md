# Override cancellation window

Anytime you place an order it’s good to understand the cancellation policy. **By default, new accounts have a 4-hour cancellation window.** Within that time frame, you can cancel mailings, free of charge. Once the cancellation time window has passed for a postcard, self-mailer, letter, or check, the mailing is no longer cancelable.

{% hint style="info" %}
Users on higher editions can customize their cancellation windows in their dashboard settings. Upgrade your [Print & Mail edition](https://dashboard.lob.com/#/settings/editions) to gain access to this feature, or reach out to our sales team to learn more.
{% endhint %}

## Can I programmatically override my cancellation window? <a href="#can-i-programmatically-override-my-cancellation-window-1" id="can-i-programmatically-override-my-cancellation-window-1"></a>

Using a custom send date in your Lob request enables you to override your default cancelation window and set a specific date and time for which you want a mail piece to go into production.

## Why is this important? <a href="#why-is-this-important-2" id="why-is-this-important-2"></a>

Some clients may want to create a campaign today with Lob, but have it actually mailed in 2 weeks. This provides them the time to QA and make sure everything is in order. Others may need to dictate when certain mail pieces go out after a trigger, e.g., two weeks after a shopper abandons their cart, a postcard is sent telling them that the item is now on sale. Either way, this feature enables customers to dictate when a mail piece goes into production if a static cancellation window is not sufficient for their needs. They can do this for each specific mail piece and can customize as needed. If this is not used in the request, it will use the default cancellation window as it is not required.

## How do we (programmatically) solve this problem? <a href="#how-do-we-programmatically-solve-this-problem-3" id="how-do-we-programmatically-solve-this-problem-3"></a>

If a custom send date is desired, you will have to send either a date or a timestamp of the desired send date. If you send a simple date (YYYY-MM-DD) it will evaluate to midnight UTC of that date. If you don't need to send a custom send date, simply do not include it in the payload—or pass `null`—to use your default cancellation window. &#x20;

In the code sample below, we want mail to go into production on July 1st at 6:00 am PST which is 2:00 pm UTC. &#x20;

To do this our send date is "`2022-07-01T14:00:00`"

{% tabs %}
{% tab title="TypeScript" %}

```typescript
import {Configuration, Postcard, PostcardsApi, PostcardEditable, CountryExtended } from "@lob/lob-typescript-sdk"
 
 async function demo() {
    const config: Configuration = new Configuration({
        username: "<YOUR_TEST_KEY>"
    })
 
    const postcardData : PostcardEditable = {
        to: {
          name: "Harry Zhang",
          address_line1: "210 King Street",
          address_city: "San Francisco",
          address_state: "CA",
          address_zip: "94107"
        },
        from: {
          name: "Leore Avidar",
          address_line1: "210 King Street",
          address_city: "San Francisco",
          address_state: "CA",
          address_zip: "94107",
          address_country: CountryExtended.Us
        },
        front:   "https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/4x6_pc_template.pdf",
        back:   "https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/4x6_pc_template.pdf",
        send_date:   "2022-07-01T14:00:00"
    }
 
    try {
        const result : Postcard = await new PostcardsApi(config).create(postcardData)
        return result
    } catch (err: any) {
        console.error(err)
    }
 }
 
 demo().then((result)=> console.log(result)).catch()
```

{% endtab %}

{% tab title="Python" %}

```python
import lob
 
 lob.api_key = "<YOUR_TEST_KEY>"
 
 postcard = lob.Postcard.create(
 description = "First Postcard",
  to_address = {
    "name": "Harry Zhang",
    "address_line1": "210 King Street",
    "address_city": "San Francisco",
    "address_state": "CA",
    "address_zip": "94107"
  },
  from_address = {
    "name": "Leore Avidar",
    "address_line1": "210 King Street",
    "address_city": "San Francisco",
    "address_state": "CA",
    "address_zip": "94107",
    "address_country": "US"
  },
  front = "<html style='padding: 1in; font-size: 50;'>Front HTML for {{name}}</html>",
  back = "<html style='padding: 1in; font-size: 20;'>Back HTML for {{name}}</html>",
  merge_variables = {
    "name": "Harry"
  },
  send_date = "2022-07-01T14:00:00"  
 )
 
 print(postcard)
```

{% endtab %}

{% tab title="Ruby" %}

```ruby
require 'lob.rb'
require 'pp'
 
lob = Lob::Client.new(api_key: "<TEST_API_KEY>")
 
pp lob.postcards.create(
  description: "First Postcard",
  to: {
    name: "Harry Zhang",
    address_line1: "210 King Street",
    address_city: "San Francisco",
    address_state: "CA",
    address_zip: "94107"
  },
  from: {
    name: "Leore Avidar",
    address_line1: "210 King Street",
    address_city: "San Francisco",
    address_state: "CA",
    address_zip: "94107"
  },
  merge_variables: { name: "Harry" },
  front: "<html style='padding: 1in; font-size: 50;'>Front HTML for {{name}}</html>",
  back: "<html style='padding: 1in; font-size: 20;'>Back HTML for {{name}}</html>",
  send_date: "2022-07-01T14:00:00"
)

```

{% endtab %}

{% tab title="PHP" %}

```php
<?php require __DIR__ . '/vendor/autoload.php';
 
$lob = new \Lob\Lob('<TEST_API_KEY');
 
$postcard = $lob->postcards()->create(array(
    "description"           => "First Postcard",
    "to[name]"              => "HARRY ZHANG",
    "to[address_line1]"     => "210 KING STREET",
    "to[address_city]"      => "SAN FRANCISCO",
    "to[address_state]"     => "CA",
    "to[address_zip]"       => "94107",
    "from[name]"            => "LEORE AVIDAR",
    "from[address_line1]"   => "210 KING STREET",
    "from[address_city]"    => "SAN FRANCISCO",
    "from[address_state]"   => "CA",
    "from[address_zip]"     => "94107",
    "front"                 => "<html style='padding: 1in; font-size: 50;'>Front HTML for {{name}}</html>",
    "back"                  => "<html style='padding: 1in; font-size: 20;'>Back HTML for {{name}}</html>",
    "merge_variables[name]" => "Harry",
    "send_date"             => "2022-07-01T14:00:00"
  ));
 print_r($postcard);
?>
```

{% endtab %}

{% tab title="Java" %}

```java
package com.company.app;
 
 // HashMap for Java 8 and below
 // import java.util.HashMap;
 import java.util.Map;
 
 import com.lob.Lob;
 import com.lob.model.Address;
 import com.lob.model.Postcard;
 import com.lob.net.LobResponse;
 
 public class App
 {
    public static void main( String[] args )
    {
        Lob.init("<TEST_API_KEY>");
 
        Map<String, String> mergeVariables = Map.of(
            "name", "Harry"
        );
 
        // FOR JAVA VERSIONS 8 AND BELOW:
        // Map<String, String> merge_variables = new HashMap<String, String>() {{
        //     put("name", "Harry");
        // }};
 
        try {
 LobResponse<Postcard> response = new Postcard.RequestBuilder()
            .setDescription("First Mail piece")
            .setTo(
                    new Address.RequestBuilder()
                            .setName("HARRY ZHANG")
                            .setLine1("210 KING STREET")
                            .setCity("SAN FRANCISCO")
                            .setState("CA")
                            .setZip("94107")
            )
            .setFrom(
                    new Address.RequestBuilder()
                            .setName("LEORE AVIDAR" )
                            .setLine1("210 KING STREET")
                            .setCity("SAN FRANCISCO")
                            .setState("CA")
                            .setZip("94107")
            )
            .setFront("<html style='padding: 1in; font-size: 50;'>Front HTML for {{name}}</html>")
            .setBack("<html style='padding: 1in; font-size: 20;'>Back HTML for {{name}}</html>")
            .setMergeVariables(mergeVariables)
            .setSendDate("2022-07-01T14:00:00")
            .create();
 
  Postcard postcard = response.getResponseBody();
 
 System.out.println(postcard);
        } catch (Exception err) {
 System.out.println("Error on postcard creation: " + err);
        }
    }
 } 
```

{% endtab %}
{% endtabs %}

{% hint style="warning" %}

#### If you are using Lob's free Developer edition, setting the `send_date` is not available <a href="#if-you-are-using-lobs-free-developer-edition-setting-the-send_date-is-not-available-4" id="if-you-are-using-lobs-free-developer-edition-setting-the-send_date-is-not-available-4"></a>

Message you will receive from Lob's API:

"Your account's Print & Mail Edition does not allow you to use the Scheduled Mailings feature. Upgrade here: <https://dashboard.lob.com/#/settings/editions>"
{% endhint %}