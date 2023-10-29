{{
    config(materialized='table')
}}

select concat('hello ', '{{ var("my_name") }}') as name