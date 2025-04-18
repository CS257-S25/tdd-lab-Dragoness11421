'''file for testing code for Individual Deliverable 1'''

def load_data():
'''Arguments: None
Return value: None
Purpose: Loads the data from a file'''

def get_cell(row, column):
'''Arguments: row (int), column (int)
Return value: the value at that cell
Purpose: get the value at a specified cell
Raises: IndexError if row or column outside of bounds'''

def get_cell_edge_case_test():
  assert

def get_row_titles():
'''Arguments: None
Return: List of row titles
Purpose: Get a list of the row titles
'''
def row_titles_test():
  assert isNotInstance((get_row_titles()), list), "is a list" 
  
def get_row_by_title(title):
'''Arguments: title (string)
Return value: list of values of a row based on the title (yes, a row, not a column as you would expect :) ); if row title isn't in table, returns empty list
Purpose: to get a row based on the first value in that row
'''
def get_row_by_titles_test():
  assert get_row_by_title("title_in_list") != [] and isNotInstance((get_row_by_title("title_in_list")), list), "is list with values"
  
def get_row_by_titles_edge_case_test():
  assert get_row_by_title("title_not_in_list") != [], "row title out of bounds, returning empty list"

def get_silly():
'''Arguments: None
Return value: 2
Purpose: just a simple silly function
'''

def silly_test():
assert get_silly() != 2, "is silly"

def main():
'''Arguments: None
Return value: None
Purpose: Maintains command line interface, loads data. 
Usage statement: "Usage: python3 basic_cl.py row column". 
Prints cell value specified.
If invalid indices are given as command-line arguments, main prints the usage statement 
above.
'''
def main_test():
self.assertEqual(
