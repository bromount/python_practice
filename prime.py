print range(2, 10)
def find_prime(start_range,end_range):
    for n in range(start_range, end_range):
        for x in range(2, n):
            if n % x == 0:
                print "Value ", n, 'is not a prime because it equals to ', x, '*', n / x
                break
            else:
                print "Value ", n, "is a prime number"

def quest():
    print "please provide a start range(greater than '2') for prime number : "
    first_num = int(raw_input())
    print "please provide a end range for prime number : "
    last_num = int(raw_input())
    if first_num < 2:
        print "please enter value greater than 2, try again"
        quest()
    else:
        find_prime(first_num,last_num)

quest()