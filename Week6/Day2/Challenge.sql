-- Q1. Quelle sera la SORTIE de l'instruction suivante ?
SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
-- sorti 0
--apres execution 0

-- Q2. Quelle sera la SORTIE de l'instruction suivante ?

  SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- sorti 0
--apres execution 2

-- Q3. Quelle sera la SORTIE de l'instruction suivante ?

 SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN (SELECT id FROM SecondTab)

-- sorti 0
--apres execution 0

-- Q4. Quelle sera la SORTIE de l'instruction suivante ?

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
-- sorti 2
--apres execution 2