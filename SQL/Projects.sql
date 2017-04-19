--https://www.hackerrank.com/challenges/projects
SELECT t1.start_date, MIN(t2.end_date) FROM
(SELECT start_date FROM projects WHERE start_date NOT IN (SELECT end_date FROM projects)) t1,
(SELECT end_date FROM projects WHERE end_date NOT IN (SELECT start_date FROM projects)) t2
WHERE t1.start_date < t2.end_date
GROUP BY 1
ORDER BY (MIN(t2.end_date) - t1.start_date),1
