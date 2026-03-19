# Checks

## Checks overview <a href="#checks-overview-0" id="checks-overview-0"></a>

To get started with sending checks, you'll need to [create a bank account](#create-a-new-bank-account) to originate checks from. You will also identify which [check template](#check-dimensions-specs-1) and [signature image](#signature-image-file-7) you want associated with the account, then Lob will [verify your account](#verifying-your-bank-account-4). This process is outlined below.

**Just looking for check specs?** Skip ahead to [Check dimensions & specs](#check-dimensions-specs-1-1) here.

More resources: Once you have setup your Bank Account, visit our [Checks API documentation](https://docs.lob.com/#tag/Checks), [GitHub library](https://github.com/lob/examples/), or our [Template Gallery](https://www.lob.com/template-gallery#checks) for ideas on how to get started.&#x20;

## Create a new Bank Account

In the dashboard, see the Bank Accounts section (under Print & Mail):

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2F05izBvQvs2u4bol5MDTy%2FNewBankAccount.png?alt=media&#x26;token=4fa6690c-c8f3-47e8-ba9e-8ae4aff53cb8" alt=""><figcaption></figcaption></figure>

You can also add a bank account [via our Bank Accounts API](https://docs.lob.com/#tag/Bank-Accounts) but note you are unable to upload a signatory image via this method.&#x20;

## Check templates <a href="#check-dimensions-specs-1" id="check-dimensions-specs-1"></a>

In the “Bank Accounts” section of your dashboard (under Print & Mail) you will select which template you would like to associate with your bank under the “Check Template Type”.

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FjWPIwg5zTqHNv8YyZ4bT%2FCheckTemplateType.png?alt=media&#x26;token=d617ba4e-b4c5-40c9-8e18-655fe504ac80" alt="" width="375"><figcaption></figcaption></figure>

We offer two options when it comes to check templates:

**Common Check:** This is the universal check we have offered that is accepted at the majority of banks across the US.

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2F0zOHfuq9TWEPyc90yoWT%2FCheck2.png?alt=media&#x26;token=a213a0af-8058-4335-b1b0-c5995266ae9c" alt=""><figcaption><p>Common check</p></figcaption></figure>

**JPM Check:** This is the JPM check template that is approved by JP Morgan Chase and utilizes Positive Pay.&#x20;

{% hint style="info" %}
If you are using the JPM Check template, you will need to add additional information (Bank City, State, Zip, and Fractional Routing Number).
{% endhint %}

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FB1I9uHDpiuVpVs3rzI1u%2FCheckJPM.png?alt=media&#x26;token=8669dde8-c9b2-4d0e-8413-d22cec6c2d1d" alt=""><figcaption><p>JPM check</p></figcaption></figure>

### Check with your bank <a href="#check-with-your-bank-3" id="check-with-your-bank-3"></a>

Check with your bank to make sure that the check will be accepted. A new check template or different signatory can cause the bank to flag your account. The best way to avoid this happening is to let your bank know that the checks are valid.

Your money is not transferred to Lob. When the payee deposits the check that was sent through Lob's Checks API, it will pull money directly from the specified bank account into the recipient's bank account.

## Uploading a signature for checks <a href="#uploading-a-signature-for-checks-6" id="uploading-a-signature-for-checks-6"></a>

One of the options for associating a custom signature to a bank account, so that it can be printed on checks, is uploading an image file when you create a Bank Account in the Lob dashboard.&#x20;

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FXRl54RILQSTqgUghe95R%2FAdd%20Signature.png?alt=media&#x26;token=513dc065-26e5-4a09-8280-934c0902d336" alt=""><figcaption></figcaption></figure>

### Signature image file  <a href="#signature-image-file-7" id="signature-image-file-7"></a>

The uploaded signature will be printed on all Lob checks originating from that specific bank account. Make sure to download the digital signature and authorize its use with your bank once your bank account is created.

If you would like to upload a new custom image file as a signature anytime after the initial creation of the bank account, you must reach out to <support@lob.com> with:

* The `bank_account_id` of the bank account that corresponds with the signature
* A PNG of the signature (the background of the image must be transparent)

{% hint style="info" %}
When an image for the signature isn’t provided, we implement a cursive font rendering of the signatory’s name instead.
{% endhint %}

Below are the guidelines to adhere to when prepping your image so that the signature can best be extracted and processed.

#### **Image format**

The image must be in either a JPEG or PNG format (.jpg, .jpeg, .png). The background of the image must be transparent.

#### **Dimensions**

The image must be at least 330px x 105px. The image may be larger but we recommend a width to height ratio of approximately 3:1 for best results.

#### **Color and size**

![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1641887754228-1641887754228.png)

The signature must be written in black or dark ink on a white or light background. The signature should be centered and should occupy most of the image.

### Things to avoid <a href="#things-to-avoid-11" id="things-to-avoid-11"></a>

Here are a few of the most common mistakes that we recommend you avoid when preparing a signature image.

{% hint style="warning" %}
**DON'T: Have the signature too small in your uploaded image.**
{% endhint %}

![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1641887361556-1641887361556.png)

Make sure to center your signature and crop your image as needed so that the signature takes up a majority of the space.

{% hint style="warning" %}
**DON'T: Write your signature on ruled or patterned paper.**
{% endhint %}

![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1641887773971-1641887773971.png)

Write your signature on a white or light-colored background to ensure proper signature processing. Using ruled or patterned paper will likely result in unintended artifacts.

{% hint style="warning" %}
**DON'T: Include other objects or artifacts in your image other than the signature.**
{% endhint %}

![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1641887785050-1641887785050.png)

If you are taking a photo of your signature rather than using a scanned image, make sure to prepare your photo so that all artifacts and non-signature objects (e.g. tables, pens, dark shadows) are cropped out.

## Verifying your bank account <a href="#verifying-your-bank-account-4" id="verifying-your-bank-account-4"></a>

Lob will send two micro-deposits, ranging from 1 - 100 cents, to the specified bank account in order to verify the account. You'll be asked to enter them in the dashboard or submit them through the API before you can send out any checks.

This is especially important if you are sending checks on behalf of your customers. You must verify all your customers' bank accounts before sending checks from them. This is most easily done through the API.

{% hint style="danger" %}
Lob's Check service only works with US banks, based on US banking standards and formats. We do not support foreign bank accounts at this time.
{% endhint %}

![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1648941588842-1648941588842.png)

### Fraudulent activity <a href="#fraudulent-activity-5" id="fraudulent-activity-5"></a>

Our security team continuously reviews newly-created accounts. New accounts that trigger a flag will be immediately suspended and required to provide additional verification.

### Limitations

{% hint style="info" %}
If you send a high volume of checks, send checks in very high dollar amounts, or you are sending HIPPA data, you may need to upgrade your [Print & Mail edition](https://dashboard.lob.com/#/settings/editions) to gain access to this form factor, or reach out to our [sales team](https://www.lob.com/sales) to learn more.
{% endhint %}

If you have any questions or concerns about the safe-guards we have in place around the use of checks, please [contact us](https://www.lob.com/contact).

## Check dimensions & specs <a href="#check-dimensions-specs-1" id="check-dimensions-specs-1"></a>

The specifications for Lob's check product are as follows:

* Measures 8.5 x 3.625" in size
* Contains warning bands, void indication, and security weaver on backer
* [Paper](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/check_bottom_template.pdf) is perforated with the bottom ⅔ of the page available for the sender to customize with artwork
* Uses fugitive ink to provide additional protection against duplication of the document
* Includes a prismatic multicolored background with subtle graduations to make copying and reproducing difficult
* Produced with controlled stock, which ensures the security of the mail piece at every stage of production. The Padlock Icon printed on the checks ensures that the product meets or exceeds industry guidelines
* Mailed in a #10 white outer envelope (double-windowed)

{% hint style="info" %}
Note that logos and branding can be added to checks via an [API request](https://docs.lob.com/#operation/check_create), but cannot be added through the dashboard. For more details on the space your logo can take up, visit our [API documentation](https://docs.lob.com/#operation/check_create).
{% endhint %}

|                                                                                                                        Check front                                                                                                                        |                                                                                                                         Check back                                                                                                                        |
| :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![](https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FipQyddGyQ09pz1crAVNN%2FScreenshot%202023-03-02%20at%202.15.11%20PM.png?alt=media\&token=1aa8f798-33bd-4481-a1a3-606bf138d4ab) | ![](https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2Fo07wD3NglcOzr6B5imyg%2FScreenshot%202023-03-02%20at%202.15.40%20PM.png?alt=media\&token=ff9b2d67-2b27-4139-a453-36ed61746d76) |

## Customizing check pages <a href="#customizing-check-pages-12" id="customizing-check-pages-12"></a>

You can choose to leverage the blank space at the **bottom of the check** by using `check_bottom` to add any branded artwork or personalization, even if these check pages themselves do not require any artwork in order to be sendable. &#x20;

It is also possible to send a letter as an **attachment** with your check (but not the other way around) by using the `attachment` string.&#x20;

If you choose to customize this optional bottom section of the check, be sure to follow the provided template and leave room for the actual check itself; otherwise you risk invalidating the check. You may also add up to 5 sheets (10 double-sided pages) of optional attachment pages.&#x20;

See our [Checks API documentation](https://docs.lob.com/#tag/Checks) for more details on the `check_bottom` and `attachment` parameters, or see the [Template Gallery](https://www.lob.com/template-gallery) for design inspiration.

* [Check bottom](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/check_bottom_template.pdf) (optional)
* [Check attachment](https://s3-us-west-2.amazonaws.com/public.lob.com/assets/templates/check_attachment_template.pdf) (optional)

{% hint style="warning" %}
Check bottoms and check attachments will **always** be printed in black and white.
{% endhint %}

|                                                   Check bottom template                                                  |                                                                                                                  Customized check example                                                                                                                 |
| :----------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| ![](https://static.helpjuice.com/helpjuice_production/uploads/upload/image/9583/direct/1641887927250-1641887927250.jpeg) | ![](https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FO92mSe9WIAPOQUmpxpIJ%2FScreenshot%202023-04-12%20at%202.15.20%20PM.png?alt=media\&token=ba9253fb-9deb-426b-a126-4943fd240aa9) |

## Mailing checks <a href="#mailing-checks-2" id="mailing-checks-2"></a>

Ensure your checks get to their final destination by following these guidelines:

* The `from` field is required for all checks, regardless of the destination
* Checks can only be mailed using[ First Class Mail](https://help.lob.com/print-and-mail/building-a-mail-strategy/mailing-classes-and-postage) (takes 4 to 6 business days)
* USPS [Standard Class](https://help.lob.com/print-and-mail/building-a-mail-strategy/mailing-classes-and-postage) Mail (Marketing Mail) and [Certified Mail](https://help.lob.com/print-and-mail/building-a-mail-strategy/mailing-classes-and-postage/certified-mail-or-registered-mail) **are not available for checks**
* Overnight mailing options are **not available for checks**