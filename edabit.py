def stutter(word):

    word = word.lower()
    return word[:2]+"..."+word[:2]+"..."+word


print(stutter("Amin"))
