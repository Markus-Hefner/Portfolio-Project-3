![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **May 14, 2024**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!



# It Is Practice Time

It Is Practice Time is a Python terminal app for musicians that utilizes spaced repetition to assist in learning new pieces as well as maintaining an already existing repertoire.

In order to achieve that the app takes care of tracking the progress on a previously added piece through user input, uses that progress to calculate the next time the piece should be practiced and thus automatically suggests what to practice in a given practice session.

Thereby it not only relieves the musician from figuring out what to practice next, which can be time consuming especially if the repertoire increases to a large number of pieces, but also from keeping track of the progress manually. Furthermore it gives her/him the peace of mind that no piece will be forgotten and it will be suggested for practice when the time comes.

All this leads to a more enjoyable practice experience since it streamlines the process by taking care of some of the "book keeping" and decision making and thus helps the musician to focus on the most important part of a practice session: to play music.

IMAGE

## Table of Contents

- User Stories
- Features
- Future Features
- Technology
- Testing
- Deployment
- Credits

## User Stories

### First Time User Goals
- I want to know what the app is about in order to decide whether or not it is of any use for me.

### Returning and Frequent User Goals
- I want to get to action as fast as possible whether this is viewing the repertoire, adding new pieces or practicing.

## Features

Main Menu

IMAGE

- In the main menu the user can select between four options:
    - Showing the already existing repertoire
    - Adding a new piece
    - Practicing
    - Exiting the app

Repertoire

IMAGE

- List of the the pieces in the repertoire with the index of the piece and the information the user added. With the mouse can scroll through the repertoire.

Adding a New Piece

IMAGE

- The user adds the title of the piece, the composer (optional), the arranger (optional) and any additional information (optional)
- As for the title the app checks whether or not the piece already exists or if the user put no title or just spaces which are all invalid inputs. This will also be reflected to the user.

Practicing

IMAGE

- A piece is suggested to the user to practice. The user can then decide if she/he wants to practice that piece, move on to the next one or go back to the main menu.
- If the user has practiced a piece and assessed how it went, she/he is then asked if she/he wants to practice it again or not or, in the case that the piece's next due date is more than two days in the future, the user is suggested the next piece.
- This process continues until the new due dates of the pieces are at least two days in the future or the user decides to end the practice session by returning to the main menu.

Exiting

IMAGE

- Exits the app.

## Future Features

- A graphical interface to make using the app more appealing.
- The user would be able to break up pieces themselves into several parts which have there own due dates. Only after all the due parts are practiced enough so that they are not due anymore the due date of the piece itself gets updated. If the user skips a part that would be due the due date of the piece would not be updated but for the current practice session she/he would still move on to the next piece.
- Adding tracking at which tempo the user is able to play a certain piece or part of it measured in beats per minute. Before updating the due date the tempo would be updated until the user is at a previously defined tempo goal. In contrast to updating the due date here negative values are also possible since if a piece/part doesn't work the user should first practice it slower.
- Removing piece from the list that the user no longer wants to practice at all.
- Editing pieces after they have been added.

## Technology

- Codeanywhere was used to write and edit the code.
- GitHub was used to store the code.
- Heroku was used to deploy the code in Code Institute's mock terminal.

## Testing

### Code Validation

- The PEP8 Python Validator was used to check the code. No error were found.

IMAGE

### User Stories

#### First Time User Goals
- I want to know what the app is about in order to decide whether or not it is of any use for me.
    - Since a short and concise explanation of the app is delivered right at the beginning I get the information I need to decide.

#### Returning and Frequent User Goals
- I want to get to action as fast as possible whether this is viewing the repertoire, adding new pieces or practicing.
    - Since there is no complex menu to navigate but all the functions can be accessed in thge main menu I can immediately start with whatever it is that I want to do. Furthermore the app takes me by the hand tells me what I can and cannot do and gives me constant feedback.

### Manual Testing

| Situation             | User Action | Outcome | Test Result |
| :------------------ | :---------: | :------ | :---------: |
| Main menu | 'r' + confirmation with 'Enter' | Repertoire is displayed and the user is redirected to the main menu | passed |
| Main menu | 'a' + confirmation with 'Enter' | User is prompted to enter and confirm a title | passed |
| User is prompted to enter and confirm a title | [already existing title] + confirmation with 'Enter' | User is informed that the title already exists, that a new name is required and prompted to enter and confirm a title again | passed |
| User is prompted to enter and confirm a title | [just one or multiple spaces] + confirmation with 'Enter' | User is informed that the title can not be empty and prompted to enter and confirm a title again | passed |
| User is prompted to enter and confirm a title | [title] + confirmation with 'Enter' | User is prompted to enter and confirm a composer | passed |
| User is prompted to enter and confirm a composer | [composer (optional)] + confirmation with 'Enter' | User is prompted to enter and confirm an arranger | passed |
| User is prompted to enter and confirm an arranger | [arranger (optional)] + confirmation with 'Enter' | User is prompted to enter and confirm additional information | passed |
| User is prompted to enter and confirm additional information | [additional information (optional)] + confirmation with 'Enter' | User is prompted to check if the given data is correct | passed |
| User is prompted to check if the given data is correct | 'a' + confirmation with 'Enter' | User is informed that the new piece has been added and is redirected to the main menu. Also the spreadsheet is updated (with cells left blank if no input was given) | passed |
| User is prompted to check if the given data is correct | 'r' + confirmation with 'Enter' | User is prompted to enter and confirm a title | passed |
| User is prompted to check if the given data is correct | 'x' + confirmation with 'Enter' | User is redirected to the main menu | passed |
| Main menu | 'p' + confirmation with 'Enter' | User is suggested the next piece to practice | passed |
| User is suggested the next piece to practice | 'p' + confirmation with 'Enter' | User is asked to practice and to assess it | passed |
| User is suggested the next piece to practice | 'n' + confirmation with 'Enter' | User is suggested the next piece to practice | passed |
| User is suggested the next piece to practice | 'x' + confirmation with 'Enter' | User is redirected to main menu | passed |
| User is asked to practice and to assess it | 'w' + confirmation with 'Enter' | (If the new due date is tomorrow) User is informed that the due date was updated, that the next due date for the piece is tomorrow and asked if she/he wants to practice it anyway | passed |
| User is asked to practice and to assess it | 'w' + confirmation with 'Enter' | (If the new due date is after tomorrow and if there are more pieces to be practiced) User is informed that the due date was updated, that the piece won't be due for another two days and suggested the next piece to practice. Also the spreadsheet is updated | passed |
| User is asked to practice and to assess it | 'w' + confirmation with 'Enter' | (If the new due date is after tomorrow and if there are no more pieces to be practiced) User is informed that the due date was updated, that she/he got through all the material and is redirected to the main menu. Also the spreadsheet is updated | passed |
| User is asked to practice and to assess it | 'o' + confirmation with 'Enter' | (if the new due date is today or before) User is informed that the due date was updated and asked if she/he wants to practice the piece again | passed |
| User is asked to practice and to assess it | 'o' + confirmation with 'Enter' | (if the new due date is tomorrow) User is informed that the due date was updated, that the next due date for the piece is tomorrow and asked if she/he wants to practice it anyway | passed |
| User is asked to practice and to assess it | 'o' + confirmation with 'Enter' | (If the new due date is after tomorrow and if there are more pieces to be practiced) User is informed that the due date was updated, that the piece won't be due for another two days and suggested the next piece to practice. Also the spreadsheet is updated | passed |
| User is asked to practice and to assess it | 'o' + confirmation with 'Enter' | (If the new due date is after tomorrow and if there are no more pieces to be practiced) User is informed that the due date was updated, that she/he got through all the material and is redirected to the main menu. Also the spreadsheet is updated | passed |
| User is asked to practice and to assess it | 'b' + confirmation with 'Enter' | (if the new due date is today or before) User is informed that the due date was updated and asked if she/he wants to practice the piece again | passed |
| User is asked to practice and to assess it | 'b' + confirmation with 'Enter' | (if the new due date is tomorrow) User is informed that the due date was updated, that the next due date for the piece is tomorrow and asked if she/he wants to practice it anyway | passed |
| User is asked to practice and to assess it | 'b' + confirmation with 'Enter' | (If the new due date is after tomorrow and if there are more pieces to be practiced) User is informed that the due date was updated, that the piece won't be due for another two days and suggested the next piece to practice. Also the spreadsheet is updated | passed |
| User is asked to practice and to assess it | 'b' + confirmation with 'Enter' | (If the new due date is after tomorrow and if there are no more pieces to be practiced) User is informed that the due date was updated, that she/he got through all the material and is redirected to the main menu. Also the spreadsheet is updated | passed |
| User is informed that the due date was updated and asked if she/he wants to practice the piece again | 'y' + confirmation with 'Enter' | User is asked to practice and to assess it | passed |
| User is informed that the due date was updated and asked if she/he wants to practice the piece again | 'n' + confirmation with 'Enter' | (If there are more pieces to be practiced) User is informed that the due date was updated and suggested the next piece to practice. Also the spreadsheet is updated | passed |
| User is informed that the due date was updated and asked if she/he wants to practice the piece again | 'n' + confirmation with 'Enter' | (If there are no more pieces to be practiced) User is informed that the due date was updated, that she/he got through all the material and is redirected to the main menu. Also the spreadsheet is updated | passed |
| User is informed that the due date was updated, that the next due date for the piece is tomorrow and asked if she/he wants to practice it anyway | 'y' + confirmation with 'Enter' | User is asked to practice and to assess it | passed |
| User is informed that the due date was updated, that the next due date for the piece is tomorrow and asked if she/he wants to practice it anyway | 'n' + confirmation with 'Enter' | (If there are more pieces to be practiced) User is informed that the due date was updated and suggested the next piece to practice. Also the spreadsheet is updated | passed |
| User is informed that the due date was updated, that the next due date for the piece is tomorrow and asked if she/he wants to practice it anyway | 'n' + confirmation with 'Enter' | (If there are no more pieces to be practiced) User is informed that the due date was updated, that she/he got through all the material and is redirected to the main menu. Also the spreadsheet is updated | passed |
| Main menu | 'x' + confirmation with 'Enter' | Exits app or (in the mock terminal) doesn't return to the main menu | passed |
| [Any] | '[any other input than the ones to be choosen from]' + confirmation with 'Enter' | The User will be notified that it was an invalid input and the same prompt/question appears again | passed |

### Bugs

#### Solved Bugs
- I could not figure out how to sort a list of list by an item in the sublists other than the first one.
    - After many trys and a lot of research for solutions I eventually found the expression 'key = lambda' which worked.

- When adjusting the code to pass the PEP8 Python Validator the value for the new_due_date variable in the update_due_date_and_count() function I was unable to split the expression (an addition) over two lines with using a backshlash.
    - I solved this by utilising an extra variable with a short name, assigning it the value of one of the terms and then using that variable in the addition.

- To pass the PEP8 Python Validator I had to shorten some of the print statement or stretch them over several lines. I thought that since the statement is between brackets I could split the state into another. However, that didn't work: It was still displayed in one line with the now added space from the identation of the second line.
    - I solved this by putting quotation marks at the end of the first and the beginning of the second line and also adding a \n at the end of the first line thus effectively splitting the statement into to several statements. I also could have simply printed a new statement but since it was one sentence I wanted to keep it in one statement.


#### Unsolved Bugs
- Currently there are no know unsolved bugs.



## Deployment

### Heroku
- Create Heroku account. (If this is already done you can skip this step.)
- Log into your IDE.
- Log into Heroku account.
- Click on the 'Create new app'-button on the dashboard. Alternatively click on the 'New'-button in the upper right corner of the dashboard and select 'Create new app' from the drop-down menu.
- Give you app a valid name in the designated input field.
- Select your region.
- Click on the 'Create app'-button.
- On the next screen select the 'Settings'-tab.
- Scroll down an click on the 'Reveal Config Vars'-button.
- Enter 'CREDS' in the field for key.
- Copy the content from your workspace



## Credits

- Code Institute's mock terminal was used to deploy the app.
- I used the if __name__ == '__main__': expression 








