
import math
import random
import os, sys


# Define Classes

class Hand(object):

    def __init__(self, ncards=2, holecard=False):
        self.cards = []
        self.hiddencard = []
        self.number_of_cards = ncards
        self.visible_cards = ncards
        for i in range(self.visible_cards):
            self.cards.append(draw_card())
        self.cardranks = {
            '0': "A",
            '1': "2",
            '2': "3",
            '3': "4",
            '4': "5",
            '5': "6",
            '6': "7",
            '7': "8",
            '8': "9",
            '9': "10",
            '10': "J",
            '11': "Q",
            '12': "K"
        }
    def __str__(self):
        handstr = ""
        for card in self.cards:
            rank = str(card % 13)
            suit = str(card // 13)
            handstr += u"{} ".format(self.cardranks[rank])
        return handstr

    def add_card(self, newcard):
        self.number_of_cards += 1
        self.visible_cards += 1
        self.cards.append(newcard)

    def reveal_cards(self):
        self.cards.extend(self.hiddencard)
        self.visible_cards += len(self.hiddencard)
        self.hiddencard = []

    def value(self):
        "Samtalið af því sem þú drógst"
        handvalue = 0
        for card in sorted(self.cards, reverse=True):
            rank = card % 13
            if rank > 0:
                handvalue += min(10, rank + 1)
            elif handvalue + 11 > 21:
                handvalue += 1
            else:
                handvalue += 11
        return handvalue


# Define auxiliary functions
def draw_card():
    "Dregur random spil"
    return random.randrange(0, 52)


def draw_initial_hands(dealerholecard=False):
    "Dregur spilinn fyrir dealer og fyrstu 2 cards hjá player"
    return Hand(holecard=dealerholecard), Hand()




def bet(player_money):
    while True:
        bet_str = input("Hversu mikið viltu veðja? [500-" + str(player_money) + "]\n")
        try:
            bet = int(bet_str.strip())
        except ValueError:
            print("Þú settir ekki inn tölu\n")
        else:
            if bet > player_money:
                print("Þú ert ekki með nóg pening til að gera þetta.\n")
                continue
            elif bet < 500:
                print("Þú verður að veðja meira minnst 500\n")
                continue
            else:
                return bet
    return bet


def play_round(money_left):
    bet_value = 0
    bet_value += bet(money_left)
    DealerHand, PlayerHand = draw_initial_hands()
    print("Dealerinn er með:\n", DealerHand)
    print("Þú ert með:\n", PlayerHand)
    if PlayerHand.value() == 21:
        print("Þú fékkst Blackjack! 21!")
        player_blackjack = True
    else:
        player_blackjack = False

    while True:
        chosen_action = input("Hvað viltu gera, H fyrir Hit, S fyrir Stand\n")
        if chosen_action in ["H", "h"]:
            PlayerHand.add_card(draw_card())
            print("Þú ert með:\n", PlayerHand)
            print("Samtals: {} \n".format(PlayerHand.value()))
            if PlayerHand.value() > 21:
                print("Þú fékkst yfir 21 og Bustaðir\n")
                return False, bet_value
            else:
                continue

        elif chosen_action in ["S", "s"]:
            yourhand = PlayerHand.value()
            break
        else:
            print("Notaðu annað hvort H eða S til að velja.\n")
            continue
    # Resolve Dealer
    DealerHand.reveal_cards()
    print("Dealerinn er með:\n", DealerHand)
    if DealerHand.value() == 21:
        print("The dealer has a Blackjack")
        if player_blackjack:
            print("Þið fenguð bæði Blackjack, jafntefli.")
            return True, 0
        else:
            print("Þú tapaðir þessum leik")
            return False, bet_value
    while DealerHand.value() < 17:
        print("Dealerinn dregur úr stokkinum")
        DealerHand.add_card(draw_card())
        print("Dealerinn er núna með:\n", DealerHand)
    if DealerHand.value() > 21:
        print("Dealerinn fékk yfir 21 og Bustaði.\n")
        return True, bet_value
    else:
        if yourhand > DealerHand.value():
            print("Þú vannst þennan leik")
            if player_blackjack:
                return True, math.floor(1.5 * bet_value)
            else:
                return True, bet_value
        else:
            print("Þú tapaðir þessum leik")
            return False, bet_value
    print("wrong end")
    return False, bet_value


# main()
def main():
    holecards = False
    player_money = 50000

    nround = 1
    print("Round", nround)
    while player_money > 500 and player_money < 150000:

        print("Þú er með " + str(player_money) + " pening")
        win, bet = play_round(player_money)
        if win:
            player_money += bet
        else:
            player_money -= bet
        nround += 1
    if player_money < 150000:
        print("Þú ert orðinn blankur, þú tapaðir leikinn. Reyndu Aftur.")
    else:
        print("Þú náðir yfir 150000 og vannst leikinn, Bankinn Sprakk")

    return


if __name__ == '__main__':
    try:
        main()
        sys.exit(0)
    except KeyboardInterrupt as e:  # Ctrl-C
        raise e
    except SystemExit as e:  # sys.exit()
        raise e
    except Exception as e:
        print('ERROR, UNEXPECTED EXCEPTION')
        print(str(e))
        os._exit(1)