
def sum_of_divisor(num):
    '''
    This function takes in a number and
    return the sum of its proper divisors
    '''
    li = []#holds the proper divisors
    summ = 0
    #loop to find the proper divisors and add them to the list 'li'
    for i in range(1,num):
        if num%i==0:
            li = li + [i]

    #loop through the list to get the sum
    for i in li:
        summ = summ + i

    return(summ)



def amicable(num1,num2):
    '''
    This function  ​that ​takes in the two numbers as input parameters​ and
    ​returns a Boolean​ indicating whether they are amicable or not.​ 
    '''

    #checks if the sum of proper divisor of num1 is equal to num2 and otherwise
    if sum_of_divisor(num1)==num2 and sum_of_divisor(num2)==num1:
        return True
    else:
        return False

print(amicable(220,284))

