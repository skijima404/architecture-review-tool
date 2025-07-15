MATCH (sc:SuccessCriteria {id: $sc_id})
CALL apoc.path.expand(sc, 'threatened_by|triggered_by|leads_from', null, 1, 10)
YIELD path
UNWIND relationships(path) AS rel
RETURN DISTINCT
  startNode(rel).id AS from_id,
  labels(startNode(rel))[0] AS from_type,
  type(rel) AS relation,
  endNode(rel).id AS to_id,
  labels(endNode(rel))[0] AS to_type
ORDER BY from_id, relation, to_id;