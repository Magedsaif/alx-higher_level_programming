-- Removes record
DELETE FROM
    second_table
WHERE
    score <= 5
ORDER BY
    score DESC
