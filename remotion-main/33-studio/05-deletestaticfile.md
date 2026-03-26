---
title: "deleteStaticFile()"
url: "https://www.remotion.dev/docs/studio/delete-static-file"
path: "/docs/studio/delete-static-file"
---

"---\nimage: /generated/articles-docs-studio-delete-static-file.png\ntitle: deleteStaticFile()\ncrumb: \"@remotion/studio\"\n---\n\n# deleteStaticFile()<AvailableFrom v=\"4.0.154\"/>\n\nDeletes a file from the [`public` directory](/docs/terminology/public-dir).  \nThis API is useful for building interactive experiences in the [Remotion Studio](/docs/terminology/studio).\n\n## Examples\n\n```tsx twoslash title=\"Delete 'video.webm'\"\nimport React, { useCallback } from \"react\";\nimport { deleteStaticFile } from \"@remotion/studio\";\n\nexport const DeleteStaticFileComp: React.FC = () => {\n  const deleteFile = useCallback(async () => {\n    const { existed } = await deleteStaticFile(\"video.webm\");\n\n    console.log(`Deleted file (${existed ? \"existed\" : \"did not exist\"})`);\n  }, []);\n\n  return <button onClick={deleteFile}>Delete</button>;\n};\n```\n\n## Rules\n\n<Step>1</Step> This API can only be used while in the Remotion Studio.\n<br />\n<Step>2</Step> The file path must be relative to the <a href=\"/docs/terminology/public-dir\">\n  <code>public</code> directory\n</a>.\n<br />\n<Step>3</Step> It's not allowed to delete a file outside the <a href=\"/docs/terminology/public-dir\">\n  <code>public</code> directory\n</a>.<br />\n<Step>4</Step> To delete a file in a subfolder, use forward slashes <code>\n  /\n</code> even on Windows.\n<Step>5</Step> You can, but don't have to wrap the file path in a <a href=\"/docs/staticfile\">\n  <code>staticFile()</code>\n</a> function.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/delete-static-file.ts)\n- [`writeStaticFile()`](/docs/studio/write-static-file)\n- [`getStaticFiles()`](/docs/studio/get-static-files)\n- [`watchStaticFile()`](/docs/studio/watch-static-file)\n"

Deletes a file from the [`public` directory](/docs/terminology/public-dir).

This API is useful for building interactive experiences in the [Remotion Studio](/docs/terminology/studio).

## Examples[​](#examples)

```

Delete 'video.webm'import React, { useCallback } from "react";
import { deleteStaticFile } from "@remotion/studio";

export const DeleteStaticFileComp: React.FC = () => {
  const deleteFile = useCallback(async () => {
    const { existed } = await deleteStaticFile("video.webm");

    console.log(`Deleted file (${existed ? "existed" : "did not exist"})`);
  }, []);

  return <button onClick={deleteFile}>Delete</button>;
};Copy
```

## Rules[​](#rules)

[](#1)
[1](#1)[ ](#1) This API can only be used while in the Remotion Studio.

[](#2)
[2](#2)[ ](#2) The file path must be relative to the [
`public` directory
](/docs/terminology/public-dir).

[](#3)
[3](#3)[ ](#3) It's not allowed to delete a file outside the [
`public` directory
](/docs/terminology/public-dir).

[
4 ](#4) To delete a file in a subfolder, use forward slashes `
/
` even on Windows.
[
5 ](#5) You can, but don't have to wrap the file path in a [
`staticFile()`
](/docs/staticfile) function.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/delete-static-file.ts)

- [`writeStaticFile()`](/docs/studio/write-static-file)

- [`getStaticFiles()`](/docs/studio/get-static-files)

- [`watchStaticFile()`](/docs/studio/watch-static-file)
](/docs/studio/watch-static-file)](/docs/studio/watch-static-file)
](/docs/studio/watch-static-file)
- ](/docs/studio/watch-static-file)
- ](/docs/studio/watch-static-file)