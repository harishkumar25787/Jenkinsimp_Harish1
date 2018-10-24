import xlrd

def getexceldata1(filename):
    rows = []
    # open the specified Excel spreadsheet as workbook
    book = xlrd.open_workbook(filename)
    # get the first sheet
    sheet = book.sheet_by_index(0)
    x = 1
    y = 1
    rows = []

    while (x <= sheet.nrows):
        rows.append(list(sheet.row_values(x, 0, sheet.ncols)))

    print(rows)
    return rows