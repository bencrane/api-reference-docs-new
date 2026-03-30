> Sources:
> - https://trigger.dev/docs/guides/python/python-crawl4ai
> - https://trigger.dev/docs/guides/python/python-doc-to-markdown
> - https://trigger.dev/docs/guides/python/python-image-processing
> - https://trigger.dev/docs/guides/python/python-pdf-form-extractor

# Python Guides

## Python headless browser web crawler example

Learn how to use Python, Crawl4AI and Playwright to create a headless browser web crawler with Trigger.dev.

## Overview

This demo showcases how to use Trigger.dev with Python to build a web crawler that uses a headless browser to navigate websites and extract content.

## Prerequisites

* A project with [Trigger.dev initialized](/quick-start)
* [Python](https://www.python.org/) installed on your local machine

## Features

* [Trigger.dev](https://trigger.dev) for background task orchestration
* Our [Python build extension](/config/extensions/pythonExtension) to install the dependencies and run the Python script
* [Crawl4AI](https://github.com/unclecode/crawl4ai), an open source LLM friendly web crawler
* A custom [Playwright extension](https://playwright.dev/) to create a headless chromium browser
* Proxy support

## Using Proxies

<Warning>
  **WEB SCRAPING:** When web scraping, you MUST use a proxy to comply with our terms of service. Direct scraping of third-party websites without the site owner's permission using Trigger.dev Cloud is prohibited and will result in account suspension. See [this example](/guides/examples/puppeteer#scrape-content-from-a-web-page) which uses a proxy.
</Warning>

Some popular proxy services are:

* [Smartproxy](https://smartproxy.com/)
* [Bright Data](https://brightdata.com/)
* [Browserbase](https://browserbase.com/)
* [Oxylabs](https://oxylabs.io/)
* [ScrapingBee](https://scrapingbee.com/)

Once you have a proxy service, set the following environment variables in your Trigger.dev .env file, and add them in the Trigger.dev dashboard:

* `PROXY_URL`: The URL of your proxy server (e.g., `http://proxy.example.com:8080`)
* `PROXY_USERNAME`: Username for authenticated proxies (optional)
* `PROXY_PASSWORD`: Password for authenticated proxies (optional)

## GitHub repo

<Card title="View the project on GitHub" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/python-crawl4ai">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## The code

### Build configuration

After you've initialized your project with Trigger.dev, add these build settings to your `trigger.config.ts` file:

```ts trigger.config.ts theme={"theme":"css-variables"}
import { defineConfig } from "@trigger.dev/sdk";
import { pythonExtension } from "@trigger.dev/python/extension";
import type { BuildContext, BuildExtension } from "@trigger.dev/core/build";

export default defineConfig({
  project: "<project ref>",
  // Your other config settings...
  build: {
    extensions: [
      // This is required to use the Python extension
      pythonExtension(),
      // This is required to create a headless chromium browser with Playwright
      installPlaywrightChromium(),
    ],
  },
});

// This is a custom build extension to install Playwright and Chromium
export function installPlaywrightChromium(): BuildExtension {
  return {
    name: "InstallPlaywrightChromium",
    onBuildComplete(context: BuildContext) {
      const instructions = [
        // Base and Chromium dependencies
        `RUN apt-get update && apt-get install -y --no-install-recommends \
          curl unzip npm libnspr4 libatk1.0-0 libatk-bridge2.0-0 libatspi2.0-0 \
          libasound2 libnss3 libxcomposite1 libxdamage1 libxfixes3 libxrandr2 \
          libgbm1 libxkbcommon0 \
          && apt-get clean && rm -rf /var/lib/apt/lists/*`,

        // Install Playwright and Chromium
        `RUN npm install -g playwright`,
        `RUN mkdir -p /ms-playwright`,
        `RUN PLAYWRIGHT_BROWSERS_PATH=/ms-playwright python -m playwright install --with-deps chromium`,
      ];

      context.addLayer({
        id: "playwright",
        image: { instructions },
        deploy: {
          env: {
            PLAYWRIGHT_BROWSERS_PATH: "/ms-playwright",
            PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD: "1",
            PLAYWRIGHT_SKIP_BROWSER_VALIDATION: "1",
          },
          override: true,
        },
      });
    },
  };
}
```

<Info>
  Learn more about executing scripts in your Trigger.dev project using our Python build extension
  [here](/config/extensions/pythonExtension).
</Info>

### Task code

This task uses the `python.runScript` method to run the `crawl-url.py` script with the given URL as an argument. You can see the original task in our examples repository [here](https://github.com/triggerdotdev/examples/blob/main/python-crawl4ai/src/trigger/pythonTasks.ts).

```ts src/trigger/pythonTasks.ts theme={"theme":"css-variables"}
import { logger, schemaTask, task } from "@trigger.dev/sdk";
import { python } from "@trigger.dev/python";
import { z } from "zod";

export const convertUrlToMarkdown = schemaTask({
  id: "convert-url-to-markdown",
  schema: z.object({
    url: z.string().url(),
  }),
  run: async (payload) => {
    // Pass through any proxy environment variables
    const env = {
      PROXY_URL: process.env.PROXY_URL,
      PROXY_USERNAME: process.env.PROXY_USERNAME,
      PROXY_PASSWORD: process.env.PROXY_PASSWORD,
    };

    const result = await python.runScript("./src/python/crawl-url.py", [payload.url], { env });

    logger.debug("convert-url-to-markdown", {
      url: payload.url,
      result,
    });

    return result.stdout;
  },
});
```

### Add a requirements.txt file

Add the following to your `requirements.txt` file. This is required in Python projects to install the dependencies.

```txt requirements.txt theme={"theme":"css-variables"}
crawl4ai
playwright
urllib3<2.0.0
```

### The Python script

The Python script is a simple script using Crawl4AI that takes a URL and returns the markdown content of the page. You can see the original script in our examples repository [here](https://github.com/triggerdotdev/examples/blob/main/python-crawl4ai/src/python/crawl-url.py).

```python src/python/crawl-url.py theme={"theme":"css-variables"}
import asyncio
import sys
import os
from crawl4ai import *
from crawl4ai.async_configs import BrowserConfig

async def main(url: str):
    # Get proxy configuration from environment variables
    proxy_url = os.environ.get("PROXY_URL")
    proxy_username = os.environ.get("PROXY_USERNAME")
    proxy_password = os.environ.get("PROXY_PASSWORD")

    # Configure the proxy
    browser_config = None
    if proxy_url:
        if proxy_username and proxy_password:
            # Use authenticated proxy
            proxy_config = {
                "server": proxy_url,
                "username": proxy_username,
                "password": proxy_password
            }
            browser_config = BrowserConfig(proxy_config=proxy_config)
        else:
            # Use simple proxy
            browser_config = BrowserConfig(proxy=proxy_url)
    else:
        browser_config = BrowserConfig()

    async with AsyncWebCrawler(config=browser_config) as crawler:
        result = await crawler.arun(
            url=url,
        )
        print(result.markdown)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python crawl-url.py <url>")
        sys.exit(1)
    url = sys.argv[1]
    asyncio.run(main(url))
```

## Testing your task

1. Create a virtual environment `python -m venv venv`
2. Activate the virtual environment, depending on your OS: On Mac/Linux: `source venv/bin/activate`, on Windows: `venv\Scripts\activate`
3. Install the Python dependencies `pip install -r requirements.txt`
4. If you haven't already, copy your project ref from your [Trigger.dev dashboard](https://cloud.trigger.dev) and add it to the `trigger.config.ts` file.
5. Run the Trigger.dev CLI `dev` command (it may ask you to authorize the CLI if you haven't already).
6. Test the task in the dashboard, using a URL of your choice.

<Warning>
  **WEB SCRAPING:** When web scraping, you MUST use a proxy to comply with our terms of service. Direct scraping of third-party websites without the site owner's permission using Trigger.dev Cloud is prohibited and will result in account suspension. See [this example](/guides/examples/puppeteer#scrape-content-from-a-web-page) which uses a proxy.
</Warning>

## Deploying your task

Deploy the task to production using the Trigger.dev CLI `deploy` command.

## Learn more about using Python with Trigger.dev

<Card title="Python build extension" icon="code" href="/config/extensions/pythonExtension">
  Learn how to use our built-in Python build extension to install dependencies and run your Python
  code.
</Card>

---

## Convert documents to markdown using Python and MarkItDown

Learn how to use Trigger.dev with Python to convert documents to markdown using MarkItDown.

## Overview

Convert documents to markdown using Microsoft's [MarkItDown](https://github.com/microsoft/markitdown) library. This can be especially useful for preparing documents in a structured format for AI applications.

## Prerequisites

* A project with [Trigger.dev initialized](/quick-start)
* [Python](https://www.python.org/) installed on your local machine. *This example requires Python 3.10 or higher.*

## Features

* A Trigger.dev task which downloads a document from a URL and runs the Python script which converts it to markdown
* A Python script to convert documents to markdown using Microsoft's [MarkItDown](https://github.com/microsoft/markitdown) library
* Uses our [Python build extension](/config/extensions/pythonExtension) to install dependencies and run Python scripts

## GitHub repo

<Card title="View the project on GitHub" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/python-doc-to-markdown-converter">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## The code

### Build configuration

After you've initialized your project with Trigger.dev, add these build settings to your `trigger.config.ts` file:

```ts trigger.config.ts theme={"theme":"css-variables"}
import { pythonExtension } from "@trigger.dev/python/extension";
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  runtime: "node",
  project: "<your-project-ref>",
  // Your other config settings...
  build: {
    extensions: [
      pythonExtension({
        // The path to your requirements.txt file
        requirementsFile: "./requirements.txt",
        // The path to your Python binary
        devPythonBinaryPath: `venv/bin/python`,
        // The paths to your Python scripts to run
        scripts: ["src/python/**/*.py"],
      }),
    ],
  },
});
```

<Info>
  Learn more about executing scripts in your Trigger.dev project using our Python build extension
  [here](/config/extensions/pythonExtension).
</Info>

### Task code

This task uses the `python.runScript` method to run the `markdown-converter.py` script with the given document URL as an argument.

```ts src/trigger/convertToMarkdown.ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";
import { python } from "@trigger.dev/python";
import * as fs from "fs";
import * as path from "path";
import * as os from "os";

export const convertToMarkdown = task({
  id: "convert-to-markdown",
  run: async (payload: { url: string }) => {
    const { url } = payload;

    // STEP 1: Create temporary file with unique name
    const tempDir = os.tmpdir();
    const fileName = `doc-${Date.now()}-${Math.random().toString(36).substring(2, 7)}`;
    const urlPath = new URL(url).pathname;
    const extension = path.extname(urlPath) || ".docx";
    const tempFilePath = path.join(tempDir, `${fileName}${extension}`);

    // STEP 2: Download file from URL
    const response = await fetch(url);
    const buffer = await response.arrayBuffer();
    await fs.promises.writeFile(tempFilePath, Buffer.from(buffer));

    // STEP 3: Run Python script to convert document to markdown
    const pythonResult = await python.runScript("./src/python/markdown-converter.py", [
      JSON.stringify({ file_path: tempFilePath }),
    ]);

    // STEP 4: Clean up temporary file
    fs.unlink(tempFilePath, () => {});

    // STEP 5: Process result
    if (pythonResult.stdout) {
      const result = JSON.parse(pythonResult.stdout);
      return {
        url,
        markdown: result.status === "success" ? result.markdown : null,
        error: result.status === "error" ? result.error : null,
        success: result.status === "success",
      };
    }

    return {
      url,
      markdown: null,
      error: "No output from Python script",
      success: false,
    };
  },
});
```

### Add a requirements.txt file

Add the following to your `requirements.txt` file. This is required in Python projects to install the dependencies.

```txt requirements.txt theme={"theme":"css-variables"}
markitdown[all]
```

### The Python script

The Python script uses MarkItDown to convert documents to Markdown format.

```python src/python/markdown-converter.py theme={"theme":"css-variables"}
import json
import sys
import os
from markitdown import MarkItDown

def convert_to_markdown(file_path):
    """Convert a file to markdown format using MarkItDown"""
    # Check if file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    # Initialize MarkItDown
    md = MarkItDown()

    # Convert the file
    try:
        result = md.convert(file_path)
        return result.text_content
    except Exception as e:
        raise Exception(f"Error converting file: {str(e)}")

def process_trigger_task(file_path):
    """Process a file and convert to markdown"""
    try:
        markdown_result = convert_to_markdown(file_path)
        return {
            "status": "success",
            "markdown": markdown_result
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e)
        }

if __name__ == "__main__":
    # Get the file path from command line arguments
    if len(sys.argv) < 2:
        print(json.dumps({"status": "error", "error": "No file path provided"}))
        sys.exit(1)

    try:
        config = json.loads(sys.argv[1])
        file_path = config.get("file_path")

        if not file_path:
            print(json.dumps({"status": "error", "error": "No file path specified in config"}))
            sys.exit(1)

        result = process_trigger_task(file_path)
        print(json.dumps(result))
    except Exception as e:
        print(json.dumps({"status": "error", "error": str(e)}))
        sys.exit(1)
```

## Testing your task

1. Create a virtual environment `python -m venv venv`
2. Activate the virtual environment, depending on your OS: On Mac/Linux: `source venv/bin/activate`, on Windows: `venv\Scripts\activate`
3. Install the Python dependencies `pip install -r requirements.txt`. *Make sure you have Python 3.10 or higher installed.*
4. Copy the project ref from your [Trigger.dev dashboard](https://cloud.trigger.dev) and add it to the `trigger.config.ts` file.
5. Run the Trigger.dev CLI `dev` command (it may ask you to authorize the CLI if you haven't already).
6. Test the task in the dashboard by providing a valid document URL.
7. Deploy the task to production using the Trigger.dev CLI `deploy` command.

## MarkItDown Conversion Capabilities

* Convert various file formats to Markdown:
  * Office formats (Word, PowerPoint, Excel)
  * PDFs
  * Images (with optional LLM-generated descriptions)
  * HTML, CSV, JSON, XML
  * Audio files (with optional transcription)
  * ZIP archives
  * And more
* Preserve document structure (headings, lists, tables, etc.)
* Handle multiple input methods (file paths, URLs, base64 data)
* Optional Azure Document Intelligence integration for better PDF and image conversion

## Learn more about using Python with Trigger.dev

<Card title="Python build extension" icon="code" href="/config/extensions/pythonExtension">
  Learn how to use our built-in Python build extension to install dependencies and run your Python
  code.
</Card>

---

## Python image processing example

Learn how to use Trigger.dev with Python to process images from URLs and upload them to S3.

## Overview

This demo showcases how to use Trigger.dev with Python to process an image using Pillow (PIL) from a URL and upload it to S3-compatible storage bucket.

## Prerequisites

* A project with [Trigger.dev initialized](/quick-start)
* [Python](https://www.python.org/) installed on your local machine

## Features

* A [Trigger.dev](https://trigger.dev) task to trigger the image processing Python script, and then upload the processed image to S3-compatible storage
* The [Trigger.dev Python build extension](https://trigger.dev/docs/config/extensions/pythonExtension) to install dependencies and run Python scripts
* [Pillow (PIL)](https://pillow.readthedocs.io/) for powerful image processing capabilities
* [AWS SDK v3](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/s3/) for S3 uploads
* S3-compatible storage support (AWS S3, Cloudflare R2, etc.)

## GitHub repo

<Card title="View the project on GitHub" icon="GitHub" href="https://github.com/triggerdotdev/examples/tree/main/python-image-processing">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## The code

### Build configuration

After you've initialized your project with Trigger.dev, add these build settings to your `trigger.config.ts` file:

```ts trigger.config.ts theme={"theme":"css-variables"}
import { pythonExtension } from "@trigger.dev/python/extension";
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  runtime: "node",
  project: "<your-project-ref>",
  // Your other config settings...
  build: {
    extensions: [
      pythonExtension({
        // The path to your requirements.txt file
        requirementsFile: "./requirements.txt",
        // The path to your Python binary
        devPythonBinaryPath: `venv/bin/python`,
        // The paths to your Python scripts to run
        scripts: ["src/python/**/*.py"],
      }),
    ],
  },
});
```

<Info>
  Learn more about executing scripts in your Trigger.dev project using our Python build extension
  [here](/config/extensions/pythonExtension).
</Info>

### Task code

This task uses the `python.runScript` method to run the `image-processing.py` script with the given image URL as an argument. You can adjust the image processing parameters in the payload, with options such as height, width, quality, output format, etc.

```ts src/trigger/processImage.ts theme={"theme":"css-variables"}
import { schemaTask } from "@trigger.dev/sdk";
import { z } from "zod";
import { python } from "@trigger.dev/python";
import { promises as fs } from "fs";
import { S3Client } from "@aws-sdk/client-s3";
import { Upload } from "@aws-sdk/lib-storage";

