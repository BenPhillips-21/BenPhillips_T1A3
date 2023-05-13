# BenPhillips_T1A3

Link to source control repository: https://github.com/HolidayGuy21/BenPhillips_T1A3/tree/main/src

My application adheres to 'PEP 8 - Style Guide for Python Code' written by the creator of Python, Guido Van Rossum.

__Features:__

**Blackjack**
The main game is Blackjack. It features 3 functions. In order to draw random cards from a deck, I initialized a deck with all the different card types, and also initialized two empty lists (one hand for the dealer and one hand for the user) and then used the random module to randomly add two cards to the dealer and users lists from the deck. The 'calculate hand' function uses a for loop that cycles through the items in the user's hand (which is a list) and adds up the total of them and subsequently returns that total which is used in the hit and stand functions. Both the hit and stand functions use global variables so that they can access the variables that aren't available to them in their local scope. After the initial hand is dealt to the player their input is asked for, and using error handling, if the input is not either 'hit' or 'stand' it asks them to re-enter the input. The hit function runs when the user inputs 'hit' after their initial hand (unless their opening hand is blackjack). 'Hit' uses an 'if/elif/else' statement to determine whether the player gets blackjack, busts, or if they get neither of these, then it asks them to 'hit' or 'stand' again. The 'stand' function starts out by revealing the dealers second card (as the dealers opening hand is always obscured in blackjack) and if the dealer has not won (or tied) with his opening hand then it goes into the else statement, and keeps drawing cards while the result of the dealers hand is less than 21 until it either busts, wins, or pushes.

**Protein Calculator**
Another feature I included is a 'protein calculator' I made which is designed to give the user an accurate calculaton of the amount of protein they should eat to reach their goals depending on various factors. The protein calculator involves one main function that takes the arguments 'age', 'weight', 'height', 'gender', 'activity level', and 'goals'. It starts by passing the arguments into the Harris Benedict Equation which determines a persons basal metabolic rate (BMR). Subsequently, the BMR goes into an if/elif/else statement and is used to calculate the users total daily energy expenditure (TDEE) by multiplying it depending on how active the user is. It then goes into another if/elif/else statement with the TDEE and calucates the final result depening on what the users goals are.



Harris Benedict equation

