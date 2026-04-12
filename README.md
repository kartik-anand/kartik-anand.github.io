# Hugo Migration Prototype

This workspace contains a first-pass Hugo rebuild of `www.kartikanand.net`.

## What's included

- A custom Hugo layout for the homepage
- Local copies of the images and PDFs currently used on the live site
- Publication data moved into YAML files for easier maintenance
- A GitHub Pages workflow for later deployment

## Local preview

1. Install Hugo extended.
2. Run:

```bash
hugo server
```

3. Open the local server URL that Hugo prints, usually `http://localhost:1313/`.

## Notes

- The live Wix site currently contains placeholder contact details and Wix-managed forms. This prototype keeps those sections migration-safe instead of reproducing incorrect public contact information.
- Manual content editing instructions are in `CONTENT_MAINTENANCE.md`.
