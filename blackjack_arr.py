def Blackjack_arr(strArr):

    blackjack_values = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,\
         'nine':9, 'ten':10, 'jack':10, 'queen':10, 'king':10, 'ace':11}

    positioning = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8,\
         'nine':9, 'ten':10, 'jack':11, 'queen':12, 'king':13, 'ace':1}


    score = 0
    highest_card_val = 0
    highest_card = ""

    for card in strArr:
        score += blackjack_values[card]
        # till program does not know if value is above 21,
        # let's king be highest card, not ace
        if positioning[card] > highest_card_val:
            highest_card_val = positioning[card]
            highest_card = card

    aux = False
    if 'ace' in strArr:
        if score > 21:    
            aux = True
        else: # if sum is under 21 or equal, and ace is in cards it becomes highest
            highest_card = 'ace'    

    if aux == True:
        score -= 10

    if score > 21:
        return "above " + highest_card
    elif score == 21:
        return "blackjack " + highest_card
    else:
        return "below " + highest_card        