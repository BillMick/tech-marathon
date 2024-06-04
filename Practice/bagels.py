def random_number()->str:
    """
    Generator of a three digits number between 000 and 999.
    """
    import random
    magic_number = random.randint(0, 999)
    magic_number = reformat_number(magic_number)
    return magic_number

def reformat_number(number:int)->str:
    """
    As we need a three digits number, zeros are completed to the left of
    the given number if len(number) != 3.
    """
    number = str(number)
    match len(number):
        case 1:
            number = '00' + number
        case 2:
            number = '0' + number
    return number

def number_guessing(magic_number:str):
    """
    Get the user entry. This must be a number of at least one digit.
    As we need a three digits number, zeros are completed to the left of
    user entry if len(user_entry) != 3."""
    try:
        user_entry = int(input("Guess the number: "))
        user_entry = reformat_number(user_entry)
        assert 0 < len(user_entry) < 4
        return user_entry
    except (TypeError, ValueError, AssertionError):
        print("Invalide input. Try again.")
        user_entry = number_guessing(magic_number)
        return user_entry

def comparison(magic_number:str, user_entry:str)->str:
    pico, fermi = [], []
    for i in range(0, len(user_entry)):
        # if user_entry[i] in magic_number: pico.append(True); pico.append(False)
        # if user_entry[i] == magic_number[i]: fermi.append(True); fermi.append(False)
        if user_entry[i] in magic_number: 
            pico.append(True)
        else:
            pico.append(False)
        if user_entry[i] == magic_number[i]: 
            fermi.append(True)
        else:
            fermi.append(False)
    if True not in pico and True not in fermi:
        return 'Bagels'
    elif fermi == [True, True, True]:
        return 'Correct'
    elif True in fermi:
        return 'Fermi'
    elif True in pico:
        return 'Pico'

def main():
    print("""
    ###########################################################################
    ### Bagels, a deductive logic game.                                     ###
    ###     By Al Sweigart al@inventwithpython.com                          ### 
    ### I am thinking of a 3-digit number. Try to guess what it is.         ### 
    ### Here are some clues:                                                ### 
    ###     When I say:     That means:                                     ### 
    ###     Pico            One digit is correct but in the wrong position. ### 
    ###     Fermi           One digit is correct and in the right position. ### 
    ###     Bagels          No digit is correct.                            ### 
    ###     Correct         You find the number.                            ### 
    ### I have thought up a number.                                         ### 
    ### You have 10 guesses to get it.                                      ### 
    ########################################################################### 
    """)
    number_of_round = 10
    found = False
    guessed_numbers_list, comparison_results_list = [], []
    while True:
        magic_number = random_number()
        for i in range(0, number_of_round):
            print(f'Guess #{i + 1}:')
            guessed_number = number_guessing(magic_number)
            guessed_numbers_list.append(guessed_number)
            comparison_result = comparison(magic_number, guessed_number)
            comparison_results_list.append(comparison_result)
            print(comparison_result)
            if comparison_result == 'Correct':
                print('Congrats !!! You have found the number.')
                break
            elif i == 9:
                print('Number not found...', f'It was {magic_number}.')
        while 1:
            game = input("\nDo you want to play again ? (Yes/No) ").lower()        
            if game in ['n', 'no', 'non']:
                print('\n##############################', "Thanks for this game. See you!", '##############################', sep = "\n")
                exit(0)
            elif game in ['y', 'yes', 'o', 'oui']:
                break


if __name__ == '__main__':
    main()

# number = random_number()
# print(f"{number}", f"{type(number)}")
# guess = number_guessing(number)
# print(f"{guess}", f"{type(guess)}")
# compare = comparison(number, guess)
# print(f"{compare}", f"{type(compare)}")