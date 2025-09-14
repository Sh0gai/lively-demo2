-- Database Schema for UGA vs Tennessee Football Statistics
-- Run this file to create the required database structure

-- Create athletes_data table for football statistics
CREATE TABLE athletes_data (
    athlete_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    position VARCHAR(50) NOT NULL,
    goals INT DEFAULT 0,  -- This will represent touchdowns
    assists INT DEFAULT 0,  -- This will represent yards
    points INT GENERATED ALWAYS AS (goals * 6) STORED,  -- Calculate points as touchdowns * 6
    club_name VARCHAR(50) NOT NULL,  -- Team (UGA or Tennessee)
    game_year INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Add indexes for common queries
CREATE INDEX idx_athletes_name ON athletes_data (name);
CREATE INDEX idx_athletes_team ON athletes_data (club_name);
CREATE INDEX idx_athletes_year ON athletes_data (game_year);

-- Keep the original sample_table for backwards compatibility
CREATE TABLE sample_table (
    sample_table_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Add indexes for sample_table
CREATE INDEX idx_sample_table_name ON sample_table (last_name, first_name);
CREATE INDEX idx_sample_table_dob ON sample_table (date_of_birth);