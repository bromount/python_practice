def print_numbers():
    i = 0
    print "Enter a number "
    numb = int(raw_input())
    if numb <0:
        print "please enter value greater than ZERO, try again"
        print_numbers()
    else:
        while i <= numb:
            print "number is : ",i
            i = i +1

print_numbers()