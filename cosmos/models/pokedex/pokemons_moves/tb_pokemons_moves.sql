WITH cte AS (
  SELECT
  	p.name
  	,p.type_1 AS type
  	,count(m.name) AS qtd_moves
  FROM pokemons p
  JOIN {{ source("pokedex", "moves_pokemons") }} mp ON p.id = mp.pokemon_id
  JOIN moves m ON m.id = mp.move_id
 GROUP BY 1, 2
)

SELECT * FROM cte