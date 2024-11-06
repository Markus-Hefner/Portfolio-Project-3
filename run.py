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
    new_piece = []
    index_number = get_index_number() + 1
    new_piece.append(index_number)

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
    #   print("Please confirm the following details are correct:\n")
    #   print(f"Title: {title}\n")
    #   print(f"Composer: {composer}\n")
    #   print(f"Arranger: {arranger}\n")
    #   print(f"Additional information: {additional_info}\n")

    #   confirm = input("Please confirm the details are correct. (Y/N)\n")
    #  if confirm.lower() == "y":
    #      break
    #  else:
    #      print("Please re-enter the details.\n")
    #      continue
    #   break

    new_piece.append(title)
    new_piece.append(composer)
    new_piece.append(arranger)
    new_piece.append(additional_info)

    add_piece_to_index(new_piece)
    add_new_worksheet(new_piece)

def get_index_number():
    """
    Gets the index number of the last piece in the index
    """
    print(index.col_values(1))
    index_number = index.col_values(1)
    return int(index_number[-1])

def add_piece_to_index(data):
    """
    Adds a new piece to the index
    """
    index.append_row(data)

def add_new_worksheet(data):
    """
    Adds a new worksheet with the name of the piece to the spreadsheet for later use
    """
    print(data)
    new_worksheet = SHEET.add_worksheet(title = data[1], rows="1", cols="10")
    new_worksheet.append_row(data)
    
    #   print(f"Successfully created a new worksheet for {data[1]}")

def practice_adding_or_repertoire():
    """
    The user decides whether to practice, add a new piece or show repertoire
    """
    print("What would you like to do?")
    print("Type 'p' and press 'Enter' if you want to start practicing.")
    print("Type 'a' and press 'Enter' if you want to add a new piece.")
    print("Type 'r' and press 'Enter' if you want to see your repertoire.\n")

    user_decision = input()

    if user_decision.lower() == "p":
        print('\nLet\'s pracitce!\n')
        start_practicing()
    elif user_decision.lower() == "a":
        print('\nLet\'s add a new piece\n')
        add_new_piece()
    elif user_decision.lower() == "r":
        print('\nLet\'s check out your repertoire\n')
        show_repertoire()
    else:
        print('\nPlease enter correct value.\n')
        practice_adding_or_index()

def show_repertoire():
    """
    Shows repetoire of pieces
    """
    print("Your repetoire:\n")
    for i in data:
        print(f'Index: {i[0]}\nTitle: {i[1]}\nComposer: {i[2]}\nArranger: {i[3]}\nAdditional Info: {i[4]}\n')
    
    # practice_adding_or_index() (Comment in in final version. Commented out to not get into an endless loop while testing)
        
        


practice_adding_or_index()







