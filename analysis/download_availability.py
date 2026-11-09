"""Download one complete Minneapolis calendar day, not a random 2024 sample.

Run: python3 analysis/download_availability.py
Requires Python 3.9+; uses only the Python standard library.
"""

import csv
import json
import time
from datetime import date, datetime, time as midnight, timedelta, timezone
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import urlopen
from zoneinfo import ZoneInfo


SERVICE = (
    "https://services.arcgis.com/afSMGVsC7QlRK1kZ/arcgis/rest/services/"
    "Scooter_and_Bike_Availability_2024/FeatureServer/0"
)
ITEM_URL = (
    "https://www.arcgis.com/sharing/rest/content/items/"
    "c9e75387ca8343ab8a68a4f3446cd9bc"
)
DAY = date(2024, 7, 15)
TIME_ZONE = "America/Chicago"
DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def get_json(url, params=None):
    """Fetch an ArcGIS response, retrying network errors up to twice."""
    query = urlencode({"f": "json", **(params or {})})
    for attempt in range(3):
        try:
            with urlopen(f"{url}?{query}", timeout=120) as response:
                result = json.load(response)
            break
        except (URLError, TimeoutError):
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)
    if "error" in result:
        raise RuntimeError(f"ArcGIS query failed: {result['error']}")
    return result


def day_filter(day):
    """Convert local midnight boundaries to UTC, including daylight saving."""
    local_zone = ZoneInfo(TIME_ZONE)
    start = datetime.combine(day, midnight.min, tzinfo=local_zone)
    end = datetime.combine(day + timedelta(days=1), midnight.min, tzinfo=local_zone)
    start_utc = start.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    end_utc = end.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    return (
        f"PollTime >= TIMESTAMP '{start_utc}' AND "
        f"PollTime < TIMESTAMP '{end_utc}'"
    )


def main():
    where = day_filter(DAY)
    print("Retrieving source metadata and row counts...", flush=True)
    item = get_json(ITEM_URL)
    schema = get_json(SERVICE)
    query_url = f"{SERVICE}/query"
    total = get_json(query_url, {
        "where": "1=1", "returnCountOnly": "true",
    })["count"]
    expected = get_json(query_url, {
        "where": where, "returnCountOnly": "true",
    })["count"]
    if expected == 0:
        raise ValueError("The selected day contains no records; choose another day.")
    print(f"Selected day has {expected:,} records; retrieving all pages...", flush=True)

    # The default limit is 1,000. Request larger pages and use stable ID ordering.
    availability = []
    while True:
        page = get_json(query_url, {
            "where": where, "outFields": "*", "returnGeometry": "false",
            "orderByFields": "ObjectId ASC", "resultOffset": len(availability),
            "resultRecordCount": 32000, "resultType": "standard",
        })
        rows = [feature["attributes"] for feature in page["features"]]
        if not rows:
            break
        availability.extend(rows)
        print(f"Downloaded {len(availability):,} / {expected:,} rows", flush=True)
        if not page.get("exceededTransferLimit", False):
            break

    # Explicit checks also run when Python is invoked with optimization enabled.
    if len(availability) != expected:
        raise ValueError(f"Expected {expected} rows, received {len(availability)}.")
    if len({row["ObjectId"] for row in availability}) != expected:
        raise ValueError("The downloaded records contain duplicate ObjectIds.")

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    csv_path = DATA_DIR / f"availability_{DAY.isoformat()}.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as output:
        writer = csv.DictWriter(output, fieldnames=[field["name"] for field in schema["fields"]])
        writer.writeheader()
        writer.writerows(availability)

    metadata = {
        "retrieved_utc": datetime.now(timezone.utc).isoformat(),
        "day_local": DAY.isoformat(), "time_zone": TIME_ZONE, "where": where,
        "full_dataset_rows": total, "subset_rows": expected,
        "service": SERVICE, "item": item, "schema": schema,
    }
    metadata_path = DATA_DIR / "availability_metadata.json"
    metadata_path.write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")
    print("Saved complete one-day subset and source metadata under data/.")


if __name__ == "__main__":
    main()
