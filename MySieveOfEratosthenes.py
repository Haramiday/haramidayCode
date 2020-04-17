#Sieve of Eratosthenes
def multiple(count):
    '''
    This function takes in a limit and returns the multiples of numbers upto
    the limit. it returns as list
    '''
    list_multiple = []  #list for the multiples
    m = 2
    while m < count:  
        for i in range(2,count):
            product = i*m
            if product <= count:
                list_multiple = list_multiple + [product]
        m = m + 1
    return list_multiple

  
def sieve_of_eratos(limiting_num):
    '''
    This fuction takes in a limiting number as input and returns a list of
    prime numbers less than it
    '''
    #list for numbers from 2 to less of limiting num
    list_of_numbers = []
    #loop for adding the numbers
    for i in range(2,limiting_num ):
        list_of_numbers = list_of_numbers + [i]
    
    #loops through the list of multiples
    for i in multiple(limiting_num): 
        #loops through the list of numbers from 2 to less of limiting num
        for j in list_of_numbers:
            if i == j : #checks if elemt in multiple and numbers are the same
                list_of_numbers[list_of_numbers.index(j)] = 0
    
    #seiving the prime numbers
    prime_num=[]
    for a in list_of_numbers:
        if a != 0:
            prime_num = prime_num + [a]
    return prime_num
        

print(sieve_of_eratos(100))
