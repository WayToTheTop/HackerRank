--https://www.hackerrank.com/challenges/full-score
SELECT s.hacker_id, h.name 
FROM submissions AS s,
     challenges AS c,
     difficulty AS d,
     hackers AS h
WHERE s.challenge_id = c.challenge_id AND
      d.difficulty_level = c.difficulty_level AND
      s.hacker_id = h.hacker_id AND
      s.score = d.score
GROUP BY s.hacker_id, h.name
HAVING COUNT(*)>1
ORDER BY COUNT(*) DESC, s.hacker_id ASC
