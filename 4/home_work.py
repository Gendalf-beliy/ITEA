import datetime
import pickle
import re
import xlrd
from xlrd.sheet import ctype_text


class ValidationError(BaseException):
    pass


class DateValidationError(ValidationError):
    pass


class EmailValidationError(ValidationError):
    pass


class UsernameValidationError(ValidationError):
    pass


class FileConverter:
    pass


def our_to_usa(date):
    return date


def error_data(raw, path='errors.log'):
    with open(path, 'a') as file:
        file.write(raw)
    return 'raw added to error.log'


fname = 'itea.xlsx'

# Open the workbook
xl_workbook = xlrd.open_workbook(fname)
xl_sheet = xl_workbook.sheet_by_index(0)
print('Sheet name: %s' % xl_sheet.name)

# Pull the first row by index (rows/columns are also zero-indexed)
row = xl_sheet.row(0)  # 1st row

# Print 1st row values and types
print('(Column #) type:value')
for idx, cell_obj in enumerate(row):
    cell_type_str = ctype_text.get(cell_obj.ctype, 'unknown type')
    print('(%s) %s %s' % (idx, cell_type_str, cell_obj.value))

# Print all values, iterating through rows and columns
num_cols = xl_sheet.ncols   # Number of columns
for row_idx in range(0, xl_sheet.nrows):    # Iterate through rows
    print ('-'*40)
    print ('Row: %s' % row_idx)   # Print row number
    for col_idx in range(0, num_cols):  # Iterate through columns
        cell_obj = xl_sheet.cell(row_idx, col_idx)  # Get cell object by row, col
        print('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))