import random
import time
import math

x = input('Enter you name: ') #Intro information on data being used about player
print()
time.sleep(3)
print('Now be careful this next input will determine how long you are able to survive in the game.')
print()
time.sleep(2)
y = int(input('Enter your age: '))
print()
time.sleep(4)
print('Well good luck ' + x + ', stay on top of your toes and you might just do all right.')
time.sleep(2)
print('Initiating game')
time.sleep(2)
print()
time.sleep(2)   #print and sleep statements added for suspense, make game flow smoothly while player can enjoyably read through each sentence
print()
time.sleep(2)
print()
time.sleep(2)
print()

def gameintro(): #gameintro lets you decide your path, starts you off with age, kills off people who choose first option
    print ('Welcome ' + x + ' to my game, NextGen!')
    time.sleep(2)
    print('If you dare to play you will be put up against the ultimate test, risking your age for success!')
    time.sleep(2)
    sure = input('This is your last chance to enter the game, if your truly want to play then type yes: ' )
    if sure == 'yes':
        time.sleep(2)
        print('Hahahahahahahah, I hope you have just realized what you have done')
        print()
        time.sleep(2)
        print('There is no going back now')
        print()
        time.sleep(4)
        print('I will show mercy and give you at least some bit of choosing')
        time.sleep(2)
        print('Before you are thrown into a world you will never escape from alive.')
        time.sleep(2)
        print()
        global c
        c = input('Now choose your social class: 1. Lower class, however you are nice and thoughtful, 2. middle class but you cursed with jelously, 3. rich and stressed aka your hair is gray at 20 (input the number of your option): ')
        #each option classified as number so user can easily enter string
        time.sleep(5)
        print("Well congratulations, your life has begun, be careful what you wish for!")
        print("Your world is being generated now")
        print('.')
        print('.')
        print('.')
        print("Let's see where you ended up")
        time.sleep(4)
        if c == "1":
            print('Humbleness is not often rewarding, sorry but you died of hunger, if you would like to play again please restart the program.')
            time.sleep(2)
            print('Goodbye')
            time.sleep(2)
            exit()
     
        if c == "2":
            print('Did you choose this path simply because you felt it was not extreme? ')
            time.sleep(4)
            print('Well I will give you some credit for thinking about your response.')
            time.sleep(4)
            print('I will add 5 years to your life.')
            time.sleep(4)
            global newage
            newage = int(y-5)               #if player does well years are subtracted indicating that they are younger whwreas adding age takes them closer to death
            print()
            time.sleep(4)
            print('You are now ' + str(newage) + ' years old.')

        if c == '3':
            print('Well, I am glad you want to be rich, but you know that you are going to take a hit for this.')
            time.sleep(5)
            print("But you already expected that didn't you, you think you will take a head start and will be able to beat me")
            print('Well you are wrong! You shall now have 20 years added on to your life')
            newage = int(y + 20)
            time.sleep(4)
            print()
            print ('You are now ' + str(newage) + ' years old.')
            

            if newage < 50:                                         #age is below certain threshold, different prompts are displayed
                print('Well it seems you are still in a healthy state.')
                time.sleep(3)
                print('You are lucky, a couple more years and you might need life support.')
                time.sleep(4)
                print('But with your wealth you can afford it so maybe things will work out for you.')
           
            else:
                print('I tried to warn you')
                time.sleep(3)
                print('You should have been wiser choosing or your age')
          
    else:
        exit()

    return(newage)

