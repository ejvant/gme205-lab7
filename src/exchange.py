def build_feature_collection(parcels):
    return {
        "type": "FeatureCollection",
        "features": [
            parcel.to_feature()
            for parcel in parcels
        ],
    }