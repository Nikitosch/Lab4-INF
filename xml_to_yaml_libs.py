import xml_parser as parser
input_file = "DataForLib.xml"
output_file = "OUT.yaml"
def main():
    with  open(input_file, 'r', encoding='utf-16') as in_,\
        open(output_file, 'w+', encoding='utf-16') as out:
        a = parser.parse(in_)
        parser.to_yaml(a, out)
main()
