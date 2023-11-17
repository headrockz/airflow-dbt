{{
    config(materialized='table')
}}

select 
    type_1 as type
    ,count(1) as qtd
FROM {{source('pokedex', 'pokemons')}}
GROUP BY 1
ORDER BY 1