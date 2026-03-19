# AV Elements

## How to get started <a href="#how-to-get-started-0" id="how-to-get-started-0"></a>

### Registration <a href="#registration-1" id="registration-1"></a>

Create an account at [Lob.com](https://www.lob.com/) to obtain a **Live Public API Key**. The key is available in the [*API Keys* tab](https://dashboard.lob.com/settings/api-keys) of the Lob [Dashboard Settings](https://dashboard.lob.com/settings/) and uses the format, `live_pub_*`

### Usage <a href="#usage-2" id="usage-2"></a>

Address Elements works by targeting the input elements of your address form and using their values with Lob's verification and autocomplete functionality. Include the AV Elements script tag immediately before the closing `<body>` tag

Code demo:

```json
<script src="https://cdn.lob.com/lob-address-elements/2.2.1/lob-address-elements.min.merged.js"
  data-lob-key="live_pub_xxx"
></script>
```

Sandbox:

![>> Click here to open sandbox environment](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1644279576838-1644279576838.png)

### Shopify users <a href="#shopify-users-3" id="shopify-users-3"></a>

AV elements works great with e-commerce platforms because they use predictable element names. For example, Shopify users can simply paste the following preconfigured script at the bottom of their Shopify Plus template.

{% hint style="success" %}
Remember to replace `live_pub_xxx` with your Lob public key
{% endhint %}

```json
<script src="https://cdn.lob.com/lob-address-elements/2.2.1/lob-address-elements.min.merged.js"
    data-lob-key="live_pub_xxx"
    data-lob-verify-value="strict"
    data-lob-primary-value="false"
    data-lob-err-bgcolor="#006eff"
    data-lob-err-color="#ffffff"></script>
```

![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1629292419366-1629292419366.jpeg)

{% hint style="warning" %}
Many E-commerce platforms have strict content security policies that prevent scripts from loading additional content. Embed the merged build of Address Elements to handle these situations as shown in the example above (`lob-address-elements.min.merged.js`). This ensures all dependencies are included in the download.
{% endhint %}

## Attribute reference cheatsheet <a href="#attribute-reference-cheatsheet-4" id="attribute-reference-cheatsheet-4"></a>

The Address Verification script has many attributes to give you complete control over its appearance and behavior. They generally go by the following pattern:

| data-lob-\*-id                                                                                                                                                                                                                                                                         | data-lob-\*-value                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p>These attributes are used to identify an element on your web page. Their values should be the elements ID and correspond to the components of an address: primary line, secondary line, city, state, and zip.</p><p></p><p>Example: <code>data-lob-primary-id="address1"</code></p> | <p>These attributes modify the behavior of autocomplete and verification. Their values are either true, false, or a string from a list of options</p><p></p><p>Example: <code>data-lob-verify-value="passthrough"</code></p> |

### **Form detection attributes** <a href="#form-detection-attributes-5" id="form-detection-attributes-5"></a>

With version 2, AV Elements can detect address form inputs automatically. We can improve performance by skipping the form detection process when these attributes are provided. Set them to the IDs for each field to target.

* `data-lob-primary-id`
* `data-lob-secondary-id`
* `data-lob-city-id`
* `data-lob-state-id`
* `data-lob-zip-id`
* `data-lob-country-id`

### **Form functionality attributes** <a href="#form-functionality-attributes-6" id="form-functionality-attributes-6"></a>

These attributes modify the behavior of AV Elements

| Attribute name             | Attribute value(s)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `data-lob-verify-value`    | <ul><li><code>strict</code></li><li><code>normal</code></li><li><code>relaxed</code></li><li><code>passthrough</code></li><li><code>false</code></li></ul><p>Controls the strictness level when verifying an address. If the strictness criteria is not met, we block the form submission and prompt the user to correct the address. Set to <code>passthrough</code> to submit the form regardless of the verification result. Set to <code>false</code> to disable verification altogether.</p><p></p><p>Default: <code>relaxed</code></p><p></p><p><a href="../../../print-and-mail/building-a-mail-strategy/managing-mail-settings#us-mail-strictness-settings-2">Learn more about Lob's strictness setting‍</a></p> |
| `data-lob-primary-valu`e   | <p>Enables or disables address autocompletion.</p><p></p><p>Default: <code>true</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `data-lob-secondary-value` | <p>When set to false, force the suite or unit number to render on the primary address line during address verification.</p><p></p><p>Default: <code>true</code></p>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

### **Custom error handling** <a href="#custom-error-handling-7" id="custom-error-handling-7"></a>

`data-lob-*-message-id` Identifies the element containing the error message at the input level. Lob will update the text content for this element and toggle its display.

| <ul><li><code>data-lob-primary-message-id</code></li><li><code>data-lob-secondary-message-id</code></li><li><code>data-lob-city-message-id</code></li><li><code>data-lob-city-message-id</code></li><li><code>data-lob-zip-message-id</code></li><li><code>data-lob-country-message-id</code></li></ul> | <p><img src="https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1629292739133-1629292739133.png" alt=""></p><p>Example: <code>data-lob-primary-message-id</code> points to the element below the input for Address 1. Any errors related to the primary line will be inserted inside this element.</p> |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

`data-lob-err-*-value` Overrides the default error message when a value is missing or specific Lob verification error messages

* `data-lob-err-primary-line-value`
* `data-lob-err-city-state-zip-value`
* `data-lob-err-zip-value`
* `data-lob-err-undeliverable-value`
* `data-lob-err-missing-unit-value`
* `data-lob-err-unnecessary-unit-value`
* `data-lob-err-incorrect-unit-value`
* `data-lob-err-confirm-value`
* `data-lob-err-default-value`

`data-lob-anchor-id` This optional attribute will place the general error message before the element with the id provided. An alternative attribute is `data-lob-anchor-class` which will search for the target element by class name.

## Usage with React & Vue <a href="#usage-with-react-vue-8" id="usage-with-react-vue-8"></a>

Modern web frameworks like React and Vue boost developer productivity without sacrificing control. Add IDs to the components of your address inputs (they will be included in the compiled HTML at runtime) then include these IDs in the form detection attributes of the AV elements script.

{% hint style="info" %}
If your component has many layers, you must ensure that the ID is propagated down to the root html components being used.
{% endhint %}

### React example <a href="#react-example-9" id="react-example-9"></a>

React demo

![>> Click here to open sandbox environment](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1629293249544-1629293249544.png)

In this demo we use React out of the box and create an address form. The AV elements script is added in `public/index.html` before the closing body tag. This demo also overrides some styles to keep the verification message centered in the form and to undo the styles applied to our primary address by our dependency algolia (for autocompletion).

### Vue example <a href="#vue-example-10" id="vue-example-10"></a>

Vue 3 demo

![>> Click here to open sandbox environment](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1629293076910-1629293076910.png)

Similarly, the AV elements script is also placed in `public/index.html` before the closing body tag.

#### A note about component libraries <a href="#a-note-about-component-libraries-11" id="a-note-about-component-libraries-11"></a>

The AV elements script searches for key form elements like the form tag and `<input type="submit" />`. When building your form with component libraries such as [Material-UI](https://material-ui.com/) or [Ant Design](https://ant.design/), check for the following:

* An ID can be propagate down to the root html elements used by the component.
* The components render the appropriate html elements for their behavior - they are materially honest (e.g. not styling links as buttons or using hidden elements to work correctly)

Case #1 may be the more common scenario you'll come across. If this happens, you will need to fallback to writing the component yourself in place of using the library's component.

## International support <a href="#international-support-12" id="international-support-12"></a>

International address verification is enabled when there is a country input present and it is set outside the United States. Form detection is relaxed on international forms since different countries may require different sets of address components.

{% hint style="warning" %}
Autocomplete is disabled for international addresses.
{% endhint %}

## Troubleshooting <a href="#troubleshooting-13" id="troubleshooting-13"></a>

AV Elements employs multiple strategies to detect your address form. If none of them work, we display an error message to help fix this. Those messages are shown below:

### Missing or duplicate form elements <a href="#missing-or-duplicate-form-elements-14" id="missing-or-duplicate-form-elements-14"></a>

**Problem**: These errors arise in the form detection process:

![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1649181170394-1649181170394.png)

![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1649181188380-1649181188380.png)

Either we are unable to find the input for a given address component, or we detected multiple inputs that may correspond to the same address component. There could be various causes for these errors including the input not existing, a label we're not familiar with, or a problem with the component's implementation from an external library.

**Solution**: Add the attribute(s) mentioned in the error to the AV elements script. The value should be an element id. For example, with the message above we must add the attribute `data-lob-state-id`.

```json
<script src="https://cdn.lob.com/lob-address-elements/2.2.1/lob-address-elements.min.merged.js"
data-lob-key="live_pub_xxx"
data-lob-state-id="id_of_state_input"
></script>pick
```