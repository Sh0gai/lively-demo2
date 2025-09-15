#!/usr/bin/env python3
"""Test script to initialize and verify the database."""

from app import app
from app.db_connect import get_db
from flask import g

def test_database():
    """Test database initialization and basic operations."""
    with app.app_context():
        print("Testing database connection...")

        # Get database connection
        db = get_db()

        if db is None:
            print("[FAIL] Database connection failed!")
            return False

        print("[PASS] Database connection successful!")

        # Test querying data
        try:
            cursor = db.execute("SELECT COUNT(*) as count FROM athletes_data")
            result = cursor.fetchone()
            count = result['count']
            print(f"[PASS] Found {count} records in athletes_data table")

            # Show a few sample records
            cursor = db.execute("SELECT name, position, club_name, game_year, goals, assists, points FROM athletes_data LIMIT 5")
            records = cursor.fetchall()

            print("\nSample records:")
            print("-" * 60)
            for record in records:
                print(f"{record['name']} ({record['position']}) - {record['club_name']} {record['game_year']}")
                print(f"   Projects: {record['goals']}, Volunteer Hours: {record['assists']}, Community Score: {record['points']}")
                print()

            return True

        except Exception as e:
            print(f"[FAIL] Database query failed: {e}")
            return False

if __name__ == '__main__':
    success = test_database()
    if success:
        print("Database test completed successfully!")
    else:
        print("Database test failed!")