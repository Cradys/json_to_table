import sys
import os
from files import extract_source_file_data
from json_data import DataTypes, JSONData, ParentObject, DataObject

JSON_SOURCE_DIR = "./jsons"
CONVERTED_TABLE_DIR = "./converted_tables"

def main():
    source_file = os.path.join(JSON_SOURCE_DIR, sys.argv[1])
    
    if not os.path.exists(CONVERTED_TABLE_DIR):
        os.mkdir(CONVERTED_TABLE_DIR)    

    json_data = extract_source_file_data(source_file)
    print(json_data_to_objects(json_data, "Root"))

    # if isinstance(json_data, list):
    #     print(f"dict_data variable is list")
    # elif isinstance(json_data, dict):
    #     for value in json_data.values():
    #         print(f"Value {value}\nType {type(value)}\n{"-"*20}")
    # else:
    #     raise Exception("Unkown data type of json_data variable")

def json_data_to_objects(json_data, name=None):
    fields_list = []
    
    if isinstance(json_data, dict):
        for value in json_data.keys():
            match json_data[value]:
                case list():
                    fields_list.append(json_data_to_objects(json_data[value], value))
                    print(f"{"-"*20}\n{fields_list}\n{"-"*20}")
                case dict():
                    fields_list.append(json_data_to_objects(json_data[value], value))
                case str():
                    fields_list.append(DataObject(name=value, data_type=DataTypes.STR, example=json_data[value]))
                case int():
                    fields_list.append(DataObject(name=value, data_type=DataTypes.INT, example=json_data[value]))
                case bool():
                    fields_list.append(DataObject(name=value, data_type=DataTypes.BOOL, example=json_data[value]))
                case float():
                    fields_list.append(DataObject(name=value, data_type=DataTypes.FLOAT, example=json_data[value]))
                case _:
                    fields_list.append(DataObject(name=value, data_type=DataTypes.NONE, example=json_data[value]))

        parent = ParentObject(name=name, data_type=DataTypes.OBJECT, children=fields_list)   
        return parent   
                    
    if isinstance(json_data, list):
        if not json_data:
            return DataObject(name=name, data_type=DataTypes.ARRAY, example="[]")
        
        for value in json_data:
            if isinstance(value, dict):
                fields_list.append(json_data_to_objects(value))
        
        if fields_list:
            for value in fields_list:
                if value.data_type != DataTypes.OBJECT:
                    return ParentObject(name=name, data_type=DataTypes.ARRAY_VALUE, children=fields_list)
            return ParentObject(name=name, data_type=DataTypes.ARRAY_OBJECTS, children=fields_list)
        return DataObject(name=name, data_type=DataTypes.ARRAY, example=json_data[:3:])

if __name__ == "__main__":
    main()