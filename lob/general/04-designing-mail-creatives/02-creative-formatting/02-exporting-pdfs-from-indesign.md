# PDF preflight checklist

## **What is preflight?**&#x20;

Preflight is a print industry standard term for checking files for things that might cause issues in the physical output before you start the printing process. It is however NOT a standard set of checks or ways to solve those problems. Every printer has its own flavor of Preflight that does the checks and/or resolution steps in a different order.

Lob’s preflight module requires each file to meet the PDF-X/1a standard. PDF-X/1a is a standard for creating reliable and predictable PDF files for print production. (The "X-1a" part refers to the specific version of the PDF/X standard, which has certain requirements and restrictions to ensure compatibility and consistency.) To render and execute your campaigns quickly, and at scale, our ability to audit every file is limited. We run an automated check—where fixes are automatically applied—but in doing so, it may negatively impact your mailpieces.&#x20;

**To ensure each mailpiece is rendered exactly like you intend, please submit print-ready files by following the preflight checklist below.**

## Requirements for static PDFs

<details>

<summary>Must be PDF/X-1a compliant</summary>

If you have Adobe Acrobat Pro, you can use the Preflight function to run a report on your PDF which will alert the issues with your PDF file and also allow you to fix/convert the PDF file to PDF/X-1a format.

To perform these actions in Adobe Acrobat, please follow the steps outlined below:

### How to review: <a href="#vtt9l5sivqnw" id="vtt9l5sivqnw"></a>

1\) Open Acrobat and the desired PDF

2\) Access the Production tools by clicking on **(View > Tools > Print Production**) from your window pane. Alternatively, you can locate it on the right-hand side of the screen under search tools by expanding the Print Production tab.

<img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2F9hZ4UDsL6laSoD21Z38M%2F0.png?alt=media" alt="" data-size="original">

3\) Once the Print Production tools are open, click on the **Preflight** option.

4\) In the Preflight window, select the **"PDF/X”** tab.

<img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FBFNgBa7Xy4Ey77Cg7yGo%2F1.png?alt=media" alt="" data-size="original">

5\) Choose the option "**Convert to PDF/X-1a (Coated GRACoL 2006)”**

6\) You then have two options:

* If you want to generate a report detailing errors in your PDF file, click on the **“Analyze”** button.
* To analyze and fix any identified issues click the **"Analyze and Fix**" button. \*\***This option will also save your file in PDF/X-1a format.\*\***

### How to Save: <a href="#dsolao16sval" id="dsolao16sval"></a>

1. Select the PDF file that you want to convert to PDF/X.
2. Once the PDF document is open, go to the “File” menu option and choose “Save As”

<img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FrosJl0VwbazAguALxm4G%2F2.png?alt=media" alt="" data-size="original">

3. In the “Save As” dialog box, specify the desired location on your computer to save the converted file. Choose a recognizable name for the converted PDF/X-1a file.
4. Next, look for a dropdown menu or an option that allows you to select the file format. Click on the **PDF/X** option.

<img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FsJLz9824LCiSywPjFJJJ%2F3.png?alt=media" alt="" data-size="original">

5. Next, configure the settings:

* Select **Save as PDF/X-1a**
* Select **Convert to PDF/X-1a (Coated GracOL 2006)**

6. Click the “OK” button to initiate the conversion process.
7. Depending on the size and complexity of the original PDF file, the conversion process may take a few moments or longer. You may see a progress bar indicating the status of the conversion.
8. Once the conversion is complete, the software will save the PDF/X-1a file to the specified location on your computer.

</details>

<details>

<summary>Flatten transparency</summary>

If transparencies are not flattened, overlapping colors may change and objects may disappear completely. To ensure predictable and accurate print results, it is generally recommended to flatten transparencies before submitting the file over to Lob for printing. Flattening eliminates potential issues and helps create a final output that closely matches the intended design.

### How to review: <a href="#dhsv0f7dhmn5" id="dhsv0f7dhmn5"></a>

1. Open the pdf you want to check
2. Open Print Production tools (View > Tools > Print Production)
3. Click Preflight
4. Click the PDF/X tab
5. Click convert to PDF/X1-a (coated GRACoL 2006)
6. Click on the Analyze button.
7. The preflight tool will return information on where transparency was applied.

<img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FOn0eF3QbFcK6dbSzYrbU%2F5.png?alt=media" alt="" data-size="original">

### How to save: <a href="#x7hvj6p3i854" id="x7hvj6p3i854"></a>

1. Open PDF file to flatten
2. Open Print Production > Flattener preview
3. Select Transparent Objects from the dropdown for highlight, any transparencies will be highlighted in red.

<img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FILZyrjzBOwtGr3w7AJbP%2F6.png?alt=media" alt="" data-size="original">

