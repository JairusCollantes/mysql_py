
CREATE DATABASE IF NOT EXISTS playlist_db;
USE playlist_db;

CREATE TABLE playlists (
    playlist_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    description TEXT
);

CREATE TABLE songs (
    song_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(150),
    channel VARCHAR(150),
    is_original BOOLEAN,
    duration DECIMAL(4,2),
    playlist_id INT,
    FOREIGN KEY (playlist_id) REFERENCES playlists(playlist_id)
);

INSERT INTO playlists (name, description) VALUES
('Hololive', 'Hololive original songs and covers'),
('Sad', 'Emotional damage playlist'),
('Low Cortisol', 'Chill / calm songs');

INSERT INTO songs (title, channel, is_original, duration, playlist_id) VALUES
-- Hololive playlist
('ROCK IN!', 'Koseki Bijou', TRUE, 2.57, 1),
('Gachca X Gacha', 'Raora Panthera', TRUE, 3.11, 1),
('SNAKE EYES', 'Hakos Baelz', TRUE, 3.46, 1),
('Your Idol', 'Nerissa Ravencroft', FALSE, 3.01, 1),
('Hibana', 'Raora Panthera', FALSE, 3.27, 1),
('Wind-Up', 'Cecilia Immergreen', TRUE, 3.29, 1),
('HOLOTORI Dance!', 'hololive English', TRUE, 3.21, 1),
('ABOVE BELOW', 'hololive English', TRUE, 4.06, 1),
-- Sad playlist
('Drag Path', 'twenty one pilots', TRUE, 3.44, 2),
('back to friends', 'sombr', TRUE, 3.20, 2),
('Habits (Stay High)', 'Tove Lo', TRUE, 3.29, 2),
('Treat You Better', 'Shawn Mendes', TRUE, 2.48, 2),
('Bawat piyesa', 'Munimuni', TRUE, 6.26, 2),
-- Low Cortisol playlist
('See Tinh (Remix)', 'Cukak', FALSE, 4.17, 3),
('Ai Đưa Em Về', 'TIA', TRUE, 3.50, 3);

SELECT * FROM songs;

UPDATE songs
SET duration = 3.00
WHERE title = 'ROCK IN!';

DELETE FROM songs
WHERE title = 'back to friends';

SELECT * FROM songs
ORDER BY duration DESC;

SELECT * FROM songs
WHERE playlist_id = 1;

SELECT * FROM songs
WHERE is_original = FALSE;

SELECT * FROM songs
WHERE title LIKE 'S%';

SELECT p.name AS playlist_name, COUNT(s.song_id) AS total_songs
FROM playlists p
JOIN songs s ON p.playlist_id = s.playlist_id
GROUP BY p.name;

SELECT AVG(duration) AS avg_duration
FROM songs;

SELECT * FROM songs
WHERE channel LIKE '%hololive%' OR channel LIKE '%Holo%';