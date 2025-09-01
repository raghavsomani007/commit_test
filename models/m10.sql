WITH s1 AS (

  SELECT * 
  
  FROM {{ ref('s1')}}

)

SELECT 456

FROM s1
