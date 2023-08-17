-- 9-cities_by_state_join.sql
SELECT
    cities.id, cities.name, states.name
FROM
    cities
INNER JOIN
    states
ON
    cities.state_id = states.id