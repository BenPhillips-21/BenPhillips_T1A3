# BenPhillips_T1A3

Link to source control repository: https://github.com/HolidayGuy21/BenPhillips_T1A3/tree/main/src

Link to Trello Board https://trello.com/b/K35wxBo9/benphillipst1a3

Link to Presentation (PART 1) https://www.loom.com/share/9d4476d0eeee493bbaa15337c215f4ef
Link to Presentation (PART 2) https://www.loom.com/share/31bb438b909e4b1fadcb758349b60e2e

My application adheres to 'PEP 8 - Style Guide for Python Code' written by the creator of Python, Guido Van Rossum.

**How To Run The Game**

I have created a simple wrapper for the app to run the game. In order to run the game, first navigate to the terminal and type in './Saloon_Game.sh' and then the program should run. If that doesn't work, type in 'chmod +x Saloon_Game.sh' and then retry and the script will work. 

__Features:__

**Blackjack**
The main game is Blackjack. It features 3 functions. In order to draw random cards from a deck, I initialized a deck with all the different card types, and also initialized two empty lists (one hand for the dealer and one hand for the user) and then used the random module to randomly add two cards to the dealer and users lists from the deck. The 'calculate hand' function uses a for loop that cycles through the items in the user's hand (which is a list) and adds up the total of them and subsequently returns that total which is used in the hit and stand functions. Both the 'hit' and 'stand' functions use global variables so that they can access the variables that aren't available to them in their local scope. 

After the initial hand is dealt to the player their input is asked for, and using error handling, if the input is not either 'hit' or 'stand' a 'ValueError' is raised and the user is asked to re-enter a valid input. The 'hit' function runs when the user inputs 'hit' after their initial hand (unless their opening hand is blackjack). 'Hit' uses an 'if/elif/else' statement to determine whether the player gets blackjack, busts, or if they get neither of these, then it asks them to 'hit' or 'stand' again. The 'stand' function starts out by revealing the dealers second card (as the dealers opening hand is always obscured in blackjack) and if the dealer has not won (or tied) with his opening hand then it goes into the else statement, and keeps drawing cards while the result of the dealers hand is less than 21 until it either busts, wins, or pushes.

**Protein Calculator**
Another feature I included is a 'protein calculator' I made which is designed to give the user an accurate calculaton of the amount of protein they should eat to reach their goals depending on various factors. The protein calculator involves one main function that takes the arguments 'age', 'weight', 'height', 'gender', 'activity level', and 'goals'. It starts by passing the arguments into the Harris Benedict Equation which determines a persons basal metabolic rate (BMR). Subsequently, the BMR goes into an if/elif/else statement and is used to calculate the users total daily energy expenditure (TDEE) by multiplying it depending on how active the user is. It then goes into another if/elif/else statement with the TDEE and calucates the final result depening on what the users goals are. The program also includes error handling to ensure that the user inputs valid values for their age, weight, and height. If the user inputs an invalid value, the program will prompt them to enter a valid value. Once the user has inputted valid values, the program will call the 'protein calculator' function with the user's input as the arguments.

**Joke Game**
The joke game involves the user 'talking' to a drunk character who tells a random joke. The script uses the requests module to send a GET request to a website with jokes on it to retrieve a list of ten jokes in JSON format. The json module is used to parse the JSON data returned by the API into a Python object, which is stored in the jokes variable. The random module is used to select a random joke from the list of jokes stored in jokes, which is assigned to the joke variable. An opening line is randomly selected from the opening_line list and assigned to the random_line variable.The opening line is printed to the console using the print function. The setup of the joke is printed to the console using the print function and accessed via the joke dictionary using the key 'setup'. The input function is used to prompt the user to press Enter to hear the punchline. Once the user presses Enter, the punchline of the joke is printed to the console using the print function and accessed via the joke dictionary using the key 'punchline'. 

The play_again function is called to ask the user if they want to play again. The use of variables and the concept of variable scope is demonstrated in this code by storing data in variables such as reply, jokes, joke, and random_line. These variables have different scopes, meaning they can be accessed from different parts of the code depending on where they were defined. The for loop is used to give the user three chances to guess the random number generated by random_number = random.randint(1, 15). The while loop is used to handle errors when the user enters an invalid guess. The except block is used for error handling by catching any ValueError exceptions that might occur when the user enters an invalid guess. The error message "Please enter a valid integer for your guess." is printed to the console if an exception is caught.

**Shoot Game**
The 'shoot' game involves the user 'talking' to a bad guy who has a problem with them, so he plays a number guessing game with the user. Using the 'random' package, it generates a random integer between 1 and 15. The game then starts by asking the player to guess the number, and it gives them up to three attempts to do so. It does this by using  a for loop to give the player three chances to guess the number. The loop iterates three times and prompts the player for their guess each time. The code also uses if/elif statements to evaluate the player's guess and provide feedback on whether the guess is too high, too low, or correct.

If the player guesses correctly, the bad guy calls the user a "lucky son of a gun" and then the play again function is called. If the player guesses incorrectly, the game provides feedback to help them guess better in the next round. If the player exhausts all three guesses it enters the else statement and the bad guy shoots the user and it the game ends using sys.exit. The code uses a try/except block to handle the possibility that the player enters a non-integer guess. The try block attempts to convert the input to an integer, and if it fails (because the input is not a valid integer), the except block catches the resulting ValueError exception and prompts the player to enter a valid integer.

