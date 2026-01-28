from json_data import DataTypes


def conver_to_markdown(data_object):
    markdown = ""
    
    if data_object.data_type in [DataTypes.ARRAY_OBJECTS, DataTypes.OBJECT]:
        markdown += create_headers(data_object)

    if data_object.children:
        for child in data_object.children:
            markdown += create_content_table(child)


def create_headers(data_object):
    header_markdown = ""

    header_markdown += f"#### {data_object.name.capitalize()}{data_object.data_type.value}\n\n"
    header_markdown += f"| Name | Data type | Example |\n"
    header_markdown += f"| --- | --- | --- |\n"
    return header_markdown


def create_content_table(data_object):
    header_markdown = ""
    print(data_object.name)
    return data_object.name

