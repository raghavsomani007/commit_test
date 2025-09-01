{%- macro g2(table_name1) -%}
    select * from {{ table_name }}
{%- endmacro -%}

{%- macro g1(table_name) -%}
    select * from {{ table_name }}
{%- endmacro -%}
