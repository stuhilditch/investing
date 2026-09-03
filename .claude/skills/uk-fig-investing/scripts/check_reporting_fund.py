#!/usr/bin/env python3
"""Check whether a fund share class has HMRC reporting-fund status.

Downloads HMRC's published "List of reporting funds A to Z" (an ODS
spreadsheet linked from the gov.uk publication page), searches it by ISIN,
and prints the matching rows with the list's publication date.

Usage:
    python3 check_reporting_fund.py IE00B5BMR087 [IE00BFMXXD54 ...]
    python3 check_reporting_fund.py --list-url <ods url> IE00B5BMR087

Standard library only. Network access to www.gov.uk and
assets.publishing.service.gov.uk only. Exit code 0 if every ISIN is found,
1 if any is missing, 2 on a fetch or parse error.
"""
import argparse
import re
import sys
import urllib.request
import zipfile
import io
import html
from datetime import date

PUB_PAGE = "https://www.gov.uk/government/publications/offshore-funds-list-of-reporting-funds"
UA = {"User-Agent": "uk-fig-investing/1.0 (reporting fund status check)"}
ROW_RE = re.compile(r"<table:table-row\b.*?</table:table-row>", re.S)
CELL_RE = re.compile(r"<table:(?:covered-)?table-cell\b([^>]*?)(?:/>|>(.*?)</table:(?:covered-)?table-cell>)", re.S)
TEXT_RE = re.compile(r"<text:p\b[^>]*>(.*?)</text:p>", re.S)
TAG_RE = re.compile(r"<[^>]+>")


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read()


def find_list_url() -> str:
    html = fetch(PUB_PAGE).decode("utf-8", "replace")
    m = re.search(r'https://assets\.publishing\.service\.gov\.uk/media/[^"\s]+\.ods', html)
    if not m:
        raise RuntimeError("could not find an .ods link on the HMRC publication page")
    return m.group(0)


def rows_from_ods(blob: bytes):
    """Yield rows as lists of cell strings. Regex-based so it needs no XML
    parser (some Python builds ship without expat)."""
    with zipfile.ZipFile(io.BytesIO(blob)) as z:
        content = z.read("content.xml").decode("utf-8", "replace")
    for row in ROW_RE.findall(content):
        cells = []
        for attrs, inner in CELL_RE.findall(row):
            m = re.search(r'number-columns-repeated="(\d+)"', attrs)
            rep = int(m.group(1)) if m else 1
            text = " ".join(html.unescape(TAG_RE.sub("", t)).strip() for t in TEXT_RE.findall(inner or ""))
            cells.extend([text.strip()] * min(rep, 20))
        if any(cells):
            yield cells


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("isins", nargs="+", help="ISIN codes to look up")
    ap.add_argument("--list-url", help="override the ODS URL (skip discovery)")
    args = ap.parse_args()

    try:
        url = args.list_url or find_list_url()
        print(f"HMRC list: {url}")
        m = re.search(r"/(\d{8})_", url)
        if m:
            print(f"List file date (from filename): {m.group(1)[:4]}-{m.group(1)[4:6]}-{m.group(1)[6:]}")
        blob = fetch(url)
        rows = list(rows_from_ods(blob))
    except Exception as e:  # noqa: BLE001
        print(f"ERROR: {e}", file=sys.stderr)
        return 2

    wanted = {i.upper().strip() for i in args.isins}
    found = {}
    for cells in rows:
        for c in cells:
            if c.upper() in wanted:
                found.setdefault(c.upper(), []).append(cells)
    print(f"Checked on: {date.today().isoformat()}  (rows scanned: {len(rows)})")
    missing = False
    for isin in sorted(wanted):
        hits = found.get(isin)
        if hits:
            print(f"FOUND   {isin}")
            for h in hits:
                print("        " + " | ".join(x for x in h if x))
        else:
            missing = True
            print(f"MISSING {isin}  (not on the HMRC reporting funds list as of the file date above)")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
