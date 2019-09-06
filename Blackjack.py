from random import randrange
import time


def main():
    cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "King", "Queen"]

    cardvalue10 = {
        "Jack": 10,
        "King": 10,
        "Queen": 10,
    }

    print("█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
    print("█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█")
    print("█░░║║║╠─║─║─║║║║║╠─░░█")
    print("█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█")
    print("█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█")

    print("To The Barj's Blackjack!\n")
    print("You start with 10 Gold, you WIN if you can make 70 Gold!\n")
    gold = 10

    while gold > 0:
        print("You currently have ", gold, " gold, you win if you can make 70 Gold!\n")
        while True:
            try:
                bet = int(input("Please enter how much you would like to bet: "))
                while bet < 1 or bet > gold:
                    bet = int(input("Please enter a valid amount: "))
            except:
                print("Please enter a valid amount")
            else:
                break

        print("You have bet ", bet, " gold\n")
        print("The Dealer is shuffling the cards...\n")
        time.sleep(2)

        dealervalue = 0
        uservalue = 0

        dealerrandomint1 = randrange(13)
        dealerrandomint2 = randrange(13)
        userrandomint1 = randrange(13)
        userrandomint2 = randrange(13)

        dealercards = [cards[dealerrandomint1], cards[dealerrandomint2]]
        usercards = [cards[userrandomint1], cards[userrandomint2]]

        dealercopy = convert(dealercards)
        usercopy = convert(usercards)
        usercopy = acecheckconvert(usercopy)
        dealercopy = acecheckconvert(dealercopy)

        print("You are dealt ", usercards[0], " and ", usercards[1], "\n")
        print("The Dealer has dealt himself X and ", dealercards[0], "\n")

        if sum(dealercopy) == 21 and sum(usercopy) == 21:
            print("You both got blackjack, you get your money back this round! \n")
        elif sum(dealercopy) == 21:
            print("The dealer got Blackjack, sorry - bet again!\n")
            gold = gold - bet
        elif sum(usercopy) == 21:
            print("You got Blackjack! Well done - please bet again\n")
            gold = gold + bet
        else:
            count = 1
            secondcard = False

            usercopy = convert(usercards)
            usercopy = acecheckconvert(usercopy)
            usersum = sum(usercopy)

            hit = input("Hit or Stick? ( h/s): \n")
            while (hit == "h") and (usersum < 21):
                count = count + 1

                print("You are being dealt another card...\n")
                time.sleep(1.5)
                usernewcard = cards[randrange(13)]
                usercards.append(usernewcard)
                usercopy = convert(usercards)
                usercopy = acecheckconvert(usercopy)
                print("You were dealt a ", usercards[count])
                if secondcard == False:
                    print("The dealers second card was a ",dealercards[1], "\n" )
                    time.sleep(1.5)
                    secondcard = True


                usersum = sum(usercopy)
                if (usersum < 21):
                    hit = input("Hit or Stick? ( h/s): \n")

            dealercount = 2

            if secondcard == False:
                print("The dealers second card was a ", dealercards[1], "\n")
                time.sleep(1.5)
                secondcard = True


            while sum(dealercopy) < 17:
                print("The dealer is dealing himself another card...\n")
                time.sleep(1.5)
                dealernewcard = cards[randrange(13)]
                dealercards.append(dealernewcard)
                dealercopy = convert(dealercards)
                dealercopy = acecheckconvert(dealercopy)
                print("The dealer was dealt a ", dealercards[dealercount], "\n")
                dealercount = dealercount + 1

            if sum(usercopy) > 21:
                print("You went bust! Sorry you lost your money - please bet again!\n  ")
                gold = gold - bet
            elif (sum(dealercopy) > 21) and sum(usercopy) < 21:
                print("The dealer went bust! Well done, you won this round - please bet again\n")
                gold = gold + bet
            elif sum(dealercopy) > sum(usercopy):
                print("You lost this round! Sorry - please bet again!\n  ")
                gold = gold - bet
            elif sum(dealercopy) <  sum(usercopy):
                print("You won this round! - please bet again\n")
                gold = gold + bet
            elif sum(dealercopy) == sum(usercopy):
                print("You both had the same score! The dealer wins - please bet again")
                gold = gold - bet

    if gold < 1:
        time.sleep(1.5)
        print("Sorry, you're out of gold!")

    elif gold > 69:
        time.sleep(1.5)
        print("You won!")


def convert(list=[]):
    newlist = list
    index = 0
    for index in range(len(list)):
        if (newlist[index] == "Jack") or (newlist[index] == "King") or (newlist[index] == "Queen"):
            newlist[index] = 10
        if "Ace" == newlist[index]:
            newlist[index] = 11


        index = index + 1
    return newlist

def acecheckconvert(list=[]):
    index = 0
    if sum(list) > 21:
        for x in list:
            if list[index] == 11:
                list[index] = 1
        index += index

    return list


main()


