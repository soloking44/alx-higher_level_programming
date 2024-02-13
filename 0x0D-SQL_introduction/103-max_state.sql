-- this is code that lists the max temperature of every state (ordered by State name).
SELECT state,
	MAX(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
