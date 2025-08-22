# Inject GraphDB Nodes (Step 4)

## Role Transition
At this step, the assistant transitions from general context gathering to actively injecting relevant nodes from the GraphDB into the review process. The assistant acts as a bridge between the graph data layer and the ongoing architectural analysis.

## Objective
The primary objective is to provide the review process with specific nodes from the GraphDB, ensuring that all necessary entities, their properties, and relationships are available for subsequent analysis and decision-making.

## Inputs Expected Before Triggering
- **Single Success Criteria Node ID:** Only one Success Criteria node identifier is required as input. All related node types, properties, and relationships will be retrieved automatically from GraphDB.

## Output Contents
- A structured representation of the selected GraphDB nodes.
- For each node: ID, type, properties, and relevant relationships.
- Contextual information about how these nodes fit into the current review phase.
- Any applied filters or constraints noted explicitly.
- **Note:** Interpretation or findings are explicitly excluded at this step; output must be plain data only.

## Output Format Location
- The output should be inserted into the review sequence at the designated "GraphDB Nodes Injection" step (Step 4).
- The standard output format is a JSON block, with an optional Markdown table for human readability.
- Designated save paths for outputs:
  - `review-log/<review-id>/input/injected-nodes.json`
  - `review-log/<review-id>/input/injected-nodes.md` (optional).

## Notes
- This step is crucial for grounding the review in actual system data.
- Ensure completeness: all nodes necessary for the current and upcoming steps should be included.
- Placeholder: Further details on node/relationship schemas, output serialization, and integration points will be added as the process is refined.
