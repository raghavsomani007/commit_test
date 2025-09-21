{{
  config({    
    "materialized": "ephemeral",
    "database": "raghav",
    "schema": "default"
  })
}}

WITH s1 AS (

  SELECT * 
  
  FROM {{ ref('s1')}}

),

Reformat_1 AS (

  SELECT 
    `First Name` AS `First Name`,
    {{ var('arrstr') }} AS c2
  
  FROM s1 AS in0

)

SELECT *

FROM Reformat_1
