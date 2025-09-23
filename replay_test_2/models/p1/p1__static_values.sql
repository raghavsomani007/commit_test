{{
  config({    
    "materialized": "ephemeral",
    "database": "raghavsomani007_gmail_com_team",
    "schema": "schema"
  })
}}

WITH static_values AS (

  SELECT 
    1 AS a,
    2 AS b,
    3 AS c

)

SELECT *

FROM static_values
