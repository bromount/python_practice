def is_palind(word):
    i=0
    j=len(word)-1
    print j
    while i<j:
        print i
        print j
        if word[i]!=word[j]:
            print "not palindrome"
            return False
        i=i+1
        j=j-1
    print "its a palindrome"
    return True

cust_input = raw_input("please enter a string : ")

is_palind(cust_input)