def clinic():
    print "You are into a Clinic"
    print "Tell us where you want to go Right/Left?"
    direction = raw_input("please enter right/left : ").lower()

    if direction == "left" or direction == "l":
        print "You chose the left"
    elif direction == "right" or direction == "r":
        print "you choose the right"
    else:
        print "You didn't choose the correct direction, please try again"

        clinic()


clinic()