# Embed Files and Prototypes

Guide for embedding Figma content in your applications.

Source: https://help.figma.com/hc/en-us/articles/360039827134-Embed-files-and-prototypes

## Supported Content Types

- Figma Design files
- FigJam files
- Figma Slides
- Prototypes

## Embedding Files/FigJam

1. Select a top-level frame (optional)
2. Click **Share** in the right sidebar
3. Configure audience and permission settings
4. Click **Get embed code**
5. Copy and paste into your application

## Embedding Prototypes

1. Open presentation view
2. Select a flow from the left sidebar
3. Click **Share prototype**
4. Set audience and permission settings
5. Click **Get embed code**

## Access Control

### Audience Levels
- **Organization-only** - Only org members can view
- **Public** - Anyone with the link can view

### Permission Levels
- **Can view** - Read-only access
- **Can edit** - Full editing access

### Restrictions
- Password-protected files cannot be embedded
- Organization files require user authentication

## Customization Options

Embeds support various customization through URL parameters:

- Control pan and zoom functionality
- Page selection capabilities
- Design or Dev Mode specification
- Full-screen expansion permissions
- Theme application (dark, light, or system)

## Limitations

- Embeds only work in **browser-based applications**
- Cannot add embeds within native/desktop applications
- Password-protected content cannot be embedded

## Developer Integration

For programmatic embedding, use:
- **Embed Kit 2.0** - Full embedding framework
- **Embed API** - Message passing and event handling

See [embed-api.md](./embed-api.md) for API details.
