# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials
import datetime
import math

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

due_dates = [col[5] for col in data if col[5] != "Timestamp"]

def add_new_piece():
    """
    Adds a new piece to spreadsheet
    """
    while True:
        print("Please enter the title of the new piece you wish to add.\nPress 'Enter' to confirm.\n(You can not use \"title\" or \"Title\".)")
        title = input("Title:\n")

        # Check if the title already exists in the spreadsheet
        existing_titles = [col[1].lower() for col in data if col[1].lower() != "title"]

        if title.lower() in existing_titles:
            print("\nThis piece already exists in your repertoire.")
            print("Please rename it or give the title additional information.")
            print(f'E.g.: "{title} (other Version)"\n')
            continue
        # Check if the title is empty
        elif title == "":
            print("Title cannot be empty.\n")
            continue
        else:
            pass

        print("\nPlease enter the composer of the new piece you wish to add. (Optional)\nPress 'Enter' to confirm.")
        composer = input("Composer:\n")
        print("\nPlease enter the arranger of the new piece you wish to add. (Optional)\nPress 'Enter' to confirm.")
        arranger = input("Arranger:\n")
        print("\nPlease enter additional information of the new piece you wish to add. (Optional)\nPress 'Enter' to confirm.")
        additional_info = input("Additional information:\n")

        print("\nPlease confirm the following details are correct:\n")
        print(f"Title: {title}")
        print(f"Composer: {composer}")
        print(f"Arranger: {arranger}")
        print(f"Additional information: {additional_info}\n")

        answer = yes_no_validation()
        print(answer)
        if answer == True:
            break
        else:
            print("\nPlease re-enter the details.\n")


    # while True:
    #     confirmation = input("Type 'y' for yes and press 'Enter'. Otherwise type 'n' for no and press 'Enter':\n")
    #     if confirmation.lower() == "y":
    #         print("\nNew piece has been added to your repertoire\n")
    #         break
    #     elif confirmation.lower() == "n":
    #         print("\nPlease re-enter the details.\n")
    #         add_new_piece()
    #     else:
    #         print("\nInvalid input.\n")

    new_piece = []
    index_number = get_index_number() + 1
    created_date = get_current_date()
    count = 1
    
    new_piece.append(index_number)
    new_piece.append(title)
    new_piece.append(composer)
    new_piece.append(arranger)
    new_piece.append(additional_info)
    new_piece.append(convert_date_to_string(created_date))
    new_piece.append(count)

    add_piece_to_index(new_piece)
    add_new_worksheet(new_piece)

    print("\nNew piece has been added to your repertoire\n")
    
    # practice_adding_or_index() (Comment in in final version. Commented out to not get into an endless loop while testing)

def yes_no_validation():
    """
    Validates the user's answer to be yes or no
    """
    while True:
        confirmation = input("Type 'y' for yes and press 'Enter'. Otherwise type 'n' for no and press 'Enter':\n")
        if confirmation.lower() == "y":
            return True
        elif confirmation.lower() == "n":
            return False
        else:
            print("\nInvalid input.\n")
        

# def search_piece():
#     """
#     Searches for a piece in the spreadsheet
#     """
#     print("Please enter the title of the piece you wish to search for.\nPress 'Enter' to confirm.")
#     search_title = input("Title:\n")
    

def get_index_number():
    """
    Gets the index number of the last piece in the index
    """
    print(index.col_values(1))
    index_number = index.col_values(1)
    print(index_number)
    if len(index_number) == 1:
        return 0
    else:
        return int(index_number[-1])

def get_current_date():
    """
    Returns current date in the Format "YYYY-MM-DD"
    """
    return datetime.datetime.now().date()

def convert_date_to_string(date):
    """
    Converts a date in the format "YYYY-MM-DD" to a string of the same format"
    """
    return date.strftime('%Y-%m-%d')

def convert_string_to_date(str_date):
    """
    Converts a date in a string datatype in the format "YYYY-MM-DD" to a date of the same format"
    """
    return datetime.datetime.strptime(str_date, '%Y-%m-%d').date()


now_as_str = convert_date_to_string(get_current_date())
print(now_as_str)
now_as_date_again = convert_string_to_date("2014-05-08")
print(now_as_date_again)

def add_piece_to_index(data):
    """
    Adds a new piece to the index
    """
    index.append_row(data)

def add_new_worksheet(data):
    """
    Adds a new worksheet with the name of the piece to the spreadsheet for later use
    """
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
        pick_a_piece()
    elif user_decision.lower() == "a":
        print('\nLet\'s add a new piece\n')
        add_new_piece()
    elif user_decision.lower() == "r":
        print('\nLet\'s check out your repertoire\n')
        show_repertoire()
    else:
        print('\nPlease enter correct value.\n')
        practice_adding_or_repertoire()

