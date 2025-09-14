-- Sample data for UGA vs Tennessee football statistics
-- Run this after creating the schema to populate with sample records

-- Football statistics data (goals = touchdowns, assists = yards)
INSERT INTO athletes_data (name, position, goals, assists, club_name, game_year) VALUES
('Carson Beck', 'QB', 3, 347, 'UGA', 2024),
('Dylan Sampson', 'RB', 2, 178, 'Tennessee', 2024),
('Ladd McConkey', 'WR', 2, 135, 'UGA', 2023),
('Hendon Hooker', 'QB', 1, 245, 'Tennessee', 2022),
('Stetson Bennett', 'QB', 4, 289, 'UGA', 2022),
('Kenny McIntosh', 'RB', 2, 156, 'UGA', 2021),
('JT Daniels', 'QB', 3, 312, 'UGA', 2021),
('Jabari Small', 'RB', 1, 89, 'Tennessee', 2021),
('D''Andre Swift', 'RB', 3, 186, 'UGA', 2020),
('Jarrett Guarantano', 'QB', 0, 147, 'Tennessee', 2020),
('Jake Fromm', 'QB', 2, 221, 'UGA', 2019),
('Brian Maurer', 'QB', 1, 156, 'Tennessee', 2019),
('Elijah Holyfield', 'RB', 2, 128, 'UGA', 2018),
('Ty Chandler', 'RB', 0, 45, 'Tennessee', 2018),
('Sony Michel', 'RB', 3, 145, 'UGA', 2017),
('John Kelly', 'RB', 0, 87, 'Tennessee', 2017),
('Nick Chubb', 'RB', 2, 119, 'UGA', 2016),
('Joshua Dobbs', 'QB', 2, 312, 'Tennessee', 2016);

-- Keep sample_table data for backwards compatibility
INSERT INTO sample_table (first_name, last_name, date_of_birth) VALUES
('John', 'Smith', '1990-05-15'),
('Jane', 'Doe', '1985-08-22'),
('Michael', 'Johnson', '1992-12-03'),
('Sarah', 'Williams', '1988-03-17'),
('David', 'Brown', '1995-09-08');