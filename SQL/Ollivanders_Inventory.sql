--https://www.hackerrank.com/challenges/harry-potter-and-wands
SELECT w.id, x.age, x.min_price, w.power FROM wands AS w
JOIN 
(SELECT w.code, wp.age, MIN(w.coins_needed) AS min_price, w.power 
FROM wands AS w, wands_property AS wp WHERE w.code = wp.code AND wp.is_evil = 0
GROUP BY wp.age, wp.code, w.power) as x
ON w.code = x.code AND w.coins_needed = x.min_price
ORDER BY w.power DESC, x.age DESC
