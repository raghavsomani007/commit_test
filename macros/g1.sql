{%- macro g234(table_name1) -%}
    select * from {{ table_name }}
{%- endmacro -%}


{%- macro g1234(table_name) -%}
    select * from {{ table_name }}
{%- endmacro -%}

}
