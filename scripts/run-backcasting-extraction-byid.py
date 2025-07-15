from neo4j import GraphDatabase
import os
import csv

# Neo4j connection parameters
URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
USER = os.getenv("NEO4J_USER", "neo4j")
PASSWORD = os.getenv("NEO4J_PASSWORD", "testpassword")

# Cypher query file paths
QUERY_DIR = "architecture-review-tool/templates/queries/backcasting"
NODE_DIR = QUERY_DIR
EDGE_FILE = os.path.join(QUERY_DIR, "from-sc.cypher")
SYMPTOM_FILE = os.path.join(NODE_DIR, "symptom.cypher")
ROOT_CAUSE_FILE = os.path.join(NODE_DIR, "root-cause.cypher")
SUCCESS_CRITERIA_FILE = os.path.join(NODE_DIR, "success-criteria.cypher")

# Output directory
OUTPUT_DIR = "architecture-review-tool/runs/backcasting"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def read_query(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_csv(filename, headers, rows):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

def run_query(session, query, parameters=None):
    result = session.run(query, parameters)
    return [record.data() for record in result]

def extract_data(sc_id):
    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
    with driver.session() as session:
        # Load queries
        edge_query = read_query(EDGE_FILE)
        symptom_query = read_query(SYMPTOM_FILE)
        root_cause_query = read_query(ROOT_CAUSE_FILE)
        sc_query = read_query(SUCCESS_CRITERIA_FILE)

        # Run queries
        edges = run_query(session, edge_query, {"sc_id": sc_id})
        for edge in edges:
            print("Edge:", edge)

        # Classify node IDs by type
        symptom_ids = sorted({edge["to_id"] for edge in edges if edge.get("to_id", "").startswith("rf-")})
        root_cause_ids = sorted({edge["to_id"] for edge in edges if edge.get("to_id", "").startswith("rc-")})
        success_criteria_ids = sorted({edge["to_id"] for edge in edges if edge.get("to_id", "").startswith("sc-")})

        # Debug output
        print("Symptom IDs:", symptom_ids)
        print("Root Cause IDs:", root_cause_ids)
        print("Success Criteria IDs:", success_criteria_ids)
        print("Running symptom query with IDs:", symptom_ids)
        print("Running root cause query with IDs:", root_cause_ids)
        print("Running SC query with ID:", sc_id)

        symptoms = run_query(session, symptom_query, {"symptom_ids": symptom_ids})

        root_causes = run_query(session, root_cause_query, {"rc_ids": root_cause_ids})

        sc_node = run_query(session, sc_query, {"sc_ids": [sc_id]})

        # Write outputs
        write_csv(os.path.join(OUTPUT_DIR, f"{sc_id}_edges.csv"), edges[0].keys() if edges else [], [r.values() for r in edges])
        write_csv(os.path.join(OUTPUT_DIR, f"{sc_id}_symptoms.csv"), symptoms[0].keys() if symptoms else [], [r.values() for r in symptoms])
        write_csv(os.path.join(OUTPUT_DIR, f"{sc_id}_root_causes.csv"), root_causes[0].keys() if root_causes else [], [r.values() for r in root_causes])
        write_csv(os.path.join(OUTPUT_DIR, f"{sc_id}_success_criteria.csv"), sc_node[0].keys() if sc_node else [], [r.values() for r in sc_node])

    driver.close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Extract backcasting data by Success Criteria ID")
    parser.add_argument("sc_id", help="Success Criteria ID (e.g., sc-001)")
    args = parser.parse_args()
    extract_data(args.sc_id)