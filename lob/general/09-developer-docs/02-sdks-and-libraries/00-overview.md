# SDKs & libraries

## SDKs <a href="#sdks-2" id="sdks-2"></a>

Currently, we have SDKs available for the following languages:

{% tabs %}
{% tab title="TypeScript" %}
![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1647371919748-github-svgrepo-com.svg)  [lob-typescript-sdk](https://github.com/lob/lob-typescript-sdk)

#### Installation <a href="#installation-3" id="installation-3"></a>

Lob's TypeScript SDK can be installed through NPM:\
`$ npm i @lob/lob-typescript-sdk`

To build and install from the latest source:\
`$ git clone git@github.com:lob/lob-typescript-sdk.git`

`$ npm install`

Learn more at the [lob-typescript-sdk](https://www.github.com/lob/lob-typescript-sdk) repository on GitHub.
{% endtab %}

{% tab title="PHP" %}

#### ![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1647371919748-github-svgrepo-com.svg)  [lob-php](https://github.com/lob/lob-php) <a href="#installation-5" id="installation-5"></a>

#### Installation <a href="#installation-5" id="installation-5"></a>

The recommended way to install lob-php is through Composer.

Install Composer

`curl -sS https://getcomposer.org/installer | php`

Add Lob.com PHP client as a dependency

`composer require lob/lob-php`

After installing, you need to require Composer's autoloader:

`require 'vendor/autoload.php';`

Learn more at the [lob-php](https://www.github.com/lob/lob-php) repository on GitHub.
{% endtab %}

{% tab title="Java" %}

#### ![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1647371919748-github-svgrepo-com.svg) [lob-java](https://github.com/lob/lob-java) <a href="#installation-7" id="installation-7"></a>

#### Installation <a href="#installation-7" id="installation-7"></a>

Include the following in your pom.xml for Maven:

```java
 <dependencies>
  <dependency>
    <groupId>com.lob</groupId>
    <artifactId>lob-java</artifactId>
    <version>13.0.0</version>
  </dependency>
  ...
 </dependencies>
```

Gradle:\
`compile 'com.lob:lob-java:13.0.0'`

Learn more at the [lob-java](https://www.github.com/lob/lob-java) repository on GitHub.
{% endtab %}

{% tab title="Python" %}
[![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1647371919748-github-svgrepo-com.svg)](https://github.com/lob/lob-python)  [lob-python](https://github.com/lob/lob-python)

#### Installation <a href="#installation-9" id="installation-9"></a>

You can use pip to install the package:

`pip install lob`

To initialize the wrapper, import lob and set the api\_key:

`import lob`&#x20;

`lob.api_key = 'your-api-key'`

Learn more at the [lob-python](https://www.github.com/lob/lob-python) repository on GitHub.
{% endtab %}

{% tab title="Ruby" %}
[![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1647371919748-github-svgrepo-com.svg)](https://github.com/lob/lob-ruby)  [lob-ruby](https://github.com/lob/lob-ruby)

#### Installation <a href="#installation-11" id="installation-11"></a>

Add this line to your application's Gemfile:\
`gem 'lob'`

And then execute:

`$ bundle`

Or manually install it yourself:

`$ gem install lob`

Learn more at the [lob-ruby](https://www.github.com/lob/lob-ruby) repository on GitHub.
{% endtab %}

{% tab title="Elixir" %}
[![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1647371919748-github-svgrepo-com.svg)](https://github.com/lob/lob-elixir)  [lob-elixir](https://github.com/lob/lob-elixir)

#### Installation <a href="#installation-13" id="installation-13"></a>

The package can be installed by adding :lob\_elixir to your list of dependencies in mix.exs:

```
def deps do
   [
     {:lob_elixir, "~> 1.5.0"}
   ]
 end
```

Learn more at the [lob-elixir](https://www.github.com/lob/lob-elixir) repository on GitHub.
{% endtab %}

{% tab title="C#/.NET" %}
[![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1647371919748-github-svgrepo-com.svg)](https://github.com/lob/lob-elixir)  [lob-dotnet](https://github.com/lob/lob-dotnet)
{% endtab %}

{% tab title="Go" %}
[<img src="https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1647371919748-github-svgrepo-com.svg" alt="" data-size="original">](https://github.com/lob/lob-ruby)  lob-go
{% endtab %}
{% endtabs %}

**Don’t see your favorite language?**

Let us know which language you’d like us to support next.  Drop us an [email.](mailto:lob-openapi@lob.com)

## Libraries <a href="#libraries-4" id="libraries-4"></a>

### Address Elements <a href="#address-elements-5" id="address-elements-5"></a>

Address Elements works by targeting the input elements of your address form and using their values with Lob's **verification** and **autocomplete** functionality.

{% tabs %}
{% tab title="JavaScript" %}
[![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1647371919748-github-svgrepo-com.svg)](https://github.com/lob/address-elements) [address-elements](https://github.com/lob/address-elements)

**Registration**

Create an account at [Lob.com](https://dashboard.lob.com/#/register) to obtain a **Live Public API Key**. The key is available in the [Lob settings panel](https://dashboard.lob.com/#/settings) and uses the format, `live_pub_*`.

**Usage**

Embed the Lob Address Elements script immediately before the closing tag in the HTML containing your address form. The script will autodetect your form and its inputs.

```
<script src="https://cdn.lob.com/lob/address-elements/2.2.1/address-elements.min.js" data-lob-key="live_pub_xxx">
```

Learn more at the [address-elements](https://www.github.com/lob/address-elements) repository on GitHub.
{% endtab %}

{% tab title="React" %}
[![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1647461208700-npm-svgrepo-com.svg)](https://www.npmjs.com/package/@lob/react-address-autocomplete) [react-address-autocomplete](https://www.npmjs.com/package/@lob/react-address-autocomplete)

This is a very lightweight component that uses the Lob Autocomplete API in order to simplify the process of adding in a search autocomplete bar or form. Check out the Autocomplete API for more configuration options in [Lob documentation](https://docs.lob.com/#operation/autocompletion).

**Installation**

```
npm install --save @lob/react-address-autocomplete
```

Learn more at the [react-address-autocomplete](https://www.npmjs.com/package/@lob/react-address-autocomplete) NPM repository.

![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1647461616365-autocompleteDemo.gif)
{% endtab %}
{% endtabs %}