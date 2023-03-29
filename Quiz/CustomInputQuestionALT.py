print("whats 9+10?")
txt = input("your answer: ")
yes = "19"
stupid = "21"
print("you answered: " + txt)
if txt == stupid:
    print("you stupid")
if txt != stupid:
    pass
elif txt == yes:
    print("you're correct!")
elif txt != yes or txt != stupid:
    print("you're wrong!")
    #REMINDER!: i need to fix this later so it doesnt input 2 messages at once when entering the requirments for stupid