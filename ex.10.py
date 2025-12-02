###############################################################################
#  Program Name   : ex10.py
#  Author         : Amro
#  Task           : (Write a program that asks for 5 test scores, stores them in a list, and prints the average)
###############################################################################

test_scores = []

print("Enter 5 test scores:")
for i in range(5):
    score = float(input(f"Score {i+1}: "))
    test_scores.append(score)

average = sum(test_scores) / 5
print(f"\nAverage score: {average}")