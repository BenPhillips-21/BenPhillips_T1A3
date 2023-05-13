import random
import sys
import requests
import json
# playagain function which can be used in all games
def play_again():
        while True:
            again = input("Do ye wish to play again? (y/n): ")
            if again == "y":
                break
            elif again == "n":
                sys.exit()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
# the game set up
print("The year is 1867, you're on the American Frontier sitting at a blackjack table in an old Saloon.")
print("Across from you is the old dealer in a worn-out suit and a bad guy, who stares you down with his hand on his gun...")
print("To your left is a silent, muscular man and to your right is a pathetic drunk babbling on...")
while True:
    while True:
        try: 
            choice = input("Do you want to play blackjack? (blackjack), talk to the muscular man? (muscles), the drunkard? (drunk), or the bad guy? (bad)\n")
            if choice.lower() not in ['blackjack', 'muscles', 'drunk', 'bad']:
                raise ValueError("Input must be one of the strings (blackjack, muscles, drunk, bad)")
            break
        except ValueError as e:
            print(e)


    if choice == "muscles":
        while True:
            try:
                response = input("Do you want to know the ideal amount of protein you should eat that suits your fitness goals, pal? (yes/no)\n")
                if response.lower() not in ['yes', 'no']:
                    raise ValueError("Input must be either 'yes' or 'no'")
                break
            except ValueError as e:
                print(e)
        if response == "yes":
# game in which a muscular man tells you how much protein you should eat depending on your age, weight, height etc
            def protein_calculator(age, weight, height, gender, activity, goals):
                if gender == 'male':
                    bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
                elif gender == 'female':
                    bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)

                if activity == 'sedentary':
                    tdee = bmr * 1.2
                elif activity == 'lightly active':
                    tdee = bmr * 1.375
                elif activity == 'moderately active':
                    tdee = bmr * 1.55
                elif activity == 'very active':
                    tdee = bmr * 1.725
                else:
                    tdee = bmr * 1.9

                if goals == 'gain':
                    protein_calories = tdee * (22/100)
                    protein = protein_calories / 4
                    print(f"You should eat {protein:.2f} grams of protein a day to put on mass")
                    play_again()
                    # yes, you actually should eat more protein when losing weight than when mantaining weight
                elif goals == 'lose':
                    protein_calories = tdee * (20/100)
                    protein = protein_calories / 4
                    print(f"You should eat {protein:.2f} grams of protein a day to lose weight")
                    play_again()
                else: 
                    protein_calories = tdee * (18/100)
                    protein = protein_calories / 4
                    print(f"You should eat {protein:.2f} grams of protein a day to maintain your current mass")
                    play_again()

                return protein
            print("Alright. Well I'm going to have to ask you a few questions first...")
            while True:
                try:
                    age = int(input("How old are you? "))
                    if not (0 <= age <= 100):
                        raise ValueError("Age must be between 0 and 100")
                    break
                except ValueError:
                    print("Please enter a valid integer for your age (0-100)")
                    
            while True:
                try:
                    height = float(input("How tall are you in centimetres? "))
                    if not (0 <= height <= 250):
                        raise ValueError("Please enter a realistic height. (0-250)")
                    break
                except ValueError as e:
                    print(e)

            while True:
                try:
                    weight = float(input("How much do you weigh in kilograms? "))
                    if not (0 <= weight <= 500):
                        raise ValueError("Please enter a realistic weight. (0-500)")
                    break
                except ValueError as e:
                    print(e)
                    
            while True:
                try:
                    gender = input("My eye sight ain't too good, you a male or female? (male/female) ")
                    if gender.lower() not in ['male', 'female']:
                        raise ValueError("Please enter either 'male' or 'female' for your gender.")
                    break
                except ValueError as e:
                    print(e)
                    
            while True:
                try:
                    activity = input("How active are you? (sedentary/lightly active/moderately active/very active/extremely active) ")
                    if activity.lower() not in ['sedentary', 'lightly active', 'moderately active', 'very active', 'extremely active']:
                        raise ValueError("Please enter a valid activity level.")
                    break
                except ValueError as e:
                    print(e)

            while True:
                try:
                    goals = input("And are you trying to gain, maintain, or lose weight? (gain, maintain, lose)  ")
                    if goals.lower() not in ['gain', 'maintain', 'lose']:
                        raise ValueError("Please enter either 'gain', 'maintain', or 'lose' for your weight goals.")
                    break
                except ValueError as e:
                    print(e)


            protein_requirement = protein_calculator(age, weight, height, gender, activity, goals)
        else:
            play_again()
