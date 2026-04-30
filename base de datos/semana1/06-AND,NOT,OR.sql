-- NOT
-- AND
-- OR

    
    SELECT *
    FROM users 
    WHERE NOT email = 'diego@gmail.com'

SELECT *
FROM users
WHERE NOT email = 'diego@gmail.com' AND age = 15

SELECT *
FROM users
WHERE NOT email = 'diego@gmail.com' OR age = 15
