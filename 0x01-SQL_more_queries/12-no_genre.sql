-- Lists all shows in hbtn_0d_tvshows that have no genre linked
-- Record display: tv_shows.title - tv_shows_genres.genre_id
-- Sorted in ascending order by tv_shows.title and tv_shows_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres
