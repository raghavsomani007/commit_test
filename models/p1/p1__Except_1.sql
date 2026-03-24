{{
  config({    
    "materialized": "ephemeral",
    "database": "raghav",
    "schema": "default"
  })
}}

WITH Pipeline_1 AS (

  SELECT *
  
  FROM {{ prophecy_tmp_source('p1', 'Pipeline_1') }}

),

Except_1 AS (

  SELECT * 
  
  FROM Pipeline_1 AS in0
  
  EXCEPT
  
  SELECT * 
  
  FROM `` AS in1

)

SELECT *

FROM Except_1
