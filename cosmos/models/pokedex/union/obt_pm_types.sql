{{
    config(materialized='table')
}}

SELECT 
    p.type as type_pokemon
    ,m.type as type_moves
    ,p.count(1) as qtd_pokemons
    ,m.count(1) as qtd_moves
FROM {{ref("tb_pokemon_types")}} p
JOIN {{ref("tb_moves_types")}} m on m.type = p.type
GROUP BY 1