""" # Importation """
# import printNumbers

""" # Renaming """
import printNumbers as PN

""" # import a specific fonction """
# from printNumbers import printBackwards 

""" import a specific fonction and rename """
# from printNumbers import printBackwards as pb

""" import all the names that a module defines there is another variant for importing. 
This imports all names except those beginning with an underscore (_). 
But this is not ideal practice as this introduces an unknown set of names into the interpreter. """
# from printNumbers import * 

PN.printForward(10)
print("#"*15)
PN.printBackwards(5)