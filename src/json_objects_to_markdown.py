from json_data import DataTypes


def conver_to_markdown(data_object):
    markdown = ""
    next_level = []
    
    if data_object.data_type in [DataTypes.ARRAY_OBJECTS, DataTypes.OBJECT]:
        markdown += create_headers(data_object)


    if data_object.children:
        for child in data_object.children:
            markdown += create_table_row(child)
            if child.data_type in [DataTypes.ARRAY_OBJECTS, DataTypes.OBJECT]:
                next_level.append(child)
        markdown += "\n"
        if next_level:
            for value in next_level:
                markdown += conver_to_markdown(value)
    
    return markdown


def create_headers(data_object):
    header_markdown = ""

    header_markdown += f"#### {data_object.name.capitalize()}{data_object.data_type.value}\n\n"
    header_markdown += f"| Name | Data type | Example |\n"
    header_markdown += f"| --- | --- | --- |\n"
    return header_markdown


def create_table_row(data_object):
    table_row = ""
    name = data_object.name
    data_type = data_object.data_type.value
    example = data_object.example


    table_row += f"| {name} "
    if data_object.data_type in [DataTypes.ARRAY_OBJECTS, DataTypes.OBJECT]:
        table_header = f"{name.capitalize()}{data_type}"
        table_row += f"| {data_type}\n [{table_header}](#{table_header.lower()}) "
    if data_object.data_type not in [DataTypes.ARRAY_OBJECTS, DataTypes.OBJECT]:
        table_row += f"| {data_type} "
    
    table_row += f"| {example} |\n"

    return table_row

