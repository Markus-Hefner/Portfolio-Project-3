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

"""
=== Main menu section ===
This code would go in the run.py file
"""


def main_menu():
    """
    The user decides whether to practice, add a new piece or show repertoire
    """
    print("===========================")
    print("Welcome to the main menu!")
    print("What would you like to do?\n")
    print("Type 'r' and press 'Enter' if you want to see your repertoire.")
    print("Type 'a' and press 'Enter' if you want to add a new piece.")
    print("Type 'p' and press 'Enter' if you want to start practicing.")
    print("Type 'x' and press 'Enter' if you want to exit the programme.\n")

    user_decision = input("\n").strip()
    print("---------------------------")

    if user_decision.lower() == "r":
        print('\nLet\'s check out your repertoire\n')
        show_repertoire()
    elif user_decision.lower() == "a":
        print('\nLet\'s add a new piece\n')
        add_new_piece()
    elif user_decision.lower() == "p":
        print('\nLet\'s pracitce!\n')
        pick_a_piece()
    elif user_decision.lower() == "x":
        exit_programme()
    else:
        print('\nPlease enter correct value.\n')
        main_menu()


"""
=== Show Repertoire section ===
This code would go in the run.py file since it's so small
"""


def show_repertoire():
    """
    Shows repetoire of pieces
    """
    print("Your repetoire:\n")
    for i in get_all_index_data():
        print(f'Index: {i[0]}')
        print(f'Title: {i[1]}')
        print(f'Composer: {i[2]}')
        print(f'Arranger: {i[3]}')
        print(f'Additional Info: {i[4]}\n')

    main_menu()


"""
=== Exit section ===
This code would go in the run.py file since it's so small
"""


def exit_programme():
    """
    Exits the programm
    """
    print("\nSee you soon :-)")


"""
=== Add New Piece section ===
This code would go in a new file called piece.py
Calls of functions from that file would be adjusted accordingly
"""


def add_new_piece():
    """
    Adds a new piece to spreadsheet
    """
    while True:
        print("Please enter the title of the new piece you wish to add.")
        print("Press 'Enter' to confirm.")
        title = input("Title:\n").strip()

        # Check if the title already exists in the spreadsheet
        existing_titles = [col[1].lower() for col in get_all_index_data() if col[1].lower() != "title"]
        # print(f'Here are all existing titles: {existing_titles}')  # check

        if title.lower() in existing_titles:
            print("\nThis piece already exists in your repertoire.")
            print("Please choose another title or add additional information.")
            print(f'(E.g.: "{title} (other Version)")\n')
            continue
        # Check if the title is empty
        elif title == "":
            print("Title cannot be empty.\n")
            continue
        else:
            pass

        print("\nPlease enter the composer of the piece. (Optional)")
        print("Press 'Enter' to confirm.")
        composer = input("Composer:\n").strip()

        print("\nPlease enter the arranger of the piece. (Optional)")
        print("Press 'Enter' to confirm.")
        arranger = input("Arranger:\n").strip()

        print("\nPlease enter additional information. (Optional)")
        print("Press 'Enter' to confirm.")
        additional_info = input("Additional information:\n").strip()

        print("\nPlease confirm the following details are correct:\n")
        print(f"Title: {title}")
        print(f"Composer: {composer}")
        print(f"Arranger: {arranger}")
        print(f"Additional information: {additional_info}\n")

        answer = yes_no_validation()
        print(answer)
        if answer is True:
            break
        else:
            print("\nPlease re-enter the details.\n")

    new_piece = []
    index_number = get_index_number() + 1
    created_date = datetime.datetime.now().date()
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


def get_index_number():
    """
    Gets the index number of the last piece in the index
    """
    # print(get_index().col_values(1))   # check
    index_number = get_index().col_values(1)
    # print(index_number)  # check
    if len(index_number) == 1:
        return 0
    else:
        return int(index_number[-1])


def add_piece_to_index(new_piece):
    """
    Adds a new piece to the index
    """
    get_index().append_row(new_piece)


