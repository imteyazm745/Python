verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
"""
What is the length of the string variable verse?
What is the index of the first occurrence of the word 'and' in verse?
What is the index of the last occurrence of the word 'you' in verse?
What is the count of occurrences of the word 'you' in the verse? """

verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)
print(len(verse)) #362
# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!
print(verse.count("you")) #8
print((verse.find("and"))) #65
print((verse.rfind("you"))) #186

# solution 2
verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse, "\n")

print("Verse has a length of {} characters.".format(len(verse))) # Verse has a length of 362 characters.
print("The first occurence of the word 'and' occurs at the {}th index.".format(verse.find('and'))) # The first occurence of the word 'and' occurs at the 65th index.
print("The last occurence of the word 'you' occurs at the {}th index.".format(verse.rfind('you'))) # The last occurence of the word 'you' occurs at the 186th index.
print("The word 'you' occurs {} times in the verse.".format(verse.count('you'))) # The word 'you' occurs 8 times in the verse.
