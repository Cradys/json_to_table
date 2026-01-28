import os
import json
from pathlib import Path

def extract_source_file_data(source_dir, file_name):
    source_file = os.path.join(source_dir, file_name)
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

def create_and_write(dest_dir, file_name, markdown):
    if Path(file_name).suffix:
        file_name = Path(file_name).stem

    dest_file = os.path.join(dest_dir, Path(file_name).with_suffix(".md"))

    file = open(dest_file, "w")
    file.write(markdown)
    file.close()

    return

