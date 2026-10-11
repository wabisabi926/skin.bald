# Bald Add-on Repository

This Kodi repository add-on points Kodi 22 at the Bald release feed hosted by
GitHub Pages. Install the `repository.bald-<version>.zip` from the site, then install **Bald** from
**Add-ons → Install from repository → Bald Add-on Repository → Look and feel →
Skin**.

The feed also publishes the separately installable **Bald XC Setup** program
add-on, which configures IPTV Simple from device-local Xtream Codes credentials,
and **Bald Process Info**, a playback info overlay for LibreELEC (a fork of
TinyPPI, which its author doesn't support; on CoreELEC, use TinyPPI from his
repository). It lives in `addons/script.bald.processinfo` as a git subtree of
dangerouslaser/script.bald.processinfo (branch `libreelec`).
`.github/workflows/follow-processinfo.yml` pulls it every morning, after the fork
has followed its upstream. When the fork has moved, it opens a
`processinfo-update` pull request once the feed and tests pass, or an issue
linking the branch if Actions may not open pull requests. If anything fails, it
opens a `processinfo-sync` issue instead.

It also publishes **LG webOS TV Control** (`service.webostv`, controls an LG webOS TV from Kodi) and the
**Estuary LG** skin (`skin.estuary.lg`, Estuary with LG TV integration). Those are developed in
dangerouslaser/kodi-webos-control and dangerouslaser/skin.estuary.lg; their release zips are copied into
`addons/` with `tools/sync_bundled_addons.py` (only runtime files, no git subtree), then released with the skin.

The skin requires **Skin Variables** (`script.skinvariables`), which Kodi's own
repository only carries at 2.1.x. Rather than copying it, the repository add-on
lists jurialmunkey's Kodi 21+ feed as a second `<dir>` (the `omega` feed of his
repository.jurialmunkey), so Kodi installs and updates Skin Variables, its
modules and TMDb Helper from him at his latest release, without his repository
installed. When his repository moves that feed, update the URLs here and bump
the repository add-on's version.

Only tagged, committed revisions are published. The release workflow rejects a
tag whose version does not match `skin.bald/addon.xml`.
