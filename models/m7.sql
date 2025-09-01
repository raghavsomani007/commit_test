WITH s1 AS (

  SELECT * 
  
  FROM {{ ref('s1')}}

)

SELECT 123

FROM s1
