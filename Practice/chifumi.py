chifumi = {
    1 : "stone",
    2 : "chisel",
    3 : "paper",
}

import random
chifumi_list = ["stone", "chisel", "paper"]
        
def virtual_player_choice():
    """
    Return randomly a choice between the chifumi_list = ["stone", "chisel", "paper"].
    """
    # random.choices(chifumi_list, weights = [1, 1, 1], k = 1)
    return chifumi_list.index(random.choice(chifumi_list))

def human_player_choice():
    """
    Get the human player choice and ensure that it respects the value, type and assertion
    constraints.
    """
    try:
        human_choice = 0
        print("Please, select an element in the following list by its number:","1. Stone", "2. Chisel", "3. Paper", sep = "\n")
        human_choice = int(input("Make your choice : "))
        assert human_choice in range(1, 4)
        return human_choice - 1
    except (ValueError, TypeError, AssertionError): 
        print("Invalide input. Try again.")
        human_player_choice()
        return human_choice - 1

def compare_players_choices(virtual_player, human_player):
    """
    Compare the players choices and give result.
    """
    rules = [[0, 1], [1, 2], [2, 0]]
    for rule in rules:
        if virtual_player in rule and human_player in rule:
            if virtual_player == rule[0]:
                return {'winner': 'Virtual player', 'loser': 'Human player'}
            else:
                return {'winner': 'Human player', 'loser': 'Virtual player'}
            print(locals().keys())

print(compare_players_choices(1, 2))
    