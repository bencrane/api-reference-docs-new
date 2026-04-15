# Filesystem Access
There are multiple options for uploading files to a Sandbox and accessing them
from outside the Sandbox.

## Filesystem API (beta)

Beta This feature is in beta and brings significant reliability improvements compared to the previous Sandbox filesystem API, which was available in releases prior to v1.4.0 and is now deprecated. We’d love to hear your feedback — please reach out via [Slack](https://modal.com/slack) or email us at [support@modal.com](mailto:support@modal.com).

The most convenient way to pass data in and out of the Sandbox during
execution is to use our filesystem API:

It has convenience APIs for streaming file copies in both directions:

These APIs may be used to read files of up to 5GB and write files of any size.

However, if you have a large dataset that you want to use repeatedly from many sandboxes,
consider [using Volumes](#using-volumes).

## Using Volumes

It’s possible to use Modal [Volume](https://modal.com/docs/reference/modal.Volume)s or [CloudBucketMount](https://modal.com/docs/guide/cloud-bucket-mounts)s with Sandboxes.

Volumes and CloudBucketMounts allow you to upload data once and access that
data efficiently from many sandboxes.

To access a Volume from a Sandbox, you can use the `volumes` parameter of `Sandbox.create`:

File syncing behavior differs between Volumes and CloudBucketMounts. For
Volumes, files are only synced back to the Volume when the Sandbox terminates.
For CloudBucketMounts, files are synced automatically.

### Committing Volume changes with sync (v2 only)

For [Volumes v2](https://modal.com/docs/guide/volumes#volumes-v2-overview), you can explicitly
commit changes at any point during Sandbox execution by running the `sync` command on the mountpoint. This persists all data and metadata changes to the
Volume’s storage without waiting for the Sandbox to terminate:

This is particularly useful for long-running Sandboxes where you want to
persist intermediate results, or when you need changes to be visible to other
containers before the Sandbox terminates.

## Adding files to an Image

In some cases, you may want to [add a file to an Image itself](https://modal.com/docs/guide/images#add-local-files-with-add_local_dir-and-add_local_file).
This is useful if the file will be used by many Sandboxes, or if you
want to access that file from the Sandbox’s entrypoint command.

This can be done using the [add_local_file](https://modal.com/docs/reference/modal.Image#add_local_file) and [add_local_dir](https://modal.com/docs/reference/modal.Image#add_local_dir) methods on the [Image](https://modal.com/docs/reference/modal.Image) class:
