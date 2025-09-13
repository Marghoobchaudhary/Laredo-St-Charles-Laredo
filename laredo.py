#!/usr/bin/env python3
password_css=args.login_password_css,
submit_css=args.login_submit_css,
post_login_wait=args.post_login_wait,
)


# Now wait for table
navigate_to_results(driver, iframe_css=args.iframe_css, table_css=args.table_css, wait_secs=args.wait)


flow["steps"].append({"event": "first_pass_begin", "ts": datetime.utcnow().isoformat()})
records = rows_to_records(
driver=driver,
county_slug=args.county_slug,
max_parties=args.max_parties,
wait_secs=args.wait,
days_back=args.days_back,
table_css=args.table_css,
)
flow["steps"].append({"event": "first_pass_records", "count": len(records)})


if rescrape_list:
for idx in rescrape_list:
flow["steps"].append({"event": "rescrape_begin", "index": idx})
more = rows_to_records(
driver=driver,
county_slug=args.county_slug,
max_parties=args.max_parties,
wait_secs=args.wait,
days_back=args.days_back,
table_css=args.table_css,
)
by_doc = {r["Doc Number"]: r for r in records}
for r in more:
by_doc[r["Doc Number"]] = r
records = list(by_doc.values())
flow["steps"].append({"event": "rescrape_records", "index": idx, "count": len(more)})


json_path, csv_path = save_json_csv(records, args.out, args.county_slug, args.skip_csv)
flow["finished_ok"] = True
flow["records"] = len(records)
flow["json_path"] = json_path
flow["csv_path"] = csv_path


except Exception as e:
log(f"FATAL: {e}")
if driver:
_dump_debug_artifacts(driver)
flow["finished_ok"] = False
flow["error"] = repr(e)
raise
finally:
if driver:
try:
driver.quit()
except Exception:
pass
write_flow_log(flow)


if args.hard_timeout and args.hard_timeout > 0:
elapsed = time.time() - start_time
if elapsed > args.hard_timeout:
log("Hard timeout reached; exiting.")
sys.exit(124)




if __name__ == "__main__":
main()
