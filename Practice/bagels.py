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

def comparison(magic_number:str, user_entry:str)->bool:
    pico, fermi = [], []
    for i in range(0, len(user_entry)):
        if user_entry[i] in magic_number: pico.append(True); pico.append(False)
        if user_entry[i] == magic_number[i]: fermi.append(True); fermi.append(False)
    if True not in pico and True not in fermi:
        return 'Bagels'
    elif True in fermi:
        return 'Fermi'
    elif True in pico:
        return 'Pico'


number = random_number()
print(f"{number}", f"{type(number)}")
guess = number_guessing(number)
print(f"{guess}", f"{type(guess)}")
compare = comparison(number, guess)
print(f"{compare}", f"{type(compare)}")