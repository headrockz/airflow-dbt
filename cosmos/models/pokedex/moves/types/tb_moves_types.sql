{{
    config(materialized='table')
}}

select 
    type
    ,count(1) as qtd
FROM {{source('pokedex', 'moves')}}
GROUP BY 1
ORDER BY 1