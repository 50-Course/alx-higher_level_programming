-- Lists the number of records with the same score in the db
SELECT score, COUNT(score) AS 'number'
FROM second_table
ORDER BY number DESC;
