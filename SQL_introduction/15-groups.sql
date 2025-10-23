-- 15-gropups.sql

SELECT score count(*) AS number
FROM second_table
GROUB BY score
ORDER BY number DESC;
