import openpyxl

class ExcelUtility:

    def __init__(self, location, sheet_name):
        self.wb = openpyxl.load_workbook(location)
        self.sheet = self.wb[sheet_name]

    def readDataByIndex(self, row, column):
        return self.sheet.cell(row, column).value