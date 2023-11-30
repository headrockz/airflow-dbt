{{config(
    materialized='table',
    enabled=true,
    tags=['pokemons'],
    )
}}

with cte as (
    SELECT 
        type_1 AS type
        ,count(1) AS qtd
    FROM {{source('pokedex', 'pokemons')}}
    GROUP BY 1
    -- union
    -- select 'z' as type, 1 as qtd
)

SELECT * FROM cte