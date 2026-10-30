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


if __name__ == "__main__":
    # Temporary check
    check_connection()