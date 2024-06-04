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
        

number = random_number()
print(f"{number}", f"{type(number)}")