// Initialize S3 client
const s3Client = new S3Client({
  region: "auto",
  endpoint: process.env.S3_ENDPOINT,
  credentials: {
    accessKeyId: process.env.S3_ACCESS_KEY_ID ?? "",
    secretAccessKey: process.env.S3_SECRET_ACCESS_KEY ?? "",
  },
});

// Define the input schema with Zod
const imageProcessingSchema = z.object({
  imageUrl: z.string().url(),
  height: z.number().positive().optional().default(800),
  width: z.number().positive().optional().default(600),
  quality: z.number().min(1).max(100).optional().default(85),
  maintainAspectRatio: z.boolean().optional().default(true),
  outputFormat: z.enum(["jpeg", "png", "webp", "gif", "avif"]).optional().default("jpeg"),
  brightness: z.number().optional(),
  contrast: z.number().optional(),
  sharpness: z.number().optional(),
  grayscale: z.boolean().optional().default(false),
});

// Define the output schema
const outputSchema = z.object({
  url: z.string().url(),
  key: z.string(),
  format: z.string(),
  originalSize: z.object({
    width: z.number(),
    height: z.number(),
  }),
  newSize: z.object({
    width: z.number(),
    height: z.number(),
  }),
  fileSizeBytes: z.number(),
  exitCode: z.number(),
});

