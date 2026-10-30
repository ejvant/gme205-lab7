import os

import psycopg
from dotenv import load_dotenv

# Load DB settings from the .env file (kept out of Git)
load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": os.getenv("DB_PORT", "5432"),
}


def check_connection():
    """Confirm that Python can reach PostgreSQL and PostGIS."""
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            row = conn.execute(
                "SELECT current_database(), PostGIS_Version();"
            ).fetchone()
        print("Connection successful.")
        print("Database:", row[0])
        print("PostGIS:", row[1])
        return True
    except psycopg.Error as error:
        print("Connection failed.")
        print("Database error:", error)
        return False

def fetch_parcels_by_land_use(land_use):
    """Return parcels with the given land use; geometry as GeoJSON in EPSG:4326."""
    query = """
        SELECT
            parcel_id,
            land_use,
            ST_AsGeoJSON(
                ST_Transform(geom, 4326)
            ) AS geometry_json
        FROM lab6.parcels
        WHERE land_use = %s
        ORDER BY parcel_id;
    """
    with psycopg.connect(**DB_CONFIG) as conn:
        return conn.execute(
            query,
            (land_use,),   # value passed separately, not inside the SQL text
        ).fetchall()

if __name__ == "__main__":
    # Temporary checks
    check_connection()

    rows = fetch_parcels_by_land_use("Residential")
    print("Rows returned:", len(rows))
    if rows:
        print("First database row:", rows[0])