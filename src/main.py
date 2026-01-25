import sys
import os
from files import extract_source_file_data

JSON_SOURCE_DIR = "./jsons"
CONVERTED_TABLE_DIR = "./converted_tables"

def main():
    source_file = os.path.join(JSON_SOURCE_DIR, sys.argv[1])
    
    if not os.path.exists(CONVERTED_TABLE_DIR):
        os.mkdir(CONVERTED_TABLE_DIR)    

    dict_data = extract_source_file_data(source_file)

    if isinstance(dict_data, list):
        print(f"dict_data variable is list")
    elif isinstance(dict_data, dict):
        for value in dict_data.values():
            print(f"Value {value}\nType {type(value)}\n{"-"*20}")
    else:
        raise Exception("Unkown data type of dict_data variable")

if __name__ == "__main__":
    main()