export const processImage = schemaTask({
  id: "process-image",
  schema: imageProcessingSchema,
  run: async (payload, io) => {
    const {
      imageUrl,
      height,
      width,
      quality,
      maintainAspectRatio,
      outputFormat,
      brightness,
      contrast,
      sharpness,
      grayscale,
    } = payload;

    try {
      // Run the Python script
      const result = await python.runScript("./src/python/image-processing.py", [
        imageUrl,
        height.toString(),
        width.toString(),
        quality.toString(),
        maintainAspectRatio.toString(),
        outputFormat,
        brightness?.toString() || "null",
        contrast?.toString() || "null",
        sharpness?.toString() || "null",
        grayscale.toString(),
      ]);

      const { outputPath, format, originalSize, newSize, fileSizeBytes } = JSON.parse(
        result.stdout
      );

      // Read file once
      const fileContent = await fs.readFile(outputPath);

      try {
        // Upload to S3
        const key = `processed-images/${Date.now()}-${outputPath.split("/").pop()}`;
        await new Upload({
          client: s3Client,
          params: {
            Bucket: process.env.S3_BUCKET!,
            Key: key,
            Body: fileContent,
            ContentType: `image/${format}`,
          },
        }).done();

        return {
          url: `${process.env.S3_PUBLIC_URL}/${key}`,
          key,
          format,
          originalSize,
          newSize,
          fileSizeBytes,
          exitCode: result.exitCode,
        };
      } finally {
        // Always clean up the temp file
        await fs.unlink(outputPath).catch(console.error);
      }
    } catch (error) {
      throw new Error(
        `Processing failed: ${error instanceof Error ? error.message : "Unknown error"}`
      );
    }
  },
});
```

### Add a requirements.txt file

Add the following to your `requirements.txt` file. This is required in Python projects to install the dependencies.

```txt requirements.txt theme={"theme":"css-variables"}
# Core dependencies
Pillow==10.2.0            # Image processing library
python-dotenv==1.0.0      # Environment variable management
requests==2.31.0          # HTTP requests
numpy==1.26.3             # Numerical operations (for advanced processing)

