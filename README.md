# Laredo – St Charles GitHub-only Scraper


This repo runs a headless Selenium scraper in **GitHub Actions** (no local setup) and commits `st-charles-county.json` to the repo root.


## Setup (new repo)
1. Create the folder structure shown above.
2. Add the files from this README to your repo. Commit and push.
3. Add repository **Secrets** under Settings → Secrets and variables → Actions:
- `LAREDO_URL`
- `LAREDO_USERNAME`, `LAREDO_PASSWORD`
- *(optional)* `LAREDO_LOGIN_USER_CSS`, `LAREDO_LOGIN_PASS_CSS`, `LAREDO_LOGIN_SUBMIT_CSS`, `LAREDO_POST_LOGIN_WAIT`, `LAREDO_IFRAME`, `LAREDO_TABLE`


## Run it
- Go to **Actions → Laredo St Charles Scrape → Run workflow**.
- After success, check the repo root for `st-charles-county.json`.


## Troubleshooting
- If the site shows a login page, set the three login CSS secrets and re-run.
- If the table is inside an iframe, set `LAREDO_IFRAME`.
- If the table rows aren’t detected, set `LAREDO_TABLE` (e.g., `table.p-datatable-table tbody tr`).
- The action commits debug artifacts (`laredo_page.html`, `laredo_page.png`, logs) on failure to help you see what the page looked like.


## Customizing
- Change `--days-back` to widen/narrow results.
- Remove `--skip-csv` to also write `st-charles-county.csv`.
- Schedule daily runs by uncommenting the `schedule:` block in the workflow.
