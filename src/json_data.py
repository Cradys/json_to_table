from enum import Enum

class DataTypes(Enum):
    STR = "string"
    INT = "int"
    FLOAT = "float"
    BOOL = "bool"
    ARRAY = "array"
    ARRAY_OBJECTS = "ArrayOfObjects"
    ARRAY_VALUES = "array of values"
    OBJECT = "Object"
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
children: {len(self.children)}
{"-"*20}"""
    

class ParentObject(JSONData):
    def __init__(self, name, data_type, example=None, children=None):
        super().__init__(name, data_type, None, children)

    def find_child_by_name(self, value):
        for child in self.children:
            if child.name == value:
                return child
        return None

    def __eq__(self, value):
        if self.name == value.name and self.children == value.children:
            return True
        
        return False

    def __repr__(self):
        return f"ParentObject {self.name} {self.data_type}:\n->{self.children}<-"
    

class DataObject(JSONData):
    def __init__(self, name, data_type, example=None, children=None):
        super().__init__(name, data_type, example, None)

    def __eq__(self, value):
        if self.name == value.name:
            return True
        return False

    def __repr__(self):
        return f"Field: {self.name}"