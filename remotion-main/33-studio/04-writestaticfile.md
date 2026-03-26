---
title: "writeStaticFile()"
url: "https://www.remotion.dev/docs/studio/write-static-file"
path: "/docs/studio/write-static-file"
---

"---\nimage: /generated/articles-docs-studio-write-static-file.png\ntitle: writeStaticFile()\ncrumb: \"@remotion/studio\"\n---\n\n# writeStaticFile()<AvailableFrom v=\"4.0.147\"/>\n\nSaves some content into a file in the [`public` directory](/docs/).  \nThis API is useful for building interactive experiences in the [Remotion Studio](/docs/terminology/studio).\n\n## Examples\n\n```tsx twoslash title=\"Write 'Hello world' to public/file.txt\"\nimport React, { useCallback } from \"react\";\nimport { writeStaticFile } from \"@remotion/studio\";\n\nexport const WriteStaticFileComp: React.FC = () => {\n  const saveFile = useCallback(async () => {\n    await writeStaticFile({\n      filePath: \"file.txt\",\n      contents: \"Hello world\",\n    });\n\n    console.log(\"Saved!\");\n  }, []);\n\n  return <button onClick={saveFile}>Save</button>;\n};\n```\n\n```tsx twoslash title=\"Allow a file upload\"\nimport React, { useCallback } from \"react\";\nimport { writeStaticFile } from \"@remotion/studio\";\n\nexport const WriteStaticFileComp: React.FC = () => {\n  const saveFile = useCallback(\n    async (e: React.ChangeEvent<HTMLInputElement>) => {\n      const file = e.target.files![0];\n\n      await writeStaticFile({\n        filePath: file.name,\n        contents: await file.arrayBuffer(),\n      });\n\n      console.log(\"Saved!\");\n    },\n    [],\n  );\n\n  return <input type=\"file\" onChange={saveFile} />;\n};\n```\n\n## Rules\n\n<Step>1</Step> This API can only be used while in the Remotion Studio.\n<br />\n<Step>2</Step> The file path must be relative to the <a href=\"/docs/terminology/public-dir\">\n  <code>public</code> directory\n</a>.\n<br />\n<Step>3</Step> It's not allowed to write outside the <a href=\"/docs/terminology/public-dir\">\n  <code>public</code> directory\n</a>.<br />\n<Step>4</Step> To write into subfolders, use forward slashes <code>/</code> even\non Windows.\n<Step>5</Step> You can pass a <code>string</code> or <code>ArrayBuffer</code>.\n\n## See also\n\n- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/write-static-file.ts)\n- [`staticFile()`](/docs/staticfile)\n- [`getStaticFiles()`](/docs/studio/get-static-files)\n- [`watchStaticFile()`](/docs/studio/watch-static-file)\n"

Saves some content into a file in the [`public` directory](/docs/).

This API is useful for building interactive experiences in the [Remotion Studio](/docs/terminology/studio).

## Examples[​](#examples)

```

Write 'Hello world' to public/file.txtimport React, { useCallback } from "react";
import { writeStaticFile } from "@remotion/studio";

export const WriteStaticFileComp: React.FC = () => {
  const saveFile = useCallback(async () => {
    await writeStaticFile({
      filePath: "file.txt",
      contents: "Hello world",
    });

    console.log("Saved!");
  }, []);

  return <button onClick={saveFile}>Save</button>;
};Copy
```

```

Allow a file uploadimport React, { useCallback } from "react";
import { writeStaticFile } from "@remotion/studio";

export const WriteStaticFileComp: React.FC = () => {
  const saveFile = useCallback(
    async (e: React.ChangeEvent<HTMLInputElement>) => {
      const file = e.target.files![0];

      await writeStaticFile({
        filePath: file.name,
        contents: await file.arrayBuffer(),
      });

      console.log("Saved!");
    },
    [],
  );

  return <input type="file" onChange={saveFile} />;
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
[3](#3)[ ](#3) It's not allowed to write outside the [
`public` directory
](/docs/terminology/public-dir).

[
4 ](#4) To write into subfolders, use forward slashes `/` even
on Windows.
[
5 ](#5) You can pass a `string` or `ArrayBuffer`.

## See also[​](#see-also)

- [Source code for this function](https://github.com/remotion-dev/remotion/blob/main/packages/studio/src/api/write-static-file.ts)

- [`staticFile()`](/docs/staticfile)

- [`getStaticFiles()`](/docs/studio/get-static-files)

- [`watchStaticFile()`](/docs/studio/watch-static-file)
](/docs/studio/watch-static-file)](/docs/studio/watch-static-file)
](/docs/studio/watch-static-file)
- ](/docs/studio/watch-static-file)
- ](/docs/studio/watch-static-file)