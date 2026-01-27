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
                    return ParentObject(name=name, data_type=DataTypes.ARRAY_VALUES, children=fields_list)
                
            merged_fields = merge_array_of_objects(fields_list)
            return ParentObject(name=name, data_type=DataTypes.ARRAY_OBJECTS, children=merged_fields)
        
        return DataObject(name=name, data_type=DataTypes.ARRAY, example=json_data[:3:])
    
def merge_array_of_objects(fields_list):
    print(fields_list)
    merged_obj = fields_list[0]
    print(f"merged_obj - {merged_obj}\n --------")

    for i in range(1, len(fields_list)):
        print(fields_list[i])
        if merged_obj == fields_list[i]:
            print("equal")
            print(merged_obj.data_type)
            print(fields_list[i].data_type)
            print(f"{"#"*10}\n{merged_obj.children}\n---{fields_list[i].children}\n{"#"*10}")
            continue
            if merged_obj.data_type is DataTypes.ARRAY_OBJECTS:
                print(f"{"@"*10}\nARRAY_OBJECTS\n{fields_list[i]}\n{"@"*10}")
                merge_array_of_objects(fields_list[i])
        
        for value in fields_list[i].children:
            print(f"{value.data_type} {value.name}")
            if value not in merged_obj.children:
                if value.data_type is DataTypes.ARRAY_OBJECTS:
                    merge_array_of_objects(value)
                merged_obj.children.append(value)
                continue
    
    print(f"{"-"*10}\nMERGERD\n{merged_obj}\n{"-"*10}")
    return merged_obj
                

    
    # merged_list = []

    # for field in fields_list:
    #     if not merged_list:
    #         merged_list = field.children
    #         continue
    #     for child in field.children:
    #         if child not in merged_list:
    #             merged_list.append(child)
        
    #return merged_list

if __name__ == "__main__":
    main()