def add_new_worksheet(new_piece):
    """
    Adds a new worksheet with the name of the piece
    to the spreadsheet for later use
    """
    new_worksheet = SHEET.add_worksheet(title=new_piece[1], rows="1", cols="10")
    new_worksheet.append_row(new_piece)


"""
=== Practice section ===
This code would go in a new file called practice.py
Calls of functions from that file would be adjusted accordingly
"""


def pick_a_piece():
    """
    Picks a piece from the index
    """
    due_pieces = create_due_list(get_all_index_data())
    # print(due_pieces)  # check
    sorted_due_pieces = sort_by_timestamp(due_pieces)
    # print(sorted_due_pieces)  # check
    # Here should be the question if the user wants to proceed
    # or go back to the main menu.
    sorted_due_pieces_len = len(sorted_due_pieces)
    # print(sorted_due_pieces_len)  # check
    iterables_list = create_iterables_list(sorted_due_pieces_len)

    for i in iterables_list:
        a, b, c, d, e, f, g = sorted_due_pieces[i]
        i += 1
        current_piece = PracticePiece(a, b, c, d, e, f, g)
        # print(current_piece.due_date)  # check

        print(f'The next piece to practice is {current_piece.title}.\n')
        # print('Would you like to practice that now?')
        # print('If not, we will move on to the next piece.')
        user_decision = [
            ("p", "Type 'p' and press 'Enter' if you want to practice the piece now."),
            ("n", "Type 'n' and press 'Enter' if you want to move on to the next piece."),
            ("x", "Type 'x' and press 'Enter' if you want get back to the main menu.")
        ]
        answer = three_options_validation(user_decision)
        if answer == 2:
            practice_piece(current_piece)
        elif answer == 1:
            print('Alright, let\'s move on to the next piece.\n')
            continue
        else:
            break
        """
        answer = yes_no_validation()
        if answer is True:
            practice_piece(current_piece)
        else:
            print('Alright, let\'s move on to the next piece.\n')
        """

    print('Congratulations, you got through all the material today')
    print('Hope to see you tomorrow again :-)')

    main_menu()


def create_due_list(all_index_data):
    """
    Removes the list item with the headings in it (which is also a list).
    Removes list items of which the timestamp is > today.
    """
    # print(f'here is all index data: {all_index_data}')  # check
    all_index_data.pop(0)
    due_list = [col for col in all_index_data if convert_string_to_date(col[5]) <= datetime.datetime.now().date()]
    # Alternative version:
    # due_list = []
    # for col in all_index_data:
    #     if convert_string_to_date(col[5]) <= datetime.datetime.now().date():
    #         due_list.append(col)

    # print(f'here is the due_list: {due_list}')  # check
    return due_list


def sort_by_timestamp(due_pieces):
    """
    Sorts the from the google sheet retrieved list of lists by last practiced
    """
    return sorted(due_pieces, key=lambda e: e[5])


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
    # print(iterables_list)  # check
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
        assessment_options = [
            ("w", "Type 'w' and press 'Enter' if it went well. (At tempo, no errors)"),
            ("o", "Type 'o' and press 'Enter' if it went okay. (Not at tempo or only a few errors)"),
            ("b", "Type 'b' and press 'Enter' if it went bad. (Not at tempo and some errors)")
        ]
        answer = three_options_validation(assessment_options)

        new_due_date = update_due_date_and_count(current_piece, answer)[0]
        # print(f'The new due date is {new_due_date}')  # check

        new_count = update_due_date_and_count(current_piece, answer)[1]
        # print(f'The new count is {new_count}')  # check

        current_piece.due_date = new_due_date
        current_piece.count = new_count

        days_diff = check_due_date(new_due_date)
        # print(days_diff)  # check

        if days_diff <= 0:
            print('Due date updated. Would you like to go again?')
            answer_2 = yes_no_validation()
            if answer_2 is True:
                continue
            else:
                update_index(current_piece)
                print('Alright, let\'s move on to the next piece.\n')
                break
                # from here it goes back to the loop in pick_a_piece
        if days_diff == 1:
            print(f'The next due date for the piece would be tomorrow.')
            print('Would you like to practice it again anyway?')
            answer_3 = yes_no_validation()
            if answer_3 is True:
                continue
            else:
                update_index(current_piece)
                break
        else:
            print("Great!")
            print(f'The piece won\'t be due for another {days_diff} days.')
            update_index(current_piece)
            print('Let\'s move on to the next piece.\n')
            break


