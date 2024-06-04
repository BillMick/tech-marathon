def random_number()->str:
    """
    Generator of a three digits number between 000 and 999.
    """
    import random
    magic_number = str(random.randint(0, 999))
    magic_number = reformat_number(magic_number)
    return magic_number

def reformat_number(number:str)->str:
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
    user entry if len(user_entry != 3)"""
    try:
        user_entry = int(input("Guess the number: "))
        user_entry = str(user_entry)
        assert 0 < len(user_entry) < 4
        user_entry = reformat_number(user_entry)
        return user_entry
    except (TypeError, ValueError, AssertionError):
        print("Invalide input. Try again.")
        user_entry = number_guessing(magic_number)
        return user_entry
        

number = random_number()
print(f"{number}", f"{type(number)}")
guess = number_guessing(number)
print(f"{guess}", f"{type(guess)}")