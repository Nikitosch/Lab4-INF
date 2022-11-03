from xmlutils.xml2csv import xml2csv
input_file = "Data.xml"
output_file ="OUTCSV"
converter = xml2csv(input_file, output_file, encoding="utf-16")
converter.convert(tag="item")
print(1)