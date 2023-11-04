{{
    config(materialized='table')
}}

select 
    type_1 as type
    ,count(1) as qtd
    ,'{{ var("my_name") }}' as start_date
FROM {{source('pokedex', 'pokemons')}}
GROUP BY 1
ORDER BY 1