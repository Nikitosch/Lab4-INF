import xmlplain
input_file = "Data.xml"
output_file = "OUT.yaml"
def main():
    with open(input_file, "r", encoding="utf-16") as xml_file,\
        open(output_file, "w", encoding="utf-16") as yaml_file:
        obj = xmlplain.xml_to_obj(xml_file,)
        xmlplain.obj_to_yaml(obj,yaml_file)
main()
