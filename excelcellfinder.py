import openpyxl

# Load the Excel workbook
workbookfile = input("Enter the path of your file: ")
workbook = openpyxl.load_workbook(workbookfile)

# Select the active sheet
sheet = workbook.active

# Get the value of a specific cell
cell = input("Enter the cell number: ")
cell_value = sheet[cell].value

print(cell_value)

