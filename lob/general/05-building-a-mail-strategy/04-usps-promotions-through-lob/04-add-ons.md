# Add-Ons

## Informed Delivery

### **What is the Informed Delivery add-on?**

Informed Delivery by USPS enhances the traditional mail experience by providing subscribers with a **daily email preview** of their incoming mail. The email also includes a **ride-along image**: a small, full-color, interactive image that links to a target URL. This additional content reinforces your mailpiece’s messaging and call-to-action while providing a digital touchpoint for engagement.

As of March 2025, 72.9 million mail recipients are subscribed to USPS’s Informed Delivery program.

**In order to qualify for the Informed Delivery Add-On, your mailpiece must be approved for an&#x20;*****active*****&#x20;base promotion on the date of mailing.**

Here’s everything you need to know to qualify for an additional **1% discount**.

**How can I sign up for Informed Delivery through Lob?**&#x20;

### Opt-in to the promotion

To get started, log into the Lob Promotions Portal:&#x20;

<https://dashboard.lob.com/promotions/available-promotions>

### 1. Select the available promotion

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2Flvp7AIo0t42QyqEoe29f%2FScreenshot%202025-12-18%20at%202.37.29%E2%80%AFPM.png?alt=media&#x26;token=28d737a6-fc65-43d3-ac47-86d34743c3d6" alt=""><figcaption></figcaption></figure>

### 2. Send an Informed Delivery Campaign

You can send an Informed Delivery campaign via **API** or **Campaigns** in Lob.

<mark style="color:$info;">Option 1: Send via API</mark>

1. **POST campaign data:**\
   Use the Lob API to send the <mark style="color:red;">`informed_delivery_campaign`</mark> and retrieve a <mark style="color:red;">`campaign_id`</mark>.
2. **Include required fields:**
   1. [Ride-along image](https://help.lob.com/print-and-mail/designing-mail-creatives/maximizing-engagement/informed-delivery%23what-makes-a-great-ride-along-image)
   2. Promotional URL
   3. Campaign size
3. **Optional fields:**
   1. Brand name: Defaults to the company name in Lob unless specified.
   2. Representative image: A sample image of the mailpiece. This should reflect all mailers in the campaign and **must not include PII**. If omitted, USPS will display a scan of the mailpiece instead.
4. **Validate campaign:**\
   After a successful POST, receive the <mark style="color:red;">`campaign_id`</mark> and confirm qualification for existing promotions.
5. **Send mail:**\
   Include the <mark style="color:red;">`informed_delivery_campaign_id`</mark> in your submission to Lob as usual.

<mark style="color:$info;">Option 2: Send via Lob Campaigns</mark>

1. **Set up campaign:**\
   Begin your campaign setup in Lob Campaigns.
2. **Enable Informed Delivery:**
   1. When prompted, select the option to use **Informed Delivery**.
   2. Choose from available approved promotions obtained in Step 1.
3. **Enter campaign details:**
   1. Promotional URL
   2. Upload the Ride-Along Image.&#x20;
4. **Ride-Along Image specifications:**
   1. Format: JPG
   2. Dimensions: 500x780 pixels
   3. Max file size: 200KB
5. Optional fields:
   1. **Brand name:** Appears in the Informed Delivery email sent to subscribers. Defaults to your company name in Lob unless customized.
   2. **Representative image:** A sample of your mailpiece (similar rules as for API campaigns apply).
6. **Launch campaign:**\
   Complete your setup and submit. Lob ensures that the mailpiece adheres to USPS’s Informed Delivery standards.

### Sustainability:

**What is the USPS Sustainability Add-On?**\
The USPS Sustainability Add-On rewards businesses that use environmentally friendly materials in their print production by offering an additional **1% discount** on all eligible mailpieces. This add-on promotes eco-conscious practices and helps businesses reduce their environmental impact.

**How can I take advantage of the USPS Sustainability Add-On through Lob?**\
As long as you opt into the Sustainability Add-On in the USPS Promotions Portal, any mailpiece tied to a USPS promotion will automatically receive the 1% Sustainability add-on.&#x20;