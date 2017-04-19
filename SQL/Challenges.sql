--https://www.hackerrank.com/challenges/challenges/submissions/database/42627135
SELECT a.hacker_id, a.name, COUNT(*) as total 
FROM hackers AS a, challenges AS b WHERE a.hacker_id = b.hacker_id
GROUP BY a.hacker_id, a.name
HAVING total = (SELECT COUNT(*) FROM challenges GROUP BY hacker_id ORDER BY COUNT(*) DESC LIMIT 1)
    OR total NOT IN (SELECT t.x FROM (SELECT COUNT(*) AS x FROM challenges GROUP by hacker_id) as t
GROUP BY t.x
HAVING COUNT(*) > 1)
ORDER BY total DESC, hacker_id
