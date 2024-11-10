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





