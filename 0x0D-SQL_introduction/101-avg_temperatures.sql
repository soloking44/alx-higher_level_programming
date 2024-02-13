-- this is code to shows the average temperature (Fahrenheit) to city ordered by temperature (descending).
SELECT city,
	AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
