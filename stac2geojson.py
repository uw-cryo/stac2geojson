#!/usr/bin/env python
"""
Create a single GeoJSON FeatureCollection from a Static STAC Catalog/Collection URL


Example:

Be sure to use the raw JSON URL, not the "browser" page:
https://www.planet.com/data/stac/browser/tanager-core-imagery/snow-ice/collection.json

CATALOG="https://www.planet.com/data/stac/tanager-core-imagery/snow-ice/collection.json"
python stac2geojson.py $CATALOG snow-ice.geojson
"""

import asyncio
import rustac
from rustac.store import HTTPStore
import sys
import os

async def catalog2geojson(catalog_url, output_path=None):
    """
    Given path to catalog.json read all child items & save as STAC-geoparquet
    """
    baseurl, catalog_name = os.path.split(catalog_url)
    store = HTTPStore(baseurl)
    catalog = await rustac.read(catalog_name, store=store)

    all_items = []
    async for _, _, items in rustac.walk(catalog):
        all_items.extend(items)

    if not output_path:
        output_path = "catalog.geojson"

    # Many format options https://stac-utils.github.io/rustac-py/latest/api/#format
    await rustac.write(output_path, all_items, format="ndjson")


if __name__ == "__main__":
    catalog_url = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    asyncio.run(catalog2geojson(catalog_url, output_path))
