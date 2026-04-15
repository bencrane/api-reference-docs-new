# Fast pull from registry
The performance of pulling public and private images from registries into Modal
can be significantly improved by adopting the [eStargz](https://github.com/containerd/stargz-snapshotter/blob/main/docs/estargz.md) compression format. By applying eStargz compression during your image build and push, Modal will be much
more efficient at pulling down your image from the registry. 
## How to use estargz
If you have [Buildkit](https://docs.docker.com/build/buildkit/) version greater than `0.10.0`, adopting `estargz` is as simple as
adding some flags to your `docker buildx build` command: `type=registry` flag will instruct BuildKit to push the image after building. If you do not push the image from immediately after build and instead attempt to push it later with docker push, the image will be converted to a standard gzip image.
- `compression=estargz` specifies that we are using the [eStargz](https://github.com/containerd/stargz-snapshotter/blob/main/docs/estargz.md) compression format.
- `oci-mediatypes=true` specifies that we are using the OCI media types, which is required for eStargz.
- `force-compression=true` will recompress the entire image and convert the base image to eStargz if it is not already.

Then reference the container image as normal in your Modal code.

At build time you should see the eStargz-enabled puller activate:

## Supported registries

Currently, Modal supports fast estargz pulling images with the following registries:
- AWS Elastic Container Registry (ECR)
- Docker Hub (docker.io)
- Google Artifact Registry (gcr.io, pkg.dev)

We are working on adding support for GitHub Container Registry (ghcr.io).
