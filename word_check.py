import enchant
chck=enchant.Dict("en_US")

if chck.check("test") is True:
    print "test success"
pig_lat = 'ay'

def word_check():
    cust_word=raw_input("please enter a english word : ")
    if chck.check(cust_word) is False:
        print "please enter a proper English word like the following : "
        sugg = str(chck.suggest(cust_word))
        print sugg
        word_check()
    elif len(cust_word) > 0 and cust_word.isalpha():
        print "test"
        word = cust_word.lower()
        first = word[0]
        if first ==('a'or'e'or'i'or'o'or'u'):
            print "vowels"
            newword = word + pig_lat
            print newword
        else:
            newword = word[1:] + first + pig_lat
            print newword
    else:
        print "its empty"

word_check()