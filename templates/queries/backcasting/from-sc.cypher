MATCH (sc:SuccessCriteria {id: $sc_id})
MATCH (sc)-[rel]->(to)
WHERE type(rel) IN ['THREATENED_BY', 'TRIGGERED_BY', 'LEADS_FROM']
RETURN 
  sc.id AS from_id,
  labels(sc)[0] AS from_type,
  type(rel) AS relation,
  to.id AS to_id,
  labels(to)[0] AS to_type
ORDER BY from_id, relation, to_id;