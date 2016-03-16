balance = 1000.00
rake = 0.00
hand_counter = 1
choice = ''
import random
from tkinter import *
game = Tk()
info = Label(text="Hand #"+str(hand_counter)+" Bankroll: "+str(balance)+"$"+" Rake: "+str(rake.__round__(2))+"$",fg="blue")
info.place(x=166,y=0)
position = ["You post 5$ SB","You post 10$ BB"]
position_widget = Label(text=position[hand_counter%2],fg="blue")
position_widget.place(x=166,y=20)
deck = ['2s','3s','4s','5s','6s','7s','8s','9s','Ts','Js','Qs','Ks','As','2h','3h','4h','5h','6h','7h','8h','9h','Th','Jh','Qh','Kh','Ah',
        '2c','3c','4c','5c','6c','7c','8c','9c','Tc','Jc','Qc','Kc','Ac','2d','3d','4d','5d','6d','7d','8d','9d','Td','Jd','Qd','Kd','Ad',]
hero_left_card = deck[random.randrange(len(deck))]
deck.remove(hero_left_card)
hero_left_card_widget = PhotoImage(file="deck/"+hero_left_card+".gif")
hero_right_card = deck[random.randrange(len(deck))]
deck.remove(hero_right_card)
hero_right_card_widget = PhotoImage(file="deck/"+hero_right_card+".gif")
opp_left_card = deck[random.randrange(len(deck))]
deck.remove(opp_left_card)
opp_left_card_widget = PhotoImage(file="deck/"+opp_left_card+".gif")
opp_right_card = deck[random.randrange(len(deck))]
deck.remove(opp_right_card)
opp_right_card_widget = PhotoImage(file="deck/"+opp_right_card+".gif")
def get_hand():
    global deck,hero_left_card,hero_right_card,hero_left_card_widget,hero_right_card_widget,opp_left_card,opp_right_card,opp_left_card_widget,opp_right_card_widget
    deck = ['2s','3s','4s','5s','6s','7s','8s','9s','Ts','Js','Qs','Ks','As','2h','3h','4h','5h','6h','7h','8h','9h','Th','Jh','Qh','Kh','Ah',
            '2c','3c','4c','5c','6c','7c','8c','9c','Tc','Jc','Qc','Kc','Ac','2d','3d','4d','5d','6d','7d','8d','9d','Td','Jd','Qd','Kd','Ad',]
    hero_left_card = deck[random.randrange(len(deck))]
    deck.remove(hero_left_card)
    hero_left_card_widget = PhotoImage(file="deck/"+hero_left_card+".gif")
    hero_right_card = deck[random.randrange(len(deck))]
    deck.remove(hero_right_card)
    hero_right_card_widget = PhotoImage(file="deck/"+hero_right_card+".gif")
    opp_left_card = deck[random.randrange(len(deck))]
    deck.remove(opp_left_card)
    opp_left_card_widget = PhotoImage(file="deck/"+opp_left_card+".gif")
    opp_right_card = deck[random.randrange(len(deck))]
    deck.remove(opp_right_card)
    opp_right_card_widget = PhotoImage(file="deck/"+opp_right_card+".gif")
    global back,HeroHandLeft,HeroHandRight,BoardFlopLeft,BoardFlopCenter,BoardFlopRight,BoardTurn,BoardRiver,OppHandLeft,OppHandRight
    HeroHandLeft.config(image=hero_left_card_widget)
    HeroHandRight.config(image=hero_right_card_widget)
    BoardFlopLeft.config(image=back)
    BoardFlopCenter.config(image=back)
    BoardFlopRight.config(image=back)
    BoardTurn.config(image=back)
    BoardRiver.config(image=back)
    OppHandLeft.config(image=back)
    OppHandRight.config(image=back)
