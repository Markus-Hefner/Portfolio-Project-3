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

def get_index():
    """
    Gets the index worksheet
    """
    return SHEET.worksheet('Index')

# index = SHEET.worksheet('Index')

def get_all_index_data():
    """
    Gets all data in the index worksheet
    """
    index = get_index()
    return index.get_all_values()

# index_data = index.get_all_values()

# due_dates = [col[5] for col in index_data if col[5] != "Timestamp"]

def add_new_piece():
    """
    Adds a new piece to spreadsheet
    """
    while True:
        print("Please enter the title of the new piece you wish to add.\nPress 'Enter' to confirm.\n(You can not use \"title\" or \"Title\".)")
        title = input("Title:\n")

        # Check if the title already exists in the spreadsheet
        existing_titles = [col[1].lower() for col in get_all_index_data() if col[1].lower() != "title"]
        print(f'Here are all existing titles: {existing_titles}') # check statement

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
    
    main_menu()

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
    print(get_index().col_values(1))
    index_number = get_index().col_values(1)
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

def add_piece_to_index(new_piece):
    """
    Adds a new piece to the index
    """
    get_index().append_row(new_piece)

def add_new_worksheet(new_piece):
    """
    Adds a new worksheet with the name of the piece to the spreadsheet for later use
    """
    new_worksheet = SHEET.add_worksheet(title = new_piece[1], rows="1", cols="10")
    new_worksheet.append_row(new_piece)
    
    #   print(f"Successfully created a new worksheet for {data[1]}")

def main_menu():
    """
    The user decides whether to practice, add a new piece or show repertoire
    """
    print("What would you like to do?")
    print("Type 'p' and press 'Enter' if you want to start practicing.")
    print("Type 'a' and press 'Enter' if you want to add a new piece.")
    print("Type 'r' and press 'Enter' if you want to see your repertoire.")
    print("Type 'x' and press 'Enter' if you want to exit the programme.\n")

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
    elif user_decision.lower() == "x":
        exit_programme()
    else:
        print('\nPlease enter correct value.\n')
        main_menu()

def show_repertoire():
    """
    Shows repetoire of pieces
    """
    print("Your repetoire:\n")
    for i in get_all_index_data():
        print(f'Index: {i[0]}\nTitle: {i[1]}\nComposer: {i[2]}\nArranger: {i[3]}\nAdditional Info: {i[4]}\n')
    
    main_menu()

def pick_a_piece():
    """
    Picks a piece from the index
    """
    due_pieces = create_due_list(get_all_index_data())
    print(due_pieces) # check print statement
    sorted_due_pieces = sort_by_timestamp(due_pieces)
    print(sorted_due_pieces) # check print statement
    # Here a loop has to start to iterate through the pieces. Before there should be the question if the user wants to proceed or go back to the main menu.
    sorted_due_pieces_len = len(sorted_due_pieces)
    print(sorted_due_pieces_len) # check print statement
    iterables_list = create_iterables_list(sorted_due_pieces_len)

    for i in iterables_list:
        a, b, c, d, e, f, g = sorted_due_pieces[i] # this needs to be looped later (if the user is done practicing the piece the loop has to get to the next item)
        i += 1
        current_piece = PracticePiece(a, b, c, d, e, f, g)
        print(current_piece.due_date) # check print statement

        print(f'The next piece to practice is {current_piece.title}.')
        print('Would like to practice that now? If not, we will move on to the next piece.')
        answer = yes_no_validation()
        if answer == True:
            practice_piece(current_piece)
        else:
            print('Alright, let\'s move on to the next piece.')
    
    print('Congratulations, you got through all the material today')
    print('Hope to see you tomorrow again :-)')
    
    main_menu()

def create_iterables_list(sorted_due_pieces_len):
    """
    Creates a list of integers to loop over in order to create as many classes
    of pieces to practice as there are lists (representing the pieces) in the
    sorted_due_pieces list since indices cannot be lists
    """
    item = 0
    iterables_list = []
    while item < sorted_due_pieces_len:
        iterables_list.append(item)
        item += 1
    print(iterables_list)
    return iterables_list

