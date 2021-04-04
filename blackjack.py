import random
#global values
suits = ('Hearts','Dimonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {"Two":2,"Three":3 , "Four":4 , "Five":5 , "Six":6 , "Seven":7,"Eight":8,"Nine":9 , "Ten":10 , "Jack":10 , "Queen":10 , "King":10 , "Ace" : 11}
class Cards:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + " of " + self.suit
class Deck:
    def __init__(self):
        self.deck_list = []
        for suit in suits:
            for rank in ranks:
                new_card = Cards(suit,rank)
                self.deck_list.append(new_card)
    def shuffle(self):
        random.shuffle(self.deck_list)
    def deal_one_card(self):
        return self.deck_list.pop()

class Player:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def add_balance(self,add):
        self.add = add
        self.balance = self.balance + self.add
    def sub_balance(self,sub):
        self.sub = sub
        self.balance = self.balance - self.sub
    def __str__(self):
        return "Hello "+ self.name +" you are left with  " +str(self.balance) +" $ in you account "
def sumup_total(my_list):
    sumup = 0
    for each_element in my_list:
        sumup = sumup + each_element.value
    return sumup
def change_ace_value():
  for each_element in range(len(player_cards)):
        if player_cards[each_element].rank == 'Ace' and sumup_total(player_cards) > 21:
            player_cards[each_element].value = 1
        elif player_cards[each_element].rank == 'Ace' and sumup_total(player_cards) < 21:
            player_cards[each_element].value = 11
        else:
            pass
  for each_element in range(len(dealer_cards)):
        if dealer_cards[each_element].rank == 'Ace' and sumup_total(dealer_cards) > 21:
            dealer_cards[each_element].value = 1
        elif dealer_cards[each_element].rank == 'Ace' and sumup_total(dealer_cards) < 21:
            dealer_cards[each_element].value = 11
        else:
            pass
          
def play_games(my_list):
    change_ace_value()
    sumup = 0
    for each_element in my_list:
        sumup = sumup + each_element.value
    return sumup
def print_dealer_cards(my_list):
    print("Dealer Cards are - \n")
    for each_element in range(len(dealer_cards)):
        print(dealer_cards[each_element])
play_game = True
player_cards =[]
dealer_cards =[]
fresh_deck = Deck()
fresh_deck.shuffle()
dealer = Player("Dealer",1000000)
'''print(dealer)'''
player_name = input("\nWhat is you name - ")
player_balance = int(input("How much money do you have - "))
bet = int(input("How Much Money do you want to bet : "))
new_player = Player(player_name,player_balance)
def start_game():
  print(new_player)
  print("Here are your two cards")
  for x in range(2):
    player_cards.append(fresh_deck.deal_one_card())
    dealer_cards.append(fresh_deck.deal_one_card())
    print("\n\t{}".format(player_cards[x]))
  print("\nMy Cards is\n\t{}".format(dealer_cards[x]  ))
  player_cards_sum = play_games(player_cards)
  print("\nyour cards value is {}".format(player_cards_sum))
if bet <= new_player.balance:
  print("You have Sufficent Money , you can play ")
  new_player.sub_balance(bet)
  start_game()
  pass
else :
  print("You Dont have Enough Money ")
  play_game = False
while play_game:
    choice = int(input("\nEnter\n1.Deal one card\n2.To Show\n"))
    if choice == 1:
        player_cards.append(fresh_deck.deal_one_card())
        print("Now you have cards ")
        for each_element in range(len(player_cards)):
            print(player_cards[each_element])
        player_cards_sum = play_games(player_cards)    
        print("\nyour cards value is {}".format(player_cards_sum))
        if(player_cards_sum >21):
            print("Player lost your money ")
            print_dealer_cards(dealer_cards)
            dealer_cards_sum = play_games(dealer_cards)
            print("Dealer cards value is - {}".format(dealer_cards_sum))
            print(new_player)
            play_game = False
            break
        else:
            continue
    elif choice == 2:
        while play_games(dealer_cards) < 17:
            dealer_cards.append(fresh_deck.deal_one_card())
                
        if play_games(dealer_cards) >= 17: 
            if play_games(dealer_cards) > 21:
                print("Player won the Money ")
                new_player.add_balance(2*bet)
                print_dealer_cards(dealer_cards)
                dealer_cards_sum = play_games(dealer_cards)
                print("Dealer cards value is - {}".format(dealer_cards_sum))
                print(new_player)
                play_game = False
                break
                
            elif play_games(dealer_cards) > play_games(player_cards) and play_game(dealer_cards) <= 21:
                print("Player lost the money")
                print_dealer_cards(dealer_cards)
                dealer_cards_sum = play_games(dealer_cards)
                print("Dealer cards value is - {}".format(dealer_cards_sum))
                print(new_player)
                play_game = False
                break
            elif play_games(dealer_cards) <= play_games(player_cards) and play_game(player_cards) <= 21 :
                print("Player won the money ")
                new_player.add_balance(2*bet)
                print_dealer_cards(dealer_cards)
                dealer_cards_sum = play_games(dealer_cards)
                print("Dealer cards value is - {}".format(dealer_cards_sum))
                print(new_player)
                play_game = False
                break
            else:
                break
    else:
        print("Wrong Input try again please")
        continue 
        
play_game = False
