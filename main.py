input_file = "Data.xml"
output_file = "OUT.yaml"
def get_rows_of_data():
    with open(input_file, encoding="utf-16") as f:
        data = f.read()
    return data.split("\n")

def double_teg(row,spaces):
    teg_name = row[row.find("<")+1:row.find(" ")]
    row_between_tegs= row[row.find(">")+1:row.rfind("<")].strip()
    row_with_ravno = row[row.find(" ")+1:row.find(">")]
    print(row_between_tegs,row_with_ravno)
    return convert_sms(row_with_ravno, spaces, teg_name, row_between_tegs)

def solo_teg(row,spaces):
    teg_name = row[row.find("<")+1:row.find(" ")]
    row = row[row.find(" ")+1:row.find("/")].strip()
    return convert_sms(row,spaces,teg_name)

def double_no_last_teg(row,spaces):
    teg_name = row[row.find("<") + 1:row.find(" ")]
    row_between_tegs = row[row.find(">") + 1:].strip()
    row_with_ravno = row[row.find(" ") + 1:row.find(">")]
    print(row_between_tegs, row_with_ravno)
    return convert_sms(row_with_ravno, spaces, teg_name, row_between_tegs)

def solo_no_last_teg(row,spaces):
    teg_name = row[row.find("<") + 1:row.find(" ")]
    row = row[row.find(" ") + 1:].strip()
    return convert_sms(row,spaces,teg_name)

def convert_sms(row, spaces, teg_name = "", dop_param = "", flag = True):
    li, tegli = [], []
    if dop_param:
        tegli.append(" "*spaces+teg_name+": "+dop_param)
        teg_name = ""
    first_flag = " -" if flag else "  "
    if teg_name:
        tegli.append(" "*spaces+teg_name+":")
    cnt = 0
    subrow = ""
    for i in row:
        subrow+=i
        if i == '"':
            cnt+=1
        if cnt == 2:
            li.append(" "*(spaces+2) + first_flag + " " +subrow)
            first_flag = " "
            cnt, subrow = 0, ""
    return tegli, li

def parse_row(row:str, result, spaces):
    if row.startswith("<?xml") or not row or ("</" in row and row.count(">") == 1):
        return result, spaces
    else:
        last_spaces = spaces
        spaces = len(row) - len(row.lstrip())
        row = row.strip()
        if row.startswith("<") and not row.startswith("</"):
            li, tegli = [], []
            if result == []:
                row = row.strip()
                row = (" "*4 +row[row.find(" ")+1:-1]).replace("=", ":")
                result.append(row)
            elif row.count(">") == 2:
                tegli, li = double_teg(row,spaces)
            elif row.endswith("/>"):
                tegli, li = solo_teg(row,spaces)
            elif row.count(">") == 0:
                tegli, li = solo_no_last_teg(row,spaces)
            else:
                tegli, li = double_no_last_teg(row,spaces)
            for i in tegli:
                if i not in result:
                    result.append(i)
            result += li
        else:
            spaces = last_spaces
            row = row[:row.index("/")].strip() if "<" not in row else row[:row.index("<")].strip()
            tegli, li = convert_sms(row,spaces,flag = False)
            for i in tegli:
                if i not in result:
                    result.append(i)
            result += li
    return result, spaces

def parse(data):
    result = []
    spaces = 0
    for row in data:
        result, spaces = parse_row(row,result,spaces)
    with open(output_file, "w",encoding="utf-16") as f:
        f.write("\n".join(result))

def main():
    data = get_rows_of_data()
    parse(data)

if __name__ == "__main__":
    main()