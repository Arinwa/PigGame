 1. General description of the game:
"Pig" is a game played by 2 players. A player gains point by throwing a dice.
If for example a player throws a "5" on a dice, he/she accumulates 5 points for that specific throw.
A player can throw as many times as he/she wants to accumulate points.
But his/her turn ends immediately he throws a "1". The points accumulated is then reset.
It will then be the turn of the next player.
A player can choose to hold his/her hand whenever he/she wants during a turn.
The first to reach 100 points wins the game.
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
2. Implementation:
The PIG GAME is run from the Main.py file. Within this file, another file in which a user passes an argument is called. The program will then set the game mode to either single or multi player depending on the argument passed in by the user.
The singleplayer.py or the multiplayer.py file will then follow. This is where most of the processing is done as all of the game logic is within these two files.

- Singleplayer.py:
Here, the game is between the user (player) and the computer.
To set up the bot difficulty, a method named "set_bot_level" is called of instance 'bot'.
The method will then ask the user the desired level he/she wants the bot to be.
Thereafter, the code will set a randomised number which will represent the times that the bot will throw dice until it decides to hold a hand.

For instance, if a player chooses "normal" level game, the bot will throw from 1 to 3 - random int in range (1-3) - times per turn.
The bot's turn itself is an automated one. It simply calls the roll method of class "Dice" after each player's turn.
If the level of difficulty is set to "hard", the bot will throw from 5 to 8 - random int in range (5-8) - times per turn.

- Multiplayer.py
 Here the game is between two real players.
 No turn is automated here. This implies that each player has to pass arguments to the console in order to do anything during a turn.
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
3. Installations:
- Download the zipped game file.
- Open cmd/any console with admin privileges.
- Be sure you already have python package installed on your PC.
  You can do this by typing "python --version" to check the current installed python version your PC.
- The above command will launch the Microsoft Store and redirect you to the Python application page 
  if you don’t have a version of Python on your system.
- Download and install the package.
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
4. To run the game:
- Extract the files in the downloaded zipped folder to another folder in your computer.
- Open cmd/any console with admin privileges.
- Change directry to the folder containg the extracted files.
- When in the directory, type "python main.py"
- Goodluck wth your game!
-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
5. To run the complete testsuite:
- Install coverage:
  open any terminal and type
  "pip install coverage"
- To run all tests, type
  "coverage run -m unittest"
- to run a particular test
  "coverage run -m unittest <test_filename>.py"
- to produce report, type:
  "coverage report"
- to generate html file with the report, type:
  "coverage html"
- Thereafter, you can navigate to <project_folder>/htmlcov/index.html to open the html file in a browser.

-----------------------------------------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------------------------------------
6. To generate documentation from the code:
- Install pdoc. 
- Type in cmd:
  "pip install pdoc"
- To generate the documentation of a file, type in cmd:
  "pdoc <name_of_module>"
- To save documentation as html under ./doc directory, type in cmd:
  "pdoc <name_of_module> -o ./docs"
  -----------------------------------------------------------------------------------------------------------------------------
  -----------------------------------------------------------------------------------------------------------------------------
  7. To generating UML diagrams for the codes:
  - Install pylint. Type in cmd:
    "pip install pylint"
  - Use pyreverse command to create the UML diagram image. Type in cmd:
    "pyreverse <name of the file>"
  - Thereafter, type: "dot -Tpng classes.dot -o <output_path_name>"
