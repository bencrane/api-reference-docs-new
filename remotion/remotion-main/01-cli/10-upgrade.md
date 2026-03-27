---
title: "upgrade"
url: "https://www.remotion.dev/docs/cli/upgrade"
path: "/docs/cli/upgrade"
---

"---\nimage: /generated/articles-docs-cli-upgrade.png\ntitle: npx remotion upgrade\nsidebar_label: upgrade\ncrumb: CLI Reference\n---\n\nUpgrades all Remotion-related packages.\n\nIf `mediabunny` is installed, it will also be upgraded to the version [compatible with the new Remotion version](/docs/mediabunny/version).\n\n```\nnpx remotion upgrade\n```\n\n## Flags\n\n### `--package-manager`<AvailableFrom v=\"3.2.33\"/>\n\n<Options id=\"package-manager\" />\n\n### `--version`<AvailableFrom v=\"4.0.15\"/>\n\n<Options id=\"version\" />\n\n## Package manager support\n\n`npm`, `yarn` and `pnpm` are all supported.\n\n## Additional arguments\n\nAny additional arguments you pass to this command will be forwarded as flags to the package manager, before the list of packages.  \nBefore v4.0.246, additional arguments were ignored.\n\n## Difference to `npm update`, `yarn upgrade`, `pnpm up`\n\nThese commands, when executed without arguments will upgrade all dependencies in your project. We recommend against it because you may unintentionally break other parts of your project when you only wanted to upgrade Remotion.\n"

Upgrades all Remotion-related packages.

If `mediabunny` is installed, it will also be upgraded to the version [compatible with the new Remotion version](/docs/mediabunny/version).

```
npx remotion upgradeCopy
```

## Flags[​](#flags)

### `--package-manager`[v3.2.33](https://github.com/remotion-dev/remotion/releases/v3.2.33)[​](#--package-manager)

Forces a specific package manager to be used. By default, Remotion will auto-detect the package manager based on your lockfile.
Acceptable values are `npm`, `yarn`, `pnpm` and `bun`.

### `--version`[v4.0.15](https://github.com/remotion-dev/remotion/releases/v4.0.15)[​](#--version)

Install a specific version. Also enables downgrading to an older version.

## Package manager support[​](#package-manager-support)

`npm`, `yarn` and `pnpm` are all supported.

## Additional arguments[​](#additional-arguments)

Any additional arguments you pass to this command will be forwarded as flags to the package manager, before the list of packages.

Before v4.0.246, additional arguments were ignored.

## Difference to `npm update`, `yarn upgrade`, `pnpm up`[​](#difference-to-npm-update-yarn-upgrade-pnpm-up)

These commands, when executed without arguments will upgrade all dependencies in your project. We recommend against it because you may unintentionally break other parts of your project when you only wanted to upgrade Remotion.](#difference-to-npm-update-yarn-upgrade-pnpm-up)](#difference-to-npm-update-yarn-upgrade-pnpm-up)
](#difference-to-npm-update-yarn-upgrade-pnpm-up)
- ](#difference-to-npm-update-yarn-upgrade-pnpm-up)
- ](#difference-to-npm-update-yarn-upgrade-pnpm-up)
- ](#difference-to-npm-update-yarn-upgrade-pnpm-up)
- ](#difference-to-npm-update-yarn-upgrade-pnpm-up)
- ](#difference-to-npm-update-yarn-upgrade-pnpm-up)