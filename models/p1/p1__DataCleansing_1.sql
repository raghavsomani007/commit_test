{{
  config({    
    "materialized": "ephemeral",
    "database": "raghav",
    "schema": "default"
  })
}}

WITH DataCleansing_1 AS (

  {{
    DatabricksSqlBasics.DataCleansing(
      '', 
      '', 
      'Keep original', 
      [], 
      false, 
      'NA', 
      false, 
      0, 
      false, 
      false, 
      false, 
      false, 
      false, 
      false, 
      false, 
      false, 
      '1970-01-01', 
      false, 
      '1970-01-01 00:00:00.0'
    )
  }}

)

SELECT *

FROM DataCleansing_1
