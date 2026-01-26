from enum import Enum

class DataTypes(Enum):
    STR = "string"
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    ARRAY = "array"
    OBJECT = "object"
    NONE = "null"

class JSONData():
    def __init__(self, name, data_type, example=None, children=None):
        self.name = name
        self.data_type = data_type
        self.example = example
        self.children = children
    
    def __repr__(self):
        return f"JSONData: {self.name}\ndata_type: {self.data_type}\nexample: {self.example}\nchildren: {self.children}\n{"-"*20}\n"