try:
    score = input("What is your score? ")
    score = float(score)
except:
    print("not a number")
    quit()
if score<0:
    print("outside range")
elif score>1:
    print("outside range")
else:
    if score>=0.9:
        print("A")
    elif score>=0.8:
        print("B")
    elif score>=0.7:
        print("C")
    elif score>=0.6:
        print("D")
    elif score<0.6:
        print("F")
