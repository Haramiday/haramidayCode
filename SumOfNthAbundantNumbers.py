def abundant(num):
    '''
    This function  ​takes in a number as its input  ​and ​
    returns a Boolean value indicating whether
    the number is abundant or not
    '''
    li = [] #holds the proper divisors
    add = 0
    for i in range(1,num): #loop through 1 to the number
        if num%i==0: #checks for the proper divisors and sttores in a list
            li = li + [i]
    
    for i in li:#loops through the list to add the proper divisors
        add = add + i

    #abundant condition
    if add > num:
        return True
    else:
        return False



def sum_abundant(n):
    '''
    This function takes in the value of n and
    returns the sum of the first n adundant
    numbers
    '''
    li = [] #holds the abundant numbers
    i = 1
    s_um = 0
    while i > 0:#loops through positive numbers to get the abundant numbers
        if abundant(i):
            li = li + [i]
        if len(li)==n:
            break #stops at the n abundant numbers
        i = i + 1

    for i in li:#loops through the list for addition
        s_um = s_um + i

    return 'The sum of the first '+str(n)+ ' abundant numbers is ' +str(s_um)
print(sum_abundant(100))