def practice_piece(current_piece):
    """
    Asks the user to play the piece and then assess the result.
    Depending on the user's answer and the data retrieved from the spreadsheet
    the function then updates the due date and the count.
    If the next due date is less then two days in the future the function asks
    if the user wants to practice again.
    """
    while True:
        print('\nGreat let\'s go!')
        print(f'Play {current_piece.title} and let us now how it went.\n')
        print('How did it go?')
        answer = three_options_validation()

        new_due_date = update_due_date_and_count(current_piece.due_date, current_piece.count, answer)[0]
        print(f'The new due date is {new_due_date}') # check print statement

        new_count = update_due_date_and_count(current_piece.due_date, current_piece.count, answer)[1]
        print(f'The new count is {new_count}') # check print statement

        current_piece.due_date = new_due_date
        current_piece.count = new_count

        days_difference = check_due_date(new_due_date)
        print(days_difference) # check print statement

        if days_difference <= 0:
            print('Due date updated. Would you like to go again?')
            answer_2 = yes_no_validation()
            if answer_2 == True:
                continue
            else:
                update_index(current_piece)
                print('Alright, let\'s move on to the next piece.')
                break
                # from here it goes back to the loop in pick_a_piece
        if days_difference == 1:
            print(f'The next due date for the piece would be {new_due_date}.')
            print('Would you like to practice it again anyway?')
            answer_3 = yes_no_validation()
            if answer_3 == True:
                continue
            else:
                update_index(current_piece)
                break
        else:
            print(f'Great! The piece won\'t be due for another {days_difference} days.')
            update_index(current_piece)
            print('Let\'s move on to the next piece.')
            break

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
            return 0
        else:
            print("\nInvalid input.\n")

def update_due_date_and_count(due_date, count, answer):
    """
    Updates due date using the count value and a factor depending on the answer variable.
    If 2 is passed as the answer variable, the due date is updated to the current date plus the new count value.
    If 1 or 0 is passed as the answer variable, the due date is updated to the old due date plus the new count value.
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
    # Update count on spreadsheet!!!
    return (convert_date_to_string(new_due_date), new_count)

def check_due_date(new_due_date):
    """
    Checks if the new due date is in the future
    """
    # if convert_string_to_date(new_due_date) > datetime.datetime.now().date():
    #     days_difference = (convert_string_to_date(new_due_date) - datetime.datetime.now().date()).days
    #     print(f'Great its {days_difference} days in the future') # check print statement
    #     return days_difference
    # else:
    #     return 0
    return (convert_string_to_date(new_due_date) - datetime.datetime.now().date()).days
    

def create_due_list(all_index_data):
    """
    Removes the list item with the headings in it (which is also a list).
    Removes list items of which the timestamp is > today.
    """
    print(f'here is all index data: {all_index_data}') # check statement
    all_index_data.pop(0)
    due_list = [col for col in all_index_data if convert_string_to_date(col[5]) <= datetime.datetime.now().date()]
    print(f'here is the due_list: {due_list}') # check statement
    return due_list

def sort_by_timestamp(due_pieces):
    """
    Sorts the from the google sheet retrieved list of lists by last practiced
    """
    # sorted_due_list = convert_string_to_date(data[5]) <= datetime.datetime.now().date()
    # print(i)
    # print(i[5])
    # print(type(i[5]))
    return sorted(due_pieces, key = lambda e: e[5])

def exit_programme():
    """
    Exits the programm
    """
    print("\nSee you soon :-)")

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
    
def update_index(current_piece):
    """
    Updates the due date and the count of the current piece
    """
    get_index().update_cell(int(current_piece.index) + 1, 6, current_piece.due_date)
    get_index().update_cell(int(current_piece.index) + 1, 7, current_piece.count)

main_menu()