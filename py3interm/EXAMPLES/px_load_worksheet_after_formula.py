#!/usr/bin/env python
import openpyxl as px
print(px.__version__)  # should be >= 2.2 or this code will not work

def main():
    wb = px.load_workbook('presidents2.xlsx')

# three ways to get to a worksheet:

    # 1
    print(wb.get_sheet_names(), '\n')
    ws = wb.get_sheet_by_name('US Presidents')
    # or
    ws = wb['US Presidents']
    print(ws, '\n')

    # 2
    for ws in wb:
        print(ws)
    print()

    # 3
    ws = wb.active
    print(ws, '\n')

    for row in ws["A2:K46"]:
        print([c.value for c in row])

if __name__ == '__main__':
    main()
