import Spin 
from random import randint
from sys import exit

class Start(object):
    
    def __init__(self):
        Start.play()  #calling play function from class Start  

    def play():
        Spin.Main()   #calling class main in Spin.py 
        End()         #End Game
        

        
class End(object):
    def __init__(self):
        print("You Have Lost Your Money !!! GAME OVER !!!!")
        exit(1)

Start()  #Start Game
