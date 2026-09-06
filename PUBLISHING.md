# Publishing MSCH Synkit FX

GitHub source and ComfyUI Manager discovery are separate steps. The [Comfy Registry publishing guide](https://docs.comfy.org/registry/publishing) describes the service that powers Manager.

1. Sign in at https://registry.comfy.org and create or select your publisher.
2. The confirmed publisher ID `mariobilly` is configured in `pyproject.toml`. Use a publishing API key belonging to this publisher.
3. Create a Registry publishing API key. In this GitHub repository, add it as the Actions secret `REGISTRY_ACCESS_TOKEN`. Do not commit it or paste it into a workflow.
4. Push the metadata change, then run **Publish to Comfy Registry** from the Actions tab. The action also runs when a GitHub release is published.
5. Check the completed action and the node's registry listing before announcing Manager availability. Registry acceptance and indexing are external steps.

For later versions, update the semantic version in `pyproject.toml`, commit it, create the corresponding GitHub release and verify the publication result. Published versions must be unique.

The registry archive excludes large previews and development files via `.comfyignore`; GitHub retains them for browsing. Workflows are kept with the package. GitHub CI checks Python syntax, JSON and package metadata without downloading models or claiming GPU execution coverage.

## Manager node-list registration

The [Manager repository also accepts node-list registration pull requests](https://github.com/Comfy-Org/ComfyUI-Manager#how-to-register-your-custom-node-into-comfyui-manager). This is separate from publishing versioned Registry archives and still requires maintainer acceptance. The collection index tracks the registration request.

## Current release

Version `0.1.0` was uploaded successfully on 2026-09-06 through [GitHub Actions](https://github.com/mariobilly/msch-synkitfx/actions/runs/34037796890). The publisher is `mariobilly`, the repository publishing secret is configured, and the uploaded ZIP was downloaded and checked. Registry reported `NodeVersionStatusPending` at verification. Further releases require a new version number; do not republish `0.1.0`.
