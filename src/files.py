import os
import json
from pathlib import Path

def extract_source_file_data(source_file):
    if not os.path.isfile(source_file):
        source_file = Path(source_file).with_suffix(".json")
        if not os.path.isfile(source_file):
            raise Exception(f"File not found by path: {source_file}")
    
    file_data = open(source_file).read()
    
    if not file_data:
        raise Exception(f"Source file is empty: {source_file}")
    
    try:
        dict_data = json.loads(file_data)
    except Exception:
        raise Exception(f"Something wront with json format in the file")
    
    return dict_data
    