# Optional enhancements
opencv-python==4.8.1.78   # For more advanced image processing
```

### The Python script

The Python script uses Pillow (PIL) to process an image. You can see the original script in our examples repository [here](https://github.com/triggerdotdev/examples/blob/main/python-image-processing/src/python/image-processing.py).

```python src/python/image-processing.py theme={"theme":"css-variables"}
from PIL import Image, ImageOps, ImageEnhance
import io
from io import BytesIO
import os
from typing import Tuple, List, Dict, Optional, Union
import logging
import sys
import json
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ImageProcessor:
    """Image processing utility for resizing, optimizing, and converting images."""

    # Supported formats for conversion
    SUPPORTED_FORMATS = ['JPEG', 'PNG', 'WEBP', 'GIF', 'AVIF']

    @staticmethod
    def open_image(image_data: Union[bytes, str]) -> Image.Image:
        """Open an image from bytes or file path."""
        try:
            if isinstance(image_data, bytes):
                return Image.open(io.BytesIO(image_data))
            else:
                return Image.open(image_data)
        except Exception as e:
            logger.error(f"Failed to open image: {e}")
            raise ValueError(f"Could not open image: {e}")

    @staticmethod
    def resize_image(
        img: Image.Image,
        width: Optional[int] = None,
        height: Optional[int] = None,
        maintain_aspect_ratio: bool = True
    ) -> Image.Image:
        """
        Resize an image to specified dimensions.

        Args:
            img: PIL Image object
            width: Target width (None to auto-calculate from height)
            height: Target height (None to auto-calculate from width)
            maintain_aspect_ratio: Whether to maintain the original aspect ratio

        Returns:
            Resized PIL Image
        """
        if width is None and height is None:
            return img  # No resize needed

        original_width, original_height = img.size

        if maintain_aspect_ratio:
            if width and height:
                # Calculate the best fit while maintaining aspect ratio
                ratio = min(width / original_width, height / original_height)
                new_width = int(original_width * ratio)
                new_height = int(original_height * ratio)
            elif width:
                # Calculate height based on width
                ratio = width / original_width
                new_width = width
                new_height = int(original_height * ratio)
            else:
                # Calculate width based on height
                ratio = height / original_height
                new_width = int(original_width * ratio)
                new_height = height
        else:
            # Force exact dimensions
            new_width = width if width else original_width
            new_height = height if height else original_height

        return img.resize((new_width, new_height), Image.LANCZOS)

    @staticmethod
    def optimize_image(
        img: Image.Image,
        quality: int = 85,
        format: Optional[str] = None
    ) -> Tuple[bytes, str]:
        """
        Optimize an image for web delivery.

        Args:
            img: PIL Image object
            quality: JPEG/WebP quality (0-100)
            format: Output format (JPEG, PNG, WEBP, etc.)

        Returns:
            Tuple of (image_bytes, format)
        """
        if format is None:
            format = img.format or 'JPEG'

        format = format.upper()
        if format not in ImageProcessor.SUPPORTED_FORMATS:
            format = 'JPEG'  # Default to JPEG if unsupported format

        # Convert mode if needed
        if format == 'JPEG' and img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')

        # Save to bytes
        buffer = io.BytesIO()

        if format == 'JPEG':
            img.save(buffer, format=format, quality=quality, optimize=True)
        elif format == 'PNG':
            img.save(buffer, format=format, optimize=True)
        elif format == 'WEBP':
            img.save(buffer, format=format, quality=quality)
        elif format == 'AVIF':
            img.save(buffer, format=format, quality=quality)
        else:
            img.save(buffer, format=format)

        buffer.seek(0)
        return buffer.getvalue(), format.lower()

    @staticmethod
    def apply_filters(
        img: Image.Image,
        brightness: Optional[float] = None,
        contrast: Optional[float] = None,
        sharpness: Optional[float] = None,
        grayscale: bool = False
    ) -> Image.Image:
        """
        Apply various filters and enhancements to an image.

        Args:
            img: PIL Image object
            brightness: Brightness factor (0.0-2.0, 1.0 is original)
            contrast: Contrast factor (0.0-2.0, 1.0 is original)
            sharpness: Sharpness factor (0.0-2.0, 1.0 is original)
            grayscale: Convert to grayscale if True

        Returns:
            Processed PIL Image
        """
        # Apply grayscale first if requested
        if grayscale:
            img = ImageOps.grayscale(img)
            # Convert back to RGB if other filters will be applied
            if any(x is not None for x in [brightness, contrast, sharpness]):
                img = img.convert('RGB')

        # Apply enhancements
        if brightness is not None:
            img = ImageEnhance.Brightness(img).enhance(brightness)

        if contrast is not None:
            img = ImageEnhance.Contrast(img).enhance(contrast)

        if sharpness is not None:
            img = ImageEnhance.Sharpness(img).enhance(sharpness)

        return img

    @staticmethod
    def process_image(
        image_data: Union[bytes, str],
        width: Optional[int] = None,
        height: Optional[int] = None,
        maintain_aspect_ratio: bool = True,
        quality: int = 85,
        output_format: Optional[str] = None,
        brightness: Optional[float] = None,
        contrast: Optional[float] = None,
        sharpness: Optional[float] = None,
        grayscale: bool = False
    ) -> Dict:
        """
        Process an image with all available options.

        Args:
            image_data: Image bytes or file path
            width: Target width
            height: Target height
            maintain_aspect_ratio: Whether to maintain aspect ratio
            quality: Output quality
            output_format: Output format
            brightness: Brightness adjustment
            contrast: Contrast adjustment
            sharpness: Sharpness adjustment
            grayscale: Convert to grayscale

        Returns:
            Dict with processed image data and metadata
        """
        # Open the image
        img = ImageProcessor.open_image(image_data)
        original_format = img.format
        original_size = img.size

        # Apply filters
        img = ImageProcessor.apply_filters(
            img,
            brightness=brightness,
            contrast=contrast,
            sharpness=sharpness,
            grayscale=grayscale
        )

        # Resize if needed
        if width or height:
            img = ImageProcessor.resize_image(
                img,
                width=width,
                height=height,
                maintain_aspect_ratio=maintain_aspect_ratio
            )

        # Optimize and get bytes
        processed_bytes, actual_format = ImageProcessor.optimize_image(
            img,
            quality=quality,
            format=output_format
        )

        # Return result with metadata
        return {
            "processed_image": processed_bytes,
            "format": actual_format,
            "original_format": original_format,
            "original_size": original_size,
            "new_size": img.size,
            "file_size_bytes": len(processed_bytes)
        }