def gamble(event):
        global balance,hand_counter,rake,deck,hero_left_card,hero_right_card,opp_left_card,opp_right_card,opp_left_card_widget,opp_right_card_widget,flop_left_widget,flop_center_widget,flop_right_widget,turn_widget,river_widget
        global BoardFlopLeft,BoardFlopCenter,BoardFlopRight,BoardTurn,BoardRiver,OppHandLeft,OppHandRight
        flop_left = deck[random.randrange(len(deck))]
        deck.remove(flop_left)
        flop_center = deck[random.randrange(len(deck))]
        deck.remove(flop_center)
        flop_right = deck[random.randrange(len(deck))]
        deck.remove(flop_right)
        turn = deck[random.randrange(len(deck))]
        deck.remove(turn)
        river = deck[random.randrange(len(deck))]
        deck.remove(river)
        flop_left_widget = PhotoImage(file="deck/"+flop_left+".gif")
        flop_center_widget = PhotoImage(file="deck/"+flop_center+".gif")
        flop_right_widget = PhotoImage(file="deck/"+flop_right+".gif")
        turn_widget = PhotoImage(file="deck/"+turn+".gif")
        river_widget = PhotoImage(file="deck/"+river+".gif")
        BoardFlopLeft.config(image=flop_left_widget)
        BoardFlopCenter.config(image=flop_center_widget)
        BoardFlopRight.config(image=flop_right_widget)
        BoardTurn.config(image=turn_widget)
        BoardRiver.config(image=river_widget)
        OppHandLeft.config(image=opp_left_card_widget)
        OppHandRight.config(image=opp_right_card_widget)
        combinations_name = ["High Card","One Pair","Two Pair","Three of a Kind","Straight","Flush","Full House","Four of a Kind","Straight Flush"]
        combinations_value = ["Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Ace"]
        hero_combination_output = "Hero has "
        opp_combination_output = "Opp has "
        results = ["","Hero","Opp","Split pot, "," wins 191$, ","rake 9$"]
        result_output = ""
        hero_seven_cards_value = [hero_left_card[0],hero_right_card[0],flop_left[0],flop_center[0],flop_right[0],turn[0],river[0]]
        hero_seven_cards_suit = [hero_left_card[1],hero_right_card[1],flop_left[1],flop_center[1],flop_right[1],turn[1],river[1]]
        opp_seven_cards_value = [opp_left_card[0],opp_right_card[0],flop_left[0],flop_center[0],flop_right[0],turn[0],river[0]]
        opp_seven_cards_suit = [opp_left_card[1],opp_right_card[1],flop_left[1],flop_center[1],flop_right[1],turn[1],river[1]]
        deck_no_suits = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
        def get_combination(hero_seven_cards_value,hero_seven_cards_suit):
            hero_combination = [0,0,0,0,0,0]
            hero_total_cards = [0,0,0,0,0,0,0,0,0,0,0,0,0]
            for i in range(13): #Fills hero(opp)_total_cards
                for j in hero_seven_cards_value:
                    if j == deck_no_suits[i]:
                        hero_total_cards[i]+=1
            for i in range(13): #Checks for Four of a kind
                if hero_total_cards[i] == 4:
                    hero_combination[0] = 7
                    hero_combination[1] = i
                    j = 12
                    while j >= 0:
                        if hero_total_cards[j] != 4 and hero_total_cards[j] != 0:
                            hero_combination[2] = j
                            break
                        j-=1

            hero_flush = [0,'']
            hero_straight = [0,0]
            hero_total_cards.insert(0,hero_total_cards[12])
            for i in range(10): #Checks for Straight
                if hero_total_cards[i] != 0 and hero_total_cards[i+1] != 0 and hero_total_cards[i+2] != 0 and hero_total_cards[i+3] != 0 and hero_total_cards[i+4] != 0:
                    if i == 9 or i == 8 and hero_total_cards[i+5] != 0 or i == 7 and hero_total_cards[i+5] != 0 and hero_total_cards[i+6] != 0:
                        hero_straight = [1,12]
                    elif i == 7 and hero_total_cards[i+5] != 0:
                        hero_straight = [1,11]
                    elif i < 7 and hero_total_cards[i+5] != 0 and hero_total_cards[i+6] != 0:
                        hero_straight = [1,i+5]
                    elif i < 7 and hero_total_cards[i+5] != 0:
                        hero_straight = [1,i+4]
                    else:
                        hero_straight = [1,i+3]

            del hero_total_cards[0]
            if hero_seven_cards_suit.count('s') >=5 or hero_seven_cards_suit.count('h') >= 5 or hero_seven_cards_suit.count('c') >=5 or hero_seven_cards_suit.count('d') >=5: #Checks for Flush
                if hero_seven_cards_suit.count('s') >=5:
                    hero_flush = [1,'s']
                elif hero_seven_cards_suit.count('h') >= 5:
                    hero_flush = [1,'h']
                elif hero_seven_cards_suit.count('c') >= 5:
                    hero_flush = [1,'c']
                else:
                    hero_flush = [1,'d']

            if hero_flush[0] == 1: #Fills hero(opp)_total_flush_cards
                hero_total_flush_cards = [0,0,0,0,0,0,0,0,0,0,0,0,0]
                for i in range(13):
                    for j in range(7):
                        if hero_seven_cards_value[j] == deck_no_suits[i] and hero_seven_cards_suit[j] == hero_flush[1]:
                            hero_total_flush_cards[i]+=1
            if hero_straight[0] == 1 and hero_flush[0] == 1: #Checks for Straight flush (hero)
                hero_total_flush_cards.insert(0,hero_total_flush_cards[12])
                for i in range(10):
                    if hero_total_flush_cards[i] != 0 and hero_total_flush_cards[i+1] != 0 and hero_total_flush_cards[i+2] != 0 and hero_total_flush_cards[i+3] != 0 and hero_total_flush_cards[i+4] != 0:
                        if i == 9 or i == 8 and hero_total_flush_cards[i+5] != 0 or i == 7 and hero_total_flush_cards[i+5] != 0 and hero_total_flush_cards[i+6] != 0:
                            hero_combination[0] = 8
                            hero_combination[1] = 12
                        elif i == 7 and hero_total_flush_cards[i+5] != 0:
                            hero_combination[0] = 8
                            hero_combination[1] = 11
                        elif i < 7 and hero_total_flush_cards[i+5] != 0 and hero_total_flush_cards[i+6] != 0:
                            hero_combination[0] = 8
                            hero_combination[1] = i+5
                        elif i < 7 and hero_total_flush_cards[i+5] != 0:
                            hero_combination[0] = 8
                            hero_combination[1] = i+4
                        else:
                            hero_combination[0] = 8
                            hero_combination[1] = i+3
                del hero_total_flush_cards[0]

            if hero_total_cards.count(3) > 0 and hero_total_cards.count(2) > 0 or hero_total_cards.count(3) == 2: #Checks for Full house
                i = 12
                hero_combination[0] = 6
                while i >= 0:
                    if hero_total_cards[i] == 3 and hero_combination[1] == 0:
                        hero_combination[1] = i
                    if hero_total_cards[i] == 2 and i >= hero_combination[2] or hero_total_cards[i] == 3 and i < hero_combination[1]:
                        hero_combination[2] = i
                    i-=1

            if hero_combination[0] == 0 and hero_flush[0] == 1: #Write Flush in combination
                hero_combination[0] = 5
                i = 12
                j = 0
                while i >= 0 and j != 5:
                        if hero_total_flush_cards[i] != 0:
                            hero_combination[j+1] = i
                            j+=1
                        i-=1

            if hero_combination[0] == 0 and hero_straight[0] == 1: #Write Straight in combination
                hero_combination[0] = 4
                hero_combination[1] = hero_straight[1]

            if hero_combination[0] == 0 and hero_total_cards.count(3) > 0: #Checks for Three of a kind
                i = 12
                hero_combination[0] = 3
                while i >= 0:
                    if hero_total_cards[i] == 3:
                        hero_combination[1] = i
                        break
                    i-=1
                i = 12
                j = 0
                while i >= 0 and j != 2:
                    if hero_total_cards[i] == 1:
                       hero_combination[j+2] = i
                       j+=1
                    i-=1

            if hero_combination[0] == 0 and hero_total_cards.count(2) >= 2: #Checks for Two pair
                hero_combination[0] = 2
                i = 12
                j = 0
                while i >= 0 and j != 2:
                    if hero_total_cards[i] == 2:
                        hero_combination[j+1] = i
                        j+=1
                    i-=1
                i = 12
                while i >= 0:
                    if hero_total_cards[i] != 0 and i != hero_combination[1] and i != hero_combination[2]:
                        hero_combination[3] = i
                        break
                    i-=1
        
            if hero_combination[0] == 0 and hero_total_cards.count(2) == 1: #Checks for One pair
                hero_combination[0] = 1
                i = 12
                j = 0
                while i >= 0:
                    if hero_total_cards[i] == 2:
                        hero_combination[1] = i
                    elif hero_total_cards[i] == 1 and j != 3:
                        hero_combination[j+2] = i
                        j+=1
                    i-=1

            if hero_combination[0] == 0: #Checks for High card
                i = 12
                j = 0
                while i >= 0 and j != 5:
                    if hero_total_cards[i] == 1:
                        hero_combination[j+1] = i
                        j+=1
                    i-=1
            return hero_combination
        def write_combination(hero_combination):
            hero_combination_output = ""
            if hero_combination[0] == 8 and hero_combination[1] == 12: #Write hero(opp)_combination_output
                hero_combination_output+="Royal Flush"
            else:
                hero_combination_output+=combinations_name[hero_combination[0]] + ", "
            if hero_combination[0] == 4 or hero_combination[0] == 5 or hero_combination[0] == 8 and hero_combination[1] != 12:
                hero_combination_output+=combinations_value[hero_combination[1]] + " High"
            if hero_combination[0] == 1 or hero_combination[0] == 3 or hero_combination[0] == 7:
                if hero_combination[1] != 4:
                    hero_combination_output+=combinations_value[hero_combination[1]] + "s"
                else:
                    hero_combination_output+=combinations_value[hero_combination[1]] + "es"
            if hero_combination[0] == 0:
                hero_combination_output+=combinations_value[hero_combination[1]]
            if hero_combination[0] == 6:
                if hero_combination[1] == 4:
                    hero_combination_output+=combinations_value[hero_combination[1]] + "es full of " + combinations_value[hero_combination[2]] + "s"
                else:
                    if hero_combination[2] == 4:
                        hero_combination_output+=combinations_value[hero_combination[1]] + "s full of " + combinations_value[hero_combination[2]] + "es"
                    else:
                        hero_combination_output+=combinations_value[hero_combination[1]] + "s full of " + combinations_value[hero_combination[2]] + "s"
            if hero_combination[0] == 2:
                if hero_combination[1] == 4:
                    hero_combination_output+=combinations_value[hero_combination[1]] + "es and " + combinations_value[hero_combination[2]] + "s"
                else:
                    if hero_combination[2] == 4:
                        hero_combination_output+=combinations_value[hero_combination[1]] + "s and " + combinations_value[hero_combination[2]] + "es"
                    else:
                        hero_combination_output+=combinations_value[hero_combination[1]] + "s and " + combinations_value[hero_combination[2]] + "s"
            return hero_combination_output
        def compare_combinations(hero_combination,opp_combination):
            hero_combination_output = ""
            opp_combination_output = ""
            if hero_combination[0] != opp_combination[0]: #Checks for winner
                if hero_combination[0] > opp_combination[0]:
                    results[0] = results[1]
                else:
                    results[0] = results[2]
            else:
                 if hero_combination[1] != opp_combination[1]:
                     if hero_combination[1] > opp_combination[1]:
                         results[0] = results[1]
                     else:
                         results[0] = results[2]
                 else:
                     if hero_combination[0] == 4 or hero_combination[0] == 8:
                         results[0] = results[3]
                     elif hero_combination[0] == 7:
                         if hero_combination[2] != opp_combination[2]:
                             if hero_combination[2] > opp_combination[2]:
                                 results[0] = results[1]
                             else:
                                 results[0] = results[2]
                         else:
                             results[0] = results[3]
                         hero_combination_output+=" - " + combinations_value[hero_combination[2]] + " Kicker"
                         opp_combination_output+=" - " + combinations_value[opp_combination[2]] + " Kicker"
                     elif hero_combination[0] == 6:
                         if hero_combination[2] != opp_combination[2]:
                             if hero_combination[2] > opp_combination[2]:
                                 results[0] = results[1]
                             else:
                                 results[0] = results[2]
                         else:
                             results[0] = results[3]
                     elif hero_combination[0] == 2:
                         if hero_combination[2] != opp_combination[2]:
                             if hero_combination[2] > opp_combination[2]:
                                 results[0] = results[1]
                             else:
                                 results[0] = results[2]
                         else:
                             if hero_combination[3] != opp_combination[3]:
                                 if hero_combination[3] > opp_combination[3]:
                                     results[0] = results[1]
                                 else:
                                     results[0] = results[2]
                             else:
                                results[0] = results[3]
                             hero_combination_output+=" - " + combinations_value[hero_combination[3]] + " Kicker"
                             opp_combination_output+=" - " + combinations_value[opp_combination[3]] + " Kicker"
                     elif hero_combination[0] == 3 or hero_combination[0] == 1:
                         if hero_combination[2] != opp_combination[2]:
                             if hero_combination[2] > opp_combination[2]:
                                 results[0] = results[1]
                             else:
                                 results[0] = results[2]
                             hero_combination_output+=" - " + combinations_value[hero_combination[2]] + " Kicker"
                             opp_combination_output+=" - " + combinations_value[opp_combination[2]] + " Kicker"
                         else:
                             if hero_combination[3] != opp_combination[3]:
                                 if hero_combination[3] > opp_combination[3]:
                                     results[0] = results[1]
                                 else:
                                     results[0] = results[2]
                             else:
                                 if hero_combination[0] == 3:
                                     results[0] = results[3]
                                 else:
                                    if hero_combination[4] != opp_combination[4]:
                                        if hero_combination[4] > opp_combination[4]:
                                            results[0] = results[1]
                                        else:
                                            results[0] = results[2]
                                    else:
                                        results[0] = results[3]
                             if hero_combination[0] == 3:
                                 hero_combination_output+=" - " + combinations_value[hero_combination[2]] + "+" + combinations_value[hero_combination[3]] + " Kicker"
                                 opp_combination_output+=" - " + combinations_value[opp_combination[2]] + "+" + combinations_value[opp_combination[3]] + " Kicker"
                             else:
                                 hero_combination_output+=" - " + combinations_value[hero_combination[2]] + "+" + combinations_value[hero_combination[3]] + "+" + combinations_value[hero_combination[4]] + " Kicker"
                                 opp_combination_output+=" - " + combinations_value[opp_combination[2]] + "+" + combinations_value[opp_combination[3]] + "+" + combinations_value[opp_combination[4]] + " Kicker"
                     elif hero_combination[0] == 0 or hero_combination[0] == 5:
                         if hero_combination[2] != opp_combination[2]:
                             if hero_combination[2] > opp_combination[2]:
                                 results[0] = results[1]
                             else:
                                 results[0] = results[2]
                             hero_combination_output+=" - " + combinations_value[hero_combination[2]] + " Kicker"
                             opp_combination_output+=" - " + combinations_value[opp_combination[2]] + " Kicker"
                         else:
                             if hero_combination[3] != opp_combination[3]:
                                 if hero_combination[3] > opp_combination[3]:
                                     results[0] = results[1]
                                 else:
                                     results[0] = results[2]
                                 hero_combination_output+=" - " + combinations_value[hero_combination[2]] + "+" + combinations_value[hero_combination[3]] + " Kicker"
                                 opp_combination_output+=" - " + combinations_value[opp_combination[2]] + "+" + combinations_value[opp_combination[3]] + " Kicker"
                             else:
                                 if hero_combination[4] != opp_combination[4]:
                                    if hero_combination[4] > opp_combination[4]:
                                        results[0] = results[1]
                                    else:
                                        results[0] = results[2]
                                    hero_combination_output+=" - " + combinations_value[hero_combination[2]] + "+" + combinations_value[hero_combination[3]] + "+" + combinations_value[hero_combination[4]] + " Kicker"
                                    opp_combination_output+=" - " + combinations_value[opp_combination[2]] + "+" + combinations_value[opp_combination[3]] + "+" + combinations_value[opp_combination[4]] + " Kicker"
                                 else:
                                     if hero_combination[5] != opp_combination[5]:
                                         if hero_combination[5] > opp_combination[5]:
                                             results[0] = results[1]
                                         else:
                                             results[0] = results[2]
                                     else:
                                         results[0] = results[3]
                                     hero_combination_output+=" - " + combinations_value[hero_combination[2]] + "+" + combinations_value[hero_combination[3]] + "+" + combinations_value[hero_combination[4]] + "+" + combinations_value[hero_combination[5]] + " Kicker"
                                     opp_combination_output+=" - " + combinations_value[opp_combination[2]] + "+" + combinations_value[opp_combination[3]] + "+" + combinations_value[opp_combination[4]] + "+" + combinations_value[opp_combination[5]] +  " Kicker"
            return hero_combination_output,opp_combination_output                         
        hero_combination = get_combination(hero_seven_cards_value,hero_seven_cards_suit)
        opp_combination = get_combination(opp_seven_cards_value,opp_seven_cards_suit)
        hero_combination_output+=write_combination(hero_combination)
        opp_combination_output+=write_combination(opp_combination)
        output = ['','']
        output[0],output[1] = compare_combinations(hero_combination,opp_combination)
        hero_combination_output+= output[0]
        opp_combination_output+= output[1]
        if results[0] != results[3]:
            result_output = results[0] + results[4] + results[5]
            if results[0] == results[1]:
                balance+=91
            else:
                balance-=100
        else:
            result_output = results[0] + results[5]
            balance-=4.5
        rake+=4.5
        global results_widget
        results_widget.config(text=hero_combination_output+"\n"+opp_combination_output+"\n"+result_output,fg="blue")
        global Push_widget,Fold_widget,Next_widget
        Push_widget.destroy()
        Fold_widget.destroy()
        def next_hand(event):
            game.unbind("<Key>")
            global Next_widget
            Next_widget.destroy()
            Next_widget = Button(game,text="NEXT\nHAND",fg="red")
            global Push_widget,Fold_widget
            Push_widget = Button(game,text="PUSH",fg="red")
            Fold_widget = Button(game,text="FOLD",fg="red")
            Push_widget.bind("<Button-1>",gamble)
            Fold_widget.bind("<Button-1>",fold)
            Push_widget.grid(row=0,column=2,stick=S)
            Fold_widget.grid(row=0,column=4,stick=S)
            game.bind("<Key>",keys)
            global results_widget
            results_widget.config(text="")
            global info
            info.config(text="Hand #"+str(hand_counter)+" Bankroll: "+str(balance)+"$"+" Rake: "+str(rake.__round__(2))+"$",fg="blue")
            get_hand()
        Next_widget = Button(game,text="NEXT\nHAND",fg="red")
        Next_widget.bind("<Button-1>",next_hand) 
        Next_widget.grid(row=0,column=2,stick=S)
        game.unbind("<Key>")
        def key(event):
            if event.char == " ":
                next_hand(event)
        game.bind("<Key>",key)        
        hand_counter+=1
