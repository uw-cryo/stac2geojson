# stac2geojson
Because sometimes you just want one geojson

## Create GeoJSON

pixi run convert CATALOG="https://www.planet.com/data/stac/tanager-core-imagery/snow-ice/collection.json"
python stac2geojson.py $CATALOG snow-ice.geojson --centroids

We recommend adding the geojson outputs to a GitHub repository so that you can use different tools to visualize them:

## Visualize GeoJSON

### GitHub:
- https://github.com/uw-cryo/stac2geojson/blob/main/planet/tanager/snow-ice.geojson

### GeoJSON.io:
- https://geojson.io/#id=github:uw-cryo/stac2geojson/blob/main/planet/tanager/snow-ice.geojson
- https://geojson.io/#id=github:uw-cryo/stac2geojson/blob/main/planet/tanager/snow-ice-centroids.geojson