__Implementation Plan__

**Blackjack Plan**

Due date: Wednesday May 10th

1. Define and implement the calculate_hand function to calculate the value of a given hand.
2. Define and implement the play_again function to ask the user if they want to play again and exit the game if they don't.
3. Define and implement the hit function to add a card to the user's hand, calculate the value of the hand, and determine if the user has won, lost, or needs to choose hit or stand again.
4. Define and implement the stand function to add cards to the dealer's hand until their hand is greater than or equal to 17, calculate the value of the hand, and determine if the dealer has won, lost, or pushed.
5. Define and create the deck of cards to be used in the game.
6. Initialize the dealer and user hands by selecting two cards from the deck.
7. Print the user's hand and ask the user if they want to hit or stand.
8. Call either the hit or stand function depending on the user's input.
9. Use conditionals to determine the winner or if the game has pushed.
10. Ask the user if they want to play again, and repeat the game if they do.



**Protein Calculator Plan**

Due date: Thursday May 11th

1. Define the protein_calculator() function that takes in age, weight, height, gender, activity, and goals as input parameters.
2. Within the protein_calculator() function, calculate the Basal Metabolic Rate (BMR) based on the gender using the appropriate formula.
3. Calculate the Total Daily Energy Expenditure (TDEE) based on the activity level using the appropriate formula.
4. Calculate the protein requirement based on the weight goals provided using the appropriate formula.
5. Return the protein requirement calculated in the function.
6. Use a loop and try-except blocks to get input from the user for age, height, weight, gender, activity, and weight goals.
7. Print error messages for invalid input and ask the user to enter valid input until they provide valid input.
8. Call the protein_calculator() function with the user's input and store the returned value in the protein_requirement variable.

**Number Guessing Game Plan**

Due date: Friday May 12th

1. Define the game's rules and win/lose conditions.
2. Generate a random number between 1 and 20.
3. Allow the player to input a guess.
4. Validate the input to ensure that it is an integer.
5. Compare the player's guess with the random number generated.
6. If the guess is correct, congratulate the player and offer to play again.
7. If the guess is incorrect, provide feedback on whether the guess is too high or too low.
8. Allow the player to guess up to 3 times.
9. If the player is unable to guess correctly within 3 attempts, inform them that they have lost the game.

**Joke Game Plan**

Due date: Friday May 12th

1. Install the requests module using pip.
2. Import the necessary modules: requests, json and random.
3. Use the requests module to get the API response from 'https://official-joke-api.appspot.com/jokes/ten'.
4. Parse the response content to JSON using the json module.
5. Choose a random joke from the list of jokes using the random module.
6. Create a list of opening lines to randomly choose from.
7. Print a random opening line.
8. Print the setup of the chosen joke.
9. Wait for user input to proceed to the punchline.
10. Print the punchline of the chosen joke.

**Help Documentation**

In order to run the program, the user must type 'python3 saloon.py' into the terminal. The set up of the game will then be presented to the user detailing that they're in an old saloon in the Wild West. The user is given four options of things they can do which can be accessed by typing in the terminal 'blackjack', 'muscles', 'drunk' or 'bad.

**Blackjack How to Play**

The user can play Blackjack by first entering 'blackjack' in the command line after the prompt at the start of the program. Blackjack is a card game where players aim to get a hand with a value of 21 or as close to 21 as possible without going over, while also beating the dealer's hand.  The user is dealt two cards, and can then choose to "hit" (by inputting 'hit' when prompted) and receive additional cards to increase their hand value, or "stand" (by inputting 'stand' when prompted) and keep their current hand. Included below where the user's hand is printed, is also printed the sum of their cards in brackets. The dealer also receives two cards, but only one of them is revealed to the players (at the start). The dealer must hit until their hand value is 17 or higher. Natural win: If a player has an ace and a 10-point card in the first two cards, it is called a natural or blackjack and wins automatically, unless the dealer also has a blackjack. If a player's hand is closer to 21 than the dealer's without going over 21, the player wins. If the dealer's hand is closer to 21 than the player's without going over 21, the dealer wins. If the player's and dealer's hands have the same value, the game is a tie or push. If a player's hand value exceeds 21, the player loses immediately, regardless of the dealer's hand.

**Protein Calculator How To Use**

The user can use the Protein Calculator by first entering 'muscles' in the command line after the prompt at the start of the program. In order to use the protein calculator, simply enter the necessary information when prompted. The calculator will then output the results.  The code assumes that you have knowledge of your weight, height and fitness goals before using it. You may need to research and gather this information before using the calculator. 

**Joke Game How To Use**

In order to run the joke game, all the user must first input 'drunk' in the command line at the prompt at the start of the program. The game will then tell the setup of the joke and in order to hear the punchline the user must hit enter on their keyboard. 

**Number Guess Game How To Use**

The user can play the number guessing game by first entering 'bad' in the command line after the prompt at the start of the program. The user must then enter a number in the command line until they either run out of guesses or they win.



