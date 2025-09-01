WITH s1 AS (

  SELECT * 
  
  FROM {{ ref('s1')}}

)

SELECT `First Name`

FROM s1
