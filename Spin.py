from random import randint

#Starting values
money = 1500
ticket = 0
winning_number = randint(1111, 9999)


class Main(object):
    def __init__(self):
       Main.enter()

    def enter():
        while money >= 50 or ticket != 0: #to check if player has enough tickets or money to continue the game
            print("--$$$---Lottery---$$$--"*3)
            Main.buy_menu()
            Main.lottery()

    def buy_menu():
        global money #without global keyword changing values inside function is not possible
        global ticket #ticket is a global variable
        if money >= 50: #check if there is enough money to buy tickets
            buy = int(input(f"Enter number of Tickets you will like to buy ? Your balance is {money} $. One Ticket costs 50$ ."))
            if buy*50 <= money: #check to avoid extra tickets
                money = money - buy*50
                ticket = ticket + buy
                print(f"You Have {ticket} tickets and a balance of ${money} ")
            else:
                print("No Cheating")

    def lottery():
        global money
        global ticket
        global winning_number
        if ticket > 0: #run if tickets available
            while ticket > 0: #runs until all purchased tickets run out
                print("Time to see your Luck!")
                spin = input("=>> press enter to spin") #allows player to spin 
                result = randint(1111, 9999) #random ticket numbers
                print(f"Your Ticket number is {result} and the winning number is {winning_number} ")
                ticket = ticket - 1 #remove used tickets
                if winning_number == result: #to determine if player won
                    print(f"=>> You Have won the JackPot .... Congrats on the $1000000 ... Tickets Left {ticket}")
                    money += 1000000
                else:
                    print(f"==> Better Luck next Time.. Tickets Left {ticket} ")
                