def show_repertoire():
    """
    Shows repetoire of pieces
    """
    print("Your repetoire:\n")
    for i in data:
        print(f'Index: {i[0]}\nTitle: {i[1]}\nComposer: {i[2]}\nArranger: {i[3]}\nAdditional Info: {i[4]}\n')
    
    # practice_adding_or_index() (Comment in in final version. Commented out to not get into an endless loop while testing)

def pick_a_piece():
    """
    Picks a piece from the index
    """
    due_pieces = create_due_list(data)
    print(due_pieces) # check print statement
    sorted_due_pieces = sort_by_timestamp(due_pieces)
    print(sorted_due_pieces) # check print statement
    a, b, c, d, e, f, g = sorted_due_pieces[0] # this needs to be looped later (if the user is done practicing the piece the loop has to get to the next item)

    current_piece = PracticePiece(a, b, c, d, e, f, g)
    print(current_piece.due_date) # check print statement

    print(f'The next piece to practice is {current_piece.title}.')
    print('Would like to practice that now? If not, we will move on to the next piece.')
    answer = yes_no_validation()
    if answer == True:
        practice_piece(current_piece)
    
    else:
        print('Alright, let\'s move on to the next piece.')

def practice_piece(current_piece):
    print('\nGreat let\'s go!')
    print(f'Play {current_piece.title} and let us now how it went.\n')
    print('How did it go?')
    answer = three_options_validation()
    if answer == 2:
        print('Great!')
        # [done] call function to update the due date. (Variable with stored due date is needed and variable with the current days to be added to the due date)
        new_due_date = update_due_date(current_piece.due_date, current_piece.count, answer)
        # [done] check if due date is in the future
        if check_due_date(new_due_date) = True:
            print(f'Congratulations! You can move on to the next piece :-)')
        # if yes print message that you can move on to the next piece and...
        # ... update the due date in the spreadsheet
        # if no ask user if they want to practice the piece again
        # if yes start again at 'Great let's go!'. Here a loop is needed until either the due date for the piece is in the future or the user doesn't want to practice the piece anymore. So...
        # if the user says no to practicing the piece again, update the spreadsheet and...
        # ... ask if they want to move on to the next piece or go back to the main menu.


def three_options_validation():
    """
    Validates the user input for three options (well, okay, bad)
    """
    print("Type 'w' and press 'Enter' if it went well. (at tempo, no errors)")
    print("Type 'o' and press 'Enter' if it went okay. (not at tempo or only a few errors)")
    print("Type 'b' and press 'Enter' if it went bad. (not at tempo and some errors)")
    while True:
        user_input = input()
        if user_input.lower() == "w":
            return 2
        elif user_input.lower() == "o":
            return 1
        elif user_input.lower() == "b":
            return o
        else:
            print("\nInvalid input.\n")

def update_due_date(due_date, count, answer):
    """
    Updates due date using the count value and a factor depending on the answer variable
    """
    if answer == 2:
        factor = 1.5
    elif answer == 1:
        factor = 1
    else:
        factor = 0.5
    new_count = math.ceil(int(count) * factor)
    print(new_count) # check print statement
    if answer == 2:
        new_due_date = datetime.datetime.now().date() + datetime.timedelta(days=new_count)
        print(new_due_date) # check print statement
    else:
        new_due_date = convert_string_to_date(due_date) + datetime.timedelta(days=new_count)
        print(new_due_date) # check print statement
    return convert_date_to_string(new_due_date)

def check_due_date(new_due_date):
    """
    Checks if the new due date is in the future
    """
    if convert_string_to_date(new_due_date) > datetime.datetime.now().date():
        return True
    else:
        return False
    

def create_due_list(data):
    """
    Removes the list item with the headings in it (which is also a list).
    Removes list items of which the timestamp is > today.
    """
    data.pop(0)
    due_list = [col for col in data if convert_string_to_date(col[5]) <= datetime.datetime.now().date()]
    return due_list

def sort_by_timestamp(data):
    """
    Sorts the from the google sheet retrieved list of lists by last practiced
    """
    # sorted_due_list = convert_string_to_date(data[5]) <= datetime.datetime.now().date()
    # print(i)
    # print(i[5])
    # print(type(i[5]))
    return sorted(data, key = lambda e: e[5])

class PracticePiece:
    """
    Class of the pieces to be practiced
    """
    def __init__(self, index, title, composer, arranger, additional_info, due_date, count):
        self.index = index
        self.title = title
        self.composer = composer
        self.arranger = arranger
        self.additional_info = additional_info
        self.due_date = due_date
        self.count = count
    


       


practice_adding_or_repertoire()







