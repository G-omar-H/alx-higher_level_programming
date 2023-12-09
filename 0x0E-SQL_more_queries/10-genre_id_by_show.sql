--script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
--	Each record should display: tv_shows.title - tv_show_genres.genre_id
--	 Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
select `ts`.`title`, `tg`.`genre_id` FROM `tv_shows` `ts` RIGHT OUTER JOIN `tv_show_genres` `tg` ON `ts`.`id` = `tg`.`show_id`
ORDER BY `ts`.`title` AND `tg`.`genre_id` ASC;
