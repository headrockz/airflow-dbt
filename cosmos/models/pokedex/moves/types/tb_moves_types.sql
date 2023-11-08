{{
    config(materialized='table')
}}

select 
    type
    ,count(1) as qtd
    ,'{{ var("start_date") }}' as start_date
FROM {{source('pokedex', 'moves')}}
GROUP BY 1
ORDER BY 1