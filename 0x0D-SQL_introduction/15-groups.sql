-- Lists the number of records with the same score in the db
SELECT score, COUNT(DISTINCT score) AS 'number'
FROM second_table
ORDER BY number DESC;
