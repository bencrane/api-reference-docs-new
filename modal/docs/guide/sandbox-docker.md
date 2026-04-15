# Docker in Sandboxes (Alpha)
Alpha This feature is currently in alpha. See [feature maturity](https://modal.com/docs/guide/feature-maturity) for more details. Compatibility with [Sandbox snapshots](https://modal.com/docs/guide/sandbox-snapshots) is known to be limited; in particular, Docker state is currently not captured when taking a [filesystem snapshot](https://modal.com/docs/guide/sandbox-snapshots#filesystem-snapshots).

Modal has Alpha support for running `docker` containers inside `modal.Sandbox`.
This is intended to support coding agents who want to interact with development environments that include
container images.

This functionality is enabled by creating Sandboxes with `experimental_options={"enable_docker": True}`.

## Demo

Run the following program with the [Image Builder version](https://modal.com/docs/guide/images#image-builder-updates) set to version `2025.06` or later.

`MODAL_IMAGE_BUILDER_VERSION=2025.06 python3 demo.py`

The output will be like this:
