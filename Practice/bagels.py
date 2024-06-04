def random_number()->str:
    """
    Generator of a three digits number between 000 and 999.
    """
    import random
    magic_number = str(random.randint(0, 999))
    return magic_number

        

number = random_number()
print(f"{number}", f"{type(number)}")