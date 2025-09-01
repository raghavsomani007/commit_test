{{
  config({    
    "materialized": "ephemeral",
    "database": "raghav",
    "schema": "default"
  })
}}

WITH g1_1 AS (

  {{ test.g1(ref('s1') }}

)

SELECT *

FROM g1_1
