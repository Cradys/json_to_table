from enum import Enum

class DataTypes(Enum):
    STR = "string"
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    ARRAY = "array"
    ARRAY_OBJECTS = "array_objects"
    ARRAY_VALUE = "array_value"
    OBJECT = "object"
    NONE = "null"

class JSONData():
    def __init__(self, name, data_type, example=None, children=None):
        self.name = name
        self.data_type = data_type
        self.example = example
        self.children = children
    
    def __repr__(self):
        return f"""
{"-"*5}ParentObject{"-"*5}
Key name: {self.name}
data_type: {self.data_type}
example: {self.example}
children: {self.children}
{"-"*20}"""
    

class ParentObject(JSONData):
    def __init__(self, name, data_type, example=None, children=None):
        super().__init__(name, data_type, None, children)

    def __repr__(self):
        return f"\nParentObject {self.name} {self.data_type} - {self.children}"

class DataObject(JSONData):
    def __init__(self, name, data_type, example=None, children=None):
        super().__init__(name, data_type, example, None)

    def __repr__(self):
        return f"Field: {self.name}"