def process_image(url, height, width, quality):
    # Download image from URL
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))

    # Resize
    img = img.resize((int(width), int(height)), Image.Resampling.LANCZOS)

    # Save with quality setting
    output_path = f"/tmp/processed_{width}x{height}.jpg"
    img.save(output_path, "JPEG", quality=int(quality))

    return output_path

if __name__ == "__main__":
    url = sys.argv[1]
    height = int(sys.argv[2])
    width = int(sys.argv[3])
    quality = int(sys.argv[4])
    maintain_aspect_ratio = sys.argv[5].lower() == 'true'
    output_format = sys.argv[6]
    brightness = float(sys.argv[7]) if sys.argv[7] != 'null' else None
    contrast = float(sys.argv[8]) if sys.argv[8] != 'null' else None
    sharpness = float(sys.argv[9]) if sys.argv[9] != 'null' else None
    grayscale = sys.argv[10].lower() == 'true'

    processor = ImageProcessor()
    result = processor.process_image(
        requests.get(url).content,
        width=width,
        height=height,
        maintain_aspect_ratio=maintain_aspect_ratio,
        quality=quality,
        output_format=output_format,
        brightness=brightness,
        contrast=contrast,
        sharpness=sharpness,
        grayscale=grayscale
    )

    output_path = f"/tmp/processed_{width}x{height}.{result['format']}"
    with open(output_path, 'wb') as f:
        f.write(result['processed_image'])

    print(json.dumps({
        "outputPath": output_path,
        "format": result['format'],
        "originalSize": result['original_size'],
        "newSize": result['new_size'],
        "fileSizeBytes": result['file_size_bytes']
    }))
