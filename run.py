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


def welcome():
    print("==================================================================")
    print("\n***** Welcome to It Is Practice Time! *****\n")
    print("It Is Practice Time is an app for musicians assisting in\n"
          "learning new pieces, building a repertoire and\n"
          "maintaining your capability to play those pieces.")
    print("In order to do that it automatically keeps track of your progress\n"
          "on a certain piece and suggests what to practice next\n"
          "utilising spaced repetition.\n")

    main_menu()


def main_menu():
    """
    The user decides whether to practice, add a new piece or show repertoire
    """
    print("============================")
    print("Your are now in the Main Menu!")
    print("What would you like to do?\n")
    print("Type 'r' and press 'Enter' if you want to see your repertoire.")
    print("Type 'a' and press 'Enter' if you want to add a new piece.")
    print("Type 'p' and press 'Enter' if you want to start practicing.")
    print("Type 'x' and press 'Enter' if you want to exit the programme.\n")

    user_decision = input("\n").strip()
    print("----------------------------")

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
    all_index_data = get_all_index_data()
    all_index_data.pop(0)
    for i in all_index_data:
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
        existing_titles = [col[1].lower() for col in get_all_index_data()
                           if col[1].lower() != "title"]

        if title.lower() in existing_titles:
            print("\n----------------------------")
            print("This piece already exists in your repertoire.")
            print("Please choose another title or add additional information.")
            print(f'(E.g.: "{title} (other Version)")\n')
            continue
        # Check if the title is empty
        elif title == "":
            print("\n----------------------------")
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

        print("\nPlease check if the following data is correct:\n")
        print(f"Title: {title}")
        print(f"Composer: {composer}")
        print(f"Arranger: {arranger}")
        print(f"Additional information: {additional_info}\n")

        user_decision = [
            ("a", "Type 'a' and press 'Enter' if you want to add the piece."),
            ("r", "Type 'r' and press 'Enter' if you want to re-enter the "
                "piece."),
            ("x", "Type 'x' and press 'Enter' if you want to discard the "
                "entry and get back to the main menu.")
        ]
        answer = three_options_validation(user_decision)
        if answer == 2:
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

            print("\nNew piece has been added to your repertoire\n")
            break
        elif answer == 1:
            continue
        else:
            break

    main_menu()


def get_index_number():
    """
    Gets the index number of the last piece in the index
    """
    index_number = get_index().col_values(1)
    if len(index_number) == 1:
        return 0
    else:
        return int(index_number[-1])


def add_piece_to_index(new_piece):
    """
    Adds a new piece to the index
    """
    get_index().append_row(new_piece)


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
    sorted_due_pieces = sort_by_timestamp(due_pieces)
    sorted_due_pieces_len = len(sorted_due_pieces)
    iterables_list = create_iterables_list(sorted_due_pieces_len)

    for i in iterables_list:
        a, b, c, d, e, f, g = sorted_due_pieces[i]
        i += 1
        current_piece = PracticePiece(a, b, c, d, e, f, g)

        print(f'The next piece to practice is {current_piece.title}.\n')

        user_decision = [
            ("p", "Type 'p' and press 'Enter' if you want to practice the "
                "piece now."),
            ("n", "Type 'n' and press 'Enter' if you want to move on to the "
                "next piece."),
            ("x", "Type 'x' and press 'Enter' if you want get back to the "
                "main menu.")
        ]
        answer = three_options_validation(user_decision)
        if answer == 2:
            practice_piece(current_piece)
        elif answer == 1:
            print('Alright, let\'s move on to the next piece.\n')
            continue
        else:
            break

    print('Congratulations, you got through all the material')
    print('Hope to see you again tomorrow :-)')

    main_menu()


def create_due_list(all_index_data):
    """
    Removes the list item with the headings in it (which is also a list).
    Removes list items of which the timestamp is > today.
    """
    all_index_data.pop(0)
    due_list = [col for col in all_index_data if convert_string_to_date(col[5])
                <= datetime.datetime.now().date()]

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
        print('\nGreat let\'s go!\n')
        print(f'---> Play {current_piece.title} and let us now how it went.\n')
        print('How did it go?')
        assessment_options = [
            ("w", "Type 'w' and press 'Enter' if it went well. "
                "(At tempo, no errors)"),
            ("o", "Type 'o' and press 'Enter' if it went okay. "
                "(Not at tempo or only a few errors)"),
            ("b", "Type 'b' and press 'Enter' if it went bad. "
                "(Not at tempo and some errors)")
        ]
        answer = three_options_validation(assessment_options)

        new_due_date = update_due_date_and_count(current_piece, answer)[0]
        new_count = update_due_date_and_count(current_piece, answer)[1]

        current_piece.due_date = new_due_date
        current_piece.count = new_count

        days_diff = check_due_date(current_piece.due_date)

        if days_diff <= 0:
            print('Due date updated.')
            print('Would you like to go again?')
            answer_2 = yes_no_validation()
            if answer_2 is True:
                continue
            else:
                update_index(current_piece)
                print('Alright, let\'s move on to the next piece.\n')
                break
        if days_diff == 1:
            print('Due date updated.')
            print('The next due date for the piece would be tomorrow.')
            print('Would you like to practice it again anyway?')
            answer_3 = yes_no_validation()
            if answer_3 is True:
                continue
            else:
                update_index(current_piece)
                break
        else:
            print("Due date updated.")
            print("Great!")
            print(f'The piece won\'t be due for another {days_diff} days.')
            update_index(current_piece)
            print('Let\'s move on to the next piece.\n')
            break


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
        print("----------------------------")
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
    due_date = current_piece.due_date

    if answer == 2:
        now = datetime.datetime.now().date()
        new_due_date = now + datetime.timedelta(days=new_count)
    else:
        due_date_as_date = convert_string_to_date(due_date)
        new_due_date = due_date_as_date + datetime.timedelta(days=new_count)

    return (convert_date_to_string(new_due_date), new_count)


def check_due_date(new_due_date):
    """
    Checks if the new due date is in the future
    """
    return (convert_string_to_date(new_due_date)
            - datetime.datetime.now().date()).days


def update_index(current_piece):
    """
    Updates the due date and the count of the current piece
    """
    get_index().update_cell(int(current_piece.index)
                            + 1, 6, current_piece.due_date)
    get_index().update_cell(int(current_piece.index)
                            + 1, 7, current_piece.count)


class PracticePiece:
    """
    Class of the pieces to be practiced
    """
    def __init__(self, index, title, composer, arranger, additional_info,
                 due_date, count):
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
        print("----------------------------")
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


if __name__ == '__main__':
    welcome()
