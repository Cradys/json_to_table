from json_data import DataTypes, JSONData, ParentObject, DataObject

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
    merged_obj = fields_list[0]

    for i in range(1, len(fields_list)):
        if merged_obj == fields_list[i]:
            continue
        for value in fields_list[i].children:
            if value not in merged_obj.children:
                if value.data_type is DataTypes.ARRAY_OBJECTS:
                    merge_ch = merged_obj.find_child_by_name(value.name)
                    merge_array_of_objects([merge_ch.children, value.children])
                    continue
                merged_obj.children.append(value)
                
    return merged_obj
                