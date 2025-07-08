MATCH (n:Symptom)
WHERE n.id IN $symptom_ids
RETURN 
  n.id AS id,
  n.title AS title,
  n.description AS description,
  n.context AS context
ORDER BY id;