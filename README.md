# SSGProject

This is the beginning of a Static Site Generator project.

Initially derived from the boot.dev code assignment, spun off into something a bit more concrete / fit for purpose.

The intended use at this early stage of development is to very easily generate an HTML page from an input Markdown text file without any issues, being then able to be transposed for simple online blogging or professional websites.

Development is intended to be slow, and my end audience is mainly me.
If people find value in using it, then they are welcome to do so for their own purposes.

### What's here

There are presently three scripts.

- `test.sh` — runs the unittest suite.
- `main.sh` — builds for local preview with basepath `/`, then serves `docs/` at http://localhost:8888 until Ctrl+C.
- `build.sh` — builds for GitHub Pages with basepath `/SSGProject/`; no server.

Both `main.sh` and `build.sh` write to `docs/`, so run `./build.sh` last before committing.

### Output

Supports the following Markdown block types:

- Paragraph
- Headings
- Code
- Quote
- Ordered List
- Unordered List

Each Markdown file is written to `docs/` at the same relative path, with `.md` replaced by `.html`. The output tree mirrors `content/`.

Example:

`content/index.md` -> `docs/index.html`
`content/index2electricboogaloo.md` -> `docs/index2electricboogaloo.html`

Both files are generated: `docs/index.html` and `docs/index2electricboogaloo.html`.

A web server serves index.html automatically when a directory is requested, so `index.html` is what visitors see at `/`; `index2electricboogaloo.html` is reachable at `/index2electricboogaloo.html`, not at `/index2electricboogaloo/`.

For a clean URL such as `/electricboogaloo/`, put the page in its own directory:

`content/index.md` -> `docs/index.html`
`content/electricboogaloo/index.md` -> `docs/electricboogaloo/index.html`

The directory's `index.html` becomes its default page, so both pages are built and both are reachable.

### Layout

- `content/` - Markdown sources; each `.md` file is mirrored to the same relative path under `docs/` as `.html`.
- `static/` - CSS and images, copied verbatim into `docs/`
- `template.html` - the HTML shell wrapped around every page.
- `docs/` - generated output, committed for GitHub Pages; do not edit by hand
