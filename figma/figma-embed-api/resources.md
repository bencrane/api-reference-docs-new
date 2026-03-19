# Embed Resources

URL formats, file types, and utilities for embedding Figma content.

Source: https://developers.figma.com/docs/embeds/resources/

## URL Validation

Regex pattern to identify valid Figma URLs:

```javascript
const URL_REGEX = /https:\/\/[\w\.-]+\.?figma.com\/([\w-]+)\/([0-9a-zA-Z]{22,128})(?:\/.*)?$/
```

## Supported File Types & URL Formats

| File Type | URL Pattern |
|-----------|-------------|
| FigJam boards | `https://www.figma.com/board/:file_key/:file_name` |
| Figma Slides | `https://www.figma.com/slides/:file_key/:file_name` |
| Slides presentation | `https://www.figma.com/deck/:file_key/:file_name` |
| Design files | `https://www.figma.com/design/:file_key/:file_name` |
| Dev Mode | `https://www.figma.com/design/:file_key/:file_name?m=dev` |

## Embed URL Conversion

To create embeds, convert the subdomain from `www.figma.com` or `figma.com` to `embed.figma.com`, then apply appropriate query parameters.

### Example

Original URL:
```
https://www.figma.com/design/abc123xyz/MyDesign
```

Embed URL:
```
https://embed.figma.com/design/abc123xyz/MyDesign?embed-host=example.com
```

## Query Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `embed-host` | Yes | Your domain name |
| `client-id` | For Embed API | OAuth app client ID |
| `node-id` | No | Specific node to display |
| `m` | No | Mode (`dev` for Dev Mode) |

## Finding Node IDs

Three methods to locate node identifiers:

### 1. Embed API Events
Extract from event data:
- `MOUSE_PRESS_OR_RELEASE`
- `PRESENTED_NODE_CHANGED`
- `NEW_STATE`

### 2. Figma URLs
Node IDs appear in the `node-id` query parameter when selecting layers in Figma:
```
https://www.figma.com/design/abc123/File?node-id=123:456
```

### 3. Developer Console
Use in Figma's console or browser dev tools:
```javascript
figma.currentPage.selection[0].id
```

## Migration from Embed Kit 1.0

JavaScript migration function:

```javascript
function migrateEmbedUrl(oldUrl) {
  const url = new URL(oldUrl);

  // Convert subdomain
  url.hostname = url.hostname.replace('www.figma.com', 'embed.figma.com');

  // Convert underscore params to hyphens
  const params = new URLSearchParams(url.search);
  const newParams = new URLSearchParams();

  for (const [key, value] of params) {
    // Remove deprecated embed_origin
    if (key === 'embed_origin') continue;

    // Convert underscores to hyphens
    const newKey = key.replace(/_/g, '-');
    newParams.set(newKey, value);
  }

  url.search = newParams.toString();
  return url.toString();
}
```

### Key Changes in Embed Kit 2.0

- `embed_origin` parameter removed
- `embed-host` is now required
- Parameter names use hyphens instead of underscores
- Subdomain changed from `www` to `embed`
