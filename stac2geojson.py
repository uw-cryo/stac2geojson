#!/usr/bin/env python
"""
Create a single GeoJSON FeatureCollection from a Static STAC Catalog/Collection URL

Usage:
python stac2geojson.py $CATALOG [output.geojson] [--centroids]

Example:

Be sure to use the raw JSON URL, not the "browser" page:
https://www.planet.com/data/stac/browser/tanager-core-imagery/snow-ice/collection.json

CATALOG="https://www.planet.com/data/stac/tanager-core-imagery/snow-ice/collection.json"
python stac2geojson.py $CATALOG snow-ice.geojson --centroids
"""

import asyncio
import rustac
from rustac.store import HTTPStore
import geopandas as gpd
import os
import argparse
import warnings

# We'll just ignore this
# UserWarning: 'crs' was not provided.  The output dataset will not have projection information defined and may not be usable in other systems.
warnings.filterwarnings("ignore", message="'crs' was not provided.", category=UserWarning)

async def catalog2geojson(catalog_url, output_path=None, output_centroids=False):
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

    # Also save polygon centroids for convenient visualization
    # NOTE: requires geopandas and pyarrow dependencies
    if output_centroids:
        outfile = output_path.replace('.geojson', '-centroids.geojson')
        table = rustac.to_arrow(items)
        gf = gpd.GeoDataFrame.from_arrow(table)
        cols = ["id","geometry","datetime"]
        centroids = gf[cols].copy()
        centroids['geometry'] = gf.centroid
        centroids.to_file(outfile, driver='GeoJSON')

    # Many format options https://stac-utils.github.io/rustac-py/latest/api/#format
    await rustac.write(output_path, all_items, format="ndjson")

if __name__ == "__main__":
    # TODO: automatically open browser? https://github.com/jwass/geojsonio.py

    parser = argparse.ArgumentParser(description="Create a single GeoJSON FeatureCollection from a Static STAC Catalog/Collection URL")
    parser.add_argument("catalog_url", help="URL to the STAC catalog or collection JSON")
    parser.add_argument("output_path", nargs="?", default=None, help="Output GeoJSON file path")
    parser.add_argument("--centroids", action="store_true", help="Output centroids instead of full geometries")
    args = parser.parse_args()

    asyncio.run(catalog2geojson(args.catalog_url, args.output_path, args.centroids))
