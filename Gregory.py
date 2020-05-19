#Gregory Tolmochow
#Computer Science Final Project 
#May 19, 2020

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

def check(): #allows me to store global variable
    gameintro()
    print(newage)
    print(c)

print()

def billy(): #new setting in which player is given more options to choose different situations that alter age
    time.sleep(8)
    print()
    time.sleep(7)
    print('Meet your bestfriend Billy')
    time.sleep(3)
    print()
    print('He knows the ins and outs of these parts and will help guide you to makeing the best life possible for yourself.')
    time.sleep(3)
    print('You and Billy are taking a stroll through the streets and')
    time.sleep(3)
    print('BOOM!')
    time.sleep(3)
    print()
    print('WACK!')
    time.sleep(2)
    print()
    print('Billy is jumped by the local gang, it is your time to prove yourself!')
    time.sleep(3)
    print('Are you going to risk your life and fight back or let him potentially die, therefore losing your connections throughout the city')
    fight = input('fight or watch: ')
    if fight == 'fight':
        time.sleep(4)
        print('Well here you go...')
        time.sleep(2)
        print('BANG!')
        print()
        time.sleep(2)
        print('BONG!')
        print()
        time.sleep(3)
        print('You saved Billy and you only got a black eye, you are rewarded 10 years of extra life.')
        global newage2
        newage2 = int(newage - 10)
        time.sleep(3)
        print()
        print('You are now ' + str(newage2) + ' years old.')
    else:
        time.sleep(3)
        print('Billy dies. You are then beat up by the gang and suffer from PTSD.')
        time.sleep(3)
        print('Because of the trauma 30 years is added to your life.')
        newage2 = int(newage + 30)
        time.sleep(3)
        print()
        print('You are now ' + str(newage2) + 'years old.')
    
    return(newage2)

print()

def check2(): #global variable usage
    billy()
    print(newage2)

print()

def checkage(): #if age is below 0 you have effectively become too young because you chose too small of an age, game will not make sense with negative age
    if int(newage2) < 0: 
        print('Sorry but you have died, you have chosen too many correct answers and therefore the game has ended.')
        print('You can either take this as a personal win or just accept that you should not be playing this game and instead should be studying for the SAT.')
        print('Goodbye')
        exit()

def precan(): #A huge mess that takes players two different routes depending on lifestyle
    if c == "2":
        time.sleep(10)
        print("Oh hey there, I know that while you were recovering in your suburbian home, you were probably looking trough Forbes magaizne wondering how you are going to afford that new Ferrari")
        time.sleep(6)
        print('So you went out the next day to your middle class job and walked in your bosses office')
        time.sleep(4)
        print('You said: Hey boss, I am quitting, today I am going to follow my dreams and the only way I will get there is if I become invested in stocks')
        time.sleep(3)
        print('Your boss: Are you sure about '+ x + ' I will not let you come back if you change your mind')
        time.sleep(3)
        throw = input('You throw your company hat on the ground to show you mean it (yes/no)(just say yes): ')
        print()
        time.sleep(4)
        if throw == "yes":
            print('Your boss: Ohhh man, your gonna get it now')
            print()
            time.sleep(4)
            print("MY MOM SEWED THOSE HATS TOGETHER WITH HER OWN BARE HANDS")
            print()
            time.sleep(3)
            print("PUNCH TO THE FACE")
            print()
            time.sleep(1)
            print("UPPERCUT")
            print()
            time.sleep(1)
            print("JAB")
            print()
            time.sleep(1)
            print("JAB")
            print()
            time.sleep(2)
            print()
            print('You are left squeling on the floor and must now be taken to the hospital.')
            time.sleep(4)
            print ('Your angel above: Great going bud.')
        
            newage3 = int(newage2 + 25)
            time.sleep(7)
            print('After waking up from your insanely long coma....')
            print()
            time.sleep(2)
            print('Your are now ' + str(newage3) + ' years old.')
            time.sleep(4)
            print('You smack yourself in the face in shame')
            
            newage4 = int(newage3 + 1)
            print()
            time.sleep(5)
            print('You are now ' + str(newage4) + ' years old')
        
        print('You now take all your savings and invest them in the Marriot Hotel chain')
        time.sleep(3)
        print()
        print('But it is the year 2020 so the world is strcuk with a pandemic called Modelo')
        print()
        time.sleep(2)
        print('The entire travel industry crashes and you literally left with no hair afterwards')
        time.sleep(3)
        hair = input("Do you want to buy a wig to show that you were not affected by the crash (yes/no): ") 
        if hair == "no":
            print('You die of shame')
            print()
            time.sleep(3)
            print("It is a real thing, trust me.")
            print()
            time.sleep(3)
            print("Now you will be bald in heaven too")
            time.sleep(2)
            print()
            print('Goodbye')
            time.sleep(3)
            exit()
        else:
            time.sleep(2)
            print()
            print("Well all the stores had left was a red Annie wig, so now people will not even hire you")
            time.sleep(3)
            print("You are probably waiting for me to tell you what your new age is, right? ")
            time.sleep(2)
            print("Well, you are in luck, I will make this a bit more fun for you")
            time.sleep(2)
            wheel = input("Pick a number between 1 and 2 (1/2): ")
            time.sleep(3)
            print("Good, because if you were going to complain about your huge variety of options I was going to boot you")
            if wheel == "1":
                print("Well, I don't know what to tell you dude")
                time.sleep(3)
                print("You really keep picking the worst of the worst")
                time.sleep(5)
                print("You're dead")
                time.sleep(2)
                print("Later :(")
                time.sleep(7)
                print("Sike, your still alive")
            else:
                print ("Ya so if you picked the other number, you would have been fine")
                time.sleep(4)
                print ("But you didn't")
                time.sleep(4)
                print("Wanna guess your age?")
                guess = int(input("Guess between 50-100: "))
                global newage5
                newage5 = int(guess/4 + newage4)
                time.sleep(4)
                print("Well, to be honest you could have either killed yourself or just added a few digits to your already demised life")
                time.sleep(6)
                print("Let's see, shall we")
                print()
                time.sleep(3)
                print('You are now '+ str(newage5)+ ' years old')
                
    if c == "3": #path 2 if you chose option 3
        print('So you are rich right?')
        time.sleep(4)
        print('Exatly, so after the fight you drop a couple million on a new police station to help combat the crime.')
        time.sleep(4)
        print('You are declared human of the year by Clock Magaizne and are asked to travel the world.')
        time.sleep(4)
        print('Eager to meet world leaders, you hop on your plane and leave.')
        time.sleep(4)
        print('However, you left your wife and kids at home will not be able to see them for a year.')
        time.sleep(4)
        print('Your wife wants to divorce and you have a nervous breakdown.')
        time.sleep(4)
        print('You are rushed to a hospital in Mumbai, India where your surgeon Marshall Olomos is taked with saving ur life.')
        time.sleep(4)
        print('You stress even more because you realize last second that...')
        time.sleep(6)
        print('You used to bully Marshall in highschool and now your life is in his hands')
        time.sleep(2)
        print()
        time.sleep(2)
        print()
        time.sleep(2)
        print()
        print('You wake up feeling new again but your attack caused you to gain 25 years on your life.')
        newage5 = int(newage2 + 40)
        print()
        time.sleep(3)
        print("You are now "+ str(newage5)+ " years old.")
    
    return(newage5)


