###############################################################################
#  Program Name   : ex8.py
#  Author         : Amro
#  Task           : This program keeps asking the user to enter words until they type 'exit'
###############################################################################

word = ""
while word.lower() != "exit":
    word = input("Enter a word (type 'exit' to quit): ")

print("Goodbye!")
