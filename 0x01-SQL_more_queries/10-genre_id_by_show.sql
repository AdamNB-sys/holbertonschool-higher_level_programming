-- Lists all shows contained in hbtn_0d_tvshows that have at least one genre linked
-- Import database dump hbtn_0d_tvshows from external source (provided in task)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