def check3(): #enables global
    precan()
    print(newage5)


def checkage6(): #checks for potential age limit which would result in you death if you passed 100 years
    if int(newage5)>100:
        print('After that last setting, you probably saw this coming.')
        time.sleep(7)
        print()
        print('Sorry but are now in the afterlife.')
        time.sleep(4)
        print('You, the one and only '+ x + ' survived to be '+ str(newage5) + ' years old.')
        time.sleep(4)
        print('Well done, please try again if you like to suffer.')
        print()
        time.sleep(7)
        print ('Goodbye')
        time.sleep(2)
        exit()
            

print()

def cointoss(): #new situation which gives you option to gamble
    time.sleep(10)
    print("You have reached Billy's friend's cantina.")
    time.sleep(3)
    print('Congratulations, this is a chance for you to earn back some years in your tragic life')
    time.sleep(5)
    print('Billy welcomes you to the back door')
    time.sleep(2)
    answerbilly = input('Do you wish to follow your best friend Billy (yes/no): ')
    if answerbilly == 'yes':
        time.sleep(1)
        print('Billy: I am glad you are coming, what I have to show you can be life changing')
        time.sleep(4)
        print('Billy: This is the notorious Ryan Lin, he owns all the underground gambling venues throughout the city')
        time.sleep(4)
        print('Billy: Hey ' + x + '! Take a shot, it is simple, you either choose 1. heads or 2. tails')
        time.sleep(2)
        coin = input('What side do you want (1/2): ')
    else:
        print('You died because you failed to take a risk in life')
        time.sleep(4)
        print('Goodbye')
        time.sleep(3)
        exit()

print()

def choosepath(path): #takes in input from last function to give different options
    

    correctClass = random.randint(1, 2) #Uses random to give true representation of coin toss

    if path == str(correctClass): #if you got correct number then it only adds 10 years
        time.sleep(4)
        print ('Well you chose wisely, unfortunetly the odds are in your favor and you have reached the end of the road.')
        time.sleep(4)
        print("Because you participated in illegal gambling, I will have to add 10 years..")
        time.sleep(3)
        print('Hopefully it does not kill you.')
        global finalage
        finalage = int(newage5 + 10)
        print()
        time.sleep(3)
        print ("You have passed through my entire simulation with your final age as "+ str(finalage)+ " years old.")
    else: #losing bet reults in 40 years added
        print ('Sorry, but the real world is tuff...')
        time.sleep(2)
        print ('Only the strongest and most able minds survive.')
        finalage = int(newage5 + 40)
        print()
        print('Because you lost the bet, Ryan takes you to his dungeon where you remain for 40 years.')
        print('You are probably dead, but theoretically you are '+ str(finalage)+ ' years old.')
    
    return(finalage)


def check4(): #enables global
    choosepath()
    print(finalage) 

def checkage3(): #end of game summary, most likely above 100 which is death marker
    if int(finalage) > 100:
        diff = int(finalage - 100)
        print('Sorry, but you barley made it.')
        time.sleep(2)
        print('You went '+ str(diff)+ ' years above your lifespan.')
        time.sleep(3)
        print('It was very fun wasting your precious time, ironically by playing this game it actually is taking time away from your lifespan.')
        time.sleep(4)
        print('So in truth, I awlays win!')
        time.sleep(2)
        print('Goodbye')
        time.sleep(3)


playAgain = "yes" #Once you get to the end of game summary you are then asked if you want to play again which will run all the functions through again keeping your original age and name
while playAgain == "yes" or playAgain == "y": 
    gameintro()
    billy()
    checkage()
    precan()
    checkage6()
    choice = cointoss() 
    choosepath(choice)
    checkage3()
    playAgain = input("If you would like to attempt to find an alternate outcome. ignroing the fact that your future is destined, then please yes or y to continue: ")
