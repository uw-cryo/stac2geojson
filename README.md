# stac2geojson
Because sometimes you just want one GeoJSON

## Create GeoJSON

#### Via Pixi Task
```
CATALOG="https://www.planet.com/data/stac/tanager-core-imagery/snow-ice/collection.json"
pixi run convert $CATALOG
```

#### Which is shorthand for the python script:
```
python stac2geojson.py $CATALOG snow-ice.geojson --centroids
```

#### Via GitHub Action
```
gh -R uw-cryo/stac2geojson workflow run convert.yml -f catalog=$CATALOG
```

This saves the geojson as an output artifact


We recommend adding the geojson outputs to a GitHub repository so that you can use different tools to visualize them:

## Visualize GeoJSON

### GitHub:

(Nice defaults for lots of crowded centroids)

- https://github.com/uw-cryo/stac2geojson/blob/main/planet/tanager/snow-ice-centroids.geojson

### GeoJSON.io:

(Great interactive map with more customizations)

- https://geojson.io/#id=github:uw-cryo/stac2geojson/blob/main/planet/tanager/snow-ice.geojson
- https://geojson.io/#id=github:uw-cryo/stac2geojson/blob/main/planet/tanager/snow-ice-centroids.geojson