```

## Testing your task

1. Create a virtual environment `python -m venv venv`
2. Activate the virtual environment, depending on your OS: On Mac/Linux: `source venv/bin/activate`, on Windows: `venv\Scripts\activate`
3. Install the Python dependencies `pip install -r requirements.txt`
4. Set up your S3-compatible storage credentials in your environment variables, in .env for local development, or in the Trigger.dev dashboard for production:
   ```
   S3_ENDPOINT=https://your-endpoint.com
   S3_ACCESS_KEY_ID=your-access-key
   S3_SECRET_ACCESS_KEY=your-secret-key
   S3_BUCKET=your-bucket-name
   S3_PUBLIC_URL=https://your-public-url.com
   ```
5. Copy the project ref from your [Trigger.dev dashboard](https://cloud.trigger.dev) and add it to the `trigger.config.ts` file.
6. Run the Trigger.dev CLI `dev` command (it may ask you to authorize the CLI if you haven't already).
7. Test the task in the dashboard by providing a valid image URL and processing options.
8. Deploy the task to production using the Trigger.dev CLI `deploy` command.

## Example Payload

These are all optional parameters that can be passed to the `image-processing.py` Python script from the `processImage.ts` task.

```json theme={"theme":"css-variables"}
{
  "imageUrl": "<your-image-url>",
  "height": 1200,
  "width": 900,
  "quality": 90,
  "maintainAspectRatio": true,
  "outputFormat": "webp",
  "brightness": 1.2,
  "contrast": 1.1,
  "sharpness": 1.3,
  "grayscale": false
}
```

## Deploying your task

Deploy the task to production using the CLI command `npx trigger.dev@latest deploy`

## Learn more about using Python with Trigger.dev

<Card title="Python build extension" icon="code" href="/config/extensions/pythonExtension">
  Learn how to use our built-in Python build extension to install dependencies and run your Python
  code.
</Card>

---

## Python PDF form extractor example

Learn how to use Trigger.dev with Python to extract form data from PDF files.

## Overview

This demo showcases how to use Trigger.dev with Python to extract structured form data from a PDF file available at a URL.

## Prerequisites

* A project with [Trigger.dev initialized](/quick-start)
* [Python](https://www.python.org/) installed on your local machine

## Features

* A [Trigger.dev](https://trigger.dev) task to trigger the Python script
* [Trigger.dev Python build extension](https://trigger.dev/docs/config/extensions/pythonExtension) to install the dependencies and run the Python script
* [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) to extract form data from PDF files
* [Requests](https://docs.python-requests.org/en/master/) to download PDF files from URLs

## GitHub repo

<Card title="View the project on GitHub" icon="GitHub" href="https://github.com/triggerdotdev/examples/edit/main/python-pdf-form-extractor/">
  Click here to view the full code for this project in our examples repository on GitHub. You can
  fork it and use it as a starting point for your own project.
</Card>

## The code

### Build configuration

After you've initialized your project with Trigger.dev, add these build settings to your `trigger.config.ts` file:

```ts trigger.config.ts theme={"theme":"css-variables"}
import { pythonExtension } from "@trigger.dev/python/extension";
import { defineConfig } from "@trigger.dev/sdk";

