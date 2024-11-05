# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('it_is_practice_time')

index = SHEET.worksheet('Index')

data = index.get_all_values()

def add_new_piece():
    """
    Adds a new piece to spreadsheet
    """
    while True:
        print("Please enter the title of the new piece you wish to add.\n Confirm with 'Enter'.")

        title = input("Title:\n")

        print("Please enter the composer of the new piece you wish to add. (Optional)\n Confirm with 'Enter'.")

        composer = input("Composer:\n")

        print("Please enter the arranger of the new piece you wish to add. (Optional)\n Confirm with 'Enter'.")

        arranger = input("Arranger:\n")

        print("Please enter additional information of the new piece you wish to add. (Optional)\n Confirm with 'Enter'.")

        additional_info = input("Additional information:\n")

        break




    new_piece = [title, composer, arranger, additional_info]
    index.append_row(new_piece)

add_new_piece()

def add_new_worksheet(name):
    """
    Adds a new worksheet to the spreadsheet
    """
    SHEET.add_worksheet(title=name, rows="100", cols="20")





