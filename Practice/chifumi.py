import random
chifumi_list = ['stone ', 'chisel', 'paper ']
results = {
    'virtual_player_choice': ' none ',
    'human_player_choice': ' none ',
    'winner': '      null      ', 
    'loser': '      null     ',
    'game_winner': '      null      ',
    'virtual_player_score' : 0,
    'human_player_score' : 0
}

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
    import random
    try:
        print("Please, select an element in the following list by its number:","1. Stone", "2. Chisel", "3. Paper", sep = "\n")
        human_choice = int(input("Make your choice : "))
        assert human_choice in range(1, 4)
        return human_choice
    except (ValueError, TypeError, AssertionError): 
        print("Invalide input. Try again.")
        human_choice = human_player_choice()
        return human_choice

def compare_players_choices( virtual_player, human_player):
    """
    Compare the players choices and give results.
    """
    rules = [[0, 1], [1, 2], [2, 0]]
    for rule in rules:
        if virtual_player in rule and human_player in rule and virtual_player != human_player:
            if virtual_player == rule[0]:
                results['virtual_player_score'] += 1
                iterator, update = 0, [chifumi_list[virtual_player], chifumi_list[human_player], ' Virtual player ', '  Human player  ', f"{'  Human player  ' if results['human_player_score'] > results['virtual_player_score'] else ('      null      ' if results['human_player_score'] == results['virtual_player_score'] else ' Virtual player ')}", results['virtual_player_score'], results['human_player_score']]
                for key in results.keys():
                    results[key] = update[iterator]
                    iterator += 1
            else:
                results['human_player_score'] += 1
                iterator, update = 0, [chifumi_list[virtual_player], chifumi_list[human_player], '  Human player  ', ' Virtual player ', f"{'  Human player  ' if results['human_player_score'] > results['virtual_player_score'] else ('      null      ' if results['human_player_score'] == results['virtual_player_score'] else ' Virtual player ')}", results['virtual_player_score'], results['human_player_score']]
                for key in results.keys():
                    results[key] = update[iterator]
                    iterator += 1
            break
        elif virtual_player == human_player:
            results['virtual_player_choice'] = chifumi_list[virtual_player]
            results['human_player_choice'] = chifumi_list[human_player]
            results['winner'], results['loser'] = '      null      ', '      null     '
            results['game_winner'] = '  Human player  ' if results['human_player_score'] > results['virtual_player_score'] else ('      null      ' if results['human_player_score'] == results['virtual_player_score'] else ' Virtual player ')

def present_results():
    """
    Custom results dictionary for presentation.
    """
    virtual_player_choice_len, human_player_choice_len = 16 - len(results['virtual_player_choice']), 14 - len(results['human_player_choice'])
    virtual_player_score_len, human_player_score_len = 16 - len(str(results['virtual_player_score'])), 14 - len(str(results['human_player_score']))
    line_ = '#'*67
    line_0 = "||" + ' '*26 + "Score board" + ' '*26 + '||'
    line_1 = f"{'#'*16}" + f"| {'#'*14} | " + f"{'#'*12} | " + f"{'#'*14} ||"
    line_2 = "||   Players    " + "| Virtual Player | " +  "Human Player | " + "    Winner     ||"
    line_3 = "|| Round result " + '|' + ' '*(int(virtual_player_choice_len/2)) + f"{results['virtual_player_choice']}" + ' '*(int(virtual_player_choice_len/2)) + '|' + ' '*(int(human_player_choice_len/2)) + f"{results['human_player_choice']}" + ' '*(int(human_player_choice_len/2)) + '|' + f"{results['winner']}" + "||"
    line_4, virtual_score, human_score = "", '', ''
    if virtual_player_score_len == 15:
        virtual_score = '0' + str(results['virtual_player_score'])
    else:
        virtual_score = results['virtual_player_score']
    if human_player_score_len == 13:
        human_score = '0' + str(results['human_player_score'])
    else:
        human_score = results['human_player_score']
    line_4 = "|| Total Score  " + '|' + ' '*(int(virtual_player_score_len/2)) + f"{virtual_score}" + ' '*(int(virtual_player_score_len/2)) + '|' + ' '*(int(human_player_score_len/2)) + f"{human_score}" + ' '*(int(human_player_score_len/2)) + '|' + f"{results['game_winner']}" + "||"
    print(line_, line_0, line_1, line_2, line_1, line_3, line_1, line_4, line_, sep = "\n")

def main():
    """
    Manage the chifumi game.
    """
    game = 'y'
    print('############################', "Welcome to the ChiFuMi game!", '############################\n', sep = "\n")
    present_results()
    while game in ['y', 'yes', 'o', 'oui']:
        virtual_player = virtual_player_choice()
        human_player = human_player_choice()
        compare_players_choices(virtual_player = virtual_player, human_player = human_player - 1)
        present_results()
        game = input("\nDo you want to continue the game ? (Yes/No) ").lower()
        if game not in ['y', 'yes', 'o', 'oui']:
            print('\n##############################', "Thanks for this game. See you!", '##############################', sep = "\n")
            break

# if __name__ == "main":
#     main()

main()