def well_okay_bad_validation():
    """
    Validates the user input for three options (well, okay, bad)
    """
    print("Type 'w' and press 'Enter' if it went well. (At tempo, no errors)")
    print("Type 'o' and press 'Enter' if it went okay. (Not at tempo or only a few errors)")
    print("Type 'b' and press 'Enter' if it went bad. (Not at tempo and some errors)")
    while True:
        user_input = input("\n").strip()
        print("---------------------------")
        if user_input.lower() == "w":
            return 2
        elif user_input.lower() == "o":
            return 1
        elif user_input.lower() == "b":
            return 0
        else:
            print("\nInvalid input.\n")


def three_options_validation(options):
    """
    Validates the user input for three options
    """
    a, b, c = options

    while True:
        print(a[1])
        print(b[1])
        print(c[1])
        user_input = input("\n").strip()
        print("---------------------------")
        if user_input.lower() == a[0]:
            return 2
        elif user_input.lower() == b[0]:
            return 1
        elif user_input.lower() == c[0]:
            return 0
        else:
            print("\nInvalid input.\n")


def update_due_date_and_count(current_piece, answer):
    """
    Updates due date using the count value and
    a factor depending on the answer variable.
    If 2 is passed as the answer variable, the due date is updated
    to the current date plus the new count value.
    If 1 or 0 is passed as the answer variable, the due date is updated
    to the old due date plus the new count value.
    """
    if answer == 2:
        factor = 1.5
    elif answer == 1:
        factor = 1
    else:
        factor = 0.5
    new_count = math.ceil(int(current_piece.count) * factor)
    # print(new_count)  # check
    due_date = current_piece.due_date
    # print(due_date)  # check
    if answer == 2:
        new_due_date = datetime.datetime.now().date() + datetime.timedelta(days=new_count)
        # print(new_due_date)  # check
    else:
        new_due_date = convert_string_to_date(due_date) + datetime.timedelta(days=new_count)
        # print(new_due_date)  # check
    # Update count on spreadsheet!!! -> Is done in practice_piece function
    return (convert_date_to_string(new_due_date), new_count)


def check_due_date(new_due_date):
    """
    Checks if the new due date is in the future
    """
    return (convert_string_to_date(new_due_date) - datetime.datetime.now().date()).days


def update_index(current_piece):
    """
    Updates the due date and the count of the current piece
    """
    get_index().update_cell(int(current_piece.index) + 1, 6, current_piece.due_date)
    get_index().update_cell(int(current_piece.index) + 1, 7, current_piece.count)


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


"""
=== Utensils section ===
This code would go in a new file called utensils.py
Calls of functions from that file would be adjusted accordingly
"""


def get_all_index_data():
    """
    Gets all data in the index worksheet
    """
    index = get_index()
    return index.get_all_values()


def get_index():
    """
    Gets the index worksheet
    """
    return SHEET.worksheet('Index')


def yes_no_validation():
    """
    Validates the user's answer to be yes or no
    """
    while True:
        print("Type 'y' for yes and press 'Enter'.")
        print("Otherwise type 'n' for no and press 'Enter':")
        confirmation = input("\n").strip()
        print("---------------------------")
        if confirmation.lower() == "y":
            return True
        elif confirmation.lower() == "n":
            return False
        else:
            print("\nInvalid input.\n")


def convert_date_to_string(date):
    """
    Converts a date in the format "YYYY-MM-DD" to a string of the same format"
    """
    return date.strftime('%Y-%m-%d')


def convert_string_to_date(str_date):
    """
    Converts a string in the format "YYYY-MM-DD" to a date of the same format"
    """
    return datetime.datetime.strptime(str_date, '%Y-%m-%d').date()


main_menu()
