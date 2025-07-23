# stac2geojson
Because sometimes you just want one GeoJSON.

There are many *static* STAC catalogs out there that don't have an API for searching, and while [STAC Browser](https://radiantearth.github.io/stac-browser) is a great web app for exploring these catalogs by Item, sometimes you just want a single GeoJSON to view *all* items in a catalog or collection at once. This works well for smallish catalogs (<1000 Items).

This script creates a copy only of fundamental properties (id, datetime, geometry) and adds a link back to the STAC-browser for convenience in case you want to view the full metadata or download assets. It also optionally creates a `-centroids.geojson` file, because it can be hard to initially see small footprints in a collection when viewing a global map!

## Create GeoJSON

#### Via Pixi Task
```
CATALOG="https://www.planet.com/data/stac/tanager-core-imagery/snow-ice/collection.json"
pixi run convert $CATALOG snow-ice.geojson --centroids
```

#### Or via standard python script
```
python stac2geojson.py $CATALOG snow-ice.geojson --centroids
```

#### Or via a GitHub Action

This saves the geojson as an output artifact, which you can access for 90 days
```
gh -R uw-cryo/stac2geojson workflow run convert.yml -f catalog=$CATALOG
```

We recommend adding the geojson outputs to a GitHub repository so that you can use different tools to visualize them:

## Visualize GeoJSON

### GitHub:

(Nice defaults for lots of crowded centroids)

- https://github.com/uw-cryo/stac2geojson/blob/main/planet/tanager/snow-ice-centroids.geojson

### GeoJSON.io:

(Great interactive map with more customizations)

- https://geojson.io/#id=github:uw-cryo/stac2geojson/blob/main/planet/tanager/snow-ice.geojson
- https://geojson.io/#id=github:uw-cryo/stac2geojson/blob/main/planet/tanager/snow-ice-centroids.geojson
