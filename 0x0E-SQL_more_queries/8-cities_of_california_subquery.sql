-- this is the code to display every cities in California that is found in database hbtn_0d_usa
SELECT id,
	name
FROM cities
WHERE state_id = (
		SELECT id
		FROM states
		WHERE name = 'California'
	)
ORDER BY id;
