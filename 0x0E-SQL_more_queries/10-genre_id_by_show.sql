-- 10-genre_id_by_show.sql

SELECT tv_shows.titles, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_shows_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;