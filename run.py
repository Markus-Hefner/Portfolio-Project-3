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

def add_new_worksheet(name):
    """
    Adds a new worksheet to the spreadsheet
    """
    SHEET.add_worksheet(title=name, rows="100", cols="20")



print(add_new_worksheet('All My Loving').get_all_values())

