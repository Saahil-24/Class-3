homework_time=int(input("Please type the amount of tiume it takes to do your homework."))
if homework_time>59:
    print("Start homework now. That is a long homework session.")
else:
    print("Finish homework quickly. That is a short homework session.")
answer=int(input("Is there free time after homework?(yes/no)"))
if answer=="yes":
    hobby=int(input("Pick a hobby."))
else:
    print()