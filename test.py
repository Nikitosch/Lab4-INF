from re import *
test = '<schedule time = "8:20 - 9:50" week = "5" subject = "ИНФОРМАТИКА(ЛЕК):ZOOM" lecturer = "Балакшин Павел Валерьевич" format = "Дистанционный"/>'
teg_name = search("(?<=<).*(?=\s)",test)[0] #row[row.find("<")+1:row.find(" ")]
row = search("(?<=\s).*(?=/)",test)[0] #row[row.find(" ")+1:row.find("/")].strip()
print(type(row),row,teg_name)