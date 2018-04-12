#!/usr/bin/env python
import openpyxl as px

def main():
    """program entry point"""
    wb = px.load_workbook('../DATA/presidents.xlsx')
    ws = wb.get_sheet_by_name('US Presidents')

    update_sheet(ws)

    wb.save('presidents4.xlsx')

def update_sheet(ws):
    """Misc updates to styles and formats"""

    # freeze header row and column 1
    ws.freeze_panes = "C2"


if __name__ == '__main__':
    main()