def fold(event):
        global balance,hand_counter,rake
        balance-=((hand_counter%2)+1)*5
        rake+=((hand_counter%2)+1)*5*0.045
        hand_counter+=1
        global info
        info.config(text="Hand #"+str(hand_counter)+" Bankroll: "+str(balance)+"$"+" Rake: "+str(rake.__round__(2))+"$",fg="blue")
        global position_widget
        position_widget.config(text=position[hand_counter%2],fg="blue")
        get_hand()
def keys(event):
    if event.char == " ":
        fold(event)
    if event.char == "x":
        gamble(event)
results_widget = Label()
results_widget.place(x=175,y=250)
Push_widget = Button(game,text="PUSH",fg="red")
Push_widget.bind("<Button-1>",gamble)
Fold_widget = Button(game,text="FOLD",fg="red")
Fold_widget.bind("<Button-1>",fold)
game.bind("<Key>",keys)
Next_widget = Button(game,text="NEXT\nHAND",fg="red")
Push_widget.grid(row=0,column=2,stick=S)
Fold_widget.grid(row=0,column=4,stick=S)
HeroHandLeft = Label(image=hero_left_card_widget)
HeroHandRight = Label(image=hero_right_card_widget)
back = PhotoImage(file="deck/"+"back.gif")
BoardFlopLeft = Label(image=back)
BoardFlopCenter = Label(image=back)
BoardFlopRight = Label(image=back)
BoardTurn = Label(image=back)
BoardRiver = Label(image=back)
OppHandLeft = Label(image=back)
OppHandRight = Label(image=back)
HeroHandLeft.grid(row=0,column=0)
HeroHandRight.grid(row=0,column=1)
BoardFlopLeft.grid(row=1,column=0)
BoardFlopCenter.grid(row=1,column=1)
BoardFlopRight.grid(row=1,column=2)
BoardTurn.grid(row=1,column=3)
BoardRiver.grid(row=1,column=4)
OppHandLeft.grid(row=2,column=0)
OppHandRight.grid(row=2,column=1)
game.mainloop()
