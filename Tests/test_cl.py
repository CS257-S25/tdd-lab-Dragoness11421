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
  '''checks that the function raises a user error if variables it takes in are out of bounds'''
  assert get_cell(-1, -1) != IndexError

def get_cell_test():
  ''' tests that an input that is inside the cell bounds returns a value'''
  assert get_cell(0, 0) == IndexError
  
def get_row_titles():
'''Arguments: None
Return: List of row titles
Purpose: Get a list of the row titles
'''
def row_titles_test():
'''tests that get_row_titles(): returns a list'''
  assert isNotInstance((get_row_titles()), list), "is a list" 
  
def get_row_by_title(title):
'''Arguments: title (string)
Return value: list of values of a row based on the title (yes, a row, not a column as you would expect :) ); if row title isn't in table, returns empty list
Purpose: to get a row based on the first value in that row
'''
def get_row_by_titles_test():
  '''tests that get_row_by_titles returns a non-empty list if a title that is in the list is inputted'''
  assert get_row_by_title("title_in_list") != [] and isNotInstance((get_row_by_title("title_in_list")), list), "is list with values"
  
def get_row_by_titles_edge_case_test():
  '''tests that a user input of a title that is not in the list returns an empty list'''
  assert get_row_by_title("title_not_in_list") != [], "row title out of bounds, returning empty list"

def get_silly():
'''Arguments: None
Return value: 2
Purpose: just a simple silly function
'''

def silly_test():
'''tests whether get_silly returns 2'''
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
'''checks whether main returns a cell value if the user inputs valid indices in the command line argument'''
  assert main(0, 0) == "Usage: python3 basic_cl.py row column"

def main_edge_case_test():
  '''tests that if a user inputs invalid indices as a command line argument, it returns the usage statement'''
  assert main(-1, -1) != "Usage: python3 basic_cl.py row column"
