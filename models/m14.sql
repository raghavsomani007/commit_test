WITH s1 AS (

  SELECT * 
  
  FROM {{ ref('s1')}}

)

SELECT 
  1 AS a,
  2 AS b

FROM s1