export default defineConfig({
  runtime: "node",
  project: "<your-project-ref>",
  // Your other config settings...
  build: {
    extensions: [
      pythonExtension({
        // The path to your requirements.txt file
        requirementsFile: "./requirements.txt",
        // The path to your Python binary
        devPythonBinaryPath: `venv/bin/python`,
        // The paths to your Python scripts to run
        scripts: ["src/python/**/*.py"],
      }),
    ],
  },
});
```

<Info>
  Learn more about executing scripts in your Trigger.dev project using our Python build extension
  [here](/config/extensions/pythonExtension).
</Info>

### Task code

This task uses the `python.runScript` method to run the `image-processing.py` script with the given image URL as an argument. You can adjust the image processing parameters in the payload, with options such as height, width, quality, output format, etc.

```ts src/trigger/pythonPdfTask.ts theme={"theme":"css-variables"}
import { task } from "@trigger.dev/sdk";
import { python } from "@trigger.dev/python";

export const processPdfForm = task({
  id: "process-pdf-form",
  run: async (payload: { pdfUrl: string }, io: any) => {
    const { pdfUrl } = payload;
    const args = [pdfUrl];

    const result = await python.runScript("./src/python/extract-pdf-form.py", args);

    // Parse the JSON output from the script
    let formData;
    try {
      formData = JSON.parse(result.stdout);
    } catch (error) {
      throw new Error(`Failed to parse JSON output: ${result.stdout}`);
    }

    return {
      formData,
      stderr: result.stderr,
      exitCode: result.exitCode,
    };
  },
});
```

### Add a requirements.txt file

Add the following to your `requirements.txt` file. This is required in Python projects to install the dependencies.

```txt requirements.txt theme={"theme":"css-variables"}
PyMuPDF==1.23.8
requests==2.31.0
```

### The Python script

The Python script uses PyMuPDF to extract form data from a PDF file. You can see the original script in our examples repository [here](https://github.com/triggerdotdev/examples/blob/main/python-pdf-form-extractor/src/python/extract-pdf-form.py).

```python src/python/extract-pdf-form.py theme={"theme":"css-variables"}
import fitz  # PyMuPDF
import requests
import os
import json
import sys
from urllib.parse import urlparse

