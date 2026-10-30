import json

from database import fetch_parcels_by_land_use
from spatial import Parcel
from exchange import build_feature_collection

rows = fetch_parcels_by_land_use("Residential")
print("Rows returned:", len(rows))
if rows:
    print("First database row:", rows[0])

parcels = [
    Parcel.from_row(row)
    for row in rows
]

print("Parcel objects created:", len(parcels))
if parcels:
    first = parcels[0]
    print(
        "First Parcel object:",
        first.parcel_id,
        first.land_use,
    )

collection = build_feature_collection(parcels)
print("GeoJSON type:", collection["type"])
print("Feature count:", len(collection["features"]))
if collection["features"]:
    print(
        "First feature:",
        json.dumps(
            collection["features"][0],
            indent=2,
        ),
    )