4\. If you’re unable to select the Transparent object instead have the option to select None (Color Preview) which means the file doesn’t have any transparencies.

5\. Click Apply.

</details>

<details>

<summary>Remove layers</summary>

When you create a PDF from layered documents using software, such as Adobe InDesign or Adobe Photoshop, your PDF can contain multiple layers with different content on each one. If you submit the PDF file as is, you will only print the layer that is visible onscreen as opposed to all visual elements from various layers. To avoid this issue, you want to flatten your PDF file for print. Flattening a PDF before print removes transparency information and converts it to a format that the printer can read. Ensure the creative/PDF file you’re submitting over is flat and there is just one single layer prior to submission.

### How to review: <a href="#id-3uyfd2u47mne" id="id-3uyfd2u47mne"></a>

1. Open the PDF file or creative you want to check.
2. Click on the layers icon on the left panel as shown in the screenshot below.
3. If there are layers on your file, they will be listed as Layer 1, Layer 2, etc.., under Layers

<img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FBEExYBFVKxO3Udy3OwE6%2F7.png?alt=media" alt="" data-size="original">

### How to remove <a href="#wk3mpr10k6sa" id="wk3mpr10k6sa"></a>

Follow the above three steps, then click on the layer icon and select the Flatten Layers option.

<img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2F67lNy7WisbBj54ktgPMR%2F8.png?alt=media" alt="" data-size="original">

Alternatively, you can flatten the PDF to remove layers and transparencies. Please check - How to Save a File under flattening transparencies.

</details>

<details>

<summary>Fonts must be embedded</summary>

