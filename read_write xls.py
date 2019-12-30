# read xls file

import xlrd

book = xlrd.open_workbook("file_name.xls")

print(book.nsheets)
print(book.sheet_names())

first_sheet = book.sheet_by_index(0)
print(first_sheet.row_values(0))

cell = first_sheet.cell(3, 1)
print(cell)


# write xls file

import xlwt

workbook = xlwt.workbook(encoding="utf-8")
sheet1 = book.add_sheet("sheet_name1")
sheet2 = book.add_sheet("sheet_name2")
sheet3 = book.add_sheet("sheet_name3")

sheet1.write(0, 0, 'Sheet 1')  # 'Sheet 1' - write some value to cell
sheet2.write(5, 0, 'Sheet 2')  # 5 - row
sheet3.write(0, 10, 'Sheet 3')  # 10 - column

workbook.save("file_name.xls")
