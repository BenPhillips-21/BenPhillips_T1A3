import random
import sys
import requests
import json

def play_again():
        while True:
            again = input("Do ye wish to play again? (y/n): ")
            if again == "y":
                break
            elif again == "n":
                sys.exit()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

# from functions import hit, stand, play_again, calculate_hand

print("You're sitting at a blackjack table in an old Saloon.")
print("Across from you is the old dealer and a bad guy, twirling his moustache...")
print("To your left is a very muscular man...")
print("To your right is a young drunk big smile on his face...")
while True:
    choice = input("Do you want to play blackjack? (blackjack), talk to the muscular man? (muscles) the drunkard? (drunk) or the bad looking guy? (bad)\n")

    if choice == "muscles":
        response = input("You look like you go to the gym, you want me to help you find out how much protein you should be eating in order to reach your goals? (yes/no)")
        if response == "yes":

            def protein_calculator(age, weight, gender, activity, goals):
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

            age = int(input("How old are you, in years that is?: "))
            height = float(input("How tall are you in centimetres? "))
            weight = float(input("How much do you weigh in kilograms? "))
            gender = input("My eye sight ain't too good, you a male or female? ")
            activity = input("How active are you? (sedentary/lightly active/moderately active/very active/extremely active): ")
            goals = input("And are you trying to gain, maintain, or lose weight? (gain, maintain, lose)  ")

            protein_requirement = protein_calculator(age, weight, gender, activity, goals)
        else:
            sys.exit()

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


        def play_again():
            while True:
                again = input("Do ye wish to play again? (y/n): ")
                if again == "y":
                    break
                elif again == "n":
                    sys.exit()
                else:
                    print("Invalid input. Please enter 'y' or 'n'.")


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
                user_input = input("Shall ye hit again or shall ye stand? (hit/stand) ")
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
                print("I win!")
                play_again()
            elif result_of_dealer_hand > result_of_user_hand and result_of_dealer_hand <= 21:
                print("I win! I win!")
                play_again()
            elif result_of_dealer_hand == result_of_user_hand or result_of_dealer_hand == 22:
                print("Push")
                play_again()
            elif result_of_dealer_hand > 22:
                print("Dangit I'm busted!")
                play_again()
            else:
                while result_of_dealer_hand < 21:
                    dealer_hand += random.sample(deck, 1)
                    result_of_dealer_hand = calculate_hand(dealer_hand) 
                    print(f'My new hand is {dealer_hand}') 
                    print(f'The sum of my new hand is: {result_of_dealer_hand}')
                    if result_of_dealer_hand == 21:
                        print("I win!")
                        play_again()
                    elif result_of_dealer_hand > result_of_user_hand and result_of_dealer_hand <= 21:
                        print("I win! I win!")
                        play_again()
                        break
                    elif result_of_dealer_hand == result_of_user_hand or result_of_dealer_hand == 22:
                        print("Push")
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
            user_input = input("Shall ye hit or shall ye stand? (hit/stand) ")

            if user_input == 'hit':
                hit()
                break
            elif user_input == 'stand':
                stand()
                break

    elif choice == "drunk":
        reply = requests.get('https://official-joke-api.appspot.com/jokes/ten')

        jokes = json.loads(reply.content)

        joke = random.choice(jokes)
        opening_line = [
        'Hey... hey buddy I got a joke for ya...',
        'Hey pal listen to this one...',
        'Ay man I got a funny one...',
        'BUUUURP sorry about that, wanna hear a joke?',
        'BUUUUURP'
        ]
        random_line = random.choice(opening_line)
        print(random_line)
        print(joke['setup'])
        input("You wanna hear the punchline? (Press enter)")
        print(joke['punchline'])
        play_again()

    elif choice == "bad":

        print("You've been lookin' at me funny this whole game. I'm thinking of a number between 1 and 20.")
        print("You guess which number I'm thinkin' of within 3 tries, you live, otherwise...")
        print("You die.")
        random_number = random.randint(1, 15)
        for i in range(3):
                
            guess = int(input("What's your guess? "))
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
        
