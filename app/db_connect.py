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
            ('Carson Beck', 'QB', 3, 347, 'UGA', 2024),
            ('Dylan Sampson', 'RB', 2, 178, 'Tennessee', 2024),
            ('Ladd McConkey', 'WR', 2, 135, 'UGA', 2023),
            ('Hendon Hooker', 'QB', 1, 245, 'Tennessee', 2022),
            ('Stetson Bennett', 'QB', 4, 289, 'UGA', 2022),
            ('Kenny McIntosh', 'RB', 2, 156, 'UGA', 2021),
            ('JT Daniels', 'QB', 3, 312, 'UGA', 2021),
            ('Jabari Small', 'RB', 1, 89, 'Tennessee', 2021),
            ("D'Andre Swift", 'RB', 3, 186, 'UGA', 2020),
            ('Jarrett Guarantano', 'QB', 0, 147, 'Tennessee', 2020),
            ('Jake Fromm', 'QB', 2, 221, 'UGA', 2019),
            ('Brian Maurer', 'QB', 1, 156, 'Tennessee', 2019),
            ('Elijah Holyfield', 'RB', 2, 128, 'UGA', 2018),
            ('Ty Chandler', 'RB', 0, 45, 'Tennessee', 2018),
            ('Sony Michel', 'RB', 3, 145, 'UGA', 2017),
            ('John Kelly', 'RB', 0, 87, 'Tennessee', 2017),
            ('Nick Chubb', 'RB', 2, 119, 'UGA', 2016),
            ('Joshua Dobbs', 'QB', 2, 312, 'Tennessee', 2016)
        ]

        for data in sample_data:
            name, position, goals, assists, club_name, game_year = data
            points = goals * 6  # Calculate points as touchdowns * 6
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