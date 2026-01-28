from json_data import DataTypes


def conver_to_markdown(data_object):
    markdown = ""
    
    if data_object.data_type in [DataTypes.ARRAY_OBJECTS, DataTypes.OBJECT]:
        pass

    if data_object.children:
        pass