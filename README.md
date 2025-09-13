# Laredo – St Charles GitHub-only Scraper

Runs a headless Selenium scraper in **GitHub Actions** (no local setup) and commits `st-charles-county.json` to the repo root.

## Setup
1. Add **Repository Secrets** (Settings → Secrets and variables → Actions → New repository secret):
   - `LAREDO_URL` – direct URL to the PrimeNG results table for St Charles.
   - `LAREDO_USERNAME` / `LAREDO_PASSWORD` – if the site requires login (optional; login stub present).
   - Optional: `LAREDO_IFRAME` and/or `LAREDO_TABLE` if selectors are needed to reach the table.
2. Commit these files to your repo:
   - `laredo.py`
   - `.github/workflows/laredo.yml`
   - `requirements.txt`
   - `README.md`
3. Trigger the workflow via **Actions → “Laredo St Charles Scrape” → Run workflow**.

## Output
- `st-charles-county.json` committed to the repo root on success.
- Debug artifacts (on failure or when saved): `laredo_page.html`, `laredo_page.png`, `laredo.logs`, `laredo-flow-logs.json`.

## Tips
- If the table isn’t detected, set `LAREDO_IFRAME` and/or `LAREDO_TABLE` secrets and re-run, or increase `--wait` in the workflow step.
- To include CSV, remove `--skip-csv`; a `st-charles-county.csv` will also be written.
- Change the output file name by adjusting `--county-slug`.
