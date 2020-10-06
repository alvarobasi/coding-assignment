import argparse
from database import Database
import json
from config import *

if __name__ == "__main__":
    # Construct the argument parser and parse the hyperparameters.
    ap = argparse.ArgumentParser()
    ap.add_argument("-b", "--build_path", type=str, help="Path to the graph_build.json file.",
                    default=GRAPH_BUILD_PATH)
    ap.add_argument("-e", "--graph_edits", default=GRAPH_EDITS_PATH,
                    help="Path to the graph_edits.json file")
    ap.add_argument("-ext", "--img_extract", default=IMG_EXTRACT_PATH,
                    help="Path to the img_extract.json file")

    args = vars(ap.parse_args())
    # Reading json strings from provided files «graph_build, graph_edits and img_extract»
    f = open(GRAPH_BUILD_PATH, "r")
    build_str = f.read()

    f = open(GRAPH_EDITS_PATH, "r")
    edits_str = f.read()

    f = open(IMG_EXTRACT_PATH, "r")
    extract_str = f.read()

    # Loading and storing its contents into variables.
    # Initial graph (List of tuples)
    build = json.loads(build_str)
    # Extract (dict)
    extract = json.loads(extract_str)
    # Graph edits (List of tuples)
    edits = json.loads(edits_str)

    status = {}
    if len(build) > 0:
        # Build graph
        db = Database(build[0][0])
        if len(build) > 1:
            db.add_nodes(build[1:])
        # Add extract
        db.add_extract(extract)
        # Graph edits
        db.add_nodes(edits)
        # Update status
        status = db.get_extract_status()

    print(status)

    # Storage of the results into a json object.
    y = json.dumps(status)

    # Save results into a file
    f = open("outputs/result.json", "w")
    f.write(y)
    f.close()
