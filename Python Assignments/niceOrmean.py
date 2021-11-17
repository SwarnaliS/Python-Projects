#Python version 3.9.7
# Author: Swarnali Satpathy
#Purpose: To write a code to build a nice or mean game, 
#         as a pert of Tech Academy's Python course.

import winsound

def start(nice=0,mean=0,name=""):
    #get user's name
    name=describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    if name!= "":
        print ('\nThank you for playing again, {}'.format(name))
    else:
        go = True
        while go:
            if name == "":
                name= input ('\nWhat is your name?\n>>>').capitalize()
                if name!= "":
                    print('\nWelcome, {}!'.format(name))
                    go = False
    return name
def nice_mean(nice,mean,name):
    go= True
    while go:
        show_score(nice,mean,name)
        pick = input('\nA stranger approaches you for a conversation\nWill you be nice or mean?\n(n/m) \n>>>').lower()
        if pick == 'n':
            winsound.PlaySound("gameSound.wav",winsound.SND_ASYNC)
            print('\nThe stranger walks away similing....')
            nice = (nice+1)
            go=False
        if pick =='m':
            winsound.PlaySound("gameSound.wav",winsound.SND_ASYNC)
            print('\nThe stranger glares at you \nmenacingly and storms off...')
            mean= (mean+1)
            go= False
    score(nice,mean,name)
def show_score(nice,mean,name):
    print('\n{}, Your current total: \n({}nice) and ({}mean)'.format(name,nice,mean))

def score(nice,mean,name):
    if nice>2:
        win(nice,mean,name)
    if mean>2:
        lose(nice,mean,name)
    else:
        nice_mean(nice,mean,name)
def win(nice,mean,name):
    print ('\nNice job {}! You win!'.format(name))
    again(nice,mean,name)
def lose(nice,mean,name):
    print('\nSorry {}, you lost the game this time'.format(name))
    again(nice,mean,name)

def again(nice,mean,name):
    go= True
    while go:
        choice = input('\nDo you want to play again? (y/n):\n>>>').lower()
        if choice == "y":
            go=False
            reset(nice,mean,name)

        if choice == 'n':
            print('\nSorry to see you go!')
            go= False
            quit()
        else:
            print("\nPlease enter y for yes, and n for no:\n>>>")
def reset(nice,mean,name):
    nice=0
    mean=0
    start(nice,mean,name)









if __name__ == '__main__':
    start()
