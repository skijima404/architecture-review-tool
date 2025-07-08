MATCH (n:SuccessCriteria)
WHERE n.id IN $sc_ids
RETURN 
  n.id AS id,
  n.title AS title,
  n.description AS description,
  n.rationale AS rationale
ORDER BY id;