import sys
import os
from files import extract_source_file_data
from json_to_objects import json_data_to_objects

JSON_SOURCE_DIR = "./jsons"
CONVERTED_TABLE_DIR = "./converted_tables"


def main():
    source_file = os.path.join(JSON_SOURCE_DIR, sys.argv[1])
    
    if not os.path.exists(CONVERTED_TABLE_DIR):
        os.mkdir(CONVERTED_TABLE_DIR)    

    json_data = extract_source_file_data(source_file)
    data_object = json_data_to_objects(json_data, "Root")
    print(data_object)


if __name__ == "__main__":
    main()