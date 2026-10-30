# GmE 205: Laboratory Exercise 7
**Python–PostGIS to Interoperable GeoJSON**
## Overview
*This laboratory exercise demonstrates how to connect Python to a PostgreSQL/PostGIS database, retrieve spatial records, convert them into Python objects, and export validated GeoJSON FeatureCollections. It focuses on spatial data transformation and interoperability between different applications.*

## Environment

| Item | Value |
|---|---|
| Database | `gme205_lab6` (Lab 6 database, `lab6` schema) |
| PostgreSQL | 18.6 |
| PostGIS | 3.6 |
| Python | 3.14.7 |
| Packages | see `requirements.txt` (psycopg 3, python-dotenv) |

## Prerequisites

- **PostgreSQL + PostGIS** – spatial database
- **pgAdmin 4** – checks the database and runs the one-time seed SQL through the Query Tool
- **Python 3** – runs the workflow in `src/`
- **psycopg 3** – connects Python to PostgreSQL/PostGIS
- **python-dotenv** – loads database settings from `.env`
- **VS Code** – edits Python, Markdown, and configuration files
- **Git / GitHub** – version control and submission

## Setup

1. Create and activate a virtual environment:
   ```cmd
   py -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and fill in your own database password.
3. Make sure `lab6.parcels` contains P-001 to P-004 (Part A seed SQL).
4. Run from the project root:
   ```cmd
   python src/run_lab7.py
   ```

## Run Output

```
Connection successful.
Database: gme205_lab6
PostGIS: 3.6 USE_GEOS=1 USE_PROJ=1 USE_STATS=1
Rows returned: 2
Parcel objects created: 2
First Parcel object: P-001 Residential
GeoJSON type: FeatureCollection
Feature count: 2
GeoJSON contract check: PASSED
Output written: output\residential_parcels.geojson
File exists: True
```

## Data Path

1. *What responsibility belongs to PostgreSQL/PostGIS?*
PostgreSQL/PostGIS stores the parcel data and retrieve the records needed. It filters rows by land use, converts their geometry, and formats it as GeoJSON.
2. *Why is `land_use` passed as a query parameter?*
The SQL command and the value are sent separately. This makes sure the value is treated as data, and not as part of the SQL command. It also prevents SQL injection and quoting errors, and allows the same query to be used for different land-use types.
3. *What changes when a database row becomes a Parcel object?*
A row is just a tuple, where it stores values by position, such as `row[0]` and `row[1]`. When converted into a Parcel object, the data gets named attributes, such as `parcel_id`, `land_use`, and `geometry`. The object can also perform actions, such as creating a GeoJSON Feature.
4. *What changes when a Parcel object becomes a GeoJSON Feature?*
The object is converted into a standard dictionary with type, id, geometry, and properties. This allows other GIS applications to read the data without needing the original Python class.
5. *Why is `ST_Transform(..., 4326)` placed at the exchange boundary?*
The data remains in EPSG:32651 (meters) inside the database for accurate spatial measurements, so area and distance calculations stay correct. GeoJSON expects WGS 84 longitude/latitude, so the conversion happens only when the data leaves the system.
6. *Why is a valid GeoJSON file an interoperability exercise without an API?*
Interoperability means that different applications can use and understand the same data format. A valid GeoJSON file can be opened in different GIS programs without needing to know how it was created. This was shown when GitHub automatically rendered `output/residential_parcels.geojson` as an interactive map, displaying P-001 and P-002 without any knowledge of my Python code. An API would only be a different way to share and deliver the data. 

## Author
Enoch Joshua V. Antonio  
MS Geomatics Engineering

## References

- Psycopg 3 documentation – connections and parameterized queries: https://www.psycopg.org/psycopg3/docs/basic/params.html
- PostGIS documentation – `ST_AsGeoJSON`: https://postgis.net/docs/ST_AsGeoJSON.html
- PostGIS documentation – `ST_Transform`: https://postgis.net/docs/ST_Transform.html
- RFC 7946 – The GeoJSON Format: https://datatracker.ietf.org/doc/html/rfc7946
- OGC API – Features (conceptual reference only; no API endpoint is implemented in this laboratory): https://ogcapi.ogc.org/features/

Edited on GitHub web interface and VS Code