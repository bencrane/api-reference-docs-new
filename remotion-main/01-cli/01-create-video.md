---
title: "create-video"
url: "https://www.remotion.dev/docs/cli/create-video"
path: "/docs/cli/create-video"
---

"---\nimage: /generated/articles-docs-cli-create-video.png\ntitle: npx create-video\nsidebar_label: create-video\ncrumb: CLI Reference\n---\n\nimport {CreateVideoTemplateFlags} from '../../components/CreateVideoTemplateFlags';\n\nScaffold a new Remotion project.\n\n```bash\nnpx create-video <directory>\n```\n\nIf no arguments are passed, an interactive TUI will guide you through the setup.\n\n## Arguments\n\n### `<directory>`\n\nThe directory in which the project should be created.\n\n## Flags\n\n### `--yes`<AvailableFrom v=\"4.0.439\" />\n\nEnable non-interactive mode. All prompts are skipped with sensible defaults.\n\nRequires a template flag and a directory argument.\n\nWhen used:\n- TailwindCSS is installed if the template supports it (disable with `--no-tailwind`)\n- Agent skills are not installed\n- The editor is not opened\n- If already inside a Git repository, the command fails\n\n```bash\nnpx create-video --yes --blank my-video\n```\n\n### `-y`<AvailableFrom v=\"4.0.439\" />\n\nAlias for `--yes`.\n\n### `--no-tailwind`<AvailableFrom v=\"4.0.439\" />\n\nWhen combined with `--yes`, skip installing TailwindCSS. Without `--yes`, this flag has no effect because TailwindCSS is offered interactively.\n\n```bash\nnpx create-video --yes --blank --no-tailwind my-video\n```\n\n### `--tmp`<AvailableFrom v=\"4.0.214\" />\n\nCreate the project in a temporary directory instead of specifying a directory name.\n\n```bash\nnpx create-video --yes --blank --tmp\n```\n\n### Template flags\n\nPass a template name as a flag to skip the template selection prompt.\n\n```bash\nnpx create-video --blank my-video\n```\n\nAvailable templates: <CreateVideoTemplateFlags />.\n\n## Non-interactive mode\n\nBy passing `--yes` (or `-y`), all prompts are skipped and the project is created with sensible defaults. This is useful for scripting and AI agents like Claude Code.\n\nA template flag and a directory argument are required.\n\n```bash\nnpx create-video --yes --blank my-video\n```\n\nWhen using `--yes`:\n\n- TailwindCSS is installed if the template supports it. Pass [`--no-tailwind`](#--no-tailwind) to skip it.\n- [Agent skills](/docs/ai/skills) are not installed. You can add them manually afterwards by running [`npx skills add remotion-dev/skills`](/docs/cli/skills) in the project directory.\n- The editor is not opened after scaffolding.\n- The command fails if you are already inside a Git repository.\n\n### Examples\n\nWithout TailwindCSS:\n\n```bash\nnpx create-video --yes --blank --no-tailwind my-video\n```\n\nIn a temporary directory:\n\n```bash\nnpx create-video --yes --blank --tmp\n```\n"

Scaffold a new Remotion project.

```
npx create-video <directory>Copy
```

If no arguments are passed, an interactive TUI will guide you through the setup.

## Arguments[​](#arguments)

### `<directory>`[​](#directory)

The directory in which the project should be created.

## Flags[​](#flags)

### `--yes`[v4.0.439](https://github.com/remotion-dev/remotion/releases/v4.0.439)[​](#--yes)

Enable non-interactive mode. All prompts are skipped with sensible defaults.

Requires a template flag and a directory argument.

When used:

- TailwindCSS is installed if the template supports it (disable with `--no-tailwind`)

- Agent skills are not installed

- The editor is not opened

- If already inside a Git repository, the command fails

```
npx create-video --yes --blank my-videoCopy
```

### `-y`[v4.0.439](https://github.com/remotion-dev/remotion/releases/v4.0.439)[​](#-y)

Alias for `--yes`.

### `--no-tailwind`[v4.0.439](https://github.com/remotion-dev/remotion/releases/v4.0.439)[​](#--no-tailwind)

When combined with `--yes`, skip installing TailwindCSS. Without `--yes`, this flag has no effect because TailwindCSS is offered interactively.

```
npx create-video --yes --blank --no-tailwind my-videoCopy
```

### `--tmp`[v4.0.214](https://github.com/remotion-dev/remotion/releases/v4.0.214)[​](#--tmp)

Create the project in a temporary directory instead of specifying a directory name.

```
npx create-video --yes --blank --tmpCopy
```

### Template flags[​](#template-flags)

Pass a template name as a flag to skip the template selection prompt.

```
npx create-video --blank my-videoCopy
```

Available templates: `--blank`, `--hello-world`, `--next`, `--vercel`, `--next-no-tailwind`, `--next-pages-dir`, `--recorder`, `--prompt-to-motion-graphics`, `--javascript`, `--render-server`, `--electron`, `--react-router`, `--three`, `--still`, `--audiogram`, `--music-visualization`, `--prompt-to-video`, `--skia`, `--overlay`, `--code-hike`, `--stargazer`, `--tiktok`.

## Non-interactive mode[​](#non-interactive-mode)

By passing `--yes` (or `-y`), all prompts are skipped and the project is created with sensible defaults. This is useful for scripting and AI agents like Claude Code.

A template flag and a directory argument are required.

```
npx create-video --yes --blank my-videoCopy
```

When using `--yes`:

- TailwindCSS is installed if the template supports it. Pass [`--no-tailwind`](#--no-tailwind) to skip it.

- [Agent skills](/docs/ai/skills) are not installed. You can add them manually afterwards by running [`npx skills add remotion-dev/skills`](/docs/cli/skills) in the project directory.

- The editor is not opened after scaffolding.

- The command fails if you are already inside a Git repository.

### Examples[​](#examples)

Without TailwindCSS:

```
npx create-video --yes --blank --no-tailwind my-videoCopy
```

In a temporary directory:

```
npx create-video --yes --blank --tmpCopy
```
](#examples)](#examples)
](#examples)
- ](#examples)
- ](#examples)
- ](#examples)
- ](#examples)
- ](#examples)
- ](#examples)
- ](#examples)
- ](#examples)
- ](#examples)