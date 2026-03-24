{{
  config({    
    "materialized": "ephemeral",
    "database": "raghav",
    "schema": "default"
  })
}}

WITH SQLStatement_0 AS (

  

),

SQLStatement_0_1 AS (

  

),

Join_1 AS (

  SELECT * 
  
  FROM SQLStatement_0 AS in0
  INNER JOIN SQLStatement_0_1 AS in1

)

SELECT *

FROM Join_1
