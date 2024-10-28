# Functions Practice, Amir Norflett, v0.0

import random 

def helloWorldMulti(): # FUNCTION SIGNATURE 
    """This function will output Hello, World! in a language the user choose.""" # DOCSTRING \
    # print a list of languages to the screen, at least three but no more than five.
    print("""
          Welcome to the Hello, World! Translator 
          The following languages are available 
          [E]nglish
          [S]panish
          [F]rench
          [G]erman
          [T]agalog
          """)
    
    # allow the user to select (input) a choice for the language 
    language = input("What language do you want?\n Please type the first letter of the language you want.\n").lower()

    # print "Hello, World!" to the screen in that language 
    print("The languages avaliable English, Spanish, French.\n")
helloWorldMulti()



























