--https://www.hackerrank.com/challenges/challenges
SELECT h.hacker_id, h.name, SUM(t.max_score) AS total
FROM (SELECT hacker_id, challenge_id, MAX(score) AS max_score FROM submissions GROUP BY 1,2) as t, hackers AS h 
WHERE h.hacker_id = t.hacker_id
GROUP BY h.hacker_id, h.name HAVING total>0
ORDER BY total DESC, h.hacker_id
