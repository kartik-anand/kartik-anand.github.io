# Content Maintenance Guide

This site is a Hugo project. Most routine content updates happen in two files:

- `data/site.yaml` for homepage/profile content
- `data/publications.yaml` for working papers, work in progress, and publications

Local assets live here:

- `static/papers/` for PDFs
- `static/images/journey/` for journey logos
- `static/images/` for profile and other site images

## Before you start

1. Open the project folder.
2. Make your edits in the YAML files below.
3. Preview locally with:

```bash
hugo server
```

4. Open the local URL Hugo prints, usually `http://localhost:1313/`.

## YAML rules to keep in mind

- Keep indentation exactly as-is, using 2 spaces.
- Each list item starts with `-`.
- If a title contains a colon, wrap it in quotes.
- Multi-line summaries use `summary: >-` followed by indented lines.

## Add, update, or delete working papers

Edit `data/publications.yaml` under `working_papers:`.

Each working-paper entry can contain:

- `title` required
- `subtitle` optional
- `authors` optional
- `summary` optional
- `links` optional

Example:

```yaml
working_papers:
  - title: My New Working Paper
    subtitle: Optional subtitle
    authors: with Coauthor Name
    summary: >-
      One or more lines describing the paper.
    links:
      - label: Download PDF
        url: /papers/my-new-working-paper.pdf
```

To add a working paper:

1. If you have a local PDF, place it in `static/papers/`.
2. Add a new `- title: ...` block under `working_papers:`.
3. Use a URL like `/papers/filename.pdf` for local PDFs.

To update a working paper:

- Edit the fields directly in its existing block.

To delete a working paper:

- Remove the entire `- title: ...` block for that paper.

## Add, update, or delete work in progress items

Edit `data/publications.yaml` under `work_in_progress:`.

Each work-in-progress entry uses the same structure as a working paper:

- `title` required
- `subtitle` optional
- `authors` optional
- `summary` optional
- `links` optional

Example:

```yaml
work_in_progress:
  - title: A New Project
    authors: with Coauthor Name
    summary: >-
      Short description of the project.
    links:
      - label: Draft
        url: https://example.com/draft
```

Notes:

- The homepage only shows the `Work in Progress` section when this list contains at least one item.
- If you leave `work_in_progress:` empty, the section stays hidden.

## Add, update, or delete publications

Edit `data/publications.yaml` under `publications:`.

Each publication entry can contain:

- `title` required
- `subtitle` optional
- `venue` usually included for published work
- `authors` optional
- `summary` optional
- `links` optional

Example:

```yaml
publications:
  - title: "My Published Paper: With Subtitle"
    venue: Journal Name, 2026
    authors: with Coauthor Name
    summary: >-
      Short abstract-style description.
    links:
      - label: WP
        url: https://example.com/working-paper
      - label: Published
        url: https://example.com/published-paper
```

Link behavior on the site:

- If one link label contains `Published`, that link becomes the main clickable title.
- Otherwise, the first link is used as the main clickable title.
- Any additional links appear beside the title in brackets.

To delete a publication:

- Remove the entire entry block from `publications:`.

## Add, update, or delete journey entries

Edit `data/site.yaml` under `journey:`.

Each journey item contains:

- `mark` short label used for internal reference
- `name` institution or employer name
- `logo` image path
- `url` destination when clicked

Example:

```yaml
journey:
  - mark: XYZ
    name: Example Institute
    logo: /images/journey/example.png
    url: https://www.example.org/
```

To add a journey entry:

1. Put the logo file in `static/images/journey/`.
2. Add the new block at the right position in the `journey:` list.

Important:

- The order in `journey:` is the order shown on the homepage.
- Keep logos reasonably compact and use PNG or SVG when possible.

To delete a journey entry:

- Remove its full block from the list.

## Add, update, or delete research interests

Edit `data/site.yaml` under `research_interests:`.

Example:

```yaml
research_interests:
  - Artificial Intelligence
  - Financial stability
  - Political economy
```

To add one:

- Add a new `- ...` line to the list.

To update one:

- Edit the existing line.

To delete one:

- Remove the line.

## Add, update, or delete top links

Edit `data/site.yaml` under `links:`.

Example:

```yaml
links:
  - label: CV
    url: /papers/cv.pdf
  - label: Google Scholar
    url: https://scholar.google.com/
```

To add a new local file link:

1. Put the file in `static/papers/` if it is a PDF or download.
2. Reference it with a site-relative path such as `/papers/cv.pdf`.

To delete a top link:

- Remove the full `label` / `url` block.

## Quick profile text updates

These live in `data/site.yaml`:

- `name`
- `hero_title`
- `hero_subtitle`
- `footer.note`

## Profile image

The homepage profile image is currently hardcoded in `layouts/index.html` and points to:

```text
/images/profile-2026-soft.png
```

To swap it:

1. Add or replace the image in `static/images/`.
2. Update the image path in `layouts/index.html` if the filename changes.

## Fields currently stored but not rendered

These fields exist in `data/site.yaml`, but the current templates do not display them on the live homepage layout:

- `intro`
- `contact`
- `newsletter`

You can still update them now if you want to keep the data ready for a later template change.