# blackjack game
    elif choice == "blackjack": 
        def calculate_hand(user_hand):
            result = 0
            for item in user_hand:
                if item == 'A':
                    if result <= 10:
                        result += 11
                    else:
                        result += 1
                elif item in ['J', 'K', 'Q']:
                    result += 10
                else:
                    result += int(item)
            return result

        def hit():
            global user_hand
            global result_of_user_hand
            user_hand += random.sample(deck, 1)
            print(user_hand)
            result_of_user_hand = calculate_hand(user_hand) 
            print(result_of_user_hand)
            if result_of_user_hand == 21:
                print("Blackjack! Ye win!")
                play_again()
            elif result_of_user_hand > 21:
                print("Yer busted!")
                play_again()
            else:
                while True:
                    try:
                        user_input = input("Shall ye hit again or shall ye stand? (hit/stand) ")
                        if user_input.lower() not in ['hit', 'stand']:
                            raise ValueError("Input must be either 'hit' or 'stand'")
                        break
                    except ValueError as e:
                        print(e)
                if user_input == 'hit':
                    hit()
                elif user_input == 'stand':
                    stand()    

        def stand():
            global dealer_hand
            global user_hand
            global result_of_dealer_hand
            global result_of_user_hand
            print(f'My opening hand is {dealer_hand}')
            result_of_dealer_hand = calculate_hand(dealer_hand)
            print(result_of_dealer_hand)
            if result_of_dealer_hand == 21:
                print("Blackjack! I win!")
                play_again()
            elif result_of_dealer_hand > result_of_user_hand and result_of_dealer_hand <= 21:
                print("I win! I win!")
                play_again()
            elif result_of_dealer_hand >= 17 and result_of_user_hand > result_of_dealer_hand:
                print("Dangit... you win")
                play_again()
            elif result_of_dealer_hand == result_of_user_hand or result_of_dealer_hand == 22:
                print("Push")
                play_again()
            elif result_of_dealer_hand > 22:
                print("Dangit I'm busted!")
                play_again()
            else:
                while result_of_dealer_hand <= 17:
                    dealer_hand += random.sample(deck, 1)
                    result_of_dealer_hand = calculate_hand(dealer_hand) 
                    print(f'My new hand is {dealer_hand}') 
                    print(f'The sum of my new hand is: {result_of_dealer_hand}')
                    if result_of_dealer_hand == 21:
                        print("Blackjack! I win!")
                        play_again()
                    elif result_of_dealer_hand > result_of_user_hand and result_of_dealer_hand <= 21:
                        print("I win! I win!")
                        play_again()
                        break
                    elif result_of_dealer_hand == result_of_user_hand or result_of_dealer_hand == 22:
                        print("Push")
                        play_again()
                    elif result_of_dealer_hand >= 17 and result_of_user_hand > result_of_dealer_hand:
                        print("Dangit... you win")
                        play_again()
                    elif result_of_dealer_hand > 22:
                        print("Dangit I'm busted!")
                        play_again()
                
        deck = [2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,9,10,
        'A', 'A', 'A', 'A', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q', 'K', 'K', 'K', 'K']

        dealer_hand = []
        user_hand = []
        while True:
            dealer_hand += random.sample(deck, 2)
            user_hand += random.sample(deck, 2)

            print(f'Your hand: {user_hand}')
            result_of_user_hand = calculate_hand(user_hand)  
            print(f'({result_of_user_hand})')
            if result_of_user_hand == 21:
                print("Blackjack! Ye win!")
                play_again()
                break

            result_of_dealer_hand = calculate_hand(dealer_hand)
            print(f"Dealer's first card: {dealer_hand[0]}")

            while True:
                    try:
                        user_input = input("Shall ye hit or shall ye stand? (hit/stand) ")
                        if user_input.lower() not in ['hit', 'stand']:
                            raise ValueError("Input must be either 'hit' or 'stand'")
                        break
                    except ValueError as e:
                        print(e)

            if user_input == 'hit':
                hit()
                break
            elif user_input == 'stand':
                stand()
                break
# game in which a drunk man tells you a random joke
    elif choice == "drunk":
        reply = requests.get('https://official-joke-api.appspot.com/jokes/ten')

        jokes = json.loads(reply.content)

        joke = random.choice(jokes)
        opening_line = [
        'Hey... hey buddy I got a joke for ya...',
        'Hey pal listen to this one...',
        'Ay I got a funny one...',
        'BUUUURP sorry about that, wanna hear a joke?',
        'BUUUUURP'
        ]
        random_line = random.choice(opening_line)
        print(random_line)
        print(joke['setup'])
        input("You wanna hear the punchline? (Press enter)")
        print(joke['punchline'])
        play_again()
# game in which a 'bad man' gives the user 3 tries to guess a number, if user can't get it, they 'die' and the system exits
    elif choice == "bad":

        print("You've been lookin' at me funny this whole game. I'm thinking of a number between 1 and 20...")
        print("You guess which number I'm thinkin' of within 3 tries, you live, otherwise...")
        print("You die.")
        random_number = random.randint(1, 15)
        for i in range(3):
            while True:
                try:
                    guess = int(input("What's your guess? "))
                    break
                except ValueError:
                    print("Please enter a valid integer for your guess.")
            if guess == random_number:
                print("You got it! You a lucky son of a gun, you know that?")
                play_again()
                break
            elif guess > random_number:
                print("Wrong... lower...")
            elif guess < random_number:
                print("Wrong... higher...")
            
        else:
            print("Adios, amigo. BANG!")
            print("You died.")
            sys.exit()
    