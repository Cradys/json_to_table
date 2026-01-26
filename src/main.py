import sys
import os
from files import extract_source_file_data
from json_data import DataTypes, JSONData

JSON_SOURCE_DIR = "./jsons"
CONVERTED_TABLE_DIR = "./converted_tables"

def main():
    source_file = os.path.join(JSON_SOURCE_DIR, sys.argv[1])
    
    if not os.path.exists(CONVERTED_TABLE_DIR):
        os.mkdir(CONVERTED_TABLE_DIR)    

    json_data = extract_source_file_data(source_file)
    print(json_data_to_objects(json_data))

    # if isinstance(json_data, list):
    #     print(f"dict_data variable is list")
    # elif isinstance(json_data, dict):
    #     for value in json_data.values():
    #         print(f"Value {value}\nType {type(value)}\n{"-"*20}")
    # else:
    #     raise Exception("Unkown data type of json_data variable")

def json_data_to_objects(json_data):
    fields_list = []
    
    if isinstance(json_data, dict):
        for value in json_data.keys():
            match json_data[value]:
                case list():
                    print("list")
                case dict():
                    print("dict")
                case str():
                    fields_list.append(JSONData(name=value, data_type=DataTypes.STR, example=json_data[value]))
                case int():
                    fields_list.append(JSONData(name=value, data_type=DataTypes.INT, example=json_data[value]))
                case bool():
                    fields_list.append(JSONData(name=value, data_type=DataTypes.BOOL, example=json_data[value]))
                case float():
                    fields_list.append(JSONData(name=value, data_type=DataTypes.FLOAT, example=json_data[value]))
                case _:
                    fields_list.append(JSONData(name=value, data_type=DataTypes.NONE, example=json_data[value]))
                    
                    
                    
            # if isinstance(json_data[value], list) or isinstance(json_data[value], dict):
            #     print(f"{value}\n{"-"*20}")
            #     json_data_to_objects(json_data[value])
    if isinstance(json_data, list):
        print(f"{type(json_data)}\n{json_data}\n{"-"*20}")
    
    return(fields_list)

if __name__ == "__main__":
    main()