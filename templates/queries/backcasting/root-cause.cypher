MATCH (n:RootCause)
WHERE n.id IN $rc_ids
RETURN 
  n.id AS id,
  n.title AS title,
  n.description AS description,
  n.context AS context,
  n.impact AS impact,
  n.introduced_in_phase AS introduced_in_phase,
  n.reviewable_in_phase AS reviewable_in_phase
ORDER BY id;