def download_pdf(url):
    """Download PDF from URL to a temporary file"""
    response = requests.get(url)
    response.raise_for_status()

    # Get filename from URL or use default
    filename = os.path.basename(urlparse(url).path) or "downloaded.pdf"
    filepath = os.path.join("/tmp", filename)

    with open(filepath, 'wb') as f:
        f.write(response.content)
    return filepath

def extract_form_data(pdf_path):
    """Extract form data from a PDF file."""
    doc = fitz.open(pdf_path)
    form_data = {}

    for page_num, page in enumerate(doc):
        fields = page.widgets()
        for field in fields:
            field_name = field.field_name or f"unnamed_field_{page_num}_{len(form_data)}"
            field_type = field.field_type_string
            field_value = field.field_value

            # For checkboxes, convert to boolean
            if field_type == "CheckBox":
                field_value = field_value == "Yes"

            form_data[field_name] = {
                "type": field_type,
                "value": field_value,
                "page": page_num + 1
            }

    return form_data

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "PDF URL is required as an argument"}), file=sys.stderr)
        return 1

    url = sys.argv[1]

    try:
        pdf_path = download_pdf(url)
        form_data = extract_form_data(pdf_path)

        # Convert to JSON for structured output
        structured_output = json.dumps(form_data, indent=2)
        print(structured_output)
        return 0
    except Exception as e:
        print(json.dumps({"error": str(e)}), file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

## Testing your task

1. Create a virtual environment `python -m venv venv`
2. Activate the virtual environment, depending on your OS: On Mac/Linux: `source venv/bin/activate`, on Windows: `venv\Scripts\activate`
3. Install the Python dependencies `pip install -r requirements.txt`
4. Copy the project ref from your [Trigger.dev dashboard](https://cloud.trigger.dev) and add it to the `trigger.config.ts` file.
5. Run the Trigger.dev CLI `dev` command (it may ask you to authorize the CLI if you haven't already).
6. Test the task in the dashboard by providing a valid PDF URL.
7. Deploy the task to production using the Trigger.dev CLI `deploy` command.

## Learn more about using Python with Trigger.dev

<Card title="Python build extension" icon="code" href="/config/extensions/pythonExtension">
  Learn how to use our built-in Python build extension to install dependencies and run your Python
  code.
</Card>

---
