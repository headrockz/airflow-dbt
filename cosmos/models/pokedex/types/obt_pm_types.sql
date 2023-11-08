config(
    materialized=table
)

select
    p.type
    ,p.qtd as qtd_pokemons
    ,m.qtd as qtd_moves
FROM {{ ref("tb_moves_types") }} m
join {{ ref("tb_pokemon_types")}} p on p.type=m.type