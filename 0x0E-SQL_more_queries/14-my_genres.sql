-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name.
SELECT `name` FROM `tv_genres` `tg` 
INNER JOIN `tv_show_genres` `tsg` ON `tg`.`id` = `tsg`.`genre_id`
INNER JOIN `tv_shows` `ts` ON `tsg`.`show_id` = `ts`.`id`
WHERE `ts`.`title` = 'Dexter'
ORDER BY `name` ASC;
