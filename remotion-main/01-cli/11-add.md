---
title: "add"
url: "https://www.remotion.dev/docs/cli/add"
path: "/docs/cli/add"
---

"---\nimage: /generated/articles-docs-cli-add.png\ntitle: npx remotion add\nsidebar_label: add\ncrumb: CLI Reference\n---\n\nAdds one or more Remotion packages to your project with the same version as your other Remotion packages.\n\nAlso supports adding `zod` and `mediabunny` with the correct version for your Remotion installation.\n\n```\nnpx remotion add <package-name...>\n```\n\n## Examples\n\nAdd a single package:\n\n```bash\nnpx remotion add @remotion/transitions\n```\n\nAdd multiple packages at once:\n\n```bash\nnpx remotion add @remotion/transitions @remotion/three @remotion/lottie\n```\n\nThis command will:\n\n1. Verify that all package names are valid Remotion packages (or supported extra packages: `zod`, `mediabunny`)\n2. Check which packages are already installed (and skip them)\n3. Detect the version of your currently installed Remotion packages\n4. Install the specified packages with the matching version\n\n## Flags\n\n### `--package-manager`<AvailableFrom v=\"4.0.367\"/>\n\n<Options id=\"package-manager\" />\n\n## Package manager support\n\n`npm`, `yarn` and `pnpm` are all supported.\n\n## Additional arguments\n\nAny additional arguments you pass to this command will be forwarded as flags to the package manager, before the package name.\n\n## Use case\n\nThis command is useful when you want to add new Remotion packages to your project and ensure they're installed with the same version as your other Remotion packages. This helps avoid version mismatches that could cause compatibility issues.\n\nFor example, if you have `remotion@4.0.100` installed and you want to add `@remotion/transitions`, running `npx remotion add @remotion/transitions` will install `@remotion/transitions@4.0.100`.\n\nWhen adding multiple packages, the command will install all of them in a single operation with the same version number.\n\n## See also\n\n- [Source code of this command](https://github.com/remotion-dev/remotion/blob/main/packages/cli/src/add.ts)\n- [npx remotion upgrade](/docs/cli/upgrade)\n- [npx remotion versions](/docs/cli/versions)\n"

Adds one or more Remotion packages to your project with the same version as your other Remotion packages.

Also supports adding `zod` and `mediabunny` with the correct version for your Remotion installation.

```
npx remotion add <package-name...>Copy
```

## Examples[​](#examples)

Add a single package:

```
npx remotion add @remotion/transitionsCopy
```

Add multiple packages at once:

```
npx remotion add @remotion/transitions @remotion/three @remotion/lottieCopy
```

This command will:

- Verify that all package names are valid Remotion packages (or supported extra packages: `zod`, `mediabunny`)

- Check which packages are already installed (and skip them)

- Detect the version of your currently installed Remotion packages

- Install the specified packages with the matching version

## Flags[​](#flags)

### `--package-manager`[v4.0.367](https://github.com/remotion-dev/remotion/releases/v4.0.367)[​](#--package-manager)

Forces a specific package manager to be used. By default, Remotion will auto-detect the package manager based on your lockfile.
Acceptable values are `npm`, `yarn`, `pnpm` and `bun`.

## Package manager support[​](#package-manager-support)

`npm`, `yarn` and `pnpm` are all supported.

## Additional arguments[​](#additional-arguments)

Any additional arguments you pass to this command will be forwarded as flags to the package manager, before the package name.

## Use case[​](#use-case)

This command is useful when you want to add new Remotion packages to your project and ensure they're installed with the same version as your other Remotion packages. This helps avoid version mismatches that could cause compatibility issues.

For example, if you have `[[email protected]](/cdn-cgi/l/email-protection)` installed and you want to add `@remotion/transitions`, running `npx remotion add @remotion/transitions` will install `@remotion/[[email protected]](/cdn-cgi/l/email-protection)`.

When adding multiple packages, the command will install all of them in a single operation with the same version number.

## See also[​](#see-also)

- [Source code of this command](https://github.com/remotion-dev/remotion/blob/main/packages/cli/src/add.ts)

- [npx remotion upgrade](/docs/cli/upgrade)

- [npx remotion versions](/docs/cli/versions)
](/docs/cli/versions)](/docs/cli/versions)
](/docs/cli/versions)
- ](/docs/cli/versions)
- ](/docs/cli/versions)
- ](/docs/cli/versions)
- ](/docs/cli/versions)
- ](/docs/cli/versions)
- ](/docs/cli/versions)