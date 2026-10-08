# chebanov-novokuznetsk-2026
CHEBANOV · Новокузнецк · Концерт-свидание 2026

## Removable postponement overlay

`site-state.json` is the single status flag. Set `postponed` to `false`, run
`python3 scripts/build-site.py`, then publish `index.html` to restore the original
landing and its original OG/Twitter metadata together. Setting it back to `true`
and rebuilding re-enables the notice and its versioned social image.

While enabled, the full previous body remains inside `#preserved-site` with
`hidden`, `inert` and `aria-hidden`; its scripts are non-executable. The fullscreen
notice locks page scrolling and prevents access to old ticket controls. The
original source remains byte-for-byte in the archive; the build never rewrites it.
