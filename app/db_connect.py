import sqlite3
from flask import g
import os

def get_db():
    if 'db' not in g:
        print("Establishing new database connection.")
        try:
            # Use SQLite for simplicity - database file will be created automatically
            db_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'football_stats.db')
            g.db = sqlite3.connect(db_path)
            g.db.row_factory = sqlite3.Row  # This makes rows behave like dictionaries

            # Initialize database if it doesn't exist
            init_db()

        except Exception as e:
            print(f"Database connection failed: {e}")
            g.db = None
            return None
    return g.db

def init_db():
    """Initialize the database with tables and sample data if they don't exist."""
    db = g.db

    # Check if athletes_data table exists
    cursor = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='athletes_data'")
    if not cursor.fetchone():
        print("Creating athletes_data table...")

        # Create the table
        db.execute('''
            CREATE TABLE athletes_data (
                athlete_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                position TEXT NOT NULL,
                goals INTEGER DEFAULT 0,
                assists INTEGER DEFAULT 0,
                points INTEGER,
                club_name TEXT NOT NULL,
                game_year INTEGER,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')

        # Create indexes
        db.execute('CREATE INDEX idx_athletes_name ON athletes_data (name)')
        db.execute('CREATE INDEX idx_athletes_team ON athletes_data (club_name)')
        db.execute('CREATE INDEX idx_athletes_year ON athletes_data (game_year)')

        # Insert sample data
        sample_data = [
            ('Mary Johnson', 'Teacher', 5, 120, 'Gray', 2020),
            ('Robert Smith', 'Farmer', 3, 80, 'Round Oak', 2018),
            ('Linda Williams', 'Nurse', 4, 150, 'Gray', 2019),
            ('James Brown', 'Mechanic', 2, 60, 'Haddock', 2021),
            ('Patricia Davis', 'Librarian', 6, 200, 'Gray', 2017),
            ('Michael Wilson', 'Pastor', 8, 300, 'Round Oak', 2015),
            ('Jennifer Moore', 'Business Owner', 4, 100, 'Gray', 2022),
            ('David Taylor', 'Police Officer', 3, 90, 'Gray', 2020),
            ('Sarah Anderson', 'Real Estate Agent', 5, 140, 'Haddock', 2019),
            ('Christopher Thomas', 'Fire Chief', 7, 250, 'Gray', 2016),
            ('Lisa Jackson', 'Bank Manager', 3, 75, 'Round Oak', 2021),
            ('Mark White', 'County Commissioner', 10, 400, 'Gray', 2014),
            ('Nancy Harris', 'Veterinarian', 4, 110, 'Haddock', 2018),
            ('Richard Martin', 'Construction Worker', 2, 50, 'Round Oak', 2023),
            ('Susan Thompson', 'School Principal', 6, 180, 'Gray', 2017),
            ('Kevin Garcia', 'Auto Shop Owner', 3, 70, 'Haddock', 2020),
            ('Angela Martinez', 'Healthcare Worker', 5, 160, 'Gray', 2019),
            ('Charles Robinson', 'Retired Military', 4, 130, 'Round Oak', 2022)
        ]

        for data in sample_data:
            name, position, goals, assists, club_name, game_year = data
            points = goals * 10 + assists // 10  # Calculate community score as projects*10 + volunteer_hours/10
            db.execute('''
                INSERT INTO athletes_data (name, position, goals, assists, points, club_name, game_year)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (name, position, goals, assists, points, club_name, game_year))

        db.commit()
        print("Database initialized with sample data.")

def close_db(exception=None):
    db = g.pop('db', None)
    if db is not None:
        print("Closing database connection.")
        db.close()