Please note the [font types](https://help.lob.com/print-and-mail/designing-mail-creatives/creative-formatting#supported-font-formats-16) Lob can and cannot support.

Fonts must be outlined (preferred) or[ embedded.](https://support.microsoft.com/en-us/office/embed-fonts-in-a-publication-to-ensure-their-availability-644449b9-22ab-4c80-9ffe-a7ddc183a650) Fonts that have not been outlined or embedded might change or render incorrectly, specific letters may be substituted with incorrect glyphs.

### How to review: <a href="#cywg2mbcuppt" id="cywg2mbcuppt"></a>

1. Go to "File" and choose "Open" to select the PDF file you want to check the fonts.
2. Click on "File" and then select "Properties" from the dropdown menu.
3. Access the Fonts tab: In the Properties dialog box, click on the "Fonts" tab.
4. Check font embedding status: You will see a list of fonts used in the PDF document. Look for fonts that are listed as "Not Embedded" or "Embedded Subset."

<img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FjtHpsNulouWIW7bKxbef%2F9.png?alt=media" alt="" data-size="original">

If the above is not true for your PDF file, you will have to follow the below instructions on how to embed fonts in PDF.

### How to save/embed fonts: <a href="#id-10v58sd16tjr" id="id-10v58sd16tjr"></a>

If you are using InDesign, export PDF with PDF/X1a setting and all fonts will be embedded. Likewise, if you are using Microsoft Word, “save as Adobe PDF” (not Microsoft's “save as PDF”) choose the High Quality Print settings, and all fonts will be embedded.

If you no longer have access to the original document and all you have is the PDF file with fonts that aren't embedded, Acrobat does provide a fix for embedding fonts via the Preflight feature. There is a fix for embedding missing fonts. Note that this requires that (1) the missing fonts are actually installed on your system and (2) the fonts themselves do not prohibit embedding in a PDF file.

1. To embed a new font, go to File > Print and then select Adobe PDF. Click Properties.
2. Select the Adobe PDF settings tab at the end and then click the EDIT button to the right of the default settings.
3. Next, a left menu of folders will appear in the pop up window. Click Fonts, then make sure the fonts you need to embed are on the fonts source list. If so, tick the box at the top that says Embed all fonts.
4. If they are not, then you will need to close the pop up window and either move or duplicate the fonts files from where you have stored them to C:/Windows/Fonts. If you struggle to find this then you can search for the folder in the search bar on the launcher menu.
5. All fonts you want to embed in the PDF should be in the Fonts source list. You now need to move the desired fonts to the Always Embed box.
6. Click OK on the pop-up window and you’re done.

Please note that font embedding may increase the file size of the PDF document.

</details>

<details>

<summary>File size under 5MB</summary>

Lower file size allows for easier processing at the print level. Large files have a higher potential to fail

### How to review: <a href="#kdmqwajyen75" id="kdmqwajyen75"></a>

1. Open the PDF file that you’re looking to check.
2. Click File > Properties. Under the Description tab check for "File Size" where you should be able to see the size of the file.

<img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FQlNALaPpmhUEChHBYVaI%2F10.png?alt=media" alt="" data-size="original">

### How to compress: <a href="#skedmxuzu076" id="skedmxuzu076"></a>

1. Open the PDF you wish to re-save as a smaller file.
2. Choose File, "Save as Other," and then "Reduced Size PDF."

### ![](https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2F0dnFbFPUUKFAoSMaCdKb%2F11.png?alt=media) <a href="#c3kjcfb13htt" id="c3kjcfb13htt"></a>

</details>

<details>

<summary>Color in CMYK</summary>

The color should be CMYK Color Space (SWOP v2 or GRACoL 2006/2013 preferred). By submitting CMYK you will avoid potential conversion errors when Lob changes RGB to CMYK.

### How to review: <a href="#vqbobcikypsw" id="vqbobcikypsw"></a>

1. Open the pdf you want to check the color profile for
2. Open Print Production tools (View > Tools > Print Production > Output Preview
3. Under Show > select dropdown CMYK.
4. This will show the area which is in the CMYK profile.

<img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2F6wGB890vbFHilb5HqrMb%2F12.png?alt=media" alt="" data-size="original">

### How to save: <a href="#m302fiypftgq" id="m302fiypftgq"></a>

1. Open the pdf you want to save
2. Open Print Production tools (View > Tools > Print Production)
3. Click Preflight
4. Click the PDF/X tab
5. Click convert to PDF/X1-a GRACoL 2006)
6. Click on Analyze and Fix button.

This will save the file in CMYK format.

</details>

<details>

<summary>Image resolution at 300 ppi</summary>

Image resolution should be 300 ppi. If the resolution is below 300 ppi, you may see pixelation and incorrect color saturation of your images; if ppi greatly exceeds 300 the file size will be too large and have the potential to fail.

### How to review: <a href="#id-43bbu0pdxav3" id="id-43bbu0pdxav3"></a>

To determine the resolution of an image in pixels per inch (PPI) on a Mac, you can use the built-in Preview application. Here's how:

1. Locate the image file on your Mac and select it.
2. Right-click (or Control-click) on the image file and select "Open With" from the context menu.
3. Choose "Preview" from the submenu. The image will open in the Preview application.
4. In Preview, click on the "Tools" menu at the top and select "Show Inspector". A sidebar with image information will appear.
5. In the Inspector sidebar, click on the "General" tab. You should see information about the image, including its dimensions, file size, and resolution.
6. Look for the "Resolution" field, which will display the image's PPI value.

<img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2F0OpjkplMnXdNWaMJCh5z%2F13.png?alt=media" alt="" data-size="original">

Please note that not all images may contain PPI information. In such cases, you can still determine the image's dimensions in pixels and calculate the PPI manually by dividing the pixel dimensions by the desired print dimensions.

</details>

<details>

<summary>No printer marks</summary>

Do not submit printer marks (or trim lines) including, but not limited to crop marks, trim marks, bleed marks, slug lines, registration marks, color bars, page information, etc.

Our production facilities have several QA standards in place to ensure cuts are made appropriately and the color is correct. Any content uploaded is treated as part of the design, and thus the printer marks will cause the dimensions to be larger than the intended image size, resulting in an error. If you are exporting an image for a printing proof the way you usually would when sending images to traditional printers, then the trim lines should be unticked in your settings to ensure a sizing error does not occur.

### How to review: <a href="#fqixgx8ay99" id="fqixgx8ay99"></a>

The below marks are referred to as the printer marks. Lob's APIs will not accept printer marks (or trim lines).

<img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FJZwEJBomxmlpEdmxrvLK%2F14.png?alt=media" alt="" data-size="original">

### How to remove: <a href="#id-3tl5me3050rd" id="id-3tl5me3050rd"></a>

Avoid having any printer's marks in your PDF by ensuring your image export settings do not include them. To remove these trim lines and color bars from your PDF, open your file in Adobe Acrobat, go to **Settings**, and clear the **Printer’s Marks** checkbox.

Note that whether or not you export with “Bleed” will depend on how you built your template. If you already manually added the bleed (e.g. 4.25" x 6.25" artwork), then you should have that unticked as well.

See also: How to download a profile on Acrobat to remove the printer marks on[ Youtube](https://www.youtube.com/watch?v=4kJS7PjKnsc).

</details>

<details>

<summary>Other considerations</summary>

* Adjust margins and borders to ensure they meet the printer's specifications and accommodate any necessary trimming.
* Page boxes (ArtBox, CropBox, TrimBox, and MediaBox) should all be consistently sized
* Set the correct page size and orientation.
* Bleed: Ensure the document has sufficient bleed (if needed) to avoid any white borders around the printed area.

### Page elements <a href="#qbyllhkwcito" id="qbyllhkwcito"></a>

* Double-check that all text is spelled correctly and positioned correctly on the page.
* Verify that images, logos, and graphics are in the correct locations and are of high quality.
* Ensure that important content is not too close to the edge to prevent it from being cut off during trimming or binding.

</details>
